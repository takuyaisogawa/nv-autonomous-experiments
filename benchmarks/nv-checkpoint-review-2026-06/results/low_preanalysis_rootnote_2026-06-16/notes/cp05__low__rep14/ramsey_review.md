# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json`.
- Run/spec/status metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Local analysis outputs created here: `analyze_ramsey.py`, `ramsey_analysis_results.json`, `ramsey_review_plot.png`.

## Calculations or Scripts Run

- Ran `python analyze_ramsey.py`.
- Parsed the terminal raw export for `nv23_ramsey_20260514_055148_auto_ramsey`: `tau=0.048..8.048 us`, `41` points, `0.2 us` step, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `20 x 50000` repetitions.
- Checked raw signal/reference channels, point-wise ratio, and signal divided by a fitted reference line.
- Checked per-average common-mode stability using `ExperimentDataEachAvg` and `ScanOrderEachAvg`; no averages exceeded the 20% common-mode drift flag threshold. Largest common-mode deviations were about `+13.3%` and `-14.8%`.
- Screened sinusoidal least-squares amplitudes across `0.2..2.3 MHz`, excluding the near-Nyquist artifact region from the main interpretation.
- Checked targets: programmed carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior artifact/control `1.192 MHz`, and previous det-shift top `1.623 MHz`.
- Compared amplitudes against noise/scatter: median raw signal SEM was `1.96 kcps`; median across-average SEM was about `0.0136` in point-wise ratio and `0.0104` in fitted-reference normalization.

## Plausible Interpretation

- The run completed normally and is usable for analysis: bridge status is completed, stop was not requested, monitor error is empty, and no simple common-mode drift flag was triggered.
- The raw channel has only weak target-scale modulation. Programmed carrier amplitude is `0.099 kcps` in raw signal, far below the `1.96 kcps` median raw signal SEM. The upper 13C-sideband target at `1.885 MHz` is larger in raw signal (`0.232 kcps`) but still well below raw per-point SEM.
- In fitted-reference normalization, the strongest non-Nyquist screen peaks are around `0.807 MHz`, `1.924 MHz`, and `1.002 MHz` with amplitudes `0.00686`, `0.00569`, and `0.00503`, all below the estimated `0.0104` median normalized point SEM.
- The programmed `1.5 MHz` carrier is not dominant in fitted-reference normalization (`0.00220`) and is only a secondary feature in point-wise ratio (`~1.517 MHz`, amplitude `0.0198`), where reference-denominator structure is a known concern.
- The `1.885 MHz` sideband-adjacent feature appears in some normalized screens, but it is not accompanied by a consistent carrier and lower sideband model. Per-average frequency screens remain mixed and many are dominated by sampling/normalization artifacts near the excluded high-frequency region.
- The descriptive damped-cosine fits are not promotable: fitting from the top normalized screen gives `~0.808 MHz` with `T2star` pinned at the upper bound (`50 us`) and only `R2~0.50`; a carrier-seeded fit drifts toward `~1.889 MHz` with `R2~0.43`. These are model-instability symptoms, not a supported T2star.

## Claims Not Yet Supported

- No numeric T2star is supported from this run.
- No nearby 13C coupling conclusion is supported from this run.
- The `0.807 MHz`, `1.924 MHz`, or point-wise-ratio `~1.517 MHz` features should not be claimed as physical Ramsey components without a stable carrier/sideband pattern across normalization choices and averages.
- The refreshed pODMR center remains a usable frequency calibration, but this Ramsey does not validate a coherent `det=1.5 MHz` carrier response.

## Recommended Next Action

- Avoid another blind long-span Ramsey repeat on r03 under the same conditions.
- Make the project-level decision that the r03 Ramsey/13C branch is currently unsupported under these measurement conditions, unless there is a reason to try a different protocol.
- If continuing experimentally, change protocol rather than only increasing shots: use a Ramsey/echo-style control that first demonstrates a robust carrier on a reference NV or this NV with a stronger/readout-cleaner condition, or run a deliberately short, phase-controlled detuning diagnostic that can separate reference-channel artifacts from true signal before attempting another T2star/13C claim.
