# NV Research Knowledge

Detailed NV experiment and OpenClaw operation knowledge. Read only the section
selected by `NV_RESEARCH_MEMORY.md`, current project state, evidence pointers,
or human advice. Keep project-specific raw history in project notes; keep this
file concise and reusable.

Treat this file as scientific memory and practice guidance, not a deterministic
checklist.

## Shared Literature

Section strength: `DEFAULT` for planning practice, `PROVENANCE` for sources.

- Shared literature lives at `<OPENCLAW_WORKSPACE>/literature/`.
  Start from `literature/INDEX.md` for local context, but do not treat local
  notes as a substitute for web literature search.
- For model choice, interpretation, experiment design, finding boundaries,
  measurement-condition design, or next-experiment selection, perform targeted
  web literature search before finalizing the decision. Prefer primary sources:
  papers, arXiv, publisher/DOI pages, and official datasets.
- For NV planning and experiment-result interpretation, especially
  Hamiltonian/coupling extraction, dynamical-decoupling spectroscopy, resonance
  assignment, and weak-signal follow-up, compare current evidence with relevant
  literature and this lab's past results before finalizing the next scientific
  decision or interpretation.
- Record search queries or source paths, papers/DOIs/arXiv ids when available,
  and decision-relevant takeaways in `work/state.md` or a linked `work/notes/`
  entry.
- Treat Tektronix AWG assumptions in old papers as historical. Current 23-C
  planning follows the current AWG manifests, bridge configuration, and MATLAB
  control path.

## Experiment Defaults

Section strength: mostly `DEFAULT`; interpretation caveats are `SOFT`.

- Choose comparison data by scientific relevance, hardware/control state,
  calibration context, and human guidance. Do not exclude data solely by age.
- Use `switch_delay = 100e-9` and `switch_tail_delay = 4e-9` by default when a
  sequence supports those variables.
- Use weak-pi pulsed ODMR to determine `mw_freq_hz`.
- Usable execute-backed weak-pi pulsed ODMR resonance evidence is normally
  valid for about 5 hours / 300 min unless drift/calibration/tracking evidence
  says otherwise. Keep this separate from fresh-position tracking horizons.
- For strong-pi pulsed ODMR, set `mod_depth = 1.0` and current-pi
  `length_rabi_pulse` explicitly.
- Do not put automatic fit requests such as `analysis.fit_kind` into ordinary
  bridge/batch jobs. Use terminal savedexperiment raw export plus plots as the
  first evidence handoff.
- When sweeping microwave frequency, the IQ mixer can leak unwanted microwave
  tones about `-15 dB` below the desired microwave tone, which may create weak
  spectral artifacts. Consider this before assigning weak features to NV
  resonance.
- In most default sequences, readout 1 is the `m_S = 0` reference. When an
  `m_S = +1/-1` reference is present, readout 2 is that reference and readout 3
  is the signal. When no `m_S = +1/-1` reference is present, readout 2 is the
  signal. Exceptions exist, so inspect the actual XML before interpreting
  readout roles. New sequences do not have to follow this convention.
- Keep candidate signal presence, physical interpretation, and derived
  parameter claims separate.
- Use weak-pi pulsed ODMR when a more accurate resonance frequency is needed.
  For weak-pi recalibration, use `length_rabi_pulse = 0.57 us` with
  `mod_depth = 0.1`. The pulsed-ODMR linewidth can be tuned by adjusting
  `mod_depth` and `length_rabi_pulse`.
- In this setup, several-hundred-kHz weak-pi pulsed ODMR center shifts can be
  routine because temperature can move the diamond/magnet relation.
- For new Hahn-echo baseline work, use `auto__cpmg` / `CPMG.xml` with `N = 1`
  rather than launching new `auto__echo` / `echo.xml` executes.
- For `CPMG.xml`, preserve/check boolean protocol variables such as
  `do_adiabatic_inversion`. Exact manual-protocol parity requires checking the
  actual bridge job, saved metadata, and sequence XML behavior.
- For pulse-sequence-dependent planning or interpretation, inspect the actual
  sequence XML and manifest: active instruction path, comments/disabled blocks,
  timing definitions, typed variables, boolean options, defaults, metadata
  forwarding, and terminal savedexperiment/result metadata when available.
