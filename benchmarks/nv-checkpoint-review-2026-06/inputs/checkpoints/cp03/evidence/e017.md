# Short-tau/high-SNR r03 Ramsey diagnostic design and start

Question: after two non-claim-grade r03 Ramsey datasets, is a non-blind follow-up still justified, and if so what should it test?

Inputs read:
- Terminal second Ramsey review: `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.json`.
- Prior first Ramsey review and fine pODMR center pointers from `work/state.md`.
- Live `auto__ramsey` manifest, `ramsey.xml`, and `AWG/ramsey.m` protocol basis.
- `NV_RESEARCH_MEMORY.md` and relevant `NV_RESEARCH_KNOWLEDGE.md` sections on experiment defaults and shot budget/data quality.
- MATLAB preview/advisory response: `.openclaw/matlab_bridge_requests/submit_spec_20260513_225937_wff0eauv/response.json`.

Action taken:
- Designed a short-tau/high-SNR Ramsey diagnostic on accepted r03 rather than another blind 8 us repeat.
- Wrote quantitative model/advisory artifact `work/artifacts/analysis/image145844_reimage_r03_ramsey_shorttau_model_plan_20260513_2257.json`.
- Wrote submit spec `work/bridge_jobs/image145844_reimage_r03_ramsey_shorttau_48ns_1968ns_12x90k_submit_spec_20260513_2257.json`.
- Queued and verified experiment intent `image145844_reimage_r03_ramsey_shorttau_48ns_1968ns_12x90k_20260513_2257`.
- Submitted the execute through the managed single-item batch path.

Result:
- Intended running bridge job: `nv23_ramsey_20260513_230331_auto_ramsey`.
- Batch id: `nv23_ramsey_20260513_230232`.
- The bridge job id has a generic suffix because the first launch reached the queue before a descriptive relaunch was stopped; the job metadata links it to the verified short-tau intent and contains the full descriptive target role.
- Measurement settings: `auto__ramsey`, `tau=48 ns..1.968 us` in 41 sample-grid points, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` repetitions, explicit r03 position.
- MATLAB preview/advisory had no blockers. Preview estimated `577.339 s` per average under the active `900 s` nighttime cap; live runtime status after start estimated `652.339 s` per average and `7853.071 s` total, still under the nighttime cap.
- Running status at copy time: average `1/12`, final-count text `44.184 kcps`, monitor `last_error` empty, no stop request.

Duplicate cleanup:
- A descriptive-suffix relaunch also queued duplicate job `nv23_ramsey_20260513_230511_image145844_reimage_r03_ramsey_shorttau_48ns_1968ns_12x90k` after the generic job had already started.
- To prevent duplicate acquisition, that duplicate was canceled before execution by writing a stop control and moving it from bridge `queued/` to `canceled/` with `cancellation_note.json`.
- Current bridge state after cleanup: queued empty; running contains only `nv23_ramsey_20260513_230331_auto_ramsey`.

Checks actually performed:
- Intent verifier returned `verdict=verified` with bridge queued/running empty before the first submission.
- MATLAB preview/advisory returned `ok=true`, validation ok, no blockers.
- Running job `job.json` was inspected to confirm it matches the intended short-tau scan/spec despite the generic suffix.
- Bridge queue was inspected after duplicate cleanup.

Remaining uncertainty:
- This diagnostic can test early-time carrier visibility and a very-short-T2star failure mode, but it is not itself terminal until the savedexperiment is complete and raw/readout-aware review is done.
- The short span is not intended as a high-resolution 13C sideband measurement. If a carrier/decay appears, a later longer/high-quality measurement may be needed for 13C. If no carrier appears, avoid further blind Ramsey repeats on r03.

Next pointer:
- While the job is running, treat autosave reviews as anomaly/progress evidence only.
- At terminal completion, copy bridge artifacts, complete the intent, raw-export final savedexperiment, run scan-order-aware drift analysis, and review raw/readout-aware short-tau carrier/decay before fitting T2star or making a 13C conclusion.
