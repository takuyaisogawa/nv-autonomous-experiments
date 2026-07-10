# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus relevant Ramsey guidance in `md/memory.md` and `md/knowledge.md`.
- Completed Ramsey data and metadata: `measurement/m001.json` raw export, `measurement/m002.json` submitted recipe, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, `measurement/m005.json` control.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.txt`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` with shape `1 x 2 x 31` and `ExperimentDataEachAvg` with shape `1 x 4 x 2 x 31`.
- Confirmed scan settings: `tau = 0..6 us`, `31` points, `0.2 us` step, `4` averages, `50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
- Computed raw signal/reference statistics, signal/reference ratio, normalized contrast, per-average ratio correlation to the mean, Gaussian-envelope decaying-cosine fit to ratio, and Hann-window FFTs after linear detrending.
- Key numeric results:
  - Signal mean `45.318 kcps`, range `44.038..47.942 kcps`; reference mean `42.098 kcps`, range `38.096..45.846 kcps`.
  - Ratio mean `1.077617`; ratio peak-to-peak `14.72%`.
  - Signal/reference correlation only `0.138`, so the two readouts are not just common-mode copies.
  - Per-average ratio correlations to mean: `0.707, 0.418, 0.546, 0.605`; the pattern is present but not highly repeatable average-by-average.
  - Best unconstrained ratio fit: `T2star = 3.12 +/- 1.03 us`, oscillation `0.946 +/- 0.039 MHz`, `R2 = 0.427`.
  - FFT top ratio peaks: `0.9677, 0.3226, 0.8065, 1.9355, 1.7742, 0.1613 MHz`.
  - FFT top raw-signal peaks: `1.9355, 1.7742, 2.0968, 0.1613, 1.4516, 1.6129 MHz`.

## Plausible interpretation

- The Ramsey job completed normally and produced analyzable data; it was not a count-gate or zero-average failure. Terminal final counts were `38.249 kcps`, lower than the prior weak-pi final-count text `43.890 kcps`, so drift or retuning risk should stay in the provenance.
- There is real tau-dependent structure in the two readouts and in signal/reference ratio, with ratio modulation around `15%` peak-to-peak.
- The normalized ratio fit prefers an oscillation near `0.95 MHz`, not the programmed `1.5 MHz` detuning. The fit quality is modest (`R2 = 0.427`) and per-average reproducibility is only moderate.
- Raw signal FFT has features near the intended Ramsey-carrier/sideband region: nearest planned carrier bin is `1.4516 MHz`; expected `det +/- 13C` bins from the project model are about `1.1290` and `1.9355 MHz`; the raw signal is strongest near `1.9355 MHz`. However, the reference and ratio spectra have strong lower-frequency content, so the `1.9355 MHz` feature is not sufficient by itself to claim a 13C sideband.
- A cautious working interpretation is: r03 still looks like the right aligned candidate, and this scout indicates nontrivial Ramsey oscillation/decay, but the first dataset is scout-grade rather than final-claim-grade.

## Claims not yet supported

- A final T2star value is not supported. The descriptive ratio fit gives `~3.1 us`, but the frequency differs from the programmed detuning and the fit explains less than half of the ratio variance.
- A nearby 13C conclusion is not supported. There is a raw-signal FFT peak at the expected high-sideband bin, but the normalized ratio does not cleanly show the expected carrier/sideband structure and lower-frequency/reference structure is comparable.
- A no-13C conclusion is also not supported; the 6 us/31 point scout has coarse `~0.16 MHz` FFT bins and visible drift/readout complications.
- It is not yet supported that the weak-pi pODMR center or programmed detuning fully describes the Ramsey phase evolution in this run.

## Recommended next action

Run a targeted Ramsey follow-up on r03 rather than switching candidates. First repeat/check tracking and weak-pi center if possible, then acquire a higher-confidence Ramsey dataset with improved per-average robustness: keep `mw_freq = 3.876 GHz` unless a quick weak-pi check shifts it, use a deliberate detuning that stays below Nyquist with sidebands, and improve SNR by increasing averages rather than stretching any single average beyond the drift/tracking comfort window. The next analysis should require consistent per-average normalized oscillations and carrier/sideband FFT agreement before making T2star or 13C claims.
