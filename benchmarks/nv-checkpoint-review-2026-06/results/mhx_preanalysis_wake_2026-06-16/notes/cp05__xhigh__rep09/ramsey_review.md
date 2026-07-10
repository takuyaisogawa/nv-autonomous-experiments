# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Planning context: `evidence/e014.json` refreshed-center Ramsey model/advisory with carrier and 13C sideband targets.

## Calculations/scripts run

- Created and ran `ramsey_analysis.py`; outputs are `ramsey_analysis_summary.json` and `ramsey_analysis_plot.png`.
- Verified raw export axis contract: mean over `ExperimentDataEachAvg` reproduces `ExperimentData` with max absolute difference `1.4e-14 kcps`.
- Confirmed scan/job: completed `auto__ramsey`, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=0.048..8.048 us`, `41` points, `20 x 50000` shots, final counts `43.433 kcps`, no stop request or monitor error.
- Noise/provenance checks: median per-point SEM from stored averages is `0.850 kcps` on signal, `0.867 kcps` on reference, and `0.0116` on point-wise signal/reference ratio. Stored-average signal/reference means co-move strongly (`corr=0.970`) with large common-mode range (`29.1%` signal, `27.0%` reference); ratio mean range is smaller (`7.44%`).
- Frequency checks used linear-baseline sinusoid LS screens, Hann-window FFT checks, skip-first-4-tau checks, and per-average complex-coefficient scatter.

## Plausible interpretation

- The refreshed-center long Ramsey is not a failed or anomalous run. It has a visible carrier-like component near the programmed `1.5 MHz`: combined raw signal LS amplitude `0.705 kcps` (`z~3.5` residual estimate), point-wise ratio amplitude `0.0157`, and per-average complex-coefficient scatter still supports a coherent carrier component (`raw z~8.7`, ratio z~6.7; skip-first-4 raw z~5.7, ratio z~4.5).
- This is stronger carrier evidence than the prior weak/mixed Ramsey branch and is consistent with the refreshed pODMR center helping.
- However, the largest full-span LS component in raw/ratio/fitted-reference views is near `2.27 MHz`, not the programmed carrier. FFT views also show comparable power around both the carrier bins (`~1.46/1.59 MHz`) and `~2.30 MHz`; after skipping the first four tau points, raw and fitted-reference FFT top move near `1.49 MHz`, but the LS screen remains strongly affected by `~2.27 MHz`.
- The expected low 13C sideband near `1.115 MHz` is not supported. The high sideband near `1.885 MHz` is weak in full-span ratio/reference views and falls away after the skip-first-4 check.
- Damped one-tone fits are not stable enough for a T2star claim: full-span fits prefer `~2.28 MHz` with `T2star~1.8-2.6 us`, while skip-first-4 raw/fitted-reference carrier-band fits prefer `~1.53 MHz` with `T2star~2.8 us`; point-wise ratio skip-first-4 still prefers `~2.25 MHz`, and carrier-band ratio gives `T2star~4.8 us`.

## Claims not yet supported

- No numeric T2star is supported from this run.
- No nearby 13C conclusion is supported; neither the expected sideband pair nor a stable coupling model is established.
- Do not claim a clean single-frequency Ramsey carrier/decay model.
- Do not assign the `~2.27 MHz` component to a physical NV/13C feature without a det-following or other control.

## Recommended next action

Do not do another blind accumulation or promote a fit. If continuing experimentally, run a targeted det-following control at the refreshed center, for example a same-grid det-shifted Ramsey around `det=1.0 MHz`, and test whether the carrier moves with programmed det while the `~2.27 MHz` structure stays fixed. If that control is not run, record the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey conditions.
