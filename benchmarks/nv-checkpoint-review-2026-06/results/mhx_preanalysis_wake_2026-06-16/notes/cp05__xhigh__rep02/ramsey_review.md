# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Ramsey design/model context: `evidence/e014.json`.
- New terminal measurement data: `measurement/m001.json` raw export, `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Local analysis artifacts created: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified run health: job `nv23_ramsey_20260514_055148_auto_ramsey` completed at `2026-05-14T09:28:25`, final counts `43.433 kcps`, `stop_requested=false`, monitor `last_error=""`, safe shutdown ok.
- Verified raw data contract: `ExperimentData` shape `[1,2,41]`, `ExperimentDataEachAvg` shape `[1,20,2,41]`, and the combined data equal the mean over stored averages. Readout1 was treated as reference and readout2 as Ramsey signal per `evidence/e014.json`.
- Scan/acquisition check: tau `48 ns..8.048 us`, 41 points, `0.2 us` step, `8.0 us` span, nominal resolution `125 kHz`, Nyquist `2.5 MHz`, `20 x 50000 = 1.0e6` shots per tau.
- Noise/provenance checks: reference mean `48.789 kcps`, signal mean `44.670 kcps`, median signal SEM `0.850 kcps`, median signal/reference SEM `0.0116`. Local snake-order in-average drift screen flagged `0/20` averages for a >15% common-mode drop. Cross-average brightness varied substantially (`ref 41.74..54.90 kcps`, `signal 37.38..50.37 kcps`), while ratio was steadier (`0.891..0.959`), so common-mode variation remains provenance.
- Target LS/FFT screens used carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, and prior controls `1.623`, `1.192`, `0.746 MHz`.
- Full-span LS amplitudes:
  - signal/reference top component: `2.270 MHz`, amplitude `0.01845`.
  - raw-signal top component: `2.270 MHz`, amplitude `0.818 kcps`.
  - programmed carrier `1.500 MHz`: ratio amplitude `0.01575`, raw amplitude `0.705 kcps`.
  - expected 13C sidebands: low `1.115 MHz` ratio amplitude `0.00278`, high `1.885 MHz` ratio amplitude `0.00962`.
  - prior `1.192 MHz` control stayed weak: ratio amplitude `0.00194`.
- Skip-first-4-tau screen still topped near `2.268 MHz`; the carrier ratio amplitude dropped to `0.01231`, and the sidebands remained weak/asymmetric.
- Bootstrap over the 20 stored averages showed target carrier amplitude is measurable but not a dominant stable frequency selector: median top frequency `2.265 MHz`, top in `2.1..2.35 MHz` for `69.0%` of resamples, and top in `1.2..1.8 MHz` for `29.4%`.

## Plausible interpretation

The Ramsey completed cleanly and returned analyzable data. The refreshed-center run does show a measurable component at the programmed `1.5 MHz` carrier, and the old `~1.192 MHz` artifact-control component is weak. However, both raw and normalized full-span screens are dominated by an unexplained high-frequency component near `2.27 MHz`, and this remains after skipping early tau points. Stored-average top frequencies are dispersed.

This is useful evidence against simply promoting the old fixed `~1.192 MHz` feature, but it still does not establish a clean Ramsey carrier/decay model. The `2.27 MHz` component should be treated as unexplained spectral/point-to-point structure unless a later protocol or control measurement supports it physically.

## Claims not yet supported

- No numeric T2star claim is supported from this run. A damped Ramsey fit would be fit-first rather than signal-presence-first because the programmed carrier is not the dominant robust component.
- No nearby 13C claim is supported. The expected `1.115/1.885 MHz` sidebands do not appear as a consistent pair around a stable carrier.
- Do not claim the `2.27 MHz` component as a physical transition, coupling, or alias without a targeted control.
- The prior alignment/pODMR conclusion for r03 remains project context, but this Ramsey does not add a T2star or 13C conclusion.

## Recommended next action

Do not run another blind Ramsey repeat on the same settings. Record this terminal Ramsey as non-claim-grade, then either close r03 as "no supported T2star/13C under the current Ramsey conditions" or design an alternate, explicitly modeled protocol/control that can test the unexplained `2.27 MHz` structure and the carrier/sideband model before any further bridge submission.
