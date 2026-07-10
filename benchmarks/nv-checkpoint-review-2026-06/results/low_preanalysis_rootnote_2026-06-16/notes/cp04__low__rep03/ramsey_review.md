# Ramsey Review: r03 det=1.5 MHz shift-check

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective and prior decision context.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: submitted job contract for `nv23_ramsey_20260514_015423_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal status/control snapshots.
- Generated locally: `ramsey_detshift_analysis.json` and `ramsey_detshift_analysis.png`.

## Calculations/scripts run

- Parsed the raw export with Python/NumPy.
- Confirmed scan shape: `tau = 0.048..1.968 us`, `41` points, `48 ns` step, `12` averages, `90000` repetitions, `mw_freq = 3.8759 GHz`, programmed `det = 1.5 MHz`.
- Treated the two readout channels as signal/reference and reviewed both raw signal and signal/reference ratio.
- Computed per-point SEM across stored averages: median signal SEM `0.745 kcps`, median ratio SEM `0.0146`.
- Checked average-level common-mode drift from per-average signal/reference means. Median common level was `46.51 kcps`, robust sigma `2.40 kcps`, and no averages exceeded a 3 robust-sigma flag.
- Ran least-squares sinusoid screens with constant + linear baseline terms over `0.2..2.5 MHz`, plus FFT checks on detrended ratio data.
- Explicitly checked target frequencies: programmed `1.500 MHz`, det-tracking prediction from the prior `~1.192 MHz` feature to `~1.692 MHz`, prior fixed `1.192 MHz`, and candidate 13C sideband positions near `1.307/2.076 MHz` and `1.116/1.884 MHz`.
- Repeated frequency screens after skipping early tau points to test sensitivity to the known early-time transient.

## Plausible interpretation

- The measurement completed and is analyzable; there is no hard run anomaly in the local snapshots.
- This det-shift run does not cleanly validate the prior `~1.192 MHz` component as a physical Ramsey carrier. In the full ratio LS screen, the broad low-frequency baseline dominates; the first non-low-frequency ratio component is near `1.61 MHz` with amplitude `0.030`, close to the explicit `1.692 MHz` target amplitude `0.0298`.
- The `1.692 MHz` det-tracking target has only weak support: ratio amplitude is about twice the median ratio SEM, but raw-signal amplitude is only `0.099 kcps`, far below the signal SEM `0.745 kcps`. The programmed `1.500 MHz` target is similarly weak in ratio and essentially absent in raw signal (`0.037 kcps`).
- The prior fixed `1.192 MHz` feature is not dominant in the full ratio analysis (`0.0059` ratio amplitude), although raw-signal-only fits still show broad structure around `~0.9..1.2 MHz`. That points more toward baseline/transient/readout structure than a stable Ramsey carrier.
- Skip-transient checks are not stable enough to rescue a carrier claim. Depending on skipped points, ratio screens shift between low-frequency baseline and weak components; raw-signal screens are dominated by slow structure.
- The best current reading is still: r03 remains a valid aligned NV candidate from pODMR, but the Ramsey data under the tried conditions have not produced a supported carrier/decay model.

## Claims not yet supported

- No supported numeric `T2*` claim from this det-shift Ramsey.
- No supported nearby `13C` coupling/sideband claim.
- No supported claim that the earlier `~1.192 MHz` feature det-tracks with programmed detuning.
- No supported claim that the programmed `1.5 MHz` carrier is resolved in raw signal.
- No supported reason to promote a damped-sinusoid fit parameter as physical; any such fit would be descriptive only.

## Recommended next action

Stop blind Ramsey repeats on r03 under the current protocol. The det-shift diagnostic failed to produce a clean det-following raw/readout-aware carrier. The next project decision should be one of:

1. Switch to an alternate coherence protocol or readout strategy intended to establish whether the Ramsey contrast is being lost at very short tau or masked by readout/transient structure.
2. Close the r03 Ramsey branch with a supported statement that alignment is established, but `T2*` and `13C` remain unsupported under the tested Ramsey conditions.
