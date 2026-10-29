# Reproducing the Earlier Three-Model Figures

The current manuscript uses six models in Figs. 3–5. See the
[current figure instructions](../additional-models-2026-10/#reproduce-the-analysis-and-figures).
This guide preserves the earlier three-model figures.

This workflow reconstructs the quantitative panels and final layouts of
manuscript Figs. 3 and 4.  It reads the released benchmark source tables and
reuses the existing vector artwork for panels 3a and 4a.

## Three-Model Figure 3 (LLM judge)

This version uses [LLM-judge scores](ramsey/llm_judge/). Reproduce the
counts and the updated Figure 3 from the repository root with:

```shell
python benchmarks/three-model-comparison-2026-07/ramsey/llm_judge/scripts/reproduce.py
python benchmarks/three-model-comparison-2026-07/ramsey/llm_judge/scripts/make_figure.py
```

Outputs are written to `ramsey/llm_judge/reproduced/`. The commands below
retain the previous Figure 3 and the unchanged Figure 4 workflow.

## Inputs for the previous Figure 3 and Figure 4

- `ramsey/three_model_checkpoint_summary.csv`
- `podmr/three_model_case_bootstrap.csv`
- `figure_sources/fig_autoNV_overview_v5_0.pdf`

The plotting scripts validate that all expected combinations of model,
reasoning effort, checkpoint, and prompt condition are present before drawing
the figures.

## Environment

The scripts require Python 3.10 or later and the packages in the repository
root `requirements.txt`.

On Windows, the complete case archive contains paths longer than the default
Git checkout limit.  Enable long paths before cloning:

```powershell
git config --global core.longpaths true
```

Create an environment from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with
`source .venv/bin/activate` or replace `.\.venv\Scripts\python` below with
`.venv/bin/python`.

## Commands

From the repository root:

```powershell
.\.venv\Scripts\python benchmarks\three-model-comparison-2026-07\scripts\make_ramsey_checkpoint_benchmark.py
.\.venv\Scripts\python benchmarks\three-model-comparison-2026-07\scripts\make_podmr_benchmark_summary.py
.\.venv\Scripts\python benchmarks\three-model-comparison-2026-07\scripts\compose_benchmark_figures.py
```

The first two commands generate data-panel trial PDFs directly from the
released CSV files.  The third command clips the existing vector artwork into
the reserved panel-a regions without redrawing it.

## Outputs

The scripts write the following files under
`benchmarks/three-model-comparison-2026-07/reproduced/`:

- `figure3_data_panels_trial.pdf` and `.png`
- `figure4_data_panels_trial.pdf` and `.png`
- `figure3_ramsey_benchmark.pdf` and `.png`
- `figure4_podmr_benchmark.pdf` and `.png`

The PDF outputs preserve vector text, lines, markers, and source artwork.  The
PNG outputs are rendered at 300 dpi for visual comparison.
