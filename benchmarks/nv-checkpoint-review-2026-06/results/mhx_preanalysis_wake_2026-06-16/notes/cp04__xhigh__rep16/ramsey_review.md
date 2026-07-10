# Ramsey Review: r03 det-shift short-tau run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New completed measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Relevant prior context/evidence: `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review, `evidence/e019.json` det=1.5 MHz model/target plan, and `evidence/e009.py` as the prior review-script pattern.
- Local outputs created: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, and `ramsey_detshift_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified raw axis contract: `ExperimentDataEachAvg` as `[scan, avg, readout, point]` averages back to `ExperimentData`.
- Checked terminal metadata: job `nv23_ramsey_20260514_015423_auto_ramsey` completed, safe shutdown OK, final counts `44.796 kcps`, monitor error empty, no stop request.
- Confirmed protocol/grid: `ramsey.xml`, `mw_freq=3.8759 GHz`, `det=1.5 MHz`, `tau=0.048..1.968 us`, `41` points, `12 x 90000` repetitions, `1.08e6` shots per tau point, nominal frequency resolution about `0.521 MHz`, Nyquist about `10.42 MHz`.
- Ran scan-order-aware local drift approximation using snake `ScanOrderInfo.order_each_avg`; no averages exceeded the `0.15` drop threshold.
- Computed raw signal, point-wise ratio, signal-over-fitted-reference-line views; per-point median SEM was `0.711 kcps` for signal and `0.0126` for ratio.
- Ran detrended FFT and least-squares sinusoid screens at the programmed `1.5 MHz` carrier, expected `13C` sidebands, predicted det-tracking carrier `1.692 MHz`, predicted det-tracking sidebands, fixed prior artifact-control `1.192 MHz`, and first-scout `0.884 MHz`.
- Ran descriptive damped-sinusoid grid fits only as diagnostics; they were not promoted to physical T2star values.

## Plausible interpretation

- The measurement is terminal and analyzable; there is no hard run anomaly in the local snapshot.
- The prior fixed `~1.192 MHz` artifact-control component is weak in the new det=1.5 MHz run: point-wise ratio LS amplitude `0.0051`, R2 improvement `0.017`.
- The point-wise ratio screen moves upward: top all-tau component `1.623 MHz`, ratio amplitude `0.0255`, R2 improvement `0.430`. The planned det-tracking target `1.692 MHz` is nearly as strong: ratio amplitude `0.0250`, R2 improvement `0.411`. This is qualitatively consistent with the dominant component not being fixed at `1.192 MHz`.
- The result is not claim-grade for a Ramsey carrier: raw signal and signal-over-reference-line screens are dominated near `0.882 MHz`, while point-wise ratio prefers `1.62 MHz`; excluding early tau points shifts the top component toward `0.75..0.81 MHz`. The frequency assignment is therefore analysis-view and mask dependent.
- The programmed carrier at `1.5 MHz` is present at comparable but not dominant scale: ratio amplitude `0.0240`, raw-signal amplitude `1.128 kcps`.
- No `13C` sideband pair is supported. Programmed sidebands at `1.115/1.885 MHz` and det-tracking sidebands at `1.307/2.077 MHz` are not dominant or consistent across readout-aware views.

## Claims that are not yet supported

- A numeric T2star for r03.
- A nearby `13C` conclusion from Ramsey FFT/sidebands.
- A precise physical Ramsey carrier frequency from this short-tau det-shift run.
- That the empirical oscillatory structure is purely physical rather than mixed with baseline/readout/transient effects.

## Recommended next action

Stop blind Ramsey repeats on r03. Use this det-shift run as evidence against a fixed `1.192 MHz` artifact, but not as a T2star/13C conclusion. Next, do a branch-level decision: either switch to an alternate protocol with clearer phase/carrier discrimination, such as a Hahn/CPMG-style T2 baseline or phase-readout 13C spectroscopy, or close the r03 Ramsey/13C branch as unsupported under the current Ramsey conditions.
