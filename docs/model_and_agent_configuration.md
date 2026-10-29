# Model And Agent Configuration

This release records the model and role configuration used for the
project-execution agent in the included autonomous NV case studies.

## Project-Execution Agent

| Field | Value |
| --- | --- |
| Agent id | `nv-researcher` |
| Model | `openai-codex/gpt-5.5` |
| Thinking level | `xhigh` |
| Role | Interpreting results, designing experiments, comparing models, and deciding which conclusions the evidence supports |

The `nv-researcher` project-execution agent is separate from the direct-chat
`main` agent. The two roles may use the same model family, but they are
separate sessions with different initial instructions and memory documents.

## Deterministic Runtime Roles

The agent proposes measurements and interprets results. Python and MATLAB
check measurement requests before execution.

- Python saves project state and run logs, tracks pending and completed tasks,
  and checks the measurement queue and safety constraints.
- The MATLAB bridge checks requests against the sequence manifests and
  hardware limits, executes accepted jobs, and saves their status and results.

## Memory And Knowledge

The agent reads the NV memory document at the start of each run and reads
knowledge sections relevant to its current task:

- Startup memory: `docs/nv_research_memory.md`
- Knowledge index: `docs/nv_research_knowledge_index.md`
- Representative knowledge excerpt: `docs/nv_research_knowledge_excerpt.md`

Memory contains the instructions read at the start of each run and explains
how to find relevant knowledge. Knowledge records lessons from earlier
experiments.

## Case Provenance

| Case | Project-execution agent | Model | Thinking level | Notes |
| --- | --- | --- | --- | --- |
| `image145844` | `nv-researcher` | `openai-codex/gpt-5.5` | `xhigh` | The archived `project.json` uses an older metadata format, so the model fields are recorded in the case README and `case.yaml` for this public release. |
| `image172647` | `nv-researcher` | `openai-codex/gpt-5.5` | `xhigh` | The archived `project.json` records `nv-researcher` and the same project-execution route, but not the explicit model fields; the public case metadata records them. |
| `image231924` | `nv-researcher` | `openai-codex/gpt-5.5` | `xhigh` | The archived `project.json` includes `project_execution_agent_model` and `project_execution_agent_thinking` fields. |

The public execution-source copy also records these defaults in
`python/openclaw_nv_execution_source/nv_project_manager.py`.

## Offline Benchmark Configuration

The autonomous case studies above used GPT-5.5. The current manuscript
compares six models on both offline benchmarks, using the same inputs,
prompts, reasoning effort settings, number of replicates, and scoring rules.

| Manuscript name | Model argument |
| --- | --- |
| GPT-5.4 | `gpt-5.4` |
| GPT-5.5 | `gpt-5.5` |
| GPT-5.6 Sol | `gpt-5.6-sol` |
| GPT-6.1 Sol | `gpt-6.1-sol` |
| GPT-6.1 Terra | `gpt-6.1-terra` |
| GPT-6 Astra | `gpt-6-astra` |

Each model has 400 Ramsey responses and 3,456 pODMR judgments. Records for
the [original three models](../benchmarks/three-model-comparison-2026-07/)
and the [three added in October](../benchmarks/additional-models-2026-10/)
document their execution settings. The latter directory also contains the
combined results and describes differences in the CLI and tool configuration.
GPT-5.4 used the alias available through Codex with ChatGPT authentication
at execution time.

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
