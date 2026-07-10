# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus `md/memory.md` for local analysis posture.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal bridge status, and `measurement/m005.json` run control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_analysis.png`.

## Calculations Or Scripts Run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` as two readouts over 41 tau points and `ExperimentDataEachAvg` as 20 averages x 2 readouts x 41 tau points.
- Checked terminal health: job completed, bridge state completed, no stop request, no monitor error, `safe_shutdown_ok=true`, final count text `43.433 kcps`.
- Confirmed intended scan: `tau=48 ns..8.048 us`, `dt=200 ns`, 41 points, `20 x 50000 = 1.0e6` shots/tau, `mw_freq=3.8765 GHz`, `det=1.5 MHz`.
- Computed raw signal/reference traces, point-wise signal/reference, and signal divided by a fitted reference line.
- Ran least-squares sinusoid screens from `0.1..2.4 MHz` for full span and after skipping the first 4 tau points.
- Checked target amplitudes at the programmed carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, previous short-tau control `1.192 MHz`, and prior det-shift full-span frequency `1.623 MHz`.
- Ran windowed FFT checks on detrended raw signal and fitted-reference-line normalized signal.
- Screened each stored average separately for raw-signal frequency consistency.
- Ran local drift proxies from stored averages and snake order: mean signal by average ranged `37.38..50.37 kcps`; acquisition order was snake and even-average balanced.

## Plausible Interpretation

- The run is analyzable and has no hard terminal anomaly.
- The combined traces contain weak oscillatory structure, but it is not a clean Ramsey carrier/sideband result.
- In least-squares screens, the strongest combined component is near `2.27 MHz` in raw signal, point-wise ratio, and fitted-reference-line normalization. This is not the programmed `1.5 MHz` carrier and not the expected `1.115/1.885 MHz` 13C sidebands.
- FFT checks are mixed: full-span FFT peaks include about `2.317 MHz` and carrier-adjacent bins near `1.46/1.59 MHz`; skip-first-4 FFT places a carrier-adjacent bin near `1.486 MHz` slightly above `2.297 MHz`. This supports "weak mixed structure" rather than a robust model.
- The raw carrier least-squares amplitude is `0.705 kcps` full-span and `0.512 kcps` after skipping the first 4 points, while median per-point signal SEM is `0.850 kcps`. Fitted-reference-line carrier amplitudes are `0.0145` and `0.0105` in normalized units, comparable to ratio SEM scale (`0.0116`).
- Expected 13C sideband amplitudes are weaker: fitted-reference-line full-span `0.0030` at `1.115 MHz` and `0.0054` at `1.885 MHz`; skip-first-4 `0.00024` and `0.00255`.
- Per-average raw frequency screens are inconsistent: several averages hit the low-frequency screen boundary, others spread across about `0.34..2.4 MHz`; this does not repeat a single carrier or sideband pattern.
- Plausibly, the refreshed-center long-span Ramsey still suffers from weak Ramsey contrast plus brightness/track variation across averages, rather than revealing a well-supported T2star or nearby-13C signature.

## Claims Not Yet Supported

- No numeric T2star is supported from this measurement. The carrier/decay signal presence is not strong or consistent enough to promote a damped Ramsey fit.
- No nearby 13C claim is supported. The expected sidebands are not dominant, not repeatable per average, and are weaker than the carrier-adjacent/noise structure.
- The `2.27 MHz` component should not be claimed as a physical coupling or detuning feature from this dataset alone; it is off-target and close enough to the Nyquist-side/high-frequency region to require artifact checks.
- The refreshed pODMR center remains useful calibration provenance, but this Ramsey does not prove that frequency calibration was the limiting issue.

## Recommended Next Action

Do not run another blind long-span Ramsey repeat on r03. Close this Ramsey branch as non-claim-grade under the current protocol, then choose one targeted fork: either switch to an alternate coherence protocol/readout diagnostic that can verify actual Ramsey contrast and timing phase response, or make a supported negative/unsupported r03 T2star/13C conclusion under current conditions. If continuing experimentally, the next measurement should be a deliberate control, such as a phase/detuning calibration Ramsey at a high-contrast short window or a protocol less sensitive to the observed weak carrier and average-to-average brightness variation.
