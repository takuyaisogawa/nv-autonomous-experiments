# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior relevant evidence: `evidence/e006.md` and `evidence/e013.md` for the fine weak-pi pODMR center and the second Ramsey design.
- New Ramsey data/metadata: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Local analysis artifacts created here: `scratch_ramsey_analysis.py`, `ramsey_analysis_results.json`, `ramsey_analysis_plot.png`.

## Calculations or scripts run

- Ran `python scratch_ramsey_analysis.py`.
- Parsed the saved Ramsey raw export: `tau = 0..8 us`, 41 points, 0.2 us step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, 8 averages x 50000 repetitions, snake order, final counts `44.184 kcps`.
- Treated readout 1 as reference and readout 2 as Ramsey signal, consistent with the project context for this sequence. Reviewed raw signal, point-wise signal/reference, and signal divided by a fitted reference line.
- Computed FFTs after linear detrending and Hann windowing, both on all tau points and after excluding the short-tau region (`tau >= 0.4 us`).
- Computed linear least-squares sine/cosine projections at the programmed carrier (`1.000 MHz`), expected 13C sidebands (`~0.616/1.384 MHz` from the local model), the prior scout component (`0.884 MHz`), and the strongest observed carrier-like band (`~1.125-1.165 MHz`).
- Bootstrapped stored averages with replacement and ran coherent frequency-grid checks over per-average normalized traces.
- Ran descriptive Gaussian-envelope Ramsey fits only as diagnostics, after excluding early tau points; these are not promoted to claims.
- Computed simple scan-order drift summaries from the saved snake acquisition order.

## Key quantitative checks

- Combined line-normalized Ramsey signal has mean `0.9040`, standard deviation `0.0261`, and median SEM across stored averages `0.0158`.
- Per-average brightness varied strongly between tracking cycles: reference means ranged `40.47..55.53 kcps`, signal means ranged `36.20..50.27 kcps`. Within-average acquisition-order ratio slopes were smaller, about `-5.5%..+8.5%` across an average, so drift is important provenance but not a hard invalidation.
- All-tau FFT top bins were `1.220 MHz`, `1.098 MHz`, `0.488 MHz`, `0.122 MHz`, and `0.610 MHz`.
- Excluding `tau < 0.4 us`, FFT top bins were `1.154 MHz`, `1.282 MHz`, `0.513 MHz`, `1.026 MHz`, and `0.385 MHz`.
- Least-squares amplitudes on the line-normalized trace, using `tau >= 0.4 us`:
  - `1.165 MHz`: amp `0.0136`, `R2 = 0.306`.
  - `1.125 MHz`: amp `0.0136`, `R2 = 0.305`.
  - expected lower 13C sideband `0.615 MHz`: amp `0.0100`, `R2 = 0.199`.
  - programmed `1.000 MHz`: amp `0.0011`, `R2 = 0.066`.
  - prior scout `0.884 MHz`: amp `0.0021`, `R2 = 0.070`.
  - expected upper 13C sideband `1.385 MHz`: amp `0.0010`, `R2 = 0.066`.
- Coherent per-average grid check for `tau >= 0.4 us` peaked at `1.145 MHz` with nearby `1.14..1.155 MHz` nearly degenerate.
- Bootstrap over the 8 stored averages for `tau >= 0.4 us` gave a peak-frequency median `1.145 MHz`, 16-84% range `1.110..1.195 MHz`, and broad 2.5-97.5% range `0.710..1.220 MHz`.
- Descriptive fits over `tau >= 0.4, 0.6, 1.0 us` returned frequencies `1.148..1.164 MHz` and T2* values `5.6..6.6 us`, with only `R2 = 0.37..0.40`; the result depends on cutoff/initialization and should not be claimed.

## Plausible interpretation

- The new Ramsey data are analyzable and show a weak but coherent carrier-like component near `1.15 MHz` after excluding the short-tau point(s). This is closer to the programmed `1.0 MHz` detuning than the earlier scout's non-claim-grade `~0.884 MHz` component, but it does not land cleanly on `1.000 MHz`.
- A carrier near `1.15 MHz` is plausible if the fine pODMR grid center is still offset from the true Ramsey resonance by order `0.1 MHz`; the prior pODMR center was only grid-supported, not sub-grid precise.
- The lower expected 13C-sideband region near `0.616 MHz` has some power, but the upper sideband near `1.384 MHz` is weak and the low-frequency/early-tau behavior is sensitive to preprocessing. This is not enough for a nearby-13C assignment.
- The data are consistent with a Ramsey contrast/oscillation that may persist for several microseconds, but the envelope is too weak and model-dependent for a supported T2* value.

## Claims not yet supported

- No claim-grade T2* value is supported. The diagnostic `~5.6..6.6 us` fit is only a guide because the fit quality is modest and sensitive to tau cutoff.
- No supported 13C conclusion is established. The expected sideband pair is not symmetrically or robustly resolved.
- The exact Ramsey carrier frequency is not established at sub-100-kHz precision. The strongest current evidence points near `1.15 MHz`, not exactly the programmed `1.0 MHz`.
- The prior `~0.884 MHz` component is not reproduced as a strong component in this run, so it should not be treated as a physical carrier or 13C feature.

## Recommended next action

Run a targeted Ramsey frequency diagnostic on the same accepted r03 before spending more shots on a T2* claim. Use the same `mw_freq = 3.8759 GHz` unless a fresh weak-pi pODMR is first obtained, but choose a Ramsey design that resolves whether the carrier is actually near `1.15 MHz` versus `1.0 MHz` and reduces the short-tau artifact, for example by starting tau at `0.4 us` or handling tau-zero separately. If the carrier is confirmed and repeatable, then run a higher-SNR Ramsey/T2* measurement centered on the confirmed carrier and only then evaluate T2* and 13C sidebands.
