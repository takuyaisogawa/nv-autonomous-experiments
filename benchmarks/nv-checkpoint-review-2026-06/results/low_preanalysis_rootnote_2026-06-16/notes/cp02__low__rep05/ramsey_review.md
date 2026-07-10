# Ramsey review: r03 det=1.0 MHz follow-up

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior decision context.
- `evidence/e006.md`, `evidence/e013.md`: fine pODMR and second-Ramsey planning context.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: submitted job contract for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- Scratch plots created: `scratch/ramsey_det1p0_review.png`, `scratch/ramsey_det1p0_fft.png`.

## Calculations or scripts run

- Used local Python to inspect JSON structure, scan variables, readout arrays, and scan order.
- Parsed `ExperimentData` as 2 readouts x 41 tau points and `ExperimentDataEachAvg` as 8 averages x 2 readouts x 41 tau points.
- Used tau grid `0..8 us`, 41 points, `dt = 0.2 us`; nominal native FFT bin spacing is about `0.122 MHz`.
- Treated readout 1 as the mS=0/reference readout and readout 2 as the post-Ramsey signal from the saved Ramsey XML sequence.
- Checked raw signal, signal/reference ratio, per-average consistency, detrended/Hann FFT, least-squares sinusoid amplitudes at target frequencies, a free decaying-cosine fit, a fixed-1.0-MHz decaying-cosine fit, and a shuffled-tau null check over `0.4..1.6 MHz`.

Key numerical checks:

- Terminal result completed normally with final counts `44.184 kcps`; saved scan reports `8` averages and `50000` repetitions.
- Combined readout means: reference `49.313 kcps`, signal `44.580 kcps`, signal/reference mean `0.9042`.
- Per-average signal means vary strongly: `[48.437, 43.441, 41.201, 49.977, 45.726, 41.383, 36.203, 50.272] kcps`, about `-18.8%` to `+12.8%` relative to the median. Signal/reference average means are more stable, `0.8909..0.9258`, but still not identical.
- Detrended dense FFT maxima:
  - raw signal: broad maximum near `1.165 MHz`, amplitude about `0.867 kcps`.
  - signal/reference: broad maximum near `1.143 MHz`, amplitude about `0.0223`.
- Native FFT bins for signal/reference:
  - strongest bins are `1.098 MHz` (`0.0211`) and `1.220 MHz` (`0.0188`).
  - nearest programmed det bin `0.976 MHz` has amplitude `0.0133`.
  - nearest expected lower 13C sideband bin `0.610 MHz` has amplitude `0.00759`.
  - nearest expected upper 13C sideband bin `1.341 MHz` has amplitude `0.00660`.
  - prior scout component bin near `0.854 MHz` has amplitude `0.00660`.
- Least-squares amplitudes in combined signal/reference:
  - `0.615 MHz`: `0.0111`, residual RMS `0.0279`, amplitude/RMS `0.40`.
  - `0.884 MHz`: `0.00742`, residual RMS `0.0285`, amplitude/RMS `0.26`.
  - `1.000 MHz`: `0.00916`, residual RMS `0.0282`, amplitude/RMS `0.32`.
  - `1.385 MHz`: `0.00843`, residual RMS `0.0283`, amplitude/RMS `0.30`.
- Per-average least-squares amplitudes at target frequencies are not consistent; coefficient of variation is about `0.39..0.64` across the four checked target frequencies.
- Per-average best-fit frequency in `0.4..1.6 MHz` jumps among averages (`0.415`, `0.435`, `0.455`, `0.635`, `0.810`, `1.165`, `1.420`, `1.480 MHz`), not a coherent shared carrier.
- Shuffled-tau null check for maximum signal/reference LS amplitude over `0.4..1.6 MHz`: observed `0.0225`; null 95th percentile `0.0212`, 99th percentile `0.0239`, empirical `p ~= 0.019`. This is weak evidence for some oscillatory structure but not robust claim-grade evidence after accounting for frequency search and average inconsistency.
- Descriptive decaying-cosine fits are unstable:
  - raw signal free fit: `f ~= 1.323 MHz`, `T2*` hits lower bound `0.2 us`, `R2 ~= 0.52`.
  - ratio free fit: `f ~= 1.187 MHz`, `T2* ~= 2.27 us`, `R2 ~= 0.49`.
  - fixed `1.0 MHz` ratio fit: `T2* ~= 0.35 us`, `R2 ~= 0.41`.

## Plausible interpretation

- The run completed and returned analyzable Ramsey-format data on accepted r03.
- There is weak combined-data spectral structure around `1.1..1.2 MHz`, which is closer to the programmed `1.0 MHz` detuning than the first scout's non-claim-grade `~0.884 MHz` component, but it is not centered cleanly at `1.0 MHz`.
- The expected 13C sideband locations near `0.615 MHz` and `1.385 MHz` are not enhanced relative to nearby/noisy components.
- Normalization removes some common-mode count changes, but per-average frequency and amplitude disagreement remains large. The data are therefore compatible with weak Ramsey contrast plus drift/noise/normalization sensitivity rather than a clean, stable Ramsey oscillation.

## Claims that are not yet supported

- Do not claim a well-supported `T2*` from this run. Fits are model-sensitive, have modest `R2`, and give inconsistent `T2*` depending on raw versus normalized data and fixed versus free frequency.
- Do not claim a resolved 13C coupling. The expected sideband bins are weak and not per-average coherent.
- Do not claim that the first scout's `~0.884 MHz` feature was physical. In this det-shifted run, the prior-frequency check is weak.
- Do not claim sub-grid or fit-level microwave-frequency precision beyond the prior pODMR-supported `3.8759 GHz` grid choice.

## Recommended next action

Do not blindly repeat the same Ramsey. First run a short Ramsey diagnostic designed to decide whether the phase ramp and readout normalization are trustworthy: keep r03 and `mw_freq = 3.8759 GHz`, use a shorter tau span with denser sampling around the first few microseconds, and collect enough averages to compare raw signal and signal/reference per average. If that diagnostic shows a coherent carrier that tracks programmed detuning across at least two det values, then run a higher-SNR T2* measurement; if it does not, revisit Ramsey sequence/readout phase/sign conventions or the microwave frequency before making T2*/13C claims.
