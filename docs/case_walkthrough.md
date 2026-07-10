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

Objective: find a magnetic-field-aligned NV from `image172647`, then obtain a
well-supported T2star and 13C conclusion.

Main entry points:

- Case README: `cases/image172647/README.md`
- Project state: `cases/image172647/project/work/state.md`
- Evidence ledger: `cases/image172647/project/.manager/evidence.jsonl`
- Recovered raw data: `cases/image172647/project/data_recovered_20260515/matlab_23C/`
- Closeout report: `cases/image172647/project/work/reports/closeout_20260515_1225/nv23_image172647_closeout_report_20260515.pdf`

### Agent Timeline

| Stage | Agent read | Agent decision | Artifact trail |
| --- | --- | --- | --- |
| Initial image audit | Saved image `3DXYZ-Image-2026-05-14-172647.mat` and candidate ranking | Select the first candidate, but require standalone tracking and pODMR before alignment claims | `work/artifacts/image172647_candidates/`, `work/notes/image172647_initial_candidate_selection_and_c01_track_20260514_1736.md` |
| Stale-candidate recovery | Initial c01 TrackCenter success, failed pODMR execute, failed retrack | Treat the failed pODMR as low-count/freshness evidence, not no-resonance evidence; re-image the original region | `work/artifacts/recovery/`, `work/artifacts/bridge_results/` |
| Fresh re-image | New imaging result and candidate ranking | Use the fresh image frame and test `reimage1804_c01`, then `reimage1804_c02` | `work/artifacts/image172647_reimage1804_candidates/`, `work/artifacts/figures/image172647_reimage1804_candidate_peaks_20260514_1812.png` |
| Reject `reimage1804_c01` | TrackCenter and terminal strong-pi pODMR review | Reject c01 because healthy-count pODMR showed no clear usable resonance and only weak depressions relative to expected contrast | `work/artifacts/analysis/reimage1804_c01_podmr_terminal_summary_4avg_20260514_1859.json`, `work/notes/reimage1804_c01_podmr_terminal_review_reject_20260514_1900.md` |
| Accept `reimage1804_c02` | TrackCenter plus terminal strong-pi pODMR | Accept c02 as the aligned branch: clear signal-only resonance near 3.875 GHz, with lower-than-reference contrast caveat | `work/artifacts/analysis/reimage1804_c02_podmr_terminal_summary_4avg_20260514_1957.json`, `work/notes/reimage1804_c02_podmr_terminal_review_accept_20260514_1959.md` |
| Ramsey scout | Initial det=1.5 MHz Ramsey terminal review | Support a weak empirical oscillation and short/few-us T2star order, but do not establish 13C or a final scalar | `work/artifacts/analysis/reimage1804_c02_ramsey_terminal_8avg_summary_20260514_2150.json`, `work/artifacts/figures/reimage1804_c02_ramsey_terminal_8avg_20260514_2150.png` |
| Weak-pi center refinement | Weak-pi pODMR terminal review | Refine the working center to `3.876501337 GHz`; rule out a large electron-resonance mis-centering explanation for the earlier high-frequency Ramsey component | `work/artifacts/analysis/reimage1804_c02_weak_pi_podmr_terminal_4avg_summary_20260514_2251.json`, `work/artifacts/figures/reimage1804_c02_weak_pi_podmr_terminal_4avg_20260514_2251.png` |
| det=1.0 Ramsey discriminator | Terminal 16-average det=1.0 MHz Ramsey | Support short/few-us T2star order and leave a weak det+13C-compatible candidate, but do not establish 13C from Ramsey alone | `work/artifacts/analysis/reimage1804_c02_ramsey_det1_terminal_summary_16avg_20260515_0245.json`, `work/artifacts/figures/reimage1804_c02_ramsey_det1_terminal_16avg_20260515_0245.png` |
| det=1.25 Ramsey discriminator | Third-detuning model, autosave trends, terminal 16-average review | Strengthen the weak det-shift-consistent candidate and weaken static/old-high alternatives, but keep Ramsey-only 13C below claim grade | `work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_terminal_summary_16avg_20260515_0645.json`, `work/artifacts/figures/reimage1804_c02_ramsey_det1p25_terminal_16avg_20260515_0645.png` |
| CPMG N=8 follow-up | Non-blind CPMG model based on the weak-pi center and 13C Larmor estimate | Use a different protocol to test the weak candidate; terminal target-region dip corroborates a weak/moderate nearby-13C-like feature | `work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_target_region_review_20260515_0945.json`, `work/artifacts/figures/reimage1804_c02_cpmg_n8_terminal_target_region_20260515_0945.png` |
| Closeout | Closeout report bundle and final state | Mark the original objective satisfied; no more bridge work by default | `work/reports/closeout_20260515_1225/`, `summaries/nv23_image172647_closeout_report_20260515.pdf` |

