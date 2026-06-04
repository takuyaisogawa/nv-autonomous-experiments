# Public Release Manifest

This file tracks what is included, sanitized, or excluded from the public
case-study release.

## Include

- Sanitized project-folder copies for `image145844`, `image172647`, and
  `image231924` as the primary release objects.
- Case state files for `image145844`, `image172647`, and `image231924`.
- Relevant bridge job records: intents, submit specs, job/status/result JSON.
- Raw saved image and savedexperiment data associated with the case studies.
- Processed JSON/HDF5 exports derived from raw MATLAB files.
- MATLAB and Python analysis code used for pODMR, Ramsey, drift, figure, and
  report generation, including the CPMG analysis path used by `image172647`.
- Case-referenced Python runtime helpers from the live NV automation workspace
  for MAT parsing, sequence design, report building, submit-spec support, and
  the MATLAB wrapper boundary used by the retained enqueue source.
- Public MATLAB helpers for savedexperiment export, savedexperiment summary,
  saved scan analysis, and image-axis normalization.
- Sanitized production Python source copy for the case-referenced NV automation
  execution path: project manager, batch runner, bridge runtime watcher, and
  direct enqueue helpers, with CLI execution disabled.
- Public agent prompt-context summary derived from the `nv-project-manager`
  skill prompt.
- Public model and agent configuration note for the `nv-researcher`
  project-execution agent.
- Minimal Python dependency list in `requirements.txt`.
- Public scope statement for the execution-source release.
- Memory/knowledge design note for the self-updating agent loop.
- Public NV research memory copy and knowledge index/excerpt.
- Public project-state template showing the readable state surface, evidence
  citation pattern, and "vibe physics" operating pattern.
- Experiment-intent schema note.
- Code inventory documenting the public Python/MATLAB subset and the
  live-lab boundary.
- Generated figures and closeout reports.
- License and citation metadata.

## Sanitize

- Absolute local paths.
- User names, machine names, WSL paths, and network share paths.
- Human advice files and ledger excerpts only where they contain private
  operational text.
- Bridge records that contain live-lab-only configuration.
- Wake payloads, advice files, and logs only where they contain private,
  credential, or live-hardware details.

## Exclude

- API keys, tokens, webhooks, chat ids, cookies, and credentials.
- Vendor licenses and redistributability-restricted vendor files.
- Private laboratory configuration and live hardware connection settings.
- Instrument drivers, live hardware configuration, and live bridge queue roots.
- Any execution entry point that could move hardware, emit microwave signals,
  move stages, or mutate live queues.
- Private configuration, real queue roots, and runnable automatic startup wiring
  for a real experiment machine.
- `openclaw_skills/` runtime skill folders and thin skill wrapper scripts;
  the relevant project-manager prompt context is summarized in
  `docs/agent_prompt_context.md` instead.
- Scheduler/startup runners, runtime-lease helpers, batch-control helpers,
  old direct-submit wrappers, offline simulation workers, setup/viewer
  utilities, monitor-only prompt wrappers, and legacy recovery-plan prompt
  wrappers not needed to inspect these cases.
- MATLAB live-lab backend source beyond the retained analysis/manifest/sequence
  inspection subset.
- Unrelated project logs, unrelated raw data, and non-case-study private memory.
