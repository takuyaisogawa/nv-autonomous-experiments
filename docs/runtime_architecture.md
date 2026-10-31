# Runtime Architecture

This document describes the code used to manage the autonomous NV experiments
and analyze their data.

## Python Side

`python/openclaw_nv_execution_source` contains the project manager and code
for running batches of measurements, monitoring jobs, and adding jobs to the queue.

`python/openclaw_runtime` contains helpers for reading MATLAB data, preparing
measurement requests, calling MATLAB, designing pulse sequences, and building reports.

## MATLAB Side

`matlab/analysis` contains helpers for inspecting saved measurements
and reordering image data to the axis order (Y, X, Z).

`matlab/manifests` lists pulse sequences and their permitted settings.
`matlab/sequences` contains the XML definitions of those sequences.

## Agent Instructions

`docs/agent_prompt_context.md` summarizes the instructions given to the NV
project agent.

Hardware execution is disabled. See [Public scope](public_scope.md) for the
included and excluded components.
