# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, `md/memory.md`, `md/knowledge.md`.
- Prior/local evidence: `evidence/e006.md` for the fine weak-pi pODMR center, `evidence/e008.json`/`evidence/e009.json` for the Ramsey plan, and `evidence/e013.md` for the pre-run handoff.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.

## Calculations or scripts run

- Added and ran `python analyze_ramsey.py`.
- Generated `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Parsed the raw export as combined data shape `1 x 2 x 41` and per-average data shape `1 x 8 x 2 x 41`. The combined readouts match the mean of stored averages to numerical precision.
- Used project context/readout convention for `full_experiment=0`: readout 1 as reference and readout 2 as Ramsey signal.
- Checked raw signal, point-wise signal/reference, fitted-reference-line normalization, per-average levels, acquisition-order slopes, FFT bins, least-squares amplitudes at planned frequencies, a broad single-frequency scan, and an exploratory decaying-cosine fit.

Key numbers:

- Run completed safely with final counts `44.184 kcps`.
- Ramsey settings: `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, `dt = 0.2 us`, `8 x 50000` shots.
- Combined mean readouts: reference `49.31 kcps`, signal `44.58 kcps`, point ratio `0.904`.
- Per-average common-mode levels vary strongly: reference means `40.47..55.53 kcps`, signal means `36.20..50.27 kcps`. Reference-line-normalized per-average means are narrower, `0.8897..0.9247`, but not flat.
- FFT of the reference-line-normalized percent trace has top bins at `0.488 MHz` (`1.95%`) and `1.220 MHz` (`1.70%`), not at the programmed `1.0 MHz` carrier.
- Least-squares amplitudes on the reference-line-normalized percent trace:
  - `0.615 MHz` expected low 13C sideband: `1.08%`, SNR `1.66`, `R2 = 0.069`.
  - Prior `0.884 MHz` component: `0.65%`, SNR `1.00`, `R2 = 0.027`.
  - Programmed `1.000 MHz` carrier: `0.62%`, SNR `0.96`, `R2 = 0.024`.
  - `1.385 MHz` expected high 13C sideband: `0.60%`, SNR `0.92`, `R2 = 0.023`.
- Broad single-frequency scan finds a best component near `0.466 MHz` with amplitude `2.06%` and `R2 = 0.261`, but this is sensitivity-dependent. Dropping the first tau point shifts the best component to about `1.145 MHz`; the `1.0 MHz` carrier then falls to `0.12%` amplitude and `R2 = 0.002`.
- Per-average phase coherence is weak/moderate, not claim-grade: carrier `0.45`, low sideband `0.68`, prior component `0.37`, high sideband `0.29`.
- An exploratory free decaying-cosine fit returns about `0.461 MHz`, `T2* = 1.63 +/- 0.54 us`, and `R2 = 0.52` versus a linear baseline, but this fit is descriptive only because it follows the analysis-sensitive non-carrier component.

## Plausible interpretation

The measurement is healthy enough to analyze: it completed, counts stayed high, and the raw export is internally consistent. However, the Ramsey spectral content does not behave like a clean detuned Ramsey signal. The programmed `1.0 MHz` carrier is weak, the prior `0.884 MHz` component is not reproduced as a stable feature, and the strongest components move when early tau points are removed.

The most plausible current interpretation is non-claim-grade Ramsey contrast dominated by drift/common-mode variation, early-time transient structure, or a sequence/phase/calibration artifact. The data do not support promoting the exploratory `0.46 MHz` component to a physical carrier. The det-shift diagnostic weakens the prior `0.884 MHz` observation as a physical assignment.

## Claims not yet supported

- No well-supported `T2*` value is established from this run.
- No well-supported nearby `13C` conclusion is established.
- The exploratory `T2* ~ 1.6 us` fit is not a physical claim.
- The `0.466 MHz` / `1.145 MHz` components are not supported as physical Ramsey carriers.
- The expected `1.0 MHz` carrier is not supported by the combined or per-average checks.
- The expected paired 13C sidebands near `0.615/1.385 MHz` are not supported; the low-sideband frequency has only weak one-sided support and the high sideband is absent.

## Recommended next action

Do not run a higher-shot repeat of the same Ramsey settings as the next move. First do a targeted Ramsey route/phase diagnostic on r03: re-check the weak-pi resonance if needed, then run a short det-control Ramsey comparison or alternate validated Ramsey/echo route to verify that the observed oscillation tracks the programmed detuning. If the carrier still does not track det, treat this Ramsey route/condition as unsuitable for a T2*/13C claim and switch diagnostic strategy rather than accumulating more shots.
