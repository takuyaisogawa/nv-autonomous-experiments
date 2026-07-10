#!/usr/bin/env python3
"""Build neutral pre-analysis checkpoint inputs from image145844 records.

Each checkpoint uses the project snapshot from immediately after the target
Ramsey job was launched. The only later files added are the terminal raw
measurement data and bridge metadata for that target Ramsey.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any


BENCH_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = BENCH_ROOT.parents[1]
PROJECT_ROOT = REPO_ROOT / "cases" / "image145844" / "project"
SOURCE_ROOT = (
    REPO_ROOT
    / "cases"
    / "image145844"
    / "project"
    / ".manager"
    / "wake_records"
)
ARTIFACT_ROOT = PROJECT_ROOT / "work" / "artifacts" / "analysis"
BRIDGE_ROOT = PROJECT_ROOT / "work" / "bridge_jobs"

CHECKPOINTS = [
    {
        "checkpoint_id": "cp01",
        "launch_snapshot": "tick_000027_ed793b01dd1a155c_project",
        "measurement_source": "first_ramsey_scout",
        "measurement_files": [
            ARTIFACT_ROOT / "image145844_reimage_r03_ramsey_t2star_raw_export_20260513_1930.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_185505_auto_ramsey.job.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_185505_auto_ramsey.result.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_185505_auto_ramsey.status.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_185505_auto_ramsey.control.json",
        ],
    },
    {
        "checkpoint_id": "cp02",
        "launch_snapshot": "tick_000037_ed793b01dd1a155c_project",
        "measurement_source": "second_ramsey_followup",
        "measurement_files": [
            ARTIFACT_ROOT / "image145844_reimage_r03_ramsey_det1p0_8us_terminal_raw_export_20260513_2220.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg.job.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg.result.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg.status.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg.control.json",
        ],
    },
    {
        "checkpoint_id": "cp03",
        "launch_snapshot": "tick_000048_ed793b01dd1a155c_project",
        "measurement_source": "short_tau_ramsey",
        "measurement_files": [
            ARTIFACT_ROOT / "image145844_reimage_r03_ramsey_shorttau_terminal_raw_export_20260514_0127.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_230331_auto_ramsey.job.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_230331_auto_ramsey.result.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_230331_auto_ramsey.status.json",
            BRIDGE_ROOT / "nv23_ramsey_20260513_230331_auto_ramsey.control.json",
        ],
    },
    {
        "checkpoint_id": "cp04",
        "launch_snapshot": "tick_000058_ed793b01dd1a155c_project",
        "measurement_source": "detuning_changed_short_tau_ramsey",
        "measurement_files": [
            ARTIFACT_ROOT / "image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_raw_export_20260514_0424.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_015423_auto_ramsey.job.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_015423_auto_ramsey.result.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_015423_auto_ramsey.status.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_015423_auto_ramsey.control.json",
        ],
    },
    {
        "checkpoint_id": "cp05",
        "launch_snapshot": "tick_000076_ed793b01dd1a155c_project",
        "measurement_source": "refreshed_center_ramsey",
        "measurement_files": [
            ARTIFACT_ROOT / "image145844_reimage_r03_ramsey_refreshed_center_terminal_raw_export_20260514_0938.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_055148_auto_ramsey.job.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_055148_auto_ramsey.result.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_055148_auto_ramsey.status.json",
            BRIDGE_ROOT / "nv23_ramsey_20260514_055148_auto_ramsey.control.json",
        ],
    },
]

_JOIN = "".join
LEAK_PATTERNS = {
    "later_human_correction": re.compile(
        "|".join(
            [
                _JOIN(["resume", "_bridge", "_free_", "shifted", "_", "sideband"]),
                _JOIN(["shifted", "_", "sideband", "_reanalysis"]),
                _JOIN(["reclose", "out"]),
            ]
        ),
        re.I,
    ),
    "explicit_answer_phrase": re.compile(
        "|".join(
            [
                _JOIN([r"residual\s+", "carrier", r"\s+", "shift"]),
                _JOIN(["carrier", "-", "shifted"]),
                _JOIN(["shifted", r"\s+", "sideband"]),
            ]
        ),
        re.I,
    ),
}

TEXT_EXTENSIONS = {
    ".csv",
    ".json",
    ".jsonl",
    ".log",
    ".m",
    ".md",
    ".py",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sanitize_text(text: str) -> str:
    sep = r"(?:\\\\|\\)"
    text = re.sub(
        rf"[A-Za-z]:{sep}Users{sep}<LAB_DOCUMENTS>{sep}MATLAB{sep}23-C",
        "<MATLAB_23C_ROOT>",
        text,
    )
    text = re.sub(
        rf"[A-Za-z]:{sep}Users{sep}<LAB_DOCUMENTS>{sep}MATLAB{sep}nv_bridge",
        "<NV_BRIDGE_ROOT>",
        text,
    )
    text = re.sub(
        rf"[A-Za-z]:{sep}Users{sep}<LAB_DOCUMENTS>{sep}MATLAB",
        "<LAB_MATLAB_ROOT>",
        text,
    )
    text = re.sub(r"[A-Za-z]:(?:\\\\|\\)[^\"'\s,}\]]+", "<WINDOWS_PATH>", text)
    return text


def copy_text_or_binary(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix.lower() in TEXT_EXTENSIONS:
        write_text(dst, sanitize_text(read_text(src)))
    else:
        shutil.copy2(src, dst)


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def compact_context(
    src_context: dict[str, Any],
    cp_id: str,
    evidence_pairs: list[tuple[Path, str]],
    measurement_pairs: list[tuple[Path, str]],
) -> dict[str, Any]:
    """Return agent-visible context without source artifact names or paths."""

    research_context = src_context.get("next_action", {}).get("research_context", {})
    recent_evidence = []
    for idx, item in enumerate(research_context.get("recent_evidence", []), start=1):
        recent_evidence.append(
            {
                "item": f"recent_{idx:03d}",
                "category": item.get("category", ""),
                "summary": item.get("summary", ""),
                "related_claims": item.get("related_claims", []),
                "tags": item.get("tags", []),
                "timestamp": item.get("timestamp", ""),
                "file_count": len(item.get("paths", [])),
            }
        )

    return {
        "schema_version": 1,
        "checkpoint_id": cp_id,
        "created_at": src_context.get("created_at", ""),
        "cutoff_time": src_context.get("cutoff_time", ""),
        "cutoff_rule": src_context.get("cutoff_rule", ""),
        "agent": {
            "id": src_context.get("agent", {}).get("id", ""),
            "model": src_context.get("agent", {}).get("model", ""),
            "thinking": src_context.get("agent", {}).get("thinking", ""),
        },
        "next_action": {
            "kind": src_context.get("next_action", {}).get("kind", ""),
            "reason": src_context.get("next_action", {}).get("reason", ""),
        },
        "agent_visible_files": {
            "project": ["project/state.md", "project/brief.md", "project/advice.md"],
            "md": ["md/memory.md", "md/knowledge.md"],
            "context": ["context.json"],
            "evidence": [f"evidence/{neutral}" for _, neutral in evidence_pairs],
            "measurement": [f"measurement/{neutral}" for _, neutral in measurement_pairs],
        },
        "recent_evidence": recent_evidence,
        "notes": [
            "Project, memory, knowledge, context, and evidence files are from the launch-time snapshot immediately after the target Ramsey was started.",
            "The measurement directory contains only later terminal raw data and bridge metadata for that target Ramsey.",
            "Source artifact names, source wake names, and source paths were removed from this agent-visible context file.",
            "Use the neutral files in this checkpoint directory as the available evidence.",
        ],
    }


def neutral_evidence_names(evidence_dir: Path) -> list[tuple[Path, str]]:
    files = sorted(path for path in evidence_dir.iterdir() if path.is_file())
    pairs: list[tuple[Path, str]] = []
    for idx, src in enumerate(files, start=1):
        suffix = src.suffix.lower() or ".dat"
        pairs.append((src, f"e{idx:03d}{suffix}"))
    return pairs


def neutral_measurement_names(files: list[Path]) -> list[tuple[Path, str]]:
    pairs: list[tuple[Path, str]] = []
    for idx, src in enumerate(files, start=1):
        suffix = src.suffix.lower() or ".dat"
        pairs.append((src, f"m{idx:03d}{suffix}"))
    return pairs


def scan_for_leaks(paths: list[Path]) -> list[str]:
    hits: list[str] = []
    for path in paths:
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text = read_text(path)
        for name, pattern in LEAK_PATTERNS.items():
            if pattern.search(text):
                hits.append(f"{path.name}:{name}")
    return hits


def reset_dir(path: Path) -> None:
    resolved = path.resolve()
    allowed = (BENCH_ROOT / "inputs").resolve()
    if allowed not in resolved.parents and resolved != allowed:
        raise RuntimeError(f"refusing to remove unexpected path: {resolved}")
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def build_checkpoint(config: dict[str, Any]) -> tuple[dict[str, str], list[dict[str, str]]]:
    cp_id = str(config["checkpoint_id"])
    tick = str(config["launch_snapshot"])
    src_root = SOURCE_ROOT / tick
    if not src_root.exists():
        raise FileNotFoundError(src_root)
    measurement_files = [Path(path) for path in config["measurement_files"]]
    for path in measurement_files:
        if not path.exists():
            raise FileNotFoundError(path)

    dst_root = BENCH_ROOT / "inputs" / "checkpoints" / cp_id
    reset_dir(dst_root)

    evidence_pairs = neutral_evidence_names(src_root / "evidence")
    measurement_pairs = neutral_measurement_names(measurement_files)

    project_files = [
        (src_root / "project" / "work_state.md", dst_root / "project" / "state.md"),
        (src_root / "project" / "brief.md", dst_root / "project" / "brief.md"),
        (src_root / "project" / "human_advice.md", dst_root / "project" / "advice.md"),
    ]
    md_files = [
        (src_root / "md" / "NV_RESEARCH_MEMORY.md", dst_root / "md" / "memory.md"),
        (src_root / "md" / "NV_RESEARCH_KNOWLEDGE.md", dst_root / "md" / "knowledge.md"),
    ]
    for src, dst in project_files + md_files:
        copy_text_or_binary(src, dst)

    for src, neutral in evidence_pairs:
        copy_text_or_binary(src, dst_root / "evidence" / neutral)
    for src, neutral in measurement_pairs:
        copy_text_or_binary(src, dst_root / "measurement" / neutral)

    context = compact_context(
        load_json(src_root / "context_manifest.json"),
        cp_id,
        evidence_pairs,
        measurement_pairs,
    )
    write_text(dst_root / "context.json", json.dumps(context, indent=2, ensure_ascii=True) + "\n")

    visible_paths = [path for path in dst_root.rglob("*") if path.is_file()]
    leak_hits = scan_for_leaks(visible_paths)

    source_row = {
        "checkpoint_id": cp_id,
        "launch_snapshot": tick,
        "measurement_source": str(config["measurement_source"]),
        "agent_visible_path": str(Path("inputs") / "checkpoints" / cp_id),
        "evidence_file_count": str(len(evidence_pairs)),
        "measurement_file_count": str(len(measurement_pairs)),
        "visible_sha256": sha256(dst_root / "context.json"),
        "leakage_status": "review" if leak_hits else "clean",
        "leakage_hits": ";".join(leak_hits),
    }

    map_rows = []
    for src, neutral in evidence_pairs:
        map_rows.append(
            {
                "checkpoint_id": cp_id,
                "neutral_path": str(Path("inputs") / "checkpoints" / cp_id / "evidence" / neutral),
                "source_kind": "launch_snapshot_evidence",
                "source_snapshot": tick,
                "source_name": src.name,
                "source_sha256": sha256(src),
            }
        )
    for src, neutral in measurement_pairs:
        map_rows.append(
            {
                "checkpoint_id": cp_id,
                "neutral_path": str(Path("inputs") / "checkpoints" / cp_id / "measurement" / neutral),
                "source_kind": "terminal_measurement_data",
                "source_snapshot": "",
                "source_name": src.name,
                "source_sha256": sha256(src),
            }
        )
    return source_row, map_rows


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    reset_dir(BENCH_ROOT / "inputs" / "checkpoints")
    (BENCH_ROOT / "inputs" / "provenance").mkdir(parents=True, exist_ok=True)

    index_rows: list[dict[str, str]] = []
    map_rows: list[dict[str, str]] = []
    for config in CHECKPOINTS:
        row, rows = build_checkpoint(config)
        index_rows.append(row)
        map_rows.extend(rows)

    write_csv(
        BENCH_ROOT / "inputs" / "checkpoint_index.csv",
        index_rows,
        [
            "checkpoint_id",
            "launch_snapshot",
            "measurement_source",
            "agent_visible_path",
            "evidence_file_count",
            "measurement_file_count",
            "visible_sha256",
            "leakage_status",
            "leakage_hits",
        ],
    )
    write_csv(
        BENCH_ROOT / "inputs" / "provenance" / "source_file_map.csv",
        map_rows,
        [
            "checkpoint_id",
            "neutral_path",
            "source_kind",
            "source_snapshot",
            "source_name",
            "source_sha256",
        ],
    )
    print(f"built {len(index_rows)} checkpoints under {BENCH_ROOT / 'inputs' / 'checkpoints'}")


if __name__ == "__main__":
    main()
