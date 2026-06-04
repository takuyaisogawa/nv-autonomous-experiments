# NV Research Knowledge Excerpt

This file contains representative public excerpts from the reusable NV research
knowledge used by the project-execution agent. It is not the complete live knowledge file. Full
wake-local copies are preserved in the case wake records.

The purpose of this excerpt is to show the kind of reusable lessons that the
agent accumulates and reuses across project wakes.

## Shared Literature

Section strength: `DEFAULT` for planning practice, `PROVENANCE` for sources.

- For model choice, interpretation, experiment design, finding boundaries,
  measurement-condition design, or next-experiment selection, perform targeted
  literature search before finalizing the decision. Prefer primary sources:
  papers, arXiv, publisher/DOI pages, and official datasets.
- For NV planning and experiment-result interpretation, especially Hamiltonian
  or coupling extraction, dynamical-decoupling spectroscopy, resonance
  assignment, and weak-signal follow-up, compare current evidence with relevant
  literature and this lab's past results before finalizing the next scientific
  decision or interpretation.
- Record search queries or source paths, papers/DOIs/arXiv ids when available,
  and decision-relevant takeaways in `work/state.md` or a linked `work/notes/`
  entry.
- Treat old hardware assumptions in old papers as historical. Current planning
  follows the active manifests, bridge configuration, and MATLAB control path.

## Experiment Defaults

Section strength: mostly `DEFAULT`; interpretation caveats are `SOFT`.

- Choose comparison data by scientific relevance, hardware/control state,
  calibration context, and human guidance. Do not exclude data solely by age.
- Use weak-pi pulsed ODMR to determine `mw_freq_hz`.
- Use strong-pi pulsed ODMR as a resonance-presence/alignment screen, but keep
  it separate from precision center claims.
- Do not put automatic fit requests such as `analysis.fit_kind` into ordinary
  bridge/batch jobs. Use terminal savedexperiment raw export plus plots as the
  first evidence handoff.
- When sweeping microwave frequency, the IQ mixer can leak unwanted microwave
  tones below the desired microwave tone, which may create weak spectral
  artifacts. Consider this before assigning weak features to NV resonance.
- Readout roles are sequence-dependent. Inspect the actual XML before
  interpreting reference/signal channels.
- Keep candidate signal presence, physical interpretation, and derived
  parameter claims separate.
- For pulse-sequence-dependent planning or interpretation, inspect the actual
  sequence XML and manifest: active instruction path, comments/disabled blocks,
  timing definitions, typed variables, boolean options, defaults, metadata
  forwarding, and terminal savedexperiment/result metadata when available.
- When a quantitative measurement cannot yield a reliable fitted value despite
  valid prerequisite signal evidence, assess whether better measurement
  conditions or higher data quality could make the result usable. This guidance
  applies only after the target signal is established.

## Drift, Tracking, And Environment

Section strength: mostly `PROVENANCE` / `SOFT`. Hard cases include tracking
loss, count collapse, hardware/safety uncertainty, discontinuous branch switch
without provenance, explicit fixed-position constraint, or explicit STOP.

- Dataset evidence can inform identity and seed choice, but it is not a hard
  gate. TrackCenter counts prove trackability, not identity by themselves.
- Prefer explicit Imaging -> agent-visible candidate selection -> standalone
  TrackCenter -> sequence execution. Do not rely on hidden sequence pre-align
  as the primary target-selection mechanism.
- For snake-ordered scans with stored averages, use even average counts by
  default and record any odd-count exception.
- When recent measurements have usable drift scores or scan-order-aware drift
  summaries, include them in acquisition planning along with advisory runtime
  estimates and cite the evidence when it changes repetitions, averages, scan
  points, or tracking cadence.
- Temperature correlation is evidence, not proof or a hard stop.
- After a successful TrackCenter, an experiment initial tracking/count-gate
  failure is drift/focus handoff provenance, not a blocker by itself.
- If continuous tracking and counts/alignment stay healthy, absolute position
  motion is not by itself a reason to stop, block, or request code changes.
- MATLAB Imaging GUI SavedImages store image values as count rate in `kcps`.
  Do not double-convert image values when comparing with TrackCenter counts.

## Shot Budget And Data Quality

Section strength: `DEFAULT` analysis practice plus `SOFT` interpretation
guidance. Hard blockers are aborted execution, missing data, collapsed
tracking/counts, wrong sequence/grid, hardware/safety uncertainty, or explicit
STOP.

- Count completed, nonfailed acquisition shots toward progress unless human
  advice or a hard failure requires stricter accounting.
- Use SEM/SEM-scaling for long acquisitions whose purpose is to improve
  statistics by accumulating more shots.
- Stored averages often reflect tracking cadence as much as independent
  statistical repeats. Unless repetitions per average are large, average-to-
  average agreement is weak evidence and should not dominate signal presence or
  parameter interpretation.
- Do not promote a numeric fit, optimizer success, extremum, or extracted
  parameter to a confirmed physical result until data shape has been reviewed.
  Use plots/images when line shape, decay, oscillation, contrast, baseline, or
  outliers matter.
- Running-job recent-average drift is advisory under snake order. Do not stop
  a job for drift alone; stop only for hard anomalies.
- Choose Ramsey `det`, tau span, and point count together. Recompute expected
  sideband locations from the actual resonance center and re-check advisory and
  drift limits before execute.

## Project Operation

Section strength: hard for queue/verifier/execute/state handoffs; default for
pacing, reporting, and bridge-free work.

- Route preflight: new, changed, or route-unknown manifests should go through
  validate -> dry_run -> execute. Validated routes with documented same-route
  success may execute directly, or validate first when extra confidence is
  useful.
- Same-wake runnable work is the norm. After completing an item, continue into
  the next safe grounded task when policy and time allow.
- During a healthy running execute, do useful bridge-free work when grounded:
  analysis, model calculations, literature/PDF review, evidence-gap closure,
  figures, interpretation, and method notes.
- Deterministic runtime monitors own routine progress/anomaly checks. Project
  wakes should focus on terminal transitions, anomalies, evidence synthesis,
  planning, and closeout.
- Keep bridge-execution contracts in JSON and scientific interpretation in
  Markdown state/notes.

## Research Practice And Closeout

Section strength: `DEFAULT` for synthesis and closeout.

- After meaningful evidence review, terminal results, model comparison, or
  bridge-free synthesis, update current findings with what is supported, useful
  for the next decision, downgraded, unresolved, and what evidence would change
  the finding.
- A closeout should state claim boundaries explicitly: what is supported, what
  is candidate-only, what is negative, and what follow-up would be needed to
  change the conclusion.
- Reusable lessons belong in the knowledge file with a short dated note and a
  provenance pointer. Project-specific raw history belongs in project notes.
