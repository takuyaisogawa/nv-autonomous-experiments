# System Overview

This release is organized around an auditable autonomous-experiment loop. The
completed NV runs used the OpenClaw platform as the agent/project-management
layer, and this repository exposes the case-referenced source and completed
project records needed to inspect those runs.

```text
human request / project brief
        |
        v
project state + backlog + memory/knowledge context
        |
        v
scheduler wake decision -> agent wake record
        |
        v
agent reads state, evidence, advice, and relevant knowledge
        |
        v
analysis, experiment intent, or closeout decision
        |
        v
intent verification -> bridge boundary
        |
        v
bridge/result artifacts -> evidence ledger -> updated project state
```

## Core Objects

`project-execution agent` is the LLM research role for these cases. Its public
configuration is recorded in `docs/model_and_agent_configuration.md`.

`project state` is the compact current truth for a project. In the case
copies, the readable form is `work/state.md`; machine state and audit records
live under `.manager/`.

`backlog` is an execution queue and audit trail, not the full scientific plan.
It captures bounded work items, external blockers, and completed decisions.

`memory / knowledge` separates wake-start operating rules from accumulated
domain lessons. In the live system, memory routes the agent to the relevant
knowledge sections instead of loading every prior lesson into every wake.

`experiment intent` is the agent-authored scientific plan before any bridge
touch. It records the objective, submit spec, safety assumptions, expected
evidence, and verification status.

`evidence ledger` is append-only provenance. It links analysis outputs, figures,
bridge results, notes, and reports to the claims they support or reject.

## Wake Loop

The scheduler inspects project state, bridge/result activity, backlog, and
recent agent-run records. If work is actionable, it writes a wake record and
dispatches the project agent. The public cases preserve the wake records and
the retained OpenClaw project-manager source at
`python/openclaw_nv_execution_source/nv_project_manager.py`; scheduler startup
wiring is outside this focused public subset.

## Backend Boundary

The public repository cannot move stages, emit microwave signals, start lasers,
control cameras, or mutate a live bridge queue. Execution-source entry points
are disabled, and private configuration/live queue roots are excluded.

Completed case folders preserve real historical bridge/result artifacts for
audit.

## Where To Look

- NV execution source copy: `python/openclaw_nv_execution_source/`
- Model and agent configuration: `docs/model_and_agent_configuration.md`
- Python runtime helpers: `python/openclaw_runtime/`
- NV research memory: `docs/nv_research_memory.md`
- NV knowledge index/excerpt: `docs/nv_research_knowledge_index.md`,
  `docs/nv_research_knowledge_excerpt.md`
- Project state template: `docs/project_state_template.md`
- Case project state: `cases/<case>/project/work/state.md`
- Evidence ledger: `cases/<case>/project/.manager/evidence.jsonl`
- Bridge records: `cases/<case>/project/work/bridge_jobs/`
- Analysis and figures: `cases/<case>/project/work/artifacts/`
