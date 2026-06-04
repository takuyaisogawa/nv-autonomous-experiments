# Source Copy Boundary

This release includes the case-referenced project-management source needed to
audit the autonomous NV workflow records, while keeping direct laboratory
execution disabled.

## Included Source

- `python/openclaw_nv_execution_source/`
- `python/openclaw_runtime/`
- `matlab/analysis/`
- `docs/agent_prompt_context.md`

These are sanitized copies or public summaries. Local paths have been
placeholdered, and the public release does not include private configuration or
live queue roots.

## Execution Guard

The execution-source Python files have direct CLI execution disabled.

This keeps the scientific and engineering record visible without turning the
repository into a live lab-control package.
