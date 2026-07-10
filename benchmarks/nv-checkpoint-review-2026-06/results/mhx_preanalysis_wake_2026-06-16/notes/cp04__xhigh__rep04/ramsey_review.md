# Ramsey Review: det=1.5 MHz short-tau diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior Ramsey context: `evidence/e008.json` for the terminal det=1.0 MHz short-tau review; `evidence/e019.json`, `evidence/e021.json`, and `evidence/e022.json` for the det-shift rationale and targets; `evidence/e009.py` as the local prior-analysis pattern.
- New measurement data: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Local outputs created: `analyze_ramsey_det1p5.py`, `ramsey_analysis_det1p5.json`, `ramsey_det1p5_diagnostic.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey_det1p5.py`.
- Verified the raw-export axis contract: the combined `ExperimentData` equals the mean of `ExperimentDataEachAvg` for both readouts. The run used snake scan order saved back in tau order.
- Checked acquisition health: completed job `nv23_ramsey_20260514_015423_auto_ramsey`, `12 x 90000` repetitions, `1.08e6` shots per tau point, `tau=0.048..1.968 us` in 41 points, final counts `44.796 kcps`, no stop request, no monitor error.
- Ran per-average common-mode and ratio robust-z drift checks; no averages were flagged.
- Computed point-wise `signal/reference`, raw signal, and signal divided by a fitted reference line; detrended FFT amplitudes; least-squares sinusoid screens with a linear baseline; target-frequency amplitudes at the programmed carrier, prior fixed component, det-tracking prediction, and 13C sideband positions; and descriptive damped-sinusoid grid fits.
- Plot file sanity check: `ramsey_det1p5_diagnostic.png` exists, is `1440 x 1920`, and is nonblank by pixel variance.

## Quantitative highlights

- Sampling limits: FFT bin spacing is `0.508 MHz`, nominal `1/span` resolution is `0.521 MHz`, and Nyquist is `10.42 MHz`. The `1.5 MHz` programmed carrier and `1.692 MHz` det-tracking prediction are closer than the nominal resolution, so they are not cleanly separable in this short window.
- Noise/variation: median per-point SEM is `0.711 kcps` for raw signal and `0.0126` in ratio. The ratio residual peak-to-peak after linear baseline is `0.133`; early `tau <= 0.75 us` ratio peak-to-peak is `0.134`.
- Prior fixed-component test: the previous det=1.0 MHz short-tau top component was near `1.192 MHz` with ratio LS amplitude `0.0363`. In this det=1.5 MHz run, the amplitude at `1.192 MHz` drops to `0.00511` ratio and `0.474 kcps`, with only `R2` improvement `0.0167` in the ratio view.
- New ratio-screen maximum: the all-tau ratio screen peaks broadly near `1.623 MHz` with ratio amplitude `0.02547` and `R2` improvement `0.430`.
- Target amplitudes: programmed `1.5 MHz` has ratio amplitude `0.02399` and raw-signal amplitude `1.128 kcps`; det-tracking `1.692 MHz` has ratio amplitude `0.02505` and raw-signal amplitude `1.225 kcps`. These are similar and cannot be distinguished strongly on this grid.
- Readout dependence: raw signal and signal-over-reference-line screens are strongest near `0.882 MHz`, not near the ratio-screen `1.623 MHz` maximum. Per-average top frequencies are inconsistent: `[1.938, 1.543, 0.870, 0.886, 1.751, 0.792, 0.897, 1.201, 0.799, 1.662, 0.250, 1.712] MHz`.
- 13C sidebands are not dominant. Programmed-det sidebands at `1.115/1.885 MHz` have ratio amplitudes `0.0108/0.0173`; det-tracking sidebands at `1.307/2.077 MHz` have ratio amplitudes `0.00953/0.00614`.
- Descriptive damped fits prefer non-target, short-T2* solutions: ratio view `0.692 MHz`, `T2* ~0.5 us`; raw signal/reference-line view `0.816 MHz`, `T2* ~0.7 us`. These are diagnostic fits only.

## Plausible interpretation

The det-shift run argues against simply carrying forward the prior `~1.192 MHz` component as a fixed artifact, because that component is strongly suppressed after changing det from `1.0 MHz` to `1.5 MHz`. However, the new evidence is still not claim-grade Ramsey physics. The strongest ratio feature is broad and sits between the programmed carrier and the det-tracking prediction, while raw-signal and reference-line-normalized views prefer a different `~0.88 MHz` component. Per-average frequency screens are also inconsistent. A weak det-related Ramsey response may be present, but the present data do not isolate a robust carrier or decay envelope.

## Claims not yet supported

- A numeric T2* for r03 is not supported by this measurement.
- Nearby 13C coupling is not supported; neither programmed-det nor det-tracking sidebands are dominant or reproducible across views.
- The new `~1.62 MHz` ratio-screen feature should not be claimed as the physical Ramsey carrier, because `1.5 MHz` and `1.692 MHz` are unresolved in this time window and the raw-signal/readout-normalized views disagree.
- The descriptive short-T2* fits should not be promoted as physical parameters.

## Recommended next action

Do not run another blind same-style Ramsey repeat. If the project continues experimentally on r03, use a deliberately artifact-sensitive check such as phase-cycled/quadrature Ramsey or another alternate protocol that can separate true Ramsey phase evolution from readout normalization and early-time transients. If that is not available, close the current r03 Ramsey/T2*/13C branch as unsupported under the present conditions while preserving the aligned-NV conclusion.
