# Case Walkthrough

This document is a reader guide for the completed autonomous NV-center case
studies. It focuses on what the agent read, what it decided, and which artifacts
it left behind.

## How To Audit A Case

Start here:

1. Read `cases/<case>/README.md`.
2. Read `cases/<case>/project/work/state.md`.
3. Use the `Evidence Pointers` section in `work/state.md` to jump into the
   evidence ledger, notes, analysis JSON, figures, and reports.
4. Check bridge/job records under `work/bridge_jobs/` for execution contracts.
5. Check analysis code and outputs under `work/artifacts/analysis/`.
6. Check figures under `work/artifacts/figures/`.
7. Read the final closeout report or closeout note.

The high-level artifact map is:

| Artifact class | Where |
| --- | --- |
| Current readable state | `cases/<case>/project/work/state.md` |
| Machine state and ledger | `cases/<case>/project/.manager/` |
| Evidence records | `cases/<case>/project/.manager/evidence.jsonl` |
| Human-readable work notes | `cases/<case>/project/work/notes/` |
| Bridge/job records | `cases/<case>/project/work/bridge_jobs/` |
| Analysis code and JSON outputs | `cases/<case>/project/work/artifacts/analysis/` |
| Figures | `cases/<case>/project/work/artifacts/figures/` |
| Reports and summaries | `cases/<case>/project/work/artifacts/reports/`, `work/reports/`, or `summaries/` |
| Raw MATLAB data copies | `cases/<case>/project/data_*/` |

## image172647

Objective: find a magnetic-field-aligned NV from `image172647`, then estimate
T2star and assess evidence for coupling to nearby 13C nuclei.

Main entry points:

- Case README: `cases/image172647/README.md`
- Project state: `cases/image172647/project/work/state.md`
- Evidence ledger: `cases/image172647/project/.manager/evidence.jsonl`
- Recovered raw data: `cases/image172647/project/data_recovered_20260515/matlab_23C/`
- Closeout report: `cases/image172647/project/work/reports/closeout_20260515_1225/nv23_image172647_closeout_report_20260515.pdf`

### Agent Timeline

