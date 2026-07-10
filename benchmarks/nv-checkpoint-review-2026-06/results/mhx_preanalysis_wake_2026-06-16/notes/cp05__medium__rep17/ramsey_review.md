# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal run status, `measurement/m005.json` run control.
- Recent project evidence checked for intent/provenance: `evidence/e022.json`, `evidence/e023.json`, `evidence/e024.json`.
- New local artifacts created: `analyze_ramsey_review.py`, `ramsey_review_analysis.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_review.py`.
- Verified raw export axes: `ExperimentData` is `[1, 2, 41]`; `ExperimentDataEachAvg` is `[1, 20, 2, 41]`; averaging stored averages reproduces `ExperimentData` to `1.4e-14`.
- Interpreted readout 0 as the 0-level reference and readout 1 as the Ramsey signal from the saved `ramsey.xml` path with `full_experiment=0`.
- Confirmed planned acquisition: `tau = 48 ns..8.048 us`, `dt = 200 ns`, 41 points, snake scan, 20 averages x 50000 reps, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`; terminal final counts were `43.433 kcps`.
- Checked raw signal, point-wise signal/reference, and signal divided by a fitted reference line.
- Least-squares sinusoid checks:
  - Carrier `1.500 MHz`: raw signal amplitude `0.705 kcps`, fitted-reference ratio amplitude `0.01445`; skip-first-4 ratio amplitude `0.01049`.
  - Expected 13C sidebands from project model: `1.115 MHz` amplitude `0.00298` ratio, `1.885 MHz` amplitude `0.00536` ratio; both weaken further after skipping first 4 points.
  - Prior controls: `1.192 MHz` amplitude `0.00226` ratio; prior det-shift `1.623 MHz` amplitude `0.00770` ratio.
- Noise/drift proxies:
  - Median per-point signal SEM across stored averages: `0.850 kcps` (range `0.504..1.097 kcps`).
  - Detrended raw-signal standard deviation: `1.006 kcps`; detrended fitted-reference-ratio standard deviation: `0.0206`.
  - First 5 vs last 5 stored averages drift proxy: signal mean `-3.23%`, reference mean `-2.62%`, ratio mean `-0.65%`.
- Frequency screens:
  - Combined fitted-reference-ratio LS screen peaks near `2.270 MHz` with amplitude `0.01677`, not at carrier or expected sidebands.
  - Skip-first-4 screen remains near `2.270 MHz` but drops to amplitude `0.01138`.
  - Windowed FFT top components are `2.317 MHz`, then bins near `1.463/1.585 MHz`.
  - Per-average frequency screens are scattered across low frequency, carrier-like, sideband-like, and high-frequency regions rather than agreeing on one component.

## Plausible interpretation

- The measurement completed cleanly and is analyzable, but it is still not claim-grade for Ramsey/T2star or 13C.
- The programmed carrier is present only as a weak component: its raw amplitude is below the median signal SEM, and its normalized amplitude is comparable to the exploratory non-target peaks.
- The expected 13C sidebands at `1.115/1.885 MHz` are much weaker than the carrier and are not consistently selected by full-span, skip-transient, FFT, or per-average checks.
- The persistent high-frequency screen near `2.27 MHz` may be an empirical oscillatory/artifact component or noise-shaped feature. It is not currently tied to the programmed detuning or the project 13C model.
- Compared with earlier r03 Ramsey attempts, this high-shot refreshed-center run argues against simply accumulating more identical Ramsey data. The limiting issue is not just shot count; the carrier/sideband model is not cleanly expressed in the raw/readout-aware data.

## Claims not yet supported

- No numeric `T2star` value is supported from this dataset.
- No nearby `13C` presence, absence, coupling, or Hamiltonian parameter is supported from this dataset.
- The `2.27 MHz` screen maximum should not be promoted to a physical Ramsey frequency without an independent protocol/control check.
- The refreshed weak-pi pODMR center remains a frequency calibration for this run, not evidence of a Ramsey decay or 13C conclusion.

## Recommended next action

- Do not run another blind long-span Ramsey repeat on r03 under the same protocol.
- Move to an alternate, diagnostic branch before any further claim attempt: either validate the Ramsey phase/readout path with a protocol/control measurement designed to produce an unambiguous carrier, or switch to a more robust coherence baseline protocol such as `auto__cpmg` with `N=1` for a Hahn-echo-style coherence check. Use the result to decide whether r03 can still support a T2star/13C conclusion under current conditions or should be closed as unsupported for Ramsey/13C.
