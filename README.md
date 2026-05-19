# OpenClaw NV Autonomous Experiments

Public release for auditable LLM-agent workflows in NV-center experiments.

This repository has two parallel parts:

- **Case studies:** sanitized completed OpenClaw project folders from real
  autonomous-agent NV experiments.
- **Benchmarks:** offline pODMR resonance-classification tests that evaluate
  how prompt context changes agent judgment on raw NV measurements.

The release preserves project state, evidence logs, bridge records, figures,
reports, analysis artifacts, benchmark inputs, labels, predictions, and scoring
scripts needed to inspect the results.

## Public Scope

The case-referenced OpenClaw/NV project-management source is public for audit.

This repository cannot control hardware.

Real completed case artifacts are included.

See [docs/public_scope.md](docs/public_scope.md) for the exact public boundary.

## Start Here

For a quick review:

| Area | Entry point |
| --- | --- |
| System overview | [docs/system_overview.md](docs/system_overview.md) |
| Agent/model configuration | [docs/model_and_agent_configuration.md](docs/model_and_agent_configuration.md) |
| Case studies | [cases/README.md](cases/README.md), [docs/case_walkthrough.md](docs/case_walkthrough.md) |
| Benchmarks | [benchmarks/podmr-model-first-resonance-2026-05/README.md](benchmarks/podmr-model-first-resonance-2026-05/README.md) |
| Code inventory | [docs/code_inventory.md](docs/code_inventory.md) |
| Safety boundary | [docs/safety_boundary.md](docs/safety_boundary.md) |

## Repository Contents

| Part | What It Shows | Main Artifacts |
| --- | --- | --- |
| Case studies | A safety-bounded LLM research agent operating real NV-center experiments | Project state, evidence logs, bridge records, figures, reports, pODMR/Ramsey/CPMG analyses |
| Benchmarks | How prompt context affects pODMR resonance judgments | Raw export JSON, raw-readout figures, prompts, labels, predictions, analysis notes, scoring scripts |
| Source and docs | Public audit boundary for OpenClaw/NV project management and analysis | Python/MATLAB analysis code, public runtime source, system docs, safety notes |

## Case Studies

The case studies are completed OpenClaw/NV project runs. They are intended to
show what the agent saw, what it decided, which artifacts it wrote, and how the
final scientific conclusions were bounded by the evidence.

| Case | Summary | Status |
| --- | --- | --- |
| [image145844](cases/image145844/README.md) | Aligned NV selection, pODMR screening, repeated Ramsey diagnostics, shifted-sideband 13C candidate reanalysis | Completed |
| [image172647](cases/image172647/README.md) | Fresh re-image recovery, pODMR candidate rejection/acceptance, multi-detuning Ramsey, CPMG N=8 nearby-13C-like corroboration | Completed |
| [image231924](cases/image231924/README.md) | Aligned NV selection, pODMR center refinement, corrected-center Ramsey, T2star closeout | Completed |

## Benchmarks

The benchmark is an offline resonance-classification test built from pODMR data.
It asks the agent to decide whether a resonance is present from one case at a
time using raw export JSON files, raw-readout figures, and prompt context.

| Benchmark | Summary |
| --- | --- |
| [pODMR model-first resonance benchmark](benchmarks/podmr-model-first-resonance-2026-05/README.md) | 96 single-case pODMR classifications with prompts, raw inputs, labels, predictions, analysis notes, and scoring scripts |

The pODMR benchmark contains 24 resonance-present and 72 resonance-absent
strong-pi measurements. Each prompt condition was run for three GPT-5.5 medium
replicates. The model-first condition adds a requirement to establish the
expected physical signal with a simulation or explicit quantitative model
calculation before deciding whether a resonance is present.

The included benchmark summary reports:

| Condition | Accuracy | False-positive rate | False-negative rate |
| --- | ---: | ---: | ---: |
| XML only | 75.3% | 32.9% | 0.0% |
| Domain facts | 93.1% | 9.3% | 0.0% |
| Model-first | 99.7% | 0.46% | 0.0% |

