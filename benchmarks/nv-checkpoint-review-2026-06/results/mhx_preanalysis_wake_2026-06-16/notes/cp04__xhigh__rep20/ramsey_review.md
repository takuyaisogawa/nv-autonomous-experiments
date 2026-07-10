# Ramsey Review: r03 det-shift short-tau run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior Ramsey context: `evidence/e008.json` terminal det=1.0 MHz short-tau review and `evidence/e019.json` det-shift model/plan.
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Local outputs created here: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, and `ramsey_detshift_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified raw export axis contract: `ExperimentDataEachAvg` averages back to `ExperimentData`, with shape `[slice, average, readout, tau]`.
- Checked run health: job completed, final counts `44.796 kcps`, no monitor error, no stop request. Scan was `tau = 0.048..1.968 us`, `41` points, `48 ns` spacing, `12 x 90000 = 1.08e6` shots per tau point.
- Estimated point uncertainty from stored averages: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`.
- Ran a local scan-order-aware drift residual check using `ScanOrderEachAvg` snake order; no averages were flagged by the residual half-delta rule.
- Ran detrended least-squares and FFT screens at the planned targets: programmed carrier `1.5 MHz`, programmed 13C sidebands `1.115/1.885 MHz`, predicted det-tracking carrier `1.692 MHz`, predicted det-tracking sidebands `1.307/2.077 MHz`, and prior artifact-control frequency `1.192 MHz`.
- Key LS results in point-wise ratio view: strongest all-tau component `1.623 MHz`, amplitude `0.02547`; programmed `1.5 MHz` amplitude `0.02399`; predicted det-tracking `1.692 MHz` amplitude `0.02505`; prior `1.192 MHz` control amplitude `0.00511`.
- Raw/readout-aware caveat: raw signal and signal divided by fitted reference line both screened strongest near `0.882 MHz`; skipping tau `<=0.2 us` moved the ratio screen top to `0.746 MHz`.

## Plausible interpretation

The det=1.5 MHz run is analyzable and does not show a hard acquisition anomaly. The fixed prior `~1.192 MHz` component is weak in this run, and the point-wise ratio screen moved upward toward the planned det-tracking target near `1.692 MHz`. That makes det tracking plausible as an empirical effect.

It is still not a supported Ramsey-carrier model. The short `1.92 us` span gives coarse FFT spacing around `0.51 MHz`, the target amplitudes are only about twice the median ratio SEM, raw signal/fitted-reference-line views prefer `~0.882 MHz`, and per-average frequency screens are inconsistent. The data are best treated as suggestive diagnostic evidence, not a T2star/13C result.

## Claims not yet supported

- A numeric `T2star` for r03 from the Ramsey data.
- A nearby `13C` coupling assignment from Ramsey sidebands.
- A clean det-following Ramsey carrier assignment for the prior `~1.19 MHz` feature.
- Sub-grid precision for the Ramsey carrier or microwave resonance.
- A negative claim that r03 has no measurable coherence; the present issue is model/readout consistency, not simple absence of all structure.

## Recommended next action

Do not fit or report `T2star` from this run, and do not run another blind same-style Ramsey repeat. Next, do a bridge-free synthesis of all r03 Ramsey datasets and choose either a targeted carrier-validation diagnostic that resolves the raw-vs-ratio conflict or an alternate coherence protocol/readout. Keep `T2star` and `13C` as unsupported until a raw/readout-aware det-tracking carrier or sideband model is established.
