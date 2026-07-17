# Source Provenance

Record every nontrivial copied artifact here before public release.

| Public path | Source location | Case(s) | Treatment | Notes |
| --- | --- | --- | --- | --- |
| `tools/check_public_release_redactions.ps1` | Authored for this release | all | public | Redaction scan helper. |
| `tools/copy_sanitized_project.ps1` | Authored for this release | all | public | Repeatable helper for copying archived project folders with public-path and sensitive-keyword redaction. |
| `.gitignore` | Authored for this release | all | public | Ignore local/generated files under `.openclaw/`. |
| `LICENSE` | Authored for this release | all | public | Split license statement: code under MIT, documentation and public case-study artifacts under CC BY 4.0. |
| `CITATION.cff` | Authored for this release | all | public | Citation metadata for the public release. |
| `requirements.txt` | Authored for this release | all | public | Minimal Python dependencies for public analysis scripts: NumPy, SciPy, Matplotlib. |
| `docs/runtime_architecture.md` | Authored for this release | all | public | Runtime layer overview for the current execution-source release. |
| `docs/public_scope.md` | Authored for this release | all | public | Explicit public boundary: current execution source public for audit, no hardware control, real completed case artifacts included. |
| `docs/system_overview.md` | Authored for this release from execution-source structure and case folders | all | public | One-page overview of the agent wake loop, state, memory/knowledge split, intents, backend boundary, and evidence ledger. |
| `docs/model_and_agent_configuration.md` | Authored for this release from project-manager source, case metadata, and public case records | all | public | Model, thinking-level, agent-role, and deterministic-boundary provenance for the included cases. |
| `docs/memory_knowledge.md` | Authored for this release from the NV project-operation design | all | public | Explanation of the memory/knowledge split used by self-updating agent wakes. |
| `docs/nv_research_memory.md` | Sanitized from live workspace `NV_RESEARCH_MEMORY.md` | all | sanitized | Public copy of the compact every-wake NV project-execution contract; local paths and operator-channel wording replaced with placeholders/general terms. |
| `docs/nv_research_knowledge_index.md` | Authored for this release from live workspace `NV_RESEARCH_KNOWLEDGE.md` section map | all | public | Public index of reusable NV research knowledge sections and read policy. |
| `docs/nv_research_knowledge_excerpt.md` | Excerpted and sanitized from live workspace `NV_RESEARCH_KNOWLEDGE.md` | all | excerpted | Representative reusable lessons showing how the agent uses accumulated experiment knowledge. |
| `docs/project_state_template.md` | Authored for this release from the NV project-state initialization template | all | public | Public version of the `work/state.md` template, including the Vibe Physics operating pattern and evidence-citation convention. |
| `docs/agent_prompt_context.md` | Authored for this release from live workspace `skills/nv-project-manager/SKILL.md` | all | summarized | Public summary of the project-manager prompt context; the runtime skill folder and thin wrapper script are omitted to avoid confusion with the real source. |
| `docs/experiment_intent_schema.md` | Authored for this release from execution-source intent handling and case intent artifacts | all | public | Explanation of the intent -> verification -> backend boundary flow. |
| `docs/case_walkthrough.md` | Authored for this release from case `work/state.md` files and closeout artifacts | `image145844`, `image172647`, `image231924` | public | Reader guide to the three case studies and where to inspect their evidence. |
| `docs/safety_boundary.md` | Authored for this release | all | public | Public safety boundary for the release. |
| `cases/README.md` | Authored for this release | all | public | Case-study entry point and audit path guide. |
| `cases/image145844/README.md` | Authored for this release from `image145844` case state and reports | `image145844` | public | Case-specific reader entry point. |
| `cases/image172647/README.md` | Authored for this release from `image172647` case state and closeout report | `image172647` | public | Case-specific reader entry point. |
| `cases/image231924/README.md` | Authored for this release from `image231924` case state and reports | `image231924` | public | Case-specific reader entry point. |
| `cases/image145844/project/` | Cold archive project folder for `image145844` | `image145844` | sanitized | Sanitized root project files, `.manager/`, `work/`, `advice/`, and `experiment_intents/`; transient lock/cache files skipped. |
| `cases/image145844/project/data_recovered_20260514/` | `23-C/savedexperiments/NV1` and `23-C/SavedImages` | `image145844` | public | Recovered 12 savedexperiment MAT files and one imaging MAT file referenced by the case artifacts but absent from the cold archive copy. See `RECOVERED_MAT_FILES.csv`. |
| `cases/image172647/project/` | Live project folder for `image172647` | `image172647` | sanitized | Sanitized root project files, `.manager/`, `work/`, `advice/`, `summaries/`, and `experiment_intents/`; transient lock/cache files skipped. |
| `cases/image172647/project/data_recovered_20260515/` | `23-C/SavedImages`, `23-C/savedexperiments/NV1`, and `nv_bridge/status/openclaw_imaging*` | `image172647` | public | Recovered raw saved image, fresh re-image, imaging exports, and 8 savedexperiment MAT files referenced by the case artifacts. See `RECOVERED_MAT_FILES.csv`. |
| Selected scripts under `cases/*/project/work/artifacts/analysis/` | Case project scripts | `image145844`, `image172647`, `image231924` | sanitized | Public-runtime patch only where needed: analysis helpers resolve to repo-local public runtime files instead of live-workspace placeholders. |
| `cases/image231924/project/` | Cold archive project folder for `image231924` | `image231924` | sanitized | Sanitized root project files, `.manager/`, `work/`, `summaries/`, `experiment_intents/`, and `data_git_20260512/`; transient lock/cache files skipped. |
| `matlab/analysis/claw_normalize_scan_image_axes.m` | `23-C/claw/claw_normalize_scan_image_axes.m` | `image231924` | public | Imaging axis normalization helper referenced by the case export contract. |
| `matlab/manifests/staging/pulsed_odmr_rabimodulated_v1.json` | `23-C/claw/sequence_manifests/staging/pulsed_odmr_rabimodulated_v1.json` | `image145844`, `image172647`, `image231924` | public | pODMR manifest referenced by project records. |
| `matlab/manifests/validated/auto__ramsey.json` | `23-C/claw/sequence_manifests/validated/auto__ramsey.json` | `image145844`, `image172647`, `image231924` | public | Ramsey manifest referenced by project records. |
| `matlab/manifests/validated/auto__cpmg.json` | `23-C/claw/sequence_manifests/validated/auto__cpmg.json` | `image172647` | public | CPMG manifest referenced by project records. |
| `matlab/sequences/SavedSequences-AWG/Rabimodulated.xml` | `23-C/SavedSequences/SavedSequences-AWG/Rabimodulated.xml` | `image145844`, `image172647`, `image231924` | public | pODMR sequence XML referenced by manifest records. |
| `matlab/sequences/SavedSequences-AWG/ramsey.xml` | `23-C/SavedSequences/SavedSequences-AWG/ramsey.xml` | `image145844`, `image172647`, `image231924` | public | Ramsey sequence XML referenced by manifest records. |
| `matlab/sequences/SavedSequences-AWG/CPMG.xml` | `23-C/SavedSequences/SavedSequences-AWG/CPMG.xml` | `image172647` | public | CPMG sequence XML referenced by project records. |
| `benchmarks/nv-checkpoint-review-2026-06/inputs/` | Built from sanitized `image145844` project wake records, memory/knowledge snapshots, and terminal Ramsey measurement artifacts | `image145844` | sanitized | Neutral checkpoint packages used for the Ramsey checkpoint benchmark. Agent-visible filenames are neutralized; later analysis notes, later measurements, and later human advice are excluded. |
| `benchmarks/nv-checkpoint-review-2026-06/prompts/task.md` | Authored for this benchmark | `image145844` | public | Exact Ramsey checkpoint task prompt. |
| `benchmarks/nv-checkpoint-review-2026-06/labels/scoring_guide.md` | Authored for this benchmark | `image145844` | public | Scoring rubric for the broader residual-offset and stricter calibration-residual scores. |
| `benchmarks/nv-checkpoint-review-2026-06/scripts/` | Authored for this benchmark | `image145844` | public | Input build, run, first-pass scoring, and figure plotting helpers. |
| `benchmarks/nv-checkpoint-review-2026-06/results/manual_rescore_codex_2026-06-30*.csv` | Manual scoring of completed Ramsey checkpoint benchmark runs | `image145844` | public | Per-run scores, scoring rationales, and checkpoint-level summaries used in the manuscript. |
| `benchmarks/nv-checkpoint-review-2026-06/results/figures/` | Derived from Ramsey checkpoint manual scores | `image145844` | public | Figure source data and rendered outputs for the Ramsey checkpoint benchmark. |
| `benchmarks/nv-checkpoint-review-2026-06/results/*/notes/` | Captured from completed Ramsey checkpoint benchmark runs | `image145844` | public | Recovered project notes used for scoring audit. Raw execution logs and full JSONL model outputs are omitted. |
| `benchmarks/podmr-model-first-resonance-2026-05/` | Built from completed pODMR measurements and benchmark runs | all | public | Main pODMR data evaluation benchmark used in the manuscript, including inputs, prompts, labels, predictions, per-run notes, figures, deterministic checks, and tool use audit. |
| `benchmarks/podmr-model-first-resonance-2026-05/results/batch_context_main_inputs_summary.*` | Derived from the appendix batch pODMR condition | all | public | Summary table for the batch comparison in which all 96 unlabeled pODMR measurements were provided in one prompt. |
| `benchmarks/podmr-model-first-resonance-2026-05/scripts/run_batch_context_main_inputs.py` | Authored for the appendix batch pODMR condition | all | public | Runner for reproducing the batch-context summary from the released pODMR inputs and prompts. |
| `benchmarks/three-model-comparison-2026-07/ramsey/` | GPT-5.4 and GPT-5.6 Sol Ramsey checkpoint runs, with the original GPT-5.5 records linked from the existing benchmark | `image145844` | sanitized | Completion audits, checkpoint summaries, per-run manual scores and rationales, and compact scoring records containing returned handoffs and project notes. Absolute user paths are placeholdered. |
| `benchmarks/three-model-comparison-2026-07/podmr/` | GPT-5.4 and GPT-5.6 Sol pODMR benchmark runs, with the original GPT-5.5 records linked from the existing benchmark | all | sanitized | Joined predictions, per-run analysis notes, replicate and case summaries, completion audits, and three model measurement bootstrap values. Absolute user paths are placeholdered. |
| `benchmarks/three-model-comparison-2026-07/scripts/build_podmr_note_records.py` | Authored for this release | all | public | Builds compact prediction and note records from joined predictions and per-run Markdown notes while replacing absolute user paths. |
| `python/openclaw_runtime/matlab_bridge_client.py` | Live workspace `matlab_bridge_client.py` | all | sanitized | Default workspace path made environment-variable based. |
| `python/openclaw_runtime/tools_mat_parse.py` | Live workspace `tools_mat_parse.py` | all | sanitized | Default MATLAB/cache paths made environment-variable based. |
| `python/openclaw_runtime/project_schema.py` | Live workspace `project_schema.py` | all | public | Project schema helper. |
| `python/openclaw_runtime/submit_spec_utils.py` | Live workspace `submit_spec_utils.py` | all | public | Submit-spec helper retained as dependency of the case-referenced enqueue and batch-run source. |
| `python/openclaw_runtime/{design_nv_sequence.py,latex_report_build.py}` | Live workspace helper scripts | all | sanitized | Sequence-design and report-build helpers referenced by the case records; local defaults made environment-variable or placeholder based. |
| `matlab/analysis/{claw_export_savedexperiment_mat_raw.m,claw_summarize_savedexperiment_mat.m,claw_analyze_saved_scan.m}` | `23-C/claw/` | all | sanitized | Savedexperiment and saved-scan analysis helpers; local cache paths made environment-variable or placeholder based. |
| `python/openclaw_nv_execution_source/` | Live workspace production Python scripts | all | sanitized | Case-referenced execution-path source copy: project manager, batch runner, bridge runtime watcher, and direct enqueue helpers. Local paths placeholdered; direct CLI execution disabled. |

## Treatment Values

- `public`: copied or authored without redaction.
- `sanitized`: copied with private/local/live-hardware details removed.
- `excerpted`: only selected sections are included.
- `omitted`: intentionally not included; explain why in notes.
