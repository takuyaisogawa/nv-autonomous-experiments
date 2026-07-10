# Ramsey Review: refreshed-center r03 det=1.5 MHz long span

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New Ramsey data/artifacts: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec/advisory payload, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Local checks also searched `evidence/` for this job id/run id to avoid missing an existing terminal review; no separate completed analysis note for this new data was present in the snapshot.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.
- Verified raw array layout: `ExperimentDataEachAvg` shape is `[1,20,2,41]`; averaging the 20-average axis reproduces `ExperimentData` with max absolute difference `1.4e-14 kcps`.
- Confirmed run parameters from local files: job `nv23_ramsey_20260514_055148_auto_ramsey`, completed normally, `ramsey.xml`, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=0.048..8.048 us`, step `0.2 us`, `41` points, `20 x 50000` shots, final counts `43.433 kcps`, scan order `snake`, no stop request.
- Computed raw-signal, point-wise ratio, and fitted-reference-line-normalized views; screened LS sinusoid amplitudes from `0.125..2.45 MHz`, checked FFT peaks, target frequencies, skip-first-4-point screens, per-average top frequencies, and SEM scale.

## Plausible interpretation

- The run is analyzable and not a terminal hardware/count failure. Final counts are healthy and the terminal bridge result reports a completed savedexperiment with safe shutdown.
- The programmed carrier is present only weakly relative to the measurement scatter. At `1.5 MHz`, LS amplitude is `0.705 kcps` in raw signal versus median per-point signal SEM `0.850 kcps`; normalized amplitudes are `0.0157` point-wise and `0.0145` fitted-reference-line, versus median ratio SEM `0.0116`.
- Expected 13C sideband targets are not compelling: lower `1.115 MHz` gives only `0.146 kcps` raw / `0.0028` ratio amplitude, and upper `1.885 MHz` gives `0.261 kcps` raw / `0.0096` ratio amplitude. These are not consistent, high-SNR sideband evidence.
- The strongest combined frequency screen is instead near `2.27 MHz` in raw, ratio, and fitted-reference views. It persists after skipping the first four points, but it is not the programmed carrier or expected `1.115/1.885 MHz` sideband pair. Its raw amplitude is only about `0.82 kcps`, near the per-point SEM scale, and per-average top frequencies are broadly mixed (`~0.125..2.34 MHz`) rather than clustered.
- Per-average mean brightness varies substantially: signal average means span `37.38..50.37 kcps` and reference means span `41.74..54.90 kcps` (`~29%` and `~27%` of median, respectively). This looks like a large common-mode average-to-average brightness variation; normalization reduces but does not turn the Ramsey feature into a clean carrier/sideband model.
- Best current reading: this high-shot refreshed-center Ramsey still does not produce claim-grade Ramsey oscillation evidence. It weakens the idea that simple shot accumulation at the refreshed center will rescue the r03 Ramsey result under this protocol.

## Claims not yet supported

- No numeric `T2*` should be claimed from this run. A damped-sinusoid fit would be fit-first rather than signal-first because the carrier/decay shape is not supported at adequate SNR.
- No nearby `13C` coupling claim is supported. The expected sideband pair around `1.115/1.885 MHz` is not consistently resolved.
- The `2.27 MHz` screen maximum should not be promoted as a physical Ramsey frequency without an independent protocol/frequency-shift check; it is high in the available band, weak relative to SEM, and per-average inconsistent.
- This run does not invalidate the r03 aligned-NV identification from pODMR; it only says the current Ramsey/T2star/13C branch remains non-claim-grade.

## Recommended next action

Avoid another blind long-span Ramsey repeat on r03 with the same protocol. Treat the r03 Ramsey/T2star/13C conclusion as unsupported under current conditions unless a targeted protocol change is justified. The next useful experimental action is a protocol diagnostic rather than more averaging: either run a Hahn-echo/CPMG `N=1` baseline to check whether coherence is recoverable under an echo sequence, or perform a deliberately shifted Ramsey carrier check designed to test whether the `2.27 MHz` feature tracks detuning. If bridge work is not immediately desired, update project state with this terminal review and mark r03 Ramsey/T2star/13C as unresolved/non-claim-grade after five analyzable Ramsey attempts.
