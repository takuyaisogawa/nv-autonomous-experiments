# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`: project objective and prior accepted r03 context.
- `measurement/m001.json`: raw exported Ramsey scan from `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job contract.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result, status, and control metadata.
- Prior context from `project/state.md`: r03 accepted from strong/weak pODMR; weak-pi resonance grid point `3.876 GHz`; pre-Ramsey count text `43.890 kcps`; expected `13C` separation about `0.385 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Script outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- Checks performed:
  - Loaded raw averaged readouts and per-average readouts.
  - Used readout 1 as the true-0/reference readout and readout 2 as the Ramsey readout, consistent with `ramsey.xml` sequence text.
  - Computed signal/reference traces per average and for the combined trace.
  - Checked scan geometry: `tau=0..6 us`, `31` points, `dt=0.2 us`, `4` averages, `50000` repetitions, `mw_freq=3.876 GHz`, `det=1.5 MHz`, `full_experiment=0`.
  - Checked count/drift scale: final bridge count `38.249 kcps`, about `12.9%` below the weak-pODMR final count `43.890 kcps`; per-average reference means `43.68..46.59 kcps`, signal means `40.55..43.36 kcps`.
  - FFT on linearly detrended, Hann-windowed normalized Ramsey trace.
  - Simple weighted damped-cosine fits with exponential and Gaussian envelopes.
  - Per-average reproducibility check via ratio-trace correlations and target-bin FFT amplitudes.

## Plausible interpretation

- The Ramsey run completed and is analyzable, but this first scout is not claim-grade.
- The normalized signal/reference ratio has mean `0.9306`, tau-dependent standard deviation `0.0339`, and median point SEM across four averages `0.0256`; the modulation scale is comparable to per-point average scatter.
- Per-average normalized trace correlations are weak; mean off-diagonal correlation is about `0.09`, so the apparent structure in the averaged trace is not strongly reproducible average-to-average.
- FFT bin spacing is `161.3 kHz` for the 31-point sampled record; Nyquist is `2.5 MHz`.
- The expected Ramsey carrier target `1.5 MHz` maps to the `1.452 MHz` bin, but that bin is not enhanced: amplitude `0.089`, rank `12/15` among nonzero bins, `0.76x` the median nonzero-bin amplitude.
- The expected `det - 13C` sideband target near `1.115 MHz` maps to `1.129 MHz`, amplitude `0.093`, also not enhanced.
- The `det + 13C` sideband target near `1.885 MHz` maps to `1.935 MHz`, amplitude `0.156`, rank `3/15`, `1.33x` the median nonzero-bin amplitude; by itself this is weak and asymmetric evidence, not a supported `13C` signature.
- Free damped-cosine fits are poor and unstable:
  - Exponential envelope: `f=1.688 +/- 0.032 MHz`, `T2*=3.16 +/- 2.13 us`, `R2=0.17`.
  - Gaussian envelope: `f=1.831 +/- 0.099 MHz`, `T2*=3.68 +/- 3.17 us`, `R2=0.076`.
- These fits are best treated as descriptive fits to noisy, low-reproducibility structure, not as physical T2* estimates.
- The result does not invalidate the prior r03 alignment evidence from pODMR, but it does show that this Ramsey scout is insufficient for the requested T2* and `13C` conclusions.

## Claims that are not yet supported

- No well-supported T2* value is supported by this Ramsey scout.
- No well-supported `13C` coupling/signature is supported.
- The observed `1.935 MHz` FFT-bin feature is not enough to claim a `det + 13C` sideband because the carrier and lower sideband are not correspondingly supported and per-average reproducibility is weak.
- The free-fit frequencies and decay constants should not be used as calibrated resonance detuning or T2* claims.
- The count drop and tracked-position shift during the Ramsey run should not be interpreted as spectroscopy evidence by themselves.

## Recommended next action

Before spending time on a longer `13C`-specific acquisition, re-establish r03 measurement quality: retrack/verify counts and repeat a compact weak-pi pODMR or equivalent resonance check near `3.876 GHz`. If the resonance and counts are still acceptable, repeat Ramsey with higher SNR and stronger drift control, then require a reproducible carrier near the programmed detuning across individual averages before fitting T2* or interpreting sidebands.