- 2026-05-07 route-review lesson for electron Ramsey/T2star: at that time
  `auto__ramsey` / `ramsey.xml` separated `tau1` free evolution from `tau2`
  second-pulse phase, so a one-dimensional sweep of only one variable was not a
  clean T2star tau sweep. Provenance: project
  `nv23_aligned_nv_t2star_t2_20260507`, note
  `work/notes/conditional_t2star_t2_route_review_20260507_0833.md`.
- 2026-05-09 direct-chat repair: the MATLAB/23-C canonical `ramsey.xml` and
  validated manifest `auto__ramsey` were repaired back to a single `tau` active
  path using `ramsey(..., tau, det, ...)`; `auto__ramsey` now allows/defaults a
  one-dimensional `tau` scan again. Agents may use `auto__ramsey` for bounded
  Ramsey/T2star after the normal bridge gates, current resonance/tracking
  checks, and pre-execute validation. Re-check the live manifest/XML before
  execute if the file has changed. `auto__ramsey_with_echo` remains a usable
  alternate single-`tau` route when `tau <= tau_echo`.
- When a quantitative measurement cannot yield a reliable fitted value despite
  valid prerequisite signal evidence, assess whether better measurement
  conditions or higher data quality could make the result usable. If so,
  prefer a redesigned repeat with increased averages and/or scan points before
  abandoning the quantitative result. This guidance applies only after the
  target signal is established; do not use it to rescue a failed
  signal-presence.
- For weak-13C Hamiltonian work, phase-readout `XY8.xml` can be a low
  increment discriminator after magnitude-style CPMG becomes limited by
  conclusion strength. Use separate 1D settings for current manifests.
- DDRF-family work remains protocol-review-heavy: check RF sign/mixer semantics,
  `which_carb`, timing helpers such as `find_int_tdelay`, and route
  reachability before hardware.

## Drift, Tracking, And Environment

Section strength: mostly `PROVENANCE` / `SOFT`. Hard cases: tracking loss,
count collapse, hardware/safety uncertainty, discontinuous branch switch without
provenance, explicit fixed-position constraint, or explicit STOP.

- For usual NV/NV23 recovery, use the existing labeled imaging/tracking dataset
  as identity/seed evidence:
  `<NV_BRIDGE_ROOT>/status/openclaw_imaging/labeled_dataset_2026_03_12_onward/`.
  Useful files: `gold_labels.csv`, `image_index.csv`, `dataset_summary.json`,
  `README.md`, and `gold_overlays/`.
- Dataset evidence is not a hard gate. TrackCenter counts prove trackability,
  not usual-NV identity by themselves.
- If usual-NV identity matters after broken continuous provenance, ground the
  seed in dataset/pattern evidence or explicit visual reasoning before
  downstream target-specific experiments. If evidence conflicts, keep identity
  candidate-only or ask operator.
- Legacy live landmark-map matching is retired for future execution/recovery:
  `claw_find_nv_by_landmarks`, `claw_nv_landmark_map`, broad landmark retry, and
  `metadata.require_landmark_match=true`.
- Prefer explicit Imaging -> agent-visible candidate selection -> standalone
  TrackCenter -> sequence execution. Do not rely on hidden sequence pre-align as
  the primary target-selection mechanism.
- Plan per-average untracked windows at `<= 300 s` daytime and `<= 600 s`
  night. This is acquisition-planning guidance, not a GUI default change.
- For snake-ordered scans with stored averages, use even average counts by
  default and record any odd-count exception. Good drift does not justify
  exceeding the active per-average/tracking-window cap. If the runtime advisory
  exceeds the cap, revise before execute by reducing repetitions per average
  and/or scan points first; use a capped, shot-preserving average split only if
  it stays within the cap.
- When measurements from the last 1 hour have usable drift scores or
  scan-order-aware drift summaries, include them in acquisition planning along
  with the advisory and cite the evidence when it changes repetitions,
  averages, scan points, or tracking cadence.
- On drift, count collapse, TrackCenter failure, imaging-frame shift, or
  resonance shift, check TSP01 logs and record temp/RH deltas as provenance.
  Temperature correlation is evidence, not proof or a hard stop.
- After a successful TrackCenter, an experiment initial tracking/count-gate
  failure is drift/focus handoff provenance, not a blocker by itself; check
  TSP01 and retrack, or re-image.
- If continuous tracking and counts/alignment stay healthy, absolute position
  motion is not by itself a reason to stop, block, or request code changes.
