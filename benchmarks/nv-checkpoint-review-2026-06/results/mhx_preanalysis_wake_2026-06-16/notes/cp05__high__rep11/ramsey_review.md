# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` run control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw array contract: combined `ExperimentData` shape `(1, 2, 41)` and per-average `ExperimentDataEachAvg` shape `(1, 20, 2, 41)`. Per-average means reproduce combined reference/signal traces.
- Terminal health: job `nv23_ramsey_20260514_055148_auto_ramsey` completed, final counts `43.433 kcps`, `safe_shutdown_ok=true`, `aborted=false`, `stop_requested=false`, monitor `last_error=""`.
- Scan parameters: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, tau `48 ns..8.048 us`, `41` points, `200 ns` step, nominal frequency resolution `125 kHz`, Nyquist `2.5 MHz`, `20 x 50000 = 1.0e6` shots/tau, snake scan order.
- Targets from the local project model: carrier `1.500 MHz`; expected 13C sidebands `1.115193 MHz` and `1.884807 MHz` using `B ~= 359.46 G` and `f_13C ~= 384.807 kHz`; old short-tau artifact control `1.192 MHz`; prior det-shift tracking target `1.692 MHz`.
- Least-squares sinusoid screens were run on raw signal, signal/reference, and signal/fitted-reference-line views over `0.2..2.45 MHz`; repeated after skipping the first 4 tau points. Windowed FFT peaks were also checked.
- Noise/provenance checks: median signal SEM `0.850 kcps`, median ratio SEM `0.01161`, median fitted-reference-line SEM `0.00937`. A simple per-average mean-signal MAD screen flagged no averages, but per-average mean signal still ranged `37.38..50.37 kcps`, so per-average consistency remains important.

## Plausible interpretation

- The run is analyzable and not a terminal failure.
- The strongest combined LS component is off-model: raw, ratio, and fitted-reference-line views all peak near `2.27 MHz`; skipping the first 4 tau points leaves the same approximate top frequency. FFT peaks include nearby high-frequency power and bins around the programmed carrier region, but the dominant LS feature is not the planned `1.5 MHz` carrier or the expected 13C sidebands.
- The programmed carrier is present only weakly/moderately: full-span signal/reference LS amplitude `0.01575`, fitted-reference-line amplitude `0.01447`, raw amplitude `0.705 kcps`; this is only `1.36x` median ratio SEM and `0.83x` median raw-signal SEM. Per-average ratio screens put only `6/20` averages within `200 kHz` of the `1.5 MHz` carrier, and `5/20` after skipping the first 4 points.
- The 13C sideband targets are weaker and less consistent: full-span ratio amplitudes are `0.00278` at `1.115 MHz` and `0.00962` at `1.885 MHz`; per-average ratio tops within `200 kHz` are `1/20` for the lower sideband and `3/20` for the upper sideband.
- The old `1.192 MHz` artifact-control target is weak in the combined view (`0.00194` ratio amplitude), so this dataset does not revive that prior feature. However, the new strongest `~2.27 MHz` component is near the upper part of the sampled band and off the intended carrier/13C model, so it should be treated as unexplained structure, not a physical assignment.

## Claims not yet supported

- No supported numeric `T2*` should be promoted from this run. The carrier/decay model is not sufficiently established before fitting a decay envelope.
- No supported nearby `13C` claim: neither expected sideband is dominant or per-average consistent.
- Do not claim that the `~2.27 MHz` feature is a real detuning, hyperfine feature, or 13C sideband without a deliberate follow-up that makes it move or disappear as predicted.
- Do not claim sub-grid precision for the pODMR-derived `3.8765 GHz` center; the project already treats it as grid-supported with several-100-kHz uncertainty.

## Recommended next action

Do not run another blind repeat of the same Ramsey. Treat the r03 Ramsey branch as still non-claim-grade after the refreshed-center high-shot run. The next runnable step should be a deliberately discriminating alternate check, for example a Ramsey variant with changed detuning/sign or phase/readout cycling and a sampling grid that keeps the suspected `~2.27 MHz` component away from the Nyquist edge, or move to an alternate protocol for 13C sensitivity. If no such protocol is available, record a supported negative/unsupported conclusion for r03 under the current Ramsey conditions rather than continuing repeats.
