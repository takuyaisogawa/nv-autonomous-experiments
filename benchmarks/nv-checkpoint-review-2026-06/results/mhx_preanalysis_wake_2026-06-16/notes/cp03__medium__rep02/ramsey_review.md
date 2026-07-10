# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `context.json` for objective, accepted r03 status, prior Ramsey conclusions, and the required terminal-review posture.
- `measurement/m001.json`: terminal savedexperiment raw export for `nv23_ramsey_20260513_230331_auto_ramsey`.
- `measurement/m002.json`: submitted job/config metadata.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control provenance.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.txt`, and `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` and `ExperimentDataEachAvg` as 2 readout channels, 12 averages, 41 tau points.
- Confirmed scan settings: tau `48 ns..1968 ns` in `48 ns` steps, `90000` repetitions per average, programmed `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`.
- Computed raw signal/reference traces, pointwise signal/reference ratio, per-point SEM across averages, and a simple linear-reference-normalized signal.
- Ran least-squares sinusoid checks at the programmed carrier `1.000 MHz` and expected 13C sidebands `0.615 MHz` and `1.385 MHz`, with a linear baseline term.
- Ran exploratory least-squares frequency scans from `0.1..5.0 MHz`, including a restricted `>=0.4 MHz` view.
- Checked per-average mean drift in signal, reference, and ratio.

## Plausible interpretation

- The measurement completed cleanly: terminal status is `completed`, safety reports no abort, monitor error is empty, and no stop request was applied.
- The raw signal does not show a claim-grade 1 MHz Ramsey carrier. At `1.000 MHz`, raw-signal LS amplitude is only `0.213 kcps`, while the median raw-signal SEM across averages is `1.120 kcps`; the raw-signal target fit explains little variance (`R2 ~ 0.14`).
- The direct pointwise ratio has apparent target-frequency amplitudes (`~0.029..0.033` ratio units at 0.615/1.000/1.385 MHz), but this is not reliable evidence: the raw reference channel has much larger target-frequency amplitudes (`~1.10..1.28 kcps`, `~4.1..4.7 sigma` by the simple LS screen), and after linear reference normalization the target amplitudes drop to `0.0033..0.0047`, below the median ratio SEM (`0.0151`) and only `~1.5..2.0 sigma`.
- Exploratory frequency scans are dominated by low-frequency/baseline structure. In the `>=0.4 MHz` scan the largest components sit at the lower edge near `0.4 MHz`, not at the programmed carrier or 13C sidebands.
- Per-average means show substantial common-mode changes: signal span `26.8%`, reference span `30.8%`, while ratio span is smaller at `6.9%`. This supports treating ratio-only features as denominator/common-mode sensitive.
- Plausible conclusion: this short-tau/high-SNR diagnostic still does not establish a robust Ramsey carrier. It also does not support a nearby-13C sideband interpretation. The result is consistent with either absent/very weak Ramsey contrast under this protocol, reference/readout/systematic structure dominating the normalized signal, or a coherence/contrast problem not fixed by short-tau/high-SNR sampling.

## Claims that are not yet supported

- No supported numeric T2star for r03.
- No supported nearby 13C claim from the FFT/LS screens.
- No supported claim that the observed ratio oscillations are physical Ramsey contrast; they are not present with sufficient strength in raw signal or reference-line-normalized signal.
- No supported claim that another blind Ramsey repeat with the same basic settings will resolve the branch.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Escalate to an alternate diagnostic/protocol that directly tests whether the problem is Ramsey contrast/readout-systematic rather than tau-window/SNR: for example, a controlled phase/readout diagnostic or another protocol already accepted by the project rules for weak-13C/T2star discrimination. If hardware time must remain on r03, first design a short, bounded diagnostic with explicit acceptance criteria for raw-signal carrier visibility before any T2star or 13C fit.
