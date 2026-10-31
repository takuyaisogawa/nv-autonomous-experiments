# Code Inventory

This document lists the NV automation code included in the release and its
relationship to the code used in the experiments.

## Python

| Public path | Purpose | Source and changes |
| --- | --- | --- |
| `python/openclaw_runtime/` | Helpers for reading MATLAB data, preparing measurement requests, designing pulse sequences, and building reports. | Copied from the software used in the experiments. Local settings are supplied through environment variables or replaced with placeholders. |
| `python/openclaw_nv_execution_source/` | Code used to manage projects, submit measurements, and monitor jobs during the experiments. | Private settings have been removed, and direct CLI execution is disabled. |
| `cases/*/project/work/artifacts/analysis/` | Analysis scripts saved with each completed experiment. | Some imports were changed to use the helpers included in this repository. |

## MATLAB

| Public path | Purpose | Source and changes |
| --- | --- | --- |
| `matlab/analysis/` | Helpers for exporting and summarizing saved measurements, analyzing scans, and reordering image axes. | Copied from the MATLAB `claw/` helpers used in the experiments. |
| `matlab/manifests/` | Manifests specifying pulse sequences and their permitted settings. | Includes the manifests referenced by the three experiments. |
| `matlab/sequences/` | XML definitions of pulse sequences. | Includes the sequences referenced by the manifests and experiment records. |

## Agent Prompt Context

| Public path | Purpose | Source and changes |
| --- | --- | --- |
| `docs/agent_prompt_context.md` | Summary of the agent instructions, including startup, work steps, project records, and safety checks. | Derived from the operating `nv-project-manager` skill prompt. The runtime skill folder and thin wrapper script are omitted from the public source tree. |

## Hardware Execution

Hardware execution is disabled. See [Public scope](public_scope.md) for the
included and excluded components.