| Stage | Agent read | Agent decision | Artifact trail |
| --- | --- | --- | --- |
| Initial image audit | Saved image `3DXYZ-Image-2026-05-14-172647.mat` and candidate ranking | The agent selected the first candidate and required tracking and pODMR measurements before deciding whether it was aligned with the magnetic field. | `work/artifacts/image172647_candidates/`, `work/notes/image172647_initial_candidate_selection_and_c01_track_20260514_1736.md` |
| Stale-candidate recovery | Initial c01 TrackCenter success, failed pODMR execute, failed retrack | The agent acquired a new image of the original region after the photon count dropped and tracking failed. | `work/artifacts/recovery/`, `work/artifacts/bridge_results/` |
| Fresh re-image | New imaging result and candidate ranking | The agent used the new image to test `reimage1804_c01`, then `reimage1804_c02`. | `work/artifacts/image172647_reimage1804_candidates/`, `work/artifacts/figures/image172647_reimage1804_candidate_peaks_20260514_1812.png` |
| Reject `reimage1804_c01` | TrackCenter and terminal strong-pi pODMR review | The agent rejected c01 because a pODMR measurement with adequate photon counts showed only shallow dips and no clear usable resonance. | `work/artifacts/analysis/reimage1804_c01_podmr_terminal_summary_4avg_20260514_1859.json`, `work/notes/reimage1804_c01_podmr_terminal_review_reject_20260514_1900.md` |
| Accept `reimage1804_c02` | TrackCenter plus terminal strong-pi pODMR | The agent accepted c02 as aligned with the magnetic field because a clear resonance near 3.875 GHz appeared only in the signal channel, although the contrast was lower than expected. | `work/artifacts/analysis/reimage1804_c02_podmr_terminal_summary_4avg_20260514_1957.json`, `work/notes/reimage1804_c02_podmr_terminal_review_accept_20260514_1959.md` |
| Initial Ramsey measurement | Analysis of the completed Ramsey measurement at 1.5 MHz detuning | The agent identified weak oscillations and tentatively estimated a T2star of a few microseconds, but did not establish 13C coupling or a reliable T2star value. | `work/artifacts/analysis/reimage1804_c02_ramsey_terminal_8avg_summary_20260514_2150.json`, `work/artifacts/figures/reimage1804_c02_ramsey_terminal_8avg_20260514_2150.png` |
| Weak-pi center refinement | Weak-pi pODMR terminal review | The agent refined the resonance frequency to `3.876501337 GHz` and ruled out a large error in the resonance frequency as the explanation for the earlier high-frequency Ramsey component. | `work/artifacts/analysis/reimage1804_c02_weak_pi_podmr_terminal_4avg_summary_20260514_2251.json`, `work/artifacts/figures/reimage1804_c02_weak_pi_podmr_terminal_4avg_20260514_2251.png` |
| det=1.0 Ramsey discriminator | Terminal 16-average det=1.0 MHz Ramsey | The agent tentatively estimated a T2star of a few microseconds and noted a weak frequency component near the programmed detuning plus the estimated 13C Larmor frequency. It did not establish 13C coupling from Ramsey alone. | `work/artifacts/analysis/reimage1804_c02_ramsey_det1_terminal_summary_16avg_20260515_0245.json`, `work/artifacts/figures/reimage1804_c02_ramsey_det1_terminal_16avg_20260515_0245.png` |
| det=1.25 Ramsey discriminator | Third-detuning model, autosave trends, terminal 16-average review | The agent judged the frequency shift consistent with a possible 13C contribution, but insufficient to confirm it from Ramsey alone. | `work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_terminal_summary_16avg_20260515_0645.json`, `work/artifacts/figures/reimage1804_c02_ramsey_det1p25_terminal_16avg_20260515_0645.png` |
| CPMG N=8 follow-up | CPMG model using the calibrated resonance frequency and estimated 13C Larmor frequency | The agent used CPMG to investigate a possible 13C contribution and interpreted the dip as supporting this hypothesis. | `work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_target_region_review_20260515_0945.json`, `work/artifacts/figures/reimage1804_c02_cpmg_n8_terminal_target_region_20260515_0945.png` |
| Closeout | Closeout report bundle and final state | The agent marked the original objective as satisfied and planned no further measurements. | `work/reports/closeout_20260515_1225/`, `summaries/nv23_image172647_closeout_report_20260515.pdf` |

### Summary

The agent selected `reimage1804_c02` after acquiring a new image, calibrated
its resonance frequency with pODMR, and measured Ramsey signals at several
detunings. It reported a T2star estimate of about `2-3 us`, depending on the
analysis method, and interpreted the subsequent CPMG response as supporting a
13C origin for the weak frequency components in the Ramsey spectra. The
surrounding 13C spin bath could contribute to both signals, but the CPMG
response does not establish that the same interactions explain the Ramsey
components.

## image145844

Objective: find a magnetic-field-aligned NV from `image145844`, then estimate
T2star and assess evidence for coupling to nearby 13C nuclei.

Main entry points:

- Case README: `cases/image145844/README.md`
- Project state: `cases/image145844/project/work/state.md`
- Evidence ledger: `cases/image145844/project/.manager/evidence.jsonl`
- Recovered raw data: `cases/image145844/project/data_recovered_20260514/matlab_23C/`

### Agent Timeline

