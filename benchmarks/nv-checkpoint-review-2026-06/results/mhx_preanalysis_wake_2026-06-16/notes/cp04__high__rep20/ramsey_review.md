# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `context.json`.
- New terminal det-shift Ramsey data:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: bridge job contract for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result, status, control.
- Prior comparison/model evidence:
  - `evidence/e008.json`: prior det=1.0 MHz short-tau terminal review.
  - `evidence/e019.json`, `evidence/e021.json`: det-shift model and success criteria.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_review.png`
- Main checks:
  - Verified raw array contract: `ExperimentDataEachAvg` averages reproduce combined reference and signal traces.
  - Used prior protocol inspection convention: readout 1 reference, readout 2 Ramsey signal.
  - Computed raw signal, reference, point-wise ratio, and signal normalized by fitted reference line.
  - Computed per-point SEM across 12 stored averages.
  - Ran least-squares sinusoid screens from 0.25 to 2.25 MHz and FFT checks after linear-baseline subtraction.
  - Checked target frequencies: programmed 1.5 MHz, det-tracking 1.692 MHz, 13C sidebands 1.307/2.077 MHz, prior fixed 1.192 MHz control, and first-scout 0.884 MHz control.
  - Ran simple robust average-mean checks for reference, signal, and ratio.
  - Ran descriptive damped-sinusoid grid fits only as diagnostics.

## Key quantitative results

- Run completed normally: status `completed`, final counts `44.796 kcps`, safe shutdown true, stop requested false, monitor last error empty.
- Scan: `tau = 0.048..1.968 us`, 41 points, 12 averages x 90000 reps = `1.08e6` shots/tau, snake order.
- Frequency resolution is coarse for fine assignment: FFT bin spacing `0.508 MHz`, nominal `1/span = 0.521 MHz`, Nyquist `10.417 MHz`.
- Noise/effect scale:
  - Median signal SEM: `0.711 kcps`.
  - Median ratio SEM: `0.0126`.
  - Signal linear-residual peak-to-peak: `6.29 kcps`.
  - Ratio linear-residual peak-to-peak: `0.133`.
  - Early tau <= 0.75 us signal peak-to-peak: `6.46 kcps`, ratio peak-to-peak `0.134`.
- Local robust average-mean checks flagged no averages, though average levels vary.
- Least-squares screens:
  - Point-wise ratio top: `1.623 MHz`, ratio amplitude `0.0255`, R2 improvement `0.430`.
  - Raw signal top: `0.882 MHz`, signal amplitude `1.533 kcps`, R2 improvement `0.577`.
  - Signal/reference-line top: `0.882 MHz`, amplitude `0.0319`, R2 improvement `0.576`.
  - Reference readout also has structure near `0.924 MHz`, amplitude `0.405 kcps`.
- Target amplitudes:
  - Programmed 1.5 MHz: ratio amplitude `0.0240`, raw signal amplitude `1.128 kcps`.
  - Det-tracking 1.692 MHz: ratio amplitude `0.0250`, raw signal amplitude `1.225 kcps`.
  - Prior fixed 1.192 MHz control: ratio amplitude `0.0051`, raw signal amplitude `0.474 kcps`.
  - First-scout 0.884 MHz control: ratio amplitude `0.0264`, raw signal amplitude `1.532 kcps`.
  - Det-tracking 13C sidebands are weak: low `1.307 MHz` ratio amplitude `0.0095` / raw `0.268 kcps`; high `2.077 MHz` ratio amplitude `0.0061` / raw `0.251 kcps`.
- Descriptive damped fits are view-dependent and not promoted:
  - Ratio view: `0.686 MHz`, `T2star ~0.49 us`.
  - Raw signal and signal/reference-line views: `0.818 MHz`, `T2star ~0.71 us`.

## Plausible interpretation

The det-shift run is analyzable and argues against simply promoting the prior fixed `~1.192 MHz` ratio component: that component is weak in the new data. However, it does not produce a clean det-following Ramsey carrier. The point-wise ratio screen shifts toward the det-shift band, but raw signal and fitted-reference normalization instead favor `~0.882 MHz`, close to the first-scout exploratory component and not to the programmed `1.5 MHz` or predicted `1.692 MHz` det-tracking carrier.

Because the raw/readout-aware views disagree, the most conservative interpretation is that the r03 Ramsey data under current `auto__ramsey` conditions contain structured short-tau oscillatory/transient content, but not a supported physical carrier/13C-sideband model. The aligned r03 ODMR conclusion remains supported by prior context; this Ramsey branch remains non-claim-grade for T2star and nearby 13C.

## Claims not yet supported

- No numeric T2star claim is supported from this run.
- No nearby 13C coupling claim is supported.
- The `1.623 MHz` ratio component is not supported as a physical Ramsey carrier because the raw signal and fitted-reference views do not agree.
- The `0.882 MHz` raw/signal-over-refline component is not supported as a physical carrier because it does not track the programmed detuning.
- The descriptive damped-fit T2star values are not supported physical parameters; they are view-dependent diagnostics.

## Recommended next action

Do not run another blind Ramsey repeat on r03 under the same `auto__ramsey` conditions. The next useful step is a branch decision: either switch to an alternate coherence protocol/check that can separate Ramsey physics from readout/protocol transients, or close the r03 Ramsey/T2star/13C branch as unsupported under the tested conditions while preserving the aligned-NV result.
