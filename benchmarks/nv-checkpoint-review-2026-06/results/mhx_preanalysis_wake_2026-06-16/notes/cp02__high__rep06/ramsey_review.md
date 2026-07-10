# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, `md/memory.md`.
- New Ramsey run metadata and data:
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted job contract.
  - `measurement/m003.json`: terminal bridge result, status `completed`.
  - `measurement/m004.json` and `measurement/m005.json`: final status/control metadata.
- Immediate prior note: `evidence/e013.md`, confirming this was the second Ramsey follow-up on accepted r03 after fine weak-pi pODMR.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs written:
  - `ramsey_analysis_summary.json`
  - `ramsey_trace_and_fit.png`
  - `ramsey_fft_checks.png`
- The script extracted the two readout channels from `ExperimentData` and `ExperimentDataEachAvg`; the embedded sequence text indicates channel 0 is the pre-Ramsey 0-level reference detection and channel 1 is the post-Ramsey Ramsey signal detection.
- Scan confirmed: `tau = 0..8 us`, 41 points, `0.2 us` step, snake scan order, 8 averages x 50000 repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, final position `[117.298, 117.538, 115.37] um`.
- Checked raw signal, point-wise `signal/reference`, and signal normalized by a fitted reference line.
- Checked per-average common-mode behavior:
  - Reference mean ranged `40.473..55.529 kcps`.
  - Signal mean ranged `36.203..50.272 kcps`.
  - Ratio mean was more stable, `0.89090..0.92582`.
- Ran Hann-window FFT after linear detrending. In the ratio trace, the largest peaks in `0.2..2.2 MHz` were `1.098 MHz` with amplitude `0.0211` and `1.220 MHz` with amplitude `0.0188`; the `0.976 MHz` bin was smaller at `0.0133`.
- Ran fixed-frequency least-squares sinusoid checks on the ratio trace:
  - Expected lower 13C sideband `0.615 MHz`: amplitude `0.0111 +/- 0.0066`, `1.68 sigma`.
  - Prior scout component `0.884 MHz`: amplitude `0.0074 +/- 0.0067`, `1.10 sigma`.
  - Programmed carrier `1.000 MHz`: amplitude `0.0092 +/- 0.0066`, `1.39 sigma`.
  - Expected upper 13C sideband `1.385 MHz`: amplitude `0.0084 +/- 0.0066`, `1.28 sigma`.
- Ran damped-cosine fits as descriptive checks, not as claim-grade parameter extraction. The ratio exponential fit gave a component near `1.187 +/- 0.027 MHz` with `T2star = 2.27 +/- 0.81 us` and amplitude `0.071 +/- 0.017`, but fit results were model/trace dependent; raw and normalized fits did not agree robustly.

## Plausible interpretation

- The run is analyzable and contains Ramsey-like early-time contrast after reference correction.
- The dominant spectral content is near `1.1..1.2 MHz`, not cleanly at the programmed `1.0 MHz` carrier and not at the expected `0.615/1.385 MHz` 13C sidebands.
- The earlier non-claim-grade `~0.884 MHz` component is not reproduced as a dominant feature in this det-shifted follow-up.
- The large per-average count swings are mostly common-mode and are partly suppressed by `signal/reference`; this makes ratio/reference-aware views more credible than raw signal alone, but also means the raw trace should not be used by itself for a T2star claim.
- A reasonable working hypothesis is that the Ramsey carrier is present but the effective detuning is offset from the programmed 1.0 MHz by roughly `+0.1..0.2 MHz`, or that the short early-time contrast plus drift/noise is biasing the apparent carrier. The current data do not decide between those possibilities.

## Claims that are not yet supported

- No well-supported numerical T2star should be claimed from this run. Descriptive fits give model-dependent values and inconsistent carrier frequencies across raw, ratio, and reference-normalized traces.
- No 13C coupling claim is supported. Fixed-frequency checks at `0.615 MHz` and `1.385 MHz` are below 2 sigma in the ratio trace, and the FFT does not show a clean sideband pair.
- Do not claim that the programmed `1.0 MHz` carrier is cleanly observed. The strongest bins/components are displaced toward `1.1..1.2 MHz`.
- Do not claim the prior `~0.884 MHz` scout feature was physical; this run does not reproduce it as a dominant component.

## Recommended next action

Do not close T2star or 13C from this measurement. Run a focused Ramsey frequency-calibration follow-up on r03 before another long T2star/13C acquisition: use a shorter high-SNR tau window emphasizing the first few microseconds and test two small microwave-frequency offsets around `3.8759 GHz` or otherwise resolve the sign/magnitude of the apparent `~0.1..0.2 MHz` detuning error. After the Ramsey carrier is pinned and common-mode drift is acceptable, repeat the T2star/13C Ramsey with enough SNR to evaluate the carrier and `13C` sideband positions in the same reference-aware analysis.
