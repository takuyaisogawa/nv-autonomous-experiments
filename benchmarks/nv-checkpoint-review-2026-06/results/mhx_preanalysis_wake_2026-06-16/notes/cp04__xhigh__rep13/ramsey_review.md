# Ramsey Review: det=1.5 MHz short-tau check

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior Ramsey context and planned success criteria: `evidence/e008.json`, `evidence/e009.py`, `evidence/e021.json`.
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Scratch outputs from this review: `ramsey_detshift_analysis_summary.json` and `ramsey_detshift_analysis.png`.

## Calculations/scripts run

- Ran local inline Python on the JSON files to reconstruct the tau axis, verify the raw-export axis contract, compute readout means/SEM, run least-squares sinusoid screens, FFT checks, per-average screens, and a scan-order-aware drift sanity check using `ScanOrderEachAvg`.
- Verified `ExperimentDataEachAvg` behaves as `[scan, avg, readout, point]`: averaging per-average readouts reproduces `ExperimentData`.
- New run geometry: tau `0.048..1.968 us`, step `0.048 us`, 41 points, 12 averages x 90000 repetitions = `1.08e6` shots/tau point. FFT bin spacing is `0.508 MHz`; Nyquist is `10.417 MHz`.
- Run status checks: completed at `2026-05-14T04:15:00`, final counts `44.796 kcps`, no error code/message, `stop_requested=false`, monitor `last_error=""`, safe shutdown OK.
- Basic readout stats: reference mean `48.084 kcps`, signal mean `44.269 kcps`, ratio mean `0.92069`; median per-point SEM is `0.711 kcps` for signal and `0.01262` for ratio.
- The early-time structure is still large: signal peak-to-peak through `0.75 us` is `6.46 kcps`, ratio peak-to-peak is `0.134`. Linear-detrended full-window peak-to-peak is similar (`6.29 kcps`, ratio `0.133`).
- Target LS/FFT checks:
  - Programmed carrier `1.500 MHz`: ratio LS amp `0.02399`, R2 improvement `0.359`; signal amp `1.128 kcps`, R2 improvement `0.345`.
  - Det-tracked prior feature `1.692 MHz`: ratio LS amp `0.02505`, R2 improvement `0.411`; signal amp `1.225 kcps`, R2 improvement `0.427`.
  - Old artifact-control position `1.192 MHz`: ratio LS amp only `0.00511`, R2 improvement `0.017`; signal amp `0.474 kcps`.
  - Det-tracked sidebands `1.307/2.077 MHz`: weak in ratio (`0.00953` and `0.00614`) and not a paired 13C pattern.
  - Programmed-det sidebands `1.115/1.885 MHz`: also not a clean pair (`0.01076` and `0.01732` ratio LS amp).
- Frequency-screen checks:
  - All-tau ratio screen peaks near `1.623 MHz` with ratio amp `0.02547`, close to but not exactly the `1.692 MHz` det-tracking target within the short-window resolution.
  - Skipping tau `<=0.2 us` moves the ratio screen top to about `0.746 MHz`, so the inferred component is transient/model-sensitive.
  - Raw signal and signal/reference-line screens instead peak near `0.882 MHz`, not the ratio screen peak.
  - Per-average top frequencies are scattered (`0.25..1.94 MHz`), not a coherent carrier across averages.
- Descriptive damped-sinusoid grid fits prefer sub-MHz frequencies (`0.678 MHz` ratio, `0.818 MHz` signal) with short apparent T2star (`0.47..0.72 us`), but this is diagnostic only because the carrier/readout model is not stable.

## Plausible interpretation

- This terminal det-shift Ramsey is analyzable and passed basic execution/count/safety checks.
- The old `~1.192 MHz` ratio feature did not remain strong at the fixed old frequency after det changed to `1.5 MHz`; that weakens a simple fixed-frequency artifact explanation in the ratio view.
- However, the evidence is still not a clean physical Ramsey model. The all-tau ratio screen is near the programmed/det-tracked carrier band, but raw signal views prefer `~0.88 MHz`, the best ratio frequency changes when early points are skipped, and per-average screens are inconsistent.
- The most conservative reading is: there is det-sensitive short-tau structure, but the current Ramsey data are still dominated by early-time/readout/baseline effects enough that a physical carrier, decay envelope, and 13C sideband model cannot be separated reliably.

## Claims not yet supported

- No numeric T2star should be claimed from this run or from the descriptive damped fits.
- No nearby 13C coupling/sideband conclusion is supported. The tested sideband targets are weak and not consistent across raw/readout-aware views.
- Do not claim that the `1.623..1.692 MHz` ratio component is definitively the physical NV Ramsey carrier.
- Do not claim that the prior `~1.192 MHz` feature was purely an artifact; the det-shift check argues against a fixed old-frequency ratio feature but does not prove a clean carrier model.
- The aligned r03 conclusion remains supported by prior pODMR evidence, not by this Ramsey run.

## Recommended next action

Stop blind Ramsey repeats on this same r03 branch. Update the project state with this terminal det-shift result as non-claim-grade: it weakens the fixed-`1.192 MHz` artifact hypothesis in ratio, but still does not support T2star or 13C. The next scientific action should be a branch-level decision between an alternate, explicitly diagnostic protocol and closing the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey conditions.
