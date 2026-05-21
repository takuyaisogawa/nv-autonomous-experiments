# Method

Each run asks GPT-5.5 to classify one pODMR measurement as
`resonance_present` or `resonance_absent`.

The three prompt conditions form an ablation:

1. `context_0_protocol_only`: NV pODMR context plus protocol/XML inspection.
2. `context_A_domain_facts`: XML inspection plus contrast/Rabi/average facts.
3. `context_B_model_first`: same domain facts plus explicit quantitative
   expected-signal modeling before judgment.

Each condition is run for three replicates over the same 96 cases at four
reasoning-effort settings: `low`, `medium`, `high`, and `xhigh`. Scoring is
performed against `labels/gold_labels.csv`.

The `analysis_notes/` folders contain model-generated free-form notes written
for each run before scoring. They are included for auditability and should not
be treated as labels or ground truth.

Result folders are organized in parallel by reasoning effort:

- `results/gpt-5.5-low/`
- `results/gpt-5.5-medium/`
- `results/gpt-5.5-high/`
- `results/gpt-5.5-xhigh/`

Each reasoning-effort folder contains `context_0_protocol_only/` and
`domain_facts_vs_model_first/` subfolders with joined predictions, summary
tables, false-positive/false-negative case lists, and all per-run analysis
notes.
