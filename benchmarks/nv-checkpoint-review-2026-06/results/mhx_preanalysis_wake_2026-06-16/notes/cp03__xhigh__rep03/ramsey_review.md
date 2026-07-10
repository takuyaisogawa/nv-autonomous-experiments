# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior short-tau design context: `evidence/e017.md`, `evidence/e009.json`.
- New terminal measurement bundle:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: submitted job/spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: control state.
- Scratch output: `ramsey_shorttau_diagnostic.png` generated from local data.

## Calculations/scripts run

- Used inline Python from this working directory with `json`, `numpy`, `scipy`, and `matplotlib`; no external data or web sources were used.
- Parsed `m001` arrays:
  - `ExperimentData` shape `(1, 2, 41)`.
  - `ExperimentDataEachAvg` shape `(1, 12, 2, 41)`.
  - tau grid: `0.048..1.968 us`, `48 ns` spacing, 41 points.
- Checked run metadata from `m002`-`m005`:
  - `auto__ramsey`, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` repetitions.
  - Completed normally, final text count `35.122 kcps`, no stop request, no monitor error.
- Quantitative raw/readout checks:
  - Reference readout mean/range: `48.573 kcps`, `47.568..49.744 kcps`.
  - Signal readout mean/range: `44.655 kcps`, `40.698..47.197 kcps`, peak-to-peak `6.499 kcps`.
  - Signal/reference ratio mean/range: `0.9195`, `0.8396..0.9829`, peak-to-peak `0.1433`.
  - Median per-tau SEM from stored averages: signal `1.138 kcps`, reference `1.120 kcps`, ratio `0.0127`, matching the planned `~1.17 kcps` raw SEM scale.
- Drift/provenance checks:
  - Stored-average signal means span `37.47..51.21 kcps`; reference means span `42.02..55.19 kcps`.
  - Ratio average means are more stable but still span `0.893..0.956`.
  - Forward-vs-reverse snake average means differ in ratio by about `-0.022`, so drift/baseline provenance remains material even without a hard run anomaly.
- Frequency/fit screens:
  - Linear-baseline least-squares amplitudes on raw signal:
    - `0.615 MHz`: `1.10 kcps`.
    - `1.000 MHz`: `1.28 kcps`.
    - `1.385 MHz`: `1.22 kcps`.
  - Same screen on ratio:
    - `0.615 MHz`: `0.0243`.
    - `1.000 MHz`: `0.0274`.
    - `1.385 MHz`: `0.0271`.
  - Linear-detrended FFT bins are largest near `0.508 MHz` and `1.016 MHz`; the `1.524 MHz` bin is smaller. The short `1.92 us` span gives coarse frequency resolution.
  - Free-frequency linear-baseline LS prefers about `1.187 MHz` on raw signal and `1.192 MHz` on ratio; a quadratic-baseline ratio screen gives about `1.198 MHz`.
  - Fixed-`1.0 MHz` decay profiles can force short apparent T2* values (`~0.16..0.37 us` depending on exponential/Gaussian model and readout), but when frequency is allowed to vary the best fits move to `~1.18..1.21 MHz` with long/weakly bounded envelopes. The T2* value is therefore model-dependent and not claim-grade.

## Plausible interpretation

- The diagnostic succeeded technically and reached the intended shot-budget/no-tau0 regime.
- The data contain a reproducible early-time oscillatory/readout shape above the pointwise noise scale; this is stronger evidence for a Ramsey-like signal than the prior weak carrier screens.
- The strongest descriptive frequency remains near `1.19 MHz`, close to the earlier det=`1.0 MHz` long-window feature near `1.178 MHz`, rather than cleanly locking to the programmed `1.000 MHz` carrier or a resolved `13C` sideband model.
- Plausible explanations include resonance drift or detuning offset relative to the fine pODMR center, a sequence/timing/systematic artifact, or a real Ramsey component whose frequency is not yet calibrated. This dataset alone does not separate those cases.

## Claims not yet supported

- No supported numeric T2* claim. Fixed-carrier fits are not stable against allowing the frequency to move.
- No supported nearby-`13C` claim. The short span was designed for early-time carrier visibility, not sideband resolution, and the `0.615/1.385 MHz` sideband screens are comparable to the carrier screen rather than distinct.
- No supported claim that the `~1.19 MHz` component is definitively physical NV precession; it needs a detuning/resonance-control check.
- No supported claim that r03 has completed the project objective for T2* or `13C`.

## Recommended next action

Do not run another blind Ramsey repeat. First recheck the r03 weak-pi pODMR center around `3.8759 GHz` with enough span to detect a `~0.2 MHz` shift. If the resonance has moved, update `mw_freq` and plan a longer, high-SNR Ramsey with adequate sideband resolution. If the resonance has not moved, use a deliberate detuning-dependence/control Ramsey or switch protocol before making T2*/`13C` claims.
