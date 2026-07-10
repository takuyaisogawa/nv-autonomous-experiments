# Ramsey review

## Files/data used

- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`, `measurement/m003.json`: submitted Ramsey job/spec metadata.
- `measurement/m004.json`, `measurement/m005.json`: terminal status and run control for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- `project/brief.md`, `project/state.md`, `project/advice.md`: objective and prior project interpretation.
- `md/memory.md`, `md/knowledge.md`: local NV analysis/readout guidance.
- `evidence/e006.md` through `evidence/e013.md`: fine-pODMR review, second-Ramsey model/advisory, validation/advisory/job/result/status context.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- Checks performed:
  - Parsed raw combined readouts and `ExperimentDataEachAvg`.
  - Built tau axis `0..8 us`, 41 points, `dt = 0.2 us`.
  - Checked raw signal/reference traces, point-wise `signal/reference`, and reference-line normalization.
  - Checked average-to-average count motion and snake-order provenance.
  - Ran detrended FFT on the raw signal readout.
  - Ran targeted least-squares sinusoid screens at the planned frequencies: prior `0.884 MHz`, expected lower 13C sideband `0.615 MHz`, carrier `1.000 MHz`, and expected upper 13C sideband `1.385 MHz`.
  - Tried a raw-signal Gaussian-decay Ramsey fit only as a diagnostic; not used as a supported T2star result.

Key numerical results:

- Run completed safely with final counts `44.184 kcps`, `8 x 50000` repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Combined readout means: reference `49.31 kcps`, signal `44.58 kcps`.
- Raw signal peak-to-peak over tau is `7.72 kcps` (`17.3%` of mean), but much of the stored-average motion is common-mode: signal average means span `31.6%`, reference means span `30.5%`.
- Signal/reference average means span only `3.86%`, so normalization removes a large common-mode component but does not make a clean target-frequency result.
- Detrended raw-signal FFT top bins are near `1.220 MHz`, `1.098 MHz`, `0.488 MHz`, `0.122 MHz`, and `0.610 MHz`; the nominal planned carrier bin at about `0.976 MHz` is weaker.
- Targeted raw-signal LS amplitudes:
  - `1.000 MHz` carrier: `0.553 kcps` peak-to-peak, `1.24%` of mean signal, phase coherence across averages `0.55`.
  - `0.615 MHz` lower 13C sideband: `0.951 kcps` peak-to-peak, `2.13%`, phase coherence `0.73`.
  - `1.385 MHz` upper 13C sideband: `0.525 kcps` peak-to-peak, `1.18%`, phase coherence `0.37`.
  - prior `0.884 MHz` component: `0.572 kcps` peak-to-peak, `1.28%`, phase coherence `0.46`.
- Point-wise ratio LS checks remain small: about `2.03%` peak-to-peak at `1.000 MHz`, `2.44%` at `0.615 MHz`, `1.87%` at `1.385 MHz`, and `1.64%` at `0.884 MHz`.
- Diagnostic decay fit returned `T2star = 0.246 us`, `freq = 0.962 MHz`, `R2 = 0.53`, but with uncertainties larger than the fitted values (`T2star stderr = 1.04 us`, frequency stderr `4.06 MHz`, amplitude stderr `30.8 kcps`). This fit is not interpretable.

## Plausible interpretation

The measurement is usable as a diagnostic run, but it still does not support a claim-grade Ramsey carrier, T2star, or 13C conclusion. The expected `1.0 MHz` carrier is not a dominant, coherent feature in raw or normalized views. The possible sideband-region features are weak and average-dependent; the lower-sideband screen at `0.615 MHz` is the largest targeted LS component, but it is still only about `2%` peak-to-peak and sits amid comparable nearby FFT structure.

The det-shift diagnostic also weakens the idea that the first scout's `~0.884 MHz` component was a stable physical Ramsey carrier or 13C feature: in this run the `0.884 MHz` targeted component is small and poorly coherent. The new run instead shows weak structure around `1.1-1.2 MHz` and `0.5-0.6 MHz`, but the evidence is not clean enough to assign those to the programmed carrier or 13C sidebands.

Large stored-average common-mode count changes are present even though the final count is healthy. Ratio normalization cancels much of that motion, so the run is not simply invalid, but the remaining oscillatory evidence is too weak and inconsistent for parameter extraction.

## Claims not yet supported

- No supported numeric T2star value.
- No supported 13C coupling/nearby-13C conclusion.
- No supported claim that the Ramsey carrier follows the programmed `det = 1.0 MHz`.
- No supported claim that the `0.615 MHz` or `1.385 MHz` features are 13C sidebands.
- No supported claim that the prior `~0.884 MHz` component is physical.
- No supported use of the diagnostic decay fit; it is underconstrained and uncertainty-dominated.

## Recommended next action

Do not run another long Ramsey accumulation blindly. First run a focused Ramsey phase/carrier diagnostic on the same r03 branch after fresh tracking and, if needed, a quick weak-pi pODMR frequency check: shorter tau span, denser sampling, and one or two deliberate det values chosen to verify that the observed oscillation follows the programmed phase ramp. If the carrier still does not appear coherently, inspect or switch the Ramsey route/readout/phase-control path before spending more shots on T2star/13C. Only fit T2star after a raw/readout-aware carrier is clearly present and average-consistent.
