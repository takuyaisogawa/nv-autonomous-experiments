# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior/planning evidence: especially `evidence/e007.json`, `evidence/e008.json`, `evidence/e009.json`, and `evidence/e013.md`.
- New Ramsey run files:
  - `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`: numeric summary.
  - `ramsey_analysis.png`: diagnostic plot.
- Checks performed:
  - Confirmed scan settings from raw export/job metadata: `tau = 0..8 us`, `41` points, `0.2 us` step, nominal `125 kHz` resolution, Nyquist `2.5 MHz`, `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`, `8 x 50000` shots.
  - Used protocol evidence that readout 1 is the `m_S=0` reference and readout 2 is the Ramsey signal for `full_experiment=0`.
  - Reviewed raw signal, point-wise signal/reference ratio, and signal normalized by a linear fit to the reference readout.
  - Ran detrended FFT checks and least-squares sinusoid screens at planned frequencies: expected 13C sidebands `0.615423 MHz` and `1.384577 MHz`, programmed carrier `1.000 MHz`, and prior scout component `0.884 MHz`.
  - Checked average-to-average common-mode readout changes from stored averages.

Key numeric checks:

- Terminal result completed without abort; final count text was `44.184 kcps`.
- Combined raw reference mean/range: `49.31 kcps` / `4.29 kcps`; combined raw signal mean/range: `44.58 kcps` / `7.72 kcps`.
- Raw signal least-squares amplitudes:
  - `0.615 MHz`: `0.475 kcps`, amp/RMS `0.39`, `R2 = 0.156`.
  - `0.884 MHz`: `0.286 kcps`, amp/RMS `0.23`, `R2 = 0.117`.
  - `1.000 MHz`: `0.277 kcps`, amp/RMS `0.22`, `R2 = 0.115`.
  - `1.385 MHz`: `0.263 kcps`, amp/RMS `0.21`, `R2 = 0.113`.
- Raw detrended FFT strongest bins were off-model: about `1.220 MHz` (`0.797 kcps`), `1.098 MHz` (`0.764 kcps`), and `0.488 MHz` (`0.640 kcps`).
- A broad single-frequency raw-signal LS scan found its best point near `0.465 MHz`, but only with `R2 = 0.33`; this is not the programmed carrier or expected 13C sideband.
- Stored-average mean levels show large common-mode changes: common readout mean spans about `38.34..52.90 kcps`, peak-to-peak fraction about `31%`.

## Plausible interpretation

This Ramsey run is analyzable, but it still does not provide claim-grade T2star or 13C evidence. The programmed `1.0 MHz` Ramsey component is weak in the raw signal and remains weak in normalized views. The expected 13C sidebands are also weak. The prior `~0.884 MHz` scout component is not strongly reproduced, which argues against treating that previous feature as a stable physical carrier or sideband.

The off-model FFT features near `1.10..1.22 MHz` and the best single-frequency LS point near `0.465 MHz` may reflect noise, drift/common-mode changes, baseline shape, or a Ramsey phase/timing/calibration issue. They are not enough to fit or claim a physical T2star. The large average-to-average common-mode variation further weakens any interpretation based on small sub-kcps spectral amplitudes.

## Claims not yet supported

- No supported T2star value from this measurement.
- No supported 13C coupling/sideband conclusion.
- No supported claim that the Ramsey carrier follows the programmed `det = 1.0 MHz`.
- No supported assignment of the `1.10..1.22 MHz` or `0.465 MHz` features to NV physics.
- No reason to revise the accepted r03 pODMR alignment conclusion from this Ramsey alone.

## Recommended next action

Do not spend the next step on a blind higher-shot T2star repeat. First run a focused Ramsey route/phase diagnostic: inspect the active Ramsey timing/phase path against saved metadata, then use a compact det-dependence Ramsey check on r03 after fresh tracking, with at least two programmed det values and enough points to verify whether the observed oscillation follows the programmed phase ramp. Only return to a longer T2star/13C acquisition after the Ramsey carrier behavior is demonstrated.
