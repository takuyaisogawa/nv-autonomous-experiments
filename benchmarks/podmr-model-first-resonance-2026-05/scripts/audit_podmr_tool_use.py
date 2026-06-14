#!/usr/bin/env python3
"""Audit shell and Python tool use in the original pODMR benchmark logs.

The original Codex CLI logs are local provenance records and are not included in
the public release.  This script reads those local logs when available and
writes sanitized derived CSV summaries.  It records whether each run used
PowerShell, any Python command, inline Python, JSON validation, or Python code
that appears to analyze the pODMR raw export.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RUNS = [
    {
        "effort": "low",
        "condition": "Sequence",
        "context": "context_0",
        "dir": "podmr_minimal_context_gpt55_low_20260519_096_context0_xml_only",
    },
    {
        "effort": "medium",
        "condition": "Sequence",
        "context": "context_0",
        "dir": "podmr_minimal_context_gpt55_medium_20260518_096_context0_xml_only",
    },
    {
        "effort": "high",
        "condition": "Sequence",
        "context": "context_0",
        "dir": "podmr_minimal_context_gpt55_high_20260519_096_context0_xml_only",
    },
    {
        "effort": "xhigh",
        "condition": "Sequence",
        "context": "context_0",
        "dir": "podmr_minimal_context_gpt55_xhigh_20260519_096_context0_xml_only",
    },
    {
        "effort": "low",
        "condition": "Facts",
        "context": "context_A",
        "dir": "podmr_minimal_context_gpt55_low_20260519_096_reduced_facts",
    },
    {
        "effort": "low",
        "condition": "Expected signal",
        "context": "context_B",
        "dir": "podmr_minimal_context_gpt55_low_20260519_096_reduced_facts",
    },
    {
        "effort": "medium",
        "condition": "Facts",
        "context": "context_A",
        "dir": "podmr_minimal_context_gpt55_medium_20260518_096_reduced_facts",
    },
    {
        "effort": "medium",
        "condition": "Expected signal",
        "context": "context_B",
        "dir": "podmr_minimal_context_gpt55_medium_20260518_096_reduced_facts",
    },
    {
        "effort": "high",
        "condition": "Facts",
        "context": "context_A",
        "dir": "podmr_minimal_context_gpt55_high_20260519_096_reduced_facts",
    },
    {
        "effort": "high",
        "condition": "Expected signal",
        "context": "context_B",
        "dir": "podmr_minimal_context_gpt55_high_20260519_096_reduced_facts",
    },
    {
        "effort": "xhigh",
        "condition": "Facts",
        "context": "context_A",
        "dir": "podmr_minimal_context_gpt55_xhigh_20260519_096_reduced_facts",
    },
    {
        "effort": "xhigh",
        "condition": "Expected signal",
        "context": "context_B",
        "dir": "podmr_minimal_context_gpt55_xhigh_20260519_096_reduced_facts",
    },
]

ANALYSIS_MARKERS = {
    "raw_export": "inputs/raw_export.json",
    "experiment_data": "ExperimentData",
    "readout": "readout",
    "ratio": "ratio",
    "contrast": "contrast",
    "rabi": "rabi",
    "lorentzian": "lorentzian",
    "gaussian": "gaussian",
    "line_shape": "line-shape",
    "sse": "sse",
    "numpy": "numpy",
    "np": "np.",
    "signal_reference": "signal/reference",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-root",
        type=Path,
        default=os.environ.get("PODMR_RAW_RUN_ROOT"),
        help=(
            "Local root containing original Codex CLI benchmark run logs. "
            "Can also be provided through PODMR_RAW_RUN_ROOT."
        ),
    )
    parser.add_argument(
        "--case-index",
        type=Path,
        default=ROOT / "inputs" / "case_index.csv",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "results",
    )
    args = parser.parse_args()
    if args.source_root is None:
        parser.error("provide --source-root or set PODMR_RAW_RUN_ROOT")
    return args


def read_case_index(path: Path) -> dict[str, str]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return {row["timestamp"]: row["case_id"] for row in csv.DictReader(f)}


def command_blocks(text: str) -> list[str]:
    """Return shell command blocks as printed by Codex CLI stderr logs."""
    lines = text.splitlines()
    blocks: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if 'powershell.exe" -Command' not in line:
            i += 1
            continue
        block = [line]
        i += 1
        while i < len(lines):
            block.append(lines[i])
            if '" in ' in lines[i] or "' in " in lines[i]:
                break
            i += 1
        blocks.append("\n".join(block))
        i += 1
    return blocks


def detect_features(block: str) -> list[str]:
    lower = block.lower()
    features = []
    for name, marker in ANALYSIS_MARKERS.items():
        if marker.lower() in lower:
            features.append(name)
    return features


def timestamp_from_case_dir(case_dir: str) -> str:
    match = re.search(r"(\d{4}-\d{2}-\d{2}-\d{6})", case_dir)
    return match.group(1) if match else ""


def replicate_from_path(path: Path) -> str:
    for part in path.parts:
        match = re.fullmatch(r"replicate_(\d+)", part)
        if match:
            return match.group(1)
    return ""


def audit_log(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace")
    blocks = command_blocks(text)
    powershell_used = bool(blocks)
    python_used = False
    inline_python_used = False
    json_validation_used = False
    analysis_python_used = False
    features: set[str] = set()
    for block in blocks:
        lower = block.lower()
        block_has_python = bool(re.search(r"\bpython(\.exe)?\b|\bpy\.exe\b", lower))
        if not block_has_python:
            continue
        python_used = True
        if "python -m json.tool" in lower:
            json_validation_used = True
        if "| python -" in lower:
            inline_python_used = True
            block_features = detect_features(block)
            if block_features:
                analysis_python_used = True
                features.update(block_features)
    return {
        "powershell_used": powershell_used,
        "python_used": python_used,
        "inline_python_used": inline_python_used,
        "json_validation_used": json_validation_used,
        "analysis_python_used": analysis_python_used,
        "analysis_features": ";".join(sorted(features)),
    }


def load_prediction(case_dir: Path) -> str:
    pred = case_dir / "prediction.json"
    if not pred.exists():
        return ""
    text = pred.read_text(encoding="utf-8", errors="replace")
    match = re.search(r'"prediction"\s*:\s*"(resonance_(?:present|absent))"', text)
    return match.group(1) if match else ""


def write_example(case_dir: Path, out_dir: Path, effort: str, condition: str, case_id: str) -> None:
    note = case_dir / "analysis_note.md"
    if not note.exists():
        return
    text = note.read_text(encoding="utf-8", errors="replace")
    keep = []
    capture = False
    for line in text.splitlines():
        lower = line.lower()
        if lower.startswith("physical model calculation") or lower.startswith("data comparison"):
            capture = True
        elif lower.startswith("decision"):
            capture = True
        if capture:
            keep.append(line)
    excerpt = "\n".join(keep).strip() or text.strip()
    out_dir.mkdir(parents=True, exist_ok=True)
    safe_condition = condition.lower().replace(" ", "_")
    out_path = out_dir / f"{effort}_{safe_condition}_{case_id}_analysis_excerpt.md"
    out_path.write_text(
        "# Sanitized pODMR Tool Use Example\n\n"
        f"- Reasoning effort: {effort}\n"
        f"- Condition: {condition}\n"
        f"- Public case id: {case_id}\n\n"
        "This excerpt is copied from the agent-written analysis note.  Local "
        "paths and raw Codex CLI runtime logs are not included.\n\n"
        "```text\n"
        f"{excerpt}\n"
        "```\n",
        encoding="utf-8",
    )


def main() -> None:
    args = parse_args()
    timestamp_to_case = read_case_index(args.case_index)
    by_case_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    examples_dir = args.output_dir / "tool_use_audit_examples"

    for run in RUNS:
        run_dir = args.source_root / run["dir"] / run["context"]
        files = sorted(run_dir.glob("replicate_*/*/codex_stderr.txt"))
        for log_path in files:
            case_dir = log_path.parent
            timestamp = timestamp_from_case_dir(case_dir.name)
            case_id = timestamp_to_case.get(timestamp, "")
            record = audit_log(log_path)
            by_case_rows.append(
                {
                    "reasoning": run["effort"],
                    "condition": run["condition"],
                    "replicate": replicate_from_path(log_path),
                    "case_id": case_id,
                    "timestamp": timestamp,
                    "prediction": load_prediction(case_dir),
                    **record,
                }
            )

        subset = [
            row
            for row in by_case_rows
            if row["reasoning"] == run["effort"] and row["condition"] == run["condition"]
        ]
        n = len(subset)
        summary_rows.append(
            {
                "reasoning": run["effort"],
                "condition": run["condition"],
                "runs": n,
                "powershell_runs": sum(bool(row["powershell_used"]) for row in subset),
                "python_runs": sum(bool(row["python_used"]) for row in subset),
                "inline_python_runs": sum(bool(row["inline_python_used"]) for row in subset),
                "analysis_python_runs": sum(bool(row["analysis_python_used"]) for row in subset),
                "json_validation_runs": sum(bool(row["json_validation_used"]) for row in subset),
            }
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    by_case_path = args.output_dir / "tool_use_audit_by_case.csv"
    summary_path = args.output_dir / "tool_use_audit_summary.csv"
    with by_case_path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "reasoning",
            "condition",
            "replicate",
            "case_id",
            "timestamp",
            "prediction",
            "powershell_used",
            "python_used",
            "inline_python_used",
            "analysis_python_used",
            "json_validation_used",
            "analysis_features",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(by_case_rows)
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "reasoning",
            "condition",
            "runs",
            "powershell_runs",
            "python_runs",
            "inline_python_runs",
            "analysis_python_runs",
            "json_validation_runs",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_rows)

    # Write one representative expected-signal example with analysis Python.
    for row in by_case_rows:
        if (
            row["condition"] == "Expected signal"
            and row["reasoning"] == "high"
            and row["analysis_python_used"]
            and row["case_id"]
        ):
            run = next(
                r
                for r in RUNS
                if r["effort"] == row["reasoning"] and r["condition"] == row["condition"]
            )
            case_dirs = sorted((args.source_root / run["dir"] / run["context"]).glob(f"replicate_{row['replicate']}/*{row['timestamp']}"))
            if case_dirs:
                write_example(case_dirs[0], examples_dir, str(row["reasoning"]), str(row["condition"]), str(row["case_id"]))
                break

    (examples_dir / "README.md").write_text(
        "# pODMR Tool Use Audit Examples\n\n"
        "These files contain sanitized excerpts from agent-written analysis notes.  "
        "The original Codex CLI stderr logs are not included in the public release "
        "because they contain local paths and unrelated runtime output.  The CSV "
        "audit files report derived counts of shell and Python use.\n",
        encoding="utf-8",
    )

    print(summary_path)
    print(by_case_path)


if __name__ == "__main__":
    main()
