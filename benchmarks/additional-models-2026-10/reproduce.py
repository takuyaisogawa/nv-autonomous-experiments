"""Recompute additional-model results and manuscript figures from saved records."""
from pathlib import Path
from collections import Counter
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
import fitz

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'reproduced'; OUT.mkdir(exist_ok=True)
MODELS=['GPT-5.4','GPT-5.5','GPT-5.6 Sol','GPT-6.1 Sol','GPT-6.1 Terra','GPT-6 Astra']
IDS=['gpt-6.1-sol','gpt-6.1-terra','gpt-6-astra']
EFFORTS=['low','medium','high','xhigh']; LABELS=['Low','Medium','High','X-high']
CPS=['cp01','cp02','cp03','cp04','cp05']
COLORS=['#009E73','#0072B2','#D55E00','#CC79A7','#333344','#E69F00']
MARKERS=['^','o','s','D','P','X']; HATCHES=['///','','xxx','...','\\\\','++']
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def lines(p):return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines() if s.strip()]
def save(name,o):(OUT/name).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
ramsey=load(ROOT/'data/ramsey_summary.json')
podmr=load(ROOT/'data/podmr_summary.json')
seq=load(ROOT/'data/sequence_summary.json')
ri={(r['model'],r['reasoning_effort'],r['checkpoint_id']):r for r in ramsey['conditions']}
si={(r['model'],r['reasoning_effort']):r for r in seq}
pi={(r['model'],r['context_id'],r['reasoning_effort']):r for r in podmr}
assert len(ri)==120 and len(si)==24 and len(pi)==60
new_counts={}
for model,mid in zip(MODELS[3:],IDS):
    rr=lines(ROOT/'ramsey'/mid/'responses.jsonl'); jj=load(ROOT/'ramsey'/mid/'judgments.json')
    assert len(rr)==len(jj)==400 and len({r['custom_id'] for r in jj})==400
    assert {r['custom_id'] for r in rr}=={r['custom_id'] for r in jj}
    assert len({(r['checkpoint_id'],r['reasoning_effort'],r['replicate']) for r in rr})==400
    for e in EFFORTS:
        for cp in CPS:
            group=[r for r in jj if r['reasoning_effort']==e and r['checkpoint_id']==cp]
            assert len(group)==20
            assert sum(r['verdict']=='PASS' for r in group)==ri[model,e,cp]['passes']
    pp=lines(ROOT/'podmr'/mid/'responses.jsonl')
    assert len(pp)==(864 if mid=='gpt-6-astra' else 3456)
    assert len({(r['case_id'],r['context_id'],r['reasoning_effort'],r['replicate']) for r in pp})==len(pp)
    for c in (['context_0'] if mid=='gpt-6-astra' else ['context_0','context_A','context_B']):
        for e in EFFORTS:
            group=[r for r in pp if r['context_id']==c and r['reasoning_effort']==e]
            ct=Counter(r['outcome'] for r in group)
            assert ct['FP']+ct['TN']==216
            if mid!='gpt-6-astra':
                assert len(group)==288 and ct['TP']+ct['FN']==72
                assert all(ct[k]==pi[model,c,e][k] for k in ['TP','TN','FP','FN'])
            if c=='context_0':assert ct['FP']==si[model,e]['FP']
    new_counts[model]={'ramsey':len(rr),'podmr':len(pp)}

# Preserve published bootstrap intervals for five models; add Astra with the same procedure.
for model in MODELS[:5]:
    for e in EFFORTS:
        row=pi[model,'context_0',e]
        for k in ['false_positive_rate_ci_low','false_positive_rate_ci_high']:si[model,e][k]=row[k]
rng=np.random.default_rng(20261028)
astra=lines(ROOT/'podmr/gpt-6-astra/responses.jsonl')
for e in EFFORTS:
    rr=[r for r in astra if r['reasoning_effort']==e]
    ids=sorted({r['case_id'] for r in rr});assert len(ids)==72
    vals=[]
    for cid in ids:
        g=[r for r in rr if r['case_id']==cid]
        assert len(g)==3 and all(r['gold_label']=='absent' for r in g)
        vals.append(sum(r['outcome']=='FP' for r in g)/3)
    vals=np.array(vals)
    lo,hi=np.quantile(vals[rng.integers(0,72,size=(20000,72))].mean(axis=1),[.025,.975])
    si['GPT-6 Astra',e].update(false_positive_rate_ci_low=float(lo),false_positive_rate_ci_high=float(hi))

points=[]
for m in MODELS:
    for e in EFFORTS:
        points.append({'model':m,'effort':e,'ramsey':sum(ri[m,e,c]['passes'] for c in CPS)/100,
                       'fpr':si[m,e]['FP']/216})
