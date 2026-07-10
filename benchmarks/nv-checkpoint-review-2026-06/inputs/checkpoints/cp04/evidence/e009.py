#!/usr/bin/env python3
"""Terminal raw/readout-aware review for r03 short-tau Ramsey diagnostic."""
from __future__ import annotations

import json, math, shutil
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
AN = PROJECT/'work/artifacts/analysis'
FIGS = PROJECT/'work/artifacts/figures'
BRIDGE_COPY = PROJECT/'work/bridge_jobs'
AN.mkdir(parents=True, exist_ok=True)
FIGS.mkdir(parents=True, exist_ok=True)
BRIDGE_COPY.mkdir(parents=True, exist_ok=True)

JOB_ID = 'nv23_ramsey_20260513_230331_auto_ramsey'
BATCH_ID = 'nv23_ramsey_20260513_230232'
DONE = Path('<NV_BRIDGE_ROOT>/done')/JOB_ID
MAT_PATH = '<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat'
RAW_PATH = AN/'image145844_reimage_r03_ramsey_shorttau_terminal_raw_export_20260514_0127.json'
DRIFT_PATH = AN/'image145844_reimage_r03_ramsey_shorttau_terminal_drift_20260514_0127.json'
MODEL_PATH = AN/'image145844_reimage_r03_ramsey_shorttau_model_plan_20260513_2257.json'
PREV_8US_REVIEW = AN/'image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.json'
FIRST_SCOUT_REVIEW = AN/'image145844_reimage_r03_ramsey_t2star_raw_fft_review_20260513_1930.json'
REVIEW_PATH = AN/'image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.json'
FIG_PATH = FIGS/'image145844_reimage_r03_ramsey_shorttau_terminal_review_20260514_0127.png'

TARGETS = {
    'programmed_carrier_det_1p0MHz': 1.0e6,
    'low_13C_sideband_det_minus_larmor': 615_422.875,
    'high_13C_sideband_det_plus_larmor': 1_384_577.125,
    'first_scout_top_component': 884_361.482,
    'prior_det1p0_8us_top_component': 1_178_000.0,
}

# Copy terminal bridge and batch artifacts into the project audit tree.
copied = []
for name in ['job.json', 'status.json', 'result.json', 'control.json', 'bridge.log', 'matlab_command_window.log']:
    src = DONE/name
    if src.exists():
        dst = BRIDGE_COPY/f'{JOB_ID}.{name}'
        shutil.copy2(src, dst)
        copied.append({'source': str(src), 'project_copy': str(dst)})
for src, dst in [
    (Path('<OPENCLAW_WORKSPACE>/.openclaw/single_submit/batches')/(BATCH_ID+'.state.json'), BRIDGE_COPY/(BATCH_ID+'.batch_state.json')),
    (Path('<OPENCLAW_WORKSPACE>/.openclaw/single_submit/batch_specs')/(BATCH_ID+'.json'), BRIDGE_COPY/(BATCH_ID+'.batch_spec.json')),
]:
    if src.exists():
        shutil.copy2(src, dst)
        copied.append({'source': str(src), 'project_copy': str(dst)})

raw = json.loads(RAW_PATH.read_text())
drift = json.loads(DRIFT_PATH.read_text())
result = json.loads((DONE/'result.json').read_text()) if (DONE/'result.json').exists() else {}
status = json.loads((DONE/'status.json').read_text()) if (DONE/'status.json').exists() else {}
model_plan = json.loads(MODEL_PATH.read_text()) if MODEL_PATH.exists() else {}

scan = raw['scan']
edata = np.asarray(scan['ExperimentData'], dtype=float)[0]
ref = edata[0]
sig = edata[1]
eavg = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]
# Verified raw-export contract for this MAT: [scan, avg, readout, point].
ref_each = eavg[:, 0, :]
sig_each = eavg[:, 1, :]
if not (np.allclose(np.mean(ref_each, axis=0), ref) and np.allclose(np.mean(sig_each, axis=0), sig)):
    raise RuntimeError('ExperimentDataEachAvg axis contract mismatch: expected [scan, avg, readout, point].')

points = int(scan['vary_points'])
tau = float(scan['vary_begin']) + np.arange(points) * float(scan['vary_step_size'])
tau_us = tau * 1e6
dt = float(np.median(np.diff(tau)))
repetitions = int(scan.get('Repetitions') or 0)
averages = int(eavg.shape[0])
ratio = sig / ref
ratio_each = sig_each / ref_each

