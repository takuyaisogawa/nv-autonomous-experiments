# Fine weak-pi pODMR terminal review

Question: did the fine weak-pi pODMR refine the usable Ramsey microwave frequency for accepted r03?

Inputs read:
- Terminal bridge result/status/job copied into `work/bridge_jobs/`.
- Raw savedexperiment export: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_raw_export_20260513_2031.json`.
- Scan-order-aware drift diagnostic: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_drift_20260513_2031.json`.
- Active `Rabimodulated.xml`, inspected this wake for readout roles.

Action taken:
- Completed experiment intent `image145844_reimage_r03_fine_weak_podmr_20260513_1950` after terminal result.
- Reviewed raw readouts, point-wise signal/reference, fitted-reference-line normalization, per-average minima, and drift flags.

Result:
- Job completed safely with final counts 39.424 kcps, 4 averages x 50000 repetitions.
- Combined raw signal, point-wise ratio, and fitted-reference-line normalization all minimize at 3.8759000 GHz.
- Raw signal drop at the selected grid point is 11.9% vs edge median; fitted-reference-line-normalized drop is 11.9%.
- Per-average raw minima are [3876000000, 3875900000, 3875900000, 3876000000] Hz, split between 3.8759 and 3.8760 GHz.
- Drift diagnostic flags no averages; scan-order source is `Scan.ScanOrderEachAvg` / `snake`.

Checks actually performed:
- `tools_mat_parse.py --pretty` raw export completed successfully.
- `analyze_savedexperiment_average_drift_mat_files(..., drop_threshold=0.15)` completed successfully.
- Readout roles were checked from XML: readout1 is mS=0 reference and readout2 is post-rabi-pulse signal when `full_expt=0`.

Remaining uncertainty:
- The selected center is grid-supported at 0.1 MHz spacing; do not claim sub-grid precision.
- Fine pODMR tightens `mw_freq` but does not by itself explain why the first Ramsey scout's strongest exploratory frequency was near 0.884 MHz rather than the programmed 1.5 MHz carrier.

Next pointer:
- Use `mw_freq_hz = 3875900000` for the redesigned Ramsey/T2star follow-up. The Ramsey plan should remain raw/readout-aware and should treat fits/FFT peaks as claim-grade only after signal presence and average consistency are supported.

Artifacts:
- `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031.json`
- `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_fine_weak_podmr_raw_review_20260513_2031.png`
