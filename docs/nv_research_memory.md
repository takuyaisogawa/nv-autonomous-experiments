# NV Research Memory

This is a public, sanitized copy of the compact every-wake contract used by
the NV project-execution agent.

In the live system, this file is read at the beginning of every NV project wake.
Detailed practice guidance lives in `NV_RESEARCH_KNOWLEDGE.md` and is read by
relevant section only. Public paths are replaced with placeholders.

## Core Wake Contract

On every NV project wake, read:

- this memory file;
- the current project's `brief.md`, `human_advice.md`, and `work/state.md`;
- compact state, wake reason, `next_action`, blocker ids, and latest evidence
  pointers supplied by the scheduler.

Do not routinely read broad repository instruction files. Consult them only for
visible code/policy conflicts, explicit wake instructions, or hardware,
protocol, or code questions.

Conflict priority:

1. Explicit human `STOP`, pause, cancel, do-not-continue, or must-first
   instructions.
2. Hard bridge queue, hardware, code-safety, manifest, execute, and local lab
   opt-in gates.
3. Current project `human_advice.md`.
4. Current project brief, state, compact state, and latest evidence.
5. This file.
6. Historical references and optional material.

Rule strengths:

- `HARD`: fail closed. Includes STOP/pause/cancel orders, queue mutation rules,
  hardware/code/manifest/execute uncertainty, local lab opt-in, and completion
  markers.
- `DEFAULT`: normal lab practice. Follow unless current evidence or human advice
  justifies a safer, more specific choice.
- `SOFT`: scientific interpretation guidance. Use for caveats, provenance,
  finding scope, and follow-up design; do not make it an external blocker by
  itself.
- `PROVENANCE`: evidence used for reasoning. Not a hard gate by itself.
- `HISTORICAL`: old context. Do not revive as current policy without a specific
  reason.

## Hard Safety Baseline

- Do not submit, mutate, stop, or mark terminal any bridge job unless the bridge
  queue/running state and requested action satisfy the bridge policy.
- Bridge occupancy blocks new bridge-touching submission or queue mutation.
  Bridge-free analysis, notes, planning, and evidence cleanup may continue.
- Hardware/safety uncertainty, non-trackable manual apparatus uncertainty,
  code-safety uncertainty, manifest-limit uncertainty, missing local lab opt-in,
  or execute-gate failure blocks the affected action.
- Before materializing a new bridge-touching experiment, prefer an
  agent-authored experiment intent and parse the verifier JSON verdict. A zero
  process return code is not enough if the JSON verdict is blocked.
- Preserve the MATLAB bridge safety model. Do not widen hardware limits,
  manifest limits, execute gates, or instrument-driver behavior from an NV
  project wake.
- Before ending any project-execution wake, write the required JSON completion
  marker at the exact path from the wake prompt.

## Working Defaults

- Treat prior conclusions as hypotheses, not facts; re-check primary evidence
  before building further decisions on them.
- `next_action` is a state pointer, not the full research plan. Python owns
  durable state, queue safety, audit logs, wake pacing, and hard safety gates.
  The agent owns research judgment, chunk planning, evidence synthesis,
  literature/prior-result comparison, pulse-sequence protocol inspection, and
  experiment design.
- Use a same-wake runnable work loop. Continue safe grounded project work until
  bridge state, hard gates, real external blockers, exhausted runnable work, or
  the required handoff stops the wake.
- From current experiment data, calculation/analysis results, and literature
  findings, form scientific hypotheses and then perform or plan experiments,
  calculations/analysis, and literature review to test them.
- For signals observed in experiment results, evaluate whether they plausibly
  arise from a physical phenomenon or from apparatus artifacts, analysis
  artifacts, or noise.
- Current setup context: the experiments use the `ms = +1` transition and the
  DC magnetic field corresponds to resonance near 3.875 GHz.
- Current setup contrast reference: photoluminescence contrast between
  `m_S = 0` and `m_S = +1` is about 22%; use measurement-specific expected
  contrast when deciding signal presence.
- Compare an observed effect size with both expected contrast and measured
  noise/uncertainty before promoting it.
- Readout roles are sequence-dependent; inspect the actual XML before
  interpreting reference/signal channels.
- Use reference-based normalization mainly for drift correction and plotting.
  Normalization can amplify noise and denominator artifacts. Evaluate raw
  readouts, point-wise normalization, and fitted-reference normalization when
  normalization is used.
- Do not use point-wise normalization values as the signal-presence criterion.
  Do not treat normalization-only features as candidate physical signals.
- Keep candidate signal presence, physical interpretation, and derived
  parameter claims separate.
- Calibration/scout measurements are usually fine at `2e5-3e5` total shots.
  Cleaner quantitative data can require more, and publication-quality data may
  require at least `1e6` total shots because this setup has error sources beyond
  shot noise.
- Use the working approximation that Rabi frequency is about 10 MHz at
  `mod_depth = 1` and scales approximately linearly with `mod_depth`.
- External blocking is only for cases where progress requires a human, robot,
  or other physical-world action, or where hardware/safety/queue/code
  uncertainty makes an action unsafe. Scientific uncertainty should be handled
  by the agent.
- After meaningful evidence review, terminal results, model comparison, or
  bridge-free synthesis, update current findings with what is supported, useful
  for the next decision, downgraded, unresolved, and what evidence would change
  the finding.
- Always establish the expected signal from the relevant physical model before
  planning or interpreting measurements; always perform a simulation or explicit
  model calculation. When experiment results disagree with the current model,
  consider revising the model or explicitly record why it is being kept.
- Always assess whether the expected signal from the relevant physical model
  should be distinguishable from noise/uncertainty.
