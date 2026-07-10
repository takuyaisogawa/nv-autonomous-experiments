# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- New terminal det-shift Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job/spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison point: `evidence/e008.json`, the terminal det=1.0 MHz short-tau Ramsey review with top empirical ratio component near 1.192 MHz.
- Local analysis artifacts created: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw export contract: `ExperimentDataEachAvg` averages back to `ExperimentData`; readout 1 is reference and readout 2 is Ramsey signal for `ramsey.xml` with `full_experiment=0`.
- Checked run health: completed, `12 x 90000` repetitions, `1.08e6` shots/tau point, final counts `44.796 kcps`, no stop request, safe shutdown OK.
- Tau grid: `0.048..1.968 us`, 41 points, `48 ns` step; FFT bin spacing about `0.508 MHz`, Nyquist about `10.42 MHz`.
- Local scan-order drift check using exported snake order found no flagged averages; maximum common-mode drop score was `0.040`.
- Noise/structure checks: median signal SEM `0.71 kcps`, median ratio SEM `0.0126`; early `tau <= 0.75 us` peak-to-peak was `6.46 kcps` in signal and `0.134` in ratio.
- Frequency screens:
  - Prior det=1.0 MHz short-tau top from context: `1.192 MHz`; det-tracking prediction after changing det to 1.5 MHz: `1.692 MHz`.
  - New all-tau ratio LS screen top: `1.623 MHz`, ratio amplitude `0.02547`.
  - Programmed 1.5 MHz carrier: ratio amplitude `0.02399`; det-tracking 1.692 MHz target: `0.02505`; prior fixed 1.192 MHz target: `0.00511`.
  - Skipping `tau <= 0.2 us` changes the ratio-screen top to `0.746 MHz`.
  - Raw-signal and fitted-reference-line screens both top near `0.882 MHz`, not near the all-tau ratio-screen top.
  - Det-tracking 13C sideband targets at `1.307/2.077 MHz` are weak, with ratio amplitudes `0.00953/0.00614`; programmed-det sidebands at `1.115/1.885 MHz` are also not dominant.
- Descriptive damped-sinusoid grid fits preferred `0.678 MHz, T2* = 0.469 us` in ratio and `0.818 MHz, T2* = 0.717 us` in raw signal, but these are diagnostics only.

## Plausible interpretation

The new det=1.5 MHz run is terminal, healthy, and analyzable. It weakens the simple fixed-artifact interpretation of the prior `1.192 MHz` ratio feature because that exact component is suppressed in the new ratio view while components near the programmed/det-shifted range are larger.

It still does not support a clean Ramsey carrier model. The apparent shifted response is sensitive to analysis view and early-time masking: ratio all-tau favors `1.623 MHz`, raw/reference-line views favor about `0.882 MHz`, and per-average top frequencies are scattered. The safest interpretation is an unresolved short-tau transient or normalization-sensitive structure, not a claim-grade det-following Ramsey oscillation.

## Claims not yet supported

- A numeric T2* for r03.
- Nearby 13C coupling or resolved 13C sidebands.
- A physical Ramsey carrier specifically at `1.5 MHz`, `1.623 MHz`, or `1.692 MHz`.
- That the prior `1.192 MHz` feature is definitively physical or definitively an artifact; this run only rules out a simple stable fixed-frequency promotion.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Make a branch decision: either switch to an alternate/calibration protocol that directly tests Ramsey phase/detuning and early-time artifacts, or close the r03 Ramsey/T2*/13C branch as unsupported under the current protocol and conditions.