| Stage | Agent read | Agent decision | Artifact trail |
| --- | --- | --- | --- |
| Initial image audit | Original `image145844` export and candidate selection outputs | The agent checked the image axes and units before accepting the export and selecting the initial candidate `r01`. | `work/artifacts/analysis/image145844_raw_export_20260513_1509.json`, `work/artifacts/analysis/image145844_candidate_selection_20260513_1509.json` |
| `r01` failure handling | TrackCenter success, failed pODMR, failed retrack | The agent did not treat the failed pODMR acquisition as evidence that `r01` lacked a resonance because the photon count had collapsed. | `work/notes/20260513_1546_r01_count_collapse_reimage.md`, `work/bridge_jobs/` |
| Re-image and candidate refresh | Fresh imaging export with explicit axis permutation and new candidate list | The agent used the new image to select candidates `r01`, `r02`, and `r03`. | `work/artifacts/analysis/image145844_reimage_raw_export_20260513_1548.json`, `work/artifacts/analysis/image145844_reimage_candidate_selection_20260513_1550.json` |
| Reject fresh `r01` | Fresh `r01` TrackCenter and strong-pi pODMR raw/readout review | The agent found no clear usable resonance despite successful tracking and did not plan Ramsey measurements on `r01`. | `work/artifacts/analysis/image145844_reimage_r01_strong_podmr_raw_review_20260513_1615.json`, `work/notes/20260513_1629_reimage_r01_r02_alignment_progress.md` |
| Reject fresh `r02` | Fresh `r02` TrackCenter and strong-pi pODMR raw/readout review | The agent rejected `r02` as an aligned candidate because it showed no clear usable resonance. | `work/artifacts/analysis/image145844_reimage_r02_strong_podmr_raw_review_20260513_1658.json`, `work/notes/20260513_1709_r02_review_and_r03_track.md` |
| Accept `r03` as aligned | Fresh `r03` TrackCenter plus strong-pi pODMR terminal review | The agent accepted `r03` as the first candidate aligned with the magnetic field because the raw signal and both normalized readouts showed a resonance at the same scan point. | `work/artifacts/analysis/image145844_reimage_r03_strong_podmr_raw_review_20260513_1741.json`, `work/notes/20260513_1808_r03_acceptance_and_weak_podmr_start.md` |
| Refine the resonant frequency | Weak-pi and fine weak-pi pODMR reviews | The agent selected microwave frequencies from the measured pODMR scan points for Ramsey measurements, without claiming precision finer than the scan spacing. | `work/artifacts/analysis/image145844_reimage_r03_weak_podmr_raw_review_20260513_1838.json`, `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031.json` |
| Initial Ramsey measurement | Raw data, Fourier analysis, and drift checks from the completed Ramsey measurement | The agent analyzed the Ramsey data but did not establish a reliable T2star value or identify 13C coupling. | `work/artifacts/analysis/image145844_reimage_r03_ramsey_t2star_raw_fft_review_20260513_1930.json`, `work/notes/20260513_1958_weak_podmr_review_and_ramsey_start.md` |
| Ramsey measurements with revised settings | Second long-span Ramsey, short-tau/high-SNR diagnostic, det-shift diagnostic | The agent varied the measurement conditions to investigate the ambiguous results and left the interpretation of the frequency components unresolved. | `work/artifacts/analysis/`, `work/notes/20260513_2220_second_ramsey_terminal_review.md`, `work/notes/20260514_0200_shorttau_terminal_review_and_detshift_start.md` |
| pODMR refresh | Fine weak-pi pODMR refresh after det-shift branch | The agent updated `mw_freq_hz` using pODMR before the final Ramsey measurement and treated that scan as a calibration. | `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_20260514_0523.json`, `work/notes/20260514_0540_podmr_refresh_review_and_refreshed_center_ramsey_design.md` |
| Final Ramsey measurement after recalibration | Analysis and model comparison for the final Ramsey measurement, acquired with 20 averages after updating the resonance frequency | The agent did not obtain a reliable T2star estimate from fits with the Ramsey frequency fixed at the programmed detuning, and did not establish 13C sidebands. | `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json`, `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.json` |
| Reanalysis without new measurements | Human advice requesting Ramsey frequency reanalysis, final Ramsey data, bootstrap/model comparison | The agent revised its interpretation of the Ramsey frequency after considering a residual calibration error, without acquiring new measurements. | `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_20260514_1308.json`, `work/artifacts/analysis/image145844_reimage_r03_shifted_triplet_targeted_bootstrap_20260514_1312.json` |
| Closeout | Revised closeout report and work note | The agent stopped further measurements and recorded the limitations of its conclusions. | `work/artifacts/reports/20260514_1320_r03_shifted_sideband_recloseout/image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.pdf`, `work/notes/20260514_1320_shifted_sideband_reanalysis_and_recloseout.md` |

