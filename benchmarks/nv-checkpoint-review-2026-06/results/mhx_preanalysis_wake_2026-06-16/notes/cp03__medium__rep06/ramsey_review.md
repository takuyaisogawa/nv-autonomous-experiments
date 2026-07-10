# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`, and latest design/start note `evidence/e017.md`.
- New terminal Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` bridge job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Run identified as `nv23_ramsey_20260513_230331_auto_ramsey`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Script outputs: `ramsey_shorttau_analysis.json` and `ramsey_shorttau_analysis.png`.
- Data shape checks: combined `ExperimentData` is `[1, 2, 41]`; per-average data is `[1, 12, 2, 41]`.
- Measurement settings confirmed from metadata: `tau = 0.048..1.968 us`, `48 ns` spacing, `41` points, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` repetitions, final counts `35.122 kcps`.
- Quantitative checks:
  - Raw signal peak-to-peak: `6.499 kcps`; raw reference peak-to-peak: `2.176 kcps`.
  - Signal/reference ratio peak-to-peak: `0.1433`.
  - Median per-point SEM across stored averages: `1.138 kcps` raw signal, `0.0127` ratio.
  - Linear-baseline LS amplitudes:
    - `1.000 MHz` carrier: `1.282 kcps` raw, `0.0274` ratio.
    - expected lower 13C sideband `0.615 MHz`: `1.103 kcps` raw, `0.0243` ratio.
    - expected upper 13C sideband `1.385 MHz`: `1.220 kcps` raw, `0.0271` ratio.
  - Broad LS screen after linear baseline is dominated by low-frequency curvature if allowed below `0.5 MHz`; restricting to `>=0.5 MHz` gives the largest component near `1.204 MHz` with amplitude about `1.69 kcps` raw and `0.0364` ratio.
  - Empirical decaying-cosine fit to ratio prefers about `1.20 MHz`, but fitted `T2* ~ 6.3 us` is longer than the measured `1.92 us` span and has uncertainty larger than the fitted value, so it is not a supported T2star estimate.
  - Snake direction pair check: forward/reverse grouped ratio RMS difference `0.0330`, comparable to the oscillatory amplitudes, so scan-order/common-mode structure remains relevant provenance.

## Plausible interpretation

- The short-tau/high-SNR diagnostic does show real early-time structure in the Ramsey signal: the raw signal swing is several times the median raw SEM, and the 1 MHz target component is now visible at roughly `1.1x` the raw SEM and `2.2x` the ratio SEM.
- The structure is not a clean programmed-carrier Ramsey result. The strongest non-curvature component is closer to `1.20 MHz` than to the programmed `1.00 MHz`, and amplitudes at the nominal 13C sideband positions are comparable to the carrier rather than forming a clear sideband pattern.
- This run argues against the simple explanation that previous long-window runs failed only because all contrast vanished before `~2 us`; oscillatory structure persists through the short window. It does not by itself establish the correct detuning, decay envelope, or nuclear-spin interpretation.

## Claims not yet supported

- No numeric T2star is supported from this dataset. The decay fit is window-limited and not constrained by the observed span.
- No nearby 13C conclusion is supported. The expected `0.615/1.385 MHz` sideband checks are not separated from the carrier-scale/background features.
- Do not claim that the `~1.20 MHz` feature is a physical detuning, a resonance shift, or a 13C feature without a detuning-following or phase-control check.
- Do not claim that r03 is unsuitable; the spectroscopy alignment evidence still stands, but Ramsey/T2star/13C remain unresolved.

## Recommended next action

Avoid another blind long-window Ramsey repeat. The next useful action is a targeted Ramsey/protocol diagnostic that tests whether the `~1.2 MHz` component follows programmed detuning/phase, or alternatively a fresh fine weak-pi pODMR immediately before such a diagnostic to check for resonance drift. Only return to T2star fitting after a raw/readout-aware Ramsey carrier is supported.
