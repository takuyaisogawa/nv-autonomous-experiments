# Ramsey det-shift review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- Current measurement: `measurement/m001.json` raw MAT export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Current run metadata/status/control: `measurement/m002.json` through `measurement/m005.json`.
- Prior local evidence for comparison: `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review, `evidence/e019.json` det-shift model/advisory, and `evidence/e009.py` to confirm the prior readout convention: readout 0 = reference, readout 1 = signal, normalized view = signal/reference.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_diagnostic.png`
  - `analysis_stdout.txt`
- Checks performed:
  - Parsed protocol and run completion metadata.
  - Computed raw reference/signal statistics and SEM.
  - Screened least-squares sinusoid amplitudes after a linear baseline in raw signal and signal/reference views.
  - Checked target frequencies: programmed `1.5 MHz`, prior empirical `1.192 MHz`, det-tracking prediction `1.692 MHz`, and expected 13C sidebands near `1.307 MHz` and `2.076 MHz`.
  - Screened each stored average for dominant normalized frequency.
  - Performed a drift proxy from stored-average mean ranges and confirmed scan order metadata is `snake`; the full prior bridge drift script was not runnable directly from this neutral snapshot.

## Quantitative summary

- Protocol: `tau = 0.048..1.968 us`, 41 points, 48 ns step, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `12 x 90000` shots per tau point, final counts `44.796 kcps`.
- Raw readouts: reference mean `48.08 kcps`, signal mean `44.27 kcps`; signal peak-to-peak `6.46 kcps`; median SEM `1.39 kcps` signal and `1.44 kcps` reference.
- Normalized signal/reference peak-to-peak is `0.134`, but low-frequency/baseline content is large: the 0.2 MHz edge component has LS amplitude `0.330`, much larger than the MHz-band targets.
- In the restricted `0.5..3.0 MHz` screen, signal/reference top components include `0.856 MHz` amplitude `0.0267`, `1.616 MHz` amplitude `0.0255`, and `1.696 MHz` amplitude `0.0250`.
- Target checks:
  - Programmed `1.5 MHz`: normalized amplitude `0.0240`, raw-signal amplitude `1.13 kcps`.
  - Det-tracking prediction `1.692 MHz`: normalized amplitude `0.0250`, raw-signal amplitude `1.22 kcps`.
  - Prior fixed `1.192 MHz`: normalized amplitude `0.0051`, raw-signal amplitude `0.47 kcps`.
  - Expected 13C sidebands: low `1.307 MHz` normalized amplitude `0.0095`, high `2.076 MHz` normalized amplitude `0.0062`.
- Raw-signal screen is not uniquely centered at the det-tracking prediction; stronger raw components appear around `0.878`, `0.958`, and `0.798 MHz`, with raw amplitudes `1.53`, `1.42`, and `1.42 kcps`.

## Plausible interpretation

The run completed and is analyzable. It weakens the fixed-artifact interpretation of the earlier `~1.192 MHz` feature because the exact prior frequency is weak in the det=1.5 MHz data. There is a plausible det-tracking hint: the normalized and raw target checks near `1.69 MHz` are comparable to or slightly above the programmed `1.5 MHz` target, and a restricted-band normalized screen includes `~1.696 MHz`.

This is still not claim-grade Ramsey evidence. The normalized trace has large low-frequency baseline/transient content, stored-average frequency screens are dominated by the lower search edge, and the raw-signal spectrum is not cleanly dominated by the det-tracking prediction. The data support "possible det-following Ramsey-like component under current conditions," not a robust physical carrier/decay model.

## Claims not yet supported

- No supported numeric T2star from this det-shift run.
- No supported nearby 13C conclusion: neither expected sideband is dominant or repeatably separated from baseline/raw-screen ambiguity.
- No supported claim that the `~1.19 MHz` feature was purely artifact or purely physical; the new run argues against a fixed-frequency artifact but does not establish a clean carrier model.
- No supported sub-grid resonance refinement beyond the prior `3.8759 GHz` pODMR-supported working frequency.

## Recommended next action

Do a bridge-free synthesis across all four r03 Ramsey datasets and decide whether the project standard allows a supported negative/unsupported Ramsey/13C conclusion under current Ramsey conditions. If more hardware time is justified, do not run another blind Ramsey repeat; use an alternate protocol or a deliberately diagnostic Ramsey variant that suppresses the early-time baseline/transient and tests the carrier with a stronger raw-signal criterion.
