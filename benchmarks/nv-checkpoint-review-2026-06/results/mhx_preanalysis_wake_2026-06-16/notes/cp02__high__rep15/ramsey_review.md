# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective and prior conclusions.
- `md/memory.md`, `md/knowledge.md`: local analysis policy, readout-role convention, Ramsey/FFT guardrails.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: submitted bridge job, scan variables, and intended analysis plan.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result/status/control.
- `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`: fine-pODMR center and second-Ramsey design context.

## Calculations Or Scripts Run

- Created and ran `analyze_ramsey.py`.
- Generated `ramsey_analysis_summary.txt` and `ramsey_analysis.png`.
- Checks performed:
  - Parsed combined and per-average readouts from `ExperimentData` and `ExperimentDataEachAvg`.
  - Used readout 1 as reference and readout 2 as Ramsey signal, consistent with the local two-readout convention, while reviewing raw signal, point-wise `signal/reference`, and `signal/fitted-reference-line`.
  - Verified scan grid: 41 points, tau `0..8 us`, `dt = 0.2 us`, FFT bin spacing about `122 kHz` from the 41-point rFFT / nominal Ramsey span target about `125 kHz`.
  - Checked programmed detuning `1.000 MHz`, expected 13C sidebands near `0.615/1.385 MHz`, and prior exploratory component near `0.884 MHz`.
  - Ran FFT peak checks and least-squares sinusoid-plus-linear fits at the target frequencies.
  - Ran a single-frequency sweep from `0.25..2.00 MHz`.
  - Checked per-average median readout drift and per-average best-frequency consistency.

Key quantitative results:

- Terminal run completed safely, final counts `44.184 kcps`, `8 x 50000` shots, saved raw data present.
- Combined raw readouts: reference median `49.337 kcps`; signal median `44.779 kcps`; raw signal span `7.721 kcps`; point-wise ratio span `0.1696`; fitted-reference-line normalized span `0.1536`.
- Common-mode per-average count variation is large: reference median CV `10.5%`, signal median CV `11.3%`; ratio median CV is much smaller at `1.7%`.
- Combined normalized FFT peaks are not centered on the programmed carrier:
  - `signal/reference` top FFT bins: `1.098 MHz` amplitude `0.0211`, `1.220 MHz` amplitude `0.0188`, `0.976 MHz` amplitude `0.0133`.
  - `signal/reference-line` top FFT bins: `1.220 MHz` amplitude `0.0162`, `1.098 MHz` amplitude `0.0155`, `0.488 MHz` amplitude `0.0130`.
- Least-squares checks on `signal/reference-line` are weak at the planned frequencies:
  - `0.615 MHz`: amplitude `0.00974`, amp/residual-RMS `0.393`, `R2 = 0.074`.
  - `0.884 MHz`: amplitude `0.00586`, amp/residual-RMS `0.231`, `R2 = 0.031`.
  - `1.000 MHz`: amplitude `0.00564`, amp/residual-RMS `0.222`, `R2 = 0.029`.
  - `1.385 MHz`: amplitude `0.00541`, amp/residual-RMS `0.213`, `R2 = 0.027`.
- Frequency sweep:
  - `signal/reference` best single-frequency component is near `1.180 MHz`, amplitude `0.0225`, `R2 = 0.307`, amp/residual-RMS `0.931`.
  - `signal/reference-line` best component is near `0.465 MHz`, amplitude `0.0186`, `R2 = 0.264`; a similar local component near `1.165 MHz` is present but not uniquely dominant.
  - Per-average best normalized frequencies are split: averages 1-2 prefer the low edge of the sweep (`0.500 MHz`), while averages 3-8 mostly prefer `1.16..1.27 MHz`; per-average best `R2` values are only `0.22..0.32`.

## Plausible Interpretation

- The measurement completed and is analyzable. Counts were healthy at terminal, and the r03 branch remains the aligned-candidate branch from the prior pODMR evidence.
- There is oscillatory structure in the Ramsey trace, but it is not a clean programmed-detuning Ramsey carrier. The strongest normalized components are around `1.10..1.22 MHz` or a low-frequency component near `0.465 MHz`, while the planned `1.000 MHz` carrier is weak in least-squares and FFT checks.
- The previous non-claim-grade `~0.884 MHz` component is not reproduced as a strong or dominant feature here. That weakens the case that the prior component was a stable physical signature.
- The 13C sideband test is negative at this evidence level: there is no symmetric, coherent pair near `0.615/1.385 MHz`, and the target-sideband least-squares amplitudes are small relative to residual scatter.
- The likely current state is "Ramsey signal exists but carrier/frequency behavior is not yet understood well enough for T2star extraction." A small resonance-frequency offset, phase-ramp/timing artifact, drift/common-mode structure, or analysis leakage could all contribute.

## Claims Not Yet Supported

- No numeric T2star value is supported from this run.
- No nearby-13C conclusion is supported.
- Do not claim a clean `1.000 MHz` Ramsey carrier.
- Do not claim the prior `~0.884 MHz` component as physical.
- Do not claim sidebands at `det +/- f13C`; the expected `0.615/1.385 MHz` pair is not supported.
- Do not infer sub-grid pODMR center precision beyond the earlier `3.8759 GHz` grid-supported value.

## Recommended Next Action

Do not run a blind higher-shot repeat. First run a targeted Ramsey frequency/phase diagnostic on r03 after a fresh tracking/count check and, ideally, a quick weak-pi pODMR sanity check. Use a shorter per-average window than this run: the terminal status estimated about `630 s` per average, exceeding the intended `600 s` planning cap. A compact detuning diagnostic, for example two short Ramsey scans with different programmed detunings on the same tau grid logic, should test whether the observed carrier shifts with `det` and whether the `1.1..1.2 MHz` component is physical, resonance-offset-driven, or sequence/analysis artifact. Only after the carrier behavior is stable should a longer T2star/13C measurement be designed.
