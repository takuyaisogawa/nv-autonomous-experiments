"""Build the quantitative panels for manuscript Fig. 3."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUMMARY = ROOT / "ramsey" / "three_model_checkpoint_summary.csv"
DEFAULT_OUTPUT = ROOT / "reproduced" / "figure3_data_panels_trial.pdf"

MODELS = ["GPT-5.4", "GPT-5.5", "GPT-5.6 Sol"]
EFFORTS = ["low", "medium", "high", "xhigh"]
EFFORT_LABELS = ["Low", "Medium", "High", "X-high"]
CHECKPOINTS = ["cp01", "cp02", "cp03", "cp04", "cp05"]
MODEL_COLORS = ["#009E73", "#0072B2", "#D55E00"]
MODEL_HATCHES = ["///", "", "xxx"]


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
            "xtick.labelsize": 6.7,
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
            key = (row["model"], row["reasoning_effort"], row["checkpoint_id"])
            data[key] = {
                "passes": int(row["passes"]),
                "total": int(row["total"]),
                "pass_rate": float(row["pass_rate"]),
            }
    expected = {
        (model, effort, checkpoint)
        for model in MODELS
        for effort in EFFORTS
        for checkpoint in CHECKPOINTS
    }
    missing = expected - data.keys()
    if missing:
        raise ValueError(f"Missing Ramsey summary rows: {sorted(missing)}")
    return data


def style_bar_axis(ax: plt.Axes) -> None:
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color="#D9D9D9", lw=0.45, alpha=0.8)
    ax.xaxis.grid(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=3, width=0.7, pad=1.6)


def plot_rate_bars(
    ax: plt.Axes,
    summary: dict[tuple[str, str, str], dict[str, float]],
) -> None:
    x = np.arange(len(EFFORTS))
    width = 0.24
    for model_index, (model, color, hatch) in enumerate(
        zip(MODELS, MODEL_COLORS, MODEL_HATCHES)
    ):
        rates: list[float] = []
        labels: list[str] = []
        for effort in EFFORTS:
            passes = sum(summary[(model, effort, cp)]["passes"] for cp in CHECKPOINTS)
            total = sum(summary[(model, effort, cp)]["total"] for cp in CHECKPOINTS)
            rates.append(passes / total)
            labels.append(f"{passes}/{total}")
        positions = x + (model_index - 1) * width
        bars = ax.bar(
            positions,
            rates,
            width=width,
            color=color,
            edgecolor="white",
            linewidth=0.45,
            hatch=hatch,
            label=model,
            zorder=3,
        )
        for bar, label in zip(bars, labels):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.013,
                label,
                ha="center",
                va="bottom",
                fontsize=5.5,
                color="#263238",
            )
    ax.set_xticks(x)
    ax.set_xticklabels(EFFORT_LABELS)
    ax.set_xlabel("Reasoning effort")
    ax.set_ylabel("Pass rate")
    ax.set_ylim(0, 0.65)
    ax.set_yticks(np.arange(0, 0.61, 0.1))
    ax.set_title(
        "Aggregate calibration residual recognition",
        y=1.25,
        pad=0,
    )
    style_bar_axis(ax)
    panel_label(ax, "b")
    ax.legend(
        ncol=3,
        frameon=False,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.15),
        columnspacing=1.1,
        handlelength=1.6,
    )


def plot_checkpoint_heatmap(
    ax: plt.Axes,
    summary: dict[tuple[str, str, str], dict[str, float]],
    model: str,
    label: str,
    cmap: LinearSegmentedColormap,
):
    matrix = np.zeros((len(EFFORTS), len(CHECKPOINTS)))
    counts = [["" for _ in CHECKPOINTS] for _ in EFFORTS]
    for row_index, effort in enumerate(EFFORTS):
        for column_index, checkpoint in enumerate(CHECKPOINTS):
            item = summary[(model, effort, checkpoint)]
            matrix[row_index, column_index] = item["pass_rate"]
            counts[row_index][column_index] = (
                f"{int(item['passes'])}/{int(item['total'])}"
            )

    image = ax.imshow(matrix, vmin=0, vmax=1, cmap=cmap, aspect="auto")
    ax.set_title(model, pad=5.0)
    ax.set_xticks(np.arange(len(CHECKPOINTS)))
    ax.set_xticklabels(CHECKPOINTS)
    ax.set_yticks(np.arange(len(EFFORTS)))
    ax.set_yticklabels(EFFORT_LABELS)
    ax.set_xlabel("Checkpoint")
    ax.tick_params(length=0, pad=1.6)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for row_index in range(len(EFFORTS)):
        for column_index in range(len(CHECKPOINTS)):
            color = "white" if matrix[row_index, column_index] > 0.58 else "#263238"
            ax.text(
                column_index,
                row_index,
                counts[row_index][column_index],
                ha="center",
                va="center",
                color=color,
                fontsize=5.8,
            )
    panel_label(ax, label)
    return image


def build_figure(summary_path: Path, output: Path) -> None:
    configure_matplotlib()
    summary = load_summary(summary_path)
    cmap = LinearSegmentedColormap.from_list(
        "ramsey_pass_rate",
        ["#F3F6F8", "#B8DDE8", "#2A91B8", "#1F5A7A"],
    )

    fig = plt.figure(figsize=(7.02, 4.13), constrained_layout=False)
    grid = fig.add_gridspec(
        2,
        6,
        height_ratios=[1.05, 1.0],
        hspace=0.53,
        wspace=0.52,
    )
    fig.subplots_adjust(left=0.075, right=0.93, top=0.90, bottom=0.11)

    blank = fig.add_subplot(grid[0, :3])
    blank.axis("off")
    panel_label(blank, "a", x=-0.02)

    rate_axis = fig.add_subplot(grid[0, 3:])
    plot_rate_bars(rate_axis, summary)

    images = []
    for index, model in enumerate(MODELS):
        axis = fig.add_subplot(grid[1, 2 * index : 2 * index + 2])
        if index == 0:
            axis.set_ylabel("Reasoning effort")
        images.append(
            plot_checkpoint_heatmap(
                axis,
                summary,
                model,
                chr(ord("c") + index),
                cmap,
            )
        )

    colorbar = fig.colorbar(images[-1], ax=fig.axes[2:5], fraction=0.022, pad=0.025)
    colorbar.set_label("Pass rate")
    colorbar.ax.tick_params(length=2.5, width=0.7, labelsize=6.4, pad=1.5)

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    build_figure(args.summary, args.output)


if __name__ == "__main__":
    main()
