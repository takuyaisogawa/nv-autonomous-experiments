# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md` for project objective and prior conclusions.
- `measurement/m002.json` for the submitted Ramsey plan: accepted target `image145844_reimage_r03`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, `8 x 50000` repetitions.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json` for terminal result/status/control. The run completed safely as `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`; final counts were `44.184 kcps`.
- `measurement/m001.json` for the raw savedexperiment export: two readout channels, combined data, per-average data, errors, and snake scan order.
- Prior context from `evidence/e013.md` and `evidence/e006.md`: fine weak-pi pODMR supports the grid center `3.8759 GHz`; this second Ramsey was intended to test a `1.0 MHz` carrier, expected 13C sidebands near `0.615/1.385 MHz`, and the earlier non-claim-grade `~0.884 MHz` component.

## Calculations/scripts run

- Used inline Python with `json`, `numpy`, `scipy.optimize`, and non-interactive `matplotlib` to inspect `measurement/m001.json`.
- Generated `ramsey_analysis_summary.txt` and `ramsey_analysis.png` in this directory.
- Checks performed:
  - Confirmed tau grid: 41 points from `0.0` to `8.0 us`, `dt = 0.200 us`, FFT bin spacing `0.122 MHz`, effective rFFT top bin `2.439 MHz`.
  - Computed raw channel means: readout 0 `49.313 kcps`, readout 1 `44.580 kcps`.
  - Computed per-average common-mode means: `50.40, 45.56, 43.76, 52.38, 48.45, 43.78, 38.34, 52.90 kcps`; average 7 is flagged by a simple `>15%` median-deviation rule.
  - Analyzed signal/reference normalized contrast. Combined ratio contrast has `19.64%` peak-to-peak and `3.29%` rms.
  - Windowed FFT of normalized contrast: strongest non-DC bin at `1.098 MHz` with `2.30%` contrast amplitude.
  - Least-squares sinusoid checks with offset and linear baseline:
    - `0.884 MHz`: amplitude `0.86% +/- 0.76%`, `R2 = 0.040`.
    - `0.615 MHz`: amplitude `1.22% +/- 0.75%`, `R2 = 0.073`.
    - `1.000 MHz`: amplitude `1.08% +/- 0.74%`, `R2 = 0.061`.
    - `1.385 MHz`: amplitude `0.97% +/- 0.74%`, `R2 = 0.050`.
  - Recomputed normalized checks excluding the common-mode-low average 7; the strongest FFT bin remained near `1.098 MHz`, so the basic spectral conclusion is not created solely by that average.
  - Exploratory decaying-cosine fits across several seeds can find a local fit near `f = 1.202 MHz`, `T = 0.95 us`, `R2 = 0.496`, but this is model-dependent and not claim-grade.

## Plausible interpretation

- The run completed and returned analyzable Ramsey-like contrast, but the expected detuning carrier is not cleanly supported. The strongest FFT bin is near `1.098 MHz`, close to but not exactly the programmed `1.0 MHz`; fixed-frequency least-squares at `1.0 MHz` explains only about `6%` of the variance.
- The prior `~0.884 MHz` component did not persist strongly in the det-shifted data. That makes a fixed, repeatable `0.884 MHz` physical feature less plausible, though the present data are not clean enough to use this as a strong exclusion.
- The expected 13C sideband positions near `0.615` and `1.385 MHz` are not supported as distinct features. Their fitted amplitudes are small, formal uncertainties are comparable to the amplitudes, and per-average amplitudes are inconsistent.
- There may be a short-lived Ramsey contrast component with sub-microsecond to about `1 us` decay, but the fitted `T2*` depends strongly on model choice and weak spectral evidence.

## Claims not yet supported

- Do not claim a reliable `T2*` value from this run.
- Do not claim resolved 13C coupling or absence of 13C coupling from this run alone.
- Do not claim the Ramsey carrier is definitively at `1.0 MHz`; the data show weak content near `1.1 MHz` and poor fixed-frequency explanatory power.
- Do not claim the `0.884 MHz` feature from the first scout is physical; this run weakens that idea but does not prove the artifact/noise mechanism.

## Recommended next action

Pause repeating Ramsey as-is. First run a short, targeted frequency/control check before spending more long Ramsey time: repeat or bracket the weak-pi pODMR center around `3.8759 GHz` after this Ramsey, and if the center is still supported, run a shorter high-SNR Ramsey/control pair around `0..4 us` with the same `det=1.0 MHz` plus a deliberately changed detuning. The goal is to verify that the Ramsey carrier follows the programmed detuning and that the early-time contrast is reproducible before making any `T2*` or 13C claim.
