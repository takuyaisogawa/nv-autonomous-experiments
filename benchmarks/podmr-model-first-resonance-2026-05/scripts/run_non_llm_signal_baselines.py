"""Run non-LLM pODMR resonance-classification baselines.

The baselines use only the released raw pODMR exports and gold labels.  They are
intended as simple signal-processing controls for the LLM-agent benchmark.
"""

from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
from scipy.optimize import curve_fit


ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "inputs" / "openclaw_raw_exports"
LABELS = ROOT / "labels" / "gold_labels.csv"
RESULTS = ROOT / "results"

EXPECTED_SETUP_CONTRAST = 0.22
EFFORT_ORDER = ["low", "medium", "high", "xhigh"]


def mad(values: np.ndarray) -> float:
    values = np.asarray(values, dtype=float)
    median = float(np.nanmedian(values))
    return float(1.4826 * np.nanmedian(np.abs(values - median)) + 1e-12)


def load_labels() -> dict[str, str]:
    with LABELS.open(newline="", encoding="utf-8") as handle:
        return {
            row["case_id"]: row["resonance_label"]
            for row in csv.DictReader(handle)
        }


def scan_axis(scan: dict) -> np.ndarray:
    return np.linspace(
        float(scan["vary_begin"]) / 1e9,
        float(scan["vary_end"]) / 1e9,
        int(scan["vary_points"]),
    )


def linear_model(x: np.ndarray, offset: float, slope: float) -> np.ndarray:
    xc = x - float(np.mean(x))
    return offset + slope * xc


def gaussian_model(
    x: np.ndarray, offset: float, slope: float, amp: float, center: float, sigma: float
) -> np.ndarray:
    return linear_model(x, offset, slope) + amp * np.exp(
        -0.5 * ((x - center) / sigma) ** 2
    )


def lorentzian_model(
    x: np.ndarray, offset: float, slope: float, amp: float, center: float, gamma: float
) -> np.ndarray:
    return linear_model(x, offset, slope) + amp / (1.0 + ((x - center) / gamma) ** 2)


def bic(y: np.ndarray, yhat: np.ndarray, n_params: int) -> float:
    resid = np.asarray(y, dtype=float) - np.asarray(yhat, dtype=float)
    n = resid.size
    rss = max(float(np.sum(resid**2)), 1e-18)
    return n * math.log(rss / n) + n_params * math.log(n)


def safe_fit(
    model: Callable,
    x: np.ndarray,
    y: np.ndarray,
    p0: list[float],
    bounds: tuple[list[float], list[float]],
) -> tuple[np.ndarray | None, float | None]:
    try:
        params, _ = curve_fit(
            model,
            x,
            y,
            p0=p0,
            bounds=bounds,
            maxfev=20000,
        )
        yhat = model(x, *params)
        return params, bic(y, yhat, len(params))
    except Exception:
        return None, None


@dataclass
class CaseFeatures:
    case_id: str
    label: str
    depth: float
    depth_frequency_ghz: float
    detrended_depth: float
    detrended_snr: float
    avg_center_separation_mhz: float
    avg_min_depth: float
    avg_min_snr: float
    lorentzian_amp: float
    lorentzian_delta_bic: float
    gaussian_amp: float
    gaussian_delta_bic: float


def per_average_features(scan: dict, x: np.ndarray) -> tuple[float, float, float]:
    each = np.asarray(scan.get("ExperimentDataEachAvg"), dtype=float)
    if each.ndim != 4 or each.shape[2] < 2:
        return float("nan"), float("nan"), float("nan")

    centers: list[float] = []
    depths: list[float] = []
    snrs: list[float] = []
    interior = np.arange(1, len(x) - 1)
    for avg_idx in range(each.shape[2]):
        reference = each[0, 0, avg_idx, :]
        signal = each[0, 1, avg_idx, :]
        contrast = 1.0 - signal / reference
        trend = np.polyval(np.polyfit(x, contrast, 1), x)
        residual = contrast - trend
        idx = int(interior[np.nanargmax(residual[interior])])
        noise = mad(np.diff(residual)) / math.sqrt(2.0)
        centers.append(float(x[idx]))
        depths.append(float(residual[idx]))
        snrs.append(float(residual[idx] / noise))

    return (
        float(abs(centers[0] - centers[1]) * 1000.0),
        float(min(depths)),
        float(min(snrs)),
    )


