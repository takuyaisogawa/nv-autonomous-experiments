# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey measurement: `measurement/m001.json` raw export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Run metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`, `analysis_run_output.txt`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw array contract: `ExperimentDataEachAvg[avg, readout, point]` averages back to `ExperimentData[readout, point]` with max absolute mismatch `1.42e-14 kcps`.
- Confirmed scan: `tau = 48 ns..8.048 us`, `41` points, `200 ns` step; job used `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `20 x 50000` shots.
- Used readout 1 as reference and readout 2 as Ramsey signal, consistent with the local Ramsey/readout convention for two-readout scans.
- Computed raw signal, reference, signal/reference ratio, per-point SEM across 20 averages, full-span and skip-first-4 least-squares sinusoid screens, bounded screens below `2.2 MHz`, FFT check, per-average frequency screens, and descriptive damped-cosine fits.

## Quantitative checks

- Terminal run health: `measurement/m003.json` status is `completed`, `safety.aborted = false`, `safe_shutdown_ok = true`; `measurement/m004.json` state is `completed`; run control has `stop_requested = false`.
- Mean counts: reference `48.789 kcps`, signal `44.670 kcps`, mean ratio `0.91563`.
- Median SEM: signal `0.850 kcps`; ratio `0.01161`.
- Per-average mean count ranges are broad but not collapsed: reference `41.739..54.899 kcps`, signal `37.377..50.371 kcps`.
- Full 0.2..2.49 MHz ratio LS screen is dominated by the Nyquist-edge region: top at `2.490 MHz` with ratio amplitude `0.0240`. This is not a clean physical carrier/sideband result.
- If frequencies above `2.2 MHz` are excluded, the combined ratio screen peaks near the programmed carrier: `1.516 MHz` full span with amplitude `0.01623`; after skipping the first four tau points it peaks near `1.515 MHz` with amplitude `0.01255`.
- Target amplitudes in the bounded ratio screen:
  - Carrier `1.500 MHz`: full `0.01575` rank `33`; skip-first-4 `0.01231` rank `30`.
  - Expected 13C lower sideband `1.115 MHz`: full `0.00277` rank `1539`; skip-first-4 `0.000678` rank `1926`.
  - Expected 13C upper sideband `1.885 MHz`: full `0.00961` rank `208`; skip-first-4 `0.00528` rank `783`.
  - Prior short-tau feature `1.192 MHz`: full `0.00194` rank `1839`; skip-first-4 `0.00191` rank `1523`.
- Raw-signal carrier amplitude from the full screen is `0.705 kcps`, below the median signal SEM (`0.850 kcps`).
- Per-average ratio screens are inconsistent: only 2 of 20 per-average top frequencies are near `1.5 MHz`; 12 of 20 are pinned near the high-frequency edge.
- Descriptive damped fits are not claim-grade. A carrier-seeded ratio fit lands near `1.527 MHz` and `T2* ~2.48 us` with low explanatory power (`R2 ~0.45`). A carrier-seeded raw-signal fit gives `T2* ~1.30 us` and `R2 ~0.56`. These are model-dependent descriptors, not supported T2star estimates.

## Plausible interpretation

The terminal refreshed-center Ramsey is analyzable and mildly improves the carrier story relative to earlier ambiguous traces: after excluding the Nyquist-edge dominated band, the combined normalized trace contains a weak feature near the programmed `1.5 MHz` detuning, and the old `~1.192 MHz` empirical feature is weak. However, the strongest unconstrained screen is still an edge-frequency component, the carrier-scale raw oscillation is at or below per-point SEM, and per-average frequency content is not consistent. The data therefore support "weak carrier-like evidence under constrained screening" but not a robust Ramsey decay model.

The expected 13C sideband pair at about `1.115/1.885 MHz` is not supported. The lower sideband is very weak, and the upper sideband is not paired with a matching lower feature or per-average consistency.

## Claims not yet supported

- A numerical T2star for r03 is not supported by this measurement.
- A nearby 13C coupling conclusion is not supported by this measurement.
- The `2.49 MHz` screen maximum should not be interpreted as a physical Ramsey frequency without a sampling/aliasing explanation.
- The carrier-seeded damped-fit T2star values around `1.3..2.5 us` should not be promoted beyond descriptive scratch fits.

## Recommended next action

Do not repeat the same `det = 1.5 MHz`, `48 ns..8.048 us`, `41` point Ramsey as a blind accumulation. Treat the current Ramsey branch as still non-claim-grade. The next project decision should be either:

1. switch to a deliberately different protocol or sampling design that tests the weak `~1.5 MHz` carrier without the Nyquist-edge ambiguity and with better short-time resolution, then only fit T2star if the carrier is reproducible per average; or
2. record a supported "T2star/13C unresolved under current Ramsey conditions" conclusion for r03 and move to an alternate 13C/coherence discriminator rather than more same-condition Ramsey repeats.
