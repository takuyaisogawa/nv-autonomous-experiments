# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior accepted r03/fine-pODMR context.
- `md/memory.md`, `md/knowledge.md`: local NV/Ramsey analysis practice, especially raw/readout-aware review before fit claims.
- `measurement/m001.json`: raw savedexperiment export for the new Ramsey run.
- `measurement/m002.json`: submitted job/spec metadata.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- `evidence/e013.md`, `evidence/e006.md`: immediately preceding fine-pODMR and second-Ramsey-start notes.

New Ramsey run reviewed:

- Job: `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`
- Saved run: `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`
- Scan: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, Nyquist `2.5 MHz`, nominal resolution `0.125 MHz`
- Settings: `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `8 averages x 50000 repetitions`
- Terminal status: completed, not aborted, final counts `44.184 kcps`

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_review_plot.png`
- Checks performed:
  - Parsed `ExperimentData` and `ExperimentDataEachAvg`; shape is `(1, 2, 41)` combined and `(1, 8, 2, 41)` per average.
  - Treated readout 1 as reference and readout 2 as Ramsey signal, consistent with the local Ramsey route context.
  - Reviewed raw readouts and signal/reference normalization.
  - Detrended raw signal and normalized traces with offset plus linear trend, then computed exploratory FFTs.
  - Projected fixed-frequency sinusoids at the planned/diagnostic frequencies: `0.615 MHz`, `0.884 MHz`, `1.000 MHz`, and `1.385 MHz`.
  - Checked per-average fixed-frequency amplitudes/phases and common-mode count variation.
  - Ran bounded descriptive damped-cosine fits on raw signal and normalized trace; these were used only as diagnostics, not as claim evidence.

Key numerical checks:

- Combined reference mean/std: `49.313 +/- 0.869 kcps`.
- Combined signal mean/std: `44.580 +/- 1.338 kcps`.
- Combined signal/reference mean/std: `0.9042 +/- 0.0294`.
- Per-average raw reference/signal means show large common-mode variation; relative to median, raw means move by roughly `-18%` to `+13%`, while per-average ratio means stay much tighter, about `-1.3%` to `+2.6%`.
- Detrended FFT top raw-signal bins: `1.220 MHz` (`0.797 kcps`), `1.098 MHz` (`0.764 kcps`), `0.488 MHz` (`0.640 kcps`), `0.122 MHz` (`0.414 kcps`), `0.610 MHz` (`0.398 kcps`).
- Detrended FFT top signal/reference bins: `1.098 MHz` (`0.0211`), `1.220 MHz` (`0.0188`), `0.976 MHz` (`0.0133`), `0.488 MHz` (`0.0123`), `0.366 MHz` (`0.00936`).
- Fixed-frequency raw-signal amplitudes versus residual scatter:
  - `0.615 MHz`: `0.477 kcps`, amplitude/residual std `0.37`
  - `0.884 MHz`: `0.286 kcps`, amplitude/residual std `0.22`
  - `1.000 MHz`: `0.277 kcps`, amplitude/residual std `0.21`
  - `1.385 MHz`: `0.264 kcps`, amplitude/residual std `0.20`
- Fixed-frequency signal/reference amplitudes versus residual scatter:
  - `0.615 MHz`: `0.0111`, amplitude/residual std `0.38`
  - `0.884 MHz`: `0.00742`, amplitude/residual std `0.25`
  - `1.000 MHz`: `0.00916`, amplitude/residual std `0.31`
  - `1.385 MHz`: `0.00843`, amplitude/residual std `0.28`
- Descriptive normalized damped-cosine fit prefers `1.182 +/- 0.023 MHz`, amplitude about `0.043`, and apparent `T2* = 4.68 +/- 1.35 us`; this is off the planned carrier and off the expected 13C sidebands.
- Descriptive raw-signal damped-cosine fit collapses to an early-time feature with `T2* ~0.20 us` and an unphysical large amplitude, so it is not a useful physical fit.

## Plausible interpretation

The run is technically usable in the narrow sense that it completed safely, produced raw data, and has the expected tau grid and per-average traces. The accepted r03 branch remains valid as an aligned NV branch from prior pODMR evidence.

This Ramsey result does not provide claim-grade Ramsey/T2star evidence. The programmed `1.0 MHz` carrier is present only weakly: raw-signal fixed-frequency amplitude is `0.277 kcps`, about `0.21` of the post-fit residual standard deviation, and normalized amplitude is only `0.0092`, about `0.31` of residual scatter. The expected `13C` sideband positions near `0.615` and `1.385 MHz` are also weak by the same check.

The strongest normalized spectral/fitted content is near `1.10-1.22 MHz`, with a descriptive normalized fit near `1.18 MHz`. That may indicate a weak off-carrier oscillatory component, residual timing/phase behavior, drift-normalization structure, or an analysis/sequence artifact. It is not enough to assign a physical T2star or 13C coupling because it does not match the planned carrier or expected sidebands and is not supported by raw-signal fixed-frequency strength.

The prior scout's non-claim-grade `~0.884 MHz` component is not reproduced as the dominant component in this det-shifted run. This weakens the case that the prior `~0.884 MHz` feature was a stable physical Ramsey carrier or a stable 13C-related sideband.

## Claims that are not yet supported

- No supported numerical `T2*` claim from this run.
- No supported nearby `13C` claim from this run.
- No supported claim that the `1.0 MHz` programmed detuning produced a clean Ramsey carrier.
- No supported claim that the normalized `~1.18 MHz` descriptive fit is the NV Ramsey frequency; it is off-plan and not raw-signal-robust.
- No supported claim that more averaging of the same exact measurement will solve the issue; the main problem is frequency/shape consistency, not just shot noise.

## Recommended next action

Do not run a blind higher-SNR repeat yet. First do a Ramsey route/timing/phase diagnostic before using Ramsey data for T2star or 13C conclusions. The practical next experiment should be a short detuning diagnostic on the same accepted r03 branch, using the recent fine-pODMR center, with several programmed detunings including `det = 0`, `0.5 MHz`, and `1.0 MHz` or positive/negative detuning if the route supports it. The goal is to verify whether the observed oscillation frequency follows the programmed phase ramp. If it does not, inspect or change the Ramsey sequence/analysis route before further T2star/13C acquisition. If it does, then repeat T2star with a detuning/grid chosen from that calibrated response.
