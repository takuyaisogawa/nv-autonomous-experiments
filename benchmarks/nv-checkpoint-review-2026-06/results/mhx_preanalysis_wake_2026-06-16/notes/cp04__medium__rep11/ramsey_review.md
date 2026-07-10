# Ramsey review: det=1.5 MHz short-tau shift check

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective and current state.
- `md/knowledge.md`, `md/memory.md`: local Ramsey/readout cautions and analysis posture.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: submitted job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control.
- `evidence/e008.json`: previous terminal det=1.0 MHz short-tau review.
- `evidence/e019.json`, `evidence/e021.json`: det-shift rationale and target frequencies.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Generated `ramsey_analysis_summary.json` and `ramsey_det1p5_review.png`.
- The script checks:
  - raw export shape and axis contract: `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; averaging over the stored-average axis reconstructs `ExperimentData`.
  - combined reference, Ramsey signal, point-wise signal/reference ratio, and signal over a fitted reference line.
  - per-point SEM over 12 stored averages.
  - linear-baseline residual size, early-time peak-to-peak transient size, FFT bin spacing, target-frequency least-squares amplitudes, and exploratory frequency screens.
  - per-average top frequency consistency.

Key numeric checks:

- Run completed: `12 x 90000` repetitions, 41 tau points from `0.048` to `1.968 us`, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, terminal final counts `44.796 kcps`, no stop request, no monitor error.
- Sampling: tau step `48 ns`, FFT bin spacing `0.508 MHz`, Nyquist `10.42 MHz`. The short time span limits frequency discrimination.
- Median per-point SEM: raw signal `0.711 kcps`, ratio `0.0126`.
- Combined trace variation after linear baseline: raw signal peak-to-peak `6.29 kcps`, ratio peak-to-peak `0.133`; first `0.75 us` remains large at `6.46 kcps` and `0.134` ratio.
- Previous det=1.0 MHz top was near `1.192 MHz` with ratio LS amplitude `0.0363` and raw-signal amplitude `1.684 kcps`.
- In the new det=1.5 MHz run:
  - ratio screen top is near `1.623 MHz`, ratio amplitude `0.0255`, R2 improvement `0.430`.
  - programmed `1.500 MHz` carrier: ratio amplitude `0.0240`, raw-signal amplitude `1.128 kcps`.
  - predicted det-tracking carrier from the prior `1.192 MHz` feature: `1.692 MHz`, ratio amplitude `0.0250`, raw-signal amplitude `1.225 kcps`.
  - prior fixed-artifact control `1.192 MHz`: ratio amplitude only `0.0051`, raw-signal amplitude `0.474 kcps`.
  - programmed 13C sidebands at `1.115/1.885 MHz`: ratio amplitudes `0.0108/0.0173`.
  - predicted det-tracking 13C sidebands at `1.307/2.077 MHz`: ratio amplitudes `0.0095/0.0061`.
- Raw-signal-only exploratory screen is strongest near `0.882 MHz`, not near the det-tracking band.
- Per-average ratio top frequencies are scattered: approximately `[1.938, 1.544, 0.870, 0.886, 1.752, 0.792, 0.898, 1.202, 0.800, 1.662, 0.250, 1.712] MHz`.

## Plausible interpretation

The det-shift check is analyzable and useful. In the normalized ratio view, the prior fixed `~1.192 MHz` feature is strongly suppressed, while the strongest combined component moves into the `~1.62 MHz` band. That is qualitatively closer to the det-tracking prediction of `~1.692 MHz` than to a fixed `1.192 MHz` artifact, so the new data argue against simply promoting the earlier `1.192 MHz` component as a fixed repeatable Ramsey/13C feature.

The result is still not claim-grade for T2star or 13C. The short span gives only `~0.508 MHz` FFT-bin spacing, the ratio top is broad relative to the planned discrimination, raw signal alone prefers `~0.882 MHz`, and stored averages do not agree on a common top frequency. The most defensible reading is: there is a weak, readout-normalized det-dependent Ramsey-like component, but the raw/readout-aware evidence is not coherent enough to fit a physical decay or sideband model.

## Claims not yet supported

- A numeric T2star for r03.
- Nearby 13C coupling or sidebands.
- A clean physical carrier at exactly `1.5 MHz` or exactly the predicted `1.692 MHz`.
- That the residual structure is purely NV Ramsey signal rather than a mix of Ramsey contrast, readout normalization, early-time transient, and baseline/reference behavior.
- That more blind Ramsey averaging on the same short-tau design will resolve the ambiguity.

## Recommended next action

Do not run another blind Ramsey repeat. Treat the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey conditions unless a deliberately different protocol is chosen. The next project action should be a bridge-free synthesis/closeout note comparing all four r03 Ramsey runs, followed by either:

1. close the current r03 Ramsey/T2star/13C claim as unsupported under these conditions, while preserving the aligned-NV claim; or
2. switch to an alternate, explicitly justified protocol aimed at a more robust coherence/13C test rather than another same-family short-tau Ramsey repeat.
