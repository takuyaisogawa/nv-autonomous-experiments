"""Rebuild manuscript Fig. 3 with frozen v6 judgments, preserving its layout."""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

import fitz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reproduced'
TMP = OUT / 'tmp'
PAPER = ROOT / 'figures/figure3_previous.pdf'
PLOT_SOURCE = ROOT.parents[1] / 'scripts/make_ramsey_checkpoint_benchmark.py'


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    batch = ROOT
    report_path = ROOT / 'legacy_comparison/comparison.json'
    report = load(report_path)
    assert load(batch / 'final_verification.json')['completed']
    rows = report['cases']
    assert len(rows) == 1200 and len({r['case_id'] for r in rows}) == 1200
    spec = importlib.util.spec_from_file_location('paper_plot', PLOT_SOURCE)
    paper_plot = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(paper_plot)
    models = paper_plot.MODELS
    efforts = paper_plot.EFFORTS
    checkpoints = paper_plot.CHECKPOINTS
    display = dict(zip(['gpt-5.4', 'gpt-5.5', 'gpt-5.6-sol'], models))
    buckets = defaultdict(list)
    for r in rows:
        assert r['new'] in ('PASS', 'FAIL')
        buckets[(display[r['model']], r['reasoning_effort'], r['checkpoint_id'])].append(r['new'])
    assert len(buckets) == 60 and all(len(v) == 20 for v in buckets.values())
    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    summary_path = OUT / 'v6_checkpoint_summary.csv'
    fields = ['model', 'criterion_group', 'reasoning_effort', 'checkpoint_id', 'passes', 'total', 'pass_rate']
    summary_rows = []
    for m in models:
        for e in efforts:
            for cp in checkpoints:
                v = buckets[(m, e, cp)]
                p = v.count('PASS')
                summary_rows.append(dict(zip(fields, [m, 'calibration-residual', e, cp, p, 20, p / 20])))
    assert sum(r['passes'] for r in summary_rows) == 269
    with summary_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary_rows)
    summary = paper_plot.load_summary(summary_path)

    # The publication PDF was laid out in Illustrator after the original plotting
    # script. Use its page dimensions and measured panel locations exactly.
    source = fitz.open(PAPER)
    W, H = source[0].rect.width, source[0].rect.height
    paper_plot.configure_matplotlib()
    plt.rcParams.update({
        'font.size': 8.5621, 'axes.titlesize': 8.5621,
        'axes.labelsize': 8.2103, 'xtick.labelsize': 7.8584,
        'ytick.labelsize': 7.8584, 'legend.fontsize': 7.7411,
        'axes.linewidth': .704, 'hatch.linewidth': 1.1729,
    })
    fig = plt.figure(figsize=(W / 72, H / 72), facecolor='white')

    def add_axis(x0, y0, x1, y1):
        return fig.add_axes([x0 / W, 1 - y1 / H, (x1 - x0) / W, (y1 - y0) / H])

    def label(letter, x, y):
        fig.text(x / W, 1 - y / H, letter, ha='left', va='top',
                 fontsize=9.9696, fontweight='bold', color='#111111')

    ax = add_axis(308.2763, 42.9425, 564.2373, 146.4335)
    x = np.arange(4)
    for i, (model, color, hatch) in enumerate(zip(models, paper_plot.MODEL_COLORS, paper_plot.MODEL_HATCHES)):
        passes = [sum(summary[(model, e, cp)]['passes'] for cp in checkpoints) for e in efforts]
        assert all(sum(summary[(model, e, cp)]['total'] for cp in checkpoints) == 100 for e in efforts)
        bars = ax.bar(x + (i - 1) * .24, np.array(passes) / 100, width=.24,
                      color=color, edgecolor='white', linewidth=.528, hatch=hatch,
                      label=model, zorder=3)
        for bar, count in zip(bars, passes):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + .013,
                    str(count), ha='center', va='bottom', fontsize=6.4509, color='#263238')
    ax.set_xticks(x, paper_plot.EFFORT_LABELS)
    ax.set_xlabel('Reasoning effort', labelpad=1.0)
    ax.set_ylabel('Pass rate', labelpad=1.2)
    ax.set_ylim(0, .65)
    ax.set_yticks(np.arange(0, .61, .1))
    paper_plot.style_bar_axis(ax)
    ax.tick_params(length=3.52, width=.821, pad=1.88)
    ax.yaxis.grid(True, color='#D9D9D9', lw=.528, alpha=.8)
    ax.legend(ncol=3, frameon=False, loc='center', bbox_to_anchor=(436.25 / W, 1 - 22 / H),
              bbox_transform=fig.transFigure, columnspacing=1.1, handlelength=1.6,
              handletextpad=.35, borderpad=0)
    label('b', 293.61, 7.0)

    cmap = LinearSegmentedColormap.from_list('ramsey_pass_rate',
        ['#F3F6F8', '#B8DDE8', '#2A91B8', '#1F5A7A'])
    image = None
    for i, model in enumerate(models):
        x0 = [52.3156, 226.5517, 400.7878][i]
        axis = add_axis(x0, 195.7091, x0 + 140.1842, 308.0253)
        matrix = np.array([[summary[(model, e, cp)]['pass_rate'] for cp in checkpoints] for e in efforts])
        image = axis.imshow(matrix, vmin=0, vmax=1, cmap=cmap, aspect='auto', interpolation='nearest')
        axis.set_title(model, pad=5.86)
        axis.set_xticks(np.arange(5), checkpoints)
        axis.set_yticks(np.arange(4), paper_plot.EFFORT_LABELS)
        axis.set_xlabel('Checkpoint', labelpad=4.2)
        if i == 0:
            axis.set_ylabel('Reasoning effort', labelpad=4.2)
        axis.tick_params(length=0, pad=1.88)
        for spine in axis.spines.values():
            spine.set_visible(False)
        for ri, effort in enumerate(efforts):
            for ci, cp in enumerate(checkpoints):
                count = summary[(model, effort, cp)]['passes']
                axis.text(ci, ri, f'{count}/20', ha='center', va='center', fontsize=6.8028,
                          color='white' if matrix[ri, ci] > .58 else '#263238')
        label(chr(ord('c') + i), x0 - 9.76, 178.2)
    cax = add_axis(552.9747, 196.0033, 558.5757, 308.0253)
    colorbar = fig.colorbar(image, cax=cax)
    colorbar.set_label('Pass rate', labelpad=4.2)
    colorbar.ax.tick_params(length=2.93, width=.821, labelsize=7.5065, pad=1.76)
    quantitative = TMP / 'v6_quantitative_panels.pdf'
    fig.savefig(quantitative, metadata={'Title': 'Ramsey checkpoint benchmark: v6 LLM judge'})
    plt.close(fig)

    # Retain panel (a) as vector artwork from the paper. Remove the other panels
    # from a temporary copy so superseded numeric labels cannot remain hidden.
    schematic = fitz.open(PAPER)
    sp = schematic[0]
    sp.add_redact_annot(fitz.Rect(276, 0, W, H), fill=(1, 1, 1))
    sp.add_redact_annot(fitz.Rect(0, 174, W, H), fill=(1, 1, 1))
    sp.apply_redactions(images=2, graphics=1, text=0)
    output = fitz.open(quantitative)
    clip = fitz.Rect(0, 0, 276, 174)
    output[0].show_pdf_page(clip, schematic, 0, clip=clip, keep_proportion=False)
    output.set_metadata({
        'title': 'Ramsey checkpoint benchmark: v6 LLM judge',
        'subject': 'GPT-6.1 Sol/high; 1200 independent judgments; v6 prompt; 269 PASS. Layout matches manuscript Fig. 3.',
        'creator': 'Matplotlib and PyMuPDF; original manuscript vector schematic',
    })
    final = OUT / 'figure3_ramsey_benchmark_v6.pdf'
    output.save(final, garbage=4, deflate=True)
    output.close()
    schematic.close()
    source.close()
    provenance = {
        'judge': 'gpt-6.1-sol', 'judge_reasoning_effort': 'high', 'judge_prompt': 'v6',
        'n': 1200, 'pass': 269, 'per_bar_n': 100, 'per_heatmap_cell_n': 20,
        'report': str(report_path), 'report_sha256': sha(report_path),
        'source_figure': str(PAPER), 'source_figure_sha256': sha(PAPER),
        'plot_code_reference': str(PLOT_SOURCE), 'plot_code_reference_sha256': sha(PLOT_SOURCE),
        'summary_csv': str(summary_path), 'summary_sha256': sha(summary_path),
        'figure': str(final), 'figure_sha256': sha(final),
        'model_effort_pass_counts': {m: [sum(summary[(m,e,cp)]['passes'] for cp in checkpoints) for e in efforts] for m in models},
        'scoring_outputs_modified': False, 'manuscript_modified': False,
    }
    (OUT / 'figure_provenance.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(provenance, indent=2))


if __name__ == '__main__':
    main()
