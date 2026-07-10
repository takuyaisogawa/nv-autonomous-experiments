# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior Ramsey/design context: `evidence/e003.json`, `evidence/e006.json`, `evidence/e009.json`, `evidence/e017.md`.
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Scratch outputs created here: `analyze_ramsey_shorttau.py`, `ramsey_analysis_summary.json`, `ramsey_shorttau_review.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- Parsed the raw export as two readouts over 41 tau points and 12 stored averages. Used the project-recorded Ramsey readout convention: readout 1 is the reference, readout 2 is the Ramsey signal.
- Checked terminal status and acquisition settings: completed run `nv23_ramsey_20260513_230331_auto_ramsey`, `tau=48 ns..1.968 us`, 48 ns step, 41 points, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000 = 1.08e6` shots per tau point, final counts `35.122 kcps`, no stop request, monitor `last_error=""`, safe shutdown true.
- Computed raw signal/reference ratio, per-point SEM across averages, linear-detrended residual sizes, fixed-frequency least-squares screens at `1.000 MHz`, `0.615 MHz`, `1.385 MHz`, and prior `0.884 MHz`, a `0.3..3 MHz` frequency scan, FFT bins, bootstrap amplitudes over stored averages, per-average carrier phase consistency, a scan-order drift proxy, and a guarded damped-cosine trial fit.

## Plausible interpretation

- The short-tau/high-SNR diagnostic produced a real early-time Ramsey-like oscillatory feature. The combined linear-detrended peak-to-peak residual is `5.25 kcps` in raw signal and `0.1146` in ratio, above median point SEM of `1.14 kcps` and `0.0127`.
- The programmed `1.0 MHz` carrier is now visible at a materially stronger level than in the prior 8 us run: fixed-frequency LS gives ratio amplitude `0.0274` and raw-signal amplitude `1.28 kcps` with residual R2 improvement about `0.35..0.38`; bootstrap 95% interval for the ratio amplitude is `0.0217..0.0336`.
- The strongest free fixed-frequency ratio screen is near `1.192 MHz` with amplitude `0.0363` and R2 improvement `0.656`. A trial damped-cosine fit gives `f~1.198 MHz`, initial ratio amplitude `~0.042`, and `T2*~6.3 us`, but the `T2*` uncertainty is larger than the estimate (`~9.6 us` stderr), so this is descriptive only.
- Stored averages are not identical, but the fixed `1 MHz` phase is mostly coherent across averages; the carrier vector coherent fraction is `0.963`. There is count-level motion between averages, and the local drift proxy finds some acquisition-order trends, but no hard bridge/status anomaly. This should be treated as a caveat because the snapshot does not include an official MATLAB drift-analysis artifact for the new terminal run.
- Relative to the prior two non-claim-grade Ramsey runs, this supports the idea that the previous long-window result was at least partly an early-time/SNR/tau-window problem, not proof of absent Ramsey contrast on r03.

## Claims not yet supported

- No numeric T2* claim. The scan spans only `1.92 us`, and the damping fit is underconstrained.
- No nearby-13C claim or no-13C claim. The FFT bin spacing is `0.508 MHz` and nominal resolution is `0.521 MHz`, while the expected 13C sidebands are only about `0.385 MHz` from the carrier; this short scan cannot separate carrier and sidebands reliably.
- No exact Ramsey frequency/detuning claim. The `~1.19 MHz` descriptive maximum is close to the target-carrier scale, but the short span and drift caveats do not justify a precision frequency update.
- No claim that drift is irrelevant. The local proxy is useful but is not a replacement for the project-standard scan-order-aware drift diagnostic.

## Recommended next action

Design and advisory-check a targeted longer, no-tau0, high-SNR Ramsey extension on the same accepted r03, preserving the successful short-tau changes while adding enough time span to constrain decay and sidebands. Keep `mw_freq=3.8759 GHz` and a deliberate `det=1.0 MHz` basis unless the design explicitly tests the observed `~1.2 MHz` descriptive maximum. Aim for enough shots per point to keep the carrier visible, keep per-average tracking under the active cap by adjusting points/averages or splitting the run, and require terminal raw export plus official scan-order drift review before fitting T2* or making any 13C conclusion.
