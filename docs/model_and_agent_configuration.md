# Model And Agent Configuration

This release records the model and role configuration used for the
project-execution agent in the included autonomous NV case studies.

## Project-Execution Agent

| Field | Value |
| --- | --- |
| Agent id | `nv-researcher` |
| Model | `openai-codex/gpt-5.5` |
| Thinking level | `xhigh` |
| Role | Scientific reasoning, experiment design, evidence synthesis, model comparison, and claim-boundary decisions |

The `nv-researcher` project-execution agent is separate from the direct-chat
`main` agent. The two roles may use the same model family, but they are
separate sessions with different startup context and memory surfaces.

## Deterministic Runtime Roles

The LLM agent does not directly control hardware. Deterministic Python and
MATLAB layers own the operational boundaries:

- Python project-management code owns durable state, backlog updates, wake
  records, audit logs, completion markers, queue checks, and hard safety
  boundaries.
- The MATLAB bridge and manifest layer owns experiment validation, hardware
  limits, submit-spec execution, and result/status artifacts.
- The agent authors scientific intent and interpretation; verified bridge
  submit specs and live execution remain behind deterministic validation.

## Memory And Knowledge Surface

The project-execution agent reads the compact NV startup memory at each wake
and reads detailed knowledge sections on demand:

- Startup memory: `docs/nv_research_memory.md`
- Knowledge index: `docs/nv_research_knowledge_index.md`
- Representative knowledge excerpt: `docs/nv_research_knowledge_excerpt.md`

This split is part of the public provenance for the self-updating agent loop:
memory provides the wake contract and routing rules, while knowledge stores
reusable experimental lessons and prior-operation guidance.

## Case Provenance

| Case | Project-execution agent | Model | Thinking level | Notes |
| --- | --- | --- | --- | --- |
| `image145844` | `nv-researcher` | `openai-codex/gpt-5.5` | `xhigh` | The archived `project.json` uses an earlier startup metadata shape, so the model fields are recorded in the case README and `case.yaml` for this public release. |
| `image172647` | `nv-researcher` | `openai-codex/gpt-5.5` | `xhigh` | The archived `project.json` records `nv-researcher` and the same project-execution route, but not the explicit model fields; the public case metadata records them. |
| `image231924` | `nv-researcher` | `openai-codex/gpt-5.5` | `xhigh` | The archived `project.json` includes `project_execution_agent_model` and `project_execution_agent_thinking` fields. |

The public execution-source copy also records these defaults in
`python/openclaw_nv_execution_source/nv_project_manager.py`.

## Offline Benchmark Configuration

The autonomous case studies above used GPT-5.5.  The offline Ramsey and pODMR
benchmarks were subsequently evaluated with three model variants under the
same inputs, prompts, reasoning effort settings, and replicate structure.

| Manuscript name | Model argument | Benchmark role |
| --- | --- | --- |
| GPT-5.4 | `gpt-5.4` | Ramsey and pODMR comparison sweep |
| GPT-5.5 | `gpt-5.5` | Original Ramsey and pODMR sweep |
| GPT-5.6 Sol | `gpt-5.6-sol` | Ramsey and pODMR comparison sweep |

The GPT-5.4 run used the alias available through Codex with ChatGPT
authentication at execution time.  Full run counts and public audit records
are documented in
`benchmarks/three-model-comparison-2026-07/README.md`.

## Reporting Convention

When citing these cases, describe the autonomy stack as:

```text
NV project-execution agent: nv-researcher
model: openai-codex/gpt-5.5
thinking level: xhigh
deterministic boundary: Python state/queue/audit layer plus MATLAB bridge validation
```

For future benchmark runs, model, thinking level, prompt/memory condition,
knowledge condition, and simulation-first condition should be recorded per
benchmark item or run group rather than only at the case level.
