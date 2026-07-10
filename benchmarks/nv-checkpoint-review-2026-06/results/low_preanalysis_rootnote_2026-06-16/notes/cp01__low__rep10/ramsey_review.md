# Ramsey review: r03 first T2star/13C scout

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior r03 acceptance context.
- `context.json`: checkpoint summary confirming that `measurement/` contains the later terminal Ramsey data and metadata.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job, `tau = 0..6 us`, 31 points, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `length_pi_pulse = 52 ns`, `4 x 50000`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result/status/control. Job completed; final text count was `38.249 kcps`.
- Generated local diagnostics: `ramsey_review_plot.png`, `ramsey_fft.png`.

## Calculations/scripts run

- Used inline Python/NumPy/SciPy/Matplotlib to inspect JSON structure, raw readouts, per-average data, damped-cosine fits, FFT bins, and diagnostic plots.
- Interpreted the two readouts using the sequence with `full_experiment=0`: readout 1 is the bright/0 reference and readout 2 is the Ramsey signal.
- Basic exported trace checks:
  - `tau` spacing: `0.2 us`, span `0..6 us`, 31 points.
  - Reference mean/range: `45.318 kcps`, `44.038..47.942 kcps`.
  - Ramsey-signal mean/range: `42.098 kcps`, `38.096..45.846 kcps`.
  - Signal/reference mean/range: `0.9292`, `0.8591..0.9946`.
  - Per-average signal/reference means: `0.9347, 0.9298, 0.9199, 0.9377`; span about `1.9%` of the mean.
  - Per-average raw reference means: `46.44, 43.68, 46.59, 44.56 kcps`; per-average raw signal means: `43.36, 40.55, 42.80, 41.68 kcps`.
- Damped cosine fits to signal/reference:
  - Exponential-envelope fit: `T2* = 0.43 us`, `f = 1.517 MHz`, `R2 = 0.15`, RMSE `0.0308` ratio units. This fit is not claim-grade.
  - Gaussian-envelope fit: `T2* = 3.21 us`, `f = 0.942 MHz`, `R2 = 0.43`, RMSE `0.0251` ratio units. This fit conflicts with the intended detuning and is not claim-grade.
  - Per-average exponential fits were inconsistent: `T2* ~14.2, 3.0, 2.8, 8.2 us` and `f ~1.50, 1.69, 1.30, 1.52 MHz`, with amplitudes changing sign/scale.
- FFT check on line-detrended, Hann-windowed signal/reference:
  - Bin spacing from the actual 31-point grid: `161.3 kHz`; Nyquist `2.419 MHz`.
  - Strongest bins: `0.968, 0.806, 0.323, 1.935, 1.774, 0.161, 0.645, 1.613 MHz`.
  - The intended `1.5 MHz` carrier is not a dominant isolated peak. Bins near the expected `det +/- 13C` scale (`~1.115` and `~1.885 MHz`) are not cleanly isolated either.

## Plausible interpretation

- The Ramsey scout completed and is analyzable, but this first 6 us trace does not provide a well-supported T2star or 13C conclusion.
- There is some oscillatory-looking structure and the global exponential fit can be forced near the programmed `1.5 MHz` detuning, but the fit quality is poor, the extracted envelope depends strongly on model choice, and per-average fits are not mutually consistent.
- The final-count drop to `38.249 kcps` and per-average common-mode variation suggest tracking/focus/drift may have degraded the Ramsey contrast during the long run, though the per-average ratio means only vary at the `~2%` level.
- The data are better treated as a non-claim-grade Ramsey scout than as evidence for a specific T2star or 13C coupling.

## Claims not yet supported

- A numerical T2star for r03 is not supported by this measurement.
- Presence or absence of nearby 13C coupling is not supported by this measurement.
- The observed FFT peaks should not be assigned to 13C sidebands.
- The low-R2 forced exponential fit near `1.5 MHz` should not be reported as a physical Ramsey fit.
- This result does not invalidate r03 as the aligned candidate; prior pODMR evidence still supports the target, but Ramsey follow-up quality is insufficient.

## Recommended next action

Run a focused Ramsey repeat on r03 under tighter drift control before changing target: retrack immediately before the run, keep even snake-ordered averages, and either shorten per-average duration or use fewer tau points around a span that still resolves the `~0.385 MHz` 13C scale. If the next trace again lacks a stable carrier/sideband structure, switch to a higher-SNR or drift-robust follow-up rather than making a T2star/13C claim from this scout.
