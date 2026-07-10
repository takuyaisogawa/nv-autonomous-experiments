# Ramsey Review: Refreshed-Center r03 Long-Span Run

## Files/data used

- Project context: `project/state.md`, `project/advice.md`, `context.json`, plus relevant guidance in `md/memory.md` and `md/knowledge.md`.
- Measurement data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Measurement metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Planning context: `evidence/e014.json` and `evidence/e017.json` for the intended refreshed-center Ramsey plan and target frequencies.
- Local outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran schema/axis checks with Python. `ExperimentData` has shape `[2, 41]`; `ExperimentDataEachAvg` has shape `[20, 2, 41]`, and averaging the per-average array reproduces `ExperimentData`, so the axis contract is consistent with `[avg, readout, tau]`.
- Ran `python analyze_ramsey.py`.
- Confirmed terminal acquisition status: job `nv23_ramsey_20260514_055148_auto_ramsey` completed, final counts `43.433 kcps`, no stop request, no monitor error, and no local hard anomaly.
- Confirmed scan settings: `ramsey.xml`, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us`, `41` points, `20 x 50000` shots (`1.0e6` shots/tau), snake scan order with data saved in tau order.
- Computed raw signal, point-wise `signal/reference`, and `signal/fitted-reference` views; linear-detrended LS frequency screens; FFT screens; explicit LS amplitudes at carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior artifact-control `1.192 MHz`, and prior det-shift top `1.623 MHz`; and per-average top-frequency checks.
- Local drift/provenance check: per-average reference means span `41.74..54.90 kcps`, signal means span `37.38..50.37 kcps`, while mean ratio spans `0.891..0.959`. This local common-mode check flagged no averages under the script's robust advisory threshold, but it is not the MATLAB scan-order drift analyzer.

## Plausible interpretation

- The data are usable terminal Ramsey data, not an acquisition failure.
- The refreshed pODMR center did not recover a clean Ramsey carrier/decay model. In the `signal/fitted-reference` view, the programmed `1.5 MHz` carrier LS amplitude is `0.01445`, only `0.83x` the median per-point SEM for that view; raw carrier amplitude is `0.705 kcps`, also below the project-plan expected order-`2..6 kcps` raw oscillation scale.
- The expected 13C sideband amplitudes are smaller than the carrier in the normalized view: `0.00296` at `1.115 MHz` and `0.00533` at `1.885 MHz`.
- The largest exploratory full-span normalized LS component is near `2.271 MHz`, not the programmed carrier, expected sidebands, prior `1.192 MHz` artifact-control, or prior `1.623 MHz` det-shift top. Skipping the first four tau points leaves the top near `2.271 MHz` but lowers its amplitude.
- Per-average screens are mixed: only `2/20` per-average top frequencies fall within `175 kHz` of the `1.5 MHz` carrier, and `5/20` fall within `175 kHz` of either expected 13C sideband. Several per-average screens peak at unrelated or boundary frequencies.
- Most plausible reading: this high-shot refreshed-center Ramsey run remains non-claim-grade. It argues against a simple stale-center explanation for the previous weak Ramsey evidence and does not show a stable carrier/sideband pattern suitable for T2star or 13C extraction.

## Claims not yet supported

- Do not claim a numeric T2star from this run. A damped-sinusoid fit would be fitting weak/mixed spectral content rather than a supported Ramsey fringe.
- Do not claim nearby 13C coupling from this run. The expected sidebands are not dominant, consistent, or per-average-stable.
- Do not promote the off-target `~2.27 MHz` component as a physical signal. It is not tied to the programmed detuning or expected 13C sidebands and lacks per-average consistency.
- Do not claim that r03 has no nearby 13C at all; the supported statement is narrower: no well-supported 13C conclusion from the Ramsey data collected so far under these conditions.

## Recommended next action

Stop blind/repeated Ramsey accumulation on r03 under the same protocol. Record the r03 Ramsey/T2star/13C branch as unsupported under the tested Ramsey conditions, and pivot only to a targeted alternate diagnostic if the project needs more physics from this NV, such as a protocol/readout validation or a different coherence/spectroscopy route rather than another refreshed-center 8 us Ramsey repeat.
