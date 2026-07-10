#!/usr/bin/env python3
from __future__ import annotations
import json, math, shutil, subprocess, sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ID='nv23_aligned_nv_t2star_13c_image145844_20260513_1507'
PROJECT=Path('<OPENCLAW_WORKSPACE>/.openclaw/projects')/PROJECT_ID
AN=PROJECT/'work/artifacts/analysis'
FIGS=PROJECT/'work/artifacts/figures'
BRJ=PROJECT/'work/bridge_jobs'
JOB_ID='nv23_pulsed_odmr_rabimodulated_v1_20260514_044105_pulsed_odmr_rabimodulated_v1'
BATCH_ID='nv23_pulsed_odmr_rabimodulated_v1_20260514_043948'
DONE_DIR=Path('<NV_BRIDGE_ROOT>/done')/JOB_ID
BATCH_ROOT=Path('<OPENCLAW_WORKSPACE>/.openclaw/single_submit/batches')
MAT_PATH=Path('<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-14-044122.mat')
XML_PATH=Path('<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/Rabimodulated.xml')
AN.mkdir(parents=True, exist_ok=True); FIGS.mkdir(parents=True, exist_ok=True); BRJ.mkdir(parents=True, exist_ok=True)
ts=datetime.now(ZoneInfo('America/New_York')).strftime('%Y%m%d_%H%M')

if not DONE_DIR.exists():
    raise SystemExit(f'missing terminal done dir: {DONE_DIR}')
if not MAT_PATH.exists():
    raise SystemExit(f'missing savedexperiment MAT: {MAT_PATH}')

copied=[]
for src_name, dest_suffix in [
    ('job.json','job.json'),('control.json','control.json'),('result.json','result.json'),
    ('status.json','status.json'),('bridge.log','bridge.log'),('matlab_command_window.log','matlab_command_window.log')]:
    src=DONE_DIR/src_name
    if src.exists():
        dest=BRJ/f'{JOB_ID}.{dest_suffix}'
        shutil.copy2(src,dest)
        copied.append(str(dest))
for src in [BATCH_ROOT/f'{BATCH_ID}.state.json', BATCH_ROOT/f'{BATCH_ID}.control.json']:
    if src.exists():
        suffix='batch_state.json' if src.name.endswith('.state.json') else 'batch_control.json'
        dest=BRJ/f'{BATCH_ID}.{suffix}'
        shutil.copy2(src,dest)
        copied.append(str(dest))

