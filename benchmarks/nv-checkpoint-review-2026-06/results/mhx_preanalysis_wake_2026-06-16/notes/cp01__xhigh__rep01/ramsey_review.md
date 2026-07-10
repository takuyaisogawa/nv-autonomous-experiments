# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`.
- Prior r03 support: `evidence/e003.json` weak-pi pODMR review supporting the 3.876 GHz grid resonance; `evidence/e005.json` Ramsey model/advisory with expected `13C` Larmor scale.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status.
- Measurement completed normally: `ramsey.xml`, tau `0..6 us`, 31 points, step `0.2 us`, `4 x 50000` repetitions, `mw_freq=3.876 GHz`, `det=1.5 MHz`, readout1 reference and readout2 Ramsey signal per local protocol context. Terminal final count was `38.249 kcps`, down from the pre-Ramsey fresh track count `43.535 kcps` but still above the job gate.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Checks performed:
  - Raw readout means and peak-to-peak ranges.
  - Signal/reference and signal/fitted-reference-line normalization.
  - Per-average signal/reference/common-mode behavior under the saved snake order.
  - FFT of detrended, windowed normalized Ramsey trace.
  - Descriptive free-frequency damped-cosine fit and fixed-frequency cosine fits at the programmed carrier and expected `13C` sidebands.

Key numbers:

- Mean reference `45.318 kcps`; mean signal `42.098 kcps`.
- Averaged signal peak-to-peak `7.75 kcps`; signal/reference peak-to-peak `0.1355`; signal/fitted-reference-line peak-to-peak `0.1734`.
- Median per-point SEM across stored averages: signal `1.015 kcps`, reference `1.011 kcps`.
- Per-average common-mode means vary by `6.3%` of their median; per-average dominant ratio FFT bins are inconsistent: about `0.968`, `1.452`, `0.323`, and `0.806 MHz`.
- Actual FFT bin spacing from 31 samples at `0.2 us` is `161.3 kHz`; endpoint-span shorthand is `166.7 kHz`; Nyquist is `2.419 MHz`.
- Working model from 3.876 GHz gives `B ~ 359.3 G`, `13C` Larmor `~0.385 MHz`; with `det=1.5 MHz`, expected sidebands are `~1.115 MHz` and `~1.885 MHz`.
- Dominant averaged FFT bin is `0.968 MHz`, amplitude `0.171`. Expected-bin amplitudes: carrier nearest `1.452 MHz` amplitude `0.071`, lower sideband nearest `1.129 MHz` amplitude `0.111`, upper sideband nearest `1.935 MHz` amplitude `0.077`; simple non-expected-bin median amplitude is `0.093`.
- Free damped-cosine descriptive fit on normalized data gives `f=0.964 MHz`, `T2*=2.04 us`, `R2=0.48`, RMSE `0.0226`. Fixed-frequency fits are poor: carrier `R2=0.005`, lower sideband `R2=0.041`, upper sideband `R2=0.034`.

## Plausible interpretation

This Ramsey scout is analyzable and shows a real-looking normalized modulation, but the modulation is not cleanly tied to the planned carrier. The strongest averaged FFT/free-fit feature is near `0.96-0.97 MHz`, not the programmed `1.5 MHz` carrier. That offset is plausibly compatible with residual microwave detuning at the scale expected from the weak-pi pODMR grid uncertainty, plus drift/limited SNR during the 35 minute run.

The data therefore support "possible Ramsey-like oscillation on r03, with a few-us-scale apparent envelope" as a scout-level observation. They do not yet support using the descriptive `T2*=2.04 us` fit as a final T2star result.

## Claims not yet supported

- A well-supported T2star value is not established. The only T2star number is a descriptive fit with moderate `R2` and an off-carrier frequency.
- A nearby `13C` conclusion is not established. The FFT does not show a clean carrier plus sideband pattern at `1.5 MHz` and `1.5 +/- 0.385 MHz`; the expected carrier bin is weak relative to the simple spectral floor.
- The data do not justify abandoning r03 or reopening broad candidate search. Prior pODMR evidence still supports r03 as the aligned candidate; this Ramsey run mainly indicates the frequency/T2star follow-up needs refinement.

## Recommended next action

Re-track r03 and run a targeted Ramsey frequency-centering follow-up before a longer T2star/`13C` acquisition. Use an even-average, shorter-window plan or split jobs if needed, and deliberately test/adjust the microwave frequency around `3.876 GHz` by the roughly `0.5 MHz` scale suggested by the off-carrier Ramsey feature. Once the Ramsey carrier is reproduced at the intended frequency with consistent per-average phase, run the higher-SNR/longer-span T2star Ramsey needed for a defensible T2star fit and `13C` sideband check.
