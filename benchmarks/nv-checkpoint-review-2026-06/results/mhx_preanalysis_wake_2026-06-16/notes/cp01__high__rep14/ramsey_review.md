# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, `measurement/m005.json` run control.
- Prior supporting context: `evidence/e001.json` through `evidence/e011.json`, especially the weak-pi pODMR and Ramsey planning/advisory records.
- Generated scratch artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_traces.png`, `ramsey_fft.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ramsey.xml` from the raw export. With `full_experiment=0`, readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
- Checked raw signal, reference, signal/reference ratio, per-average traces, point SEM across 4 stored averages, detrended/windowed FFT, bootstrap resampling over stored averages, permutation nulls for maximum FFT amplitude, and simple cosine / exponentially decaying cosine fits.
- Measurement grid: `tau = 0..6 us`, 31 points, `dt = 0.2 us`; FFT bin spacing from the sampled array is `161.3 kHz`, Nyquist is `2.419 MHz`.

## Plausible interpretation

- The Ramsey job completed normally and saved `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`. Final count text was `38.249 kcps`, down from the prior weak-pi pODMR final `43.890 kcps`, so drift/count change is relevant provenance.
- Mean raw readouts: reference `45.32 kcps`, signal `42.10 kcps`. The mean signal has a `7.75 kcps` peak-to-peak span; signal/reference has `0.1355` peak-to-peak span. Median point SEM across stored averages is about `1.01 kcps` for the signal and `0.0256` for signal/reference.
- Stored-average signal shapes are moderately correlated with the mean shape (`r = 0.60..0.71`), so the trace is not purely one-average behavior. However average means drift substantially: signal average means are `43.36, 40.55, 42.80, 41.68 kcps`; reference average means are `46.44, 43.68, 46.59, 44.56 kcps`.
- The strongest detrended/windowed FFT peak is near `0.968 MHz` in both signal and signal/reference. This is not the programmed `det = 1.5 MHz` carrier. A genuine Ramsey oscillation with an effective carrier closer to `1.0 MHz` is plausible, consistent with a resonance offset of order `0.5 MHz`, but this is not claim-grade from this scout.
- The all-point exponentially decaying cosine fit gives a descriptive `T2* ~ 2.06 us` and `f ~ 0.962 MHz` with `R2 ~ 0.48`, but this relies heavily on the low `tau=0` point. Excluding `tau=0`, the decaying fit loses explanatory power (`R2 ~ 0.06`, decay time hits the upper bound), so the fitted T2* should not be used as a result.
- FFT checks do not support a 13C assignment. The programmed carrier bin near `1.452 MHz` is rank 13 in the signal FFT and rank 12 in the ratio FFT. Expected sideband bins near `1.129 MHz` and `1.935 MHz` are not consistently dominant across signal and ratio. A permutation check gives non-significant maximum FFT amplitudes (`p ~ 0.57` for signal, `p ~ 0.69` for ratio).

## Claims that are not yet supported

- No well-supported T2* value is established by this Ramsey scout.
- No well-supported nearby-13C conclusion is established.
- The observed `~0.97 MHz` FFT/fitted frequency is not yet a confirmed physical detuning; it could include drift, endpoint/pulse-overlap behavior at `tau=0`, baseline/reference effects, or noise.
- The all-point descriptive `T2* ~ 2 us` fit is not supportable because it fails the endpoint-exclusion check.

## Recommended next action

Before a longer T2*/13C measurement, run a short targeted follow-up: fresh TrackCenter/count check plus a narrow weak-pi pODMR or Ramsey-frequency diagnostic to confirm whether the resonance has shifted by about `0.5 MHz`. Then repeat Ramsey on r03 with `tau=0` excluded or separately diagnosed, an even-average split that stays under the tracking-window cap, and enough averages/SNR to make the carrier and any `~0.385 MHz` 13C sidebands significant in both raw signal and reference-normalized views.
