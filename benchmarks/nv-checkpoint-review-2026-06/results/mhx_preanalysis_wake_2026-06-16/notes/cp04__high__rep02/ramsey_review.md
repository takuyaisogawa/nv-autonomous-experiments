# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: completed bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: bridge control state.
- Prior comparison context:
  - `evidence/e008.json`: terminal det=1.0 MHz short-tau Ramsey review.
  - `evidence/e019.json`, `evidence/e021.json`, `evidence/e022.json`, `evidence/e023.json`, `evidence/e024.json`: det-shift model/intent/submit/start context.
- Local outputs created here:
  - `analyze_ramsey_detshift.py`
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_analysis.png`

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified the raw export axis contract by reconstructing combined `ExperimentData` from `ExperimentDataEachAvg`; max absolute reconstruction error was `1.42e-14 kcps`, consistent with `[scan, avg, readout, point]`.
- Computed raw reference/signal, signal/reference, and signal divided by a fitted reference line.
- Computed per-point SEM across 12 stored averages.
- Ran exploratory least-squares sine screens from `0.2..3.0 MHz`, plus target checks at:
  - programmed det: `1.500 MHz`
  - det-tracking prediction from the prior `~1.192 MHz` feature: `1.692 MHz`
  - prior fixed-feature control: `1.192 MHz`
  - expected 13C sidebands for the det-tracking hypothesis: `1.307 MHz` and `2.076 MHz`
- Ran coarse per-average frequency screens.
- Ran FFT checks; the short `1.92 us` span gives coarse `~0.508 MHz` bin spacing, so FFT bins were used only as a sanity check.
- Ran descriptive damped-sinusoid grid fits as diagnostics only, not as promoted T2star estimates.

## Key quantitative checks

- New run completed: `nv23_ramsey_20260514_015423_auto_ramsey`, status `completed`, final counts `44.796 kcps`, no stop request, no monitor error in terminal status.
- Scan: `tau = 48 ns..1.968 us`, `41` points, `12` averages, `90000` repetitions per average, `1.08e6` shots per tau point, snake scan order.
- Readout levels: median reference `47.91 kcps`, median signal `44.16 kcps`.
- Per-point uncertainty: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`.
- Early-time structure is visible: raw signal peak-to-peak over the first `0.75 us` is `6.46 kcps`; signal/reference peak-to-peak is `0.134`.
- Stored-average count sanity: signal-average means range `39.64..46.92 kcps`; reference-average means range `44.59..50.60 kcps`. Average 7 is low by about `10.7%` in signal and `8.3%` in reference relative to median, but this is not a count collapse. No MATLAB scan-order drift-analysis output for the new run was present in the checkpoint.
- Exploratory LS screens:
  - Raw signal top: `0.882 MHz`, amplitude `1.53 kcps`, linear-baseline residual improvement `0.577`.
  - Signal/reference top: `1.623 MHz`, amplitude `0.0255`, improvement `0.430`.
  - Signal over fitted reference line top: `0.882 MHz`, amplitude `0.0319`, improvement `0.576`.
- Target LS amplitudes:
  - `1.500 MHz` programmed det: raw `1.13 kcps`, ratio `0.0240`.
  - `1.692 MHz` det-tracking prediction: raw `1.22 kcps`, ratio `0.0250`.
  - `1.192 MHz` prior fixed-feature control: raw `0.474 kcps`, ratio `0.0051`.
  - `1.307/2.076 MHz` 13C sidebands: raw `0.266/0.251 kcps`, ratio `0.0095/0.0062`.
- Per-average top frequencies are scattered. Coarse ratio-screen tops were `1.94, 1.545, 0.87, 0.885, 1.75, 0.79, 0.895, 1.2, 0.8, 1.66, 0.2, 1.71 MHz`.
- Descriptive damped fits are view-dependent and not target-consistent:
  - raw signal: `0.820 MHz`, `T2star ~0.72 us`
  - signal over fitted reference line: `0.820 MHz`, `T2star ~0.72 us`
  - point-wise ratio: `0.685 MHz`, `T2star ~0.48 us`

## Plausible interpretation

The new det=1.5 MHz Ramsey run is valid and analyzable, and it contains real early-time structure above the per-point SEM. The prior `~1.192 MHz` point-wise ratio feature does not remain strong as a fixed feature in the new point-wise ratio view, and the point-wise ratio screen shifts upward toward `~1.62 MHz`, near the `1.692 MHz` det-tracking prediction.

That partial shift is suggestive but not claim-grade. The raw signal and fitted-reference normalization are still dominated by `~0.88 MHz`, the descriptive damped fits prefer still lower frequencies and short apparent decays, and the stored-average frequency screens do not cluster tightly. The safest interpretation is that the Ramsey data show a repeatable short-tau transient whose apparent frequency depends on normalization/baseline treatment, not a clean, supported Ramsey carrier.

## Claims that are not yet supported

- A numeric T2star value for r03 is not supported by this run.
- A nearby 13C coupling claim is not supported; the expected `1.307/2.076 MHz` sidebands are weak and not dominant.
- A clean det-following Ramsey carrier is not supported. The point-wise ratio view is compatible with partial det tracking, but raw/readout-aware checks and per-average consistency do not support promoting it.
- The data should not be dismissed as pure noise; the early-time transient is above SEM, but its physical assignment is unresolved.

## Recommended next action

Do not run another blind Ramsey repeat on r03 under the same scheme. Make a branch-level decision: either close the current r03 Ramsey/T2star/13C line as unsupported under these Ramsey conditions, or switch to an alternate, explicitly modeled protocol after fresh tracking/frequency checks. If continuing experimentally, the next measurement should be designed to separate a real coherence signal from readout-normalization and short-tau transient effects rather than accumulating more of the same Ramsey data.
