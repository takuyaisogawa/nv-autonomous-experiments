# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Planning/model context: `evidence/e014.json`.
- New Ramsey run: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Unpacked raw arrays: `ExperimentData` shape `[1, 2, 41]`; `ExperimentDataEachAvg` shape `[1, 20, 2, 41]`. Per project protocol, readout 1 is the reference and readout 2 is the Ramsey signal.
- Confirmed terminal health: job/status completed, final counts `43.433 kcps`, no stop requested, no monitor error, no safety abort.
- Scan parameters: `tau = 48 ns..8.048 us`, `200 ns` step, `41` points, `8.0 us` span, nominal resolution `125 kHz`, Nyquist `2.5 MHz`, `20 x 50000 = 1.0e6` shots per tau point, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
- Stored-average SEM estimates: median raw signal SEM `0.850 kcps`; median `signal/reference` SEM `0.01161`.
- Snake-order drift check: no flagged averages with the project-style `15%` drop threshold. Largest common-mode negative slope was about `6.5%`; largest single-trace drop score was about `8.0%`.
- Least-squares frequency checks with constant plus linear background:
  - Programmed carrier `1.5 MHz`: `signal/reference` amplitude `0.01575` full span and `0.01231` after skipping first 4 tau points; raw signal amplitude `0.705 kcps` full span and `0.512 kcps` skip-4.
  - Expected 13C sidebands from the project model, `1.115/1.885 MHz`: `signal/reference` amplitudes `0.00278/0.00962` full span and `0.00067/0.00527` skip-4.
  - The largest broad LS components are not a clean carrier/sideband pattern: low-frequency structure near the search floor dominates, and an unplanned lobe near `2.27 MHz` is comparable to or larger than the carrier in the normalized screens.
- FFT check on detrended `signal/reference`: carrier-adjacent bins appear near `1.463/1.585 MHz`, but similarly strong bins also appear near `2.195/2.317 MHz`. Skip-4 FFT still shows mixed carrier-adjacent and unplanned high-frequency content.
- Per-average consistency: the carrier was the non-low-frequency top component in `5/20` averages and in the top two in `7/20`. The expected low/high 13C sidebands were top components in `0/20` and `2/20` averages, respectively. Carrier phase resultant was moderate (`R = 0.669`); sideband phase resultants were weak (`R = 0.163` low, `0.336` high).
- Descriptive carrier-decay fits were run only as diagnostics. They returned inconsistent effective T2* values across views (`~1 us` raw/refline, `~2.15 us` ratio), so they are not promoted.

## Plausible interpretation

This is a valid terminal Ramsey dataset on accepted `image145844_reimage_r03`, not a failed acquisition. It contains weak carrier-adjacent structure near the programmed `1.5 MHz`, but the amplitude is small relative to point scatter and it weakens after skipping early tau points. The run does not convert the prior mixed Ramsey evidence into a clean carrier-plus-decay result.

The expected nearby-13C sidebands at about `1.115 MHz` and `1.885 MHz` are not consistently present. The low sideband is essentially absent in combined and per-average checks; the high sideband is weak and not paired with the low sideband. The strongest non-carrier structure remains mixed with low-frequency transient/background behavior and an unassigned high-frequency lobe near `2.27 MHz`.

## Claims not yet supported

- No numeric T2* claim is supported from this run.
- No nearby-13C coupling claim is supported from this run.
- A strong absence claim for all nearby 13C spins is not supported; the supported statement is narrower: this Ramsey branch has not shown a consistent carrier/sideband signature at the expected 13C targets.
- The `~2.27 MHz` lobe should not be assigned to sample physics or 13C without a targeted control.
- The diagnostic decay fits should not be quoted as T2* because signal presence and model consistency are not established.

## Recommended next action

Do not run another identical long-span Ramsey repeat. Record this refreshed-center high-shot Ramsey as non-claim-grade for T2* and 13C. If continuing on `r03`, switch to an alternate carrier-validation protocol that suppresses early-time/background structure and tests whether the Ramsey carrier tracks a deliberate detuning change before any T2* fit is promoted; otherwise close the current Ramsey branch as unsupported under these conditions.