- Tracking final kcps has ordinary scatter. Interpret it with rolling history,
  seed-to-tracked motion, final-count collapses, environment, and drift/SEM
  evidence.
- MATLAB Imaging GUI SavedImages store `ImageData` as count rate in `kcps`,
  not raw counts per pixel dwell. `claw_export_imaging_scan_for_python` writes
  `ImageData_YXZ` with `image_data_units = kcps`; `DwellTime` is acquisition
  provenance only. Do not divide `ImageData` or `ImageData_YXZ` by `DwellTime`
  to compare with TrackCenter `Final = ... kcps`.
- `HARD`: For MATLAB Imaging GUI SavedImages, `ImageData`/`ImageData_YXZ`
  values are already `kcps`. Do not compute `kcps = ImageData / DwellTime /
  1000`; that double-converts and can falsely reject bright NV candidates.
  If unit metadata is missing, inspect the MATLAB Imaging export path before
  making brightness/gate decisions.

## Shot Budget And Data Quality

Section strength: `DEFAULT` analysis practice plus `SOFT` interpretation
guidance. Hard blockers are aborted execution, missing data, collapsed
tracking/counts, wrong sequence/grid, hardware/safety uncertainty, or explicit
STOP.

- Count completed, nonfailed acquisition shots toward progress unless human
  advice or a hard failure requires stricter accounting.
- Use SEM/SEM-scaling for long acquisitions whose purpose is to improve
  statistics by accumulating more shots. Treat it as shot-accumulation and
  data-quality evidence.
- In this setup, stored averages often reflect tracking cadence as much as
  independent statistical repeats. Unless repetitions per average are large,
  average-to-average agreement is weak evidence and should not dominate signal
  presence or parameter interpretation. SEM scaling usually needs many stored
  averages or enough independent shots to become interpretable.
- 2026-05-09 image122341 c02 Ramsey lesson: if a bounded Ramsey scout completes
  safely but is non-claim-grade because the programmed phase-ramp component is
  not supported and an empirical T2* fit is unconstrained, do not claim T2* or
  nearby 13C from FFT peaks. A bounded repeat can be justified by increasing
  averages rather than repetitions when the per-average drift/tracking window is
  already near the advisory cap, and by changing only a provenance-backed
  resonance setting such as an alternate pODMR center supported by direct data
  review. If that repeat is still non-claim-grade, avoid blind repeats; choose a
  candidate branch or a targeted frequency/sequence diagnostic.
- Do not promote a numeric fit, optimizer success, extremum, or extracted
  parameter to a confirmed physical result until data shape has been reviewed.
  Use plots/images when the line shape, decay, oscillation, contrast, baseline,
  or outliers matter.
- 2026-05-13 savedexperiment raw-export lesson: do not assume
  `ExperimentDataEachAvg` axis order from array shape. For at least the running
  short-tau Ramsey autosave in project
  `nv23_aligned_nv_t2star_13c_image145844_20260513_1507`, the raw export shape
  behaved as `[scan, avg, readout, point]`; treating it as
  `[scan, readout, avg, point]` mislabeled per-average readouts. Before using
  per-average curves, SEM, or drift summaries from Python, verify the axis
  contract by checking that averaging the chosen per-average readout axis
  reproduces `ExperimentData`. Provenance: notes
  `work/notes/20260513_2346_shorttau_ramsey_3avg_autosave_refresh.md` and
  review script
  `work/artifacts/analysis/run_shorttau_autosave_3avg_review_20260513_2346.py`.
- 23-C defaults the first scan dimension to snake order. Use
  `analyze_savedexperiment_average_drift.m` for scan-order-aware drift analysis.
- Running-job recent-average drift is advisory under snake order. Do not stop or
  write `control.json` for drift alone; stop only for hard anomalies.
- 2026-05-11 c01 Ramsey repeat planning lesson: when an 8 us Ramsey/T2star
  scout needs to preserve FFT resolution for a ~2 MHz carrier plus ~0.4 MHz
  13C sideband but the advisory per-average tracking window is too long,
  first reduce tau points before increasing repetitions. In project
  `nv23_aligned_nvs_t2star_image001627_restart_20260511_0154`, changing
  101 points x 2 averages x 100000 reps to 51 points x 4 averages x 100000
  reps preserved the 8 us span and kept the candidate 2.436 MHz sideband
  below Nyquist, while the MATLAB advisory/initial status kept the
  per-average window under the 900 s nighttime cap. Treat this as a design
  pattern, not a universal recipe; re-run current advisory before execute.
