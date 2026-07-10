# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior Ramsey evidence: `evidence/e008.json` for the terminal `det = 1.0 MHz` short-tau review, and `evidence/e019.json` / `evidence/e021.json` for the det-shift model and success criteria.
- New measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- New run: `nv23_ramsey_20260514_015423_auto_ramsey`, run id `1DExp-seq-ramsey-vary-tau-2026-05-14-015440`, completed with `tau = 0.048..1.968 us` in 41 points, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, `12 x 90000` shots per tau point, final counts `44.796 kcps`.

## Calculations or scripts run

- Created and ran `analyze_ramsey_det1p5.py`.
- Outputs: `ramsey_det1p5_analysis.json` and `ramsey_det1p5_analysis.png`.
- Checks performed:
  - Verified raw array contract: `ExperimentDataEachAvg` shape `[1, 12, 2, 41]` averages back to `ExperimentData`; readout 1 treated as reference and readout 2 as Ramsey signal.
  - Reconstructed tau grid and scan-order-aware drift check using snake `ScanOrderInfo.order_each_avg`; no average was drift-flagged.
  - Computed point SEM across averages, point-wise signal/reference ratio, signal over fitted reference line, LS sinusoid screens, FFT sanity bins, per-average frequency screens, and descriptive damped-sinusoid grid fits.
- Key quality numbers: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`; ratio residual peak-to-peak after linear baseline `0.133`; early `<=0.75 us` ratio peak-to-peak `0.134`; FFT bin spacing `0.508 MHz`, so FFT is coarse and only a sanity check.

## Plausible interpretation

- The new run is terminal and analyzable: status completed, no stop request, empty monitor error, and no drift flags.
- The old `det = 1.0 MHz` top at `1.192 MHz` did not persist as the dominant ratio feature in the new run. Its new ratio LS amplitude is only `0.00511`, versus `0.0363` in the prior terminal review.
- There is some ratio-view movement toward the intended higher-frequency det-shift region, but it is not clean enough to claim a physical Ramsey carrier:
  - ratio all-tau LS top: `1.623 MHz`, amplitude `0.02547`;
  - programmed `1.500 MHz` carrier: amplitude `0.02399`;
  - planned det-tracking target `1.692 MHz`: amplitude `0.02505`.
- Readout-aware views disagree with the ratio-only top: raw signal and signal/fitted-reference-line screens peak near `0.882 MHz`, not `1.623 MHz` or `1.692 MHz`.
- Window choice matters: skipping only the first point gives a ratio top near `1.650 MHz`, but skipping `tau <= 0.2 us` moves the top to about `0.746 MHz`.
- Per-average frequency screens are not coherent: tops span `0.250..1.938 MHz`; only `1/12` is within `50 kHz` of the combined ratio top, and only `2/12` are within `50 kHz` of the det-tracking target.
- Expected 13C sideband targets are weak/non-dominant. Effective det-tracking sidebands at `1.307/2.077 MHz` have ratio amplitudes `0.00953/0.00614`.
- Descriptive damped fits are not promoted: ratio view gives `f = 0.678 MHz`, `T2* = 0.469 us`; raw signal gives `f = 0.818 MHz`, `T2* = 0.717 us`. These are model-dependent because the carrier assignment fails.

## Claims not yet supported

- No supported numeric `T2*` for r03 from this Ramsey branch.
- No supported nearby-13C claim from Fourier/LS sideband structure.
- No supported clean det-following Ramsey carrier assignment.
- No supported claim that the prior `1.192 MHz` component was a simple physical carrier; the new run argues against a fixed `1.192 MHz` artifact-control peak but does not replace it with a robust physical model.

## Recommended next action

Do not run another blind same-protocol Ramsey repeat on r03. Make a branch decision: either close the current r03 Ramsey/T2*/13C path as unsupported under these conditions, or switch to a targeted protocol/control that can separate pulse/readout baseline transients from true free precession before attempting a numeric `T2*` or 13C conclusion.
