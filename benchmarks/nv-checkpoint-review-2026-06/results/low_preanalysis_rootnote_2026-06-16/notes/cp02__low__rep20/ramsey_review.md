# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, and `project/advice.md` for the project objective and prior decisions.
- `measurement/m001.json`: raw export for completed Ramsey savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: submitted Ramsey job contract, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, 8 averages x 50000 repetitions.
- `measurement/m003.json` and `measurement/m004.json`: terminal/status records showing job completed, 2026-05-13 20:49:36 to 22:17:11.
- `measurement/m005.json`: control record, no stop requested.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Wrote numeric output to `ramsey_analysis_summary.json`.
- Parsed `ExperimentData` as two readout channels over 41 tau points and `ExperimentDataEachAvg` as 8 stored averages.
- Checked combined signal/reference ratio, per-average ratios, linear drift/common-mode behavior, windowed FFT after linear detrending, and least-squares sinusoid amplitudes at:
  - programmed carrier: `1.000 MHz`
  - expected 13C sidebands from project model: `0.615 MHz` and `1.385 MHz`
  - prior scout component: `0.884 MHz`
- Robustness checks repeated FFT/least-squares estimates after dropping `tau = 0` and after dropping the first three tau points.

## Plausible interpretation

- The new Ramsey data are analyzable and the run completed normally.
- The combined ratio has a visible early high point and then low-contrast oscillatory structure; ratio peak-to-peak over all points is `0.217`, but this is strongly affected by the high `tau = 0` point. Dropping `tau = 0` reduces peak-to-peak to `0.126`.
- The dominant combined FFT bins are near the intended detuned carrier: top peaks are `1.098 MHz`, `1.220 MHz`, and `0.976 MHz`; dropping `tau = 0` gives `1.125 MHz`, `1.250 MHz`, and `1.000 MHz`.
- The det-shift diagnostic disfavors treating the prior scout's `~0.884 MHz` feature as a fixed physical carrier: the strongest combined spectral content moved toward the new `1.0 MHz` programmed detuning.
- However, least-squares sinusoid fits on the combined ratio remain weak:
  - `1.000 MHz`: amplitude `0.0120` ratio units, `R2 = 0.061`
  - `0.615 MHz`: amplitude `0.0135`, `R2 = 0.073`
  - `1.385 MHz`: amplitude `0.0107`, `R2 = 0.050`
  - `0.884 MHz`: amplitude `0.0095`, `R2 = 0.040`
- Stored averages show large common-mode count changes, but ratio means are much more stable: signal mean relative span `30.5%`, reference mean relative span `31.6%`, ratio mean relative span `4.0%`. This suggests reference normalization removes much of the count drift, but it does not by itself establish coherent Ramsey contrast.
- Per-average 1 MHz amplitudes vary from `0.0053` to `0.0305` ratio units, and carrier phase coherence across averages is only `0.673` on a 0-to-1 scale. This is not claim-grade consistency.

## Claims that are not yet supported

- A quantitative T2star value is not yet supported. The combined trace has carrier-like spectral content, but sinusoid-plus-linear fits explain only about `6%` of the variance at `1 MHz`, and a damped Ramsey fit would be underconstrained/fragile.
- A nearby 13C conclusion is not supported. The expected sideband checks at `0.615 MHz` and `1.385 MHz` have amplitudes comparable to the carrier/prior-artifact checks and similarly weak `R2`; they are not separated from noise/fit leakage strongly enough.
- Sub-grid frequency precision or a definitive Ramsey carrier frequency is not supported. The FFT resolution is about `122 kHz`, and neighboring bins around `1 MHz` are comparable.
- It is not supported that the prior `~0.884 MHz` scout component was a stable physical splitting; the new run points more toward the programmed detuning, but still weakly.

## Recommended next action

Do not claim T2star or 13C yet. Use the completed det-shifted Ramsey as evidence that the sequence can produce carrier-near-detuning structure, but the contrast/consistency are too weak for final conclusions. The next action should be to improve Ramsey signal quality before another claim attempt: rerun on r03 only after checking/retracking counts and using a tighter Ramsey acquisition focused on carrier visibility, with more averages or repetitions and a tau grid chosen to resolve around `1 MHz` while preserving enough short-time points for decay. If another similar Ramsey remains weak, close the 13C branch as unsupported for this NV rather than continuing blind repeats.
