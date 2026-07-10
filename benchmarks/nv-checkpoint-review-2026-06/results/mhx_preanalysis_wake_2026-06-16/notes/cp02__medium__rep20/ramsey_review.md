# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior context/evidence: `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New Ramsey run artifacts: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the 8-average Ramsey export: `ramsey.xml`, `tau = 0..8 us`, 41 points, `dt = 0.2 us`, `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`, `8 x 50000` repetitions, snake scan order.
- Checked raw signal readout, reference readout, point-wise signal/reference, and signal normalized by a fitted reference line.
- Computed linear-detrended Hann FFTs at the programmed carrier (`1.0 MHz`), expected 13C sidebands (`~0.615/1.385 MHz` from project model), and the prior exploratory component (`~0.884 MHz`).
- Checked per-average signal means, acquisition-order slopes, signal extrema, and per-average FFT peaks.
- Ran descriptive damped-cosine fits seeded near `1.0 MHz`; these were treated as diagnostics only, not claim evidence.
- Ran additional scratch checks excluding early tau points (`tau >= 0.2, 0.4, 1.0 us`) to test sensitivity to the strong tau-zero/early-time feature.

## Plausible interpretation

- The run completed safely: terminal status `completed`, final counts `44.184 kcps`, saved raw data present.
- The combined signal has visible structure: raw signal peak-to-peak is `7.72` readout units, `17.3%` of mean signal, about `4.0x` the median per-point SEM across stored averages.
- The strongest combined FFT components are not at the exact programmed carrier. After linear detrending:
  - raw signal peak: `1.220 MHz`; amplitude at `1.000 MHz` is `42%` of that peak.
  - point-wise ratio peak: `1.098 MHz`; amplitude at `1.000 MHz` is `63%` of that peak.
  - fitted-reference-line-normalized signal peak: `1.220 MHz`; amplitude at `1.000 MHz` is `42%` of that peak.
- The expected 13C sidebands are not dominant or mutually supported: raw amplitudes at `0.615/1.385 MHz` are about `50%/46%` of the raw peak, while ratio amplitudes are about `36%/31%` of the ratio peak.
- The prior `~0.884 MHz` component is not reproduced as the dominant feature in this det-shifted run; this weakens a fixed-frequency physical interpretation of the prior scout peak, but does not by itself prove the new `~1.1-1.2 MHz` feature is physical.
- Per-average behavior is the limiting issue. Average-level FFT peaks scatter widely (`0.122, 0.488, 0.488, 0.244, 1.707, 0.244, 1.220, 0.366 MHz`), and per-average signal/reference means show large common-mode changes. Ratio means are more stable, so much of the average-to-average movement is likely count/baseline drift, but coherent Ramsey evidence remains weak.
- Descriptive damped-cosine fits give `f ~1.19 MHz`, `T2* ~2.1-2.3 us`, and only `R2 ~0.46-0.49`. Removing early tau points lowers fit quality (`R2 ~0.31-0.34`) and leaves peaks near `1.1-1.18 MHz`. These fits are not reliable enough to quote as T2*.
- Terminal status recorded an expected per-average/tracking window of `629.8 s`, above the earlier planning cap of `600 s`; this supports treating drift/average inconsistency as important provenance.

## Claims that are not yet supported

- No well-supported T2* value is supported by this run.
- No claim-grade 13C conclusion is supported by this run.
- Do not claim a resolved Ramsey carrier exactly at the programmed `1.0 MHz`.
- Do not assign the `~1.1-1.2 MHz` exploratory component to physical detuning or hyperfine structure without a follow-up that improves average consistency and reproduces the frequency.
- Do not interpret the descriptive `T2* ~2 us` fit as a measured T2*; it is fit-only/low-R2 and sensitive to early-time handling.

## Recommended next action

Do not blindly repeat the same long Ramsey. First, do a targeted Ramsey diagnostic that reduces drift exposure and tests the carrier assignment: either shorten the per-average window with fewer tau points/repetitions while preserving coverage of `~1.0-1.3 MHz`, or run a small det-dependence check after confirming the weak-pi ODMR center is still valid. Treat success criteria as raw/readout-aware reproduction of a carrier that follows programmed det and per-average agreement before fitting T2* or making any 13C claim.
