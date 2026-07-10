#!/usr/bin/env python3
"""Run the neutral Ramsey project-wake reasoning sweep with Codex CLI."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import shutil
import subprocess
import tempfile
import time
import traceback
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EFFORTS = ("low", "medium", "high", "xhigh")
NOTE_RELATIVE_PATHS = [
    Path("ramsey_review.md"),
    Path("work") / "notes" / "ramsey_review.md",
]
PRIVATE_PATH_PATTERNS = [
    (re.compile(r"C:[\\/]+Users[\\/]+[^\\/]+[\\/]+AppData[\\/]+Local[\\/]+Temp[\\/]+tmp[\w.-]+", re.I), "<RUN_TMP>"),
    (re.compile(r"C:[\\/]+Users[\\/]+[^\\/]+", re.I), "<USER_HOME>"),
]


def sanitize_runtime_text(text: str) -> str:
    sanitized = text
    for pattern, replacement in PRIVATE_PATH_PATTERNS:
        sanitized = pattern.sub(replacement, sanitized)
    return sanitized


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--reasoning-effort", choices=("all", *EFFORTS), default="all")
    parser.add_argument("--replicates", type=int, default=10)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--checkpoint", default="all")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--result-dir", type=Path, default=ROOT / "results")
    return parser.parse_args()


def checkpoint_ids() -> list[str]:
    root = ROOT / "inputs" / "checkpoints"
    ids = sorted(path.name for path in root.iterdir() if path.is_dir())
    return ids


def build_requests(args: argparse.Namespace) -> list[dict[str, Any]]:
    efforts = list(EFFORTS) if args.reasoning_effort == "all" else [args.reasoning_effort]
    checkpoints = checkpoint_ids() if args.checkpoint == "all" else [args.checkpoint]
    if args.limit is not None:
        checkpoints = checkpoints[: args.limit]
    requests = []
    for effort in efforts:
        for replicate in range(1, args.replicates + 1):
            for checkpoint_id in checkpoints:
                requests.append(
                    {
                        "custom_id": f"{checkpoint_id}__{effort}__rep{replicate:02d}",
                        "checkpoint_id": checkpoint_id,
                        "reasoning_effort": effort,
                        "replicate": replicate,
                    }
                )
    return requests


def prompt_text() -> str:
    task = (ROOT / "prompts" / "task.md").read_text(encoding="utf-8").strip()
    return (
        task
        + "\n\n"
        + "Use only the files in this working directory. The available project snapshot is under "
        + "`project/`, `md/`, `evidence/`, and `measurement/`; the files have neutral names. "
        + "You may create scratch scripts, plots, and notes inside this directory, and you may use "
        + "local shell/Python tools for analysis. "
        + "Do not use outside knowledge of this case beyond ordinary NV/Ramsey physics.\n"
    )


def copy_checkpoint_to_tmp(checkpoint_id: str, tmp_root: Path) -> None:
    src = ROOT / "inputs" / "checkpoints" / checkpoint_id
    if not src.exists():
        raise FileNotFoundError(src)
    shutil.copytree(src, tmp_root, dirs_exist_ok=True)


def png_args(tmp_root: Path) -> list[str]:
    args: list[str] = []
    for path in sorted((tmp_root / "evidence").glob("*.png")):
        args.extend(["--image", str(path)])
    return args


def extract_project_note(response: str) -> str:
    match = re.search(r"(?im)^#{0,6}\s*(?:\*\*)?Project note(?:\*\*)?\s*$", response)
    if not match:
        match = re.search(r"(?im)^#{0,6}\s*(?:\*\*)?Project note(?:\*\*)?\s*[:：]\s*", response)
    if not match:
        return ""
    return response[match.start() :].strip()


def collect_note_outputs(tmp_root: Path, result_dir: Path, custom_id: str, response: str) -> dict[str, Any]:
    notes_root = tmp_root / "work" / "notes"
    note_text = ""
    note_path = ""
    note_source = ""
    note_errors: list[str] = []
    try:
        notes_exists = notes_root.exists()
    except OSError as exc:
        notes_exists = False
        note_errors.append(f"stat work/notes: {exc!r}")
    try:
        note_files = sorted(notes_root.glob("*.md")) if notes_exists else []
    except OSError as exc:
        note_files = []
        note_errors.append(f"list work/notes: {exc!r}")

    selected = None
    for note_relative_path in NOTE_RELATIVE_PATHS:
        preferred = tmp_root / note_relative_path
        try:
            preferred_exists = preferred.exists()
        except OSError as exc:
            preferred_exists = False
            note_errors.append(f"stat {note_relative_path.as_posix()}: {exc!r}")
        if preferred_exists:
            selected = preferred
            break
    if selected is None and note_files:
        selected = note_files[0]
    if selected is not None:
        note_path = str(selected.relative_to(tmp_root)).replace("\\", "/")
        try:
            note_text = selected.read_text(encoding="utf-8", errors="replace").strip()
            note_source = "file"
        except OSError as exc:
            note_errors.append(f"read {note_path}: {exc!r}")

    saved_files: list[str] = []
    root_note = tmp_root / "ramsey_review.md"
    all_note_files = []
    try:
        if root_note.exists():
            all_note_files.append(root_note)
    except OSError as exc:
        note_errors.append(f"stat ramsey_review.md: {exc!r}")
    all_note_files.extend(note_file for note_file in note_files if note_file not in all_note_files)

    if all_note_files:
        out_dir = result_dir / "notes" / custom_id
        try:
            if out_dir.exists():
                shutil.rmtree(out_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            for note_file in all_note_files:
                dst = out_dir / note_file.relative_to(tmp_root)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(note_file, dst)
                saved_files.append(str(dst.relative_to(result_dir)).replace("\\", "/"))
        except OSError as exc:
            note_errors.append(f"copy notes: {exc!r}")

    if not note_text:
        note_text = extract_project_note(response)
        if note_text:
            note_path = "final_response:Project note"
            note_source = "response"

    return {
        "note_path": note_path,
        "note_text": sanitize_runtime_text(note_text),
        "note_source": note_source,
        "note_files": saved_files,
        "note_errors": [sanitize_runtime_text(error) for error in note_errors],
    }


def cleanup_tmp(tmp_root: Path) -> None:
    for _ in range(3):
        try:
            shutil.rmtree(tmp_root)
            return
        except PermissionError:
            time.sleep(0.5)
    shutil.rmtree(tmp_root, ignore_errors=True)


def run_one(args: argparse.Namespace, request: dict[str, Any]) -> dict[str, Any]:
    tmp_root = Path(tempfile.mkdtemp(prefix="nv_checkpoint_run_"))
    try:
        copy_checkpoint_to_tmp(request["checkpoint_id"], tmp_root)
        last_message = tmp_root / "last_message.txt"
        cmd = [
            args.codex_bin,
            "exec",
            "--config",
            f'model_reasoning_effort="{request["reasoning_effort"]}"',
            "--ephemeral",
            "--ignore-rules",
            "--skip-git-repo-check",
            "--sandbox",
            "workspace-write",
            "--model",
            args.model,
            "--cd",
            str(tmp_root),
            "--output-last-message",
            str(last_message),
            *png_args(tmp_root),
            "-",
        ]
        started = time.time()
        proc = subprocess.run(
            cmd,
            input=prompt_text(),
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=args.timeout,
        )
        elapsed = time.time() - started
        response_error = ""
        try:
            response = last_message.read_text(encoding="utf-8", errors="replace") if last_message.exists() else ""
        except OSError as exc:
            response = ""
            response_error = repr(exc)
        notes = collect_note_outputs(tmp_root, args.result_dir, request["custom_id"], response)
        return {
            **request,
            "model": args.model,
            "elapsed_s": round(elapsed, 3),
            "returncode": proc.returncode,
            "response": sanitize_runtime_text(response.strip()),
            "response_error": sanitize_runtime_text(response_error),
            **notes,
            "stdout_tail": sanitize_runtime_text(proc.stdout[-2000:]),
            "stderr_tail": sanitize_runtime_text(proc.stderr[-2000:]),
        }
    finally:
        cleanup_tmp(tmp_root)


def read_existing(path: Path) -> dict[str, dict[str, Any]]:
    existing: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return existing
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            existing[row["custom_id"]] = row
    return existing


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    args = parse_args()
    output_path = args.result_dir / "model_outputs.jsonl"
    existing = read_existing(output_path)
    requests = []
    for req in build_requests(args):
        row = existing.get(req["custom_id"])
        if args.overwrite:
            requests.append(req)
        elif args.retry_failed:
            if row is None or row.get("returncode") != 0:
                requests.append(req)
        elif row is None:
            requests.append(req)
    if not requests:
        print("nothing to run")
        return

    print(f"running {len(requests)} requests; results -> {output_path}", flush=True)
    completed: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        future_map = {pool.submit(run_one, args, req): req for req in requests}
        for future in concurrent.futures.as_completed(future_map):
            req = future_map[future]
            try:
                row = future.result()
            except Exception as exc:  # noqa: BLE001
                row = {
                    **req,
                    "model": args.model,
                    "elapsed_s": "",
                    "returncode": -1,
                    "response": "",
                    "response_error": "",
                    "note_path": "",
                    "note_text": "",
                    "note_source": "",
                    "note_files": [],
                    "note_errors": [],
                    "stdout_tail": "",
                    "stderr_tail": sanitize_runtime_text(traceback.format_exc()),
                }
            append_jsonl(output_path, [row])
            completed.append(row)
            print(f"{len(completed)}/{len(requests)} {row['custom_id']} rc={row['returncode']}", flush=True)
            if args.sleep:
                time.sleep(args.sleep)


if __name__ == "__main__":
    main()
