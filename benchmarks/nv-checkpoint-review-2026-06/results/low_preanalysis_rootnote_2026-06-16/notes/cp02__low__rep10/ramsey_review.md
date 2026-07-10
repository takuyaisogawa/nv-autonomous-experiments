# Ramsey review: image145844_reimage_r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, and prior note `evidence/e013.md`.
- New Ramsey run metadata/status/control: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- New raw Ramsey export: `measurement/m001.json`, savedexperiment path `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Analysis artifacts created locally: `analysis/ramsey_analysis_summary.json` and `analysis/ramsey_review_plot.png`.

## Calculations or scripts run

- Ran an inline Python analysis over `measurement/m001.json` using NumPy/SciPy and matplotlib Agg.
- Parsed the 8-average, 2-channel Ramsey data: `tau = 0..8 us`, `41` points, `dt = 0.2 us`, `8 x 50000` shots, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Computed raw signal/reference traces, signal/reference ratio, per-average ratio traces, linear-detrended FFTs, and least-squares sinusoid amplitudes at:
  - expected det carrier: `1.0 MHz`
  - expected 13C sidebands from the project model: `0.615 MHz` and `1.385 MHz`
  - prior scout component: `0.884 MHz`
- Ran a descriptive decaying-cosine fit to the combined signal/reference ratio, treating it as exploratory only.

## Quantitative checks

- Terminal run completed without abort; final count text was `Final = 44.184 kcps`.
- Combined raw means: signal `49.31 kcps`, reference `44.58 kcps`; mean ratio `1.1071`.
- Common-mode count variation across averages is large: per-average mean signal range is `30.5%` of mean, and reference range is `31.6%` of mean. The ratio is more stable but still shifts by about `4%` between average means.
- Ratio-domain detrended FFT top bins:
  - `1.098 MHz`, fractional amplitude `0.0230`
  - `1.220 MHz`, `0.0204`
  - `0.976 MHz`, `0.0148`
  The strongest ratio FFT content is near the programmed `1.0 MHz` carrier, but split across neighboring bins.
- Raw-signal FFT top bins are not as clean: `0.854 MHz` and `0.976 MHz` are the two largest, each about `0.0091` fractional amplitude.
- Fixed-frequency least-squares checks on the ratio have low explanatory power:
  - `0.615 MHz`: amp `0.0119`, `R2 = 0.066`
  - `0.884 MHz`: amp `0.0085`, `R2 = 0.033`
  - `1.000 MHz`: amp `0.0108`, `R2 = 0.054`
  - `1.385 MHz`: amp `0.0097`, `R2 = 0.044`
- Per-average dominant FFT bins are inconsistent: averages peak at `2.317`, `2.317`, `1.098`, `0.488`, `1.220`, `0.610`, `1.463`, and `0.488 MHz`.
- The exploratory decaying-cosine fit returns `f = 0.889 MHz`, `T2* = 0.444 us`, `R2 = 0.461`, with a large frequency uncertainty (`~0.50 MHz`). This is not a supportable T2* estimate.

## Plausible interpretation

- This second Ramsey is analyzable and does show some combined ratio spectral weight near the programmed `1.0 MHz` detuned carrier. That is better aligned with the det-shift intent than the first scout's non-claim-grade `~0.884 MHz` component.
- However, the evidence is not internally consistent enough for a final Ramsey/T2* claim: per-average spectra disagree, the raw and ratio FFTs emphasize somewhat different bins, and the fixed-frequency least-squares `R2` values are all low.
- There is no strong evidence for a resolved nearby 13C modulation. The expected sideband checks at `0.615` and `1.385 MHz` are comparable to other weak components and do not separate cleanly from noise/drift.
- The large per-average common-mode count swing suggests tracking/count-state changes affected the measurement. Ratio normalization helps, but does not make the oscillation claim-grade.

## Claims not yet supported

- Do not claim a measured `T2*` from this run.
- Do not claim resolved 13C coupling or absence of all 13C coupling from this run alone.
- Do not claim the fitted `0.444 us` decay time as physical; it is a descriptive fit under inconsistent spectral evidence.
- Do not claim the prior `~0.884 MHz` component was definitively physical or definitively an artifact. The det-shift run weakens a fixed-frequency interpretation, but does not close the question by itself.

## Recommended next action

- Do not blindly repeat the same Ramsey as-is. First run a short frequency/contrast sanity check at the accepted r03 position:
  - retrack r03 and repeat a narrow weak-pi pODMR around `3.8759 GHz`, or equivalent minimal resonance/contrast check;
  - only if contrast and counts are stable, run a higher-quality Ramsey with the same det diagnostic but improved drift control, e.g. shorter per-average blocks or more interleaved/randomized averaging if the bridge supports it.
- If the sanity check shows degraded pODMR contrast or unstable counts, prioritize target stability/tracking before another T2* acquisition.
