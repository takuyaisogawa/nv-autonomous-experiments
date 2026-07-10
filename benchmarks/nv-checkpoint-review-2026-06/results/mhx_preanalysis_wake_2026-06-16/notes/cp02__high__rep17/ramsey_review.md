# Ramsey review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- Prior context notes/model: `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New Ramsey artifacts:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`, `measurement/m005.json`: terminal status/control.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed raw readouts from `ExperimentData` and per-average readouts from `ExperimentDataEachAvg`.
- Reconstructed `tau = 0..8 us` in 41 points, step `0.2 us`; FFT bin spacing from the actual sampled array is `121.95 kHz`, Nyquist `2.439 MHz`.
- Checked raw signal, reference, signal/reference, and signal divided by a fitted reference line.
- Computed per-average common-mode count summaries as a drift proxy.
- Ran windowed FFT on detrended signal and normalized traces.
- Ran least-squares quadrature tests at:
  - programmed carrier `1.000 MHz`
  - expected 13C sidebands from the project model, `0.615423 MHz` and `1.384577 MHz`
  - prior scout component `0.884 MHz`
- Tried a damped-cosine fit to raw signal as a descriptive check only.

## Key quantitative checks

- Job completed safely: `status=completed`, `aborted=false`, `safe_shutdown_ok=true`; terminal final count was `44.184 kcps`.
- Acquisition matched plan: `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `8 averages x 50000 repetitions`.
- Combined raw signal:
  - mean `44.58 kcps`, edge median `44.50 kcps`
  - min/max `39.31/47.03 kcps`
  - peak-to-peak `7.72 kcps` (`17.4%` of edge median)
  - detrended RMS `1.27 kcps`
  - median signal error from stored averages `1.87 kcps`
- Per-average common-mode count variation is large:
  - mean total kcps by average: `[50.40, 45.56, 43.76, 52.38, 48.45, 43.78, 38.34, 52.90]`
  - relative span `31%` of median
  - average 7 falls below a simple `15%` drop threshold; variation is intermittent, not a clean first-to-last decay.
- Least-squares amplitudes in raw signal:
  - `1.000 MHz`: `0.277 +/- 0.287 kcps`, z `0.96`
  - `0.615 MHz`: `0.475 +/- 0.287 kcps`, z `1.66`
  - `1.385 MHz`: `0.263 +/- 0.287 kcps`, z `0.92`
  - `0.884 MHz`: `0.286 +/- 0.286 kcps`, z `1.00`
- Reference-line-normalized ratio gives the same conclusion; target-frequency z scores are about `0.9..1.7`.
- Largest exploratory FFT bins in the detrended raw signal are near `1.220 MHz` (`0.80 kcps`), `1.098 MHz` (`0.76 kcps`), and `0.488 MHz` (`0.64 kcps`). The expected lower sideband bin near `0.610 MHz` is only `0.40 kcps`; the upper sideband neighborhood near `1.341 MHz` is `0.37 kcps`.
- Damped-cosine fit is not claim-grade: it drives `T2star` to the lower bound `0.2 us`, with large parameter uncertainty (`freq = 1.32 +/- 0.54 MHz`, amplitude `-9.4 +/- 8.7 kcps`). Treat this as a failed/unstable descriptive fit, not a T2star estimate.

## Plausible interpretation

- The measurement is valid as an acquired Ramsey dataset, but it does not show a clean Ramsey carrier at the programmed `1.0 MHz`.
- The det-shift diagnostic does not reproduce the prior scout's non-claim-grade `~0.884 MHz` feature; the `0.884 MHz` least-squares check is only z `~1`.
- The weak lower-sideband-sized component is also below claim threshold and appears in a noisy/drift-affected spectrum rather than as a carrier-plus-sideband pattern.
- The low initial point and broad early-time structure could be consistent with a very short dephasing/transient, imperfect Ramsey contrast, det/phase implementation issues, or drift obscuring the oscillation. This run does not distinguish those possibilities.

## Claims not yet supported

- No supported T2star value can be quoted from this run.
- No supported 13C coupling or sideband claim can be made.
- This run also does not support a strong "no 13C exists" conclusion, because the underlying Ramsey carrier itself is not established.
- Do not use the damped-cosine boundary fit as evidence for `T2star = 0.2 us`.
- Do not claim that the microwave center `3.8759 GHz` is wrong from this Ramsey alone; that would require a targeted resonance/carrier diagnostic.

## Recommended next action

Run a short-tau Ramsey carrier-validation diagnostic on r03 before any further T2star/13C measurement: keep the refined `mw_freq=3.8759 GHz` and `det=1.0 MHz`, but scan only the early window with finer spacing, e.g. `tau = 0..2 us` in about 41 points, with enough averages to keep per-point uncertainty comparable. The goal is not 13C yet; it is to verify whether the programmed Ramsey phase ramp produces a visible, repeatable `1.0 MHz` carrier before designing a longer T2star/FFT acquisition. If that carrier is still absent, inspect the Ramsey sequence/det phase path and re-check the local resonance/tracking before repeating long Ramsey scans.
