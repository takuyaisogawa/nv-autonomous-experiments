# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior relevant evidence: `evidence/e003.json` (terminal det=1.0 MHz, 8 us Ramsey review), `evidence/e006.json` and `evidence/e009.json` (short-tau model/advisory and intent), `evidence/e017.md` (short-tau design/start note).
- New terminal measurement bundle:
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350`.
  - `measurement/m002.json`: bridge job spec for `nv23_ramsey_20260513_230331_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: terminal control state.

## Calculations/scripts run

- Added and ran `analyze_shorttau_ramsey.py`.
- Script outputs:
  - `ramsey_analysis_results.json`: parsed raw arrays, readout statistics, target least-squares fits, FFT screen, bootstrap over stored averages, per-average frequency screen, and simple snake-order drift summary.
  - `ramsey_shorttau_diagnostic.png`: raw/readout and FFT diagnostic plot.
- Data shape and acquisition:
  - Combined readouts: `[1, 2, 41]`; per-average readouts: `[1, 12, 2, 41]`.
  - Tau range `0.048..1.968 us`, step `48 ns`, 41 points, span `1.92 us`.
  - `12 x 90000 = 1.08e6` shots per tau point.
  - FFT bin spacing about `0.508 MHz`; nominal `1/span` resolution about `0.521 MHz`; Nyquist about `10.42 MHz`.
- Completion/safety checks:
  - Job completed, no stop request, monitor `last_error` empty.
  - Final count text/result `35.122 kcps`, above the stated `20 kcps` gate but lower than the previous `44.184 kcps` terminal count.
- Raw/readout checks:
  - Reference mean `48.573 kcps`, reference std over tau `0.456 kcps`.
  - Signal mean `44.655 kcps`, signal std over tau `1.574 kcps`.
  - Median signal SEM across stored averages `1.138 kcps`; median ratio SEM `0.0127`.
  - Signal peak-to-peak over full trace `6.50 kcps`; first `0.75 us` peak-to-peak `5.69 kcps`.
  - Ratio peak-to-peak over full trace `0.143`; first `0.75 us` peak-to-peak `0.111`.
- Target harmonic fits after linear baseline:
  - Programmed `1.0 MHz` carrier: ratio amplitude `0.0274`, raw-signal amplitude `1.28 kcps`, residual R2 improvement `0.355`; bootstrap raw amplitude CI `[0.99, 1.58] kcps`.
  - Expected low 13C sideband `0.615 MHz`: ratio amplitude `0.0243`, raw amplitude `1.10 kcps`.
  - Expected high 13C sideband `1.385 MHz`: ratio amplitude `0.0271`, raw amplitude `1.22 kcps`.
  - Prior det=1.0 MHz 8 us exploratory component `1.178 MHz`: ratio amplitude `0.0362`, raw amplitude `1.68 kcps`, residual R2 improvement `0.654`; bootstrap raw amplitude CI `[1.34, 2.05] kcps`.
- Exploratory screens:
  - Strongest combined ratio LS component near `1.192 MHz`; strongest raw-signal LS component near `1.187 MHz`.
  - Detrended ratio FFT largest bins: `1.524 MHz`, `1.016 MHz`, `0.508 MHz`.
  - Per-average LS top frequencies are not stable: several averages prefer the low search boundary near `0.2 MHz`, several prefer `~1.13..1.29 MHz`, and one prefers `2.103 MHz`.
- Simple scan-order drift/provenance check:
  - Stored-average signal means range `37.47..51.21 kcps`; reference means range `42.02..55.19 kcps`, indicating sizable common-mode run-to-run variation.
  - Largest acquisition-order linear span appears in average 7: signal `6.90 kcps`, reference `4.21 kcps`, both about `3.5 x` their residual scatter. This is drift/baseline provenance rather than a hard abort flag.

## Plausible interpretation

- The short-tau/high-SNR run is analyzable and did what it was designed to do: it avoids tau=0, improves the per-point SEM to about `1.14 kcps`, and concentrates sampling over the first `1.92 us`.
- Unlike the prior long-window runs, the combined short-tau trace shows visible early-time structure above the per-point SEM. This partly weakens the hypothesis that there is simply no Ramsey-scale signal on r03 under current conditions.
- The structure is not yet claim-grade Ramsey/T2star evidence. The strongest combined LS component is near `1.19 MHz`, not exactly the programmed `1.0 MHz` carrier. The `1.0 MHz` carrier projection is present but weaker, and the short `1.92 us` span makes `0.615`, `1.0`, `1.178`, and `1.385 MHz` assignments highly correlated.
- Per-average frequency screens and common-mode count variation argue for caution: the combined trace is better than any single average as a diagnostic, but average-to-average stability is not strong enough to promote a physical frequency or fitted decay.
- The result is compatible with an early-time Ramsey-like oscillatory structure plus drift/baseline/systematic effects. It is not enough to identify a 13C sideband or extract a robust T2star envelope.

## Claims not yet supported

- No numeric T2star value is supported from this run.
- No nearby 13C presence, absence, coupling, or sideband assignment is supported.
- The `~1.19 MHz` exploratory component should not be claimed as a physical transition or coupling frequency yet.
- The programmed `1.0 MHz` carrier is not cleanly established as the dominant Ramsey component.
- The run does not prove that r03 lacks Ramsey signal; it only shows that the current Ramsey evidence remains model-ambiguous.

## Recommended next action

Do not run another blind long-window Ramsey repeat or fit T2star from this trace. If continuing the r03 Ramsey branch, run one targeted short-tau det-shift control with the same tau grid/readout strategy and comparable shot budget, changing only `det` away from `1.0 MHz` (for example to `1.5 MHz`). The decision criterion should be simple: if the `~1.19 MHz` structure moves with programmed det, then design a follow-up for T2star extraction; if it does not move, treat the r03 Ramsey/13C branch as unsupported under current conditions and switch to an alternate protocol or close the branch without T2star/13C claims.
