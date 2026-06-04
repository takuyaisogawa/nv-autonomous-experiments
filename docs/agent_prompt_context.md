# Agent Prompt Context

This document summarizes the project-manager prompt context used by the
NV project agent. The original runtime skill wrapper is not included
as public source because it was only a thin launcher around the real project
manager source in `python/openclaw_nv_execution_source/nv_project_manager.py`.

## Role Split

- `nv-researcher` owns research judgment, experiment-design reasoning,
  evidence synthesis, model comparison, finding scope, and agenda/backlog
  expansion.
- Python owns durable state, queue safety, audit logs, wake pacing, completion
  markers, and hard hardware/code safety boundaries.
- The MATLAB bridge remains the execute safety gate. The agent must not bypass
  bridge validation, manifest limits, local lab opt-in, queue execute opt-in,
  or hardware safety limits.

## Wake Startup

For an NV project wake, the agent was instructed to read:

1. `NV_RESEARCH_MEMORY.md`.
2. The current project's `brief.md`, `human_advice.md`, and `work/state.md`.
3. Compact wake state, `next_action`, blocker ids, and latest evidence
   pointers from the wake prompt.
4. Relevant sections of `NV_RESEARCH_KNOWLEDGE.md`, selected by the Memory
   Index and current evidence.

Broad repository instructions and long reference documents were treated as
on-demand context, not routine startup context.

## Work Loop

The agent was instructed to treat `next_action` and backlog items as state
pointers, not as a complete research plan. A normal wake should:

- choose the next safe grounded task from objective, evidence, human advice,
  policy, and bridge state;
- complete or update that task;
- record evidence and decisions in durable project files;
- continue into the next runnable task while policy, bridge state, evidence,
  and time budget permit.

During a running execute, useful bridge-free work was allowed: analysis, model
calculations, literature review, evidence-gap closure, notes, figures, tables,
or interpretation updates. The agent was not allowed to mutate the bridge queue
or stop/mark terminal a running job without terminal evidence or a hard anomaly.

## Project Memory Surface

The main durable records were:

- `work/state.md`: compact project state, candidate findings, final claims,
  decisions, and next pointers.
- `work/bridge_jobs/`: bridge-execution contract JSON.
- `work/notes/`: one small note per meaningful analysis, calculation,
  experiment decision, check, review, or failed idea.
- `.manager/evidence.jsonl`: append-only evidence/artifact registry.
- `log.md`: human-readable research notebook.

Reusable detailed NV lessons were recorded in `NV_RESEARCH_KNOWLEDGE.md`.
Every-wake rules and routing belonged in `NV_RESEARCH_MEMORY.md`.

## Intent And Safety

For bridge-touching experiments, the intended flow was:

```text
agent-authored scientific intent
        |
        v
deterministic safety / queue verification
        |
        v
bridge submit spec or blocked/rejected intent
```

A verified intent was not itself a bridge job. The verifier checked hard
constraints such as queue state, forbidden safety-bypass keys, missing
rationale, expected evidence, and bridge-idle requirements.

## Included Source

The public source corresponding to this prompt context is:

- `python/openclaw_nv_execution_source/nv_project_manager.py`
- `python/openclaw_nv_execution_source/nv_batch_run.py`
- `python/openclaw_nv_execution_source/nv_bridge_runtime_watch.py`
- `python/openclaw_nv_execution_source/enqueue_nv_sequence_direct.py`
- `python/openclaw_nv_execution_source/enqueue_nv_imaging_direct.py`

Direct execution of these public source files is disabled in this release.
