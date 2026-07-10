# Ramsey review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus targeted guidance from `md/memory.md` and `md/knowledge.md`.
- Prior spectroscopy context: `evidence/e003.json` supports r03 weak-pi pODMR grid resonance at `3.876 GHz`.
- New Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` completion status, `measurement/m005.json` run control.
- Inspected `evidence/e011.json`; it is a stale batch-state snapshot still marked running, so terminal interpretation uses `measurement/m003.json` / `measurement/m004.json`.

## Calculations or scripts run

- Created and ran `ramsey_analysis.py`.
- Outputs: `ramsey_analysis_summary.json`, `ramsey_trace.png`, `ramsey_fft.png`.
- Verified PNG creation/dimensions with PIL after the local image viewer returned access denied for this temp path.
- Quantitative checks performed:
  - Parsed Ramsey scan: `tau = 0..6 us`, `31` points, `0.2 us` step, `4 x 50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
  - Treated readout 1 as reference and readout 2 as Ramsey signal because `full_experiment = 0` and the sequence acquires a 0-level reference followed by Ramsey detection.
  - Computed raw readout statistics, signal/reference ratios, per-average ratios, per-average correlations, scan-order drift trends, FFT peaks, and sine+linear fits at `1.5 MHz` and `1.5 +/- 0.384615 MHz`.

## Key numerical results

- Run completed without bridge error. Final counts were `38.249 kcps` versus fresh pre-Ramsey counts `43.535 kcps`, a `-12.1%` change.
- Saved position `[117.279, 117.294, 115.535] um` differs from fresh tracked position `[117.314436, 117.761644, 115.141679] um` by `0.612 um`.
- Raw reference: mean `45.318 kcps`, range `44.038..47.942 kcps`.
- Raw Ramsey signal: mean `42.098 kcps`, range `38.096..45.846 kcps`.
- Mean per-average signal/reference ratio: mean `0.9306`, std across tau `0.0339`, median SEM `0.0256`.
- Per-average ratio correlations are weak/inconsistent: off-diagonal correlations range from about `-0.09` to `0.28`.
- Fixed `1.5 MHz` sine+linear fit to the mean per-average ratio is not meaningful: amplitude `0.0057` ratio units, `R2 = 0.015` versus linear baseline, `p = 0.815`.
- Fits at expected 13C sideband frequencies are also not meaningful:
  - `1.115385 MHz`: amplitude `0.0086`, `R2 = 0.034`, `p = 0.628`.
  - `1.884615 MHz`: amplitude `0.0124`, `R2 = 0.071`, `p = 0.367`.
- FFT bin spacing from the actual `31` samples is `161.3 kHz` (`166.7 kHz` using endpoint span). Largest rectangular-window ratio FFT peak is at `0.968 MHz`, not at the programmed `1.5 MHz`; neighboring/sideband-scale bins are comparable.
- Unconstrained sine scan finds a best unweighted feature near `0.949 MHz` with amplitude `0.024` and `R2 = 0.261`, but weighted scan shifts to `0.301 MHz`; per-average best frequencies vary (`0.925`, `1.652`, `1.301`, `0.854 MHz`).

## Plausible interpretation

The measurement is a completed, analyzable Ramsey scout, but it is not claim-grade. The normalized trace contains weak oscillatory-looking structure, yet it does not lock to the programmed `1.5 MHz` carrier, does not reproduce coherently across the four averages, and has a significant brightness/position drift signature. A real Ramsey frequency offset around `~0.95 MHz` is possible, but the present data do not distinguish that from noise/drift and sparse-window FFT leakage.

## Claims not yet supported

- No supported T2* value from this Ramsey run.
- No supported nearby `13C` coupling or resolved sideband conclusion.
- No supported claim that the `0.95 MHz` feature is the true Ramsey carrier.
- No supported claim that r03 is invalid; the prior pODMR evidence still supports r03 as the aligned candidate, but this Ramsey scout did not produce a reliable T2*/13C result.

## Recommended next action

Do not run a blind longer Ramsey yet. First perform a targeted frequency/stability diagnostic on r03: retrack, verify counts/position recovery, then do a short resonance/Ramsey-carrier check around the `3.876 GHz` basis to determine whether the effective Ramsey oscillation should be near `1.5 MHz` or closer to `~0.95 MHz`. Only after the carrier is reproducible should a higher-SNR T2*/13C Ramsey be run.
