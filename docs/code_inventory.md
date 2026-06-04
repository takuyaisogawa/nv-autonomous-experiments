# Code Inventory

This repository publishes the audit-relevant NV automation code paths as close to
the operating system as is reasonable for a public release. The boundary is that
source inspection, case-data inspection, validation, and analysis review are
public, while direct laboratory execution remains outside this release.

## Python

| Public path | Role | Production relationship |
| --- | --- | --- |
| `python/openclaw_runtime/` | Case-referenced runtime and analysis helpers copied from the live NV automation workspace: MATLAB MAT parsing, MATLAB wrapper support, project schema / submit-spec support, sequence design, and report build helpers. | Closest public Python layer needed by the retained case source. Local defaults are represented by environment variables or placeholders. |
| `python/openclaw_nv_execution_source/` | Sanitized production source copy for the case-referenced path: project manager, batch runner, bridge runtime watcher, and direct enqueue helpers. | Source-inspection copy of the retained operating layer. Direct CLI execution is disabled in the public release. |
| `cases/*/project/work/artifacts/analysis/` | Case-specific analysis scripts captured with each completed project. | Historical scripts used or retained by the project artifacts, patched only where needed to resolve public runtime helpers inside this repository. |

Execution-source Python files are included for audit, but direct CLI execution
is disabled in the public release.

## MATLAB

| Public path | Role | Production relationship |
| --- | --- | --- |
| `matlab/analysis/` | Savedexperiment export, savedexperiment summary, saved scan analysis, and image-axis normalization. | Public subset copied from MATLAB `claw/` helpers that is useful for inspecting and regenerating case artifacts. |
| `matlab/manifests/` | Sequence manifests referenced by the public cases. | Public case-relevant manifest subset. |
| `matlab/sequences/` | Sequence XML files referenced by public manifests and case records. | Public case-relevant sequence subset. |

Production-only MATLAB execution remains outside the public runnable surface.
The execution-source copy is published for audit and is deliberately disabled as
code.

## Agent Prompt Context

| Public path | Role | Production relationship |
| --- | --- | --- |
| `docs/agent_prompt_context.md` | Summary of the project-manager prompt context: role split, wake startup, work loop, project memory surface, and intent safety flow. | Derived from the operating `nv-project-manager` skill prompt. The runtime skill folder and thin wrapper script are omitted from the public source tree. |

## Boundary

The public code is intended for audit, case-data inspection, schema review, and
analysis review. It is not a complete live-lab distribution and it cannot
control laboratory hardware.
