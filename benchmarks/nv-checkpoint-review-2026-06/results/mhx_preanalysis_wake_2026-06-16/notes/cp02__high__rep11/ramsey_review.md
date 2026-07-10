# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`
- `md/memory.md`, `md/knowledge.md`
- `context.json`
- `evidence/e006.md`, `evidence/e013.md`, and targeted `rg` search over `evidence/`, `project/`, and `measurement/`
- New terminal Ramsey files:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`
  - `measurement/m002.json`: submitted job spec
  - `measurement/m003.json`: terminal bridge result
  - `measurement/m004.json`: terminal bridge status
  - `measurement/m005.json`: control state
- Scratch outputs created here:
  - `analyze_ramsey.py`
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis_summary.md`
  - `ramsey_analysis_plot.png`

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` as combined readouts `[reference, signal]` and `ExperimentDataEachAvg` as per-average `[average, readout, tau]`.
- Confirmed from embedded `ramsey.xml` path and `full_experiment=0` that readout 1 is the true `mS=0` reference and readout 2 is the Ramsey signal.
- Computed the tau grid: 41 points over 0..8 us, dt 0.2 us, nominal 1/span FFT resolution 125 kHz, Nyquist 2.5 MHz.
- Recomputed the local model from the fine pODMR frequency: `mw_freq = 3.8759 GHz` gives approximately `B = 359.2 G`, `13C Larmor = 384.6 kHz`, and expected detuned Ramsey components near `1.000 MHz` and possible sidebands near `0.615/1.385 MHz`.
- Reviewed combined raw signal, point-wise signal/reference ratio, and signal divided by a fitted reference line.
- Detrended traces with a linear baseline, then computed windowed FFT peaks and least-squares sinusoid amplitudes at `0.884 MHz`, `0.615 MHz`, `1.000 MHz`, and `1.385 MHz`.
- Checked per-average raw-signal target amplitudes and average-to-average count variation.
- Tried bounded Gaussian-envelope sinusoid grid fits as a diagnostic only; they collapse to the shortest tested T2* for all target frequencies and are not interpretable as a T2* result.

## Plausible interpretation

- The Ramsey job completed normally and produced analyzable data: terminal status completed, final counts `44.184 kcps`, saved scan has `8 x 50000` repetitions and 41 tau points.
- The det-shift diagnostic does not support a clean physical Ramsey carrier at the programmed `1.0 MHz`. In the combined raw signal, the targeted 1.000 MHz least-squares amplitude is only `0.276 kcps` with `R2 = 0.024`.
- The expected 13C sidebands are also not supported. The lower sideband check at `0.615 MHz` is the largest targeted raw-signal amplitude (`0.465 kcps`) but still explains only `R2 = 0.068`; the upper sideband at `1.385 MHz` is `0.264 kcps`, `R2 = 0.022`.
- The previous scout's `~0.884 MHz` exploratory component is not reproduced as a compelling fixed feature: the new targeted raw-signal amplitude at `0.884 MHz` is `0.286 kcps`, `R2 = 0.026`.
- FFT peaks are weak and view-dependent. The strongest detrended raw-signal FFT bin is near `1.220 MHz`; normalized traces emphasize nearby bins around `1.098/1.220 MHz`. These do not cleanly match the programmed carrier or the expected 13C sidebands.
- Per-average behavior is not consistent enough for a claim. Individual averages show different target-frequency amplitudes, and the average signal means span about `31.6%` of the median, indicating substantial count/readout variation across the long run even though the first-to-last signal mean changes only `3.8%`.
- Overall: r03 remains the supported aligned NV candidate from pODMR evidence, but this second Ramsey remains non-claim-grade for both T2star and 13C. The det-shift result weakens the idea that the first scout's `~0.884 MHz` feature was a stable physical carrier.

## Claims that are not yet supported

- No numerical T2star should be claimed from this data.
- No nearby `13C` coupling or sideband assignment should be claimed.
- No claim that the Ramsey carrier follows the programmed detuning is supported.
- No claim that the prior `~0.884 MHz` component is a real, stable physical feature is supported.
- Do not use the diagnostic short-T2* grid fits: they collapse to the fit lower bound and mainly fit early-time/outlier structure rather than a shared oscillatory decay.

## Recommended next action

Do not blindly repeat the same Ramsey. First run a bridge-free synthesis/design step to decide whether the failure is most consistent with Ramsey phase/sequence behavior, readout/count drift, or frequency/calibration mismatch. The most useful next experiment is likely a targeted Ramsey/sequence diagnostic with a deliberately chosen detuning set or phase-control check, plus shorter per-average windows, rather than another higher-shot repeat of the same 1.0 MHz Ramsey. Keep the project state at: aligned r03 supported; T2star unresolved; 13C unresolved.
