# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job contract, `measurement/m003.json` completed bridge result, `measurement/m004.json` status, `measurement/m005.json` control.
- Planning/context evidence: `evidence/e005.json` for Ramsey model/protocol/readout basis; `evidence/e009.json` for submitted job copy.
- Generated local artifacts: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.

## Calculations or Scripts Run

- Used inline Python with `json`, `numpy`, `scipy.optimize`, and `matplotlib` to parse the exported arrays, compute readout1/reference, readout2/Ramsey signal, ratio `readout2/readout1`, average-by-average statistics, FFTs, and damped-sinusoid fits.
- Measurement dimensions checked as 4 averages, 2 readouts, 31 tau points over 0..6 us with 0.2 us spacing. Scan order is snake, but `ScanOrderInfo.data_saved_in_tau_order` is true.
- Readout basis used from `evidence/e005.json`: readout1 is mS=0 reference; readout2 is Ramsey signal for `full_experiment=0`.
- Quantitative checks:
  - Final bridge count was 38.249 kcps, above the 20 kcps gate but below the fresh pre-Ramsey track value of 43.535 kcps.
  - Reference mean 45.32 kcps with 8.6% span; signal mean 42.10 kcps with 18.4% span.
  - Ratio mean 0.9292 with 14.6% span; median per-point SEM across averages 0.0256.
  - Average ratio means were 0.9347, 0.9298, 0.9199, 0.9377; correlations of each average ratio trace with the mean trace were 0.68, 0.42, 0.58, 0.56.
  - FFT grid spacing from the actual 31-point sampled trace is 0.1613 MHz, with highest positive bin 2.419 MHz. The planned detuning is 1.5 MHz; expected 13C sideband scale from the project model is near 1.115 and 1.885 MHz.
  - Ratio FFT strongest bins: 0.968, 0.806, 0.323, 0.161, 1.935, 1.774 MHz. The nominal 1.5 MHz carrier is not the dominant averaged feature.
  - Free exponential-envelope sinusoid fit to the ratio: frequency 0.901 +/- 0.040 MHz, T = 2.04 +/- 0.91 us, R2 = 0.40, residual RMS 0.0259, about the same as the median SEM.
  - Gaussian-envelope fit gives similar weak support: frequency 0.886 MHz, T = 2.98 us, R2 = 0.37.
  - Forced 1.5 MHz exponential fit is worse: T = 0.50 us, R2 = 0.19.

## Plausible Interpretation

- The Ramsey scout is analyzable and shows a modulation in the reference-normalized signal with a few-percent-to-10% scale. The modulation is strong enough to justify targeted follow-up, but it is not cleanly locked to the programmed 1.5 MHz carrier.
- A plausible descriptive fit is a short few-us decay with an apparent oscillation near 0.9 MHz. This could reflect residual detuning from the weak-pODMR grid center, drift, or a mixture of real Ramsey phase evolution with readout/count fluctuations.
- The scan remains consistent with r03 being the target aligned NV from prior pODMR evidence; this Ramsey scout does not invalidate that earlier alignment conclusion.

## Claims Not Yet Supported

- Do not claim a final T2star from this scout. The best free fit has low explanatory power and average-by-average frequency content is not consistent enough.
- Do not claim 13C coupling. Bins near the expected sideband region exist, especially around 1.935/1.774 MHz and 1.129 MHz in raw signal, but they are not a clean, reproducible sideband pair and the reference readout also has power in the upper-frequency region.
- Do not claim the true Ramsey carrier is 0.9 MHz without follow-up. The result is descriptive, not yet a calibrated resonance/frequency conclusion.
- Do not claim absence of 13C. The 6 us scout has limited resolution/SNR, and the unstable average-wise spectra make a negative conclusion premature.

## Recommended Next Action

Repeat Ramsey on r03 with a better-centered microwave frequency and stronger frequency/T2star leverage: first run a narrow weak-pi pODMR or short Ramsey frequency-centering check around 3.876 GHz, then run a longer or higher-SNR Ramsey if counts remain stable. Use the new center to target a clean carrier and only then fit T2star and inspect FFT sidebands for 13C.