- 2026-05-11 Ramsey FFT sampling guardrail: choose the deliberate Ramsey
  `det`, tau span, and point count together. For an 8 us span, 51 points gives
  Nyquist about 3.125 MHz, which can cover a 2 MHz carrier plus a ~0.38-0.40 MHz
  13C sideband but will alias the `auto__ramsey` default `det=5 MHz`; keeping
  `det=5 MHz` over the same span needs about 101 points or another grid with
  Nyquist above `det + f13C`. Recompute `f13C` from the actual weak-pi center
  and re-check advisory/drift caps before execute. Provenance: project
  `nv23_aligned_nvs_t2star_image111410_restart_20260511_1127`, note
  `work/notes/ramsey_t2star_fft_guardrail_20260511_1245.md`.

## OpenClaw Project Operation

Section strength: hard for queue/verifier/execute/state handoffs; default for
pacing, reporting, and bridge-free work.

- NV bridge jobs should be tracked and reported after enqueue by default.
- Route preflight:
  - New, changed, or route-unknown manifests: validate -> dry_run -> execute.
  - Validated route with documented same-route success: execute directly, or
    validate then execute when extra confidence is useful.
- Same-wake runnable work is the norm. After completing an item, continue into
  the next safe grounded task when policy and time allow.
- 2026-05-12 pODMR route/gate lesson: if a pODMR/Experiment route produces zero
  averages or no data because the in-run tracking/count gate reports low
  fluorescence, but standalone TrackCenter immediately before/after succeeds at
  high counts, do not treat the result as no-resonance evidence and do not
  blindly try more candidates or repeat pODMR. Record it as a route/count-gate
  issue, run at most a bounded standalone retrack diagnostic, then pause pODMR
  executes pending bridge-wrapper route review or a verified safe route-control
  path. Provenance: project
  `nv23_aligned_nv_t2star_13c_image150635_20260512_1506`, notes
  `work/notes/image150635_refresh1_c03_strong_podmr_failed_zeroavg_20260512_1654.md`
  and `work/notes/image150635_refresh1_c03_retrack_after_podmr_fail_20260512_1700.md`.
- 2026-05-12 follow-up from operator: in the same image150635 project, operator
  judged the pODMR count-gate behavior likely to be ordinary drift and advised
  not to require a bridge-wrapper code change right now. If similar evidence is
  otherwise compatible with drift, prefer fresh Imaging/re-image and resume from
  fresh image evidence before changing bridge-wrapper route controls. Keep normal
  bridge safety gates and do not bypass hardware/safety limits. Provenance:
  project `nv23_aligned_nv_t2star_13c_image150635_20260512_1506`,
  `human_advice.md` 2026-05-12T17:23 EDT, code-change rollback artifacts under
  `work/artifacts/code_changes/podmr_route_tracking_gate_review_20260512_1704/post_human_advice_rollback/`.
- During a healthy running execute, look for useful bridge-free work: completed
  or autosaved data analysis, model calculations, literature/PDF review,
  evidence-gap closure, figures, interpretation, and method notes.
- 2026-05-10 running-autosave lesson: bridge `status.json` can report
  `autosave_target_exists=false` when `runtime.autosave_target_path` omits the
  `.mat` suffix, even though the in-progress savedexperiment MAT exists under
  `savedexperiments/NV1`. When status says autosave is enabled and provides a
  `date_time`, check for `*<date_time>.mat` directly before concluding that no
  autosave is available. Provenance: project
  `nv23_aligned_nvs_t2star_image183006_20260510_183006`, note
  `work/notes/image183006_c02_ramsey_t2star_inprogress_autosave_20260510_2106.md`.
- Deterministic runtime monitors own routine progress/anomaly checks. Project
  cron should wake the agent for terminal transitions, anomalies, monitor
  errors, explicit bridge-free work, or low-frequency opportunity review.
- New NV projects use the simple research-state layout: `brief.md`,
  `work/state.md`, `work/notes/`, `work/bridge_jobs/`, and `.manager/`.
  WSL project state is canonical. Operational logs, advice inboxes, and
  generated artifacts may exist as support files, but they are not the
  research-plan surface.
- Do not read large history files in full by default. Use tail or targeted
  search on logs/ledger/evidence history.
- Process `advice/inbox` promptly. Human wording such as `STOP`,
  `do not continue`, `before continuing`, or `must first` should become an
  effective blocked next action or equivalent pending item before bridge work
  continues.
