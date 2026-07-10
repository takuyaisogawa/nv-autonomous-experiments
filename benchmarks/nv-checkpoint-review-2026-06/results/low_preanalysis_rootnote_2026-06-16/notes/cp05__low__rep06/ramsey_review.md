# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective, current supported claims, and required interpretation posture.
- `md/memory.md`, `md/knowledge.md`: local NV/Ramsey analysis guidance, especially raw/readout-aware signal checks and caution against fit-only claims.
- `context.json`: checkpoint context identifying the just-completed refreshed-center long-span Ramsey.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: job spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json`: terminal bridge status, completed at `2026-05-14T09:28:25`, elapsed `12990 s`.
- `measurement/m005.json`: run control, `stop_requested=false`.
- Prior Ramsey/pODMR context was taken from the project state and evidence summaries only; no outside case knowledge was used.

## Calculations/Scripts Run

- Ran a local Python analysis script against `measurement/m001.json`.
- Wrote scratch outputs:
  - `analysis/ramsey_analysis_summary.json`
  - `analysis/ramsey_review_plot.png`
- Parsed the raw export and sequence XML. The sequence acquires readout 1 as the pre-Ramsey `m_S=0` reference and readout 2 as the Ramsey signal after the Ramsey block, so readout 2 was treated as the primary signal.
- Confirmed scan settings from raw export:
  - `tau = 0.048..8.048 us`, `41` points, `0.200 us` spacing.
  - `20` averages x `50000` repetitions, `1.0e6` shots per tau.
  - `ScanOrderMode = snake`.
  - Job spec target: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
- Computed raw signal/reference curves, point-wise `signal/reference`, and `signal / fitted-reference-line`.
- Estimated per-point uncertainty from stored averages:
  - median raw-signal SEM: `0.850 kcps`.
  - median ratio SEM: `0.0116`.
- Ran least-squares sinusoid screens with constant + linear baseline over `0.1..3.0 MHz`, using both the full span and a skip-first-4-points span.
- Checked target LS amplitudes at:
  - carrier: `1.500 MHz`.
  - expected 13C sidebands from the project model: `1.115 MHz` and `1.885 MHz`.
  - prior empirical controls: `1.192 MHz` and `1.623 MHz`.
- Ran a descriptive fixed-carrier damped sinusoid fit only as a diagnostic, not as a claim basis.

## Quantitative Results

- Raw readout levels:
  - mean signal: `44.67 kcps`.
  - mean reference: `48.79 kcps`.
  - raw edge-to-min signal contrast: about `9.5%`, but this is not organized into a clean target-frequency Ramsey pattern.
- Simple average-to-average common-mode span was large, about `28%` relative span, but a robust MAD screen did not flag individual stored averages as hard outliers. Treat this as drift/provenance, not by itself a hard anomaly.
- Dominant exploratory frequency:
  - Full and skip-first-4 screens in raw signal, point-wise ratio, and fitted-reference normalization all peak at about `2.50 MHz`, the Nyquist edge for `0.200 us` spacing.
  - This edge-locked component is not the programmed carrier or the expected 13C sidebands and is suspicious for point-to-point alternation/grid artifact rather than a physical Ramsey result.
- Target amplitudes:
  - Raw signal LS amplitude at `1.500 MHz`: `0.705 kcps` full, `0.512 kcps` skip-first-4, below the median raw SEM of `0.850 kcps`.
  - Ratio LS amplitude at `1.500 MHz`: `0.0157` full, `0.0123` skip-first-4, only near the median ratio SEM of `0.0116`.
  - Ratio LS amplitude at `1.115 MHz`: `0.00277` full, `0.000678` skip-first-4.
  - Ratio LS amplitude at `1.885 MHz`: `0.00961` full, `0.00528` skip-first-4.
  - Prior `1.192 MHz` control is weak in this dataset: ratio amplitude `0.00194` full, `0.00191` skip-first-4.
  - Prior det-shift `1.623 MHz` control is moderate but not dominant: ratio amplitude `0.00801` full, `0.00709` skip-first-4.
- Per-average ratio screens are inconsistent: most top components sit near the Nyquist edge, with only averages 8 and 20 screening near `1.535 MHz`; the carrier amplitude is not consistently dominant.
- The descriptive fixed-`1.5 MHz` damped fit returned `T2star ~1.40 us` and amplitude `3.29 kcps`, but this is not supported as a physical fit because the target-frequency signal-presence checks fail and the global screen is dominated by a Nyquist-edge component.

## Plausible Interpretation

- The experiment completed and produced analyzable Ramsey data at the intended refreshed pODMR center.
- This run does not give a clean Ramsey carrier at the programmed `1.5 MHz` detuning.
- It also does not give consistent sideband evidence at the expected `1.115/1.885 MHz` 13C positions.
- The strongest feature is locked to the sampling Nyquist edge, which is more plausibly a point-to-point/systematic/grid artifact or unstable readout pattern than a claim-grade physical oscillation.
- Relative to earlier runs, this dataset weakens the case for simply promoting the old `~1.19 MHz` empirical feature, but it still does not establish a replacement carrier/sideband model.

## Claims Not Yet Supported

- No well-supported numeric `T2star` is supported from this dataset.
- No nearby-13C coupling conclusion is supported from this dataset.
- The fixed-carrier damped-fit `T2star ~1.40 us` should not be promoted.
- The `2.50 MHz` Nyquist-edge screen peak should not be assigned to NV Ramsey physics without an explicit sampling/control test.
- A `1.5 MHz` carrier is not established at claim grade because the amplitude is below or near measured SEM and is not consistently dominant across views or averages.

## Recommended Next Action

- Do not run another blind long-span Ramsey repeat under the same conditions.
- Next, choose a protocol or sampling-control diagnostic that can separate point-to-point/Nyquist artifacts from real Ramsey evolution:
  - repeat a short targeted Ramsey with a deliberately changed tau step/Nyquist limit and the same detuning, or
  - switch to a more robust alternate coherence protocol such as Hahn/CPMG baseline if the project goal can accept an alternate route to a supported coherence conclusion.
- Before any new bridge-touching experiment, refresh the pODMR/tracking only if the calibration age or counts require it, and explicitly model whether the planned grid can distinguish the carrier and expected 13C sidebands from the observed Nyquist-edge artifact.
