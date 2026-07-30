#!/usr/bin/env python3
"""Run the public pODMR benchmark with one isolated workspace per case.

This is a reconstructed, provider-neutral runner built from the released
inputs, prompts, scoring files, and batch runner. It is not claimed to be the
exact private harness used for the manuscript runs.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import platform
import re
import shutil
import subprocess
import tempfile
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EFFORTS = ("low", "medium", "high", "xhigh")
CONDITION_FILES = {
    "context_0": ROOT / "prompts" / "context_0_protocol_only.md",
    "context_A": ROOT / "prompts" / "context_A_domain_facts.md",
    "context_B": ROOT / "prompts" / "context_B_model_first.md",
}
PREDICTIONS = {"resonance_present", "resonance_absent"}
FIELDNAMES = [
    "provider",
    "model",
    "reasoning_effort",
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
    "elapsed_s",
    "total_cost_usd",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one pODMR case per isolated model workspace."
    )
    parser.add_argument("--provider", choices=("codex", "claude"), required=True)
    parser.add_argument(
        "--model",
        required=True,
        help="Use the exact model id when the provider exposes one.",
    )
    parser.add_argument("--reasoning-effort", choices=EFFORTS, required=True)
    parser.add_argument(
        "--condition",
        choices=("all", *CONDITION_FILES),
        default="all",
    )
    parser.add_argument(
        "--case-index",
        type=Path,
        default=ROOT / "inputs" / "case_index.csv",
    )
    parser.add_argument(
        "--case-id",
        action="append",
        dest="case_ids",
        help="Run only this case id. May be repeated.",
    )
    parser.add_argument("--replicates", type=int, default=3)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--claude-bin", default="claude")
    parser.add_argument(
        "--max-budget-usd",
        type=float,
        help="Optional per-run Claude CLI budget limit.",
    )
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--keep-workspaces", action="store_true")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Prepare one preview workspace and print its command without invoking a model.",
    )
    parser.add_argument("--result-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be at least 1")
    if args.replicates < 1:
        parser.error("--replicates must be at least 1")
    if args.max_budget_usd is not None and args.provider != "claude":
        parser.error("--max-budget-usd is only valid with --provider claude")
    return args


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def cli_version(binary: str) -> str:
    try:
        proc = subprocess.run(
            [binary, "--version"],
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return f"unavailable: {type(exc).__name__}"
    text = (proc.stdout or proc.stderr).strip()
    return text.splitlines()[0] if text else f"returncode={proc.returncode}"


def git_commit() -> str:
    try:
        proc = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return proc.stdout.strip() if proc.returncode == 0 else ""


def selected_conditions(name: str) -> list[str]:
    return list(CONDITION_FILES) if name == "all" else [name]


def selected_case_rows(args: argparse.Namespace) -> list[dict[str, str]]:
    case_index = args.case_index if args.case_index.is_absolute() else ROOT / args.case_index
    rows = read_rows(case_index)
    if args.case_ids:
        requested = set(args.case_ids)
        rows = [row for row in rows if row["case_id"] in requested]
        found = {row["case_id"] for row in rows}
        missing = sorted(requested - found)
        if missing:
            raise ValueError(f"Unknown case id(s): {', '.join(missing)}")
    if args.limit is not None:
        rows = rows[: args.limit]
    if not rows:
        raise ValueError("No cases selected")
    return rows


def build_requests(
    args: argparse.Namespace, case_rows: list[dict[str, str]]
) -> list[dict[str, Any]]:
    requests: list[dict[str, Any]] = []
    for context_id in selected_conditions(args.condition):
        for replicate in range(1, args.replicates + 1):
            for row in case_rows:
                requests.append(
                    {
                        "custom_id": f"{context_id}__rep{replicate}__{row['case_id']}",
                        "context_id": context_id,
                        "replicate": replicate,
                        "case_id": row["case_id"],
                        "timestamp": row["timestamp"],
                        "case_row": row,
                    }
                )
    return requests


def compact_sequence_text(sequence: str) -> str:
    return sequence.replace("\r\n", "\n").replace("\r", "\n")


def task_prompt(context_id: str) -> str:
    condition = CONDITION_FILES[context_id].read_text(encoding="utf-8").strip()
    return (
        "You are evaluating exactly one pODMR benchmark case. Use only the "
        "files in this working directory. Do not use web search, labels, "
        "previous outputs, sibling cases, repository files, or other external "
        "context.\n\n"
        "Before deciding, read sequence.xml and raw_export.json and open "
        "raw_readouts.png with the available image or file-reading tool. "
        "case_metadata.json contains only acquisition metadata.\n\n"
        f"{condition}\n\n"
        "Write outputs/prediction.json as a JSON object with exactly these "
        "fields:\n"
        '{"prediction":"resonance_present or resonance_absent",'
        '"short_reason":"a concise reason"}\n\n'
        "You may also write a longer analysis to outputs/analysis_note.md. "
        "Then reply with a brief completion message that includes the final "
        "prediction."
    )


def prepare_workspace(
    workspace: Path, row: dict[str, str], context_id: str
) -> None:
    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "outputs").mkdir(exist_ok=True)
    raw_src = ROOT / "inputs" / row["raw_export_path"]
    image_src = ROOT / "inputs" / row["diagnostic_figure_path"]
    if not raw_src.is_file() or not image_src.is_file():
        raise FileNotFoundError(f"Missing public input for {row['case_id']}")
    shutil.copy2(raw_src, workspace / "raw_export.json")
    shutil.copy2(image_src, workspace / "raw_readouts.png")
    export = json.loads(raw_src.read_text(encoding="utf-8"))
    sequence = compact_sequence_text(export["scan"].get("Sequence", ""))
    (workspace / "sequence.xml").write_text(sequence, encoding="utf-8")
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
    (workspace / "case_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (workspace / "task.md").write_text(
        task_prompt(context_id) + "\n", encoding="utf-8"
    )


def provider_command(
    args: argparse.Namespace, workspace: Path, last_message: Path
) -> list[str]:
    if args.provider == "codex":
        return [
            args.codex_bin,
            "exec",
            "--config",
            f'model_reasoning_effort="{args.reasoning_effort}"',
            "--ephemeral",
            "--ignore-rules",
            "--skip-git-repo-check",
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
    command = [
        args.claude_bin,
        "-p",
        "--model",
        args.model,
        "--effort",
        args.reasoning_effort,
        "--output-format",
        "json",
        "--no-session-persistence",
        "--safe-mode",
        "--strict-mcp-config",
        "--permission-mode",
        "bypassPermissions",
    ]
    if args.max_budget_usd is not None:
        command.extend(["--max-budget-usd", str(args.max_budget_usd)])
    return command


def sanitize_runtime_text(text: str, workspace: Path | None = None) -> str:
    sanitized = text
    if workspace is not None:
        sanitized = sanitized.replace(str(workspace), "<CASE_WORKSPACE>")
    sanitized = re.sub(
        r"C:[\\/]+Users[\\/]+[^\\/]+", "<USER_HOME>", sanitized, flags=re.I
    )
    return sanitized


def response_from_process(
    args: argparse.Namespace,
    proc: subprocess.CompletedProcess[str],
    last_message: Path,
) -> tuple[str, str, Any]:
    if args.provider == "codex":
        response = (
            last_message.read_text(encoding="utf-8", errors="replace")
            if last_message.exists()
            else ""
        )
        return response, "", None
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        return proc.stdout, f"Claude JSON parse failed: {exc}", None
    if not isinstance(payload, dict):
        return proc.stdout, "Claude JSON output was not an object", None
    response = payload.get("result", "")
    if not isinstance(response, str):
        response = json.dumps(response, ensure_ascii=False)
    return response, "", payload.get("total_cost_usd")


def parse_prediction(workspace: Path, response: str) -> tuple[str, str]:
    prediction_path = workspace / "outputs" / "prediction.json"
    if prediction_path.exists():
        try:
            payload = json.loads(prediction_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            payload = {}
        prediction = str(payload.get("prediction", "")).strip()
        reason = str(payload.get("short_reason", "")).strip()
        if prediction in PREDICTIONS:
            return prediction, reason
    matches = re.findall(r"\bresonance_(?:present|absent)\b", response)
    prediction = matches[-1] if matches else "parse_failed"
    reason = re.sub(r"\s+", " ", response).strip()
    if len(reason) > 300:
        reason = reason[:297].rstrip() + "..."
    return prediction, reason


def make_workspace(
    args: argparse.Namespace, custom_id: str
) -> tuple[Path, bool]:
    if args.keep_workspaces:
        workspace = args.result_dir / "workspaces" / custom_id
        if workspace.exists():
            shutil.rmtree(workspace)
        workspace.mkdir(parents=True)
        return workspace, False
    return Path(tempfile.mkdtemp(prefix="podmr_case_")), True


def run_one(args: argparse.Namespace, request: dict[str, Any]) -> dict[str, Any]:
    workspace, remove_after = make_workspace(args, request["custom_id"])
    try:
        prepare_workspace(workspace, request["case_row"], request["context_id"])
        last_message = workspace / "outputs" / "last_message.txt"
        command = provider_command(args, workspace, last_message)
        started = time.time()
        proc = subprocess.run(
            command,
            input=task_prompt(request["context_id"]),
            cwd=workspace,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=args.timeout,
        )
        elapsed = time.time() - started
        response, response_error, cost = response_from_process(
            args, proc, last_message
        )
        prediction, short_reason = parse_prediction(workspace, response)
        analysis_path = workspace / "outputs" / "analysis_note.md"
        analysis = (
            analysis_path.read_text(encoding="utf-8", errors="replace").strip()
            if analysis_path.exists()
            else response.strip()
        )
        return {
            "custom_id": request["custom_id"],
            "provider": args.provider,
            "model": args.model,
            "reasoning_effort": args.reasoning_effort,
            "context_id": request["context_id"],
            "replicate": request["replicate"],
            "case_id": request["case_id"],
            "timestamp": request["timestamp"],
            "prediction": prediction,
            "short_reason": sanitize_runtime_text(short_reason, workspace),
            "analysis": sanitize_runtime_text(analysis, workspace),
            "elapsed_s": round(elapsed, 3),
            "total_cost_usd": cost,
            "returncode": proc.returncode,
            "response_error": sanitize_runtime_text(response_error, workspace),
            "stdout_tail": sanitize_runtime_text(proc.stdout[-2000:], workspace),
            "stderr_tail": sanitize_runtime_text(proc.stderr[-2000:], workspace),
        }
    finally:
        if remove_after:
            shutil.rmtree(workspace, ignore_errors=True)


def error_record(
    args: argparse.Namespace, request: dict[str, Any]
) -> dict[str, Any]:
    return {
        "custom_id": request["custom_id"],
        "provider": args.provider,
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "context_id": request["context_id"],
        "replicate": request["replicate"],
        "case_id": request["case_id"],
        "timestamp": request["timestamp"],
        "prediction": "parse_failed",
        "short_reason": "",
        "analysis": "",
        "elapsed_s": "",
        "total_cost_usd": None,
        "returncode": -1,
        "response_error": "",
        "stdout_tail": "",
        "stderr_tail": sanitize_runtime_text(traceback.format_exc()),
    }


def read_raw_records(path: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return records
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                record = json.loads(line)
                custom_id = record.get("custom_id")
                if isinstance(custom_id, str):
                    records[custom_id] = record
    return records


def completed_ids(
    records: dict[str, dict[str, Any]], retry_failed: bool
) -> set[str]:
    completed: set[str] = set()
    for custom_id, record in records.items():
        if retry_failed:
            if record.get("returncode") == 0 and record.get("prediction") in PREDICTIONS:
                completed.add(custom_id)
        else:
            completed.add(custom_id)
    return completed


def load_labels() -> dict[str, str]:
    return {
        row["case_id"]: row["resonance_label"]
        for row in read_rows(ROOT / "labels" / "gold_labels.csv")
    }


def outcome(gold: str, prediction: str) -> tuple[str, str]:
    if prediction not in PREDICTIONS:
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


def write_outputs(
    result_dir: Path, records: dict[str, dict[str, Any]]
) -> None:
    labels = load_labels()
    rows: list[dict[str, Any]] = []
    for record in sorted(
        records.values(),
        key=lambda item: (
            item["context_id"],
            int(item["replicate"]),
            item["case_id"],
        ),
    ):
        note_relative = (
            Path("analysis_notes")
            / record["context_id"]
            / f"replicate_{record['replicate']}"
            / f"{record['case_id']}.md"
        )
        note_path = result_dir / note_relative
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(record.get("analysis", "") + "\n", encoding="utf-8")
        gold = labels[record["case_id"]]
        correct, result = outcome(gold, record["prediction"])
        row = {
            **record,
            "gold_label": gold,
            "correct": correct,
            "outcome": result,
            "analysis_note_path": note_relative.as_posix(),
        }
        rows.append({field: row.get(field, "") for field in FIELDNAMES})
    with (result_dir / "joined_predictions.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def run_conditions(
    args: argparse.Namespace, case_index: Path
) -> dict[str, Any]:
    binary = args.codex_bin if args.provider == "codex" else args.claude_bin
    return {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "provider": args.provider,
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "condition": args.condition,
        "replicates": args.replicates,
        "image_delivery": (
            "The agent opens raw_readouts.png from the isolated per-case workspace."
        ),
        "workspace_files": [
            "raw_export.json",
            "raw_readouts.png",
            "sequence.xml",
            "case_metadata.json",
            "task.md",
            "outputs/",
        ],
        "labels_in_workspace": False,
        "cli_binary": Path(binary).name,
        "cli_version": cli_version(binary),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "runner_git_commit": git_commit(),
        "case_index_sha256": sha256_file(case_index),
        "prompt_sha256": {
            name: sha256_file(path) for name, path in CONDITION_FILES.items()
        },
    }


def write_conditions(
    args: argparse.Namespace, case_index: Path
) -> None:
    path = args.result_dir / "run_conditions.json"
    conditions = run_conditions(args, case_index)
    if path.exists() and not args.overwrite:
        previous = json.loads(path.read_text(encoding="utf-8"))
        immutable = (
            "provider",
            "model",
            "reasoning_effort",
            "condition",
            "case_index_sha256",
            "prompt_sha256",
        )
        mismatches = [
            key for key in immutable if previous.get(key) != conditions.get(key)
        ]
        if mismatches:
            raise ValueError(
                "Existing run_conditions.json is incompatible for: "
                + ", ".join(mismatches)
            )
        return
    path.write_text(
        json.dumps(conditions, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def dry_run_preview(
    args: argparse.Namespace, request: dict[str, Any]
) -> None:
    preview = args.result_dir / "dry_run_workspace"
    if preview.exists():
        raise FileExistsError(
            f"{preview} already exists; choose a new --result-dir for dry-run"
        )
    prepare_workspace(preview, request["case_row"], request["context_id"])
    command = provider_command(
        args, preview, preview / "outputs" / "last_message.txt"
    )
    print(f"Prepared {request['custom_id']} at {preview}")
    print("Command:")
    print(subprocess.list2cmdline(command))
    print("No model was invoked.")


def main() -> None:
    args = parse_args()
    args.result_dir = args.result_dir.resolve()
    case_index = args.case_index if args.case_index.is_absolute() else ROOT / args.case_index
    case_rows = selected_case_rows(args)
    requests = build_requests(args, case_rows)
    args.result_dir.mkdir(parents=True, exist_ok=True)
    write_conditions(args, case_index)
    if args.dry_run:
        dry_run_preview(args, requests[0])
        return

    raw_path = args.result_dir / "model_outputs.jsonl"
    existing = {} if args.overwrite else read_raw_records(raw_path)
    done = completed_ids(existing, args.retry_failed)
    pending = [request for request in requests if request["custom_id"] not in done]
    print(
        f"Running {len(pending)} pending of {len(requests)} requests "
        f"with provider={args.provider}, jobs={args.jobs}",
        flush=True,
    )
    mode = "w" if args.overwrite else "a"
    with raw_path.open(mode, encoding="utf-8", newline="\n") as handle:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {
                pool.submit(run_one, args, request): request for request in pending
            }
            for index, future in enumerate(
                concurrent.futures.as_completed(futures), start=1
            ):
                request = futures[future]
                try:
                    record = future.result()
                except Exception:  # noqa: BLE001
                    record = error_record(args, request)
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                handle.flush()
                existing[record["custom_id"]] = record
                print(
                    f"[{index}/{len(pending)}] {record['custom_id']} "
                    f"rc={record['returncode']} prediction={record['prediction']}",
                    flush=True,
                )
                if args.sleep:
                    time.sleep(args.sleep)
    write_outputs(args.result_dir, existing)


if __name__ == "__main__":
    main()
