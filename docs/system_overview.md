# System Overview

OpenClaw ran the agent and managed the experimental projects. This repository
contains the code and records needed to inspect how the agent analyzed data,
planned measurements, and updated its conclusions.

```text
human request / project brief
        |
        v
project state + backlog + memory/knowledge context
        |
        v
scheduler starts the agent and records the run
        |
        v
agent reads state, evidence, advice, and relevant knowledge
        |
        v
agent analyzes data, plans a measurement, or ends the project
        |
        v
software checks measurement requests before submission
        |
        v
measurement results -> evidence log -> updated project state
```

## Core Objects

`project-execution agent` is the LLM research role for these cases. Its public
configuration is recorded in `docs/model_and_agent_configuration.md`.

`project state` summarizes the agent's current findings and next steps. In the
case copies, the readable form is `work/state.md`; machine state and audit
records are stored under `.manager/`.

`backlog` is an execution queue and audit trail, not the full scientific plan.
It captures bounded work items, external blockers, and completed decisions.

`memory` contains instructions read at the start of each run. It directs the
agent to relevant sections of `knowledge`, which contains lessons from earlier
experiments.

`experiment intent` is the scientific plan prepared by the agent before
submitting a measurement to the MATLAB bridge. It records the objective,
submit spec, safety assumptions, expected evidence, and verification status.

The `evidence ledger` is a log that links claims to the records used to assess
them, including analysis outputs, figures, measurement results, notes, and
reports. New entries are added without changing earlier ones.

## Wake Loop

A "wake" is one invocation of the project agent by the scheduler.

The scheduler checks the project state, measurement status, pending tasks, and
recent runs. When the agent can proceed with a task, the scheduler starts it
and records the run. These records are included with each experiment. The
project manager's code is in
`python/openclaw_nv_execution_source/nv_project_manager.py`. Scripts that
automatically start the scheduler on the laboratory computer are not included.

## Hardware Execution

Hardware execution is disabled in the public code. See
[Public scope](public_scope.md) for the included records and excluded components.

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
