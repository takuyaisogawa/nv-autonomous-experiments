# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior comparator/model context: `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review; `evidence/e019.json` det-shift design.
- New terminal measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Local outputs created: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, `ramsey_detshift_review.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified raw-export axis contract: `ExperimentDataEachAvg` averages back to `ExperimentData` for readout1 reference and readout2 Ramsey signal.
- Checked terminal health: status/result completed, final counts `44.796 kcps`, monitor `last_error=""`, `stop_requested=false`.
- Ran scan-order-aware drift check using recorded snake `ScanOrderEachAvg`; no averages crossed the 15% drop flag threshold.
- Computed raw signal, signal/reference ratio, signal/fitted-reference-line normalization, per-point SEM, linear-residual peak-to-peak, FFT bins, least-squares sinusoid screens, and descriptive damped-sinusoid grid fits.

## Key quantitative checks

- Acquisition: `tau=0.048..1.968 us`, `41` points, `48 ns` step, `12 x 90000` shots, `1,080,000` shots/tau. FFT bin spacing is `0.508 MHz`; nominal `1/span` resolution is `0.521 MHz`.
- Noise/variation: median raw signal SEM `0.711 kcps`; median ratio SEM `0.0126`. Early `tau<=0.75 us` peak-to-peak remains large: signal `6.46 kcps`, ratio `0.134`.
- All-tau ratio LS screen: top component `1.623 MHz`, ratio amplitude `0.02547`, raw-signal amplitude at that frequency `1.252 kcps`, ratio R2 improvement `0.430`.
- Planned target amplitudes:
  - programmed `1.5 MHz`: ratio amp `0.02399`, raw amp `1.128 kcps`, ratio R2 improvement `0.359`.
  - det-tracking prediction from prior `1.192 MHz` feature: `1.692 MHz`, ratio amp `0.02505`, raw amp `1.225 kcps`, ratio R2 improvement `0.411`.
  - fixed artifact control at prior `1.192 MHz`: ratio amp only `0.00511`, raw amp `0.474 kcps`, ratio R2 improvement `0.017`.
- 13C-sideband targets are not dominant:
  - programmed sidebands `1.115/1.885 MHz`: ratio amps `0.01076/0.01732`.
  - det-tracking sidebands `1.307/2.077 MHz`: ratio amps `0.00953/0.00614`.
- Robustness caveats: raw-signal-only LS screen peaks near `0.882 MHz`; ratio screen after skipping `tau<=0.2 us` peaks near `0.746 MHz`; per-average top frequencies are inconsistent. Descriptive damped fits prefer ratio `0.678 MHz, T2*=0.469 us` and raw signal `0.818 MHz, T2*=0.717 us`, inconsistent with the all-tau ratio carrier-band screen.

## Plausible interpretation

The det-shift result is useful evidence against the prior `~1.192 MHz` feature being a fixed, det-independent artifact: after changing programmed det from `1.0` to `1.5 MHz`, the fixed `1.192 MHz` control becomes weak, while the strongest all-tau normalized component moves into the `1.5..1.7 MHz` carrier band and is close to the planned `1.692 MHz` det-tracking prediction within the coarse `~0.52 MHz` frequency resolution.

This is not yet a clean physical Ramsey/T2star model. The signal is dominated by an early-time transient, the raw-only and skip-early screens prefer different frequencies, and per-average screens do not lock to one component. The run supports "det-sensitive Ramsey-like response exists under this protocol" more than it supports a numeric T2star.

## Claims not yet supported

- No supported numeric T2star for r03. Descriptive T2* fits are model/transient dependent and not tied to a robust carrier assignment.
- No supported nearby 13C claim. Neither programmed nor det-tracking sidebands are dominant or consistently separated from a supported carrier by the expected offset.
- No claim that the carrier is exactly `1.623 MHz` or `1.692 MHz`; the short `1.92 us` span gives coarse frequency resolution and the model is not robust across analysis views.
- No reason to invalidate the existing aligned-NV conclusion for r03.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Make a bridge-free branch decision note: either close the r03 Ramsey/13C branch as unsupported under the current Ramsey protocol, or switch to a deliberately different protocol/analysis path aimed at resolving the early-time transient and obtaining a claim-grade coherence measurement.
