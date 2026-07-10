# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Relevant prior context: `evidence/e009.py` prior short-tau review script pattern, `evidence/e020.json` / `evidence/e028.json` det-shift planning artifacts, `evidence/e029.json` / `evidence/e030.json` batch/control snapshots.
- New local outputs: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw axis contract: `ExperimentDataEachAvg` has shape `[scan, avg, readout, point] = [1,12,2,41]`; averaging over `avg` exactly reproduces `ExperimentData`.
- Checked measurement metadata: completed `nv23_ramsey_20260514_015423_auto_ramsey`, run `1DExp-seq-ramsey-vary-tau-2026-05-14-015440`, `tau = 0.048..1.968 us`, 41 points, step `0.048 us`, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, `12 x 90000 = 1.08e6` shots/tau, final counts `44.796 kcps`, no stop request, no monitor error, safe shutdown OK.
- Computed raw reference/signal, point-wise signal/reference, signal/fitted-reference-line, per-point SEM across stored averages, rough per-average drift/outlier checks, FFT bin checks, and least-squares sinusoid screens from `0.4..2.4 MHz`.
- Frequency-resolution caveat: the time span gives nominal `1/span = 0.521 MHz` and FFT bin spacing `0.508 MHz`; LS screens can rank components but are not high-resolution frequency proof by themselves.

## Plausible interpretation

- The run is terminal and analyzable; no hard acquisition anomaly is evident in the provided files.
- The all-tau combined ratio LS screen peaks near `1.623 MHz` with ratio amplitude `0.02547` and baseline-residual improvement `0.430`. This is much closer to the det-shift prediction region (`~1.692 MHz`) than to the old `~1.192 MHz` component.
- Target amplitudes in the combined all-tau ratio view:
  - programmed `1.500 MHz`: amplitude `0.02399`, raw-signal amplitude `1.128 kcps`
  - shifted-carrier prediction `1.692 MHz`: amplitude `0.02505`, raw-signal amplitude `1.225 kcps`
  - old `1.192 MHz` component: amplitude `0.00511`, raw-signal amplitude `0.474 kcps`
- Median point SEM is `0.711 kcps` for raw signal and `0.0126` for ratio, so the all-tau `1.5..1.7 MHz` component is visible but only modestly above pointwise uncertainty.
- The early-time structure is large: within `tau <= 0.75 us`, raw signal peak-to-peak is `6.46 kcps` and ratio peak-to-peak is `0.134`. Removing `tau <= 0.2 us` changes the top ratio screen to `0.746 MHz`, so the apparent det-tracking component is not robust to early-transient handling.
- Per-average top frequencies are inconsistent (`~0.79..1.94 MHz`), with only some averages favoring the `1.5..1.7 MHz` region. Rough robust checks on per-average mean reference/signal/ratio did not flag a hard drift outlier, but average-to-average spectral consistency is not strong.
- Plausible read: the det shift argues against a fixed `1.192 MHz` artifact surviving unchanged, but the measurement still looks dominated by short-tau transient / model sensitivity rather than a clean Ramsey carrier plus sideband pattern.

## Claims not yet supported

- No well-supported numerical `T2*` claim. Descriptive damped fits prefer sub-microsecond-scale components (`ratio`: `0.675 MHz`, `T2* ~0.463 us`; raw signal: `0.818 MHz`, `T2* ~0.709 us`), but these are early-transient-sensitive and not tied cleanly to the programmed carrier/det-shift model.
- No supported nearby `13C` claim. Shifted-sideband targets near `1.307/2.077 MHz` are weak (`ratio amplitudes 0.00953/0.00614`), and programmed-carrier sidebands near `1.115/1.885 MHz` are not a coherent sideband pair.
- No clean claim that the Ramsey carrier is established. The all-tau result is compatible with a det-related component, but the skip-transient and per-average checks are not stable enough.

## Recommended next action

Do not run another blind same-style Ramsey repeat on r03. First make a cross-run Ramsey branch synthesis across the scout, 8 us det=1.0 run, short-tau det=1.0 run, and this det=1.5 shift check. If the project continues experimentally on r03, switch to a specifically modeled alternate protocol or control measurement rather than accumulating more identical Ramsey data; otherwise record the r03 Ramsey/T2*/13C conclusion as unsupported under current conditions while keeping the aligned-NV finding intact.