def flagged_list(value):
    if value is None or value == '':
        return []
    if isinstance(value, list):
        return value
    return [value]

def linear_fit(x, y):
    coef = np.polyfit(x, y, 1)
    fit = np.polyval(coef, x)
    return fit, y - fit, coef

def ls_amp(t, y, f):
    base = np.column_stack([np.ones_like(t), t])
    b0, *_ = np.linalg.lstsq(base, y, rcond=None)
    pred0 = base @ b0
    rss0 = float(np.sum((y - pred0)**2))
    w = 2*np.pi*f*t
    design = np.column_stack([np.ones_like(t), t, np.cos(w), np.sin(w)])
    b1, *_ = np.linalg.lstsq(design, y, rcond=None)
    pred1 = design @ b1
    rss1 = float(np.sum((y - pred1)**2))
    amp = float(math.hypot(b1[2], b1[3]))
    imp = 0.0 if rss0 <= 0 else max(0.0, (rss0-rss1)/rss0)
    return {'freq_hz': float(f), 'freq_mhz': float(f/1e6), 'amplitude': amp, 'baseline_residual_r2_improvement': imp, 'rss0': rss0, 'rss1': rss1}

def frequency_screen(t, y, lo=0.25e6, hi=2.25e6, step=1e3, limit=12):
    rows = [ls_amp(t, y, float(f)) for f in np.arange(lo, hi + step/2, step)]
    rows.sort(key=lambda r: (r['baseline_residual_r2_improvement'], r['amplitude']), reverse=True)
    return rows[:limit]

def fft_spectrum(t, y):
    fit, resid, _ = linear_fit(t, y)
    freq = np.fft.rfftfreq(len(t), float(np.median(np.diff(t))))
    amp = 2*np.abs(np.fft.rfft(resid))/len(t)
    return freq, amp

def nearest_fft(freq, amp, f):
    idx = int(np.argmin(np.abs(freq-f)))
    return {'nearest_fft_bin_hz': float(freq[idx]), 'nearest_fft_bin_mhz': float(freq[idx]/1e6), 'fft_amplitude': float(amp[idx])}

def damped_grid_fit(t, y, f_lo=0.25e6, f_hi=2.25e6, f_step=2e3):
    """Grid search over frequency/T2; solve linear baseline+quadratures at each grid point."""
    t_us = t * 1e6
    t0 = t_us - float(np.mean(t_us))
    base = np.column_stack([np.ones_like(t0), t0])
    b0, *_ = np.linalg.lstsq(base, y, rcond=None)
    rss_baseline = float(np.sum((y - base @ b0)**2))
    best = None
    # Include long-T boundary; if selected, decay is not resolved by this window.
    T_grid_us = np.unique(np.concatenate([np.geomspace(0.05, 20.0, 100), np.array([50.0])]))
    f_grid = np.arange(f_lo, f_hi + f_step/2, f_step)
    for T_us in T_grid_us:
        env = np.exp(-t_us / T_us)
        for f in f_grid:
            w = 2*np.pi*f*t
            X = np.column_stack([np.ones_like(t0), t0, env*np.cos(w), env*np.sin(w)])
            coef, *_ = np.linalg.lstsq(X, y, rcond=None)
            pred = X @ coef
            rss = float(np.sum((y - pred)**2))
            amp0 = float(math.hypot(coef[2], coef[3]))
            entry = {
                'freq_hz': float(f), 'freq_mhz': float(f/1e6), 'T2star_us': float(T_us),
                'amplitude_at_tau0': amp0, 'rss': rss,
                'baseline_rss': rss_baseline,
                'r2_improvement_vs_linear_baseline': 0.0 if rss_baseline <= 0 else max(0.0, (rss_baseline-rss)/rss_baseline),
            }
            if best is None or (rss, -amp0) < (best['rss'], -best['amplitude_at_tau0']):
                best = entry
    n = len(y)
    best['bic_linear_baseline'] = float(n*np.log(rss_baseline/n) + 2*np.log(n)) if rss_baseline > 0 else None
    best['bic_damped_model'] = float(n*np.log(best['rss']/n) + 6*np.log(n)) if best['rss'] > 0 else None
    best['delta_bic_damped_minus_linear'] = None if best['bic_linear_baseline'] is None else float(best['bic_damped_model'] - best['bic_linear_baseline'])
    best['T2star_boundary_note'] = 'upper_boundary_or_long_window_unresolved' if best['T2star_us'] >= 20.0 else ('lower_boundary_very_short_or_artifact_sensitive' if best['T2star_us'] <= 0.051 else 'interior_grid_value')
    return best

