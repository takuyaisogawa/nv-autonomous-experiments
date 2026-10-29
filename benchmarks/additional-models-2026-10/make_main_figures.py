"""Generate Figs. 3--5 and the supplementary scatter from frozen summaries.

The original conceptual panels remain vector artwork. No responses or labels
are changed. Run from any directory with Python, numpy, matplotlib and PyMuPDF.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
import fitz

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'reproduced/main_figures'
OUT.mkdir(parents=True, exist_ok=True)
MODELS = ['GPT-5.4', 'GPT-5.5', 'GPT-5.6 Sol', 'GPT-6.1 Sol', 'GPT-6.1 Terra', 'GPT-6 Astra']
EFFORTS = ['low', 'medium', 'high', 'xhigh']
LABELS = ['Low', 'Medium', 'High', 'X-high']
CPS = ['cp01', 'cp02', 'cp03', 'cp04', 'cp05']
COLORS = ['#009E73', '#0072B2', '#D55E00', '#CC79A7', '#333344', '#E69F00']
MARKERS = ['^', 'o', 's', 'D', 'P', 'X']
HATCHES = ['///', '', 'xxx', '...', '\\\\', '++']

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
ramsey = load(ROOT / 'data/ramsey_summary.json')
podmr = {'conditions': load(ROOT / 'data/podmr_summary.json')}
ri = {(r['model'], r['reasoning_effort'], r['checkpoint_id']): r for r in ramsey['conditions']}
pi = {(r['model'], r['context_id'], r['reasoning_effort']): r for r in podmr['conditions']}
assert len(ri) == 120 and len(pi) == 72
assert sum(r['total'] for r in ri.values()) == 2400
assert sum(r['passes'] for r in ri.values()) == 581
assert all(r['total'] == 20 for r in ri.values())
for r in pi.values():
    assert r['n'] == sum(r[k] for k in ['TP', 'TN', 'FP', 'FN']) == 288
    assert r['TP'] + r['FN'] == 72 and r['TN'] + r['FP'] == 216
    assert np.isclose(r['false_positive_rate'], r['FP'] / 216)
    assert np.isclose(r['accuracy'], (r['TP'] + r['TN']) / 288)
    for k in ['false_positive_rate', 'accuracy']:
        assert r[k + '_ci_low'] - 1e-6 <= r[k] <= r[k + '_ci_high'] + 1e-6
# Recheck the full Astra summary against the saved 3,456 predictions.
records_path = ROOT / 'podmr/gpt-6-astra/responses.jsonl'
record_source = next(s for s in load(ROOT/'provenance.json')['sources'] if s['file']=='podmr/gpt-6-astra/responses.jsonl')
assert sha(records_path) == record_source['public_sha256']
records = [json.loads(s) for s in records_path.read_text(encoding='utf-8').splitlines() if s.strip()]
assert len(records) == len({r['custom_id'] for r in records}) == 3456
for c in ['context_0', 'context_A', 'context_B']:
    for e in EFFORTS:
        group = [r for r in records if r['context_id'] == c and r['reasoning_effort'] == e]
        assert len(group) == 288 and all(r['complete'] and r['scorable'] for r in group)
        counts = Counter(r['outcome'] for r in group)
        assert all(counts[k] == pi['GPT-6 Astra', c, e][k] for k in ['TP', 'TN', 'FP', 'FN'])

plt.rcParams.update({'font.family': 'Arial', 'font.size': 8.56,
    'axes.titlesize': 8.56, 'axes.labelsize': 8.21, 'xtick.labelsize': 7.86,
    'ytick.labelsize': 7.86, 'legend.fontsize': 7.74, 'axes.linewidth': .70,
    'pdf.fonttype': 42, 'ps.fonttype': 42, 'hatch.linewidth': .8})

def axis(fig, box):
    w, h = fig.get_size_inches() * 72
    x0, y0, x1, y1 = box
    return fig.add_axes([x0/w, 1-y1/h, (x1-x0)/w, (y1-y0)/h])

def letter(fig, s, x, y):
    w, h = fig.get_size_inches() * 72
    fig.text(x/w, 1-y/h, s, ha='left', va='top', fontsize=9.97, fontweight='bold')

def style(ax):
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#D9D9D9', lw=.53, alpha=.8)
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(length=3.5, width=.8, pad=1.9)

def finish(fig, name, schematic=None, clip=None, destination=None):
    temporary = OUT / (name + '_panels.pdf')
    fig.savefig(temporary)
    plt.close(fig)
    doc = fitz.open(temporary)
    if schematic:
        source = fitz.open(schematic)
        page = source[0]
        # Remove artwork outside the retained panel, including hidden old labels.
        c = fitz.Rect(clip)
        for rect in [fitz.Rect(c.x1, 0, page.rect.width, page.rect.height),
                     fitz.Rect(0, c.y1, page.rect.width, page.rect.height)]:
            if not rect.is_empty:
                page.add_redact_annot(rect, fill=(1, 1, 1))
        page.apply_redactions(images=2, graphics=1, text=0)
        doc[0].show_pdf_page(fitz.Rect(destination or clip), source, 0, clip=c, keep_proportion=True)
        source.close()
    doc.set_metadata({'title': name.replace('_', ' '), 'creator': 'Matplotlib and PyMuPDF',
                      'subject': 'Six models; frozen benchmark results; original vector schematic'})
    target = OUT / (name + '.pdf')
    doc.save(target, garbage=4, deflate=True)
    doc.close()
    temporary.unlink()
    with fitz.open(target) as d:
        d[0].get_pixmap(matrix=fitz.Matrix(2, 2)).save(target.with_suffix('.png'))

# Figure 3: retain the top-row arrangement; add a second row of heat maps.
W, H = 595.276, 510
fig = plt.figure(figsize=(W/72, H/72), facecolor='white')
ax = axis(fig, (308.3, 60, 564.2, 164))
x = np.arange(4)
for i, m in enumerate(MODELS):
    counts = [sum(ri[m, e, c]['passes'] for c in CPS) for e in EFFORTS]
    bars = ax.bar(x+(i-2.5)*.13, np.array(counts)/100, width=.13,
                  color=COLORS[i], hatch=HATCHES[i], edgecolor='white', lw=.45, label=m, zorder=3)
    for b, count in zip(bars, counts):
        ax.text(b.get_x()+b.get_width()/2, b.get_height()+.012, str(count), ha='center',
                va='bottom', fontsize=6.1, color='#263238')
ax.set(xticks=x, xticklabels=LABELS, ylim=(0, .65), yticks=np.arange(0, .61, .1),
       xlabel='Reasoning effort', ylabel='Pass rate')
ax.xaxis.labelpad=1; ax.yaxis.labelpad=1.2
style(ax)
ax.legend(ncol=2, frameon=False, loc='upper center', bbox_to_anchor=(440/W, 1-3/H),
          bbox_transform=fig.transFigure, columnspacing=1.3, handlelength=1.7, handletextpad=.45)
letter(fig, 'b', 293.6, 7)
cmap = LinearSegmentedColormap.from_list('ramsey', ['#F3F6F8', '#B8DDE8', '#2A91B8', '#1F5A7A'])
for i, m in enumerate(MODELS):
    row, col = divmod(i, 3)
    x0 = [52.3, 226.55, 400.79][col]
    y0 = [220, 380][row]
    a = axis(fig, (x0, y0, x0+140.18, y0+100))
    v = np.array([[ri[m, e, c]['passes'] for c in CPS] for e in EFFORTS])
    im = a.imshow(v/20, vmin=0, vmax=1, cmap=cmap, aspect='auto', interpolation='nearest')
    a.set_title(m, pad=5.86)
    a.set_xticks(range(5), CPS); a.set_yticks(range(4), LABELS)
    a.set_xlabel('Checkpoint', labelpad=4.2)
    if col == 0: a.set_ylabel('Reasoning effort', labelpad=4.2)
    a.tick_params(length=0, pad=1.88)
    for sp in a.spines.values(): sp.set_visible(False)
    for yy in range(4):
        for xx in range(5):
            a.text(xx, yy, f'{v[yy,xx]}/20', ha='center', va='center', fontsize=6.8,
                   color='white' if v[yy,xx]/20 > .58 else '#263238')
    letter(fig, chr(99+i), x0-9.76, y0-17.5)
ca = axis(fig, (552.97, 220, 558.58, 480))
cb = fig.colorbar(im, cax=ca); cb.set_label('Pass rate', labelpad=4.2)
cb.ax.tick_params(length=2.9, width=.8, labelsize=7.5, pad=1.76)
finish(fig, 'figure3_ramsey_benchmark', ROOT/'figure_sources/figure3_original.pdf', (0, 0, 276, 174))

# Figure 4: retain the left-hand conceptual panel and three-by-two result panels.
W, H = 595.276, 335
fig = plt.figure(figsize=(W/72, H/72), facecolor='white')
axes = []
for row, metric in enumerate(['false_positive_rate', 'accuracy']):
    for col, (context, title) in enumerate(zip(['context_0', 'context_A', 'context_B'],
                                              ['Sequence only', 'Setup information', 'Expected signal'])):
        x0 = [280, 390, 500][col]
        y0, y1 = [(27, 141), (194, 304)][row]
        a = axis(fig, (x0, y0, x0+89, y1)); axes.append(a)
        for i, m in enumerate(MODELS):
            vals = [pi[m, context, e] for e in EFFORTS]
            v = np.array([r[metric] for r in vals])*100
            lo = np.array([r[metric+'_ci_low'] for r in vals])*100
            hi = np.array([r[metric+'_ci_high'] for r in vals])*100
            a.errorbar(x+(i-2.5)*.038, v, yerr=np.maximum(0, np.vstack([v-lo, hi-v])),
                       color=COLORS[i], marker=MARKERS[i], ms=3.4, lw=1.05,
                       elinewidth=.48, capsize=1.4, label=m, zorder=3)
        a.set(xticks=x, xticklabels=LABELS, xlim=(-.3, 3.3))
        a.tick_params(axis='x', labelsize=6.7)
        if row == 0:
            a.set(ylim=(-1, 65), yticks=[0,20,40,60]); a.set_title(title, pad=7)
            a.set_xticklabels([])
        else:
            a.set(ylim=(50,102), yticks=[50,60,70,80,90,100], xlabel='Reasoning effort')
            a.xaxis.label.set_size(7.5)
        if col == 0: a.set_ylabel('False positive rate (%)' if row == 0 else 'Accuracy (%)', labelpad=2)
        else: a.set_yticklabels([])
        style(a)
        letter(fig, chr(98+row*3+col), x0-6, y0-21)
fig.legend(*axes[0].get_legend_handles_labels(), ncol=2, frameon=False, loc='upper center',
           bbox_to_anchor=(140/W, 1-280/H), columnspacing=1.5, handlelength=1.8, handletextpad=.5)
finish(fig, 'figure4_podmr_benchmark', ROOT/'figure_sources/figure4_original.pdf',
       (0, 0, 250, 238.615), (0, 4, 250, 242.615))

# Figure 5 and the supplementary raw scatter use exactly the same 24 pairs.
points = [{'model':m, 'effort':e, 'ramsey':sum(ri[m,e,c]['passes'] for c in CPS)/100,
           'fpr':pi[m,'context_0',e]['FP']/216} for m in MODELS for e in EFFORTS]
x = np.array([p['ramsey'] for p in points]); y = np.array([p['fpr'] for p in points])
xc=x.copy(); yc=y.copy(); mid=np.array([p['model'] for p in points])
individual=[]
for m in MODELS:
    s=mid==m; xc[s]-=x[s].mean(); yc[s]-=y[s].mean()
    individual.append({'model':m, 'pearson_r':float(np.corrcoef(x[s],y[s])[0,1])})
r=float(np.corrcoef(xc,yc)[0,1]); raw_r=float(np.corrcoef(x,y)[0,1])
slope=float(xc@yc/(xc@xc))
assert np.isclose(r, .805902520619575)
for centered, name in [(True, 'figure5_benchmark_relationship'), (False, 'benchmark_observed_rates')]:
    W,H=440,345
    fig=plt.figure(figsize=(W/72,H/72),facecolor='white')
    a=axis(fig,(65,63,426,270))
    xx,yy=(xc*100,yc*100) if centered else (x*100,y*100)
    for i,m in enumerate(MODELS):
        for j,e in enumerate(EFFORTS):
            q=i*4+j
            a.scatter(xx[q], yy[q], color=COLORS[i], marker=['o','s','^','D'][j],
                      s=36, edgecolor='white', linewidth=.35, zorder=4)
    if centered:
        a.axvline(0,color='#999999',lw=.6); a.axhline(0,color='#999999',lw=.6)
        line=np.array([-25,20]); a.plot(line,line*slope,'--',color='#666666',lw=.85)
        a.set(xlim=(-25,20),ylim=(-25,25),
              xlabel='Ramsey pass rate minus model mean\n(percentage points)',
              ylabel='False positive rate minus model mean\n(percentage points)')
    else:
        a.set(xlim=(0,60),ylim=(0,60),xlabel='Ramsey pass rate (%)',ylabel='False positive rate (%)')
    a.text(.04,.95,f'$r = {r if centered else raw_r:.3f}$',transform=a.transAxes,va='top')
    style(a)
    handles=[Line2D([],[],color=c,marker='o',ls='',ms=5,label=m) for m,c in zip(MODELS,COLORS)]
    fig.legend(handles=handles,loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(.53,.995),
               columnspacing=1.4,handletextpad=.45)
    handles=[Line2D([],[],color='#444444',marker=k,ls='',ms=5,label=e) for k,e in zip(['o','s','^','D'],LABELS)]
    fig.legend(handles=handles,loc='lower center',ncol=4,frameon=False,bbox_to_anchor=(.53,.005))
    finish(fig,name)

analysis={'ramsey_responses':2400,'ramsey_passes':581,'podmr_judgments':sum(r['n'] for r in pi.values()),
          'centered_r':r,'raw_r':raw_r,'slope':slope,'points':points,
          'individual_correlations':individual,
          'leave_one_model_out':{m:float(np.corrcoef(xc[mid!=m],yc[mid!=m])[0,1]) for m in MODELS},
          'model_effort_pass_counts':{m:[sum(ri[m,e,c]['passes'] for c in CPS) for e in EFFORTS] for m in MODELS},
          'checkpoint_pass_counts':{c:sum(ri[m,e,c]['passes'] for m in MODELS for e in EFFORTS) for c in CPS}}
(OUT/'analysis.json').write_text(json.dumps(analysis,indent=2)+'\n',encoding='utf-8')
sources=[*sorted((ROOT/'data').glob('*.json')),*sorted((ROOT/'figure_sources').glob('*.pdf')),Path(__file__)]
provenance={'sources':{p.relative_to(ROOT).as_posix():sha(p) for p in sources}, 'outputs':{p.name:sha(p) for p in sorted(OUT.glob('*.pdf'))},
            'responses_and_scores_modified':False,'bootstrap_intervals':'Retained from the verified comparison summaries.'}
(OUT/'figure_provenance.json').write_text(json.dumps(provenance,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:analysis[k] for k in ['ramsey_responses','ramsey_passes','podmr_judgments','centered_r','raw_r']}))
print(OUT)