result=json.loads((DONE_DIR/'result.json').read_text(encoding='utf-8'))
status=json.loads((DONE_DIR/'status.json').read_text(encoding='utf-8'))
status_snapshot=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_status_snapshot_{ts}.json'
status_snapshot.write_text(json.dumps(status,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
result_snapshot=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_result_snapshot_{ts}.json'
result_snapshot.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

raw_path=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_raw_export_{ts}.json'
cmd=['python3','<OPENCLAW_WORKSPACE>/tools_mat_parse.py','--force','--pretty',str(MAT_PATH)]
with raw_path.open('w',encoding='utf-8') as f:
    proc=subprocess.run(cmd,stdout=f,stderr=subprocess.PIPE,text=True,timeout=420)
if proc.returncode!=0:
    raise RuntimeError(f'raw export failed rc={proc.returncode}: {proc.stderr[-2000:]}')
raw=json.loads(raw_path.read_text(encoding='utf-8'))

sys.path.insert(0,'<OPENCLAW_WORKSPACE>')
import tools_mat_parse as tmp
try:
    drift_payload=tmp.analyze_savedexperiment_average_drift_mat_files([str(MAT_PATH)], force=True, timeout_seconds=420)[0]
except Exception as e:
    drift_payload={'ok':False,'source':'analyze_savedexperiment_average_drift.m','data_path':str(MAT_PATH),'error_code':type(e).__name__,'error_message':str(e)}
drift_path=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_drift_{ts}.json'
drift_path.write_text(json.dumps(drift_payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

scan=raw['scan']
edata=np.asarray(scan['ExperimentData'],dtype=float)[0]
eavg=np.asarray(scan['ExperimentDataEachAvg'],dtype=float)[0]
if edata.ndim!=2 or eavg.ndim!=3:
    raise RuntimeError(f'unexpected data shapes: ExperimentData {edata.shape}, ExperimentDataEachAvg {eavg.shape}')
ref=edata[0]
sig=edata[1]
ref_each=eavg[:,0,:]
sig_each=eavg[:,1,:]
if not (np.allclose(ref_each.mean(axis=0),ref) and np.allclose(sig_each.mean(axis=0),sig)):
    raise RuntimeError('ExperimentDataEachAvg axis contract mismatch: expected [scan, avg, readout, point].')
averages=int(eavg.shape[0])
points=int(scan.get('vary_points') or len(sig))
begin=float(scan['vary_begin']); step=float(scan['vary_step_size'])
freq=begin+np.arange(points)*step
freq_ghz=freq/1e9
freq_offset_mhz=(freq-3.876e9)/1e6
repetitions=int(scan.get('Repetitions') or scan.get('repetitions') or 0)
ratio=sig/ref
ratio_each=sig_each/ref_each
x=(freq-freq.mean())/1e6
ref_coef=np.polyfit(x,ref,1)
ref_line=np.polyval(ref_coef,x)
sig_over_refline=sig/ref_line
sig_over_refline_each=sig_each/ref_line[None,:]

def edge_median(arr,n=5):
    return float(np.median(np.r_[arr[:n],arr[-n:]]))

def min_metric(arr, label):
    idx=int(np.argmin(arr))
    edge=edge_median(arr)
    return {'label':label,'index':idx,'freq_hz':float(freq[idx]),'freq_ghz':float(freq_ghz[idx]),'offset_mhz_from_3p876GHz':float(freq_offset_mhz[idx]),'value':float(arr[idx]),'edge_median':edge,'fractional_drop_vs_edge':float((edge-arr[idx])/edge) if edge else None}

combined_metrics={
    'raw_signal':min_metric(sig,'raw_signal'),
    'pointwise_ratio':min_metric(ratio,'pointwise_ratio'),
    'reference_line_normalized_signal':min_metric(sig_over_refline,'reference_line_normalized_signal'),
}
per_average=[]
for i in range(averages):
    rr=ratio_each[i]
    sr=sig_over_refline_each[i]
    row={'average_index':i+1,
         'raw_signal':min_metric(sig_each[i],'raw_signal'),
         'pointwise_ratio':min_metric(rr,'pointwise_ratio'),
         'reference_line_normalized_signal':min_metric(sr,'reference_line_normalized_signal'),
         'mean_ref_kcps':float(ref_each[i].mean()),
         'mean_signal_kcps':float(sig_each[i].mean())}
    per_average.append(row)

final_counts=((result.get('summary') or {}).get('run_experiment') or {}).get('post_run',{}).get('final_counts_kcps')
post=((result.get('summary') or {}).get('run_experiment') or {}).get('post_run',{})
control=status.get('control') or {}
monitor=status.get('monitor') or {}
safety=result.get('safety') or {}
hard_anomaly=not (result.get('status')=='completed' and status.get('state')=='completed') or bool(control.get('stop_requested')) or bool(monitor.get('last_error')) or bool(safety.get('aborted'))
if final_counts is not None and float(final_counts)<20:
    hard_anomaly=True

combo_freqs=[combined_metrics[k]['freq_hz'] for k in ['raw_signal','pointwise_ratio','reference_line_normalized_signal']]
combo_span_hz=max(combo_freqs)-min(combo_freqs)
raw_center=combined_metrics['raw_signal']['freq_hz']
refline_center=combined_metrics['reference_line_normalized_signal']['freq_hz']
ratio_center=combined_metrics['pointwise_ratio']['freq_hz']
near_raw_count=sum(1 for r in per_average if abs(r['raw_signal']['freq_hz']-raw_center)<=500000.1)
refline_near_raw_count=sum(1 for r in per_average if abs(r['reference_line_normalized_signal']['freq_hz']-raw_center)<=500000.1)
# Use raw signal plus fitted-reference-line normalization as the primary signal-presence criterion.
# Point-wise ratio is provenance and can move by several grid points when reference fluctuations are structured.
clear_resonance=(not hard_anomaly and abs(refline_center-raw_center)<=100000.1 and abs(ratio_center-raw_center)<=300000.1 and combined_metrics['raw_signal']['fractional_drop_vs_edge']>=0.10 and near_raw_count==averages and refline_near_raw_count>=3)
selected_freq=raw_center if clear_resonance else None

B_G=None; larmor=None
if selected_freq:
    # Working ms=+1 model used throughout the project: f = D + gamma_e B, with D=2.87 GHz and gamma_e ~2.8 MHz/G.
    B_G=(selected_freq-2.87e9)/2.8e6
    larmor=B_G*1070.5

xml_basis='Rabimodulated.xml lines 48-50 acquire the true mS=0 reference; with full_expt=0 lines 55-65 skip the optional mS=1 reference; lines 71-78 apply the Rabi pulse and acquire readout2 as the signal.'
summary={
    'sequence':'Rabimodulated.xml',
    'readout_role_basis':xml_basis,
    'scan':{'begin_hz':float(freq[0]),'end_hz':float(freq[-1]),'points':points,'spacing_hz':float(step),'averages':averages,'repetitions':repetitions,'total_shots_per_point':averages*repetitions},
    'terminal_result':{'status':result.get('status'),'state':status.get('state'),'started_at':result.get('started_at'),'finished_at':result.get('finished_at'),'final_counts_kcps':final_counts,'safety':safety,'monitor_last_error':monitor.get('last_error',''),'stop_requested':bool(control.get('stop_requested'))},
    'drift_summary':{'ok':drift_payload.get('ok'),'num_averages':drift_payload.get('num_averages'),'scan_order_source':drift_payload.get('scan_order_source',''),'scan_order_mode':drift_payload.get('scan_order_mode',''),'scan_order_used_count':drift_payload.get('scan_order_used_count'),'flagged_average_indices':drift_payload.get('flagged_average_indices',[])},
}
interpretation={
    'hard_anomaly':hard_anomaly,
    'signal_presence':'supported clear weak-pi pODMR resonance' if clear_resonance else 'not supported as a clear weak-pi pODMR resonance',
    'selected_mw_freq_hz':selected_freq,
    'selected_mw_freq_ghz':selected_freq/1e9 if selected_freq else None,
    'basis':('Combined raw signal and fitted-reference-line normalization both minimize at %.7f GHz; point-wise ratio minimum is at %.7f GHz and is treated as denominator-sensitive provenance. Raw signal drop is %.1f%% vs edge median; %d/%d stored averages have raw minima within 0.5 MHz of the combined raw minimum. Select the raw/refline grid minimum as the refreshed center.' % (raw_center/1e9, ratio_center/1e9, 100*combined_metrics['raw_signal']['fractional_drop_vs_edge'], near_raw_count, averages)) if clear_resonance else 'Combined minima, contrast, or per-average support were insufficient for a refreshed center.',
    'caveats':['0.1 MHz grid spacing; do not claim sub-grid center precision.','Point-wise ratio is reviewed but not used alone as the signal-presence criterion.','This pODMR is a frequency calibration refresh only; it does not establish T2star or 13C.'],
    'derived_model_update':{'B_G_from_ms_plus_resonance_working_model':B_G,'gamma_e_hz_per_G_used':2.8e6,'gamma_13c_hz_per_G_used':1070.5,'expected_13C_larmor_Hz':larmor} if selected_freq else {},
    'next_implication':'Use refreshed mw_freq_hz for the next targeted Ramsey/T2star design if bridge/advisory gates pass. Treat the center as grid-supported with several-100-kHz uncertainty, not sub-grid precision.' if clear_resonance else 'Do not design a Ramsey from this refresh; either repeat/diagnose pODMR or reassess candidate calibration.'
}
review={
    'ok':True,
    'created_at':datetime.now(ZoneInfo('America/New_York')).isoformat(),
    'question':'Terminal raw/readout-aware review of fine weak-pi pODMR refresh on accepted r03 after det-shift Ramsey diagnostics.',
    'bridge_job_id':JOB_ID,
    'batch_id':BATCH_ID,
    'source_bridge_result':str(DONE_DIR/'result.json'),
    'project_bridge_artifacts_copied':copied,
    'data_path':str(MAT_PATH),
    'raw_export_path':str(raw_path),
    'drift_analysis_path':str(drift_path),
    'status_snapshot_path':str(status_snapshot),
    'result_snapshot_path':str(result_snapshot),
    'xml_path':str(XML_PATH),
    **summary,
    'freq_hz':[float(v) for v in freq],
    'freq_offset_mhz_from_3p876GHz':[float(v) for v in freq_offset_mhz],
    'readout1_ref_kcps':[float(v) for v in ref],
    'readout2_signal_kcps':[float(v) for v in sig],
    'signal_over_ref':[float(v) for v in ratio],
    'signal_over_refline':[float(v) for v in sig_over_refline],
    'combined_metrics':combined_metrics,
    'per_average_metrics':per_average,
    'interpretation':interpretation,
}
review_path=AN/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_{ts}.json'
review_path.write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

fig_path=FIGS/f'image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_{ts}.png'
fig,axes=plt.subplots(4,1,figsize=(11,12),sharex=True)
axes[0].plot(freq_ghz,ref,'o-',label='readout1 reference')
axes[0].plot(freq_ghz,sig,'o-',label='readout2 pODMR signal')
axes[0].axvline(raw_center/1e9,color='k',ls='--',alpha=0.5,label='selected raw min' if selected_freq else 'raw min')
axes[0].set_ylabel('raw kcps'); axes[0].legend(fontsize=8); axes[0].grid(alpha=0.25)
axes[1].plot(freq_ghz,ratio,'o-',label='signal/ref point-wise')
axes[1].plot(freq_ghz,sig_over_refline,'o-',label='signal / fitted reference line')
axes[1].axvline(raw_center/1e9,color='k',ls='--',alpha=0.5)
axes[1].set_ylabel('normalized'); axes[1].legend(fontsize=8); axes[1].grid(alpha=0.25)
for i in range(averages):
    axes[2].plot(freq_ghz,sig_each[i],marker='o',ms=3,label=f'avg {i+1} signal')
axes[2].axvline(raw_center/1e9,color='k',ls='--',alpha=0.5)
axes[2].set_ylabel('per-avg signal kcps'); axes[2].legend(ncol=2,fontsize=8); axes[2].grid(alpha=0.25)
axes[3].plot(freq_ghz,ref_each.mean(axis=0),'o-',label='mean reference')
axes[3].plot(freq_ghz,ref_line,'--',label='reference linear fit')
axes[3].plot(freq_ghz,sig,'o-',label='mean signal')
axes[3].axvline(raw_center/1e9,color='k',ls='--',alpha=0.5)
axes[3].set_ylabel('kcps'); axes[3].set_xlabel('mw_freq (GHz)'); axes[3].legend(fontsize=8); axes[3].grid(alpha=0.25)
title='r03 fine weak-pi pODMR refresh terminal review: '
if clear_resonance:
    title += f'center {selected_freq/1e9:.7f} GHz, drop {100*combined_metrics["raw_signal"]["fractional_drop_vs_edge"]:.1f}%'
else:
    title += 'no clear refreshed resonance'
fig.suptitle(title)
fig.tight_layout(rect=[0,0,1,0.97])
fig.savefig(fig_path,dpi=180)

print(json.dumps({'ok':True,'review_path':str(review_path),'figure_path':str(fig_path),'raw_path':str(raw_path),'drift_path':str(drift_path),'selected_mw_freq_hz':selected_freq,'clear_resonance':clear_resonance,'final_counts_kcps':final_counts,'drift_flagged_average_indices':drift_payload.get('flagged_average_indices',[])},indent=2))
