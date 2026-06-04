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

`matlab/analysis` contains the runnable helper subset for savedexperiment
inspection and the image-axis normalization contract used by the cases.

`matlab/manifests` and `matlab/sequences` contain the case-relevant manifest
and XML records needed to inspect what was requested.

The live MATLAB lab backend source is not included in this public release.

## Prompt Surface

`docs/agent_prompt_context.md` summarizes the retained NV project-manager
project-manager prompt context used for long-running project wake context. The
runtime skill folder and thin wrapper script are omitted from the public source
tree to avoid confusing them with the real project-manager implementation.

The public case folders preserve real completed records, but the repository
does not provide a route to live hardware.