### Final Case Reading

The case shows the strongest autonomous hypothesis-discrimination path in this
release: stale-candidate recovery, pODMR-based rejection and acceptance,
weak-pi center refinement, multi-detuning Ramsey, and a different-protocol CPMG
follow-up. Final reading: aligned `reimage1804_c02` found; T2star is
short/few-us order, about `2-3 us` but method-sensitive; 13C evidence supports
a likely weak/moderate nearby-13C-like signature, without precise coupling
extraction or a publication-grade single-spin claim.

## image145844

Objective: find a magnetic-field-aligned NV from `image145844`, then obtain a
well-supported T2star and 13C conclusion.

Main entry points:

- Case README: `cases/image145844/README.md`
- Project state: `cases/image145844/project/work/state.md`
- Evidence ledger: `cases/image145844/project/.manager/evidence.jsonl`
- Recovered raw data: `cases/image145844/project/data_recovered_20260514/matlab_23C/`

### Agent Timeline

| Stage | Agent read | Agent decision | Artifact trail |
| --- | --- | --- | --- |
| Initial image audit | Original `image145844` export and candidate selection outputs | Treat the image export as valid only after checking axis/units; select initial candidate `r01` | `work/artifacts/analysis/image145844_raw_export_20260513_1509.json`, `work/artifacts/analysis/image145844_candidate_selection_20260513_1509.json` |
| `r01` failure handling | TrackCenter success, failed pODMR, failed retrack | Do not reject `r01` for no resonance because the pODMR did not acquire useful resonance data after count collapse | `work/notes/20260513_1546_r01_count_collapse_reimage.md`, `work/bridge_jobs/` |
| Re-image and candidate refresh | Fresh imaging export with explicit axis permutation and new candidate list | Use the fresh image frame and choose new candidates `r01`, `r02`, `r03` | `work/artifacts/analysis/image145844_reimage_raw_export_20260513_1548.json`, `work/artifacts/analysis/image145844_reimage_candidate_selection_20260513_1550.json` |
| Reject fresh `r01` | Fresh `r01` TrackCenter and strong-pi pODMR raw/readout review | Trackable is not enough; no clear usable resonance, so do not plan Ramsey on `r01` | `work/artifacts/analysis/image145844_reimage_r01_strong_podmr_raw_review_20260513_1615.json`, `work/notes/20260513_1629_reimage_r01_r02_alignment_progress.md` |
| Reject fresh `r02` | Fresh `r02` TrackCenter and strong-pi pODMR raw/readout review | No clear usable resonance; reject `r02` for alignment selection for now | `work/artifacts/analysis/image145844_reimage_r02_strong_podmr_raw_review_20260513_1658.json`, `work/notes/20260513_1709_r02_review_and_r03_track.md` |
| Accept `r03` as aligned | Fresh `r03` TrackCenter plus strong-pi pODMR terminal review | Accept `r03` as first magnetic-field-aligned candidate because raw signal, ratio, and reference-line-normalized views agree at the resonance grid point | `work/artifacts/analysis/image145844_reimage_r03_strong_podmr_raw_review_20260513_1741.json`, `work/notes/20260513_1808_r03_acceptance_and_weak_podmr_start.md` |
| Refine resonance center | Weak-pi and fine weak-pi pODMR reviews | Use grid-supported microwave centers for Ramsey planning without claiming sub-grid precision | `work/artifacts/analysis/image145844_reimage_r03_weak_podmr_raw_review_20260513_1838.json`, `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031.json` |
| First Ramsey scout | Ramsey terminal raw export, FFT review, drift review | Data are analyzable, but spectral content is not claim-grade for T2star or 13C | `work/artifacts/analysis/image145844_reimage_r03_ramsey_t2star_raw_fft_review_20260513_1930.json`, `work/notes/20260513_1958_weak_podmr_review_and_ramsey_start.md` |
| Non-blind Ramsey follow-ups | Second long-span Ramsey, short-tau/high-SNR diagnostic, det-shift diagnostic | Change measurement conditions to test failure modes; do not promote ambiguous components into claims | `work/artifacts/analysis/`, `work/notes/20260513_2220_second_ramsey_terminal_review.md`, `work/notes/20260514_0200_shorttau_terminal_review_and_detshift_start.md` |
| pODMR refresh | Fine weak-pi pODMR refresh after det-shift branch | Refresh `mw_freq_hz` before final long-span Ramsey; treat pODMR refresh as calibration only | `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_20260514_0523.json`, `work/notes/20260514_0540_podmr_refresh_review_and_refreshed_center_ramsey_design.md` |
| Final refreshed-center Ramsey | 20-average refreshed-center Ramsey terminal review and model comparison | Under fixed-carrier interpretation, no unconditional numeric T2star and no fixed 13C sideband claim | `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json`, `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.json` |
| Bridge-free reanalysis | Human advice requesting Ramsey frequency reanalysis, final Ramsey data, bootstrap/model comparison | Revise the Ramsey frequency interpretation after considering a residual calibration offset; do not touch the bridge | `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_20260514_1308.json`, `work/artifacts/analysis/image145844_reimage_r03_shifted_triplet_targeted_bootstrap_20260514_1312.json` |
| Closeout | Revised closeout report and work note | Stop automatic bridge work; preserve conservative claim boundaries | `work/artifacts/reports/20260514_1320_r03_shifted_sideband_recloseout/image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.pdf`, `work/notes/20260514_1320_shifted_sideband_reanalysis_and_recloseout.md` |

