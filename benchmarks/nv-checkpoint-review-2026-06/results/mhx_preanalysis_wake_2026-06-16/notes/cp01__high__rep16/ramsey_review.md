# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior r03 resonance/model context: `evidence/e003.json`, `evidence/e004.json`, `evidence/e005.json`.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export, plus `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status, and `measurement/m005.json` control state.
- Generated local artifacts: `ramsey_analysis_summary.json`, `ramsey_review_overview.png`, `ramsey_review_fft.png`, `ramsey_review_fit.png`.

## Calculations or scripts run

- Ran local Python/numpy/scipy/matplotlib inspection from the working directory.
- Parsed `measurement/m001.json`; confirmed `ramsey.xml`, `tau = 0..6 us`, 31 points, `dt = 0.2 us`, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `4 x 50000` shots, `full_experiment = 0`.
- Used the inspected protocol basis from `evidence/e005.json`: readout 1 is the `mS=0` reference and readout 2 is the Ramsey signal.
- Computed raw readout statistics, signal/reference normalization, signal/reference-line normalization, per-average behavior, snake-order common-mode drift, detrended Hann-window FFTs, and descriptive fits.
- Key numerical checks:
  - Terminal bridge result completed without abort; final count text was `38.249 kcps`.
  - Mean raw reference/signal were `45.318/42.098 kcps`.
  - Raw signal peak-to-peak range was `7.75 kcps`; median pointwise SEM across stored averages was about `1.01 kcps`.
  - Per-average signal means were `43.365, 40.553, 42.797, 41.677 kcps`; per-average ratio means were `0.9347, 0.9298, 0.9199, 0.9377`.
  - Simple acquisition-order common-mode drift scores were modest by the prior 15% flag threshold: avg 2 drop `3.5%`, avg 3 drop `3.0%`, avg 1/4 did not show a net drop by this check.
  - Detrended FFT bin spacing from `np.fft.rfftfreq` is `161.3 kHz` for the 31 inclusive samples; nominal span resolution is `166.7 kHz`.
  - The strongest combined-view FFT feature is near `0.968 MHz`, not the programmed `1.5 MHz` carrier.
  - Expected first-order 13C sideband scale from the planning model is `det +/- 0.385 MHz`, i.e. about `1.115` and `1.885 MHz`.
  - Target-bin checks were not persuasive: in raw signal, carrier/lower/upper target-bin ranks were `13/5/11`; in ratio they were `12/11/4`; in line-normalized signal they were `13/5/11`.
  - Per-average FFT peaks were not stable across averages, and pairwise detrended correlations were low: raw signal roughly `0.20..0.33`, ratio roughly `-0.11..0.26`.
  - Best descriptive raw exponential-envelope fit preferred about `0.962 MHz`, amplitude `3.18 kcps`, `T ~ 2.06 us`, with only `R2 = 0.48`; the ratio fit similarly preferred about `0.941 MHz`, `T ~ 2.39 us`, `R2 = 0.45`. These are descriptive only.

## Plausible interpretation

- The Ramsey execute itself is valid as a completed scout: correct sequence, intended tau grid, expected readout roles, no stop request, no abort, no zero-average failure, and counts stayed above the minimum gate.
- There is oscillatory-looking structure in the Ramsey signal. A feature near `0.95..0.97 MHz` appears in the combined raw, ratio, and line-normalized FFT/fits.
- That feature could be a real Ramsey component if the effective detuning shifted by roughly several hundred kHz from the weak-pi pODMR center, which is plausible in ordinary NV/Ramsey terms and consistent with some count/drift change since weak pODMR.
- However, the evidence is not claim-grade: the programmed `1.5 MHz` carrier is weak, the fitted frequency is not the planned carrier, the fit quality is low, and per-average FFT/correlation checks do not show stable repeatable structure.

## Claims not yet supported

- No supported numeric `T2star` claim. The `~2 us` descriptive fit is not robust enough to use as a project conclusion.
- No supported nearby `13C` claim. FFT amplitudes at the expected `det +/- 0.385 MHz` sideband bins are inconsistent across normalizations and not stable across averages.
- No supported conclusion that the r03 weak-pi pODMR center was wrong. The Ramsey scout only suggests a possible residual detuning; it does not prove a shifted resonance.
- No supported conclusion that r03 is unsuitable. The prior pODMR alignment evidence still stands; this scout is mainly a non-claim-grade Ramsey/T2star data-quality result.

## Recommended next action

Before spending on a longer/high-SNR Ramsey, re-check the r03 resonance with a short weak-pi pODMR or equivalent frequency diagnostic near `3.876 GHz`, because the Ramsey scout did not put its strongest feature at the programmed `1.5 MHz` detuning. If the center is stable or corrected, repeat Ramsey with a design that preserves even averages and the FFT guard for `det +/- ~0.385 MHz`; improve claim strength by adding stored averages rather than extending the per-average tracking window blindly.
