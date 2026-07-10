from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"

EFFORTS = ["low", "medium", "high", "xhigh"]
CHECKPOINTS = ["cp01", "cp02", "cp03", "cp04", "cp05"]

SCORE_FILES = {
    "residual-offset": [
        RESULTS
        / "low_preanalysis_rootnote_2026-06-16"
        / "manual_scored_low_rootnote_residual_offset_20rep.csv",
        RESULTS
        / "mhx_preanalysis_wake_2026-06-16"
        / "manual_scored_mhx_residual_offset_20rep.csv",
    ],
    "strong calibration-residual": [
        RESULTS
        / "low_preanalysis_rootnote_2026-06-16"
        / "manual_scored_low_rootnote_strong_calibration_residual_20rep.csv",
        RESULTS
        / "mhx_preanalysis_wake_2026-06-16"
        / "manual_scored_mhx_strong_calibration_residual_20rep.csv",
    ],
}


def read_scores() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for criterion, paths in SCORE_FILES.items():
        for path in paths:
            if not path.exists():
                raise FileNotFoundError(path)
            with path.open("r", encoding="utf-8", newline="") as f:
                for row in csv.DictReader(f):
                    row = dict(row)
                    row["criterion_group"] = criterion
                    rows.append(row)
    return rows


def summarize(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    buckets: dict[tuple[str, str, str], list[int]] = defaultdict(lambda: [0, 0])
    for row in rows:
        key = (
            row["criterion_group"],
            row["reasoning_effort"],
            row["checkpoint_id"],
        )
        buckets[key][1] += 1
        if row["criterion_group"] == "strong calibration-residual":
            score = row.get("score") or row.get("strong_score")
        else:
            score = row.get("score") or row.get("manual_score") or row.get("weak_score")
        if score == "pass":
            buckets[key][0] += 1

    summary: list[dict[str, object]] = []
    for criterion in SCORE_FILES:
        for effort in EFFORTS:
            for checkpoint in CHECKPOINTS:
                passes, total = buckets[(criterion, effort, checkpoint)]
                summary.append(
                    {
                        "criterion_group": criterion,
                        "reasoning_effort": effort,
                        "checkpoint_id": checkpoint,
                        "passes": passes,
                        "total": total,
                        "pass_rate": passes / total if total else float("nan"),
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
        for row in summary:
            writer.writerow(row)


def make_plot(summary: list[dict[str, object]], out_base: Path) -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.labelsize": 10,
            "axes.titlesize": 11,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
        }
    )

    colors = {
        "residual-offset": "#2E7D32",
        "strong calibration-residual": "#1565C0",
    }
    x = np.arange(len(EFFORTS))
    fig = plt.figure(figsize=(11.5, 8.2), constrained_layout=True)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.35])

    ax_line = fig.add_subplot(gs[0, :])
    ax_line.set_axisbelow(True)
    bar_width = 0.34
    offsets = {
        "residual-offset": -bar_width / 2,
        "strong calibration-residual": bar_width / 2,
    }
    for criterion in SCORE_FILES:
        rates = []
        labels = []
        for effort in EFFORTS:
            subset = [
                r
                for r in summary
                if r["criterion_group"] == criterion
                and r["reasoning_effort"] == effort
            ]
            passes = sum(int(r["passes"]) for r in subset)
            total = sum(int(r["total"]) for r in subset)
            rate = passes / total if total else float("nan")
            rates.append(rate)
            labels.append(f"{passes}/{total}")
        xpos = x + offsets[criterion]
        ax_line.bar(
            xpos,
            rates,
            width=bar_width,
            color=colors[criterion],
            label=criterion,
            zorder=3,
        )
        for xi, yi, label in zip(xpos, rates, labels):
            ax_line.text(
                xi,
                yi + 0.015,
                label,
                ha="center",
                va="bottom",
                fontsize=8,
                zorder=4,
            )

    ax_line.set_title("Reasoning effort sweep: manual pass rate")
    ax_line.set_xticks(x, EFFORTS)
    ax_line.set_ylim(0, 0.6)
    ax_line.set_ylabel("Pass rate")
    ax_line.grid(axis="y", color="#dddddd", linewidth=0.8, zorder=0)
    ax_line.legend(loc="upper left", frameon=False)
    ax_line.text(
        0.0,
        -0.23,
        "All efforts used the stabilized root-level note prompt; two low runs were scored from returned output after note-file permission errors.",
        transform=ax_line.transAxes,
        fontsize=8,
        color="#555555",
    )

    for idx, criterion in enumerate(SCORE_FILES):
        ax = fig.add_subplot(gs[1, idx])
        mat = np.zeros((len(EFFORTS), len(CHECKPOINTS)))
        text = [["" for _ in CHECKPOINTS] for __ in EFFORTS]
        for i, effort in enumerate(EFFORTS):
            for j, checkpoint in enumerate(CHECKPOINTS):
                item = next(
                    r
                    for r in summary
                    if r["criterion_group"] == criterion
                    and r["reasoning_effort"] == effort
                    and r["checkpoint_id"] == checkpoint
                )
                mat[i, j] = float(item["pass_rate"])
                text[i][j] = f"{int(item['passes'])}/{int(item['total'])}"
        im = ax.imshow(mat, vmin=0, vmax=1, cmap="YlGnBu")
        ax.set_title(criterion)
        ax.set_xticks(np.arange(len(CHECKPOINTS)), CHECKPOINTS)
        ax.set_yticks(np.arange(len(EFFORTS)), EFFORTS)
        for i in range(len(EFFORTS)):
            for j in range(len(CHECKPOINTS)):
                color = "white" if mat[i, j] > 0.58 else "#222222"
                ax.text(j, i, text[i][j], ha="center", va="center", color=color, fontsize=9)
        ax.set_xlabel("Checkpoint")
        if idx == 0:
            ax.set_ylabel("Reasoning effort")
        cbar = fig.colorbar(im, ax=ax, shrink=0.82)
        cbar.set_label("Pass rate")

    fig.suptitle("NV checkpoint review benchmark", fontsize=14, fontweight="bold")
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
