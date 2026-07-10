# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`.
- Completed Ramsey artifacts:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
  - `measurement/m002.json`: executed job spec for `nv23_ramsey_20260513_185505_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result, status `completed`.
  - `measurement/m004.json`: terminal bridge status, elapsed time `2124 s`.
  - `measurement/m005.json`: run control, no stop requested.
- Prior supporting evidence/context: `evidence/e005.json` through `evidence/e011.json` for Ramsey plan/advisory/submission/status; prior r03 weak-pODMR context from project state.

## Calculations or scripts run

- Used local Python to inspect JSON schemas and raw array dimensions.
- Analyzed `measurement/m001.json` with a scratch Python workflow saved under `scratch_ramsey_analysis/`:
  - Built tau axis from `0..6 us`, `31` points, `dt = 0.2 us`; `4` averages x `50000` repetitions.
  - Used readout2/readout1 as the primary common-mode-normalized Ramsey trace; also checked raw readout means and per-average ratios.
  - Fit averaged ratio to descriptive damped-cosine models:
    - Gaussian envelope fit: `f = 0.942 MHz`, `T = 3.21 us`, `R2 = 0.43`.
    - Exponential envelope fit: `f = 1.517 MHz`, `T = 0.78 us`, `R2 = 0.14`.
  - FFT of averaged ratio after median normalization/Hann window:
    - bin spacing `0.161 MHz`.
    - largest bins: `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `0.161 MHz`, `1.935 MHz`, `1.774 MHz`.
    - planned detuning bin near `1.5 MHz` was weak (`nearest 1.452 MHz`), not dominant.
    - expected rough 13C sideband bins for `1.5 +/- 0.385 MHz` were not cleanly supported.
  - Frequency-scan sinusoid checks:
    - mean trace best fixed-envelope sinusoid near `0.948 MHz`, `R2 = 0.28`.
    - at `1.5 MHz`, mean-trace sinusoid `R2 = 0.015`.
    - per-average best frequencies were inconsistent: about `0.928`, `0.515`, `1.301`, and `0.861 MHz`.
    - per-average centered-shape correlations were weak/mixed, with max off-diagonal correlation only about `0.28`.
  - Saved plot: `scratch_ramsey_analysis/ramsey_ratio_fit_fft.png`.
  - Saved numeric summary: `scratch_ramsey_analysis/summary.json`.

## Plausible interpretation

- The Ramsey job completed and produced analyzable data, but this scout does not give claim-grade T2star or 13C evidence.
- The averaged ratio contains low-contrast oscillatory structure, but the preferred frequency depends strongly on model choice and averaging. The planned `det = 1.5 MHz` carrier is not a strong feature of the averaged FFT or fixed-frequency sinusoid check.
- Per-average behavior is the main weakness: individual averages do not share a stable oscillatory shape, fitted frequencies scatter, and sinusoidal fits explain little variance in most averages. This is more consistent with drift/noise/sequence or frequency-setting mismatch than with a clean Ramsey decay.
- A descriptive Gaussian-envelope fit could be quoted only as a non-final characterization of the averaged trace (`T ~3.2 us`, `f ~0.94 MHz`, low `R2`), not as a supported T2star result.

## Claims not yet supported

- A well-supported T2star value is not established.
- A 13C coupling conclusion is not established; there is no robust pair of sidebands around the planned Ramsey carrier at the expected `~0.385 MHz` separation.
- The planned detuning carrier at `1.5 MHz` is not confirmed in this measurement.
- This run does not invalidate r03 as the aligned NV; prior pODMR evidence still supports r03 as the targeted candidate, but the Ramsey scout itself is not conclusive.

## Recommended next action

- Do not make final T2star or 13C claims from this scout.
- Before repeating Ramsey, check the Ramsey frequency convention and sequence implementation against the `det` setting, because the strongest averaged structure is nearer `0.9-1.0 MHz` than `1.5 MHz`.
- Then run a focused follow-up on r03 with either:
  - a shorter, higher-SNR Ramsey centered on the actually observed oscillation scale after confirming the detuning convention, or
  - a repeat at the intended carrier only if the frequency-setting path is verified.
- Include enough repeated averages to require per-average reproducibility before fitting T2star or interpreting FFT sidebands.
