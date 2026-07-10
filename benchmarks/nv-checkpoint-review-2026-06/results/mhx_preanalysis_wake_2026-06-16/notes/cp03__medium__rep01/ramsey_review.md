# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective and prior decision state.
- `md/memory.md`, `md/knowledge.md`: local NV/Ramsey analysis guidance.
- `evidence/e003.json`: prior det=1.0 MHz, 8 us Ramsey terminal review.
- `evidence/e006.json`, `evidence/e017.md`: short-tau diagnostic model/advisory and start note.
- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- `measurement/m002.json`: job specification for `nv23_ramsey_20260513_230331_auto_ramsey`.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json`, `measurement/m005.json`: final status/control snapshots.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py` using only local JSON inputs.
- The script wrote `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Checks performed:
  - parsed combined and per-average raw readouts from `measurement/m001.json`;
  - reconstructed the tau grid: 48 ns to 1.968 us, 41 points, 48 ns spacing;
  - computed raw signal/reference ratio and signal normalized by a fitted reference line;
  - computed per-point SEM from 12 stored averages;
  - screened least-squares sinusoid components against a linear baseline at 1.000 MHz, 0.615 MHz, 1.385 MHz, and prior 0.884 MHz;
  - ran dense exploratory LS frequency screens and FFT checks;
  - ran a diagnostic fixed-1 MHz exponential-envelope fit only as a non-claim-grade shape check.

Key numbers:

- Acquisition completed: `12 x 90000 = 1.08e6` shots per tau point, final counts `35.122 kcps`, no stop request, status completed.
- Combined means: reference `48.573 kcps`, Ramsey signal `44.655 kcps`, ratio `0.91946`.
- Median point uncertainty from stored averages: signal SEM `1.138 kcps`, ratio SEM `0.01271`.
- Raw signal residual after linear baseline has peak-to-peak span `5.25 kcps`; ratio residual peak-to-peak is `0.1146`.
- Programmed carrier LS amplitude at `1.000 MHz`: signal `1.282 kcps`, ratio `0.0274`, R2 improvement vs linear baseline about `0.35-0.38`.
- Expected sideband target amplitudes are not separated from the carrier: `0.615 MHz` gives signal `1.103 kcps`, ratio `0.0243`; `1.385 MHz` gives signal `1.220 kcps`, ratio `0.0271`.
- Dense combined LS screen peaks near `1.19 MHz` with ratio amplitude `0.0363` and raw signal amplitude about `1.68 kcps`; FFT bins are coarse because the window is short, with top ratio bins at about `1.52 MHz`, `1.02 MHz`, and `0.51 MHz`.
- Per-average means vary substantially: signal means range about `37.47..51.21 kcps`, reference means about `42.02..55.19 kcps`, and ratio means about `0.8935..0.9561`. Per-average frequency screens are inconsistent.
- A fixed-1 MHz exponential-envelope diagnostic fit prefers an apparent very short timescale around `0.16..0.19 us`, but this is not robust enough to promote as T2star because it is driven by early-time/baseline structure and lacks per-average/frequency support.

## Plausible interpretation

- The short-tau/high-SNR diagnostic is analyzable and did improve early-time sensitivity relative to the prior 8 us run.
- The combined trace contains a broad Ramsey-like oscillatory residual around the programmed-carrier scale, and this is plausibly compatible with a weak or very short-lived Ramsey response on r03.
- However, the measured carrier-scale amplitude is only about one median raw SEM per point and below the several-kcps signal scale the diagnostic was designed to make clearly visible. The 0.615 MHz and 1.385 MHz sideband targets are comparable to the carrier component rather than distinct. The short time window also gives poor frequency discrimination, and per-average behavior is not consistent enough to turn the combined residual into a parameter claim.

## Claims that are not yet supported

- No numeric T2star is supported from this Ramsey dataset.
- No nearby-13C conclusion is supported from the FFT/LS screens.
- The exploratory `~1.19 MHz` combined LS maximum should not be claimed as a physical detuning; it is not well resolved from 1.0 MHz on this short window and is not stable across averages.
- The diagnostic exponential-envelope fit should not be reported as T2star.
- This Ramsey result does not invalidate the prior pODMR-supported conclusion that r03 is a magnetic-field-aligned candidate; it only leaves the r03 Ramsey/T2star/13C branch unresolved under the tested conditions.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the short-tau result as weak, non-claim-grade evidence for a possible very short/low-contrast Ramsey response, then either switch to a deliberately modeled alternate protocol/check that can answer the T2star/13C question under low Ramsey contrast, or close the r03 Ramsey/T2star/13C branch as unsupported under current conditions. A good next project action is a protocol-level decision note comparing an alternate pulse sequence or calibration diagnostic against branch closeout, with explicit expected signal and resolvability before any new bridge submission.