### Summary

The agent selected `r03` as aligned with the magnetic field and varied the
Ramsey measurement conditions to investigate ambiguous results. It later
revised its interpretation of the Ramsey frequency after considering a residual
calibration error, without acquiring new data. The analysis did not establish
a reliable T2star value or identify coupling to an individual nearby 13C nucleus.

## image231924

Objective: find a magnetic-field-aligned NV from `image231924`, then estimate
T2star and assess evidence for coupling to nearby 13C nuclei.

Main entry points:

- Case README: `cases/image231924/README.md`
- Project state: `cases/image231924/project/work/state.md`
- Evidence ledger: `cases/image231924/project/.manager/evidence.jsonl`
- Raw/data copy: `cases/image231924/project/data_git_20260512/`

### Agent Timeline

| Stage | Agent read | Agent decision | Artifact trail |
| --- | --- | --- | --- |
| Initial image audit | Source image export and candidate list | The agent selected `image231924_c01` and used TrackCenter to assess tracking, without inferring alignment from tracking alone. | `work/artifacts/analysis/image231924_candidate_list.json`, `work/notes/image231924_candidate_selection_20260511_2324.md` |
| First pODMR failure | Failed first strong-pi pODMR result and TrackCenter recheck | The agent rechecked tracking before further spectroscopy and did not use the failed acquisition to judge whether a resonance was present. | `work/bridge_jobs/`, `work/state.md` evidence pointers |
| Strong-pi pODMR retry | Retry bridge result and raw/readout-aware pODMR review | The agent accepted the NV as aligned with the magnetic field after observing a resonance near `3.879 GHz`, but did not treat this as a precise estimate of its center. | `work/artifacts/analysis/image231924_c01_strong_podmr_retry1_review.json`, `work/notes/image231924_c01_strong_podmr_retry1_review_20260512_0038.md` |
| Weak-pi pODMR | Weak-pi pODMR result and review | The agent selected a resonance frequency from the measured pODMR scan points for the Ramsey measurement. | `work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json`, `work/notes/image231924_c01_weak_podmr_review_20260512_0116.md` |
| Initial Ramsey measurement | Analysis of the completed Ramsey measurement and a note on the expected Fourier spectrum | The agent identified oscillations but left the T2star estimate and the attribution to 13C unresolved. | `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_terminal_review.json`, `work/notes/image231924_c01_ramsey_terminal_and_narrow_weak_podmr_decision_20260512_0311.md` |
| Narrow pODMR refresh | Narrow weak-pi review after Ramsey | The agent updated the resonance frequency to the measured scan point at `3.8761166667 GHz`. | `work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.json`, `work/notes/image231924_c01_narrow_weak_podmr_after_ramsey_review_20260512_0318.md` |
| Repeated Ramsey measurement | Terminal Ramsey raw export, drift, review, and figures after resonant frequency refinement | The agent used this measurement for its final report, estimated T2star at about `4 us`, and did not resolve coupling to an individual nearby 13C nucleus. | `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_review.json`, `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_review.png` |
| Closeout | Closeout note, TeX/PDF report, report build evidence | The agent marked the project objective as satisfied and planned no further measurements. | `work/notes/image231924_c01_corrected_center_ramsey_terminal_closeout_20260512_0520.md`, `summaries/closeout_20260512_0525.pdf`, `summaries/closeout_20260512_0525.tex` |

### Summary

The agent recovered from a failed acquisition, identified `c01` as aligned
with the magnetic field, and refined the resonance frequency before repeating
the Ramsey measurement. It estimated T2star at about `4 us` and did not resolve
coupling to an individual nearby 13C nucleus in that measurement.