- Do not hand-compose queue commands with unquoted natural-language metadata.
  Prefer JSON submit specs or wrappers that pass argv lists.
- `verify-experiment-intent` requires parsing the JSON verdict before enqueue.
  Do not materialize jobs after a blocked verdict.
- Windows-side `.openclaw/projects` or ad hoc bridge jobs are scratch/migration
  signals. Import durable facts into the WSL project root before resuming
  autonomous work.
- Standalone Imaging/TrackCenter use
  `<OPENCLAW_WORKSPACE>/enqueue_nv_imaging_direct.py`. Sequence jobs
  use manifest-backed submit specs / batch execution.
- 2026-05-08 Imaging raw-export lesson: when MATLAB-loading saved
  `ConfocalScan` Imaging `.mat` artifacts from WSL for raw export or custom
  review, add both `Imaging` and `Imaging/Functions` from the active 23-C tree
  to the MATLAB path before `load(...)`. With only `root`, `claw`, and
  `experiment` paths, the object may load without numeric `ImageData`, causing
  `claw_normalize_scan_image_axes` to block with `Scan did not contain numeric
  ImageData.` Provenance: project
  `nv23_aligned_nv_t2star_t2_image234451_20260508_014317`, note
  `work/notes/image234451_rank04_transition_local_terminal_and_physical_check_20260508_1014.md`.
- 2026-05-08 direct-helper lesson: for
  `enqueue_nv_imaging_direct.py`, `--print-json` is preview-only and exits
  before writing to `queued/`, even when `--mode execute` is present. For real
  queue materialization, omit `--print-json` and verify that the stdout contains
  `ok: true` plus a `job_path` under the bridge queue. Provenance: project
  `nv23_aligned_nv_t2star_t2_image234451_20260508_014317`, wake around
  `work/notes/image234451_expand_imaging_track_failures_synthesis_20260508_0517.md`.
- 2026-05-08 sequence-direct execute lesson: for external
  `enqueue_nv_sequence_direct.py --mode execute` submissions, the wrapper may
  reject `--skip-measurement-plan` with `MEASUREMENT_PLAN_BYPASS_FORBIDDEN` and
  reject `--no-wait-for-result` with `MEASUREMENT_PLAN_REQUIRED`. In that
  route, use the managed single-item batch path with `--wait-for-result`; it
  runs the validation/advisory gates before queueing. A rejected wrapper call
  before enqueue does not by itself create a bridge job, but re-check project
  lifecycle and bridge idle before rerunning. Provenance: project
  `nv23_aligned_nv_t2star_t2_image102756_20260508_104319`, note
  `work/notes/image102756_expanded_rank02_track_passed_and_cw_plan_20260508_1306.md`.
- 2026-05-09 sequence-direct submit-spec lesson: when using
  `enqueue_nv_sequence_direct.py --submit-spec-json` directly, pass a single
  item/job spec, not the outer `nv_batch_run.py` batch spec with an `items`
  array. Passing the outer batch spec can fall back to helper defaults such as
  `odmr_cw_v1` and fail validation before enqueue (observed as
  `INVALID_SCAN: scan.vary_prop is required`). No bridge job is created by that
  pre-enqueue rejection; re-check project lifecycle and bridge idle, then retry
  with the extracted item spec. Provenance: project
  `nv23_aligned_nvs_t2star_image014057_20260509_015521`, note
  `work/notes/image014057_cand01_track_passed_strong_podmr_started_20260509_0221.md`.
- 2026-05-03 lesson: legacy
  `PulseSequencer/Functions/parsexml.m` can fail on otherwise usable sequence
  XML when MATLAB `%` comments contain multiple percent markers on a line; the
  observed wrapper failure was `Unable to parse XML file ... ODMR.xml` with
  MATLAB debug `Colon operands must be real scalars`. From a project wake, do
  not edit the legacy parser or GUI/hardware code for this. Prefer a staging
  manifest/XML clone that removes comments only, then run the normal
  staging-new route `validate -> dry_run -> execute`. Provenance:
  project `imaging_gui_tracked_nv_13c_hamiltonian_fresh_20260504_2320`, note
  `work/notes/cw_odmr_staging_rationale_20260503_2347.md`, staging manifest
  `current_gui_odmr_cw_sanitized_v1_20260503_2342`.
