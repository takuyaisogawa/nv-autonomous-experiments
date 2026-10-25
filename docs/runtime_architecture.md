# Runtime Architecture

The public release exposes the OpenClaw-based NV project-management path and
completed case records for audit.

## Python Side

`python/openclaw_nv_execution_source` contains the case-referenced project
manager, batch runner, bridge runtime watcher, and direct enqueue helpers.

`python/openclaw_runtime` contains publishable runtime helpers for MATLAB data
parsing, MATLAB wrapper support, project schema / submit-spec handling,
sequence design, and report building.

## MATLAB Side

`matlab/analysis` contains helpers for inspecting saved measurements
and reordering image data to the axis order (Y, X, Z).

`matlab/manifests` and `matlab/sequences` contain the case-relevant manifest
and XML records needed to inspect what was requested.

## Agent Instructions

`docs/agent_prompt_context.md` summarizes the instructions given to the NV
project agent.

Hardware execution is disabled. See [Public scope](public_scope.md) for the
included and excluded components.
