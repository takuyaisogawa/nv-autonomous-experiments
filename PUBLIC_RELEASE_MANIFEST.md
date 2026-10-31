# Public Release Manifest

This file tracks what is included, sanitized, or excluded from the public
release.

## Include

- Project folders for `image145844`, `image172647`, and `image231924`, including
  their state files, with private information removed.
- Relevant bridge job records: intents, submit specs, job/status/result JSON.
- Raw saved image and savedexperiment data associated with the case studies.
- Processed JSON/HDF5 exports derived from raw MATLAB files.
- MATLAB and Python analysis code used for pODMR, Ramsey, drift, figure, and
  report generation, including the CPMG analysis path used by `image172647`.
- Python helpers used in the experiments to read MATLAB data, design pulse
  sequences, build reports, prepare measurement requests, and call MATLAB.
- MATLAB helpers for exporting and summarizing saved measurements, analyzing
  scans, and reordering image axes.
- Python code used to manage projects, run batches of measurements, monitor
  jobs, and add jobs to the queue. Private settings are removed and direct CLI
  execution is disabled.
- Public agent prompt-context summary derived from the `nv-project-manager`
  skill prompt.
- Public model and agent configuration note for the `nv-researcher`
  project-execution agent.
- Minimal Python dependency list in `requirements.txt`.
- Description of the published code and records.
- Explanation of how the agent uses and updates memory and knowledge.
- Public NV research memory copy and knowledge index/excerpt.
- Project-state template specifying how the agent records findings and links
  them to supporting evidence.
- Experiment-intent schema note.
- Inventory of the published Python and MATLAB code and its relationship to
  the code used in the laboratory.
- Generated figures and final reports.
- Ramsey checkpoint benchmark package used in the manuscript, including neutral
  checkpoint inputs, task prompt, scoring guide, selected scripts, previous
  manual scores, recovered project notes, and figure source data.
- pODMR data evaluation benchmark package used in the manuscript, including raw
  inputs, prompt conditions, labels, predictions, per-run notes, tool use audit,
  deterministic checks, figures, and the appendix batch-comparison summary.
- Reconstructed provider-neutral pODMR per-case runner and a post-release
  Claude adapter for the Ramsey checkpoint benchmark. These use temporary
  case-level workspaces and do not expose benchmark labels to the model
  workspace.
- Benchmark records for the original three models, GPT-5.4, GPT-5.5, and
  GPT-5.6 Sol, including predictions, responses, analysis notes, previous scores,
  and checks that all evaluations completed.
- Complete Ramsey and pODMR records for GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6
  Astra, with 400 Ramsey responses and 3,456 pODMR judgments per model, in
  [additional-models-2026-10](benchmarks/additional-models-2026-10/).
- Judge prompts, judgments for all 2,400 Ramsey responses, and the original
  100-response human validation records with 96% agreement.
- Combined results for all six models, current manuscript Figs. 3–5, vector
  artwork, and scripts for reproducing the analyses and figures. See the
  [figure instructions](benchmarks/additional-models-2026-10/#reproduce-the-analysis-and-figures).
- License and citation metadata.
- The original September 2023 human NV selection log and a retrospective
  explanation of its purpose and selection criteria in
  `human_reference/2023-09_nv_selection/`.

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
