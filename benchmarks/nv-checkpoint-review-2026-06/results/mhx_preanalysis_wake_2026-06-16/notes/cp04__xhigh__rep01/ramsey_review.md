# Ramsey Review

## Files/Data Used

- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: submitted det-shift Ramsey job spec.
- `measurement/m003.json`: terminal bridge result; run completed with final counts `44.796 kcps`.
- `measurement/m004.json` and `measurement/m005.json`: terminal status/control; no monitor error and no stop request.
- `project/state.md` and `context.json`: project history and prior Ramsey interpretation.
- `evidence/e008.json`: prior det=1.0 MHz short-tau terminal review.
- `evidence/e019.json`: det=1.5 MHz shift-check model/advisory and target frequencies.

## Calculations/Scripts Run

- Created and ran `review_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_review.json`
  - `ramsey_detshift_review.png`
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract by reconstructing combined `ExperimentData`; contract is `[scan, avg, readout, point]`.
  - Confirmed tau grid: `48 ns..1.968 us`, 41 points, `48 ns` step; 12 averages x 90000 repetitions = `1.08e6` shots per tau point.
  - Used readout 1 as reference and readout 2 as Ramsey signal, consistent with project context for `ramsey.xml` with `full_experiment=0`.
  - Computed raw signal, signal/reference ratio, and signal/fitted-reference-line views.
  - Computed per-point SEM: median raw-signal SEM `0.711 kcps`; median ratio SEM `0.01262`.
  - Ran local scan-order-aware drift proxy using `ScanOrderInfo.order_each_avg`; no averages flagged.
  - Ran FFT and least-squares sinusoid screens over `0.25..2.25 MHz`, plus target checks at:
    - programmed carrier `1.500 MHz`
    - programmed 13C sidebands `1.115/1.885 MHz`
    - predicted det-tracking carrier `1.692 MHz`
    - predicted det-tracking sidebands `1.307/2.077 MHz`
    - prior artifact/control component `1.192 MHz`
  - Ran descriptive damped-sinusoid grid fits for diagnostic use only.

## Plausible Interpretation

- The run is terminal and analyzable: bridge state `completed`, final counts `44.796 kcps`, no stop request, no monitor error, and no drift flags from the local scan-order-aware proxy.
- The previous det=1.0 MHz short-tau run had its combined-ratio LS maximum near `1.192 MHz`. In this det=1.5 MHz run, the old `1.192 MHz` ratio amplitude is strongly suppressed (`0.00511`), while the combined-ratio LS maximum moves upward to `1.623 MHz` with amplitude `0.02547`.
- This upward movement is qualitatively more compatible with a det-dependent Ramsey structure than with a perfectly fixed `1.192 MHz` artifact.
- It is still not claim-grade. The short span gives only about `0.52 MHz` nominal frequency resolution, so `1.500`, `1.623`, and `1.692 MHz` are not cleanly separated. Raw-signal and signal/fitted-reference-line screens prefer about `0.882 MHz`, not the combined-ratio maximum. Per-average ratio screens are inconsistent.
- Target amplitudes are close to the measured uncertainty scale: programmed `1.5 MHz` carrier amplitude is `0.02399` ratio / `1.128 kcps`; det-tracking `1.692 MHz` amplitude is `0.02505` ratio / `1.225 kcps`.
- 13C sideband support is weak: programmed sidebands have ratio amplitudes `0.01076` and `0.01732`; det-tracking sidebands have `0.00953` and `0.00614`. None is dominant or consistent enough for a nearby-13C claim.

## Claims Not Yet Supported

- No numeric `T2star` is supported from this run.
- No nearby `13C` coupling/sideband conclusion is supported.
- The `1.623 MHz` combined-ratio feature should not be promoted as a precise Ramsey carrier.
- The old `1.192 MHz` feature is not supported as a fixed artifact by this run, but its physical origin is still not established.
- The descriptive damped fits are not physical results; they are sensitive to transient/baseline behavior and conflicting readout views.

## Recommended Next Action

Do not run another blind Ramsey repeat. Do a bridge-free synthesis of all r03 Ramsey runs, then either switch to an alternate coherence/sequence diagnostic or close the r03 Ramsey `T2star`/`13C` branch as unsupported under current Ramsey conditions.