ref_line, ref_resid, ref_coef = linear_fit(tau, ref)
sig_line, sig_resid, sig_coef = linear_fit(tau, sig)
ratio_line, ratio_resid, ratio_coef = linear_fit(tau, ratio)
sig_over_refline = sig / ref_line
sig_over_refline_line, sig_over_refline_resid, sig_over_refline_coef = linear_fit(tau, sig_over_refline)

sig_sem = np.std(sig_each, axis=0, ddof=1)/math.sqrt(averages)
ratio_sem = np.std(ratio_each, axis=0, ddof=1)/math.sqrt(averages)

masks = {
    'all_tau': np.ones_like(tau, dtype=bool),
    'skip_first_point': np.arange(len(tau)) > 0,
    'skip_tau_le_0p2us': tau > 0.2e-6,
    'early_0p75us': tau <= 0.75e-6,
}

screens = {
    'ratio_all_tau': frequency_screen(tau[masks['all_tau']], ratio[masks['all_tau']]),
    'ratio_skip_first_point': frequency_screen(tau[masks['skip_first_point']], ratio[masks['skip_first_point']]),
    'ratio_skip_tau_le_0p2us': frequency_screen(tau[masks['skip_tau_le_0p2us']], ratio[masks['skip_tau_le_0p2us']]),
    'signal_all_tau_kcps': frequency_screen(tau, sig),
    'signal_over_refline_all_tau': frequency_screen(tau, sig_over_refline),
}
fft_freq, fft_amp = fft_spectrum(tau, ratio)
fft_freq_sig, fft_amp_sig = fft_spectrum(tau, sig)