def extract_features(case_id: str, label: str) -> CaseFeatures:
    raw = json.loads((INPUTS / f"{case_id}_openclaw_raw_export.json").read_text())
    scan = raw["scan"]
    x = scan_axis(scan)
    readouts = np.asarray(scan["ExperimentData"], dtype=float)[0]
    reference = readouts[0]
    signal = readouts[1]

    contrast = 1.0 - signal / reference
    interior = np.arange(1, len(x) - 1)
    trend = np.polyval(np.polyfit(x, contrast, 1), x)
    residual = contrast - trend
    depth_idx = int(interior[np.nanargmax(contrast[interior])])
    residual_idx = int(interior[np.nanargmax(residual[interior])])
    detrended_noise = mad(np.diff(residual)) / math.sqrt(2.0)

    linear_fit = linear_model(x, *np.polyfit(x - float(np.mean(x)), contrast, 1)[::-1])
    linear_bic = bic(contrast, linear_fit, 2)
    amp0 = max(float(residual[residual_idx]), 1e-4)
    offset0 = float(np.nanmedian(contrast))
    slope0 = 0.0
    center0 = float(x[residual_idx])

    lower = [-0.2, -5.0, 0.0, float(x[1]), 0.0015]
    upper = [0.4, 5.0, 0.6, float(x[-2]), 0.0500]
    lorentz_params, lorentz_bic = safe_fit(
        lorentzian_model,
        x,
        contrast,
        [offset0, slope0, amp0, center0, 0.010],
        (lower, upper),
    )
    gaussian_params, gaussian_bic = safe_fit(
        gaussian_model,
        x,
        contrast,
        [offset0, slope0, amp0, center0, 0.010],
        (lower, upper),
    )

    avg_sep, avg_min_depth, avg_min_snr = per_average_features(scan, x)
    return CaseFeatures(
        case_id=case_id,
        label=label,
        depth=float(contrast[depth_idx]),
        depth_frequency_ghz=float(x[depth_idx]),
        detrended_depth=float(residual[residual_idx]),
        detrended_snr=float(residual[residual_idx] / detrended_noise),
        avg_center_separation_mhz=avg_sep,
        avg_min_depth=avg_min_depth,
        avg_min_snr=avg_min_snr,
        lorentzian_amp=float(lorentz_params[2]) if lorentz_params is not None else float("nan"),
        lorentzian_delta_bic=float(linear_bic - lorentz_bic) if lorentz_bic is not None else float("nan"),
        gaussian_amp=float(gaussian_params[2]) if gaussian_params is not None else float("nan"),
        gaussian_delta_bic=float(linear_bic - gaussian_bic) if gaussian_bic is not None else float("nan"),
    )


def outcome(label: str, present: bool) -> str:
    if label == "present" and present:
        return "TP"
    if label == "absent" and not present:
        return "TN"
    if label == "absent" and present:
        return "FP"
    if label == "present" and not present:
        return "FN"
    raise ValueError(label)


def summarize(predictions: list[tuple[str, str, bool]]) -> dict[str, float | int]:
    counts = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}
    for _, label, present in predictions:
        counts[outcome(label, present)] += 1
    total = sum(counts.values())
    positives = counts["TP"] + counts["FN"]
    negatives = counts["TN"] + counts["FP"]
    return {
        **counts,
        "accuracy": (counts["TP"] + counts["TN"]) / total,
        "fpr": counts["FP"] / negatives if negatives else float("nan"),
        "fnr": counts["FN"] / positives if positives else float("nan"),
    }


def fixed_classifiers(feature: CaseFeatures) -> dict[str, bool]:
    return {
        "contrast_depth_ge_0p132": feature.depth >= 0.60 * EXPECTED_SETUP_CONTRAST,
        "contrast_depth_ge_0p10": feature.depth >= 0.10,
        "detrended_depth_snr": feature.detrended_depth >= 0.10 and feature.detrended_snr >= 2.5,
        "avg_consistent_depth_snr": (
            feature.depth >= 0.10
            and feature.avg_min_depth >= 0.05
            and feature.avg_min_snr >= 1.5
            and feature.avg_center_separation_mhz <= 25.0
        ),
        "lorentzian_bic_depth": (
            feature.lorentzian_amp >= 0.08 and feature.lorentzian_delta_bic >= 6.0
        ),
        "gaussian_bic_depth": (
            feature.gaussian_amp >= 0.08 and feature.gaussian_delta_bic >= 6.0
        ),
    }


