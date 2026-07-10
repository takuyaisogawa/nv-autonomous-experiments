# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus prior local notes `evidence/e006.md` and `evidence/e013.md`.
- New Ramsey run metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- New Ramsey raw export: `measurement/m001.json`, savedexperiment path recorded as `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py` to parse the exported `ExperimentData` and `ExperimentDataEachAvg` arrays.
- Confirmed scan settings: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, FFT bin spacing `121.95 kHz`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `8 x 50000` shots.
- Treated readout 1 as reference and readout 2 as Ramsey signal, then checked raw readouts, signal/reference ratio, median-normalized ratio, per-average behavior, FFT, exact-frequency least-squares amplitudes, and simple damped-cosine fits.
- Common-mode per-average check flagged average 7 only at the `>15%` level (`-18.4%` vs median). Excluding average 7 left the combined strongest FFT peak near `1.098 MHz`, so the main issue is not only that one average.
- Combined median-normalized signal/reference ratio has peak-to-peak span `18.7%`.
- Combined FFT top bins are near `1.098 MHz`, `1.220 MHz`, and `0.976 MHz`; this is broadly near the programmed `1.0 MHz` carrier, unlike the prior scout's strongest `~0.884 MHz` feature.
- Exact-frequency least-squares sinusoid amplitudes on normalized ratio:
  - `0.615 MHz` low 13C sideband: `1.23%`, delta-R2 vs line `0.072`.
  - prior `0.884 MHz` component: `0.82%`, delta-R2 `0.032`.
  - `1.000 MHz` carrier: `1.01%`, delta-R2 `0.050`.
  - `1.385 MHz` high 13C sideband: `0.93%`, delta-R2 `0.043`.
- Per-average strongest FFT peaks are inconsistent: averages peak at about `2.317, 2.317, 1.098, 0.488, 1.220, 0.610, 1.463, 0.488 MHz`.
- Descriptive damped-cosine fits are model-sensitive: exponential-envelope fit gives `T2star = 2.27 +/- 0.81 us`, `f = 1.187 +/- 0.027 MHz`, `R2 = 0.486`; Gaussian-envelope fit gives `T2star = 0.466 +/- 0.171 us`, `f = 0.956 +/- 0.444 MHz`, `R2 = 0.411`.

## Plausible interpretation

- The det-shifted Ramsey produced analyzable contrast and now shows its strongest combined spectral weight close to the programmed `1.0 MHz` detuning. This weakly favors the interpretation that the prior `~0.884 MHz` scout peak was not a stable physical Ramsey carrier.
- A conservative, descriptive T2star scale is "order 1-2 us", but the exact T2star is not claim-grade because fitted T2star changes strongly with envelope model and per-average spectral content is inconsistent.
- There is no supported 13C conclusion from this run. The low-sideband bin near `0.610 MHz` is present but smaller than the carrier-region cluster and is not consistently the strongest per average; the high sideband near `1.385 MHz` is also weak.

## Claims not yet supported

- Do not claim a final T2star value from this Ramsey.
- Do not claim nearby 13C coupling or absence of nearby 13C from this dataset alone.
- Do not claim that the fine pODMR center is sub-grid accurate; the local context only supports using the grid-selected `3.8759 GHz` setting.
- Do not claim that average 7 invalidates the whole run; it is a provenance flag, but removing it does not materially improve average-to-average spectral consistency.

## Recommended next action

- Do not immediately repeat the same Ramsey unchanged. First inspect whether the Ramsey sequence/control path should produce a phase-coherent `det` carrier in every average, because the combined carrier-like feature is not reproduced consistently average by average.
- If the control path is considered valid, run one targeted higher-SNR confirmation at the same accepted r03 position with a shorter/focused tau window or repeated phase/readout settings designed to lock the carrier near `1.0 MHz`; require per-average carrier consistency before making T2star or 13C claims.
- If the control path is questionable, switch to a more diagnostic Ramsey/echo or calibration check before spending another long acquisition on 13C sideband interpretation.
