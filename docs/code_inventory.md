# Code Inventory

This document lists the NV automation code included in the release and its
relationship to the code used in the experiments.

## Python

| Public path | Role | Production relationship |
| --- | --- | --- |
| `python/openclaw_runtime/` | Case-referenced runtime and analysis helpers copied from the live NV automation workspace: MATLAB MAT parsing, MATLAB wrapper support, project schema / submit-spec support, sequence design, and report build helpers. | Closest public Python layer needed by the retained case source. Local defaults are represented by environment variables or placeholders. |
| `python/openclaw_nv_execution_source/` | Sanitized production source copy for the case-referenced path: project manager, batch runner, bridge runtime watcher, and direct enqueue helpers. | Source-inspection copy of the retained operating layer. Direct CLI execution is disabled in the public release. |
| `cases/*/project/work/artifacts/analysis/` | Case-specific analysis scripts captured with each completed project. | Historical scripts used or retained by the project artifacts, patched only where needed to resolve public runtime helpers inside this repository. |

## MATLAB

| Public path | Role | Production relationship |
| --- | --- | --- |
| `matlab/analysis/` | Savedexperiment export, savedexperiment summary, saved scan analysis, and image-axis normalization. | Public subset copied from MATLAB `claw/` helpers that is useful for inspecting and regenerating case artifacts. |
| `matlab/manifests/` | Sequence manifests referenced by the public cases. | Public case-relevant manifest subset. |
| `matlab/sequences/` | Sequence XML files referenced by public manifests and case records. | Public case-relevant sequence subset. |

## Agent Prompt Context

| Public path | Role | Production relationship |
| --- | --- | --- |
| `docs/agent_prompt_context.md` | Summary of the agent instructions, including startup, work steps, project records, and safety checks. | Derived from the operating `nv-project-manager` skill prompt. The runtime skill folder and thin wrapper script are omitted from the public source tree. |

## Boundary

Hardware execution is disabled. See [Public scope](public_scope.md) for the
included and excluded components.
