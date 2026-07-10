# Ramsey review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- New bridge metadata: `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Prior comparison context: `evidence/e003.json` for the previous det=1.0 MHz, 0..8 us Ramsey terminal review, and `evidence/e017.md` for the short-tau diagnostic design/start note.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Parsed Ramsey readout roles from project context as readout 1 = reference and readout 2 = Ramsey signal for `full_experiment=0`.
- Checked acquisition integrity, raw signal/reference/ratio traces, per-point SEM across 12 stored averages, snake-order common-mode drift, target least-squares sinusoids, a frequency screen, FFT amplitudes, and fixed-frequency phase coherence across stored averages.
- Measurement facts: completed `auto__ramsey`, no stop request or monitor error in available metadata, final counts `35.122 kcps`, tau `0.048..1.968 us` in 41 points with `48 ns` step, `det=1.0 MHz`, `mw_freq=3.8759 GHz`, `12 x 90000 = 1.08e6` shots per tau point.
- Data quality checks: no stored averages exceeded the 15% common-mode drop flag; median SEM was `1.14 kcps` for signal and `0.0127` for signal/reference ratio.
- Target checks in signal/reference ratio:
  - Programmed carrier `1.0 MHz`: LS amplitude `0.0274` ratio, raw-signal amplitude `1.28 kcps`, R2 improvement `0.355` in ratio.
  - Expected 13C sidebands from the prior model, `0.615 MHz` and `1.385 MHz`: comparable ratio amplitudes `0.0243` and `0.0271`, not selectively dominant.
  - Prior scout component `0.884 MHz`: weaker, ratio amplitude `0.0126`, R2 improvement `0.071`.
  - Largest combined frequency-screen component: near `1.192 MHz`, ratio amplitude `0.0363`, raw-signal amplitude about `1.68 kcps`, ratio R2 improvement `0.656`.
- The FFT bin spacing is coarse for sideband assignment over this short span: about `0.508 MHz`; nearest ratio FFT bins were `1.016 MHz` and `1.524 MHz` for the carrier/high-sideband region.
- Per-average frequency screens were not uniquely locked to one frequency; top ratio frequencies included several near `1.13..1.29 MHz`, several at the low-frequency search boundary `0.4 MHz`, and one near `2.10 MHz`. At fixed frequency, phase coherence was high for the combined top component (`R=0.967` at `1.192 MHz`) and also high at the programmed carrier (`R=0.948`), so the combined oscillation is not just a single-average outlier.

## Plausible interpretation

- The short-tau/high-SNR run gives the strongest evidence so far for a weak early-time Ramsey-like oscillation on r03. It appears in raw signal, signal/reference, and signal/reference-line views, with no hard run anomaly and no scan-order drift flag.
- The dominant component is closer to `1.19 MHz` than to the programmed `1.0 MHz`. This could reflect a resonance/frequency offset since the fine pODMR calibration was earlier, or it could be a short-window/baseline artifact. The present files do not distinguish those.
- The result weakens the hypothesis that prior non-claim-grade Ramsey traces were caused only by an oscillation fully dying before about `2 us`, because a coherent weak oscillation is still visible across this short window. It still does not provide a stable decay envelope.
- The short window was designed as an early-time diagnostic, not as a high-resolution 13C spectroscopy run. Comparable carrier/sideband LS amplitudes and coarse FFT bins make 13C assignment unsafe.

## Claims not yet supported

- No numeric T2star is supported from this run. A decay fit would be model-driven rather than data-constrained.
- No nearby 13C conclusion or coupling assignment is supported.
- The `1.192 MHz` component should not yet be claimed as the true Ramsey carrier, a 13C sideband, or a protocol artifact.
- The prior `0.884 MHz` scout feature is not promoted by this dataset.
- r03 remains an aligned NV candidate from prior pODMR evidence, but the Ramsey/T2star/13C branch is still not closed with a supported final value.

## Recommended next action

Do not run another blind Ramsey repeat. First do a fresh weak-pi pODMR/frequency check on r03, or an equivalent detuning diagnostic, to test whether the apparent `~0.19 MHz` offset from the programmed `1.0 MHz` carrier is explainable by resonance drift or detuning. If the frequency check supports a shifted center, update `mw_freq` and run a longer, properly sampled Ramsey for T2star/13C. If it does not, treat the `1.19 MHz` feature as unresolved and move to an alternate T2/13C protocol or close the r03 Ramsey claim as unsupported under current conditions.
