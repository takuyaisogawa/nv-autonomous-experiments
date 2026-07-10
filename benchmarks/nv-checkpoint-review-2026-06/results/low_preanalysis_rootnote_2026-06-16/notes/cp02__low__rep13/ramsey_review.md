# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for project context.
- `measurement/m001.json`: raw savedexperiment export for the new Ramsey run.
- `measurement/m002.json`: submitted job/sequence metadata.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed run settings: `ramsey.xml`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us` in 41 points, `8 x 50000` repetitions, final counts `44.184 kcps`.
- Interpreted sequence readouts from the exported XML with `full_experiment=0`: readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
- Checked raw signal, signal/reference, signal divided by fitted reference line, per-average signal traces, FFTs, and least-squares sinusoid amplitudes at the prior `0.884 MHz` component, expected `13C` sidebands near `0.615/1.385 MHz`, and the programmed `1.000 MHz` detuning.
- Numerical highlights from `ramsey_analysis_summary.json`:
  - Combined raw signal mean `44.58 kcps`; peak-to-peak `7.72 kcps` (`17.3%` of mean).
  - Reference peak-to-peak `8.7%` of mean.
  - Largest non-DC FFT component: raw signal near `1.220 MHz`; ratio near `1.098 MHz` on the actual 41-point FFT grid.
  - Fixed-frequency raw-signal least-squares checks: `0.884 MHz` amplitude `0.278 kcps`, `R2=0.023`; `0.615 MHz` amplitude `0.555 kcps`, `R2=0.087`; `1.000 MHz` amplitude `0.300 kcps`, `R2=0.026`; `1.385 MHz` amplitude `0.266 kcps`, `R2=0.021`.
  - A free damped-cosine fit returned `freq=1.257 MHz`, `T2*=0.20 us` at the lower bound, and `R2=0.51`; this is descriptive only and not a supported T2star estimate.

## Plausible interpretation

- The run completed normally and produced analyzable data, but the Ramsey spectral content does not cleanly follow the programmed `1.0 MHz` phase ramp.
- The previous non-claim-grade `~0.884 MHz` feature is not reproduced as a strong fixed component in this det-shifted run.
- The expected `13C` sidebands near `0.615 MHz` and `1.385 MHz` are not supported: least-squares amplitudes are small and explain little variance.
- The raw signal has sizable structure, but per-average extrema are inconsistent and average-to-average levels vary strongly. This points to drift/baseline/systematic structure or unstable Ramsey contrast rather than a claim-grade physical oscillation.
- The terminal run was healthy, but `measurement/m004.json` reports an estimated tracking window of `629.8 s` per average, above the earlier `600 s` cap/advisory. Treat this as drift provenance when interpreting the per-average disagreement.

## Claims that are not yet supported

- No well-supported T2star value is established from this Ramsey run.
- No well-supported nearby `13C` conclusion is established from this Ramsey run.
- The observed `1.10..1.26 MHz` exploratory structure should not be assigned as the true Ramsey carrier without a repeatable carrier diagnostic.
- The fine pODMR center `3.8759 GHz` remains the best grid-supported microwave input from prior evidence, but this Ramsey run does not independently validate the detuned Ramsey response.

## Recommended next action

Do not blindly repeat the same Ramsey. First run a targeted Ramsey carrier/control diagnostic on accepted r03 with shorter per-average windows and high contrast visibility: keep the fine pODMR center, use a simpler/no-13C-focused scan designed only to verify that the Ramsey carrier follows programmed detuning, and compare at least two detunings with the same tau grid and reduced per-average runtime. If the carrier still fails to track detuning, switch to recalibration/protocol diagnosis before attempting another T2star or `13C` claim measurement.
