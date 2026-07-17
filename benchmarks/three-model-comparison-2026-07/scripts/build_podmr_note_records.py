"""Build compact public pODMR prediction records with per-run notes."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


USER_PATH = re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+[^\\/]+", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--joined-predictions", type=Path, required=True)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def sanitize(text: str) -> str:
    redacted = USER_PATH.sub("<USER_HOME>", text)
    return "\n".join(line.rstrip() for line in redacted.splitlines())


def main() -> None:
    args = parse_args()
    with args.joined_predictions.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        rows = list(reader)
        source_fields = list(reader.fieldnames or [])

    output_fields = source_fields + ["analysis_note"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=output_fields)
        writer.writeheader()
        for row in rows:
            note_path = args.run_root / Path(row["analysis_note_path"])
            if not note_path.is_file():
                raise FileNotFoundError(note_path)
            output_row = dict(row)
            output_row["analysis_note"] = sanitize(note_path.read_text(encoding="utf-8"))
            writer.writerow(output_row)

    if len(rows) != 3456:
        raise RuntimeError(f"expected 3456 records, found {len(rows)}")


if __name__ == "__main__":
    main()