x=np.array([r['ramsey'] for r in points]); y=np.array([r['fpr'] for r in points])
xc=x.copy();yc=y.copy();mid=np.array([r['model'] for r in points]);individual=[]
for m in MODELS:
    s=mid==m;xc[s]-=x[s].mean();yc[s]-=y[s].mean()
    individual.append({'model':m,'pearson_r':float(np.corrcoef(x[s],y[s])[0,1])})
r=float(np.corrcoef(xc,yc)[0,1]);slope=float(xc@yc/(xc@xc))
leave=[float(np.corrcoef(xc[mid!=m],yc[mid!=m])[0,1]) for m in MODELS]
assert np.isclose(r,.8059025206195752)
save('analysis.json',{'verified_additional_counts':new_counts,'sequence':list(si.values()),'points':points,
     'individual_correlations':individual,'centered_r':r,'uncentered_r':float(np.corrcoef(x,y)[0,1]),
     'slope':slope,'leave_one_model_out':dict(zip(MODELS,leave)),
     'astra_bootstrap':{'seed':20261028,'resamples':20000,'unit':'measurement, with all three repetitions'}})

plt.rcParams.update({'font.family':'Arial','font.size':8,'axes.titlesize':8,'axes.labelsize':8,
 'xtick.labelsize':7,'ytick.labelsize':7,'legend.fontsize':7,'axes.linewidth':.6,'pdf.fonttype':42,
 'ps.fonttype':42,'hatch.linewidth':.6})
def style(ax):
    ax.spines[['top','right']].set_visible(False);ax.set_axisbelow(True)
    ax.grid(axis='y',color='#D9D9D9',lw=.45,alpha=.8)
    ax.tick_params(length=3,width=.7,pad=2)
def label(ax,s):ax.text(-.07,1.08,s,transform=ax.transAxes,fontweight='bold',fontsize=10)
def export(fig,name):
    fig.savefig(OUT/(name+'.pdf'));plt.close(fig)
    d=fitz.open(OUT/(name+'.pdf'));d[0].get_pixmap(matrix=fitz.Matrix(2,2)).save(OUT/(name+'.png'));d.close()

# Supplementary performance figures show only the three additional models.
# The original three models remain in the main-text figures.
extra=MODELS[3:]
fig=plt.figure(figsize=(7,3.9))
gs=fig.add_gridspec(2,3,height_ratios=[1,1],left=.095,right=.89,top=.86,bottom=.10,hspace=.82,wspace=.30)
ax=fig.add_subplot(gs[0,:]);xx=np.arange(4)
for j,m in enumerate(extra):
    i=MODELS.index(m)
    vals=[sum(ri[m,e,c]['passes'] for c in CPS) for e in EFFORTS]
    bars=ax.bar(xx+(j-1)*.23,np.array(vals)/100,width=.23,color=COLORS[i],hatch=HATCHES[i],edgecolor='white',lw=.4,label=m)
    for b,v in zip(bars,vals):ax.text(b.get_x()+b.get_width()/2,b.get_height()+.012,str(v),ha='center',fontsize=7)
ax.set(xticks=xx,xticklabels=LABELS,ylim=(0,.65),yticks=np.arange(0,.61,.2),ylabel='Pass rate',xlabel='Reasoning effort');style(ax);label(ax,'a')
fig.legend(*ax.get_legend_handles_labels(),loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(.5,1))
cmap=LinearSegmentedColormap.from_list('ramsey',['#F3F6F8','#B8DDE8','#2A91B8','#1F5A7A'])
for j,m in enumerate(extra):
    a=fig.add_subplot(gs[1,j]);v=np.array([[ri[m,e,c]['passes'] for c in CPS] for e in EFFORTS])
    im=a.imshow(v/20,vmin=0,vmax=1,cmap=cmap,aspect='auto');a.set_title(m,pad=6)
    a.set_xticks(range(5),CPS);a.set_yticks(range(4),LABELS);a.tick_params(length=0,pad=2)
    a.set_xlabel('Checkpoint')
    if j==0:a.set_ylabel('Reasoning effort')
    for sp in a.spines.values():sp.set_visible(False)
    for yy in range(4):
        for xx in range(5):a.text(xx,yy,f'{v[yy,xx]}/20',ha='center',va='center',fontsize=6,color='white' if v[yy,xx]>=13 else '#263238')
    label(a,chr(98+j))
ca=fig.add_axes([.91,.10,.012,.28]);fig.colorbar(im,cax=ca,label='Pass rate')
export(fig,'additional_ramsey')

