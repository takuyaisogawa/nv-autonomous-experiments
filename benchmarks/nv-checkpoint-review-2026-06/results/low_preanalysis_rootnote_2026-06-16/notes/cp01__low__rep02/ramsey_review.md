# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior support for target selection: `evidence/e003.json` and `evidence/e004.json` for the r03 weak-pi pODMR review/drift context, plus `evidence/e005.json` through `evidence/e009.json` for the Ramsey model/advisory/job plan.
- New Ramsey terminal data and metadata: `measurement/m001.json` raw export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Scratch outputs created: `scratch_ramsey_analysis/ramsey_metrics.json` and `scratch_ramsey_analysis/ramsey_ratio_fft.png`.

## Calculations or scripts run

- Used local inline Python with `json`, `numpy`, `scipy.optimize.curve_fit`, and Matplotlib `Agg` to inspect the raw export, normalize readouts, fit damped cosines, compute FFTs, and save a diagnostic plot.
- Confirmed Ramsey scan shape: `ramsey.xml`, tau `0..6 us`, `31` points, `0.2 us` spacing, `4` averages x `50000` repetitions, two readout traces.
- Used `signal/reference` as the primary Ramsey observable. Aggregate trace means: reference `45.318 kcps`, signal `42.098 kcps`, ratio mean `0.9292`, aggregate ratio peak-to-peak `0.1355`.
- Per-average ratio means were stable at the few-percent level but noisy: averages 1-4 ratio means `0.9347`, `0.9298`, `0.9199`, `0.9377`; per-average correlations with the aggregate pattern were only `0.42..0.68`.
- Damped-cosine fits were weak:
  - Free-frequency fit to mean per-average ratio: frequency `1.682 MHz`, T2* `2.83 us`, but `R2 = 0.180` and RMSE `0.0302`.
  - Fixed `1.5 MHz` fit to mean per-average ratio: T2* `0.509 us`, but `R2 = 0.175` and T uncertainty was comparable to T.
  - Aggregate-ratio fits similarly had only `R2 ~ 0.20`.
- FFT check used linear detrending plus a Hann window. Nominal resolution is `1/6 us = 0.167 MHz`; Nyquist is `2.5 MHz`.
  - Largest mean-ratio FFT local peaks: `0.928 MHz`, `1.896 MHz`, `0.262 MHz`, `2.433 MHz`.
  - Amplitudes at expected locations: `1.500 MHz` carrier `0.0927`, lower expected 13C sideband `1.115 MHz` `0.1028`, upper expected sideband `1.885 MHz` `0.1585`; median spectral amplitude over `0.05..2.5 MHz` was `0.1181`.
- Checked terminal result warnings/status. The job completed without abort; final counts were `38.249 kcps`, safety shutdown was OK, and no zero-average/incomplete condition was reported.

## Plausible interpretation

- This is a valid completed Ramsey scout on accepted r03, not a hardware/count-gate failure.
- The raw normalized Ramsey observable shows fluctuations on the expected contrast scale, but the oscillatory decay is not cleanly resolved. The fitted frequency and T2* depend on model constraints, and the fits explain only about one fifth of the variance.
- The FFT does not give a clean carrier-dominated peak at the programmed `1.5 MHz` detuning. The strongest peaks are displaced; one peak near `1.896 MHz` is close to the expected upper `det + 13C` sideband scale, but the matching lower sideband is not comparably strong and the carrier is below the median spectral amplitude. This is at most a hint, not evidence for a 13C conclusion.
- The final count drop from the weak-pi pODMR final text (`43.890 kcps`) to Ramsey final counts (`38.249 kcps`) suggests drift or state/readout condition changes may have reduced Ramsey quality, although the run itself completed normally.

## Claims that are not yet supported

- A well-supported numerical T2* for r03 is not supported by this scout. Reporting either `~2.8 us` from the free fit or `~0.5 us` from the fixed-detuning fit would be over-interpreting low-R2, noisy data.
- A supported 13C coupling/splitting conclusion is not established. The FFT has a possible upper-sideband-scale feature, but no robust carrier plus symmetric sideband pattern.
- The existing r03 alignment claim remains supported by prior strong-pi and weak-pi pODMR evidence, but this Ramsey scout does not by itself strengthen that claim.

## Recommended next action

Repeat a targeted Ramsey on r03 under better drift/readout conditions before changing target. Use the same weak-pi frequency basis but improve claim power: re-track/check counts first, keep the run under the tracking cap, and either increase SNR at the same `0..6 us`/`0.2 us` grid or run a slightly longer/higher-point Ramsey if advisory permits. The next analysis should require a visibly repeatable per-average carrier near the intended detuning and a carrier-plus-sideband FFT pattern before making T2* or 13C claims.
