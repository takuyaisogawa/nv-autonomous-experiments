# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, plus relevant guidance from `md/memory.md` and `md/knowledge.md`.
- New Ramsey measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
  - `measurement/m002.json`: submitted job contract for `nv23_ramsey_20260513_185505_auto_ramsey`.
  - `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result, status, and control metadata.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_metrics.json`, `ramsey_analysis_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed raw Ramsey data as 1 scan slice, 2 readouts, 31 tau points, 4 stored averages, 50000 repetitions/average.
- Confirmed actual variables from raw export/job contract: `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `tau = 0..6 us` in `0.2 us` steps, `full_experiment = 0`.
- Treated readout 1 as the 0-level reference and readout 2 as the Ramsey signal, consistent with `full_experiment=0` sequence text.
- Computed raw readout summaries, signal/reference ratio, per-average ratio summaries, FFT of detrended/windowed ratio, and cosine fits excluding `tau=0`.
- Quantitative checks:
  - Terminal run completed; final count text was `38.249 kcps`, above the `20 kcps` gate but down by about 12-13% from the pre-Ramsey/weak-pODMR count level near `43.5-43.9 kcps`.
  - Reference mean `45.32 kcps`, signal mean `42.10 kcps`, ratio mean `0.9292`.
  - Fractional peak-to-peak variation: reference `8.6%`, signal `18.4%`, ratio `14.6%`.
  - Per-average ratio means were close (`0.920..0.938`), but per-average ratio standard deviations were large (`0.056..0.065`); stored-average SEM median was `0.0256`.
  - FFT bin spacing was `0.161 MHz`, Nyquist `2.5 MHz`.
  - Ratio FFT top bins were `0.968`, `0.806`, `0.323`, `1.935`, `1.774`, `0.645 MHz`; the programmed carrier bin near `1.5 MHz` was only `0.087` amplitude at `1.452 MHz`.
  - Expected 13C sideband bins from the prior model were near `1.129` and `1.935 MHz`; amplitudes were `0.093` and `0.151`. The upper bin is visible but not paired with a matching lower-sideband pattern and is comparable to unrelated peaks.
  - Free-frequency Gaussian-damped cosine fit gave `f = 1.741 +/- 0.057 MHz`, `T2* = 3.37 +/- 1.52 us`, but low `R2 = 0.165`; this is descriptive only.
  - Fixed-`1.5 MHz` damped fit was poor/unstable (`R2 = 0.076`, `T2* = 0.69 +/- 0.68 us`), and fixed-`1.5 MHz` no-decay cosine had negative `R2`.

## Plausible interpretation

- The Ramsey scout is analyzable and not a zero-data or count-gate failure.
- There may be weak Ramsey-like modulation, but the measured trace is noisy and not dominated by the programmed `1.5 MHz` carrier.
- The descriptive free-frequency fit can produce a few-us decay scale, but the fit explains little variance and the preferred frequency is displaced from the programmed carrier, so it is not claim-grade T2* evidence.
- The FFT does not show a clean carrier plus symmetric 13C sideband structure. The `1.935 MHz` bin could be consistent with an upper `det + 13C` sideband scale, but it is not isolated, is not paired by a comparable lower sideband, and appears amid other large non-target peaks.
- The final-count drop and long per-average tracking window are relevant drift provenance, but they do not by themselves invalidate the dataset.

## Claims that are not yet supported

- No well-supported T2* value is established from this Ramsey scout.
- No well-supported nearby-13C conclusion is established.
- The data also do not support a negative claim that there is no usable T2* or no nearby 13C; this is a non-claim-grade scout, not decisive absence evidence.
- Do not claim a precise Ramsey detuning/frequency offset from the free fit.
- Do not use the final count or tracked position alone as proof of NV identity or alignment; alignment support still comes from the previous strong/weak pODMR evidence on r03.

## Recommended next action

Repeat Ramsey on accepted r03 with the same weak-pODMR-supported `mw_freq = 3.876 GHz` and deliberate `det = 1.5 MHz`, but redesign the acquisition to improve tracking cadence and independent averaging: keep the 6 us / 31 point grid for the immediate repeat, split shots into more stored averages with fewer repetitions per average if advisory permits, and require a reproducible carrier/FFT pattern before fitting T2* or interpreting 13C sidebands. If the repeat remains non-claim-grade, retake a quick weak-pi pODMR/track check before planning a longer Ramsey span.
