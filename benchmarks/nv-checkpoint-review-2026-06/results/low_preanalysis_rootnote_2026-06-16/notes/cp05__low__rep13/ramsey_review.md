# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Run metadata: `measurement/m002.json` submit spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` status, `measurement/m005.json` control.
- Recent local evidence snapshot: `evidence/e022.json`, `evidence/e023.json`, `evidence/e024.json`.
- Generated local analysis outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw-export axis contract: averaging `ExperimentDataEachAvg[scan, avg, readout, point]` reproduced `ExperimentData[scan, readout, point]` to numerical precision (`ref_max_abs_diff=1.4e-14`, `sig_max_abs_diff=7.1e-15`).
- Used the active `ramsey.xml` readout roles from the export: readout 1 is the 0-reference, readout 2 is the Ramsey signal because `full_experiment=0`.
- Checked full-span and skip-first-4-points least-squares sinusoid amplitudes with intercept+slope terms for raw signal, point-wise ratio, and fitted-reference normalization.
- Checked FFT peaks after demeaning/windowing.
- Compared programmed carrier and sideband targets: carrier `1.5 MHz`, expected 13C sidebands `1.115 MHz` and `1.885 MHz`, plus prior empirical controls near `1.192 MHz` and `1.623 MHz`.

## Plausible interpretation

- The run completed cleanly: `20 x 50000` shots, tau `0.048..8.048 us` in 41 points, final counts `43.433 kcps`, no stop request or bridge error.
- There is a carrier-like component near the programmed detuning. Full-span LS amplitude at `1.5 MHz` is `0.705 kcps` in raw signal, `0.0157` in point-wise ratio, and `0.0145` in fitted-reference normalization. The grid screen also finds a nearby `1.515 MHz` component.
- The carrier-like feature is not strong enough to promote a T2star fit. It is comparable to the median raw signal SEM (`0.850 kcps`) and not uniquely dominant: the strongest full-span LS component in all three views is near `2.27 MHz`, with raw amplitude `0.818 kcps` and point-wise ratio amplitude `0.0185`.
- Excluding the first four tau points keeps the same qualitative result: `1.5 MHz` remains visible (`0.512 kcps` raw, `0.0123` ratio), but `~2.27 MHz` remains slightly stronger.
- The expected 13C sidebands are weak: full-span raw amplitudes are `0.146 kcps` at `1.115 MHz` and `0.261 kcps` at `1.885 MHz`; point-wise ratio amplitudes are `0.00277` and `0.00961`. The minus sideband especially is not supported, and the plus-sideband-sized feature is not cleanly separable from neighboring screen peaks.
- Per-average frequency screens are mixed rather than repeatedly selecting the programmed carrier or sidebands. A few averages peak near `1.53..1.58 MHz`, but many peak elsewhere, including low-frequency and `>2 MHz` regions.
- Average-level common-mode variation is nontrivial (`ref` mean range `41.74..54.90 kcps`, `sig` mean range `37.38..50.37 kcps`, CV about `6.7..7.1%`). The ratio/fitted-reference views reduce but do not remove the ambiguity.

## Claims not yet supported

- No well-supported numeric T2star from this run.
- No supported nearby 13C conclusion from sidebands at `1.115/1.885 MHz`.
- No claim that the `~2.27 MHz` component is physical; it is a stronger screen peak but lacks a planned-model assignment in the provided context.
- No sub-grid refinement of the pODMR center beyond the prior grid-supported `3.8765 GHz` calibration.

## Recommended next action

Do not launch another blind Ramsey repeat on r03 under the same conditions. The project has now accumulated multiple non-claim-grade Ramsey datasets; this refreshed-center high-shot long-span run gives useful evidence that the route is working and the detuning can appear weakly, but it still does not yield a clean carrier/sideband model. Next, choose between an alternate protocol targeted at T2/13C contrast, such as Hahn/CPMG/XY8 after route review, or closing the r03 Ramsey branch with a supported negative/unsupported T2star and 13C conclusion under the current Ramsey conditions.
