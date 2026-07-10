# Ramsey Review: r03 det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`.
- New completed measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior comparison/context: `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review; `evidence/e019.json` / `evidence/e021.json` det-shift model and success criteria; `evidence/e023.json`, `evidence/e028.json`, `evidence/e029.json` launch/progress copies for the same det=1.5 MHz job.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`; outputs are `ramsey_detshift_analysis.json` and `ramsey_detshift_review.png`.
- Verified raw-export axis contract: `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; averaging readout 1 and readout 2 over averages reconstructs `ExperimentData`.
- Measurement parameters checked from local files: `auto__ramsey`, `tau = 0.048..1.968 us`, 41 points, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, 12 averages x 90000 repetitions, final counts `44.796 kcps`.
- Drift/common-mode check: no averages exceeded a 15% common-mode drop threshold; largest negative common-mode deviation was about `-9.45%`.
- Noise and sampling checks: median point SEM was `0.711 kcps` raw signal and `0.0126` in signal/reference ratio; FFT bin spacing was `0.508 MHz`, so target discrimination relied mainly on least-squares frequency screens rather than raw FFT-bin labels.
- Target LS amplitudes in the ratio view:
  - Programmed carrier `1.500 MHz`: amplitude `0.0240`, R2 improvement `0.359`.
  - Det-tracking prediction from prior det=1.0 MHz top, `1.692 MHz`: amplitude `0.0250`, R2 improvement `0.411`.
  - Prior fixed component `1.192 MHz`: amplitude `0.0051`, R2 improvement `0.0167`.
  - Expected 13C sidebands using the project model, `1.115/1.885 MHz`: amplitudes `0.0108` and `0.0173`.
- Exploratory screens:
  - All-tau screens are dominated by a low-frequency boundary term at `0.25 MHz`, consistent with slow curvature/transient rather than a clean Ramsey carrier.
  - Excluding near-DC by screening `0.75..2.4 MHz`, raw signal and signal/reference-line views prefer about `0.878 MHz`; ratio-only prefers about `0.856 MHz`.
  - Screening only `1.0..2.4 MHz`, ratio prefers about `1.616 MHz`, while raw/signal-reference views prefer about `1.626 MHz`.

## Plausible interpretation

The det=1.5 MHz diagnostic is terminal and analyzable, with no hard status, stop, or common-mode drift anomaly. It does reject the simplest fixed-artifact interpretation of the previous `~1.192 MHz` det=1.0 feature, because that exact component is weak in this run.

However, it also does not cleanly support the intended det-tracking Ramsey-carrier model. The strongest non-near-DC content is view-dependent: raw/readout-normalized views show a strong `~0.878 MHz` component, while ratio-only high-frequency screens show `~1.62 MHz`, near but not equal to the `1.692 MHz` det-tracking prediction and not cleanly centered on the programmed `1.500 MHz` carrier. The expected 13C sidebands are weaker and not dominant.

The most conservative interpretation is that r03 remains an aligned NV with analyzable Ramsey data, but under the current Ramsey conditions the oscillatory content is not yet a claim-grade physical carrier/sideband pattern. This run is useful because it constrains the prior `~1.19 MHz` feature, but it still does not justify extracting a supported T2star.

## Claims not yet supported

- A numeric T2star for r03.
- A nearby 13C coupling or resolved 13C sideband pattern.
- That the dominant Ramsey oscillation is the programmed `1.5 MHz` carrier.
- That the previous `~1.19 MHz` component cleanly det-tracked by `+0.5 MHz`.
- That the `~0.878 MHz` feature is a physical NV Ramsey frequency rather than protocol/readout/transient structure.

## Recommended next action

Stop blind Ramsey repeats on r03. Do a branch-level synthesis of all four r03 Ramsey datasets and either close the r03 Ramsey/13C conclusion as unsupported under current conditions or switch to an alternate protocol/frequency-control diagnostic with explicit success criteria. A reasonable next experimental direction is a non-Ramsey baseline such as Hahn/CPMG-style coherence or a deliberate sequence/readout diagnostic, not another same-grid Ramsey accumulation.
