# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior local context/evidence: `md/memory.md`, `md/knowledge.md`, selected `evidence/*.json` and `evidence/e017.md` for the prior r03 Ramsey status and planned short-tau diagnostic.
- New terminal measurement: `measurement/m001.json` raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` terminal status; `measurement/m005.json` control.

## Calculations or scripts run

- Wrote and ran scratch script `analyze_ramsey.py`; output summary `ramsey_analysis_summary.json` and plot `ramsey_diagnostics.png`.
- Checked terminal provenance: job `nv23_ramsey_20260513_230331_auto_ramsey` completed, no stop request, no monitor error, final count `35.122 kcps`.
- Parsed scan: `tau = 0.048..1.968 us`, `41` points at `48 ns` spacing, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` repetitions.
- Raw/readout checks:
  - reference median `48.57 kcps`, point-to-point range `2.18 kcps`;
  - signal median `44.75 kcps`, point-to-point range `6.50 kcps`;
  - signal/reference ratio median `0.9274`, point-to-point range `0.1433`;
  - median SEM from stored averages: signal `1.14 kcps`, ratio `0.0127`.
- Frequency checks:
  - Least-squares target amplitudes with linear baseline: at `1.000 MHz`, signal `1.28 kcps`, ratio `0.0274`; at expected `13C` sidebands `0.615/1.385 MHz`, signal `1.10/1.22 kcps`, ratio `0.0243/0.0271`.
  - Exploratory linear-baseline LS has broad low-frequency leakage and a lobe near `1.1..1.3 MHz`; coarse FFT bins are at about `0.508 MHz` spacing, with large bins near `1.016` and `1.524 MHz`.
  - Free damped-cosine fits land near `0.726..0.728 MHz` with short apparent decay (`~0.26..0.30 us`), but fixed-frequency damped fits at `0.615`, `1.000`, and `1.385 MHz` are comparably non-unique over this short window.
- Drift/common-mode checks:
  - Per-average reference and signal medians vary strongly (`13.63` and `13.68 kcps` ranges) and are highly correlated (`r = 0.969`), consistent with common-mode brightness drift.
  - Ratio per-average medians vary less but still materially (`0.059` range). Scan-order residual ratio slopes are small compared with the observed ratio fringe scale, so within-average ordering is not the dominant effect.

## Plausible interpretation

The short-tau/high-SNR run is analyzable and shows a real early-time Ramsey-scale modulation in the signal and signal/reference ratio that was not evident in the previous long-window runs. The feature is large compared with per-point scatter in ratio space and roughly comparable to one SEM in raw signal target-amplitude space.

However, the data do not cleanly identify the programmed `1.0 MHz` carrier or either expected `13C` sideband. The short `1.92 us` span gives poor spectral resolution, and damped fits are underconstrained: multiple target frequencies can explain the same early-time curvature with short decay and different phase. A very short dephasing time, detuning mismatch, residual sequence/readout artifact, or unresolved multi-frequency response remain plausible.

## Claims not yet supported

- No claim-grade numeric `T2*` yet. A `~0.2..0.6 us` apparent decay scale is plausible from fits, but it is model-dependent and not robust enough to report as T2*.
- No supported nearby-`13C` conclusion. The expected sideband frequencies are not distinguishable from the carrier or from coarse-window leakage in this run.
- No sub-grid resonance-frequency update from this Ramsey alone.
- Do not claim that r03 has no Ramsey signal; this run shows an early-time feature, but not a clean interpretable carrier/sideband model.

## Recommended next action

Avoid another blind long Ramsey repeat. Run an alternate diagnostic that separates carrier visibility from frequency ambiguity: first re-check the microwave resonance/drive condition with a quick fine weak-pi pODMR or phase-sensitive Ramsey frequency/detuning sweep around the current `3.8759 GHz` setting, then, only if the carrier is pinned, run a targeted Ramsey optimized for T2* extraction. If hardware time is limited, close the current r03 `13C` branch as unsupported while preserving the conclusion that short-tau Ramsey contrast exists but is not yet model-resolved.
