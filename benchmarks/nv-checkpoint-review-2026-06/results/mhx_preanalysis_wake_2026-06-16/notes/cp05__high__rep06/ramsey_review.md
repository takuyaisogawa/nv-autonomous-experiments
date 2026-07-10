# Ramsey review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`, and prior project constraints summarized there.
- New terminal Ramsey data: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` run status, `measurement/m005.json` run control.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed raw arrays: `ExperimentData` shape `(1, 2, 41)` and `ExperimentDataEachAvg` shape `(1, 20, 2, 41)`.
- Confirmed terminal/run health: job completed, final counts `43.433 kcps`, no stop request, empty monitor error, safe shutdown true.
- Checked scan parameters: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=0.048..8.048 us` in `0.2 us` steps, `41` points, `20 x 50000 = 1.0e6` shots/tau, snake scan order.
- Computed raw signal, point-wise `signal/reference`, and fitted-reference-line normalization.
- Ran least-squares frequency screens over `0.125..2.45 MHz`, both full span and skipping the first 4 tau points.
- Evaluated target amplitudes at expected carrier/sidebands: `1.500 MHz`, `1.115 MHz`, `1.885 MHz`; also checked prior/control frequencies `1.192 MHz`, `1.623 MHz`, and the empirical top near `2.27 MHz`.
- Ran weighted multi-frequency ratio fits and damped Gaussian sinusoid fits, with both fixed `1.5 MHz` carrier and free frequency.
- Ran a simple per-average drift/outlier check using median residuals; it flagged no averages, but per-average mean ratio varied from `0.8911` to `0.9593`.

## Plausible interpretation

- The data are usable and not obviously failed.
- There is a reproducible carrier-like component near the programmed detuning:
  - Ratio LS amplitude at `1.500 MHz`: `0.01575 +/- 0.00445` full span (`z=3.54`) and `0.01231 +/- 0.00390` after skipping first 4 points (`z=3.15`).
  - Raw-signal amplitude at `1.500 MHz`: `0.705 +/- 0.201 kcps` full span and `0.512 +/- 0.152 kcps` after skipping first 4 points.
  - The previous fixed `1.192 MHz` feature is weak here (`z~0.38` full ratio, `z~0.43` skip-first-4 ratio), so this run is not just reproducing that earlier artifact.
- However, the strongest empirical frequency screen is not the planned carrier:
  - Ratio full-span top is near `2.270 MHz` with amplitude `0.01845`, above the `1.516 MHz` carrier-near peak.
  - The same `~2.27 MHz` top persists in raw signal and fitted-reference-line normalization, and after skipping the first 4 tau points.
  - Free-frequency damped fits prefer `2.269 MHz` full span and `2.227 MHz` skip-first-4 over the fixed `1.5 MHz` model.
- A fixed-carrier damped fit gives a descriptive `T2* ~4.6 us` full span and `~4.7 us` after skipping first 4 points, but this should not be promoted because the free-frequency model fits better and the residual reduced chi-squared remains high (`~2.4` fixed-carrier full, `~2.0` fixed-carrier skip-first-4).
- The 13C sideband case is not supported:
  - The lower sideband `1.115 MHz` is absent (`z~0.54` full ratio, `z~0.16` skip-first-4 ratio).
  - The upper sideband `1.885 MHz` is at most marginal (`z~1.99` full ratio, `z~1.23` skip-first-4 ratio; higher only in multi-frequency fits that also include the unexplained `2.27 MHz` term).
  - Per-average top frequencies are mixed rather than consistently carrier/sideband locked.

## Claims not yet supported

- A well-supported numerical `T2*` for r03.
- A supported nearby `13C` coupling conclusion.
- That the `2.27 MHz` component is physical NV Ramsey precession rather than an artifact, alias, transient, or unmodeled sequence/readout effect.
- Sub-grid precision on the pODMR/Ramsey microwave center beyond the prior grid-supported `3.8765 GHz` calibration.

## Recommended next action

Do not run another blind same-configuration Ramsey. Treat this as improved but still non-claim-grade evidence: it supports a weak carrier-like response near `1.5 MHz`, rejects promotion of the old `1.192 MHz` feature, and does not support 13C. The next project action should be a decision/control step: either record a supported "T2*/13C unsupported under current Ramsey conditions" conclusion for r03, or design a targeted alternate protocol/control specifically to disambiguate the stronger `~2.27 MHz` component from the programmed-carrier Ramsey response before fitting or claiming `T2*`.
