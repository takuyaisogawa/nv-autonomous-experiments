from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"
SCORE_FILE = RESULTS / "manual_calibration_residual_scores_2026-07-11.csv"

EFFORTS = ["low", "medium", "high", "xhigh"]
CHECKPOINTS = ["cp01", "cp02", "cp03", "cp04", "cp05"]
CRITERION = "calibration-residual"
COLOR = "#3AA35C"


def read_scores() -> list[dict[str, str]]:
    with SCORE_FILE.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 400:
        raise ValueError(f"Expected 400 score rows, found {len(rows)}")
    return rows


def summarize(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    buckets: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0])
    for row in rows:
        key = (row["reasoning_effort"], row["checkpoint_id"])
        buckets[key][1] += 1
        if row["calibration_residual_score"] == "pass":
            buckets[key][0] += 1

    summary: list[dict[str, object]] = []
    for effort in EFFORTS:
        for checkpoint in CHECKPOINTS:
            passes, total = buckets[(effort, checkpoint)]
            if total != 20:
                raise ValueError(f"Expected 20 rows for {effort}/{checkpoint}, found {total}")
            summary.append(
                {
                    "criterion_group": CRITERION,
                    "reasoning_effort": effort,
                    "checkpoint_id": checkpoint,
                    "passes": passes,
                    "total": total,
                    "pass_rate": passes / total,
                }
            )
    return summary


def write_summary_csv(summary: list[dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "criterion_group",
                "reasoning_effort",
                "checkpoint_id",
                "passes",
                "total",
                "pass_rate",
            ],
        )
        writer.writeheader()
        writer.writerows(summary)


def make_plot(summary: list[dict[str, object]], out_base: Path) -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.labelsize": 9,
            "axes.titlesize": 10,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
        }
    )

    fig = plt.figure(figsize=(8.8, 3.25), constrained_layout=False)
    gs = fig.add_gridspec(1, 2, width_ratios=[0.9, 1.45], wspace=0.30)
    fig.subplots_adjust(left=0.075, right=0.92, top=0.88, bottom=0.20)

    ax_bar = fig.add_subplot(gs[0, 0])
    x = np.arange(len(EFFORTS))
    rates = []
    labels = []
    for effort in EFFORTS:
        subset = [r for r in summary if r["reasoning_effort"] == effort]
        passes = sum(int(r["passes"]) for r in subset)
        total = sum(int(r["total"]) for r in subset)
        rates.append(passes / total)
        labels.append(f"{passes}/{total}")
    ax_bar.bar(x, rates, width=0.55, color=COLOR, edgecolor="white", linewidth=0.4)
    for xi, yi, label in zip(x, rates, labels):
        ax_bar.text(xi, yi + 0.012, label, ha="center", va="bottom", fontsize=7.5)
    ax_bar.set_title("Aggregate pass rate")
    ax_bar.set_xticks(x, EFFORTS)
    ax_bar.set_xlabel("Reasoning effort")
    ax_bar.set_ylabel("Pass rate")
    ax_bar.set_ylim(0, 0.4)
    ax_bar.grid(axis="y", color="#d9e1e5", linewidth=0.7)
    ax_bar.set_axisbelow(True)
    ax_bar.text(-0.12, 1.02, "(a)", transform=ax_bar.transAxes, fontsize=9)

    ax_heat = fig.add_subplot(gs[0, 1])
    matrix = np.zeros((len(EFFORTS), len(CHECKPOINTS)))
    labels_heat = [["" for _ in CHECKPOINTS] for __ in EFFORTS]
    for i, effort in enumerate(EFFORTS):
        for j, checkpoint in enumerate(CHECKPOINTS):
            item = next(
                r
                for r in summary
                if r["reasoning_effort"] == effort and r["checkpoint_id"] == checkpoint
            )
            matrix[i, j] = float(item["pass_rate"])
            labels_heat[i][j] = f"{int(item['passes'])}/{int(item['total'])}"
    image = ax_heat.imshow(matrix, vmin=0, vmax=1, cmap="Blues", aspect="auto")
    ax_heat.set_title("Checkpoint pass rate")
    ax_heat.set_xticks(np.arange(len(CHECKPOINTS)), CHECKPOINTS)
    ax_heat.set_yticks(np.arange(len(EFFORTS)), EFFORTS)
    ax_heat.set_xlabel("Checkpoint")
    ax_heat.set_ylabel("Reasoning effort")
    for i in range(len(EFFORTS)):
        for j in range(len(CHECKPOINTS)):
            color = "white" if matrix[i, j] > 0.58 else "#263238"
            ax_heat.text(j, i, labels_heat[i][j], ha="center", va="center", color=color, fontsize=7.5)
    ax_heat.text(-0.10, 1.02, "(b)", transform=ax_heat.transAxes, fontsize=9)
    colorbar = fig.colorbar(image, ax=ax_heat, fraction=0.04, pad=0.025)
    colorbar.set_label("Pass rate")
    colorbar.ax.tick_params(labelsize=7)

    out_base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_base.with_suffix(".png"), dpi=220)
    fig.savefig(out_base.with_suffix(".pdf"))
    plt.close(fig)


def main() -> None:
    rows = read_scores()
    summary = summarize(rows)
    out_csv = FIGURES / "reasoning_effort_sweep_low_to_xhigh_summary.csv"
    write_summary_csv(summary, out_csv)
    make_plot(summary, FIGURES / "reasoning_effort_sweep_low_to_xhigh")
    print(out_csv)
    print(FIGURES / "reasoning_effort_sweep_low_to_xhigh.png")
    print(FIGURES / "reasoning_effort_sweep_low_to_xhigh.pdf")


if __name__ == "__main__":
    main()
