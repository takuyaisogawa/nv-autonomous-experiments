# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey terminal data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` run status, `measurement/m005.json` run control.
- Relevant prior context from evidence/project state: accepted r03, fine weak-pi pODMR grid center `mw_freq = 3.8759 GHz`, expected Ramsey carrier `1.0 MHz`, expected 13C sidebands near `0.615/1.385 MHz`, prior non-claim-grade Ramsey component near `0.884 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Script output artifacts:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- Checks performed:
  - Parsed raw Ramsey data shape: combined `ExperimentData = [1, 2, 41]`; per-average `ExperimentDataEachAvg = [1, 8, 2, 41]`.
  - Confirmed scan: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, 8 averages, 50000 repetitions, snake order.
  - Treated readout 1 as reference and readout 2 as Ramsey signal, consistent with the project protocol inspection for `auto__ramsey` / `full_experiment=0`.
  - Computed raw signal, reference, signal/reference fractional Ramsey trace.
  - Ran linear-detrended FFT on the fractional signal/reference trace.
  - Ran least-squares sine/cosine component checks at `1.000 MHz`, `0.615 MHz`, `1.385 MHz`, and `0.884 MHz`.
  - Checked per-average signal/reference means, forward/reverse average means, per-average correlation with the combined detrended trace, and acquisition-order slopes.
  - Tried fixed-1 MHz and free-frequency Gaussian-decay Ramsey fits as descriptive checks only.

## Quantitative results

- Terminal run completed cleanly:
  - status `completed`
  - savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`
  - final counts `44.184 kcps`
  - no stop requested
  - safe shutdown reported OK
- Signal/reference fractional trace:
  - range `-11.3%` to `+7.4%`
  - standard deviation `3.25%`
  - robust residual scale after removing a 1 MHz component: about `2.6%`
- FFT, detrended signal/reference:
  - strongest bins: `1.098 MHz` amplitude `2.33%`, `1.220 MHz` amplitude `2.08%`, `0.976 MHz` amplitude `1.47%`
  - 13C lower-sideband bin near `0.610 MHz`: `0.84%`
  - upper-sideband nearest bin near `1.341 MHz`: `0.73%`
  - prior-component nearest bin near `0.854 MHz`: `0.73%`
- Least-squares target amplitudes on fractional signal/reference:
  - `1.000 MHz`: `1.01%`, residual RMS `3.12%`
  - `0.615 MHz`: `1.20%`, residual RMS `3.09%`
  - `1.385 MHz`: `0.93%`, residual RMS `3.13%`
  - `0.884 MHz`: `0.82%`, residual RMS `3.15%`
- Per-average checks:
  - signal mean by average varied substantially, about `36.2..50.3` in exported units, so there is real average-to-average brightness/baseline motion.
  - signal/reference mean by average was narrower, about `0.891..0.926`.
  - forward and reverse average mean ratios were close: `0.9018` vs `0.9077`.
  - detrended per-average correlations with the combined trace were positive but only moderate: about `0.32..0.65`.
- Descriptive fit checks:
  - fixed-1 MHz Gaussian-decay cosine gave `T2star ~0.47 us`, amplitude about `12%`, `R2 ~0.41`.
  - free-frequency fits from several initial frequencies converged near `0.956 MHz`, `T2star ~0.47 us`, `R2 ~0.41`; an alternate shallow solution near `1.21 MHz` gave similar but slightly worse `R2`.

## Plausible interpretation

- The det-shifted Ramsey contains a short-lived carrier-like feature near the programmed `1.0 MHz` detuning. This is more compatible with a real Ramsey response than the previous scout, because the strongest spectral content is now near `1.0..1.2 MHz` and the previous `~0.884 MHz` component is not prominent.
- The apparent decay is fast. A descriptive fit points to `T2star` on the order of `0.5 us`, but this is dominated by the first few tau points and is not yet a robust final value.
- The 13C sideband checks do not show a supported feature at the expected `0.615/1.385 MHz` positions. Those target amplitudes are small compared with residual scatter and are not per-average coherent enough to claim nearby 13C coupling.

## Claims not yet supported

- Do not claim a final, well-supported numeric `T2star` from this 0..8 us / 0.2 us grid alone.
- Do not claim a resolved 13C coupling or sideband.
- Do not claim a firm negative 13C conclusion yet; if `T2star` is truly around `0.5 us`, ordinary Ramsey FFT sideband resolution is intrinsically poor, so the method may be resolution-limited rather than proving absence.
- Do not claim that the previous `~0.884 MHz` feature was definitely an artifact. This run argues against it being the dominant reproducible carrier, but does not identify its origin.

## Recommended next action

Run one targeted short-time Ramsey confirmation on r03 before further long-span Ramsey repeats:

- keep `mw_freq = 3.8759 GHz` and a deliberate detuning near `1.0 MHz`;
- scan densely over the early decay, e.g. `tau = 0..2 us` or `0..3 us` with substantially finer spacing than `0.2 us`;
- keep even averages and per-average tracking, but reduce scan length/points if needed so the per-average tracking window stays under the active cap;
- analyze raw readout 2 and signal/reference together, then fit `T2star` only if the early-time oscillation and decay reproduce.

If that short-time repeat confirms `T2star ~0.5 us`, then treat the current Ramsey-FFT route as poorly suited for resolving weak `13C` sidebands on this NV and move to either a different 13C-sensitive sequence or a bounded no-resolved-13C conclusion for Ramsey.
