#!/usr/bin/env python3
"""First-pass calibration residual scoring for Ramsey model outputs."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


RESIDUAL_MODEL_PATTERNS = [
    re.compile(r"\bprogrammed\b.{0,80}\b1\.0\s*MHz\b.{0,160}\b(plus|\+|shifted|offset|effective|residual)\b.{0,160}\b(192\s*kHz|0\.19[0-9]?\s*MHz|1\.19[0-9]?\s*MHz)\b", re.I | re.S),
    re.compile(r"\b(192\s*kHz|0\.19[0-9]?\s*MHz|1\.19[0-9]?\s*MHz)\b.{0,160}\b(plus|\+|shifted|offset|effective|residual)\b.{0,160}\bprogrammed\b.{0,80}\b1\.0\s*MHz\b", re.I | re.S),
    re.compile(r"\bprogrammed\b.{0,80}\b1\.5\s*MHz\b.{0,160}\b0\.884\s*MHz\b.{0,160}\b(center|centre|resonance|microwave|detuning)\b.{0,80}\b(error|offset|mismatch|off|miscentered|mis[- ]?cent(?:er|re)ed)\b", re.I | re.S),
    re.compile(r"\b0\.884\s*MHz\b.{0,160}\bprogrammed\b.{0,80}\b1\.5\s*MHz\b.{0,160}\b(center|centre|resonance|microwave|detuning)\b.{0,80}\b(error|offset|mismatch|off|miscentered|mis[- ]?cent(?:er|re)ed)\b", re.I | re.S),
    re.compile(r"\bprogrammed\s+ramsey\s+detuning\b.{0,180}\b(center|centre|resonance|microwave|detuning)\b.{0,80}\b(error|offset|mismatch|off|miscentered|mis[- ]?cent(?:er|re)ed)\b", re.I | re.S),
    re.compile(r"\b(nominal|programmed)\s+(detuning|det)\b.{0,120}\b(residual|additional|extra|remaining|unaccounted)\s+(offset|detuning)\b", re.I | re.S),
    re.compile(r"\b(residual|additional|extra|remaining|unaccounted)\s+(offset|detuning)\b.{0,120}\b(nominal|programmed)\s+(detuning|det)\b", re.I | re.S),
    re.compile(r"\b(effective|actual)\s+(detuning|carrier|ramsey\s+frequency)\b.{0,120}\b(nominal|programmed)\s+(detuning|det)\b.{0,120}\b(offset|residual|difference|mismatch)\b", re.I | re.S),
    re.compile(r"\b(nominal|programmed)\s+(detuning|det)\b.{0,120}\b(effective|actual)\s+(detuning|carrier|ramsey\s+frequency)\b.{0,120}\b(offset|residual|difference|mismatch)\b", re.I | re.S),
    re.compile(r"\bdet\s*=\s*1\.0\s*MHz\b.{0,160}\b1\.19[0-9]?\s*MHz\b.{0,160}\b(residual|offset|effective\s+detuning)\b", re.I | re.S),
    re.compile(r"\b1\.19[0-9]?\s*MHz\b.{0,160}\bdet\s*=\s*1\.0\s*MHz\b.{0,160}\b(residual|offset|effective\s+detuning)\b", re.I | re.S),
    re.compile(r"\b(microwave|mw|resonance|center|centre)\b.{0,80}\b(error|offset|drift|miscentered|mis[- ]?cent(?:er|re)ed|shifted)\b.{0,120}\b(nominal|programmed)\s+(detuning|det)\b", re.I | re.S),
    re.compile(r"\b(nominal|programmed)\s+(detuning|det)\b.{0,120}\b(microwave|mw|resonance|center|centre)\b.{0,80}\b(error|offset|drift|miscentered|mis[- ]?cent(?:er|re)ed|shifted)\b", re.I | re.S),
]

CALIBRATION_PATTERNS = [
    re.compile(r"\b(pODMR|weak[- ]?pi|mw_freq|microwave|resonance|frequency calibration)\b.{0,140}\b(error|offset|drift|mismatch|miscentered|mis[- ]?cent(?:er|re)ed|recalibrat(?:e|ed|ion)|center|centre)\b", re.I | re.S),
    re.compile(r"\b(error|offset|drift|mismatch|miscentered|mis[- ]?cent(?:er|re)ed)\b.{0,140}\b(pODMR|weak[- ]?pi|mw_freq|microwave|resonance center|resonance centre|frequency calibration)\b", re.I | re.S),
]

WEAK_ONLY_PATTERNS = [
    re.compile(r"\b(collect|measure|run|repeat)\b.{0,80}\b(more|another|new|additional)\b", re.I | re.S),
    re.compile(r"\bunsupported|not supported|non-claim|no claim|inconclusive\b", re.I),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("outputs", type=Path)
    parser.add_argument("--scored-csv", type=Path, default=None)
    parser.add_argument("--summary-md", type=Path, default=None)
    return parser.parse_args()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def classify(text: str) -> tuple[str, str]:
    residual = [pat.pattern for pat in RESIDUAL_MODEL_PATTERNS if pat.search(text)]
    calibration = [pat.pattern for pat in CALIBRATION_PATTERNS if pat.search(text)]
    if residual and calibration:
        return "pass", f"residual={residual[0]} calibration={calibration[0]}"
    if residual:
        return "fail", "residual interpretation without a calibration link"
    weak = [pat.pattern for pat in WEAK_ONLY_PATTERNS if pat.search(text)]
    if weak:
        return "fail", weak[0]
    return "ambiguous", ""


def score_rows(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    scored = []
    for row in rows:
        response = str(row.get("response", ""))
        note_text = str(row.get("note_text", ""))
        combined_text = response + "\n\n" + note_text
        score, evidence = classify(combined_text)
        scored.append(
            {
                "custom_id": str(row.get("custom_id", "")),
                "checkpoint_id": str(row.get("checkpoint_id", "")),
                "reasoning_effort": str(row.get("reasoning_effort", "")),
                "replicate": str(row.get("replicate", "")),
                "model": str(row.get("model", "")),
                "returncode": str(row.get("returncode", "")),
                "score": score,
                "score_evidence": evidence,
                "note_path": str(row.get("note_path", "")),
                "response_excerpt": re.sub(r"\s+", " ", response).strip()[:300],
                "note_excerpt": re.sub(r"\s+", " ", note_text).strip()[:300],
            }
        )
    return scored


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "custom_id",
        "checkpoint_id",
        "reasoning_effort",
        "replicate",
        "model",
        "returncode",
        "score",
        "score_evidence",
        "note_path",
        "response_excerpt",
        "note_excerpt",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_summary(path: Path, rows: list[dict[str, str]]) -> None:
    counts: dict[tuple[str, str], dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for row in rows:
        counts[(row["reasoning_effort"], row["checkpoint_id"])][row["score"]] += 1
        counts[(row["reasoning_effort"], row["checkpoint_id"])]["n"] += 1

    efforts = sorted({row["reasoning_effort"] for row in rows})
    checkpoints = sorted({row["checkpoint_id"] for row in rows})
    lines = ["# Score Summary", ""]
    lines.append("| Reasoning | Checkpoint | N | Pass | Fail | Ambiguous | Pass rate |")
    lines.append("| --- | --- | ---: | ---: | ---: | ---: | ---: |")
    for effort in efforts:
        for checkpoint in checkpoints:
            c = counts[(effort, checkpoint)]
            n = c["n"]
            pass_rate = (c["pass"] / n) if n else 0.0
            lines.append(
                f"| {effort} | {checkpoint} | {n} | {c['pass']} | {c['fail']} | "
                f"{c['ambiguous']} | {pass_rate:.1%} |"
            )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    args = parse_args()
    rows = read_jsonl(args.outputs)
    scored = score_rows(rows)
    scored_csv = args.scored_csv or args.outputs.with_name("scored_outputs.csv")
    summary_md = args.summary_md or args.outputs.with_name("score_summary.md")
    write_csv(scored_csv, scored)
    write_summary(summary_md, scored)
    print(f"wrote {scored_csv}")
    print(f"wrote {summary_md}")


if __name__ == "__main__":
    main()
