# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior local evidence used for expectations: `evidence/e004.json` fine weak-pi pODMR review, `evidence/e007.json` second-Ramsey model/advisory, and `evidence/e013.md` Ramsey-start note.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.
- Local analysis artifacts created: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ramsey.xml` saved data as `full_experiment=0`: readout 1 is the reference and readout 2 is the Ramsey signal.
- Confirmed terminal completion: job `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg` completed, final counts `44.184 kcps`, safe shutdown true, stop request false.
- Checked acquisition: `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, `dt = 0.2 us`, 8 averages x 50000 repetitions, `400000` shots per tau point. FFT Nyquist is `2.5 MHz`; exact FFT bin spacing from 41 points is `121.95 kHz`.
- Model frequencies from the local plan: expected carrier `1.000 MHz`; expected 13C sidebands `0.615423 MHz` and `1.384577 MHz`; prior scout component checked at `0.884 MHz`.
- Scan-order-aware common-mode drift check using `ScanOrderEachAvg` found no average with a >15% linear drop. Stored-average signal means still varied strongly, `36.20..50.27 kcps`, so average-to-average stationarity is limited.
- Raw Ramsey signal: mean `44.58 kcps`, range `7.72 kcps`. The tau-zero point is low: `39.31 kcps`, which is `5.67 kcps` below the median signal over `0.4..1.6 us`.
- Fixed-frequency least-squares fits against a linear baseline:
  - raw signal at `1.000 MHz`: amplitude `0.277 kcps`, SNR `0.96`, delta-R2 `0.024`;
  - raw signal at `0.615423 MHz`: amplitude `0.475 kcps`, SNR `1.66`, delta-R2 `0.069`;
  - raw signal at `1.384577 MHz`: amplitude `0.263 kcps`, SNR `0.92`, delta-R2 `0.022`;
  - raw signal at prior `0.884 MHz`: amplitude `0.286 kcps`, SNR `1.00`, delta-R2 `0.026`.
- Reference-line-normalized signal gives essentially the same target-frequency result: `1.000 MHz` amplitude `0.278 kcps`, SNR `0.96`.
- Exploratory frequency scans are not stable enough to claim: all-points raw/ref-line-normalized scans prefer about `0.466 MHz`, while excluding early tau points shifts raw/ref-line-normalized preference near `1.15 MHz`; point-wise ratio prefers about `1.18 MHz` for some cuts and about `0.45 MHz` for another.
- Damped fixed-`1 MHz` Ramsey fit hit the lower bound, `T2* = 0.2 us`, driven by the tau-zero transient. I do not treat this as a supported T2* estimate.

## Plausible interpretation

This is valid, analyzable Ramsey data, but it does not support a Ramsey carrier at the programmed `1.0 MHz` detuning. The dominant visible feature is a low-tau transient or contrast recovery, especially the tau-zero deficit, rather than a clean decaying sinusoid.

The det-shift diagnostic did not make the prior non-claim-grade `~0.884 MHz` component recur as a strong feature, so that prior component should not be promoted to a physical carrier. The weak lower-sideband-sized response near `0.615 MHz` is below claim strength and lacks the required context of a clear carrier and matching upper sideband. The current data therefore do not support a 13C assignment.

The run stayed bright and completed safely, so this is not evidence that r03 was lost or that the aligned-NV pODMR conclusion is invalid. It is evidence that this Ramsey configuration still did not produce a claim-grade T2*/13C trace.

## Claims not yet supported

- No numeric T2* value is supported by this Ramsey trace.
- No nearby 13C coupling or sideband assignment is supported.
- No stable physical assignment is supported for the prior `~0.884 MHz` component.
- The data do not prove whether the failure is caused by very short T2*, tau-zero/pulse-overlap artifacts, resonance drift, phase-ramp behavior, or readout/normalization artifacts.
- The boundary-hitting `T2* = 0.2 us` fit is not a physical result.

## Recommended next action

Do not repeat the same 8 us Ramsey blindly. First run a targeted diagnostic after confirming the weak-pi pODMR center has not moved: use a shorter, denser early-tau Ramsey that either omits tau zero or explicitly treats it as a separate diagnostic point, and use two programmed detunings to verify that any carrier follows the det setting. Keep the per-average tracking window under the active cap; `measurement/m004.json` reports a terminal estimate of `629.8 s` per average for this run, so a repeat should reduce points or repetitions if the same cap applies.

If a det-following carrier appears, then fit T2* and revisit 13C sidebands. If no det-following carrier appears, switch from claim attempts to a route/phase/readout diagnostic or close this r03 Ramsey/13C branch as no-claim.