def target_entry(name, f):
    r = ls_amp(tau, ratio, f)
    s = ls_amp(tau, sig, f)
    n = ls_amp(tau, sig_over_refline, f)
    skip = ls_amp(tau[masks['skip_tau_le_0p2us']], ratio[masks['skip_tau_le_0p2us']], f)
    out = {
        'target_hz': float(f), 'target_mhz': float(f/1e6),
        'least_squares_amplitude_ratio': r['amplitude'],
        'baseline_residual_r2_improvement_ratio': r['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_kcps': s['amplitude'],
        'baseline_residual_r2_improvement_signal': s['baseline_residual_r2_improvement'],
        'least_squares_amplitude_signal_over_refline': n['amplitude'],
        'baseline_residual_r2_improvement_signal_over_refline': n['baseline_residual_r2_improvement'],
        'skip_tau_le_0p2us_amplitude_ratio': skip['amplitude'],
        'skip_tau_le_0p2us_r2_improvement_ratio': skip['baseline_residual_r2_improvement'],
    }
    out.update({('ratio_'+k): v for k, v in nearest_fft(fft_freq, fft_amp, f).items()})
    out.update({('signal_'+k): v for k, v in nearest_fft(fft_freq_sig, fft_amp_sig, f).items()})
    return out

frequency_targets = {name: target_entry(name, f) for name, f in TARGETS.items()}
top_ratio = screens['ratio_all_tau'][0]
frequency_targets['combined_top_ratio_screen_component'] = target_entry('combined_top_ratio_screen_component', top_ratio['freq_hz'])

per_average = []
for i in range(averages):
    rr = ratio_each[i]
    ss = sig_each[i]
    top = frequency_screen(tau, rr, limit=1)[0]
    row = {
        'average_index': i+1,
        'mean_signal_kcps': float(np.mean(ss)),
        'mean_reference_kcps': float(np.mean(ref_each[i])),
        'mean_ratio': float(np.mean(rr)),
        'top_frequency_mhz': float(top['freq_mhz']),
        'top_amplitude_ratio': float(top['amplitude']),
        'top_r2_improvement': float(top['baseline_residual_r2_improvement']),
    }
    for key, f in TARGETS.items():
        val = ls_amp(tau, rr, f)
        row['amplitude_at_'+key+'_ratio'] = float(val['amplitude'])
        row['r2_improvement_at_'+key] = float(val['baseline_residual_r2_improvement'])
    per_average.append(row)

fit_ratio = damped_grid_fit(tau, ratio)
fit_signal = damped_grid_fit(tau, sig)

runtime = result.get('summary', {}).get('run_experiment', {}) if isinstance(result, dict) else {}
post = runtime.get('post_run', {}) if isinstance(runtime, dict) else {}
monitor = status.get('monitor', {}) if isinstance(status, dict) else {}
control = status.get('control', {}) if isinstance(status, dict) else {}
final_counts = post.get('final_counts_kcps') or runtime.get('incomplete_detail', {}).get('final_counts_kcps')
final_counts_text = post.get('text_final_counts') or (f'{final_counts} kcps' if final_counts is not None else '')
monitor_last_error = monitor.get('last_error') or ''
stop_requested = bool(control.get('stop_requested'))
drift_flags = flagged_list(drift.get('flagged_average_indices'))

expected = model_plan.get('quantitative_expectation', {}) if isinstance(model_plan, dict) else {}
expected_raw_sem = expected.get('expected_median_raw_signal_sem_kcps')
expected_ratio_sem = expected.get('expected_median_ratio_sem')

summary_stats = {
    'readout_roles': 'ramsey.xml full_experiment=0: readout1 reference, readout2 Ramsey signal; inspected live XML/function and terminal job metadata.',
    'tau_start_us': float(tau_us[0]),
    'tau_stop_us': float(tau_us[-1]),
    'tau_step_us': float(dt*1e6),
    'points': points,
    'averages': averages,
    'repetitions': repetitions,
    'total_shots_per_point': int(averages*repetitions),
    'fft_bin_spacing_hz': float(fft_freq[1]-fft_freq[0]) if len(fft_freq)>1 else None,
    'nominal_resolution_1_over_span_hz': float(1/(tau[-1]-tau[0])) if tau[-1] != tau[0] else None,
    'nyquist_hz': float(0.5/dt),
    'raw_reference_mean_kcps': float(np.mean(ref)),
    'raw_reference_std_over_tau_kcps': float(np.std(ref, ddof=1)),
    'raw_signal_mean_kcps': float(np.mean(sig)),
    'raw_signal_std_over_tau_kcps': float(np.std(sig, ddof=1)),
    'ratio_mean': float(np.mean(ratio)),
    'ratio_std_over_tau': float(np.std(ratio, ddof=1)),
    'signal_point_sem_kcps': {'median': float(np.median(sig_sem)), 'min': float(np.min(sig_sem)), 'max': float(np.max(sig_sem))},
    'ratio_point_sem': {'median': float(np.median(ratio_sem)), 'min': float(np.min(ratio_sem)), 'max': float(np.max(ratio_sem))},
    'planned_expected_median_raw_signal_sem_kcps': expected_raw_sem,
    'planned_expected_median_ratio_sem': expected_ratio_sem,
    'signal_linear_residual_peak_to_peak_kcps': float(np.ptp(sig_resid)),
    'ratio_linear_residual_peak_to_peak': float(np.ptp(ratio_resid)),
    'signal_over_refline_linear_residual_peak_to_peak': float(np.ptp(sig_over_refline_resid)),
    'early_0p75us_signal_peak_to_peak_kcps': float(np.ptp(sig[masks['early_0p75us']])),
    'early_0p75us_ratio_peak_to_peak': float(np.ptp(ratio[masks['early_0p75us']])),
    'average_signal_means_kcps': [float(x) for x in np.mean(sig_each, axis=1)],
    'average_reference_means_kcps': [float(x) for x in np.mean(ref_each, axis=1)],
    'average_ratio_means': [float(x) for x in np.mean(ratio_each, axis=1)],
    'drift_flagged_average_indices': drift_flags,
    'drift_scan_order_source': drift.get('scan_order_source',''),
    'drift_scan_order_mode': drift.get('scan_order_mode',''),
    'drift_scan_order_used_count': drift.get('scan_order_used_count',''),
    'status_state': status.get('state',''),
    'status_phase': status.get('phase',''),
    'finished_at': result.get('finished_at',''),
    'elapsed_seconds': status.get('elapsed_seconds'),
    'final_counts_kcps': final_counts,
    'final_counts_text': final_counts_text,
    'monitor_last_error': monitor_last_error,
    'stop_requested': stop_requested,
}

carrier = frequency_targets['programmed_carrier_det_1p0MHz']
low = frequency_targets['low_13C_sideband_det_minus_larmor']
high = frequency_targets['high_13C_sideband_det_plus_larmor']
top = frequency_targets['combined_top_ratio_screen_component']

# Evidence-based decision: the data are analyzable and have a stable empirical component, but the programmed carrier and 13C-sideband model is not supported.
hard_anomaly = bool(monitor_last_error or stop_requested or (status.get('state') not in ('completed','done')) or result.get('status') not in ('completed','done'))
claim_grade = False
interpretation = {
    'hard_anomaly': hard_anomaly,
    'signal_presence': 'empirical_short_tau_transient_present_but_not_claim_grade_ramsey_model',
    't2star_claim': 'not_supported',
    'nearby_13c_claim': 'not_supported',
    'fit_decision': 'Do not promote a T2star fit. The strongest empirical component is not the programmed det carrier or the expected 13C sidebands, and the damped-sinusoid grid fit leaves T2star model-dependent / boundary-sensitive over the short window.',
    'supported_points': [
        f"Run completed safely with {averages} averages x {repetitions} repetitions ({averages*repetitions} shots/tau), final counts {final_counts_text}, monitor_last_error={monitor_last_error!r}, stop_requested={stop_requested}.",
        f"Scan-order-aware drift used {drift.get('scan_order_source','unknown')} / {drift.get('scan_order_mode','unknown')} and flagged averages {drift_flags}.",
        f"The high-SNR terminal data still contain a large early-time transient: first 0.75 us signal peak-to-peak {summary_stats['early_0p75us_signal_peak_to_peak_kcps']:.2f} kcps and ratio peak-to-peak {summary_stats['early_0p75us_ratio_peak_to_peak']:.3f}, with median SEM {summary_stats['signal_point_sem_kcps']['median']:.2f} kcps / {summary_stats['ratio_point_sem']['median']:.3f} ratio.",
        f"The programmed 1.0 MHz carrier remains weaker than the empirical top: carrier ratio LS amplitude {carrier['least_squares_amplitude_ratio']:.5f} / raw {carrier['least_squares_amplitude_signal_kcps']:.3f} kcps, while the combined ratio screen top is near {top['target_mhz']:.3f} MHz with ratio amplitude {top['least_squares_amplitude_ratio']:.5f}.",
        f"Expected 13C sidebands are not dominant: low sideband ratio amplitude {low['least_squares_amplitude_ratio']:.5f}, high sideband ratio amplitude {high['least_squares_amplitude_ratio']:.5f}; neither provides a well-supported 13C conclusion.",
        f"The best descriptive damped-sinusoid grid fit in the ratio view prefers f={fit_ratio['freq_mhz']:.3f} MHz and T2*={fit_ratio['T2star_us']:.3g} us ({fit_ratio['T2star_boundary_note']}), so it is not a robust physical T2star extraction.",
    ],
    'decision': 'Accept the measurement as terminal, analyzable evidence but do not claim numeric T2star or nearby-13C coupling from r03 Ramsey data. The aligned-NV conclusion remains supported; the Ramsey/T2star branch now needs bridge-free synthesis and a targeted det-shift/alternate-protocol decision rather than another identical Ramsey repeat.',
    'recommended_next': 'Do a bridge-free branch synthesis comparing the three Ramsey datasets and then either design a targeted det-shift Ramsey diagnostic to test whether the ~1.18 MHz component tracks programmed det, or close r03 Ramsey/13C as unsupported under current conditions. Do not enqueue another blind same-det repeat.',
}

fft_visual = [{'freq_mhz': float(f/1e6), 'ratio_amp': float(a)} for f,a in zip(fft_freq[(fft_freq>=0.2e6)&(fft_freq<=2.5e6)], fft_amp[(fft_freq>=0.2e6)&(fft_freq<=2.5e6)])]

review = {
    'ok': True,
    'created_at': datetime.now(timezone.utc).astimezone().isoformat(),
    'question': 'Terminal review of the short-tau/high-SNR r03 Ramsey diagnostic after prior non-claim-grade Ramsey data.',
    'bridge_job_id': JOB_ID,
    'batch_id': BATCH_ID,
    'data_path': MAT_PATH,
    'raw_export_path': str(RAW_PATH),
    'drift_analysis_path': str(DRIFT_PATH),
    'figure_path': str(FIG_PATH),
    'project_copied_bridge_artifacts': copied,
    'inputs': {
        'terminal_done_dir': str(DONE),
        'model_plan': str(MODEL_PATH),
        'previous_det1p0_8us_terminal_review': str(PREV_8US_REVIEW),
        'first_scout_review': str(FIRST_SCOUT_REVIEW),
        'ramsey_xml': '<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/ramsey.xml',
        'ramsey_function': '<MATLAB_23C_ROOT>/PulseSequencer/Sequence-commands/AWG/ramsey.m',
    },
    'protocol_basis': {
        'sequence_manifest_id': 'auto__ramsey',
        'sequence_file': 'SavedSequences/SavedSequences-AWG/ramsey.xml',
        'readout_roles': summary_stats['readout_roles'],
        'det_phase_path': 'PulseSequencer/Sequence-commands/AWG/ramsey.m applies second pi/2 phase det*tau*360 degrees.',
        'axis_contract_check': 'ExperimentDataEachAvg axis verified by averaging per-average readout axis back to ExperimentData.',
        'scan_order_source': summary_stats['drift_scan_order_source'],
        'scan_order_mode': summary_stats['drift_scan_order_mode'],
    },
    'summary_stats': summary_stats,
    'frequency_targets': frequency_targets,
    'least_squares_top_components': screens,
    'fft_visual_components_ratio': fft_visual,
    'per_average_frequency_screen': per_average,
    'descriptive_damped_sinusoid_grid_fit': {
        'ratio_view': fit_ratio,
        'raw_signal_view': fit_signal,
        'caveat': 'Descriptive only. Frequency/T2 are grid-fit diagnostics after signal-review, not promoted physical parameters.',
    },
    'interpretation': interpretation,
}
REVIEW_PATH.write_text(json.dumps(review, indent=2) + '\n', encoding='utf-8')

# Figure.
FIGS.mkdir(parents=True, exist_ok=True)
fig, axes = plt.subplots(5, 1, figsize=(12, 15), constrained_layout=True)
axes[0].plot(tau_us, ref, 'o-', label='readout1 reference')
axes[0].plot(tau_us, sig, 'o-', label='readout2 Ramsey signal')
axes[0].plot(tau_us, sig_line, '--', alpha=0.7, label='signal linear baseline')
axes[0].set_title('r03 short-tau Ramsey terminal review (12/12 averages)')
axes[0].set_ylabel('raw kcps')
axes[0].legend(fontsize=8)
axes[0].grid(alpha=0.25)

axes[1].plot(tau_us, ratio, 'o-', label='signal/ref point-wise')
axes[1].plot(tau_us, sig_over_refline, 'o-', label='signal / fitted ref line')
axes[1].plot(tau_us, ratio_line, '--', alpha=0.7, label='ratio linear baseline')
axes[1].set_ylabel('normalized')
axes[1].legend(fontsize=8)
axes[1].grid(alpha=0.25)

mask = (fft_freq >= 0.2e6) & (fft_freq <= 2.5e6)
axes[2].plot(fft_freq[mask]/1e6, fft_amp[mask], 'o-', label='FFT amplitude of detrended ratio')
for name, f in TARGETS.items():
    axes[2].axvline(f/1e6, linestyle='--', alpha=0.45, label=name.replace('_',' '))
axes[2].set_ylabel('ratio amp')
axes[2].set_xlim(0.2, 2.5)
axes[2].legend(fontsize=7, ncol=2)
axes[2].grid(alpha=0.25)

freqs = np.arange(0.25e6, 2.25e6+25e3, 25e3)
amp_all = [ls_amp(tau, ratio, f)['amplitude'] for f in freqs]
amp_skip = [ls_amp(tau[masks['skip_tau_le_0p2us']], ratio[masks['skip_tau_le_0p2us']], f)['amplitude'] for f in freqs]
axes[3].plot(freqs/1e6, amp_all, 'o-', ms=3, label='ratio LS all tau')
axes[3].plot(freqs/1e6, amp_skip, 's-', ms=3, label='ratio LS skip tau<=0.2us')
for name, f in TARGETS.items():
    axes[3].axvline(f/1e6, linestyle='--', alpha=0.35)
axes[3].set_xlabel('frequency (MHz)')
axes[3].set_ylabel('LS ratio amp')
axes[3].legend(fontsize=8)
axes[3].grid(alpha=0.25)

for i in range(averages):
    axes[4].plot(tau_us, sig_each[i], marker='o', ms=2.5, linewidth=0.9, label=f'avg {i+1}')
axes[4].set_xlabel('tau (us)')
axes[4].set_ylabel('per-avg signal kcps')
axes[4].legend(fontsize=7, ncol=4)
axes[4].grid(alpha=0.25)

fig.savefig(FIG_PATH, dpi=150)
print(json.dumps({'ok': True, 'review_path': str(REVIEW_PATH), 'figure_path': str(FIG_PATH), 'n_avg': averages, 'final_counts': final_counts, 'drift_flags': drift_flags, 'top_ratio_mhz': top['target_mhz'], 'carrier_amp_ratio': carrier['least_squares_amplitude_ratio'], 'fit_ratio': fit_ratio}, indent=2))
