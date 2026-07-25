"""Compose manuscript Figs. 3 and 4 from existing vector artwork."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARCHITECTURE = ROOT / "figure_sources" / "fig_autoNV_overview_v5_0.pdf"
DEFAULT_FIGURE3_TRIAL = ROOT / "reproduced" / "figure3_data_panels_trial.pdf"
DEFAULT_FIGURE4_TRIAL = ROOT / "reproduced" / "figure4_data_panels_trial.pdf"
DEFAULT_OUTPUT_DIR = ROOT / "reproduced"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--architecture", type=Path, default=DEFAULT_ARCHITECTURE)
    parser.add_argument("--figure3-trial", type=Path, default=DEFAULT_FIGURE3_TRIAL)
    parser.add_argument("--figure4-trial", type=Path, default=DEFAULT_FIGURE4_TRIAL)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def show_clip(
    target_page: fitz.Page,
    target_rect: fitz.Rect,
    source_doc: fitz.Document,
    clip: fitz.Rect,
) -> None:
    target_page.show_pdf_page(
        target_rect,
        source_doc,
        0,
        clip=clip,
        keep_proportion=True,
        overlay=True,
    )


def save_document(document: fitz.Document, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    document.save(path, garbage=4, deflate=True)
    document.close()

    reopened = fitz.open(path)
    if len(reopened) != 1:
        raise ValueError(f"Expected a one-page PDF: {path}")
    page = reopened[0]
    pixmap = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), alpha=False)
    pixmap.save(path.with_suffix(".png"))
    reopened.close()


def compose_figure3(
    architecture: fitz.Document,
    trial_path: Path,
    output_path: Path,
) -> None:
    trial = fitz.open(trial_path)
    source_page = trial[0]
    output = fitz.open()
    page = output.new_page(width=source_page.rect.width, height=source_page.rect.height)
    page.show_pdf_page(page.rect, trial, 0, keep_proportion=False)
    show_clip(
        page,
        fitz.Rect(43, 20, 251, 158),
        architecture,
        fitz.Rect(306, 309, 526, 563),
    )
    save_document(output, output_path)
    trial.close()


def compose_figure4(
    architecture: fitz.Document,
    trial_path: Path,
    output_path: Path,
) -> None:
    trial = fitz.open(trial_path)
    source_page = trial[0]
    output = fitz.open()
    page = output.new_page(width=source_page.rect.width, height=source_page.rect.height)
    page.show_pdf_page(page.rect, trial, 0, keep_proportion=False)
    show_clip(
        page,
        fitz.Rect(20, 18, 179, 214),
        architecture,
        fitz.Rect(556, 309, 766, 563),
    )
    save_document(output, output_path)
    trial.close()


def require_file(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(
            f"Required source file not found: {path}. "
            "Run the quantitative-panel scripts first."
        )


def main() -> None:
    args = parse_args()
    for path in (args.architecture, args.figure3_trial, args.figure4_trial):
        require_file(path)

    architecture = fitz.open(args.architecture)
    compose_figure3(
        architecture,
        args.figure3_trial,
        args.output_dir / "figure3_ramsey_benchmark.pdf",
    )
    compose_figure4(
        architecture,
        args.figure4_trial,
        args.output_dir / "figure4_podmr_benchmark.pdf",
    )
    architecture.close()


if __name__ == "__main__":
    main()
