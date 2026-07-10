# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: current project objective and prior decisions.
- `md/memory.md`, `md/knowledge.md`: local project practice, especially raw/readout-aware Ramsey interpretation and normalization cautions.
- `evidence/e019.json`: model plan for the det-shift Ramsey diagnostic and frequency targets.
- `evidence/e008.json`: prior terminal short-tau det=1.0 MHz Ramsey review for comparison.
- `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json` through `measurement/m005.json`: job, result, status, and control metadata for `nv23_ramsey_20260514_015423_auto_ramsey`.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_analysis.json`: numerical review output.
  - `ramsey_detshift_review.png`: diagnostic plot artifact.
- Verified the raw-export axis contract: `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; averaging per-average readouts reconstructs `ExperimentData`.
- Used readout 1 as reference and readout 2 as Ramsey signal, consistent with the local `full_experiment=0` Ramsey protocol notes and job metadata.
- Checked terminal metadata: run completed, final counts `44.796 kcps`, `stop_requested=false`, monitor `last_error=""`, safe shutdown true.
- Scan/grid:
  - `tau = 0.048..1.968 us`, step `0.048 us`, 41 points.
  - `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`.
  - `12 x 90000` repetitions = `1.08e6` shots per tau point.
  - FFT bin spacing `0.508 MHz`; nominal `1/span` resolution `0.521 MHz`; Nyquist `10.42 MHz`.
- Noise/scale checks:
  - Median signal SEM across averages `0.711 kcps`.
  - Median ratio SEM `0.0126`.
  - Signal linear-residual peak-to-peak `6.29 kcps`; early `tau <= 0.75 us` signal peak-to-peak `6.46 kcps`.
  - Ratio linear-residual peak-to-peak `0.133`; early ratio peak-to-peak `0.134`.
- Least-squares sinusoid screens after a linear baseline:
  - Point-wise ratio all-tau top: `1.623 MHz`, amplitude `0.0255`, residual improvement `0.430`.
  - Raw signal all-tau top: `0.882 MHz`, amplitude `1.533 kcps`, residual improvement `0.577`.
  - Signal over fitted reference-line top: `0.882 MHz`, amplitude `0.0319`, residual improvement `0.576`.
  - Ratio after skipping `tau <= 0.2 us` top: `0.746 MHz`, amplitude `0.0207`, residual improvement `0.421`.
- Target checks:
  - Programmed carrier `1.500 MHz`: ratio amp `0.0240`, raw amp `1.128 kcps`.
  - Det-tracking carrier target `1.692 MHz`: ratio amp `0.0250`, raw amp `1.225 kcps`.
  - Previous fixed-artifact control `1.192 MHz`: ratio amp `0.00511`, raw amp `0.474 kcps`.
  - Programmed 13C sidebands `1.115/1.885 MHz`: ratio amps `0.0108/0.0173`.
  - Det-tracking 13C sidebands `1.307/2.077 MHz`: ratio amps `0.00953/0.00614`.
- Per-average ratio frequency-screen tops were inconsistent: approximately `1.938, 1.543, 0.870, 0.886, 1.751, 0.792, 0.897, 1.201, 0.799, 1.662, 0.250, 1.712 MHz`.
- Descriptive damped-grid fits were also view-dependent:
  - Ratio fit: `0.674 MHz`, `T2* ~0.461 us`.
  - Raw signal and fitted-reference-line fits: `~0.82 MHz`, `T2* ~0.739 us`.
  - These are diagnostics only, not promoted parameters.

## Plausible interpretation

The measurement is valid terminal evidence and has enough SNR to show structured tau dependence, but it does not cleanly support a Ramsey carrier model. The point-wise ratio feature near `1.623 MHz` is closer to the planned det-tracking carrier target (`1.692 MHz`) than to the fixed previous `1.192 MHz` control, and the old `1.192 MHz` feature is weak in this ratio view. However, the raw signal and fitted-reference-line normalization both peak near `0.882 MHz`, not near `1.5 MHz` or `1.692 MHz`. Since the supported analysis posture requires raw/readout-aware agreement, the det-shift result is ambiguous rather than claim-grade.

The large early-time transient remains comparable to or larger than the target component amplitudes. The short time window also gives coarse FFT resolution, so interpolated LS frequency peaks should not be treated as precise frequency assignments.

The new run weakens a simple "fixed 1.192 MHz artifact" explanation in the point-wise ratio view, but it does not replace it with a supported physical det-tracking carrier. A normalization/reference interaction, short-tau transient, sequence/readout artifact, or unresolved baseline behavior remains plausible.

## Claims not yet supported

- No numeric T2* is supported from this run.
- No nearby 13C conclusion is supported.
- The `1.623 MHz` ratio feature is not yet a supported physical Ramsey carrier.
- The `1.692 MHz` det-tracking hypothesis is not confirmed across raw/readout-aware views.
- The sideband targets are not supported; neither programmed nor det-tracking 13C sidebands are dominant or consistent.
- The descriptive damped-grid fits are not supported physical T2* fits.
- This result does not invalidate the existing aligned-r03 pODMR conclusion; it only limits the Ramsey/T2*/13C conclusion under the current Ramsey conditions.

## Recommended next action

Do not run another blind same-style Ramsey repeat. Treat the r03 Ramsey branch as non-claim-grade under the current conditions unless the project deliberately switches to a targeted alternate route. If continuing, first use an alternate calibration/protocol decision that can establish a raw/readout-aware carrier signal before fitting T2* or assigning 13C sidebands; otherwise close the Ramsey/T2*/13C finding for r03 as unsupported under these conditions.
