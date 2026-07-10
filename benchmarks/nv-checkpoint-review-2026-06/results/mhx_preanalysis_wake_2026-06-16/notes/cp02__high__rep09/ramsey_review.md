# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior fine-pODMR/second-Ramsey context: `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New Ramsey data and terminal artifacts:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: completed terminal bridge result.
  - `measurement/m004.json`: final status.
  - `measurement/m005.json`: control state.

## Calculations/Scripts Run

- Created and ran `analyze_ramsey.py` using only local JSON files.
- Outputs:
  - `ramsey_analysis_results.json`: numeric summaries, FFT/least-squares checks, drift summaries, and fits.
  - `ramsey_trace_fft.png`: raw readouts, point-wise normalization, and signal FFT plot.
- Main checks:
  - Confirmed scan: `ramsey.xml`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, `41` points, `8 x 50000` repetitions, snake order, readout 1 reference and readout 2 Ramsey signal from project protocol context.
  - Terminal result completed safely with final counts `44.184 kcps`.
  - Signal readout mean `44.58 kcps`; reference mean `49.31 kcps`; signal peak-to-peak is `17.4%` of edge-median signal, but this is strongly affected by the low `tau = 0` point.
  - Median across-average SEM is `1.92 kcps` for signal and `0.0187` for signal/reference.
  - Scan-order drift check found no `15%` common-mode drop flags; per-average end-minus-start fractions ranged from about `-3.9%` to `+10.5%`.
  - FFT/bin checks: nominal span resolution `125 kHz`, FFT bin spacing about `121.95 kHz`, Nyquist `2.5 MHz`. Top windowed signal FFT peaks are near `1.220`, `1.098`, `0.488`, `0.610`, and `1.341 MHz`.
  - Coherent least-squares amplitudes in the signal readout:
    - `1.000 MHz` carrier: `0.277 kcps`.
    - expected low 13C sideband `0.615 MHz`: `0.477 kcps`.
    - expected high 13C sideband `1.385 MHz`: `0.264 kcps`.
    - prior scout component `0.884 MHz`: `0.286 kcps`.
  - Per-average phase coherence is weak/moderate, not claim-grade: `0.55` at `1.000 MHz`, `0.73` at `0.615 MHz`, `0.37` at `1.385 MHz`, `0.46` at `0.884 MHz`.
  - Fixed-frequency damped-cosine fits using all points collapse to the lower `T2*` bound (`0.2 us`) with only `R2 ~ 0.51`, driven largely by the `tau = 0` point.
  - Excluding `tau = 0`, the free-frequency damped-cosine fit gives `f = 1.210 +/- 0.026 MHz`, `T2* = 4.1 +/- 2.7 us`, and `R2 = 0.295`; this is not robust enough to claim a T2star.
  - Frequency-scan least-squares checks prefer a broad low-frequency component near `0.47 MHz`, showing that the result is model-dependent and not a clean programmed-carrier measurement.

## Plausible Interpretation

- The second Ramsey is analyzable and not invalidated by terminal status, count collapse, or large scan-order drift.
- There is visible Ramsey-like structure in the combined signal trace, but the spectral content is not cleanly locked to the programmed `1.0 MHz` carrier.
- The `tau = 0` point is unusually low and dominates simple damped-cosine fits; it should not be used alone to infer rapid dephasing.
- The prior scout's `~0.884 MHz` component is not reproduced as a strong coherent feature in this det-shifted run, which weakens a fixed physical assignment for that earlier peak.
- The `0.615 MHz` feature is interesting because it lies near the expected lower 13C sideband, but the lack of a clean carrier, weak high-sideband support, model dependence, and per-average phase scatter make it only a follow-up candidate.

## Claims Not Yet Supported

- No well-supported numeric `T2*` value is established from this run.
- No well-supported nearby `13C` conclusion is established.
- The `0.615 MHz`, `1.1-1.2 MHz`, `0.47 MHz`, or prior `0.884 MHz` components should not yet be assigned to a physical carrier, 13C sideband, or apparatus artifact.
- The fine-pODMR center `3.8759 GHz` remains supported by prior pODMR evidence, but this Ramsey run does not prove the Ramsey phase ramp is behaving as an ideal `1.0 MHz` carrier around that center.

## Recommended Next Action

Do not start another long T2star/13C Ramsey repeat blindly. First run a shorter targeted Ramsey diagnostic after fresh tracking/frequency sanity checks: avoid or separately treat `tau = 0`, use a range such as `tau = 0.2..4 us` with enough points to resolve `0.5..1.5 MHz`, and test whether the observed oscillation follows the programmed detuning. If that diagnostic locks cleanly to the carrier, then acquire a higher-SNR T2star dataset for fitting; if it remains model-dependent, switch to a frequency/sequence diagnostic rather than claiming T2star or 13C from Ramsey FFT peaks.
