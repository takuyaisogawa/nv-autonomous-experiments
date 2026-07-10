# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, and relevant Ramsey guidance from `md/knowledge.md`.
- New terminal Ramsey data: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison data/context: `evidence/e006.json` prior det=1.0 MHz short-tau raw export and `evidence/e008.json` prior terminal review. The prior review's key empirical component was near `1.192 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis.json` and `ramsey_analysis.png`.
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract by averaging per-average traces back to `ExperimentData`.
  - Confirmed new run parameters: `tau = 0.048..1.968 us`, `41` points, `48 ns` step, `12 x 90000` shots per tau point, `det = 1.5 MHz`, snake order, data saved in tau order.
  - Checked terminal health: completed, final counts `44.796 kcps`, safe shutdown OK, monitor last error empty, stop not requested.
  - Computed raw signal/reference, point-wise ratio, fitted-reference-normalized signal, per-point SEM, detrended FFT, least-squares sinusoid screens, early-tau-cut screens, per-average frequency screens, a simple robust average-mean drift check, and descriptive damped-sinusoid grid fits.

## Key quantitative results

- Median per-point SEM: raw signal `0.711 kcps`, ratio `0.0126`.
- Detrended residual scale remains large: raw-signal residual peak-to-peak `6.29 kcps`, ratio residual peak-to-peak `0.133`; within `tau <= 0.75 us`, raw-signal peak-to-peak is `6.46 kcps` and ratio peak-to-peak is `0.134`.
- Combined all-tau ratio LS screen peaks near `1.623 MHz` with amplitude `0.0255` ratio units.
- Target LS amplitudes in the ratio view:
  - Programmed carrier `1.500 MHz`: `0.0240`.
  - Expected low 13C sideband `1.115 MHz`: `0.0108`.
  - Expected high 13C sideband `1.885 MHz`: `0.0173`.
  - Prior fixed empirical component `1.192 MHz`: `0.0051`.
  - Prior component shifted by the det change, `1.692 MHz`: `0.0250`.
- The all-tau FFT is coarse because the Ramsey span is short: bin spacing is `0.508 MHz`; nearest-bin amplitudes put the largest ratio bin at `1.524 MHz`.
- Removing `tau <= 0.2 us` changes the ratio LS top to about `0.746 MHz`, so the spectral result is strongly early-transient/model dependent.
- Per-average top frequencies are inconsistent (`0.25..1.94 MHz`), though the simple robust average-mean drift check did not flag an average.
- Descriptive damped fits prefer short-decay/interior values (`ratio: 0.678 MHz, T2* ~0.47 us`; raw signal: `0.818 MHz, T2* ~0.72 us`), but these are not promoted because the fit is dominated by early-time structure and does not agree with the carrier/sideband hypothesis.

## Plausible interpretation

- The new det=1.5 MHz measurement is terminal and analyzable; there is no hard run anomaly in the provided files.
- The old fixed `~1.192 MHz` feature does not persist as a fixed-frequency component in the new run, which argues against simply carrying that exact component forward as a stationary physical feature.
- The new spectral weight is broadly near the programmed/det-shifted region, but the short time span gives poor frequency resolution and the LS result is sensitive to early-tau removal. The all-tau top (`~1.623 MHz`) sits between the programmed carrier (`1.500 MHz`) and the det-shift prediction from the prior empirical feature (`~1.692 MHz`), so it is not a clean discriminator.
- Expected 13C sidebands at `~1.115 MHz` and `~1.885 MHz` are not dominant or consistently supported.

## Claims not yet supported

- No numeric T2* value is supported from this run.
- No nearby 13C coupling/sideband conclusion is supported.
- A clean det-following Ramsey carrier is not yet supported.
- The previous `~1.192 MHz` feature should not be claimed as a physical Ramsey feature; this run weakens the fixed-frequency version but does not replace it with a robust carrier/sideband model.

## Recommended next action

Do not run another blind same-style Ramsey repeat. Treat the r03 alignment claim as still supported, but close the current Ramsey evidence as non-claim-grade for T2*/13C under these conditions. The next useful step is a bridge-free branch synthesis and decision: either switch to a targeted alternate protocol/control that can separate early-time pulse/transient artifacts from true Ramsey phase evolution, or record a supported negative/unsupported conclusion for r03 Ramsey-based T2*/13C in this configuration.
