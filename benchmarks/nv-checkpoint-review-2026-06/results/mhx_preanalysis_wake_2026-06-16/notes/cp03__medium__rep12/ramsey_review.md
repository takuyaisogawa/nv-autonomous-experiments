# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- Prior Ramsey context: `evidence/e003.json` terminal review of the det=1.0 MHz 8 us Ramsey, `evidence/e006.json` short-tau/high-SNR plan, `evidence/e017.md` design/start note.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` run status, `measurement/m005.json` control state.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_shorttau_review.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py` to parse the raw export, reconstruct tau/readout arrays, compute signal/reference and signal/linear-reference traces, estimate per-point scatter from 12 stored averages, screen least-squares sinusoid components, generate a detrended Hann FFT view, and write `ramsey_analysis_summary.json` plus `ramsey_shorttau_review.png`.
- Key acquisition facts from the export/result: `tau = 48 ns..1.968 us` in 41 points, 48 ns step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000 = 1.08e6` shots per tau point, snake scan order, final counts `35.122 kcps`, no stop request or bridge error.
- Readout summary: reference mean `48.57 kcps`, signal mean `44.65 kcps`, ratio mean `0.9195`; stored median signal error `1.40 kcps`, empirical median ratio SEM `0.0127`; simple average-level drift check flagged no averages.
- Frequency checks:
  - Programmed 1.0 MHz carrier: ratio LS amplitude `0.0274`, raw-signal LS amplitude `1.28 kcps`, R2 improvement vs linear baseline `0.355` ratio / `0.377` raw.
  - Best combined ratio LS screen: near `1.192 MHz`, amplitude `0.0363`, R2 improvement `0.656`.
  - FFT is coarse because the span is only `1.92 us`: bin spacing `0.508 MHz`, nominal `1/span = 0.521 MHz`. Top ratio FFT bins were `1.524 MHz`, `1.016 MHz`, and `0.508 MHz`.
  - Expected 13C sideband targets from the prior model are near `0.615 MHz` and `1.385 MHz`; these are not resolvable cleanly from the carrier in this short window.
- Bounded scratch decay fits were not stable enough for a T2* claim. A free-frequency ratio fit landed near `1.198 MHz` with `T2* ~6.3 us`, but the T2* uncertainty was larger than the estimate; a fixed 1.0 MHz fit collapsed to a short-time/high-amplitude edge solution.

## Plausible interpretation

- The short-tau/high-SNR diagnostic did what it was designed to test: unlike the prior 8 us run, this dataset shows a plausible early-time Ramsey oscillation component near the intended 1 MHz carrier scale.
- The best empirical component is shifted high, around `1.19 MHz`, but the short span gives poor frequency discrimination. Treat the difference between `1.0 MHz` and `1.19 MHz` as suggestive rather than a resolved detuning error.
- The measurement supports "there is likely an early-time Ramsey-like signal on r03 under this short-tau protocol." It does not yet support a durable quantitative model.

## Claims not yet supported

- Do not claim a numeric T2*. The decay envelope is not constrained by a 1.92 us window with only about two carrier cycles, and bounded fits are model-sensitive.
- Do not claim nearby 13C coupling. The expected sidebands are separated from the carrier by about `0.385 MHz`, below the `~0.52 MHz` resolution of this diagnostic, and the FFT/LS screens do not isolate them.
- Do not claim the Ramsey frequency is exactly `1.192 MHz`; that value is a short-window screen maximum, not a high-resolution estimate.
- Do not use this result to revise the accepted pODMR center by itself.

## Recommended next action

Run one targeted confirmation Ramsey on r03, not another blind repeat: keep the short-tau start after zero, extend the span enough to improve frequency/T2* discrimination while preserving early-time SNR, and choose tau spacing/shot budget to resolve a 1 MHz carrier and potential +/-13C sidebands. A practical next design is a mid-window confirmation such as roughly `48 ns..4-5 us` with high shots and even averages, followed by the same raw/readout-aware review. If that confirms a carrier and gives a stable envelope, then fit T2*; only after that use a longer/high-resolution measurement for 13C.
