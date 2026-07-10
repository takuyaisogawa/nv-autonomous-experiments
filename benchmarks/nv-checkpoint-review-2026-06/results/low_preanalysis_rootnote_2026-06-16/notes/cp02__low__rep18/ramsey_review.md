# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, selected Ramsey-related context from `md/memory.md` and `evidence/e006.md` / `evidence/e013.md`.
- New measurement data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Measurement metadata: `measurement/m002.json` job request, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_plot.png`, `analysis_stdout.txt`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` to inspect both exported readout channels, `readout2/readout1`, per-average means, FFT bins, least-squares sinusoid amplitudes at diagnostic frequencies, and a descriptive damped-cosine fit.
- Confirmed settings from the raw export: `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, `dt = 0.2 us`, `41` points, `8 x 50000` shots, recorded position about `[117.298, 117.538, 115.370] um`.
- FFT of the detrended ratio had its largest bins at `1.220 MHz` with amplitude `0.0197`, `0.488 MHz` with amplitude `0.0165`, `1.098 MHz` with amplitude `0.0133`, `0.976 MHz` with amplitude `0.0129`, and `0.610 MHz` with amplitude `0.0112`.
- Least-squares checks on the ratio gave small target amplitudes relative to residual RMS: `0.615 MHz` sideband amplitude `0.0108` with amp/RMS `0.39`; prior `0.884 MHz` amplitude `0.0074` with amp/RMS `0.26`; `1.000 MHz` carrier amplitude `0.0091` with amp/RMS `0.32`; `1.385 MHz` sideband amplitude `0.0084` with amp/RMS `0.30`.
- Per-average ratio phases were not strongly coherent: phase-lock values were about `0.43` at `0.615 MHz`, `0.42` at `0.884 MHz`, `0.65` at `1.000 MHz`, and `0.60` at `1.385 MHz`.
- Average means showed large common-mode variation across averages: readout1 mean ranged `40.47..55.53`, readout2 mean ranged `36.20..50.27`. Ratio normalization reduced but did not eliminate ambiguous structure; the combined ratio mean was `0.904`, point-to-point span `0.170`, and standard deviation `0.029`.
- A free descriptive damped-cosine fit to the ratio returned `f = 0.956 MHz`, `T2* = 0.466 us`, amplitude `-0.109`, and `R2 = 0.41`; this is not robust enough to use as a T2star claim.

## Plausible interpretation

- The second Ramsey run completed and produced analyzable data, but the quantitative checks do not support a clean Ramsey carrier at the programmed `1.0 MHz`.
- The strongest ratio FFT bin is near `1.22 MHz`, while nearby bins around `0.98/1.10 MHz` and a low-side bin near `0.61 MHz` are comparable in scale. This looks more like weak, mixed spectral content plus drift/noise than a clean det-shifted carrier.
- The previous scout's `~0.884 MHz` feature did not reappear as a dominant component after changing the programmed detuning to `1.0 MHz`; in this run it is weaker than the target carrier and sideband checks. That argues against treating the earlier `0.884 MHz` component as a stable physical Ramsey carrier.
- The expected `13C` sideband positions for this plan, about `0.615 MHz` and `1.385 MHz`, are not supported as claim-grade features. The low sideband has a visible nearby FFT bin (`0.610 MHz`) but its target least-squares amplitude is still small relative to residual RMS and not phase-coherent across averages.
- The run is useful diagnostically: it strengthens the conclusion that the current Ramsey evidence is not yet sufficient for either T2star or `13C`, despite the earlier pODMR evidence supporting r03 as an aligned candidate.

## Claims not yet supported

- Do not claim a measured `T2*` from this dataset. The damped-cosine fit is descriptive only and has low explanatory power (`R2 ~ 0.41`) with a short fitted decay that is not independently established by stable carrier evidence.
- Do not claim `13C` coupling or resolved `13C` sidebands. The `0.615/1.385 MHz` checks are weak and not sufficiently consistent across averages.
- Do not claim that the programmed `1.0 MHz` Ramsey carrier is clearly observed. It is present only as a weak component comparable to neighboring FFT bins and residual structure.
- Do not claim that r03 is invalid as an aligned NV from this Ramsey alone. The pODMR evidence still supports r03 alignment; this run mainly says the Ramsey/T2star/13C branch remains unresolved.

## Recommended next action

- Do not simply repeat the same Ramsey. First run a focused calibration/diagnostic: repeat a short detuning series on r03 with otherwise similar readout settings, for example two or three Ramsey scans at distinct detunings such as `0.5`, `1.0`, and `1.5 MHz`, with enough averages to test whether the dominant frequency shifts linearly with programmed detuning and whether per-average phase coherence improves.
- If the carrier tracks detuning, then run a higher-SNR Ramsey optimized around the confirmed carrier before fitting `T2*` or searching for `13C` sidebands. If it does not track detuning, pause T2star/13C claims and troubleshoot sequence/readout timing, microwave/IQ detuning implementation, and common-mode count instability.
