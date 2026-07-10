# Ramsey review: r03 first T2star/13C scout

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`; spot-checked `md/knowledge.md` / `md/memory.md` for Ramsey/FFT guardrails.
- Ramsey job/result/status: `measurement/m002.json` through `measurement/m005.json`.
- Ramsey raw export: `measurement/m001.json`, run `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`.
- Related Ramsey launch evidence cross-checks: `evidence/e009.json`, `evidence/e010.json`, and batch context in `evidence/e011.json`.
- Local outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_diagnostic.png`.

## Calculations or scripts run

- Inspected local context and measurement JSON with PowerShell/Python.
- Ran `python analyze_ramsey.py`.
- The script reads `measurement/m001.json`, computes raw-channel statistics, `signal/reference` ratio, per-average consistency, acquisition-order slopes, detrended Hanning FFTs, weighted fixed-frequency sinusoid projections, and a best-effort damped-cosine fit.
- It wrote `ramsey_analysis_summary.json` and `ramsey_diagnostic.png`; PIL verified the PNG as `1980 x 1440` RGBA. The local image viewer failed with an access error, so the plot was not visually inspected in-browser.

## Quantitative checks

- Measurement setup: tau `0..6 us`, `31` points, `dt = 0.2 us`; raw-export FFT bins are spaced by `161.3 kHz` with Nyquist `2.419 MHz`.
- The run completed and saved data; final counts were `38.249 kcps`, below the fresh track `43.535 kcps` and weak-pODMR final `43.890 kcps`, but still above the configured `20 kcps` floor.
- Averaged raw means: reference/readout-0 `45.32 kcps`, Ramsey signal `42.10 kcps`. Reference relative span is `8.6%`; signal relative span is `18.4%`.
- Averaged `signal/reference` ratio: mean `0.9292`, standard deviation `0.0340`, peak-to-peak span `14.6%`.
- Individual-average ratio traces are not reproducible: pairwise correlations range from `-0.09` to `0.28`; median SEM of the ratio is `0.0256`, or `2.75%` of the mean.
- Scan-order drift proxies are non-negligible: fitted full-order ratio slopes per average are about `+4.6%`, `+6.4%`, `+1.3%`, and `-5.6%`.
- Averaged ratio FFT top bins are `0.968 MHz` (`2.54%` fractional amplitude), `0.806 MHz` (`2.30%`), `0.323 MHz` (`2.22%`), `1.935 MHz` (`2.16%`), and `1.774 MHz` (`2.04%`). The planned `1.5 MHz` carrier is not the dominant averaged component; the nearby `1.613 MHz` bin is only `1.61%`.
- Per-average FFT peaks move: average 1 is dominated by `0.968 MHz`, average 2 by `1.452/1.935/1.613 MHz`, average 3 by `0.323/1.129/1.290 MHz`, and average 4 by `0.806/0.161/0.323 MHz`.
- Weighted sinusoid projections on the mean ratio give only weak amplitudes: `0.967742 MHz` amplitude `0.0199 +/- 0.0055` ratio units; `1.451613 MHz` `0.0121 +/- 0.0054`; `1.612903 MHz` `0.0122 +/- 0.0057`; `1.935484 MHz` `0.0108 +/- 0.0049`. Fits have elevated reduced chi-square around `2.1..2.4`.
- Best-effort damped-cosine fit returns `T2star ~2.39 +/- 1.19 us` and `f ~0.941 +/- 0.035 MHz` with `R2 = 0.446`; this is descriptive only because it follows an unstable averaged feature rather than a reproducible per-average Ramsey component.

## Plausible interpretation

The Ramsey job itself completed and produced analyzable raw data on the accepted r03 candidate. The averaged ratio contains oscillatory structure, but the dominant frequency content is not stable across averages and does not cleanly lock to the planned `1.5 MHz` detuning or a consistent detuning +/- expected `13C` sideband pattern. The most plausible read is that this scout saw a weak Ramsey-like modulation mixed with drift/readout/systematic variation over long per-average windows, not a claim-grade T2star or 13C signature.

## Claims not yet supported

- Do not claim a measured T2star from this run.
- Do not claim nearby `13C` coupling from the FFT peaks.
- Do not claim absence of `13C`; the present run is too unstable/noisy for that exclusion.
- Do not retune the resonance or reinterpret the weak-pODMR center from the fitted `~0.94 MHz` Ramsey frequency; that fit is not robust.

## Recommended next action

Keep r03 as the active target, but treat this as a non-claim-grade scout. Before another bridge-touching measurement, retrack/confirm counts, then run a revised Ramsey repeat only after advisory approval, aiming to reduce the untracked per-average drift window while preserving the FFT sideband test. A practical candidate is the same `0..6 us`, `31` point, `det=1.5 MHz` grid with more tracked averages and fewer repetitions per average, for example `8 x 25000` if the advisory shows a shorter per-average window and acceptable SNR; otherwise shorten the tau grid/span only as much as needed by the advisory.
