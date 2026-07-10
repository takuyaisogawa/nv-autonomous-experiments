# Ramsey Review: r03 First T2star Scout

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: objective, current candidate status, and planned Ramsey analysis criteria.
- `context.json`: confirms this checkpoint contains terminal Ramsey measurement data after the prior wake had started the run.
- `measurement/m002.json`: submitted Ramsey job contract for `nv23_ramsey_20260513_185505_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result/status/control. The run completed, saved `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`, and reported final counts `38.249 kcps`.
- `measurement/m001.json`: raw savedexperiment export used for the quantitative analysis. It contains `ExperimentData` with shape `1 x 2 x 31`, `ExperimentDataEachAvg` with shape `1 x 4 x 2 x 31`, tau `0..6 us` in `31` points, and snake acquisition order saved back in tau order.

## Calculations or scripts run

Scratch outputs were written under `ramsey_scratch/`:

- `ramsey_scratch/analysis_summary.txt`
- `ramsey_scratch/ramsey_review_plots.png`

Checks run locally in Python:

- Loaded `measurement/m001.json`; treated readout 0/readout 1 as the Ramsey contrast ratio for raw/readout-aware review.
- Computed tau sampling: `dt = 0.200 us`, FFT bin spacing `0.161 MHz`, Nyquist `2.500 MHz`.
- Computed combined raw readout statistics:
  - readout 0 mean/range: `45.318 kcps`, `44.038..47.942 kcps`
  - readout 1 mean/range: `42.098 kcps`, `38.096..45.846 kcps`
  - ratio mean/range: `1.077617`, `1.005453..1.164059`
  - normalized ratio peak-to-peak: `14.72%`
- Per-average mean ratio: `1.074544`, `1.079174`, `1.091064`, `1.071287`.
- Per-average top FFT frequencies for the normalized ratio were not stable: `0.968`, `1.452`, `1.129`, and `0.806 MHz`.
- Combined detrended/windowed FFT top non-DC peak was `0.968 MHz`, amplitude `0.1857`; median non-DC amplitude `0.1228`; top/median only `1.51`.
- Simple damped-cosine fits to the combined normalized ratio:
  - exponential envelope: `T2star ~ 2.289 +/- 1.112 us`, frequency `0.9472 +/- 0.0353 MHz`, `R2 = 0.435`
  - Gaussian envelope: `T2star ~ 3.122 +/- 1.031 us`, frequency `0.9456 +/- 0.0393 MHz`, `R2 = 0.427`

## Plausible interpretation

The run completed and the raw ratio has real-looking Ramsey-scale modulation, but the measurement is not strong enough for a well-supported T2star or 13C conclusion. The combined fit prefers an oscillation near `0.95 MHz` and a few-us decay scale, but the fit explains less than half of the variance and the fitted decay depends on the envelope model. The per-average spectra disagree substantially, and the combined FFT peak is only `1.5x` the median non-DC FFT amplitude.

The planned Ramsey detuning was `1.5 MHz`; one average has its strongest FFT component near that value, but the combined data and other averages do not. This could reflect drift, phase instability, insufficient SNR, imperfect normalization/reference behavior, or that the effective Ramsey phase evolution did not match the intended detuning. It should not be reduced to a physical field or coupling claim without a cleaner repeat.

## Claims that are not yet supported

- A numeric T2star for r03 is not yet supported. The rough fit values around `2..3 us` are descriptive only.
- A nearby 13C conclusion is not supported. There is no robust carrier plus sideband pattern, and no stable feature at the expected `~0.385 MHz` separation scale.
- The discrepancy between the intended `1.5 MHz` detuning and the combined `~0.95 MHz` fit/FFT feature is not explained by this dataset alone.
- This dataset does not invalidate r03 as the aligned candidate; the prior strong-pi and weak-pi pODMR evidence still supports using r03 for targeted follow-up.

## Recommended next action

Repeat a bounded Ramsey scout on r03 before claiming T2star or 13C. Keep the weak-pi pODMR frequency basis, but improve claim quality by reducing per-average drift risk and checking the detuning behavior explicitly. A practical next run is a shorter-tracking-window repeat with the same order of tau span and at least the same total averages, or a small detuning sanity check if bridge overhead permits. After the repeat, require per-average agreement, a clear carrier near the programmed detuning, and a stronger FFT/fit before fitting T2star or interpreting 13C sidebands.