- 2026-05-07 follow-up: for `odmr_cw_v1` / `ODMR.xml`, bridge `validate` can
  pass while execute pre-enqueue advisory later fails on the legacy XML parser.
  Treat validate-only success as insufficient after this failure signature;
  use advisory and dry_run evidence for the sanitized staging route before
  execute. Provenance: project `nv23_aligned_nv_t2star_t2_20260507`, note
  `work/notes/candidate1_wide_cw_route_recovery_sanitized_xml_20260507_0206.md`,
  staging manifest `odmr_cw_sanitized_v1_20260507`.
- 2026-05-08 follow-up: the same legacy parsexml failure pattern can affect
  `auto__ramsey_with_echo` / `ramsey_with_echo.xml` during pre-enqueue advisory
  even though the validated manifest allows execute. Do not edit the parser or
  GUI from a project wake; create a comment-sanitized staging clone, preserve the
  active Ramsey/echo branch logic and boolean metadata, then run the normal
  staging-new `validate -> dry_run -> execute` route. For Ramsey/T2star, inspect
  that `tau <= tau_echo` keeps the XML on the plain Ramsey branch. Provenance:
  project `nv23_aligned_nv_t2star_t2_image102756_20260508_104319`, note
  `work/notes/image102756_expanded_rank04_ramsey_route_materialized_20260508_1442.md`,
  staging manifest `ramsey_with_echo_sanitized_v1_20260508`.
- Queue writers should create job directories under `staging/<job_id>__staging`
  and atomically move completed jobs to `queued/`.
- Completion marker JSON is required for every cron-triggered project wake; log
  or note updates do not release the inflight lock by themselves.
- Low-risk WSL-side analysis/orchestration edits may auto-resume after
  allowed-scope and passed-verification evidence. Keep human review for
  instrument drivers, legacy GUI, safety-policy edits, execute-gate changes, and
  manifest safety-limit changes.
- Preserve `bool_vars` through submit-spec, direct-plan, batch-item, bridge job,
  and saved-result paths when protocol depends on typed booleans.
- Execute approval usageunits are retired. Active execute gating is local lab
  opt-in, `metadata.queue_execute_opt_in=true`, validation, manifest/limit
  checks, and runtime safety gates.
- 2026-05-07 lesson: if a WSL `enqueue_nv_sequence_direct.py --wait-for-result`
  session is interrupted, the child `nv_batch_run.py` can survive and continue
  retrying according to its batch policy. Before launching another bridge job
  after an interrupted single-submit execute, check `ps`, bridge queued/running,
  and the single-submit state/control files; request stop through
  `nv_batch_control.py` and confirm bridge idle before killing or patching stale
  local audit state. Provenance: project
  `nv23_aligned_nv_t2star_t2_20260507`, notes
  `candidate7_targeted_podmr_retry_execute_failure_20260507_0623.md` and
  single-submit batch `nv23_pulsed_odmr_rabimodulated_v1_20260507_060251`.
- 2026-05-12 single-submit reconciliation lesson: before materializing a
  verified experiment intent, check recent bridge `done/` and `failed/` results
  for matching metadata/verified_intent_id as well as the intent directory. A
  stale verified intent can remain after a terminal bridge result if the local
  single-submit waiter or project state did not reconcile. In that case,
  complete the stale intent from the terminal bridge evidence instead of
  submitting a duplicate. If a duplicate local waiter is already stale after the
  bridge job is terminal and queued/running/staging are empty, request stop via
  `nv_batch_control.py`, confirm bridge idle, and only then terminate or patch
  local audit state. Provenance: project
  `nv23_aligned_nv_t2star_13c_image150635_20260512_1506`, note
  `work/notes/image150635_refresh2_c08_podmr_fail_and_retrack_queued_20260512_1858.md`.
- Use `project_lifecycle` for whether a project should run and
  `operational_state` for what an active project is waiting on. Treat legacy
  `status` fields as aliases.
- notification_service progress reports are separate reporting work. Reporter agents must
  not submit, stop, mutate bridge jobs, backlog, state, or lifecycle. Important
  images should be sent through `openclaw_notification_service_media_send.py`.
