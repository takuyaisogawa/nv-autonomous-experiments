# 2026-05-14 01:07 short-tau Ramsey 10-average autosave refresh

## Question

While the short-tau/high-SNR r03 Ramsey diagnostic is still running, is there any hard anomaly in the latest autosave, and what nonterminal context should be preserved for terminal review?

## Inputs read

- Live bridge status: `<NV_BRIDGE_ROOT>/running/nv23_ramsey_20260513_230331_auto_ramsey/status.json`
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`
- Raw export: `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_10avg_raw_export_20260514_0107.json`
- Review JSON: `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_autosave_10avg_review_20260514_0107.json`
- Status snapshots: `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_status_snapshot_20260514_0107.json` and `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_status_snapshot_20260514_0117.json`
- Figure: `work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_10avg_review_20260514_0107.png`

## Action taken

- Confirmed the bridge had one running job (`nv23_ramsey_20260513_230331_auto_ramsey`), no queued jobs, and no monitor error or stop request.
- Raw-exported the in-progress autosave after 10 stored averages were available.
- Re-ran the same raw/readout-aware autosave review used for earlier partial checks, including raw reference/signal, point-wise signal/reference, signal over fitted reference line, per-average signal traces, target LS/FFT screens, and an exploratory all-frequency LS screen.
- Took a later live-status snapshot after the job advanced to 11/12 averages.

## Result

- The raw export contains 10/12 stored averages, 41 tau points from 48 ns to 1.968 us, snake scan order, and 90,000 repetitions per stored average: 900,000 shots per tau point so far.
- The 10-average status snapshot was healthy: state `running`, phase `run_experiment_scan_point`, message `(10/12) averages completed`, final-count text `Final = 42.469 kcps`, monitor `last_error` empty, and `stop_requested=false`.
- A later 01:17 status snapshot had advanced to 11/12 averages with final-count text `Final = 35.122 kcps`, monitor `last_error` still empty, and `stop_requested=false`. This is a count decrease but not a hard anomaly or count collapse under the current threshold.
- Median signal SEM across tau points was about `1.06 kcps` at 10 averages.
- The early-time signal/ratio transient persisted: first-0.75-us raw-signal peak-to-peak about `6.42 kcps`, ratio peak-to-peak about `0.119`.
- The exploratory all-tau ratio LS screen remained strongest near `1.187 MHz` (ratio amplitude about `0.0381`; raw-signal LS amplitude near the programmed carrier was about `1.41 kcps`).
- Target amplitudes remain nonterminal context only: programmed `1.0 MHz` carrier ratio amplitude about `0.0289`; expected 13C sidebands at `0.615 MHz` and `1.385 MHz` have ratio amplitudes about `0.0261` and `0.0276`.

## Checks performed

- Verified raw export shape `ExperimentDataEachAvg = (1, 10, 2, 41)` and that per-average means reconstruct combined `ExperimentData` under the savedexperiment axis contract `[scan, avg, readout, point]`.
- Captured current live status snapshots in the project artifacts and refreshed the running job status/control copies in `work/bridge_jobs/`.
- Produced a review figure in `work/artifacts/figures/image145844_reimage_r03_ramsey_shorttau_autosave_10avg_review_20260514_0107.png`.

## Remaining uncertainty

This is still an in-progress autosave review. It does not support a T2star or 13C claim before terminal raw export, scan-order-aware drift review, and final raw/readout-aware carrier/decay analysis. The 11/12 count decrease should be checked in terminal status and drift/environment provenance, but by itself it is not a stop condition.

## Next pointer

Continue monitoring the running job. On terminal completion, copy terminal bridge artifacts and batch state, complete verified intent `image145844_reimage_r03_ramsey_shorttau_48ns_1968ns_12x90k_20260513_2257`, raw-export the final savedexperiment, run scan-order-aware drift, and then decide whether raw/readout-aware signal presence supports a T2star fit or 13C sideband conclusion.