## Agent / Model Configuration

The included case studies are documented as `nv-researcher`
project-execution runs using `openai-codex/gpt-5.5` with `xhigh` thinking.

The direct-chat `main` agent and the project-execution `nv-researcher` agent
are separate sessions. Scientific reasoning, experiment design, evidence
synthesis, and claim-boundary decisions belong to the agent role; deterministic
Python/MATLAB layers handle durable state, queue checks, audit records, bridge
validation, and hardware safety boundaries.

See [docs/model_and_agent_configuration.md](docs/model_and_agent_configuration.md)
for case-level model provenance.

## Repository Layout

```text
cases/
  image145844/
    project/
  image172647/
    project/
  image231924/
    project/
benchmarks/
  podmr-model-first-resonance-2026-05/
python/
  openclaw_runtime/
  openclaw_nv_execution_source/
matlab/
  analysis/
  manifests/
  sequences/
tools/
requirements.txt
docs/
```

The project folders were copied from the local cold archive with
[tools/copy_sanitized_project.ps1](tools/copy_sanitized_project.ps1); copied
sources and treatments are tracked in
[SOURCE_PROVENANCE.md](SOURCE_PROVENANCE.md).

Install the Python analysis dependencies with:

```powershell
python -m pip install -r requirements.txt
```

## Documentation Map

| Topic | Entry point |
| --- | --- |
| Public boundary | [docs/public_scope.md](docs/public_scope.md) |
| System architecture | [docs/system_overview.md](docs/system_overview.md), [docs/runtime_architecture.md](docs/runtime_architecture.md) |
| Model and agent configuration | [docs/model_and_agent_configuration.md](docs/model_and_agent_configuration.md), [docs/agent_prompt_context.md](docs/agent_prompt_context.md) |
| Case guide | [docs/case_walkthrough.md](docs/case_walkthrough.md), [cases/README.md](cases/README.md) |
| Memory and knowledge | [docs/memory_knowledge.md](docs/memory_knowledge.md), [docs/nv_research_memory.md](docs/nv_research_memory.md), [docs/nv_research_knowledge_index.md](docs/nv_research_knowledge_index.md), [docs/nv_research_knowledge_excerpt.md](docs/nv_research_knowledge_excerpt.md) |
| Agent prompt context | [docs/agent_prompt_context.md](docs/agent_prompt_context.md) |
| Project state and intents | [docs/project_state_template.md](docs/project_state_template.md), [docs/experiment_intent_schema.md](docs/experiment_intent_schema.md) |
| Code and safety | [docs/code_inventory.md](docs/code_inventory.md), [docs/source_release_boundary.md](docs/source_release_boundary.md), [docs/safety_boundary.md](docs/safety_boundary.md) |

## Safety Boundary

Public code paths are analysis-only by default. Instrument control, stage
motion, microwave output, and live bridge queue mutation are not included as
public execution entry points.

Hardware credentials, private laboratory configuration, and queue execution
settings are intentionally excluded.

The included `python/openclaw_nv_execution_source` directory exposes the
case-referenced project-management execution source for audit. Direct execution
entry points are disabled in the public release. The live MATLAB lab backend
source is not included; historical bridge records are included as case
artifacts.

Project folders are intended to be close mirrors of the original public
case-study folders. Redactions are limited to safety/privacy sanitization and
redistribution constraints.

Before publishing or pushing new case artifacts, run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\check_public_release_redactions.ps1
```

Copied artifacts should be recorded in `SOURCE_PROVENANCE.md`.

## License

Code is licensed under the MIT License. Documentation, public case-study
folders, included data exports, generated figures, reports, and analysis
artifacts are licensed under CC BY 4.0. See `LICENSE`.

## Reproducibility

The included case artifacts are intended to support analysis review and
rebuilding of selected figures, metrics, and reports. Full live laboratory
re-execution is outside the scope of this public release.

## Citation

Citation metadata is provided in `CITATION.cff`.
