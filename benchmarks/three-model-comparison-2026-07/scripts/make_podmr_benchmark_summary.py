"""Build the quantitative panels for manuscript Fig. 4."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUMMARY = ROOT / "podmr" / "three_model_case_bootstrap.csv"
DEFAULT_OUTPUT = ROOT / "reproduced" / "figure4_data_panels_trial.pdf"

MODELS = ["GPT-5.4", "GPT-5.5", "GPT-5.6 Sol"]
MODEL_COLORS = ["#009E73", "#0072B2", "#D55E00"]
MODEL_MARKERS = ["^", "o", "s"]
EFFORTS = ["low", "medium", "high", "xhigh"]
EFFORT_LABELS = ["Low", "Medium", "High", "X-high"]
CONDITIONS = ["protocol_only", "domain_facts", "model_first"]
CONDITION_LABELS = ["Sequence", "Facts", "Expected signal"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def configure_matplotlib() -> None:
    plt.rcParams.update(
        {
            "font.family": "Arial",
            "font.size": 7.3,
            "axes.titlesize": 7.3,
            "axes.labelsize": 7.0,
            "xtick.labelsize": 6.4,
            "ytick.labelsize": 6.7,
            "legend.fontsize": 6.6,
            "axes.linewidth": 0.6,
            "lines.linewidth": 0.8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def panel_label(ax: plt.Axes, label: str, *, x: float = -0.07) -> None:
    ax.text(
        x,
        1.06,
        label,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8.5,
        fontweight="bold",
        color="#111111",
    )


def load_summary(path: Path) -> dict[tuple[str, str, str], dict[str, float]]:
    data: dict[tuple[str, str, str], dict[str, float]] = {}
    with path.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            key = (row["model"], row["reasoning_effort"], row["condition"])
            data[key] = {
                "accuracy": float(row["accuracy"]) * 100.0,
                "accuracy_ci_low": float(row["accuracy_ci_low"]) * 100.0,
                "accuracy_ci_high": float(row["accuracy_ci_high"]) * 100.0,
                "false_positive_rate": float(row["false_positive_rate"]) * 100.0,
                "false_positive_rate_ci_low": (
                    float(row["false_positive_rate_ci_low"]) * 100.0
                ),
                "false_positive_rate_ci_high": (
                    float(row["false_positive_rate_ci_high"]) * 100.0
                ),
            }
    expected = {
        (model, effort, condition)
        for model in MODELS
        for effort in EFFORTS
        for condition in CONDITIONS
    }
    missing = expected - data.keys()
    if missing:
        raise ValueError(f"Missing pODMR summary rows: {sorted(missing)}")
    return data


def style_axis(ax: plt.Axes) -> None:
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color="#D9D9D9", lw=0.45, alpha=0.8)
    ax.xaxis.grid(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=3, width=0.7, pad=1.6)


def plot_metric(
    ax: plt.Axes,
    summary: dict[tuple[str, str, str], dict[str, float]],
    condition: str,
    metric: str,
    label: str,
) -> None:
    x = np.arange(len(EFFORTS))
    for model, color, marker in zip(MODELS, MODEL_COLORS, MODEL_MARKERS):
        values = np.asarray(
            [summary[(model, effort, condition)][metric] for effort in EFFORTS]
        )
        lows = np.asarray(
            [
                summary[(model, effort, condition)][f"{metric}_ci_low"]
                for effort in EFFORTS
            ]
        )
        highs = np.asarray(
            [
                summary[(model, effort, condition)][f"{metric}_ci_high"]
                for effort in EFFORTS
            ]
        )
        ax.errorbar(
            x,
            values,
            yerr=np.vstack([values - lows, highs - values]),
            color=color,
            marker=marker,
            markersize=3.5,
            linewidth=1.15,
            elinewidth=0.55,
            capsize=1.6,
            label=model,
            zorder=3,
        )
    ax.set_xticks(x)
    ax.set_xticklabels(EFFORT_LABELS)
    style_axis(ax)
    panel_label(ax, label)


def build_figure(summary_path: Path, output: Path) -> None:
    configure_matplotlib()
    summary = load_summary(summary_path)

    fig = plt.figure(figsize=(7.10, 3.01), constrained_layout=False)
    grid = fig.add_gridspec(
        2,
        4,
        width_ratios=[2.2, 1.0, 1.0, 1.0],
        hspace=0.40,
        wspace=0.31,
    )
    fig.subplots_adjust(left=0.025, right=0.985, top=0.83, bottom=0.17)

    blank = fig.add_subplot(grid[:, 0])
    blank.axis("off")
    panel_label(blank, "a", x=-0.01)

    axes: list[list[plt.Axes]] = [[], []]
    panel_labels = [["b", "c", "d"], ["e", "f", "g"]]
    for column, (condition, title) in enumerate(
        zip(CONDITIONS, CONDITION_LABELS),
        start=1,
    ):
        top = fig.add_subplot(grid[0, column])
        plot_metric(
            top,
            summary,
            condition,
            "false_positive_rate",
            panel_labels[0][column - 1],
        )
        top.set_title(title, pad=5.0)
        top.set_ylim(-1, 65)
        top.set_xticklabels([])
        axes[0].append(top)

        bottom = fig.add_subplot(grid[1, column])
        plot_metric(
            bottom,
            summary,
            condition,
            "accuracy",
            panel_labels[1][column - 1],
        )
        bottom.set_ylim(55, 102)
        bottom.set_xlabel("Reasoning effort")
        axes[1].append(bottom)

    axes[0][0].set_ylabel("False positive rate (%)")
    axes[1][0].set_ylabel("Accuracy (%)")
    for row in range(2):
        for column in range(1, 3):
            axes[row][column].set_yticklabels([])

    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        ncol=3,
        frameon=False,
        loc="upper center",
        bbox_to_anchor=(0.72, 0.985),
        columnspacing=1.1,
        handlelength=1.6,
        handletextpad=0.45,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    build_figure(args.summary, args.output)


if __name__ == "__main__":
    main()
