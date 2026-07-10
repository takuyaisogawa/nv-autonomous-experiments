#!/usr/bin/env python3
"""Run a batch-context version of the main pODMR benchmark inputs.

The main pODMR benchmark gave each case an isolated workspace containing
raw_export.json, raw_readouts.png, and sequence.xml.  This runner preserves that
file-based input style, but places all cases in one workspace and asks the model
to classify the full unlabeled batch.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

CONDITION_FILES = {
    "context_0": ROOT / "prompts" / "context_0_protocol_only.md",
    "context_A": ROOT / "prompts" / "context_A_domain_facts.md",
    "context_B": ROOT / "prompts" / "context_B_model_first.md",
}

FIELDNAMES = [
    "context_id",
    "replicate",
    "case_id",
    "timestamp",
    "gold_label",
    "prediction",
    "correct",
    "outcome",
    "short_reason",
    "analysis_note_path",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument(
        "--reasoning-effort",
        choices=("low", "medium", "high", "xhigh"),
        required=True,
    )
    parser.add_argument(
        "--case-index",
        type=Path,
        default=ROOT / "inputs" / "case_index.csv",
    )
    parser.add_argument("--replicates", type=int, default=3)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--result-dir", type=Path, required=True)
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_labels() -> dict[str, str]:
    return {
        row["case_id"]: row["resonance_label"]
        for row in read_rows(ROOT / "labels" / "gold_labels.csv")
    }


def compact_sequence_text(sequence: str) -> str:
    return sequence.replace("\r\n", "\n").replace("\r", "\n")


def link_or_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def prepare_workspace(workspace: Path, case_rows: list[dict[str, str]]) -> None:
    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "outputs").mkdir(exist_ok=True)
    for row in case_rows:
        case_dir = workspace / "cases" / row["case_id"] / "inputs"
        case_dir.mkdir(parents=True, exist_ok=True)
        raw_src = ROOT / "inputs" / row["raw_export_path"]
        img_src = ROOT / "inputs" / row["diagnostic_figure_path"]
        link_or_copy(raw_src, case_dir / "raw_export.json")
        link_or_copy(img_src, case_dir / "raw_readouts.png")
        export = json.loads(raw_src.read_text(encoding="utf-8"))
        sequence = compact_sequence_text(export["scan"].get("Sequence", ""))
        (case_dir / "sequence.xml").write_text(sequence, encoding="utf-8")
        metadata = {
            "case_id": row["case_id"],
            "timestamp": row["timestamp"],
            "sequence_name": row.get("sequence_name"),
            "actual_begin_hz": row.get("actual_begin_hz"),
            "actual_end_hz": row.get("actual_end_hz"),
            "actual_points": row.get("actual_points"),
            "actual_step_hz": row.get("actual_step_hz"),
            "actual_num_avg": row.get("actual_num_avg"),
        }
        (case_dir / "case_metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
        )


def condition_prompt(context_id: str) -> str:
    prompt = CONDITION_FILES[context_id].read_text(encoding="utf-8")
    return prompt.replace(
        "Do not use labels, previous outputs, sibling cases, or external context.",
        (
            "Do not use labels, previous outputs, or external context. "
            "The other unlabeled cases in this batch are provided intentionally "
            "and may be used for comparison."
        ),
    )


def batch_prompt(context_id: str, case_rows: list[dict[str, str]]) -> str:
    case_lines = [
        f"- {row['case_id']}: cases/{row['case_id']}/inputs/raw_export.json, "
        f"cases/{row['case_id']}/inputs/raw_readouts.png, "
        f"cases/{row['case_id']}/inputs/sequence.xml"
        for row in case_rows
    ]
    case_ids = ", ".join(row["case_id"] for row in case_rows)
    return (
        "You are evaluating a batch of pODMR benchmark cases.  This is the "
        "batch-context version of the main file-based benchmark.  Each case has "
        "the same input file types used in the main per-case benchmark.  Do not "
        "use web search, labels, previous outputs, or external context.  Use "
        "only the prompt and the files in this isolated workspace.\n\n"
        "Classify every case independently, but you may compare cases within "
        "this provided unlabeled batch to calibrate the scale of features.  "
        "Return exactly one prediction for every required case_id.  The final "
        "CSV is invalid if any required case_id is missing.\n\n"
        f"{condition_prompt(context_id)}\n\n"
        "Required case IDs:\n"
        f"{case_ids}\n\n"
        "Files in this isolated workspace:\n"
        + "\n".join(case_lines)
        + "\n\n"
        "Write exactly one CSV file to outputs/batch_predictions.csv with these "
        "columns:\n"
        "case_id,prediction,short_reason\n\n"
        "prediction must be exactly resonance_present or resonance_absent.  "
        "short_reason should be a short phrase, not a full analysis note.  Do "
        "not include labels, scoring, post-hoc accuracy, or extra columns.  "
        "Use ASCII-only text in the CSV.  After writing the CSV, reply with a "
        "brief completion message only."
    )


def parse_csv_predictions(text: str, case_ids: set[str]) -> dict[str, dict[str, str]]:
    predictions: dict[str, dict[str, str]] = {}
    lines = [line for line in text.splitlines() if line.strip()]
    start = 0
    for i, line in enumerate(lines):
        if re.match(r"\s*case_id\s*,\s*prediction\b", line):
            start = i
            break
    csv_text = "\n".join(lines[start:])
    try:
        reader = csv.DictReader(csv_text.splitlines())
        for row in reader:
            case_id = (row.get("case_id") or "").strip()
            pred = (row.get("prediction") or "").strip()
            if case_id in case_ids and pred in {"resonance_present", "resonance_absent"}:
                predictions[case_id] = {
                    "prediction": pred,
                    "short_reason": (row.get("short_reason") or "").strip(),
                }
    except csv.Error:
        pass
    if len(predictions) < len(case_ids):
        for line in lines:
            match = re.search(
                r"\b(case_\d{3})\b[,\s:|\t]+(resonance_(?:present|absent))\b(?:[,\s:|\t]+(.+))?",
                line,
            )
            if match and match.group(1) in case_ids:
                predictions[match.group(1)] = {
                    "prediction": match.group(2),
                    "short_reason": (match.group(3) or "").strip(),
                }
    return predictions


def outcome(gold: str, prediction: str) -> tuple[str, str]:
    if prediction == "":
        return "0", "PARSE_FAILED"
    if gold == "present" and prediction == "resonance_present":
        return "1", "TP"
    if gold == "absent" and prediction == "resonance_absent":
        return "1", "TN"
    if gold == "absent" and prediction == "resonance_present":
        return "0", "FP"
    if gold == "present" and prediction == "resonance_absent":
        return "0", "FN"
    return "0", "UNKNOWN"


def existing_ids(raw_path: Path) -> set[str]:
    if not raw_path.exists():
        return set()
    ids: set[str] = set()
    with raw_path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                custom_id = record.get("custom_id")
                if (
                    isinstance(custom_id, str)
                    and record.get("returncode") == 0
                    and record.get("num_predictions") == record.get("num_cases")
                ):
                    ids.add(custom_id)
    return ids


def run_one(
    args: argparse.Namespace,
    context_id: str,
    replicate: int,
    case_rows: list[dict[str, str]],
    labels: dict[str, str],
) -> dict[str, Any]:
    workspace = args.result_dir / "workspaces" / context_id / f"replicate_{replicate}"
    prepare_workspace(workspace, case_rows)
    prompt = batch_prompt(context_id, case_rows)
    last_message = workspace / "outputs" / "last_message.txt"
    predictions_file = workspace / "outputs" / "batch_predictions.csv"
    if predictions_file.exists():
        predictions_file.unlink()
    cmd = [
        args.codex_bin,
        "exec",
        "--config",
        f'model_reasoning_effort="{args.reasoning_effort}"',
        "--ephemeral",
        "--ignore-rules",
        "--sandbox",
        "workspace-write",
        "--model",
        args.model,
        "--cd",
        str(workspace),
        "--output-last-message",
        str(last_message),
        "-",
    ]
    proc = subprocess.run(
        cmd,
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=args.timeout,
    )
    response = last_message.read_text(encoding="utf-8") if last_message.exists() else ""
    csv_text = predictions_file.read_text(encoding="utf-8-sig") if predictions_file.exists() else response
    case_ids = {row["case_id"] for row in case_rows}
    predictions = parse_csv_predictions(csv_text, case_ids)
    rows = []
    for row in case_rows:
        case_id = row["case_id"]
        parsed = predictions.get(case_id, {})
        prediction = parsed.get("prediction", "")
        correct, result = outcome(labels[case_id], prediction)
        rows.append(
            {
                "context_id": context_id,
                "replicate": replicate,
                "case_id": case_id,
                "timestamp": row["timestamp"],
                "gold_label": labels[case_id],
                "prediction": prediction or "parse_failed",
                "correct": correct,
                "outcome": result,
                "short_reason": parsed.get("short_reason", ""),
                "analysis_note_path": (
                    f"workspaces/{context_id}/replicate_{replicate}/outputs/batch_predictions.csv"
                ),
            }
        )
    return {
        "custom_id": f"{context_id}__rep{replicate}",
        "context_id": context_id,
        "replicate": replicate,
        "num_cases": len(case_rows),
        "num_predictions": len(predictions),
        "returncode": proc.returncode,
        "response": response.strip(),
        "rows": rows,
        "stdout_tail": proc.stdout[-2000:],
        "stderr_tail": proc.stderr[-2000:],
    }


def summarize(rows: list[dict[str, Any]]) -> str:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((str(row["context_id"]), str(row["replicate"])), []).append(row)
    lines = [
        "# Batch-context main-input pODMR benchmark",
        "",
        "All cases were provided in one isolated workspace for each condition and replicate.",
        "Each case had raw_export.json, raw_readouts.png, and sequence.xml, matching",
        "the file types used in the main per-case benchmark.",
        "",
        "| Condition | Replicate | TP | TN | FP | FN | Parse failed | Accuracy |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for (context_id, replicate), items in sorted(grouped.items()):
        counts = {key: 0 for key in ("TP", "TN", "FP", "FN", "PARSE_FAILED")}
        for item in items:
            counts[item["outcome"]] = counts.get(item["outcome"], 0) + 1
        correct = counts["TP"] + counts["TN"]
        n = len(items)
        acc = 100.0 * correct / n if n else 0.0
        lines.append(
            f"| {context_id} | {replicate} | {counts['TP']} | {counts['TN']} | "
            f"{counts['FP']} | {counts['FN']} | {counts['PARSE_FAILED']} | {acc:.1f}% |"
        )
    return "\n".join(lines) + "\n"


def write_outputs(result_dir: Path, raw_records: list[dict[str, Any]]) -> None:
    rows: list[dict[str, Any]] = []
    for record in raw_records:
        rows.extend(record["rows"])
    with (result_dir / "joined_predictions.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    (result_dir / "summary.md").write_text(summarize(rows), encoding="utf-8")


def read_raw_records(raw_path: Path) -> list[dict[str, Any]]:
    if not raw_path.exists():
        return []
    records: dict[str, dict[str, Any]] = {}
    with raw_path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                custom_id = record.get("custom_id")
                if isinstance(custom_id, str):
                    records[custom_id] = record
    return [records[key] for key in sorted(records)]


def main() -> None:
    args = parse_args()
    labels = load_labels()
    case_index = args.case_index if args.case_index.is_absolute() else ROOT / args.case_index
    case_rows = read_rows(case_index)
    if args.limit is not None:
        case_rows = case_rows[: args.limit]
    args.result_dir.mkdir(parents=True, exist_ok=True)
    raw_path = args.result_dir / "model_outputs.jsonl"
    done = set() if args.overwrite else existing_ids(raw_path)
    requests = [
        (context_id, replicate)
        for context_id in CONDITION_FILES
        for replicate in range(1, args.replicates + 1)
    ]
    pending = [
        (context_id, replicate)
        for context_id, replicate in requests
        if f"{context_id}__rep{replicate}" not in done
    ]
    print(
        f"Running {len(pending)} pending of {len(requests)} main-input batch "
        f"requests for {args.reasoning_effort}",
        flush=True,
    )
    mode = "w" if args.overwrite else "a"
    with raw_path.open(mode, encoding="utf-8") as f:
        for i, (context_id, replicate) in enumerate(pending, start=1):
            print(f"[{i}/{len(pending)}] {context_id} replicate {replicate}", flush=True)
            started = time.time()
            result = run_one(args, context_id, replicate, case_rows, labels)
            elapsed = time.time() - started
            result["elapsed_s"] = round(elapsed, 1)
            f.write(json.dumps(result, ensure_ascii=False) + "\n")
            f.flush()
            print(
                f"  returncode={result['returncode']} "
                f"predictions={result['num_predictions']}/{result['num_cases']} "
                f"elapsed={elapsed:.1f}s",
                flush=True,
            )
            if args.sleep:
                time.sleep(args.sleep)
    write_outputs(args.result_dir, read_raw_records(raw_path))


if __name__ == "__main__":
    main()
