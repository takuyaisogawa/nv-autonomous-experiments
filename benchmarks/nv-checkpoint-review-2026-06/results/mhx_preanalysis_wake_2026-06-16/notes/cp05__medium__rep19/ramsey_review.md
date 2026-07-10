# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus relevant `md/memory.md` / `md/knowledge.md` context.
- New measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Run metadata/status: `measurement/m002.json` through `measurement/m005.json`.
- Prior target expectations from project context: accepted r03 NV, refreshed weak-pi pODMR center `mw_freq = 3.8765 GHz`; Ramsey detuning `det = 1.5 MHz`; expected 13C sidebands near `1.115 MHz` and `1.885 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis.json` and `ramsey_review_plot.png`.
- Checks performed:
  - Terminal health/status: run completed, final count `43.433 kcps`, `stop_requested=false`, monitor `last_error=""`, safe shutdown ok, not aborted.
  - Readout role check from embedded `ramsey.xml`: readout 1 is the true 0-level reference; with `full_experiment=0`, readout 2 is the Ramsey signal.
  - Scan geometry: `tau = 0.048..8.048 us`, `41` points, `0.2 us` step, `8.0 us` span, nominal frequency resolution `125 kHz`, Nyquist `2.5 MHz`, `20 x 50000 = 1.0e6` shots per tau.
  - Local per-average drift screen on raw/normalized traces: no robust outlier averages flagged.
  - Signal views: raw signal, signal/reference, and signal/fitted-reference-line.
  - FFT and least-squares sinusoid screens on full span and after skipping first 4 tau points.
  - Target least-squares amplitudes at `1.5 MHz`, `1.115 MHz`, `1.885 MHz`, prior `1.192 MHz` control, and prior det-shift `1.623 MHz`.

## Plausible interpretation

- The dataset is terminal and analyzable; no hard run anomaly is evident from the local files.
- The strongest full-span LS screen in the normalized Ramsey signal is at the Nyquist edge (`~2.499 MHz`, normalized amplitude `~0.285`) and remains Nyquist-edge-dominated after skipping the first 4 tau points. This is not a clean physical carrier/sideband result and is likely dominated by alternating-point/high-frequency structure or endpoint/conditioning sensitivity.
- Away from the Nyquist edge, the most plausible target-like component is near the programmed carrier: excluding the high-edge region, the normalized LS screen peaks near `1.515 MHz`, close to the `1.5 MHz` detuning. The direct `1.5 MHz` target amplitude is `0.0146` in signal/refline units and `0.705 kcps` in raw signal. Median per-point SEM is `0.00937` normalized and `0.850 kcps` raw, so this is weak.
- Per-average target phase consistency is best at the carrier (`vector_coherence ~0.85`) but not at the 13C sidebands (`~0.28` lower, `~0.45` upper). The sideband target amplitudes are small: `0.0032` at `1.115 MHz` and `0.0054` at `1.885 MHz`, both below the carrier and near/no better than noise-scale structure.
- This run modestly supports that a weak det-tracking Ramsey component may be present, but the trace is not clean enough to promote a reliable T2star fit. The repeated lack of clean carrier/sideband behavior across prior runs remains important context.

## Claims not yet supported

- No well-supported numeric T2star is supported from this dataset.
- No nearby 13C claim is supported: the expected sidebands are not strong, isolated, or per-average-consistent.
- The Nyquist-edge `~2.5 MHz` feature should not be claimed as a physical Ramsey/13C feature from this scan.
- The refreshed pODMR center remains a frequency calibration input, not a T2star or 13C conclusion.

## Recommended next action

- Avoid another blind Ramsey repeat on the same settings. The project can now either:
  - switch to an alternate protocol designed to suppress/read through the apparent high-frequency/alternating-point artifact and test coherence more directly, or
  - record a supported negative/unsupported conclusion for r03 under the current Ramsey conditions: aligned NV found, but T2star and 13C remain unsupported by the completed Ramsey branch.
