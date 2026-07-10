# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` bridge job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior local evidence/context: `evidence/e017.md` for the short-tau design/start note and recent context entries describing the two non-claim-grade earlier Ramsey runs.
- Generated local analysis artifacts: `analysis/ramsey_shorttau_summary.json`, `analysis/ramsey_shorttau_views.png`, `analysis/ramsey_shorttau_ls_spectrum.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/NumPy. Raw data shape is `ExperimentData = (1, 2, 41)` and `ExperimentDataEachAvg = (1, 12, 2, 41)`.
- Verified scan settings from raw export: `tau = 0.048..1.968 us`, `dt = 48 ns`, 41 points, Nyquist `10.42 MHz`, FFT bin spacing `0.508 MHz`, `12 x 90000` repetitions.
- Treated readout 1 as reference and readout 2 as signal, consistent with the local sequence-default note for Ramsey-style two-readout data. Checked raw signal, signal/reference, and signal normalized by a fitted reference line.
- Ran least-squares screens using `linear baseline + cos/sin(f*tau)` at target frequencies `0.615 MHz`, `1.000 MHz`, and `1.385 MHz` where the sideband targets follow prior project context for `det = 1.0 MHz` and expected nearby `13C` Larmor near `0.385 MHz`.
- Ran a frequency-amplitude screen, Hann-window FFT after linear detrending, per-average 1.0 MHz phase/amplitude checks, forward/reverse snake-order grouping, first-half/last-half grouping, simple AIC comparisons against polynomial baselines, and damped-cosine fits with fixed/free frequency.

## Quantitative checks

- Terminal execution completed safely with final count text `35.122 kcps`, above the `20 kcps` gate but lower than the previous `44.184 kcps`; this is drift/count provenance.
- Signal median per-point uncertainty is about `1.40 kcps` from `ExperimentDataError`, and the median SEM from stored-average scatter is about `1.14 kcps`.
- The programmed `1.0 MHz` component is now visible in the short-tau data:
  - raw signal amplitude `1.282 kcps`, LS amplitude SNR `4.73`, `R2 = 0.455`;
  - signal/reference amplitude `0.0274`, LS amplitude SNR `4.50`, `R2 = 0.447`;
  - fitted-reference-line-normalized signal amplitude `1.282 kcps`, LS amplitude SNR `4.73`, `R2 = 0.476`.
- Per-average 1.0 MHz phases are mostly consistent: phase-resultant length `0.93` unweighted and `0.95` amplitude-weighted. The 1.0 MHz component remains in both snake-order groups: forward/odd average group amplitude `1.34 kcps`, reverse/even group `1.23 kcps`.
- Stored-average mean levels drift substantially: average signal means range from about `37.47` to `51.21 kcps`, with late averages 10-11 low. The target component persists in first six averages (`1.53 kcps`) and last six averages (`1.03 kcps`), but drift is still important provenance.
- Frequency specificity is limited. A low-frequency edge component dominates the amplitude screen (`0.2 MHz` screen edge), consistent with strong broad curvature over the short window. FFT resolution is coarse (`0.508 MHz` bins); the largest detrended FFT bin is `1.524 MHz`, not a resolved physical sideband claim.
- Damped-cosine T2star fits are not stable enough for a claim. Fixed `1.0 MHz` fits return very short `T2*` values (`0.19 us` exponential or `0.36 us` Gaussian) with large initial amplitudes, while free-frequency fits prefer `~1.18-1.19 MHz` and give either `T2* ~2.8 us` with large uncertainty or a boundary-like `100 us` Gaussian result.
- Simple AIC checks prefer a quadratic baseline over `linear + 1.0 MHz` for both raw signal and signal/reference, showing that the short window cannot by itself separate smooth baseline curvature from a full physical Ramsey decay model.

## Plausible interpretation

- This diagnostic does support an early-time Ramsey-like oscillatory structure near the programmed `1.0 MHz` detuning. That is materially stronger than the prior 8 us Ramsey result, where the programmed carrier was weak and below/near SEM.
- The result argues against the strongest version of "there is no early Ramsey response on r03." It is compatible with the earlier long-window failures being affected by windowing, tau-zero/baseline behavior, drift, or low carrier contrast.
- The data do not yet provide a reliable T2star. The scan was intentionally short, contains only about two programmed carrier periods, has substantial broad curvature, and produces model-dependent decay constants.
- The data do not support a nearby `13C` conclusion. The short span gives poor FFT resolution, and the apparent `1.524 MHz` bin cannot distinguish a true sideband from leakage of a broad/shifted carrier, windowing, baseline curvature, or drift.

## Claims not yet supported

- No numeric T2star should be claimed from this run.
- No nearby `13C` coupling or absence claim should be made from this run.
- No sub-grid Ramsey frequency correction should be claimed from the free-frequency fits.
- Do not claim that late-run count drift is harmless; it did not destroy the 1.0 MHz check, but it remains provenance that must inform the next acquisition.

## Recommended next action

Do not run another blind repeat. Because this diagnostic now shows a plausible early Ramsey carrier, run a non-blind follow-up designed to estimate T2star: avoid `tau = 0`, keep the fine-pODMR `mw_freq = 3.8759 GHz` initially, sample a longer but still focused window such as roughly `0.048..4-6 us` with enough points to resolve the `1.0 MHz` carrier and the expected `0.615/1.385 MHz` sideband positions, and keep high shots with even averages and per-average tracking. Use the result first to confirm carrier/decay shape in raw and reference-normalized views; only then fit T2star or make a 13C statement.
