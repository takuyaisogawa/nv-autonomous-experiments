# Project State Template

This document shows the public version of the template used to initialize
`work/state.md` for autonomous NV projects.

`work/state.md` is the main readable state surface for the project agent. It is
short, current, and evidence-oriented. Detailed derivations, failed ideas, and
per-task checks belong in `work/notes/`, while backend-facing execution
contracts belong in `work/bridge_jobs/` or the backend boundary.

The template is included because it captures the operating pattern behind the
case folders: the agent may use qualitative scientific judgment to propose
directions, but important claims must be tied to checks, calculations, code
paths, bridge artifacts, or evidence ids.

## Template

```markdown
# Project State: {project_id}

This is the main readable project state. Keep it short, current, and useful.
Keep bridge-execution contracts in `work/bridge_jobs/` or the live bridge queue.
Put detailed derivations, checks, and failed ideas in `work/notes/` so future wakes
can look them up without carrying everything in context.

## Objective

{objective or "(not recorded)"}

## Vibe Physics Operating Pattern

- Work in small, separately summarized tasks.
- Record what was actually checked; do not write that something is verified unless it was checked.
- When a result matters, include the calculation, bridge artifact, code path, or evidence id that supports it.
- If an assertion is only taste, intuition, or a candidate interpretation, label it that way.
- Repeat verification after fixes; finding one issue is not proof that the rest is clean.

## Standing Operational Assumptions

- Read the shared NV startup memory at `<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md` before choosing NV project steps.
- Use its Memory Index to read relevant sections from `<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` only when the current state, evidence, or human advice makes them useful.
- When an NV wake produces a durable reusable detailed lesson, update `<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` in the relevant section with a concise dated note and provenance pointer.
- New NV projects use the `start-project` -> cron/force wake `nv-researcher` flow. `start-project` preserves the human request and durable state; `nv-researcher` owns the research agenda, backlog expansion, evidence synthesis, and experiment-design judgment.
- Treat backlog items as execution/audit pointers, not as a complete scientific plan. Keep any seed backlog item minimal unless the operator explicitly asked for detailed gates.
- For usual-NV recovery, prefer recent tracking, explicit human seeds, or prompt-visible label-dataset evidence before standalone Imaging/TrackCenter. Do not use the legacy live landmark-map route for future execution or recovery.
- If NV tracking remains continuous and counts/alignment evidence stay healthy, absolute position motion by itself is not a reason to stop or block an experiment. Treat the motion as provenance and drift evidence to record, while continuing bounded work when the scientific intent and safety gates still hold.
- Do pause or re-check when tracking is lost, counts collapse, a discontinuous jump or branch switch lacks continuous tracking provenance, hardware safety is uncertain, or a project-specific human constraint explicitly requires a fixed landmark/position.

## Current Status

- (agent-maintained)

## Candidate Findings

- (agent-maintained)

## Final Claims

- (agent-maintained; cite evidence ids from `.manager/evidence.jsonl` or referenced bridge artifacts)

## Decisions

- (agent-maintained)

## Next Step

- (agent-maintained)

## Evidence Pointers

- (agent-maintained)

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
```

## Why This Matters

The template is deliberately not a detailed scientific script. It gives the
agent a compact state surface and makes the audit rules explicit:

- keep the current state readable;
- write small retrievable notes;
- separate backend execution contracts from scientific interpretation;
- mark uncertain interpretations honestly;
- cite evidence ids or artifacts for important claims.

This is the practical meaning of the "vibe physics" section in the released
case folders: intuition can start a hypothesis, but the project record must
show what was actually checked and what evidence supports the result.
