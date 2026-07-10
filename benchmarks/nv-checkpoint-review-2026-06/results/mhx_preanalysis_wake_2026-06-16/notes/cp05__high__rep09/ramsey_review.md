# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior model/design context: `evidence/e014.json`, which set the refreshed-center Ramsey targets: carrier `1.5 MHz`, 13C sidebands near `1.115 MHz` and `1.885 MHz`, `tau = 48 ns..8.048 us`, `41` points, and `20 x 50000` shots.
- New terminal data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` bridge result, `measurement/m004.json` status, `measurement/m005.json` control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw array contract: `ExperimentData` shape `[1, 2, 41]`, `ExperimentDataEachAvg` shape `[1, 20, 2, 41]`; averaging over the stored-average axis reproduces `ExperimentData`.
- Used saved `ramsey.xml` text in `measurement/m001.json` to assign readout 1 as the `mS=0` reference and readout 2 as the Ramsey signal (`full_experiment=0` skips the optional second reference).
- Confirmed scan settings: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us`, `0.2 us` step, nominal resolution `0.125 MHz`, Nyquist `2.5 MHz`, total shots per tau `1.0e6`.
- Terminal health check from bridge files: completed, final counts `43.433 kcps`, no stop request, no monitor error, `aborted=false`, safe shutdown OK.
- Performed least-squares sinusoid screens with constant + linear trend terms over `0.25..2.4 MHz`, both full span and after skipping the first 4 tau points. Also computed Hann-window FFT summaries and target-bin amplitudes.
- Compared raw signal, point-wise signal/reference, and signal/fitted-reference-line views against stored-average SEM and per-average top-frequency consistency.

## Plausible interpretation

- The run is technically usable, but it does not give claim-grade Ramsey/T2star/13C evidence.
- There is a small coherent component at the programmed `1.5 MHz` carrier, but it is not dominant. Full-span carrier amplitudes are about `0.705 kcps` raw, `0.0157` point-wise ratio, and `0.0145` fitted-reference normalization. After skipping the first 4 points they fall to about `0.512 kcps`, `0.0123`, and `0.0105`.
- The strongest full-span LS screen is near `2.27 MHz` in all three views. Its raw amplitude is `0.818 kcps`, only about `0.96x` the median raw point SEM (`0.850 kcps`), and it is close enough to the high-frequency/Nyquist side of the scan that it should be treated as exploratory.
- FFT bins show carrier-near power around `1.46..1.59 MHz`, especially in the point-wise ratio view, but raw and fitted-reference views have comparable or stronger high-frequency power near `2.2..2.3 MHz`.
- The 13C sideband targets are weak: full-span raw LS amplitudes are `0.145 kcps` at `1.115 MHz` and `0.261 kcps` at `1.885 MHz`; after skipping 4 points they are `0.012 kcps` and `0.124 kcps`. Normalized sideband amplitudes are similarly not dominant.
- Stored-average screens are mixed. Within `0.2 MHz`, only `6/20` point-wise-ratio average screens land near the carrier, `1..2/20` near the low sideband, and `3/20` near the high sideband depending on skip. Raw and fitted-reference views are weaker (`2..3/20` near carrier).
- Average-to-average common-mode variation is material: average ref means range `41.739..54.899 kcps`, signal means range `37.377..50.371 kcps`, and ratio means range `0.891..0.959`. This reinforces using readout-aware and per-average consistency checks rather than fitting a single combined curve.

## Claims not yet supported

- No well-supported numeric `T2star` can be claimed from this measurement.
- No nearby `13C` assignment is supported from the expected carrier/sideband model.
- The `~2.27 MHz` exploratory component should not be assigned to a physical coupling without an artifact/control check.
- The small `1.5 MHz` component should not be promoted to a fitted Ramsey decay model because the carrier is not dominant and sideband/per-average consistency is weak.

## Recommended next action

Avoid another blind Ramsey repeat on r03 using the same route and basic conditions. The current dataset had higher shots and a refreshed pODMR center, yet still did not produce a clean carrier/sideband model. The next useful step is either an alternate protocol/control diagnostic that directly tests Ramsey sequence/timing or readout artifacts, or closing the current r03 Ramsey/13C branch as unsupported under these conditions.
