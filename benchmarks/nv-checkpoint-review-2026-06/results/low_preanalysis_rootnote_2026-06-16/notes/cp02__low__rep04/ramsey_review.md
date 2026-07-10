# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`.
- Measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_review_calc_summary.json`, `ramsey_review_ratio.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the second Ramsey run `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940`.
- Confirmed run status `completed`, final counts `44.184 kcps`, `tau = 0..8 us`, 41 points, `dt = 0.2 us`, nominal FFT resolution `0.125 MHz`, Nyquist `2.5 MHz`, 8 averages x 50000 reps.
- Used `signal/reference` as the main readout-aware Ramsey trace. Combined ratio mean was `0.9042` with standard deviation `0.0294`; extrema were strongly affected by the first few tau points (`min 0.8025` at `0 us`, `max 0.9721` at `1.2 us`).
- FFT of linearly detrended combined ratio gave largest exploratory peaks at `1.098 MHz` (`amp 0.0211`) and `1.220 MHz` (`amp 0.0188`); the nearest carrier-bin peak around `0.976 MHz` had smaller amplitude `0.0133`, and the lower 13C-sideband bin near `0.610 MHz` was weaker (`0.0076`).
- Fixed-frequency least-squares fits of combined ratio with intercept + slope + sinusoid:
  - `0.615 MHz` lower 13C sideband: amp `0.0111`, amp/SE `1.68`, R2 `0.074`.
  - `0.884 MHz` prior scout component: amp `0.0074`, amp/SE `1.10`, R2 `0.035`.
  - `1.000 MHz` programmed detuning carrier: amp `0.0092`, amp/SE `1.39`, R2 `0.053`.
  - `1.385 MHz` upper 13C sideband: amp `0.0084`, amp/SE `1.28`, R2 `0.046`.
- Per-average fits were not mutually reinforcing: individual averages showed different strongest target components, with some acquisition-order first/second-half shifts of a few percent in ratio.

## Plausible interpretation

- The second Ramsey run completed cleanly and is analyzable, with adequate count level and the intended sampling band for the planned detuning and expected 13C sidebands.
- The data show weak oscillatory structure near the planned carrier region, but the programmed `1.0 MHz` carrier is not the dominant or statistically strong component in the combined readout-aware trace.
- The prior scout's `~0.884 MHz` component does not persist as a supported fixed feature in this det-shifted run.
- The weak peaks around `1.10..1.22 MHz` could be a noisy/detuned Ramsey response, residual normalization/readout structure, drift/scan-order influence, or a mixture of weak physical signal and acquisition artifacts. The current evidence is not strong enough to distinguish these.

## Claims that are not yet supported

- No claim-grade T2star value is supported. A decay fit would be underconstrained because signal presence at a stable carrier is weak.
- No 13C conclusion is supported. Neither expected sideband near `0.615 MHz` nor `1.385 MHz` is strong or consistent enough in the combined and per-average checks.
- Do not claim that r03 lacks 13C coupling from this alone; the correct conclusion is non-detection/non-claim under this Ramsey configuration.
- Do not claim sub-grid resonance precision beyond the fine weak-pi pODMR grid-supported `mw_freq = 3.8759 GHz` basis already recorded in project state.

## Recommended next action

Stop blind Ramsey repeats on this branch. Use a targeted diagnostic before any T2star/13C claim: either recalibrate the resonance immediately with a short fine weak-pi pODMR/check centered near `3.8759 GHz` and then run a shorter, higher-SNR Ramsey around the observed `~1.1 MHz` response, or switch to a Hahn-echo/CPMG-N=1 baseline if the project goal can tolerate moving from T2star to a more robust coherence check. If staying with T2star, require a clear combined carrier and per-average phase/amplitude consistency before fitting T2star.