- 2026-05-07 STOP/cancel interpretation lesson: before treating
  `NVBridge:RunExperimentAborted` as a route/hardware/candidate failure, inspect
  the bridge `control.json` and live project lifecycle/state for a human
  STOP/cancel. If `control.json` shows `stop_requested=true` from direct chat,
  record the run as canceled/stopped, avoid physical or route conclusions from
  the incomplete data, cancel/supersede any queued next-step backlog, and do not
  continue autonomous work until explicit human resume. Provenance: project
  `nv23_aligned_nv_t2star_t2_image112001_20260507_123942`, note
  `work/notes/candidate4_reduced_wide_cw_failure_20260507_1318.md`.
- 2026-05-08 lifecycle-race lesson: after an experiment intent is verified but
  immediately before materializing any bridge job, re-read the current project
  lifecycle/cancellation fields as well as the bridge queue. Cancellation can
  arrive between verifier approval and enqueue; if `project_lifecycle/status` is
  canceled or `cancellation.do_not_resume` /
  `do_not_submit_or_mutate_bridge_queue` is true, do not submit, even when the
  verifier verdict and queue state were previously clear. If a race already
  submitted and the bridge job is stopped by direct-chat control, record it as a
  canceled/no-physical-conclusion run and do not retry without explicit human
  resume. Provenance: project
  `nv23_aligned_nv_t2star_t2_image234451_20260508_011426`, note
  `work/notes/image234451_rank07_current_cw_stopped_by_control_20260508_0141.md`.
- 2026-05-07 pODMR route-failure lesson: if `Rabimodulated.xml` /
  `pulsed_odmr_rabimodulated_v1` passes advisory/Setscan but execute fails before
  acquisition with `NVBridge:RunExperimentFailed`, MATLAB `badsubscript`, and
  `ExperimentFunctions.RunExperiment` at `obj.Std_dev{q}`, treat it as a
  bridge/legacy Experiment GUI route failure, not candidate resonance evidence.
  Do not auto-retry no-agent-recovery candidate screens; request stop through
  the single-submit control, confirm bridge queued/running are empty before
  terminating stale local wait processes, and block further bridge work on GUI
  reset/route inspection or explicit safe resume. Provenance: project
  `nv23_aligned_nv_t2star_t2_image112001_20260507_132134`, note
  `work/notes/candidate12_cw_terminal_and_podmr_route_failure_20260507_1908.md`,
  failed bridge job
  `nv23_pulsed_odmr_rabimodulated_v1_20260507_190014_pulsed_odmr_rabimodulated_v1`.
- 2026-05-11 pODMR incomplete-run lesson: if `Rabimodulated.xml` /
  `pulsed_odmr_rabimodulated_v1` passes validation, Setscan, and the local
  execute gate but `RunExperiment(handles)` returns after a short time with
  `NVBridge:RunExperimentIncomplete`, empty `data_path`, no new
  savedexperiment, and no populated `ExperimentalScan.ExperimentData`, do not
  treat it as candidate resonance or alignment evidence. If the bridge reports
  `summary.run_experiment.incomplete_kind =
  in_run_tracking_or_low_fluorescence_gate_failure`, treat it first as an
  in-experiment TrackCenter/count-gate failure: re-check standalone
  TrackCenter/current counts for the same candidate, then retry or move to the
  next candidate from that evidence. Escalate to GUI/route reset or inspection
  only when there is independent route/hardware uncertainty, repeated
  incomplete runs, or counts/GUI state cannot be recovered. Provenance:
  project `nv23_aligned_nvs_t2star_image111410_restart_20260511_1127`, note
  `work/notes/image111410_c01_strong_podmr_execute_failure_20260511_1152.md`,
  failed bridge job
  `nv23_pulsed_odmr_rabimodulated_v1_20260511_114800_image111410_c01_strong_podmr`.

## Research Practice And Closeout

Section strength: `DEFAULT`.

- Non-experiment findings can change experiment design. After analysis,
  literature review, simulation, code/tooling work, or evidence-gap closure,
  record whether the insight changes hypotheses, parameters, safety gates,
  inclusion/exclusion rules, analysis plan, stopping criteria, or next steps.
- Keep Current Findings updated after meaningful evidence review, terminal
  result, model comparison, or bridge-free synthesis. Record evidence-backed
  findings even when final physical interpretation is not settled.
- Before marking a project complete, paused after line-complete, stopped,
  disabled, or otherwise inactive, produce a detailed LaTeX closeout report with
  figures unless one already reflects the final evidence state.
- When reviewing latest evidence, include relevant manual experiments as well as
  Claw-launched jobs, especially for calibration, resonance, and T2-family
  baseline decisions.
