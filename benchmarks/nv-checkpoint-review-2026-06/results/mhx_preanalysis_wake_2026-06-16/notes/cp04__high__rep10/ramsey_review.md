# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, with prior Ramsey conclusions and the det-shift success criteria.
- New measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison: `evidence/e008.json`, the terminal det=1.0 MHz short-tau Ramsey review with top combined ratio component near 1.192 MHz.
- Local outputs created: `analyze_ramsey_local.py`, `ramsey_analysis_summary.json`, `ramsey_det1p5_review.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey_local.py`.
- Verified raw-export axis contract by averaging `ExperimentDataEachAvg` back to `ExperimentData`.
- Used readout1 as reference and readout2 as Ramsey signal, consistent with the local project context for `ramsey.xml` with `full_experiment=0`.
- Computed point-wise `signal/reference`, signal divided by a fitted reference line, per-point SEM over 12 averages, FFT of linear-detrended ratio/signal, and least-squares sinusoid screens from 0.25 to 2.25 MHz.
- Checked target frequencies:
  - programmed det carrier: 1.500 MHz,
  - programmed 13C sidebands: 1.115 and 1.885 MHz,
  - prior fixed-feature control: 1.192 MHz,
  - det-tracking prediction from prior 1.192 MHz feature: 1.692 MHz,
  - sidebands around that shifted feature: 1.307 and 2.077 MHz.
- Ran descriptive damped-sinusoid grid fits only as diagnostics, not as promoted T2* estimates.

## Quantitative summary

- Run completed: `nv23_ramsey_20260514_015423_auto_ramsey`, final counts 44.796 kcps, status completed, no stop request, monitor last error empty.
- Acquisition: tau 0.048 to 1.968 us, 41 points, 48 ns step, 12 averages x 90000 repetitions = 1.08e6 shots/tau. FFT bin spacing is about 0.508 MHz and nominal 1/span resolution is about 0.521 MHz.
- Median per-point SEM: signal 0.711 kcps, ratio 0.0126. Signal linear-residual peak-to-peak is 6.29 kcps; ratio linear-residual peak-to-peak is 0.133. In the first 0.75 us, signal peak-to-peak is 6.46 kcps and ratio peak-to-peak is 0.134.
- Local common-mode count check found no average with >15% drop vs the median common-mode count, but this is not the same as the missing MATLAB drift-analysis artifact. Per-average top-frequency screens are inconsistent.
- Combined ratio LS screen top over all tau is 1.623 MHz, ratio amplitude 0.02547, raw-signal amplitude 1.252 kcps, residual R2 improvement 0.430.
- At the programmed 1.500 MHz carrier: ratio amplitude 0.02399, raw-signal amplitude 1.128 kcps, residual R2 improvement 0.359.
- At the predicted det-tracking carrier 1.692 MHz: ratio amplitude 0.02505, raw-signal amplitude 1.225 kcps, residual R2 improvement 0.411.
- At the prior fixed 1.192 MHz feature: ratio amplitude 0.00511 and residual R2 improvement 0.0167, so the old fixed feature is not reproduced in this run.
- Programmed-sideband checks are weaker than the main/top components: 1.115 MHz ratio amplitude 0.01076, 1.885 MHz ratio amplitude 0.01732.
- Sidebands around the shifted 1.692 MHz candidate are also weak: 1.307 MHz ratio amplitude 0.00953, 2.077 MHz ratio amplitude 0.00614.
- The all-tau top is not robust to early-time exclusion: skipping tau <= 0.2 us moves the strongest ratio screen to about 0.746 MHz with amplitude about 0.0207.
- Descriptive damped fits prefer ratio-view 0.678 MHz with T2* 0.469 us, and raw-signal 0.818 MHz with T2* 0.717 us. These do not align with the programmed carrier or det-tracking carrier, so they are diagnostic only.

## Plausible interpretation

The det=1.5 MHz run is analyzable and argues against a strictly fixed 1.192 MHz artifact, because that component is weak here. However, it does not cleanly validate the physical det-tracking carrier hypothesis either. The strongest all-tau ratio screen is near 1.623 MHz, close to but not exactly at the 1.692 MHz prediction, and comparable to the programmed 1.500 MHz and 1.692 MHz target amplitudes within a short 1.92 us window with about 0.52 MHz nominal frequency resolution. The early-time transient still dominates enough that excluding tau <= 0.2 us changes the top screen to about 0.746 MHz.

The most conservative interpretation is: r03 remains an aligned, usable NV candidate, but the Ramsey data under this protocol show an early-time oscillatory/transient feature whose physical assignment is still ambiguous. The det-shift check is suggestive of some det dependence but is not sufficient for a supported carrier, T2*, or 13C sideband model.

## Claims not yet supported

- A numeric T2* for r03 from these Ramsey data.
- Nearby 13C coupling from Ramsey Fourier/sideband structure.
- A clean physical Ramsey carrier at 1.500 MHz or 1.692 MHz.
- Promotion of the descriptive damped-fit T2* values as physical parameters.
- A claim that the prior 1.192 MHz feature was purely a fixed artifact; this run only shows it did not persist as a fixed dominant feature.

## Recommended next action

Do not enqueue another blind Ramsey repeat on r03. Make a bridge-free branch decision from the accumulated Ramsey evidence: either close the r03 Ramsey/T2*/13C branch as unsupported under the current Ramsey protocol, or switch to a deliberately different protocol/diagnostic if the project needs more evidence before closeout. The immediate next action should be a concise synthesis/closeout note comparing all four Ramsey datasets against the original T2* and 13C objectives.
