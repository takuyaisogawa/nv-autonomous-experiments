# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey run metadata/data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Recent setup/design evidence: `evidence/e022.json`, `evidence/e023.json`, `evidence/e024.json`, plus project-state summaries of earlier r03 Ramsey diagnostics.
- Generated here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw data shape and axis contract: `ExperimentData` is `[2,41]`; `ExperimentDataEachAvg` is `[20,2,41]`; averaging stored averages reproduces the combined data.
- Used embedded `ramsey.xml` readout roles: with `full_experiment=0`, readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
- Checked terminal health: job completed, final counts `43.433 kcps`, no stop request, no monitor error, not aborted, safe shutdown OK.
- Confirmed scan: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, `41` points, `200 ns` step, `20 x 50000 = 1.0e6` shots/tau, Nyquist `2.5 MHz`, nominal resolution `125 kHz`.
- Performed line detrending, target-frequency least-squares sinusoid checks, full-span and skip-first-4-point frequency screens, FFT bin checks, per-average frequency-top checks, and SEM comparisons.

## Plausible interpretation

- The run is technically usable, but the planned Ramsey carrier/sideband model is still not supported.
- Carrier at `1.5 MHz`: raw LS amplitude `0.705 kcps` vs median per-point raw SEM `0.850 kcps`; point-wise ratio amplitude `0.0157` vs ratio SEM `0.0116`; reference-line normalized amplitude `0.0144` vs refline SEM `0.0174`. This is weak and not dominant.
- Expected 13C sidebands from the project model are near `1.115 MHz` and `1.885 MHz`; they are not dominant. Ratio amplitudes were `0.00276` and `0.00961`, respectively.
- The strongest combined screens cluster near `2.27 MHz`, with ratio amplitude about `0.0184` and refline-normalized amplitude about `0.0168`, but this is still only order-SEM and not robust across stored averages.
- Per-average frequency tops are mixed: within `0.25 MHz`, only `6/20` ratio averages and `7/20` refline-normalized averages support the `~2.27 MHz` feature; `1.5 MHz` and `1.885 MHz` also get scattered partial support. This looks more like weak structured noise/artifact plus drift/common-mode variation than a claim-grade coherent Ramsey signal.
- The old short-tau empirical `~1.192 MHz` feature is weak here (`0.00194` ratio amplitude), so this run does not revive it.

## Claims not yet supported

- No numeric T2star is supported from this Ramsey run.
- No nearby 13C coupling conclusion is supported.
- The `~2.27 MHz` feature is not supported as a physical Ramsey carrier or sideband.
- The refreshed pODMR center at `3.8765 GHz` remains useful frequency-calibration evidence, but this Ramsey run does not convert it into a T2star/13C result.

## Recommended next action

Do not run another blind same-protocol Ramsey repeat on r03. The refreshed-center, high-shot, long-span Ramsey was the planned non-blind test and remains non-claim-grade. The next project action should be a decision point: either switch to an alternate protocol/diagnostic designed to avoid the current Ramsey failure mode, or record a supported negative/unsupported conclusion for r03 Ramsey/T2star/13C under the current conditions.
