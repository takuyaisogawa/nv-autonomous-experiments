# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/advice.md`, `project/state.md`: objective and current project status.
- `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`: fine-pODMR review, second-Ramsey model/advisory, and run-start note.
- `measurement/m001.json`: completed raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: bridge job metadata for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.

## Calculations/Scripts Run

- Created and ran `analyze_ramsey.py`.
- Saved diagnostic figure `ramsey_diagnostic.png` (headless Matplotlib; local image viewer could not read it because of an access error, but the PNG exists).
- Confirmed raw shape: 8 averages, 2 readouts, 41 tau points from 0 to 8 us in 0.2 us steps; 50000 reps/average.
- Used project/advisory readout assignment: readout1 is mS=0/reference, readout2 is Ramsey signal for `full_experiment=0`.
- Checked raw signal, signal/reference ratio, per-average means, scan-order first-half/second-half common-mode shifts, FFT, least-squares sinusoid amplitudes at expected frequencies, and damped-cosine fits.

Key numerical checks:

- Terminal run completed safely; final counts were 44.184 kcps.
- Per-average mean counts varied substantially across averages: reference span 30.5% vs median, signal span 31.6% vs median. Signal/reference ratio span was smaller, 3.9% vs median.
- Within-average scan-order common-mode first-half/second-half changes were modest: -1.2% to +5.6%; no average crossed the simple 15% drift flag used here.
- Combined signal/reference ratio had mean 0.90421 and peak-to-peak variation 0.16962, about 18.8% of the mean.
- Detrended/windowed FFT ratio peaks in 0.25 to 2.2 MHz: strongest at 1.0976 MHz, then 1.2195 MHz, then 0.9756 MHz.
- Least-squares amplitudes on combined ratio with constant+linear background:
  - Expected low 13C sideband 0.615 MHz: amp 0.01109, complex mean/SEM 1.47.
  - Prior scout component 0.884 MHz: amp 0.00742, complex mean/SEM 1.43.
  - Programmed carrier 1.000 MHz: amp 0.00916, complex mean/SEM 1.93.
  - Expected high 13C sideband 1.385 MHz: amp 0.00843, complex mean/SEM 1.51.
- Frequency scan of the combined ratio preferred about 1.175 to 1.19 MHz. A free-frequency damped Ramsey fit gave f = 1.187 MHz, T2* = 2.27 us, R2 = 0.486. A fixed 1.000 MHz damped fit forced T2* to 0.35 us with R2 = 0.405.
- Per-average dominant LS frequencies were inconsistent: 0.265, 1.635, 0.455, 0.415, 1.165, 0.635, 2.040, and 1.420 MHz.

## Plausible Interpretation

The second Ramsey data are analyzable and show an oscillatory component in the combined normalized trace. The strongest combined evidence is near 1.1 to 1.2 MHz, plausibly around 1.18 MHz, not exactly at the programmed 1.0 MHz carrier and not at the expected 13C sidebands near 0.615 or 1.385 MHz.

The prior non-claim-grade 0.884 MHz component from the 1.5 MHz scout is not dominant here, which weakens a simple fixed-artifact interpretation. However, the new dominant component also does not follow the programmed detuning cleanly, and stored averages do not independently select the same dominant frequency. This supports a cautious interpretation: there may be a real Ramsey beat with an effective detuning offset of order 0.18 MHz, but the present dataset is not enough for a well-supported T2* or 13C claim.

The free-frequency fit's T2* near 2.3 us should be treated as a descriptive number only. It is driven by the combined trace, has moderate R2, and is not yet backed by stable per-average spectral consistency.

## Claims Not Yet Supported

- No claim-grade T2* value is supported yet.
- No nearby 13C coupling conclusion is supported yet.
- The 1.18 MHz feature should not yet be claimed as the true Ramsey carrier.
- The mismatch between programmed detuning and observed spectral content is not yet explained.
- The fine-pODMR center should remain a grid-supported operating point, not a sub-grid resonance claim.

## Recommended Next Action

Do not spend the next run on a longer blind Ramsey repeat. First run a targeted Ramsey frequency/phase-ramp diagnostic on r03: choose a detuning that separates the expected carrier and 13C sidebands from both 0.884 MHz and the new 1.18 MHz feature, keep per-average tracking and comparable shots, and require the dominant component to shift with the programmed detuning and appear coherently across stored averages. If that passes, then fit T2* and revisit the 13C sideband search; if it fails, treat the current Ramsey branch as non-claim-grade and switch to a calibration/control or alternate-sequence path.
