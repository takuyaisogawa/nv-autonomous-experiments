#!/usr/bin/env python3
"""Run the public Ramsey checkpoint sweep with Claude CLI.

This adapter reuses the released checkpoint preparation, note collection, and
resume logic from run_sweep.py. It is a post-release provider adapter, not the
exact Codex CLI harness used for the manuscript results.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import platform
import subprocess
import tempfile
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import run_sweep as base


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        required=True,
        help="Use the exact Claude model id rather than a moving alias.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=("all", *base.EFFORTS),
        default="all",
    )
    parser.add_argument("--replicates", type=int, default=10)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--claude-bin", default="claude")
    parser.add_argument("--max-budget-usd", type=float)
    parser.add_argument("--checkpoint", default="all")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--result-dir",
        type=Path,
        default=base.ROOT / "results" / "claude-local",
    )
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be at least 1")
    if args.replicates < 1:
        parser.error("--replicates must be at least 1")
    return args


def prompt_text() -> str:
    return (
        base.prompt_text()
        + "\nBefore deciding, use the Read tool to open every PNG file under "
        "`evidence/`. Do not infer image content from filenames alone.\n"
    )


def claude_command(args: argparse.Namespace, effort: str) -> list[str]:
    command = [
        args.claude_bin,
        "-p",
        "--model",
        args.model,
        "--effort",
        effort,
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


def parse_claude_output(stdout: str) -> tuple[str, Any, str]:
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError as exc:
        return stdout, None, f"Claude JSON parse failed: {exc}"
    if not isinstance(payload, dict):
        return stdout, None, "Claude JSON output was not an object"
    response = payload.get("result", "")
    if not isinstance(response, str):
        response = json.dumps(response, ensure_ascii=False)
    return response, payload.get("total_cost_usd"), ""


def run_one(args: argparse.Namespace, request: dict[str, Any]) -> dict[str, Any]:
    tmp_root = Path(tempfile.mkdtemp(prefix="nv_checkpoint_claude_"))
    try:
        base.copy_checkpoint_to_tmp(request["checkpoint_id"], tmp_root)
        command = claude_command(args, request["reasoning_effort"])
        started = time.time()
        proc = subprocess.run(
            command,
            input=prompt_text(),
            cwd=tmp_root,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=args.timeout,
        )
        elapsed = time.time() - started
        response, total_cost_usd, response_error = parse_claude_output(
            proc.stdout
        )
        notes = base.collect_note_outputs(
            tmp_root,
            args.result_dir,
            request["custom_id"],
            response,
        )
        return {
            **request,
            "provider": "claude",
            "model": args.model,
            "elapsed_s": round(elapsed, 3),
            "total_cost_usd": total_cost_usd,
            "returncode": proc.returncode,
            "response": base.sanitize_runtime_text(response.strip()),
            "response_error": base.sanitize_runtime_text(response_error),
            **notes,
            "stdout_tail": "",
            "stderr_tail": base.sanitize_runtime_text(proc.stderr[-2000:]),
        }
    finally:
        base.cleanup_tmp(tmp_root)


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


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_conditions(args: argparse.Namespace) -> None:
    path = args.result_dir / "run_conditions.json"
    conditions = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "provider": "claude",
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "replicates": args.replicates,
        "checkpoint": args.checkpoint,
        "image_delivery": (
            "The agent is instructed to open PNG files under evidence/ with "
            "the Read tool; images are not attached to the initial message."
        ),
        "cli_binary": Path(args.claude_bin).name,
        "cli_version": cli_version(args.claude_bin),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "task_prompt_sha256": sha256_file(base.ROOT / "prompts" / "task.md"),
    }
    if path.exists() and not args.overwrite:
        previous = json.loads(path.read_text(encoding="utf-8"))
        immutable = (
            "provider",
            "model",
            "reasoning_effort",
            "checkpoint",
            "task_prompt_sha256",
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


def dry_run(args: argparse.Namespace, requests: list[dict[str, Any]]) -> None:
    request = requests[0]
    tmp_root = Path(tempfile.mkdtemp(prefix="nv_checkpoint_claude_preview_"))
    try:
        base.copy_checkpoint_to_tmp(request["checkpoint_id"], tmp_root)
        print(f"Prepared preview for {request['custom_id']} at {tmp_root}")
        print("Command:")
        print(
            subprocess.list2cmdline(
                claude_command(args, request["reasoning_effort"])
            )
        )
        print("No model was invoked. The preview workspace will now be removed.")
    finally:
        base.cleanup_tmp(tmp_root)


def main() -> None:
    args = parse_args()
    args.result_dir = args.result_dir.resolve()
    args.result_dir.mkdir(parents=True, exist_ok=True)
    write_conditions(args)
    requests = base.build_requests(args)
    if args.dry_run:
        dry_run(args, requests)
        return

    output_path = args.result_dir / "model_outputs.jsonl"
    existing = {} if args.overwrite else base.read_existing(output_path)
    pending = []
    for request in requests:
        row = existing.get(request["custom_id"])
        if args.overwrite:
            pending.append(request)
        elif args.retry_failed:
            if row is None or row.get("returncode") != 0:
                pending.append(request)
        elif row is None:
            pending.append(request)
    if not pending:
        print("nothing to run")
        return

    print(
        f"running {len(pending)} Claude requests; results -> {output_path}",
        flush=True,
    )
    completed = 0
    mode = "w" if args.overwrite else "a"
    with output_path.open(mode, encoding="utf-8", newline="\n") as handle:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            future_map = {
                pool.submit(run_one, args, request): request
                for request in pending
            }
            for future in concurrent.futures.as_completed(future_map):
                request = future_map[future]
                try:
                    row = future.result()
                except Exception:  # noqa: BLE001
                    row = {
                        **request,
                        "provider": "claude",
                        "model": args.model,
                        "elapsed_s": "",
                        "total_cost_usd": None,
                        "returncode": -1,
                        "response": "",
                        "response_error": "",
                        "note_path": "",
                        "note_text": "",
                        "note_source": "",
                        "note_files": [],
                        "note_errors": [],
                        "stdout_tail": "",
                        "stderr_tail": base.sanitize_runtime_text(
                            traceback.format_exc()
                        ),
                    }
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                handle.flush()
                completed += 1
                print(
                    f"{completed}/{len(pending)} {row['custom_id']} "
                    f"rc={row['returncode']}",
                    flush=True,
                )
                if args.sleep:
                    time.sleep(args.sleep)


if __name__ == "__main__":
    main()