### Final Case Reading

The case shows iterative candidate selection and rejection, explicit separation
between tracking evidence and resonance evidence, non-blind follow-up design
after ambiguous Ramsey data, and a bridge-free interpretation update. The final
claim boundary is deliberately conservative: aligned `r03` found; no
unconditional claim-grade numeric T2star; revised Ramsey frequency
interpretation after considering a residual calibration offset, without an
independently confirmed nearby-13C coupling claim.

## image231924

Objective: find a magnetic-field-aligned NV from `image231924`, then obtain a
well-supported T2star and 13C conclusion.

Main entry points:

- Case README: `cases/image231924/README.md`
- Project state: `cases/image231924/project/work/state.md`
- Evidence ledger: `cases/image231924/project/.manager/evidence.jsonl`
- Raw/data copy: `cases/image231924/project/data_git_20260512/`

### Agent Timeline

| Stage | Agent read | Agent decision | Artifact trail |
| --- | --- | --- | --- |
| Initial image audit | Source image export and candidate list | Select `image231924_c01`; treat TrackCenter as trackability evidence only | `work/artifacts/analysis/image231924_candidate_list.json`, `work/notes/image231924_candidate_selection_20260511_2324.md` |
| First pODMR failure | Failed first strong-pi pODMR result and TrackCenter recheck | Do not treat the failed acquisition as spectroscopy evidence; re-establish trackability first | `work/bridge_jobs/`, `work/state.md` evidence pointers |
| Strong-pi pODMR retry | Retry bridge result and raw/readout-aware pODMR review | Alignment screen passes with visible resonance near `3.879 GHz`; not a precision center claim | `work/artifacts/analysis/image231924_c01_strong_podmr_retry1_review.json`, `work/notes/image231924_c01_strong_podmr_retry1_review_20260512_0038.md` |
| Weak-pi pODMR | Weak-pi pODMR result and review | Use a grid/noise-limited microwave center for Ramsey planning | `work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json`, `work/notes/image231924_c01_weak_podmr_review_20260512_0116.md` |
| Ramsey scout | First Ramsey terminal review and FFT expectation note | Real oscillatory signal exists, but T2star and 13C remain candidate-only | `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_terminal_review.json`, `work/notes/image231924_c01_ramsey_terminal_and_narrow_weak_podmr_decision_20260512_0311.md` |
| Narrow pODMR refresh | Narrow weak-pi review after Ramsey | Supersede the first center with `3.8761166667 GHz` grid-scale center | `work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.json`, `work/notes/image231924_c01_narrow_weak_podmr_after_ramsey_review_20260512_0318.md` |
| Corrected-center Ramsey | Terminal corrected-center Ramsey raw export, drift, review, figures | Use this as the closeout dataset; T2star scale about `4 us`, no resolved nearby 13C | `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_review.json`, `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_review.png` |
| Closeout | Closeout note, TeX/PDF report, report build evidence | Project objective satisfied; no more autonomous bridge work by default | `work/notes/image231924_c01_corrected_center_ramsey_terminal_closeout_20260512_0520.md`, `summaries/closeout_20260512_0525.pdf`, `summaries/closeout_20260512_0525.tex` |

### Final Case Reading

The case shows a shorter successful path: recovery from an invalid first
acquisition, pODMR-based alignment, center refinement before Ramsey, terminal
Ramsey closeout, and a clear distinction between a positive T2star scale and a
negative nearby-13C claim. Final reading: aligned `c01` found; T2star scale
about `4 us`; no resolved nearby 13C coupling in the corrected-center dataset.
