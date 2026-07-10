# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`.
- Ramsey raw export: `measurement/m001.json`, savedexperiment path `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Ramsey job/terminal metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Planning/model context: `evidence/e005.json` plus the prior weak-pi pODMR review summary in `project/state.md`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.
- Checked raw readout 1/reference and readout 2/signal, signal/reference, signal over fitted reference line, per-average means/ranges, across-average SEM, linear-detrended Hann FFT peaks, and simple damped-cosine fits.

Key quantitative checks:

- Acquisition matches the planned scout: `ramsey.xml`, tau `0..6 us`, 31 points, `0.2 us` step, 4 averages x 50000 repetitions, `mw_freq=3.876 GHz`, `det=1.5 MHz`.
- Mean readouts: reference `45.32 kcps`, signal `42.10 kcps`; signal/reference mean `0.929`.
- Variation/noise scale: signal std over tau `1.44 kcps`; mean exported signal error `1.82 kcps`; mean across-average signal SEM `1.06 kcps`.
- Per-average common-mode movement is nontrivial: average signal means range `40.55..43.36 kcps`, reference means `43.68..46.59 kcps`.
- Pooled ratio FFT, after linear detrend and Hann window, has the largest peak at `0.968 MHz`; adjacent/other strong bins are `0.806`, `0.323`, `1.935`, and `1.774 MHz`.
- The expected programmed-carrier bin near `1.5 MHz` is at `1.452 MHz` with lower amplitude than the largest peaks. Expected 13C sideband bins for `det +/- 0.385 MHz` are near `1.129 MHz` and `1.935 MHz`; the high-side bin is present but not accompanied by a clean carrier/low-sideband pattern.
- Per-average FFT peaks are inconsistent: average 1 favors `0.968 MHz`, average 2 favors `1.452/1.935 MHz`, average 3 favors `0.323/1.129/1.290 MHz`, and average 4 favors `0.806 MHz`.
- Damped-cosine fit on signal/reference with fixed `1.5 MHz` carrier gives a poorly constrained short decay (`T2 ~0.38 +/- 0.34 us`) and only marginal improvement over a linear baseline (`delta AIC ~ -0.73`).
- A free-frequency damped-cosine fit on signal/reference prefers `0.941 +/- 0.035 MHz`, amplitude about `0.067` in normalized units, and `T2 ~2.39 +/- 1.19 us`; the analogous raw-signal fit gives `0.962 +/- 0.036 MHz`, amplitude about `3.18 kcps`, and `T2 ~2.06 +/- 0.91 us`.

## Plausible interpretation

- The accepted r03 NV likely produced a Ramsey-like oscillatory response at the few-kcps scale expected from the prior weak-pi pODMR contrast.
- The dominant oscillation is not centered at the programmed `1.5 MHz` carrier. A plausible explanation is an effective Ramsey detuning or resonance-center mismatch of roughly `0.5..0.6 MHz`, which is within the coarse `1 MHz` weak-pi pODMR grid scale and comparable to the pre-run center-uncertainty guard.
- The scout is therefore useful as a frequency/quality diagnostic, but not yet as a claim-grade T2star measurement. The free-frequency fit suggests an apparent coherence scale of order `2 us`, but this should be treated as a redesign input, not a final T2star.
- The FFT does not provide a supported 13C conclusion. The high-side expected sideband region is not enough by itself because the carrier is weak/misaligned and the per-average spectral content is not stable.

## Claims that are not yet supported

- A well-supported numeric T2star for r03.
- A supported nearby-13C coupling claim.
- A supported no-13C conclusion.
- A precise Ramsey resonance shift or sign of the effective detuning error.
- Attribution of the non-1.5 MHz carrier to a specific physical cause rather than sequence phase convention, residual detuning, drift, or analysis/noise.

## Recommended next action

Do not run a blind longer Ramsey from this center. First refine the effective resonance/Ramsey carrier for r03: run a finer weak-pi pODMR or short Ramsey frequency diagnostic around the `3.876 GHz` grid minimum, with spacing small compared with `0.5 MHz`. Then repeat the Ramsey/T2star measurement using the updated center and a grid that cleanly resolves the programmed carrier and expected `~0.385 MHz` 13C sidebands while respecting the per-average drift cap.
