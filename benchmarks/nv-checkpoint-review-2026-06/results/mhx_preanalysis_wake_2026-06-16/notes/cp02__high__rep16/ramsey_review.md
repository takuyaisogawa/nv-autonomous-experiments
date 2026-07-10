# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior/relevant evidence: `evidence/e006.md` fine weak-pi pODMR review, `evidence/e007.json` second-Ramsey model/advisory, `evidence/e013.md` handoff before the Ramsey completed.
- New Ramsey files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis_stdout.txt`, `ramsey_trace_fft.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` to parse the raw export and job metadata, reconstruct `tau = 0..8 us` with 41 points, and analyze combined plus per-average readouts.
- Sampling checks: `dt = 0.2 us`, Nyquist `2.5 MHz`, nominal span resolution `125 kHz`; the finite-length FFT bin spacing is `121.95 kHz`.
- Run completed normally: status `completed`, final counts `44.184 kcps`, `8 x 50000` repetitions, `mw_freq = 3.8759 GHz`, programmed `det = 1.0 MHz`.
- Combined readout statistics: reference mean `49.31 kcps`, signal mean `44.58 kcps`, signal/ref-line mean `0.9040`, normalized peak-to-peak `0.1536`.
- Average-to-average count provenance: reference means span `40.47..55.53 kcps`, signal means span `36.20..50.27 kcps`, relative ranges about `30.5%` and `31.6%`; snake order is balanced 4 forward / 4 reverse.
- Least-squares sinusoid screens on signal/ref-line:
  - `1.000 MHz`: amplitude `0.00564`, `R2 = 0.029`.
  - expected 13C sidebands: `0.615 MHz` amplitude `0.00974`, `R2 = 0.074`; `1.385 MHz` amplitude `0.00541`, `R2 = 0.027`.
  - prior exploratory `0.884 MHz`: amplitude `0.00586`, `R2 = 0.031`.
- Detrended Hann FFT on signal/ref-line:
  - nearest `1.0 MHz` bin (`0.976 MHz`) amplitude `0.00684`.
  - nearest prior `0.884 MHz` bin (`0.854 MHz`) amplitude `0.00468`.
  - nearest sideband bins: `0.610 MHz` amplitude `0.00812`, `1.341 MHz` amplitude `0.00747`.
  - largest bins are `1.220 MHz` amplitude `0.01618`, `1.098 MHz` amplitude `0.01551`, and `0.488 MHz` amplitude `0.01301`.
- Exploratory free-frequency sinusoid scan is not claim evidence: using all points prefers `0.465 MHz` with `R2 = 0.264`; excluding early points from `tau >= 0.4 us` prefers about `1.145 MHz` with `R2 = 0.317`.

## Plausible interpretation

- The measurement is valid as a completed, analyzable Ramsey follow-up, but it is not claim-grade for T2star or 13C.
- The prior non-claim-grade `~0.884 MHz` component does not remain dominant in this det-shifted run, so it is more plausibly artifact/noise/transient than a stable physical carrier.
- The new data may contain weak det-ish spectral content around `1.1..1.2 MHz`, but the programmed `1.0 MHz` carrier is not the dominant or well-fit component, and per-average top FFT frequencies/phases are inconsistent.
- The large tau-zero/early-time structure plus large average-to-average common count changes can plausibly leak into the FFT and simple sinusoid fits.

## Claims not yet supported

- No supported numerical `T2star`.
- No supported nearby `13C` conclusion or coupling assignment.
- No supported claim that the `1.098/1.220 MHz` FFT bins are physical Ramsey carrier frequencies.
- No supported claim that the `0.615/1.385 MHz` features are 13C sidebands.
- No supported claim that the fine-pODMR center is wrong based on this Ramsey alone.

## Recommended next action

Do not spend another long Ramsey repeat solely to improve SNR. First run a focused Ramsey route/phase-ramp diagnostic, or equivalent sequence/readout review plus short control measurement, that verifies a clean Ramsey carrier follows the programmed detuning. Require raw/readout-aware carrier presence and phase/frequency consistency across stored averages before attempting a T2star fit or 13C sideband interpretation.
