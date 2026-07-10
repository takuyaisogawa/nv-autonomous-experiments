# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- New run metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior relevant context: `evidence/e017.md` and state pointers for the fine pODMR center and the two earlier non-claim-grade Ramsey runs.
- Generated local artifacts: `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python and inspected `ExperimentData`, `ExperimentDataEachAvg`, scan variables, stored-average order, and readout dimensions.
- Used readout 1 as reference and readout 2 as signal, consistent with the project convention for this Ramsey route.
- Built tau axis from saved scan metadata: `48 ns..1.968 us`, 41 points, `48 ns` step, Nyquist `10.42 MHz`, frequency resolution about `0.521 MHz`.
- Checked raw signal, point-wise signal/reference ratio, and signal normalized by a fitted reference line.
- Least-squares screened sin/cos components with offset and linear baseline terms at:
  - programmed carrier: `1.000 MHz`
  - expected nearby-13C sidebands from prior model: `0.615 MHz` and `1.385 MHz`
  - exploratory `0.2..8.0 MHz` frequency screen.
- Checked stored-average means and per-average frequency components for drift/common-mode behavior.
- Wrote plot `ramsey_review_plot.png` showing raw readouts, normalized views, and LS frequency screen.

## Quantitative checks

- Terminal run completed normally: `12 x 90000` repetitions, no abort, no stop request, final text count `35.122 kcps`, above the stated `20 kcps` gate but lower than earlier `44.184 kcps` provenance.
- Mean readouts: reference `48.57 kcps`, signal `44.65 kcps`.
- Median per-point SEM from export: signal `1.40 kcps`; detrended raw-signal point scatter `1.47 kcps`.
- Target LS amplitudes:
  - `1.000 MHz`: raw signal `1.28 kcps`, ratio `0.0274`, reference-line normalized `0.0264`.
  - `0.615 MHz`: raw signal `1.10 kcps`, ratio `0.0243`, line-normalized `0.0227`.
  - `1.385 MHz`: raw signal `1.22 kcps`, ratio `0.0271`, line-normalized `0.0251`.
- The strongest exploratory screen over `>=0.5 MHz` is broad around `1.20 MHz`, with ratio amplitude about `0.036`, not exactly the programmed `1.0 MHz` carrier or either expected sideband.
- The all-frequency screen is dominated by very-low-frequency baseline/common-mode structure near the lower bound (`0.2 MHz`), so low-frequency peaks are not interpreted as Ramsey physics.
- Stored-average signal means vary substantially (`37.47..51.21 kcps`) with an average-index trend about `-0.59 kcps/average`; reference means move similarly, indicating common-mode count drift/provenance even though normalization reduces it.
- Per-average phase at `1.0 MHz` is fairly coherent in the signal/reference ratio, but scalar amplitudes at `0.615`, `1.0`, and `1.385 MHz` are comparable enough that this is not a clean carrier-plus-sideband model.

## Plausible interpretation

The short-tau/high-SNR diagnostic produced analyzable Ramsey data and improved sensitivity relative to the prior long-window follow-up. There is weak coherent-looking content near the intended `1 MHz` detuning, and the short window may be exposing early-time oscillation that was diluted in the earlier `8 us` scan. However, the same data also show sizable common-mode count drift, broad low-frequency baseline structure, and an exploratory maximum closer to `1.2 MHz` than to the programmed carrier. The expected `13C` sideband locations are not distinct from the carrier-scale components.

This is therefore suggestive but not claim-grade evidence for a Ramsey carrier. It does not yet support a fitted T2star, and it does not support a nearby-13C conclusion.

## Claims not yet supported

- No numeric T2star should be claimed from this dataset.
- No nearby-13C coupling or sideband assignment should be claimed.
- Do not claim that the true Ramsey carrier is exactly `1.0 MHz`; the strongest screened feature is broad and displaced toward about `1.2 MHz`.
- Do not claim the r03 branch has failed definitively; this run has more signal-like content than the earlier long-window Ramsey data, but not enough for the requested final conclusion.

## Recommended next action

Run a non-blind confirmation rather than another broad/blind Ramsey repeat. The next useful step is a short-tau Ramsey confirmation on r03 with conditions chosen to separate carrier frequency from drift: keep high shots, start after tau=0, include enough points/window to resolve `1.0` versus `1.2 MHz`, and ideally use a phase/quadrature or repeated-short-window design that tests phase consistency of the suspected carrier. If that confirmation does not produce a clean raw/readout-aware carrier, stop Ramsey repeats on r03 and switch to an alternate T2star/13C diagnostic or close the r03 T2star/13C claims as unsupported under current conditions.
