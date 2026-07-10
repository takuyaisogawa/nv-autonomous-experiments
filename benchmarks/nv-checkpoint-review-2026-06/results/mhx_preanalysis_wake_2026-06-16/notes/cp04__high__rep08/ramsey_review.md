# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`.
- New completed Ramsey run: `measurement/m001.json` raw savedexperiment export, plus `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Prior/model context: `evidence/e008.json` prior det=1.0 MHz short-tau terminal review, `evidence/e019.json` det-shift model plan, and `evidence/e009.py` as the local review-style reference.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs: `ramsey_detshift_analysis.json` and `ramsey_detshift_analysis.png`.
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract by averaging per-average readouts back to combined `ExperimentData`.
  - Computed raw reference/signal, point-wise `signal/reference`, and `signal / fitted-reference-line` views.
  - Computed per-point SEM across 12 stored averages.
  - Ran least-squares sinusoid screens from 0.25 to 2.35 MHz, targeted LS checks, FFT-bin checks, per-average frequency screens, a descriptive damped-sinusoid grid fit, and a Python robust per-average drift proxy.

## Quantitative summary

- Run completed without a local hard anomaly: status `completed`, final count `44.796 kcps`, monitor `last_error` empty, `stop_requested=false`.
- Acquisition: `tau = 48 ns..1.968 us`, 41 points, 48 ns step, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, `12 x 90000` shots = `1.08e6` shots per tau point.
- Sampling: nominal resolution `0.521 MHz`, FFT bin spacing `0.508 MHz`, Nyquist `10.42 MHz`.
- Noise/variation: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`. Signal linear-residual peak-to-peak was `6.29 kcps`; ratio residual peak-to-peak was `0.133`. The first `0.75 us` still had a large transient: signal peak-to-peak `6.46 kcps`, ratio peak-to-peak `0.134`.
- Det-shift targets:
  - Prior det=1.0 MHz short-tau top component: `1.192 MHz`, ratio LS amplitude `0.0363`.
  - New all-tau ratio screen top: `1.623 MHz`, ratio LS amplitude `0.0255`.
  - Predicted det-tracked carrier: `1.692 MHz`, ratio LS amplitude `0.0250`.
  - Programmed `1.5 MHz` carrier: ratio LS amplitude `0.0240`.
  - Fixed artifact-control `1.192 MHz`: ratio LS amplitude only `0.0051`.
- Readout-view disagreement:
  - Raw signal and `signal / fitted-reference-line` screens are dominated near `0.882 MHz`, not near the ratio-view `1.623 MHz` component.
  - Skipping `tau <= 0.2 us` moves the ratio-screen top to about `0.746 MHz`.
  - Per-average top frequencies are inconsistent; only some averages prefer the `~1.5-1.7 MHz` region.
- 13C target checks:
  - Programmed sidebands `1.115/1.885 MHz` have ratio amplitudes `0.0108/0.0173`.
  - Det-tracked sidebands `1.307/2.077 MHz` have ratio amplitudes `0.0095/0.0061`.
  - These are not dominant or consistent across views.

## Plausible interpretation

The new det=1.5 MHz run is terminal and analyzable. The point-wise ratio view no longer supports a fixed `~1.192 MHz` artifact as the dominant all-tau component; it shows a component near `1.623 MHz`, close to the predicted det-tracked `~1.692 MHz` expectation and near the programmed `1.5 MHz` carrier.

However, the evidence is not claim-grade. The raw signal and fitted-reference-normalized views are dominated near `0.882 MHz`, the frequency screen changes when early tau points are removed, and per-average frequency preferences are scattered. This makes the apparent det-tracking feature plausibly a mixture of real Ramsey response, early-time transient, reference/baseline effects, and short-window model degeneracy rather than a clean physical carrier.

## Claims not yet supported

- A numeric T2star for r03 is not supported. The descriptive damped-sinusoid fit returned model-dependent values and should not be promoted.
- A nearby 13C coupling conclusion is not supported. Neither programmed nor det-tracked sidebands are independently dominant or consistent across raw/readout-aware views.
- The new run does not prove the prior `~1.192 MHz` feature was a clean physical Ramsey carrier; it only argues against a simple fixed-frequency artifact in the ratio view.
- A negative physical conclusion about the NV itself is not yet supported; the unsupported result is specific to the current Ramsey/readout conditions and analysis evidence.

## Recommended next action

Do a bridge-free synthesis across all Ramsey datasets, then stop blind Ramsey repeats. If the project continues experimentally, switch to a more discriminating protocol or measurement design that suppresses the early-time/reference transient before attempting another T2star or 13C claim. If no alternate protocol is justified, close this r03 Ramsey/13C branch as unsupported under the current conditions while retaining the aligned-NV conclusion.
