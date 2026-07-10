# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Analysis guidance/context: `md/memory.md`, `md/knowledge.md`.
- Prior local evidence: `evidence/e001.json` for the refreshed pODMR center and `evidence/e014.json` for the planned Ramsey targets/model.
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` control state.

## Calculations/scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis.json` and `ramsey_analysis.png`.
- Verified raw axis contract: `ExperimentData` shape `[2, 41]`, `ExperimentDataEachAvg` shape `[20, 2, 41]`; averaging stored traces reproduces `ExperimentData` with max absolute error `1.4e-14`.
- Confirmed measurement settings: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us`, `41` points, `0.2 us` step, `20 x 50000` shots = `1.0e6` shots/tau, nominal resolution `125 kHz`, Nyquist `2.5 MHz`.
- Terminal health: completed, final counts `43.433 kcps`, safe shutdown true, no stop request, monitor `last_error` empty.
- Drift/provenance checks: snake order, 10 forward and 10 reverse averages. Per-average reference means ranged `41.74..54.90 kcps`, signal means `37.38..50.37 kcps`, but ratio mean CV was `1.79%`; forward/reverse ratio means were `0.9159` and `0.9176`.
- Full-span and skip-first-4-point least-squares screens used raw signal, signal/reference, and signal/fitted-reference-line channels. Targets came from `evidence/e014.json`: carrier `1.500 MHz`, expected 13C sidebands `1.115` and `1.885 MHz`, prior diagnostic controls `1.623 MHz`, `0.746 MHz`, and `1.192 MHz`.

## Plausible interpretation

- The run is valid and analyzable, but it is still non-claim-grade for T2star/13C.
- The strongest continuous-frequency LS screen is not at the programmed carrier. Full-span ratio top is about `2.270 MHz` with amplitude `0.01845`; raw-signal top is about `2.271 MHz` with amplitude `0.818 kcps`. After skipping the first four tau points, the ratio/raw tops remain near `2.266..2.271 MHz`.
- The programmed `1.500 MHz` carrier is present but not dominant: full-span ratio amplitude `0.01575` and raw amplitude `0.705 kcps`; skip-first-4 ratio amplitude `0.01231` and raw amplitude `0.512 kcps`. These are near the measured per-point uncertainty scale (`median signal SEM 0.85 kcps`, `median ratio SEM 0.0116`) and do not form a clean per-average pattern.
- Expected 13C sidebands are weak: skip-first-4 ratio amplitudes are `0.00067` at `1.115 MHz` and `0.00527` at `1.885 MHz`. Per-average ratio screens peak near the carrier in only `5/20` averages, near the combined `2.27 MHz` feature in `4/20`, near the low sideband in `1/20`, and near the high sideband in `2/20`.
- Bootstrap over stored averages supports the same caution: in 300 resamples, the top ratio-screen frequency was within `150 kHz` of `2.27 MHz` in `218/300` resamples and near the programmed carrier in `80/300`; it was near the low/high 13C sidebands in `0/300` and `2/300`.
- The old fixed `~1.192 MHz` artifact-control target is weak in this terminal data, so the refreshed-center run argues against simply promoting that earlier component. It does not replace it with a clean carrier/sideband model.

## Claims not yet supported

- No supported numeric `T2star` value from this run.
- No supported nearby-13C claim from Ramsey sidebands.
- No supported physical assignment of the `~2.27 MHz` empirical component.
- No support for claiming that the refreshed `3.8765 GHz` center solved the Ramsey failure mode.
- No support for a decay-envelope fit until a raw/readout-aware carrier signal is established.

## Recommended next action

Do not run another blind same-style Ramsey repeat on r03. Treat this refreshed-center high-shot long-span Ramsey as a terminal non-claim-grade Ramsey result under the current route. The next project decision should be either an alternate diagnostic/protocol to explain the persistent non-target spectral structure, or a documented r03 conclusion that T2star and nearby-13C remain unsupported under these conditions before moving effort to another candidate.
