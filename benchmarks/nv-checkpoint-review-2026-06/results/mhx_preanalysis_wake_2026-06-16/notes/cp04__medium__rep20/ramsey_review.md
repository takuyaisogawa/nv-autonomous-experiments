# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data/metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: executed job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control.
- Prior comparison:
  - `evidence/e008.json`: terminal det=1.0 MHz short-tau review.
  - `evidence/e019.json`, `evidence/e021.json`: det-shift model plan and success criteria.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Wrote `ramsey_detshift_analysis.json` and `ramsey_detshift_plot.png`.
- Checked raw export axis contract: `ExperimentDataEachAvg` shape `[1,12,2,41]`; averaging the per-average axis reproduces `ExperimentData` with max absolute error `1.4e-14`.
- Confirmed acquisition settings from job/result metadata: `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 0.048..1.968 us` in 41 points, 12 averages x 90000 repetitions, final counts `44.796 kcps`.
- Computed raw reference/signal, signal/reference ratio, signal divided by fitted reference line, point SEM from stored averages, FFT screens, and baseline-plus-sinusoid least-squares screens from 0.2 to 4.0 MHz.
- Compared the new frequency screens against the previous det=1.0 MHz short-tau component near `1.192 MHz`, the expected det-tracked component near `1.692 MHz`, programmed `1.5 MHz`, and planned 13C sideband targets.

## Quantitative checks

- Sampling: tau step `48 ns`, span `1.92 us`, nominal frequency resolution `0.521 MHz`, FFT bin spacing `0.508 MHz`, Nyquist `10.42 MHz`.
- Noise/variation: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`. Raw signal mean `44.27 kcps`; reference mean `48.08 kcps`.
- Per-average means show common-mode count variation but not a hard collapse: signal min/max mean ratio `0.845`, reference `0.881`, ratio `0.933`.
- Prior fixed component check: the previous `1.192 MHz` target is weak in the new run: ratio amplitude `0.0051`, raw-signal amplitude `0.474 kcps`, low R2 improvement.
- Det-tracking target check: `1.692 MHz` has ratio amplitude `0.0250`, raw-signal amplitude `1.225 kcps`, signal/reference-line amplitude `0.0255`; all three views give moderate baseline-fit improvement. After skipping tau <= 0.2 us, the target remains visible but weaker.
- Screen maxima are not fully consistent:
  - Ratio LS screen top: about `1.624 MHz`, amplitude `0.0255`, observed shift from prior top `+0.432 MHz` versus expected `+0.500 MHz`.
  - Raw signal and signal/reference-line LS screens top: about `0.882 MHz`, not the det-tracked carrier.
  - FFT is coarse and not decisive; largest ratio FFT bin is `0.508 MHz`, with nearby bins at `1.524` and `2.033 MHz`.
- 13C sideband checks are weak. The det-tracked sideband targets near `1.307` and `2.077 MHz` have small amplitudes and low R2 improvement, and do not form a robust sideband pattern.

## Plausible interpretation

The det=1.5 MHz run argues against a fixed `~1.192 MHz` artifact being the whole story: that component is strongly suppressed, and a feature near the expected det-shifted region appears in the ratio and reference-line-corrected checks. However, the evidence is still not clean enough to promote a quantitative Ramsey carrier, because the raw-signal screen prefers a different `~0.88 MHz` component and the frequency resolution is coarse over the 1.92 us span.

The most plausible current interpretation is a weak det-dependent Ramsey-like contribution mixed with baseline/transient structure. This is useful diagnostic evidence, but not yet a claim-grade T2star or 13C result.

## Claims not yet supported

- No well-supported numeric T2star from this run.
- No well-supported nearby 13C claim.
- No claim that the true Ramsey carrier is exactly `1.624 MHz`, `1.692 MHz`, or `1.5 MHz`.
- No claim that the `~0.88 MHz` raw-signal component is physical.
- No claim of a resolved carrier-plus-13C-sideband model.

## Recommended next action

Do not run another same-condition blind Ramsey repeat. Use this result as a det-shift diagnostic: the fixed `1.192 MHz` hypothesis is weakened, but the carrier model is not yet clean. The next bridge action should be a non-blind carrier-confirmation measurement, preferably another short-tau/high-SNR det-shift point such as `det = 2.0 MHz` on the same grid/shot budget, with the explicit prediction that the det-dependent component should move by another `+0.5 MHz`. If that also tracks across raw signal, ratio, and reference-line views, then design the T2star extraction scan around the confirmed carrier; if it does not, switch to an alternate protocol rather than more Ramsey repeats.
