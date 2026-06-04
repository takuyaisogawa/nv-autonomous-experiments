# Production Source Copy

This directory contains sanitized source copies from the NV project
execution path that are referenced by the two public cases: project manager,
batch runner, bridge runtime watcher, and direct enqueue helpers.

These files are included so readers can inspect the production architecture.
Direct CLI execution is disabled in this public release.

Local paths have been replaced by placeholders such as `<OPENCLAW_WORKSPACE>`,
`<MATLAB_23C_ROOT>`, and `<NV_BRIDGE_ROOT>`.

Scheduler/startup runners, runtime-lease helpers, batch-control helpers, legacy
cron runners, deprecated replay/evaluation helpers, and unrelated
notification/result watcher code are omitted to keep this directory focused on
the case-referenced path.