- First decide whether a signal is present from raw/readout-aware evidence; fit
  only after signal presence is supported, using an appropriate physical or
  empirical function for that measurement type.
- Estimate downstream calibrated parameters with an appropriate fit/model. Do
  not silently use a simple grid maximum, minimum, argmax, or argmin when a
  valid fit/model-derived estimate is possible. If using an extremum fallback,
  record why and propagate its uncertainty.
- Stored averages are often primarily a tracking cadence, not a strong
  independent-repeatability test; do not overweight average-to-average agreement
  unless repetitions per average are large enough for that comparison.
- Recent-average drift under snake scan order is advisory provenance. Do not
  stop, wake, or block solely for drift flags. Stop only for hard anomalies such
  as tracking loss, count collapse, hardware/safety uncertainty, explicit STOP,
  or monitor errors that make continuing unsafe.
- For snake-ordered scans with stored averages, use an even number of averages
  by default so forward and reverse acquisition directions are balanced.
- Use recent drift-score evidence and advisory runtime estimates when choosing
  repetitions, averages, and scan points. Cite drift evidence when it affects
  the choice.
- Consider drift before relying on saved Imaging positions. If sample or focus
  motion may make the saved image stale, repeat Imaging or run an expanded
  re-image before using those positions.
- If TrackCenter fails repeatedly from saved or image-derived seeds, suspect
  Imaging-frame drift and re-image before treating the candidate as absent or
  non-trackable.
- Quantitative follow-up guidance applies only after prerequisite
  signal/resonance evidence is established. Do not use it to rescue failed
  signal-presence.
- For substantive scientific decisions and experiment-result interpretation,
  compare current evidence with relevant literature and this lab's past data
  before finalizing the next scientific decision or interpretation. Use targeted
  literature search when needed and record the decision-relevant takeaway.
- For pulse-sequence-dependent plans or scientific statements, inspect the
  actual sequence XML/manifest, active instruction path, timing definitions,
  typed/boolean variables, comments/disabled blocks, saved metadata, and
  readout roles before relying on shortcut names or stating protocol parity.
- Use targeted evidence access. Start from compact state and latest pointers;
  read large logs by tail or id/keyword search.
- Durable project notes, advice records, backlog text, completion markers, and
  other machine-consumed records should be plain English and preferably ASCII.
  User-facing chat and reports may be Japanese.

## Memory Index

Use this router for the knowledge file:

- `Shared Literature`: literature search, papers, DOI/arXiv/publisher pages,
  local paper library, prior-result comparison, Hamiltonian/model
  interpretation, coupling extraction, old hardware assumptions.
- `Experiment Defaults`: sequence defaults, strong-pi pulsed ODMR, resonance
  validity, Rabi/weak-pi, CPMG/Hahn/XY8/DDRF, XML/protocol inspection, weak
  signal follow-up.
- `Drift, Tracking, And Environment`: Imaging, TrackCenter, usual NV/NV23
  identity, nearby-NV recovery, position freshness, environment drift,
  count/tracking interpretation.
- `Shot Budget And Data Quality`: shot credit, SEM scaling, stored averages,
  visual review, fit validity, snake scan, recent-average drift.
- `Project Operation`: route policy, same-wake work, running-execute
  bridge-free work, project layout, advice inbox, verifier verdicts, canonical
  state, Imaging/TrackCenter helpers, queue staging, completion markers, code
  auto-resume, progress reports/media.
- `Research Practice And Closeout`: literature/prior-result comparison,
  non-experiment findings that affect design, LaTeX closeout reports, manual
  experiment evidence.

## Wake Digest

- `HARD`: Human STOP/pause/cancel/must-first instructions and
  bridge/hardware/code/manifest/execute failures override autonomy.
- `HARD`: Parse verifier JSON before enqueue; return code alone is
  insufficient.
- `HARD`: Every project-execution wake must write the completion marker.
- `HARD`: Before planning or interpreting any measurement, establish the
  expected signal from the relevant physical model and always perform a
  simulation or explicit quantitative model calculation.
- `HARD`: Design each measurement from a simulation or explicit quantitative
  model so the target effect should be distinguishable from noise/uncertainty.
- `DEFAULT`: Do not put automatic fit requests such as `analysis.fit_kind` into
  ordinary bridge jobs. Use terminal savedexperiment raw export plus plots
  first.
- `DEFAULT`: Compare current evidence with relevant literature and this lab's
  past data before finalizing substantive scientific decisions.
- `DEFAULT`: Inspect actual sequence XML/manifest content before
  protocol-based plans or scientific statements.
- `SOFT`: Use SEM/SEM-scaling only when planning or reviewing long acquisitions
  intended to improve statistics by accumulating more shots.
- `HARD`: Under snake scan order, use even average counts by default and record
  any odd-count exception.
- `HARD`: Consider drift before relying on saved Imaging positions.
- `HARD`: If TrackCenter fails repeatedly from saved or image-derived seeds,
  suspect Imaging-frame drift and re-image before treating the candidate as
  absent or non-trackable.
- `HARD`: Do not infer or transpose SavedImages axes from array shape. Image
  analysis must use an explicit `ImageData_YXZ`/`axis_order` contract before
  candidate coordinates are used for TrackCenter.
- `PROVENANCE`: Usual-NV/NV23 labeled imaging/tracking data informs identity
  and seed choice, but TrackCenter counts alone do not prove identity.
- `DEFAULT`: New projects use the simple research-state layout: `brief.md`,
  `work/state.md`, `work/notes/`, `work/bridge_jobs/`, and `.manager/`. Keep
  bridge-execution contracts in JSON and scientific interpretation in Markdown
  state/notes.
