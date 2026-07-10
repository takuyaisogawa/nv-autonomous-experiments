# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective, current accepted NV candidate, prior Ramsey/pODMR conclusions, and required analysis posture.
- `md/memory.md`, `md/knowledge.md`: local NV analysis guidance on raw/readout-aware review, normalization caveats, shot budget, scan-order drift, and claim thresholds.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: bridge job spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json`, `measurement/m005.json`: terminal status/control provenance.

## Calculations or scripts run

- Created and ran `analyze_ramsey_m001.py`.
- Outputs: `ramsey_m001_analysis.json` and `ramsey_m001_review.png`.
- Confirmed terminal run metadata: completed safely, no stop request, final counts `43.433 kcps`, `tau = 0.048..8.048 us` in 41 points, `20 x 50000` shots, two readouts.
- Treated readout 1 as reference and readout 2 as signal, consistent with the exported `ExperimentData`/`ExperimentDataEachAvg` shape and prior Ramsey practice.
- Computed raw signal/reference traces, fitted-reference normalization, per-tau SEM across 20 stored averages, common-mode average drift screen, least-squares sinusoid amplitude screens, skip-first-4-point screens, and windowed FFT frequency checks.

Key numeric results:

- Median signal `44.804 kcps`; median reference `48.881 kcps`.
- Median signal SEM across stored averages `0.850 kcps`; median ratio SEM `0.0116`.
- No simple 3-sigma common-mode stored-average drift flags by the local screen.
- Full-span fitted-reference ratio LS top frequencies:
  - `2.272 MHz`, amplitude `0.0168`, R2 `0.326`.
  - `1.515 MHz`, amplitude `0.0148`, R2 `0.262`.
  - `2.171 MHz`, amplitude `0.0103`, R2 `0.134`.
  - `1.616 MHz`, amplitude `0.00833`, R2 `0.085`.
- Target LS amplitudes on fitted-reference ratio:
  - Programmed carrier `1.500 MHz`: amplitude `0.01445`, raw-signal amplitude `0.705 kcps`, R2 `0.249`.
  - Expected lower 13C sideband `1.115 MHz`: amplitude `0.00298`, raw `0.145 kcps`, R2 `0.0107`.
  - Expected upper 13C sideband `1.885 MHz`: amplitude `0.00536`, raw `0.261 kcps`, R2 `0.0348`.
  - Previous det-shift top/control `1.623 MHz`: amplitude `0.00770`, raw `0.375 kcps`.
  - Previous short-tau artifact-control `1.192 MHz`: amplitude `0.00226`, raw `0.110 kcps`.
- Skip-first-4 check still has a carrier-region component near `1.518 MHz`, but the largest screen remains near `2.272 MHz`; lower/upper 13C sidebands remain weak.
- Per-average top frequencies are mixed across the scan band rather than clustering cleanly at the programmed carrier or expected sidebands.

## Plausible interpretation

The refreshed-center long-span Ramsey is valid/analyzable and improves the prior 8 us shot budget to `1.0e6` shots per tau point. Unlike earlier det=1.5 MHz short-tau data, the full-span screen now has a real carrier-region component near the programmed `1.5 MHz` detuning, visible in both raw signal and fitted-reference normalization. However, the carrier amplitude is small compared with the measured per-point scatter (`0.705 kcps` raw amplitude vs median signal SEM `0.850 kcps`), and it is not the largest exploratory component; a stronger feature appears near `2.27 MHz`, outside the planned carrier/13C model.

The expected 13C sidebands at about `1.115 MHz` and `1.885 MHz` are weak in both raw and normalized views and do not form a consistent carrier-plus-sideband pattern. The per-average screens are also mixed, so this run does not provide claim-grade T2star or nearby-13C evidence.

The result is nevertheless useful: it weakly supports that a detuning-related Ramsey component can be present after the refreshed pODMR center, but the amplitude/coherence is still too marginal to promote a decay fit or Hamiltonian/13C interpretation.

## Claims not yet supported

- A numeric T2star for `image145844_reimage_r03`.
- A nearby 13C coupling conclusion.
- That the `2.27 MHz` component is physical rather than artifact/noise/analysis leakage.
- That the programmed `1.5 MHz` carrier is strong enough to justify fitting and reporting T2star.
- Sub-grid precision for the pODMR-derived microwave center beyond the refreshed grid-supported `3.8765 GHz` calibration context.

## Recommended next action

Do not run another blind 8 us Ramsey repeat on this branch. The project now has multiple analyzable but non-claim-grade Ramsey datasets, including a high-shot refreshed-center run. The next action should be a decision point: either switch to an alternate T2/13C protocol designed to be more robust to the weak Ramsey contrast/baseline structure, or close the r03 Ramsey branch with a supported negative/unsupported conclusion under the present Ramsey conditions. If continuing experimentally, prefer a targeted alternate protocol with an explicit expected-signal calculation and claim criterion before acquisition, not more accumulation at the same Ramsey settings.
