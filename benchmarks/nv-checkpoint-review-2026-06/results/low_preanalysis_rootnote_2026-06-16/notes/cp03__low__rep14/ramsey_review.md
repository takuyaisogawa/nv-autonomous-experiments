# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, and `evidence/e017.md`.
- New Ramsey measurement artifacts: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control file.
- Measurement identity: `nv23_ramsey_20260513_230331_auto_ramsey`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`, completed 2026-05-14 01:23:47.
- Run settings from local metadata: accepted r03 target, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 48 ns..1.968 us`, 41 points, 12 averages x 90000 repetitions, `auto__ramsey`, snake scan order, tracking per average.

## Calculations or scripts run

- Used local Python to parse `measurement/m001.json`, identify the lower-mean readout as the Ramsey signal and the higher-mean readout as the reference, compute raw signal, reference, signal/reference ratio, per-point SEM across 12 averages, target least-squares sinusoid amplitudes, exploratory frequency screens, subset checks, and a descriptive fixed-1 MHz decaying-cosine fit.
- Wrote `ramsey_analysis_summary.json` with numerical results and `ramsey_shorttau_review.png` showing raw signal/reference and ratio versus tau.
- Key combined-data checks:
  - Mean signal/reference: `44.655 kcps / 48.573 kcps`; median SEM: `1.138 kcps` signal and `0.0127` ratio.
  - Signal range: `40.698..47.197 kcps`; ratio range: `0.8396..0.9829`.
  - Least-squares ratio amplitudes: `1.0 MHz carrier = 0.0274`, expected lower 13C sideband `0.615 MHz = 0.0243`, expected upper sideband `1.385 MHz = 0.0271`.
  - Corresponding raw-signal amplitudes: `1.282 kcps`, `1.103 kcps`, and `1.220 kcps`.
  - Exploratory frequency screen strongest combined component: about `1.20 MHz` in both ratio (`0.0354`) and raw signal (`1.64 kcps`).
  - Direction/subset checks keep a broad best-ratio component near `1.18..1.24 MHz`, but not a stable, target-specific carrier/sideband model. Per-average best frequencies split among about `0.42 MHz`, `1.13..1.30 MHz`, and one `2.12 MHz` case.
  - Descriptive fixed-carrier decaying-cosine fit gives `T2* ~0.158 us`, `A_ratio ~-0.206`, `R2 ~0.58`; this is not claim-grade because it is strongly model-dependent and dominated by the first few points.
- Drift/provenance checks:
  - Terminal job completed without reported bridge error.
  - Snake scan order alternated forward/reverse tau order and data were saved in tau order.
  - Average means show substantial common-mode run drift: median slopes about `-0.65 kcps/avg` reference and `-0.57 kcps/avg` signal; 21/41 reference points and 15/41 signal points had absolute correlation with average index above `0.6`. Ratio normalization reduces but does not eliminate this concern.

## Plausible interpretation

- The short-tau/high-SNR Ramsey diagnostic is more informative than the prior long-window Ramsey scans: it shows a clear early-time structured variation above the per-point SEM scale, with raw-signal amplitude around `1.2..1.6 kcps` and ratio amplitude around `0.03`.
- The data are consistent with r03 having very short dephasing/early-time Ramsey contrast under these conditions, plausibly on the sub-microsecond scale. A descriptive fixed-1 MHz fit lands near `0.16 us`, but this should be treated as a qualitative indicator rather than a reported T2star.
- The dominant exploratory component near `1.2 MHz` is close enough to the designed short-window bandwidth limits and subset variability that it should not be promoted as a physical frequency without a targeted confirmation.
- There is still no clean evidence for the programmed `1.0 MHz` carrier or the expected `0.615/1.385 MHz` 13C sideband pattern. The short window was not designed to resolve 13C sidebands well.

## Claims not yet supported

- A numerical, final T2star value for r03 is not yet supported.
- A nearby 13C coupling conclusion is not supported.
- The `~1.2 MHz` screen maximum is not yet supported as a real Ramsey detuning, hyperfine sideband, or calibration offset.
- The fixed-carrier `T2* ~0.158 us` fit is not supported as a claim-grade parameter because drift, early-point leverage, and model choice are too influential.
- The data do not justify returning to blind long-window Ramsey repeats on r03.

## Recommended next action

- Do not claim final T2star or 13C from this measurement alone.
- Next, run a non-blind confirmation of the early-time behavior rather than another long-window repeat: use a short, dense tau window starting after zero, keep high shots, and include a phase/frequency diagnostic that can distinguish a true `1.0 MHz` carrier from the observed `~1.2 MHz` screen feature. If available within the project constraints, vary Ramsey detuning deliberately or use quadrature/phase-stepped Ramsey; otherwise close the r03 13C branch as unsupported and report only that r03 shows very short, non-claim-grade Ramsey contrast under current conditions.
