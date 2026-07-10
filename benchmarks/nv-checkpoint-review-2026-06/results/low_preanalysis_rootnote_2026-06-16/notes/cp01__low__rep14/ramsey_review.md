# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior r03 alignment/weak-pi pODMR context.
- `measurement/m002.json`: submitted Ramsey job contract.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: completed bridge result/status/control.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `evidence/e005.json`: pre-run Ramsey model/advisory, including expected 13C Larmor scale.
- Generated diagnostic plot: `ramsey_analysis.png`.

## Calculations/scripts run

- Used local Python with `json`, `numpy`, `scipy.optimize.curve_fit`, and noninteractive `matplotlib` to inspect `measurement/m001.json`.
- Confirmed measurement settings from raw export and bridge summary:
  - `tau = 0..6 us`, 31 points, `dt = 0.2 us`.
  - `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
  - 4 averages, 50000 repetitions, snake scan order, tracking per average.
  - Run completed without abort; final bridge count text was `38.249 kcps`.
- Built the Ramsey observable as `trace2 / trace1` because trace1 is the brighter reference-like readout and trace2 is the darker signal-like readout.
- Quantitative checks on the 4-average mean:
  - Mean trace1 `45.318 kcps`, mean trace2 `42.098 kcps`, mean ratio `0.9292`.
  - Ratio peak-to-peak span `0.1355`.
  - Descriptive Gaussian-envelope cosine fit to fractional normalized ratio:
    - `f = 1.684 +/- 0.058 MHz`, `T = 3.47 +/- 2.01 us`, amplitude `-3.76%`.
    - Fit quality is poor: `R2 = 0.19`.
  - FFT after linear detrend and Hann window:
    - Native-bin strongest components: `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `1.935 MHz`, `1.774 MHz`, `0.161 MHz`.
    - Zero-padded maximum is near `0.929 MHz`.
    - Amplitude checks at expected scales: `1.500 MHz -> 0.0967`, `1.115 MHz -> 0.1109`, `1.885 MHz -> 0.1664`, `0.385 MHz -> 0.1429` in arbitrary FFT units.
  - Per-average normalized-ratio correlations with the combined trace were only moderate: `0.68`, `0.42`, `0.58`, `0.56`; per-average strongest zero-padded FFT peaks varied widely (`0.900`, `1.484`, `1.211`, `0.232 MHz`).

## Plausible interpretation

- The Ramsey scout is analyzable but not clean. There is oscillatory structure in the reference-normalized signal, but it is not robustly centered on the programmed `1.5 MHz` detuning and is not consistent across averages.
- The descriptive damped-cosine fit suggests a few-us envelope scale, but the low `R2` and large `T` uncertainty make this a heuristic, not a defensible T2star measurement.
- FFT content around the expected `det + 13C` sideband (`~1.885 MHz`) is present, but comparable or larger components also appear at unrelated low frequencies and the per-average peak positions do not agree. This is compatible with drift/noise plus weak Ramsey contrast, not a resolved 13C signature.
- The final count (`38.249 kcps`) is lower than the weak-pODMR final count recorded in project state (`43.890 kcps`), so count/focus drift is a plausible contributor.

## Claims that are not yet supported

- Do not claim a well-supported T2star value from this run.
- Do not claim detection or exclusion of a nearby 13C spin from this run.
- Do not claim the observed strongest FFT peak near `0.93 MHz` is a physical splitting without repeatability or a control/check scan.
- Do not use the descriptive fit center/frequency as a calibration update for the resonance.

## Recommended next action

- Repeat Ramsey on accepted r03 only after a fresh TrackCenter/count check and, ideally, a short weak-pi pODMR or Ramsey detuning sanity check if counts remain shifted.
- For the repeat, keep the analysis goal narrow: first verify a stable Ramsey carrier near the programmed detuning across averages; then use a longer/higher-SNR tau span for T2star and 13C sideband resolution if the carrier is clean.
- Avoid a blind 13C claim or T2star report from the current scout; treat it as a failed/weak scout that motivates a better-controlled repeat rather than as negative spectroscopy evidence.
