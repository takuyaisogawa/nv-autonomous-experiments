# Ramsey review: image145844_reimage_r03

## Files/data used

- `project/brief.md`, `project/advice.md`, and `project/state.md` for the project objective and current r03 status.
- `measurement/m002.json` for the Ramsey job plan: `tau = 0..6 us`, 31 points, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `4 x 50000` shots, validated `auto__ramsey` / `ramsey.xml`.
- `measurement/m003.json` and `measurement/m004.json` for terminal job status: completed, safe shutdown ok, final counts `38.249 kcps`, saved run `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`.
- `measurement/m001.json` for exported Ramsey data: `ExperimentData` plus `ExperimentDataEachAvg`, snake scan order, data saved in tau order.
- `md/knowledge.md` was checked for local Ramsey/FFT guardrails and the warning not to claim T2star or nearby 13C from weak/noisy bounded Ramsey scouts.

## Calculations/scripts run

- Ran local Python/Numpy/Scipy/Matplotlib inspection on `measurement/m001.json`.
- Created `ramsey_analysis_metrics.json` with extracted numerical metrics and `ramsey_analysis.png` showing raw readouts, pointwise signal/reference traces by average, and detrended FFT.
- Raw mean readouts: signal `45.318 kcps`, reference `42.098 kcps`; ranges were signal `44.038..47.942 kcps`, reference `38.096..45.846 kcps`.
- Pointwise signal/reference ratio: mean `1.0776`, range `1.0055..1.1641`, peak-to-peak variation `14.7%`.
- Per-average readout means show common-mode changes: avg1 `[46.44, 43.36] kcps`, avg2 `[43.68, 40.55] kcps`, avg3 `[46.59, 42.80] kcps`, avg4 `[44.56, 41.68] kcps`.
- FFT convention with 31 samples at `0.2 us` spacing gives bin spacing `161.3 kHz` and Nyquist `2.419 MHz` (the project planning estimate used the 6 us span, `166.7 kHz`). Expected `13C` Larmor from the 3.876 GHz resonance is about `0.384 MHz`, so `det +/- f13C` would be about `1.116 MHz` and `1.884 MHz`.
- Detrended FFT top bins were `0.968 MHz` (amplitude `2.04x` median non-DC), `0.323 MHz` (`1.32x`), `1.613 MHz` (`1.20x`), `0.806 MHz` (`1.19x`), and `1.935 MHz` (`1.13x`). The programmed `1.5 MHz` detuning is not the dominant bin.
- A descriptive damped-cosine fit can reduce residuals versus a line (`RSS 0.0227` vs `0.0398`) with best parameters `f = 0.941 MHz`, `T2star = 3.11 +/- 1.04 us`, `A = 0.057 +/- 0.016`, `R2 = 0.44`. This is not claim-grade because the fitted frequency is not at the programmed detuning, the FFT support is weak, and individual average FFT peaks do not agree.

## Plausible interpretation

- The Ramsey run completed and produced nonzero, normalized tau-dependent structure, so this is not a hardware/no-data failure.
- The trace is compatible with weak Ramsey-like modulation plus drift/common-mode readout variation, but the observed spectral content is not cleanly locked to `det = 1.5 MHz`.
- The fitted `T2star ~3 us` should be treated as a descriptive scale only. It is useful for planning the next measurement window, not as a supported T2star conclusion.
- The FFT has small peaks near the expected `det + f13C` sideband region (`1.935 MHz` bin near `1.884 MHz`) and lower-frequency structure near the expected `13C` Larmor scale, but peak heights are close to the non-DC background and are inconsistent across averages.

## Claims not yet supported

- No well-supported T2star value is established from this run.
- No nearby `13C` conclusion is established.
- Do not claim the `0.968 MHz` FFT/bin fit frequency as the real detuning without a repeat or independent frequency check.
- Do not interpret the `1.935 MHz` FFT bin as a `13C` sideband yet; its amplitude is only about `1.13x` the median non-DC FFT amplitude in the mean trace and per-average peaks are not stable.

## Recommended next action

Run a bounded Ramsey repeat on the same accepted r03 NV after a fresh track/ODMR-frequency check, with higher spectral confidence rather than a blind identical repeat. Practical options are: keep `det = 1.5 MHz` but increase SNR and, if runtime allows, extend to about `8 us` for finer FFT bins; or first run a quick weak-pi pODMR/recenter check because this Ramsey did not show a dominant 1.5 MHz carrier. The next Ramsey should be judged on raw/readout normalization, per-average reproducibility, and FFT support before fitting or making T2star/13C claims.
