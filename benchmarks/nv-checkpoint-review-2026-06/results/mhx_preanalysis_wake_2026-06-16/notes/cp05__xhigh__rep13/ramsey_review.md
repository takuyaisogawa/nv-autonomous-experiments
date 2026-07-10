# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` status, `measurement/m005.json` control.
- Supporting local references checked: `evidence/e003.json` for the prior scan-order drift-analysis convention, and `evidence/e021.log`/measurement records for error/final-count text.

## Calculations or scripts run

- Added and ran `analyze_ramsey.py`.
- Generated `ramsey_analysis_summary.json` and `ramsey_analysis_plot.png`.
- Checks performed:
  - raw schema/layout check: combined `ExperimentData` equals the mean of `ExperimentDataEachAvg` to numerical precision;
  - run-health check from bridge result/status/control;
  - scan-order-aware drift screen using `Scan.ScanOrderEachAvg` snake order;
  - raw signal, point-wise `signal/reference`, and linear-reference normalization;
  - continuous least-squares sinusoid screens from 0.2 to 2.4 MHz, both full span and with the first 4 tau points skipped;
  - FFT sanity check with linear detrending/Hann window;
  - target-frequency LS amplitudes at 1.500 MHz carrier, 1.115/1.885 MHz expected 13C sidebands, and prior empirical controls near 1.192 and 1.623 MHz;
  - per-average top-frequency and phase-consistency checks.

## Key quantitative checks

- Run completed cleanly: `nv23_ramsey_20260514_055148_auto_ramsey`, started `2026-05-14T05:51:56`, finished `2026-05-14T09:28:25`, elapsed `12990 s`, final counts `43.433 kcps`, safe shutdown OK, `stop_requested=false`, monitor `last_error=""`.
- Measurement settings: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, tau `48 ns..8.048 us`, `41` points, `200 ns` step, `20 x 50000` repetitions = `1.0e6` shots/tau. Nyquist is `2.5 MHz`; nominal FFT bin spacing is about `122 kHz`.
- Readout statistics: reference mean `48.789 kcps`, signal mean `44.670 kcps`, mean signal/reference `0.9156`. Median SEMs: raw signal `0.850 kcps`, signal/reference `0.0116`, linear-reference normalization `0.00937`.
- Drift: no averages flagged. Worst common-mode drop score was `0.064`; worst single-trace drop score was `0.080`, both below the `0.15` threshold used for this style of review.
- Full-span LS frequency screens:
  - raw signal top: `2.271 MHz`, amplitude `0.818 kcps`;
  - signal/reference top: `2.270 MHz`, amplitude `0.01845`;
  - signal/linear-reference top: `2.271 MHz`, amplitude `0.01678`.
  Skipping the first 4 tau points did not move the top away from about `2.27 MHz`.
- Target LS amplitudes in signal/reference:
  - carrier `1.500 MHz`: amplitude `0.01575`, about `1.36x` median ratio SEM;
  - lower 13C sideband `1.115 MHz`: `0.00278`, about `0.24x` SEM;
  - upper 13C sideband `1.885 MHz`: `0.00962`, about `0.83x` SEM;
  - prior `1.192 MHz` control: `0.00194`, about `0.17x` SEM;
  - prior det-shift `1.623 MHz` control: `0.00801`, about `0.69x` SEM.
- Raw-signal carrier amplitude was only `0.705 kcps`, about `0.83x` raw-signal SEM. Linear-reference carrier amplitude was `0.01447`, about `1.54x` its median SEM.
- FFT sanity check is mixed: signal/reference has nearby bins around `1.463` and `1.585 MHz` slightly above the `2.317 MHz` bin, while the continuous LS screen prefers `2.27 MHz`. This is not a clean carrier-only result.
- Per-average screens are inconsistent: top frequencies span `0.356..2.341 MHz`; only `5/20` averages have a top within `0.15 MHz` of the 1.5 MHz carrier, and only `3/20` are sideband-like. Carrier phase consistency is moderate (`phase resultant 0.67`); sidebands are weak/incoherent (`0.16` lower, `0.34` upper).

## Plausible interpretation

The measurement is technically usable and not obviously compromised by run failure or scan-order drift. It provides a higher-shot, refreshed-center Ramsey dataset on the accepted r03 NV.

The data still do not support a clean Ramsey carrier/decay model. There is a weak carrier-like component in some combined checks, but it is comparable to empirical SEM, is not the dominant continuous LS feature, and is not stable enough across averages. The expected 13C sidebands are weaker than the carrier and are not per-average coherent.

This is best treated as additional non-claim-grade Ramsey evidence: r03 remains a supported aligned candidate, but this terminal long-span Ramsey does not establish a numerical T2star or nearby-13C coupling conclusion.

## Claims not yet supported

- A numerical T2star for r03 from this run.
- A resolved nearby 13C sideband/coupling claim at `1.115/1.885 MHz`.
- Treating the `2.27 MHz` screen maximum as a physical Ramsey frequency.
- Treating the weak `1.5 MHz` carrier amplitude as sufficient for a decay fit.
- A definitive physical absence of nearby 13C; the supported statement is narrower: no well-supported 13C evidence appears in the current Ramsey datasets under this protocol.

## Recommended next action

Do not run another blind repeat of the same Ramsey branch. Close this refreshed-center long-span Ramsey as analyzable but non-claim-grade, then make the project decision called out in `project/state.md`: either move to an alternate protocol designed to fix the weak/incoherent Ramsey signature, or record a supported negative/unsupported conclusion for r03 under the current Ramsey protocol.
