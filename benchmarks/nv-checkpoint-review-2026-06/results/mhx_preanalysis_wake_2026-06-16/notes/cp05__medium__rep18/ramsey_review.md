# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: objective, prior Ramsey/pODMR context, terminal-review criteria.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted Ramsey spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control records.
- Created local outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed combined and per-average readouts. Treated readout 1 as reference and readout 2 as Ramsey signal, per project protocol notes.
- Checked raw signal, point-wise `signal/reference`, and `signal/fitted-reference-line` views.
- Ran least-squares sinusoid screens over `0.25..2.45 MHz`, plus windowed FFT checks.
- Checked full-span data and skip-first-4-point data.
- Evaluated target frequencies: programmed carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior artifact/control `1.192 MHz`, prior det-shift top `1.623 MHz`, and prior det-tracking target `1.692 MHz`.
- Reviewed per-average frequency-screen consistency and simple average-level common-mode drift.

## Quantitative summary

- Run completed: `nv23_ramsey_20260514_055148_auto_ramsey`, final counts `43.433 kcps`, safe shutdown OK, `tau=0.048..8.048 us`, `41` points, `20 x 50000` shots, `mw_freq=3.8765 GHz`, `det=1.5 MHz`.
- Median per-point SEM from stored averages: raw signal `0.850 kcps`; ratio `0.0116`.
- Full-span LS top:
  - raw signal: `2.271 MHz`, amplitude `0.818 kcps`;
  - point-wise ratio: `2.270 MHz`, amplitude `0.01845`;
  - fitted-reference ratio: `2.271 MHz`, amplitude `0.01678`.
- Skip-first-4 LS top remains near `2.266..2.271 MHz`, not at the programmed carrier or expected 13C sidebands.
- Carrier `1.500 MHz` amplitudes are present but weak: full-span raw `0.705 kcps` and ratio `0.01575`; these are below/near the measured SEM scale and have amplitude/residual-sigma `<1`.
- Expected 13C sidebands are weaker/inconsistent: full-span ratio amplitudes `0.00277` at `1.115 MHz` and `0.00961` at `1.885 MHz`; skip-first-4 lower sideband falls to `0.00068`.
- FFT is not decisive: ratio FFT peaks near `1.463/1.486 MHz` for full/skip views, while LS amplitude screens prefer `~2.27 MHz`.
- Per-average ratio screens are mixed: only `6/20` averages have top frequency within `0.2 MHz` of the `1.5 MHz` carrier, and `5/20` are within `0.2 MHz` of the combined `~2.27 MHz` LS top.
- Average-level common-mode variation flags averages `6` and `11` under a simple `>12%` relative-deviation heuristic, but robust z-scores are below `2.3`; excluding those averages does not change the main result (`~2.27 MHz` remains the LS top).

## Plausible interpretation

The refreshed-center long-span Ramsey is analyzable and did not fail operationally, but it still does not provide a clean Ramsey carrier/decay model. The programmed `1.5 MHz` component is weak relative to SEM/residual scales, the strongest LS component is an unplanned `~2.27 MHz`, FFT and LS emphasize different frequencies, and per-average screens are not coherent. This supports the project trend that r03 Ramsey under the current protocol/settings is not producing claim-grade T2star or 13C evidence.

## Claims that are not yet supported

- No numeric T2star should be promoted from this dataset.
- No nearby 13C coupling/sideband claim is supported.
- The `~2.27 MHz` LS top should not be treated as a physical Ramsey frequency without an explicit follow-up; it is not the programmed carrier or planned 13C sideband target and is not per-average coherent.
- The weak carrier-like FFT content near `1.5 MHz` is not enough by itself to claim a carrier/decay model.

## Recommended next action

Do not run another blind long-span Ramsey repeat on r03. Record this refreshed-center 20-average run as non-claim-grade, then choose between an alternate contrast-validation protocol and a supported "T2star/13C unsupported under current r03 Ramsey conditions" conclusion. If continuing experimentally, the next measurement should directly test the failure mode, for example a controlled Ramsey phase/detuning/contrast validation at selected tau points before any more T2star or 13C extraction attempts.