def threshold_sweep(features: list[CaseFeatures]) -> list[dict[str, str | float | int]]:
    specs: list[tuple[str, str, np.ndarray]] = [
        ("depth", "depth", np.linspace(0.02, 0.22, 101)),
        ("detrended_snr", "detrended_snr", np.linspace(0.5, 6.0, 111)),
        ("lorentzian_delta_bic", "lorentzian_delta_bic", np.linspace(-10.0, 40.0, 101)),
        ("gaussian_delta_bic", "gaussian_delta_bic", np.linspace(-10.0, 40.0, 101)),
    ]
    rows: list[dict[str, str | float | int]] = []
    for feature_name, attr, thresholds in specs:
        for threshold in thresholds:
            predictions = [
                (f.case_id, f.label, bool(getattr(f, attr) >= threshold))
                for f in features
            ]
            summary = summarize(predictions)
            rows.append(
                {
                    "feature": feature_name,
                    "threshold": float(threshold),
                    **summary,
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    labels = load_labels()
    features = [
        extract_features(case_id, label)
        for case_id, label in sorted(labels.items())
    ]
    absent_depth_max = max(f.depth for f in features if f.label == "absent")
    present_depth_min = min(f.depth for f in features if f.label == "present")

    feature_rows = [f.__dict__ for f in features]
    write_csv(RESULTS / "non_llm_signal_features.csv", feature_rows)

    prediction_rows: list[dict[str, str | float | int]] = []
    summary_rows: list[dict[str, str | float | int]] = []
    classifier_names = list(fixed_classifiers(features[0]).keys())
    for classifier_name in classifier_names:
        predictions: list[tuple[str, str, bool]] = []
        for feature in features:
            pred = fixed_classifiers(feature)[classifier_name]
            predictions.append((feature.case_id, feature.label, pred))
            prediction_rows.append(
                {
                    "classifier": classifier_name,
                    "case_id": feature.case_id,
                    "gold_label": feature.label,
                    "prediction": "present" if pred else "absent",
                    "outcome": outcome(feature.label, pred),
                }
            )
        summary = summarize(predictions)
        summary_rows.append({"classifier": classifier_name, **summary})

    write_csv(RESULTS / "non_llm_signal_baseline_predictions.csv", prediction_rows)
    write_csv(RESULTS / "non_llm_signal_baseline_summary.csv", summary_rows)

    sweep_rows = threshold_sweep(features)
    write_csv(RESULTS / "non_llm_signal_threshold_sweep.csv", sweep_rows)

    best_rows = []
    for feature_name in sorted({str(r["feature"]) for r in sweep_rows}):
        rows = [r for r in sweep_rows if r["feature"] == feature_name]
        best_accuracy = max(rows, key=lambda r: (r["accuracy"], -r["FP"], -r["FN"]))
        zero_fn = [r for r in rows if r["FN"] == 0]
        best_zero_fn = min(zero_fn, key=lambda r: (r["FP"], -r["threshold"])) if zero_fn else None
        best_rows.append({"feature": feature_name, "selection": "best_accuracy", **best_accuracy})
        if best_zero_fn is not None:
            best_rows.append({"feature": feature_name, "selection": "zero_fn_min_fp", **best_zero_fn})
    write_csv(RESULTS / "non_llm_signal_threshold_sweep_best.csv", best_rows)

    lines = [
        "# Non-LLM pODMR Signal-Processing Baselines",
        "",
        "The baselines use the released raw pODMR exports and the same 96 gold-labeled cases.",
        "Readout 1 is treated as reference and readout 2 as signal.  The main contrast",
        "feature is `1 - signal/reference`, so a pODMR dip appears as a positive local",
        "feature.  Fixed-threshold baselines are not fitted to the labels.  The threshold",
        "sweep is reported separately as a diagnostic for how much separation is present",
        "in this dataset.",
        "",
        "## Fixed baselines",
        "",
        "| Classifier | TP | TN | FP | FN | Accuracy | FPR | FNR |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            "| {classifier} | {TP} | {TN} | {FP} | {FN} | {acc:.1f}% | {fpr:.1f}% | {fnr:.1f}% |".format(
                classifier=row["classifier"],
                TP=row["TP"],
                TN=row["TN"],
                FP=row["FP"],
                FN=row["FN"],
                acc=100 * float(row["accuracy"]),
                fpr=100 * float(row["fpr"]),
                fnr=100 * float(row["fnr"]),
            )
        )
    lines += [
        "",
        "## Contrast-depth separation",
        "",
        "The contrast-depth feature alone fully separates this dataset.  The largest",
        f"resonance-absent contrast depth is `{absent_depth_max:.9f}`, and the smallest",
        f"resonance-present contrast depth is `{present_depth_min:.9f}`.  Therefore any threshold",
        f"larger than `{absent_depth_max:.9f}` and no larger than `{present_depth_min:.9f}` gives 24 TP, 72 TN,",
        "0 FP, and 0 FN when the rule is `present` if `depth >= threshold`.",
        "",
        "## Threshold sweep diagnostics",
        "",
        "| Feature | Selection | Threshold | TP | TN | FP | FN | Accuracy | FPR | FNR |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in best_rows:
        lines.append(
            "| {feature} | {selection} | {threshold:.4g} | {TP} | {TN} | {FP} | {FN} | {acc:.1f}% | {fpr:.1f}% | {fnr:.1f}% |".format(
                feature=row["feature"],
                selection=row["selection"],
                threshold=float(row["threshold"]),
                TP=row["TP"],
                TN=row["TN"],
                FP=row["FP"],
                FN=row["FN"],
                acc=100 * float(row["accuracy"]),
                fpr=100 * float(row["fpr"]),
                fnr=100 * float(row["fnr"]),
            )
        )
    lines += [
        "",
        "## Interpretation",
        "",
        "A simple contrast-depth threshold is already very strong on this benchmark.",
        "This means the pODMR classification task is not evidence that an LLM is a",
        "better detector than conventional signal processing.  Instead, it supports a",
        "narrower claim: when the agent is asked to calculate the expected signal, its",
        "judgment moves toward the same physical comparison that a simple signal",
        "baseline exploits.",
        "",
    ]
    (RESULTS / "non_llm_signal_baseline_summary.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    print(RESULTS / "non_llm_signal_baseline_summary.md")


if __name__ == "__main__":
    main()