fig,axes=plt.subplots(1,3,figsize=(7,2.65),sharey=True)
fig.subplots_adjust(left=.09,right=.98,bottom=.21,top=.72,wspace=.18)
for j,(ax,c,title) in enumerate(zip(axes,['context_0','context_A','context_B'],['Sequence only','Setup information','Expected signal'])):
    for k,m in enumerate(extra if c=='context_0' else extra[:2]):
        i=MODELS.index(m)
        rows=[si[m,e] if c=='context_0' else pi[m,c,e] for e in EFFORTS]
        v=np.array([z['false_positive_rate'] for z in rows])*100
        lo=np.array([z['false_positive_rate_ci_low'] for z in rows])*100;hi=np.array([z['false_positive_rate_ci_high'] for z in rows])*100
        ax.errorbar(np.arange(4)+(k-1)*.055,v,yerr=np.maximum(0,np.vstack([v-lo,hi-v])),
                    color=COLORS[i],marker=MARKERS[i],ms=4,lw=1.1,elinewidth=.6,capsize=1.7,label=m)
    ax.set(xticks=range(4),xticklabels=LABELS,xlim=(-.3,3.3),ylim=(0,22),yticks=[0,5,10,15,20],xlabel='Reasoning effort',title=title)
    style(ax);label(ax,chr(97+j))
axes[0].set_ylabel('False positive rate (%)')
fig.legend(*axes[0].get_legend_handles_labels(),loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(.5,1))
export(fig,'additional_podmr_sequence')

# Display the raw association and the association within models, not a duplicate zoom.
fig,axes=plt.subplots(1,2,figsize=(7,3.5))
fig.subplots_adjust(left=.10,right=.98,top=.77,bottom=.25,wspace=.40)
raw_r=float(np.corrcoef(x,y)[0,1])
for j,(a,xx,yy) in enumerate(zip(axes,[x*100,xc*100],[y*100,yc*100])):
    for i,m in enumerate(MODELS):
        for k,e in enumerate(EFFORTS):
            q=next(q for q,p in enumerate(points) if p['model']==m and p['effort']==e)
            a.scatter(xx[q],yy[q],c=COLORS[i],marker=['o','s','^','D'][k],s=27,edgecolors='white',linewidth=.3,zorder=3)
    if j==0:
        a.set(xlim=(0,60),ylim=(0,60),xlabel='Ramsey pass rate (%)',ylabel='False positive rate (%)',title='Observed rates')
    else:
        a.axhline(0,color='#999999',lw=.6);a.axvline(0,color='#999999',lw=.6)
        line=np.linspace(-25,20,100);a.plot(line,slope*line,'--',color='#666666',lw=.8)
        a.set(xlim=(-25,20),ylim=(-25,25),xlabel='Ramsey pass rate minus model mean\n(percentage points)',ylabel='False positive rate minus model mean\n(percentage points)',title='After subtracting model means')
    a.text(.04,.95,f'$r={[raw_r,r][j]:.3f}$',transform=a.transAxes,va='top');style(a);label(a,chr(97+j))
handles=[Line2D([],[],color=c,marker='o',ls='',ms=4,label=m) for m,c in zip(MODELS,COLORS)]
fig.legend(handles=handles,loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(.5,1.01))
eh=[Line2D([],[],color='#444444',marker=k,ls='',ms=4,label=e) for k,e in zip(['o','s','^','D'],LABELS)]
fig.legend(handles=eh,loc='lower center',ncol=4,frameon=False,bbox_to_anchor=(.5,.005))
export(fig,'additional_benchmark_correlation')

# Tables use the same columns and percentage formatting as Supplementary Table S1.
rows=[]
for c,title in [('context_0','Sequence only'),('context_A','Setup information'),('context_B','Expected signal')]:
    rows.append(r'\multicolumn{8}{l}{\textbf{'+title+r'}} \\')
    for m in MODELS[3:5]:
        for e in EFFORTS:
            z=pi[m,c,e]
            fpr=f"{100*z['false_positive_rate']:.1f} [{100*z['false_positive_rate_ci_low']:.1f}, {100*z['false_positive_rate_ci_high']:.1f}]"
            acc=f"{100*z['accuracy']:.1f} [{100*z['accuracy_ci_low']:.1f}, {100*z['accuracy_ci_high']:.1f}]"
            rows.append(' & '.join([m,e]+[str(z[k]) for k in ['TP','TN','FP','FN']]+[fpr,acc])+r' \\')
    rows.append(r'\midrule')
(OUT/'podmr_table_rows.tex').write_text('\n'.join(rows[:-1])+'\n',encoding='utf-8')
(OUT/'correlation_table_rows.tex').write_text('\n'.join(f"{z['model']} & {z['pearson_r']:.3f}"+r' \\' for z in individual)+'\n',encoding='utf-8')
print(json.dumps({'centered_r':r,'raw_r':float(np.corrcoef(x,y)[0,1]),'leave_range':[min(leave),max(leave)],'counts':new_counts}))
