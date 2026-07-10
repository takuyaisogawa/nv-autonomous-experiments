# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Local outputs created for this review: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed raw array contract: `ExperimentData` shape `[1,2,41]`, `ExperimentDataEachAvg` shape `[1,20,2,41]`, and the 20-average mean exactly matches `ExperimentData`.
- Confirmed run metadata: job `nv23_ramsey_20260514_055148_auto_ramsey`, run `1DExp-seq-ramsey-vary-tau-2026-05-14-055200`, status completed, safe shutdown true, no stop request, empty monitor error, final counts `43.433 kcps`.
- Confirmed scan: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us`, `41` points, `0.200 us` step, `20 x 50000` shots, `1.0e6` shots/tau, nominal frequency resolution `125 kHz`, Nyquist `2.5 MHz`.
- Performed simple scan-order-aware drift checks using stored `snake` order and per-average common-mode readout. No averages were flagged by the robust/common-mode threshold used here. Common-mode by-average range was `39.56..52.64 kcps`; within-average acquisition-order first/second-half common-mode changes ranged from `-4.0%` to `+6.9%`.
- Compared raw signal, point-wise signal/reference, and signal/linear-reference-normalized views using FFT and least-squares sinusoid screens.
- Checked full-span and skip-first-4-points screens at the programmed carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior short-tau feature `1.192 MHz`, prior det-shift top `1.623 MHz`, and prior det-tracking target `1.692 MHz`.

## Plausible interpretation

- The measurement is analyzable and does not show a hard bridge/counting failure.
- It still does not support the planned Ramsey carrier/sideband model. The strongest full-span LS component is near `2.27 MHz` in raw signal, point-wise ratio, and linear-reference-normalized signal; skip-first-4-points gives essentially the same top. This is not the programmed `1.5 MHz` carrier or the expected `1.115/1.885 MHz` 13C sidebands.
- The programmed-carrier amplitude is weak relative to measured scatter: point-wise ratio amplitude `0.01575`, about `1.36x` median ratio SEM (`0.01161`); raw-signal carrier amplitude `0.705 kcps`, below median raw-signal SEM (`0.850 kcps`); linear-reference-normalized carrier amplitude `0.01447`, about `0.83x` its median SEM.
- 13C sideband checks are weaker: point-wise ratio amplitudes `0.00277` at `1.115 MHz` and `0.00961` at `1.885 MHz`, both below median ratio SEM.
- Per-average top frequencies are mixed rather than locked to the programmed carrier: ratio-view tops include low-frequency, carrier-near, sideband-near, and high-frequency values. This argues against promoting a single coherent Ramsey frequency or decay envelope from the average trace.
- The empirical `2.27 MHz` feature should be treated as non-claim-grade exploratory structure, not as a physical conclusion, because it is near the high-frequency end of the usable band and lacks the project/model support expected for carrier or 13C sidebands.

## Claims not yet supported

- A numeric T2star fit from this refreshed-center Ramsey run.
- A resolved nearby 13C conclusion from `1.115/1.885 MHz` sidebands.
- Promotion of the `2.27 MHz` empirical component as a physical Ramsey frequency.
- Sub-grid microwave-frequency precision beyond the refreshed pODMR grid-supported `3.8765 GHz` center.

## Recommended next action

Do not run another blind same-protocol Ramsey repeat on r03. The refreshed-center, higher-shot, long-span measurement remained non-claim-grade. The next project step should be either an alternate targeted protocol/diagnostic that tests why the Ramsey carrier is not robust, or a supported negative/unsupported r03 Ramsey/T2star/13C conclusion under the current conditions.
