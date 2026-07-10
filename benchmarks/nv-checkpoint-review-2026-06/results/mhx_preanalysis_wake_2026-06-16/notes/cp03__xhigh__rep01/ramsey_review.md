# Ramsey review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- New measurement data: `measurement/m001.json` terminal savedexperiment raw export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Prior/context evidence: `evidence/e003.json` prior det=1.0 MHz 8 us Ramsey terminal review; `evidence/e006.json` short-tau model/advisory; `evidence/e009.json` verified intent; `evidence/e017.md` design/start note.

## Calculations or scripts run

- Created and ran `ramsey_shorttau_review.py`.
- Script outputs: `ramsey_shorttau_review.json` and `ramsey_shorttau_review.png`.
- Checks performed:
  - Raw readout and ratio statistics using readout1 as mS=0 reference and readout2 as Ramsey signal, consistent with prior project review.
  - Scan-order-aware drift proxy using snake `ScanOrderEachAvg`; flag threshold 0.15 negative common-mode end-minus-start fraction.
  - Linear-baseline least-squares components at 1.000 MHz carrier, 0.615 MHz and 1.385 MHz expected 13C sidebands, and the prior 0.884 MHz scout component.
  - Exploratory LS frequency scan over 0.25 to 2.5 MHz, FFT bin check, and per-average frequency screens.

## Key quantitative results

- Run completed: `nv23_ramsey_20260513_230331_auto_ramsey`, 2026-05-13 23:03:46 to 2026-05-14 01:23:47, status completed, no stop request, monitor error empty. Final counts were 35.122 kcps.
- Scan matched intent: `tau = 0.048..1.968 us`, 41 points, 48 ns step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, 12 averages x 90000 repetitions = 1.08e6 shots per tau point.
- Median point SEM improved vs the prior 8 us run: signal SEM 1.397 kcps vs 1.917 kcps prior; ratio SEM 0.0127 vs 0.0187 prior.
- Drift proxy flagged no averages; max negative common-mode score was 0.062, below the 0.15 threshold. Cross-average brightness still varied substantially, with mean signal 37.47 to 51.21 kcps and mean reference 42.02 to 55.19 kcps.
- Target 1.0 MHz component:
  - Ratio LS amplitude 0.0274 with R2 improvement 0.355.
  - Raw signal LS amplitude 1.28 kcps with R2 improvement 0.377; this is about 0.92 x the median raw signal SEM.
- Exploratory combined ratio screen peaks near 1.192 MHz with amplitude 0.0363 and R2 improvement 0.656, but the 1.92 us span gives coarse FFT spacing of about 0.508 MHz and cannot cleanly resolve 1.0 MHz from nearby components or 13C sidebands.
- Expected sideband target amplitudes are comparable to the carrier, not separated or dominant: low sideband 0.0243 ratio / 1.10 kcps; high sideband 0.0271 ratio / 1.22 kcps.
- Per-average frequency screens are inconsistent: several averages peak at the low scan boundary near 0.25 MHz, several near 1.13 to 1.29 MHz, and one near 2.10 MHz.

## Plausible interpretation

The short-tau run is analyzable and does show stronger near-carrier/low-MHz structure than the prior 8 us det=1.0 MHz Ramsey, but it remains non-claim-grade. The raw 1.0 MHz amplitude is only about one median raw SEM, sideband-target amplitudes are similar to the carrier, and per-average frequency behavior is not consistent. The combined 1.19 MHz screen peak may be a weak Ramsey-like component, a baseline/windowing artifact, or residual systematics; the short 1.92 us span does not support assigning it as a precise physical frequency.

This result is compatible with a weak or very short-lived Ramsey signal under current conditions, but it does not supply a stable carrier/decay shape suitable for fitting T2*.

## Claims not yet supported

- No numeric T2* is supported from this Ramsey dataset.
- No nearby 13C coupling or sideband conclusion is supported.
- The 1.192 MHz exploratory peak should not be claimed as a calibrated Ramsey frequency.
- A negative 13C conclusion is also not supported from this short-window FFT, because the frequency resolution is intentionally poor for sideband separation.
- The r03 alignment conclusion is not invalidated; it remains supported by the earlier strong-pi and weak-pi pODMR context.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the r03 Ramsey/T2*/13C branch as unsupported under the current Ramsey conditions unless a deliberately different diagnostic is chosen. The next project action should be a branch decision: either switch to an alternate, explicitly justified protocol after rechecking counts/resonance/tracking, or record no supported r03 T2*/13C conclusion from Ramsey and move to the next candidate/search path.
