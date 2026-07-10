# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- New measurement: `measurement/m001.json` terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Bridge/job metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Prior context from `project/state.md`: r03 is the accepted aligned candidate with fine weak-pi center `mw_freq = 3.8759 GHz`; prior 6 us and 8 us Ramsey runs were analyzable but non-claim-grade for T2star/13C.

## Calculations or scripts run

- Used local Python to parse `measurement/m001.json`, extract `ExperimentData`, `ExperimentDataEachAvg`, tau axis, scan-order metadata, and per-average traces.
- Checked acquisition metadata: tau `0.048..1.968 us`, step `48 ns`, `41` points, `12` averages, `90000` reps/point, tracking per average, snake scan, and `data_saved_in_tau_order = true`.
- Computed raw difference `ch1 - ch0` and normalized difference `(ch1 - ch0)/(ch1 + ch0)`, with per-tau SEM from stored averages.
- Ran linear-detrended FFT screens and least-squares sinusoid screens at candidate frequencies.
- Ran fixed-1.0 MHz and free-frequency Gaussian-decay cosine fits with linear baseline.
- Wrote scratch artifacts: `ramsey_scratch_summary.txt` and `ramsey_shorttau_review.png`.

Key numerical checks:

- Raw signal: mean `-3.918 kcps`, tau SD `1.705 kcps`, median SEM `0.652 kcps`, peak-to-peak `7.044 kcps`.
- Normalized signal: mean `-0.04230`, tau SD `0.01909`, median SEM `0.00685`, peak-to-peak `0.07855`.
- FFT top components after linear detrend:
  - raw: `0.508 MHz` amp `1.460 kcps`, `1.016 MHz` amp `1.363 kcps`, `1.524 MHz` amp `0.671 kcps`.
  - normalized: `0.508 MHz` amp `0.01645`, `1.016 MHz` amp `0.01531`, `1.524 MHz` amp `0.00731`.
- LS amplitudes:
  - at `1.000 MHz`: raw `1.334 kcps`, normalized `0.01493`.
  - at `1.179 MHz`: raw `1.764 kcps`, normalized `0.01974`.
  - at `0.500 MHz`: raw `1.486 kcps`, normalized `0.01673`.
- Per-average 1 MHz amplitudes:
  - raw mean `1.383 kcps`, SD `0.567 kcps`, min/max `0.627/2.272 kcps`.
  - normalized mean `0.01537`, SD `0.00579`, min/max `0.00691/0.02396`.
- Fixed-1 MHz Gaussian-decay fits:
  - raw: `T2star = 0.365 +/- 0.081 us`, amplitude `-5.47 +/- 1.14 kcps`.
  - normalized: `T2star = 0.346 +/- 0.077 us`, amplitude `-0.0657 +/- 0.0139`.
- Free-frequency Gaussian-decay fits:
  - raw: `f = 0.886 +/- 0.183 MHz`, `T2star = 0.418 +/- 0.097 us`.
  - normalized: `f = 0.696 +/- 0.240 MHz`, `T2star = 0.347 +/- 0.137 us`.

## Plausible interpretation

- This short-tau/high-SNR run does show an early-time oscillatory Ramsey-like component in both raw and normalized views. That is a meaningful change from the prior 8 us run, where the programmed 1 MHz carrier was below/near SEM.
- The plausible working interpretation is very short apparent dephasing on r03, with T2star on the order of `0.35..0.42 us` under this measurement configuration.
- The short tau window and rapid decay make the carrier frequency poorly pinned. Power near `0.5 MHz`, `1.0 MHz`, and `~1.18 MHz` is close enough that the data do not uniquely support a clean det-following 1 MHz carrier model.
- The result supports the earlier concern that the previous long-window Ramsey scans may have missed most useful contrast by sampling too late or diluting the early-time decay.

## Claims that are not yet supported

- Do not claim a final T2star value yet. A short-T2star estimate around `0.35..0.42 us` is plausible, but it is model-dependent and frequency-ambiguous.
- Do not claim nearby `13C` coupling. The scan was optimized for early-time carrier visibility, not resolving 13C sidebands, and the frequency screens do not establish expected sidebands.
- Do not claim the oscillation frequency is exactly the programmed `1.0 MHz` detuning. Fixed-1 MHz fits work, but free-frequency fits move lower with broad uncertainty, and the `~1.18 MHz` LS screen is also strong.
- Do not interpret the smooth baseline/common-mode behavior as a resolved physical beat without additional controls.

## Recommended next action

Run a targeted confirmation measurement rather than another blind long-window Ramsey repeat: keep the same r03 target and `mw_freq = 3.8759 GHz`, sample an early window with dense points from roughly `48 ns` to `1.2 us`, include multiple phase settings or a quadrature Ramsey variant if available, and use enough averages to test whether the short `~0.35 us` decay and carrier phase reproduce. If quadrature/phase cycling is not readily available, repeat the short-tau scan once with a deliberately changed detuning so a real Ramsey carrier should shift while baseline/drift features should not. Only after carrier identity is confirmed should a T2star number be promoted or a 13C-sideband measurement be designed.
