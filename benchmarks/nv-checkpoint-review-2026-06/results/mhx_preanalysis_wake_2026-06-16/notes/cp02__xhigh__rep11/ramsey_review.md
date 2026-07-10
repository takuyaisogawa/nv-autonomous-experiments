# Ramsey review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/state.md`, `project/advice.md`, `context.json`.
- Prior relevant notes/model: `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` run control.
- Derived local artifacts: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_trace_fft.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- The script reads only local files and computes raw signal, signal/reference, reference-line-normalized signal, Hann-window FFTs, fixed-frequency least-squares sinusoid fits, per-average phase/amplitude checks, scan-order drift checks, and sensitivity subsets excluding low-brightness averages.
- Generated `ramsey_analysis.json` and `ramsey_trace_fft.png`; PNG integrity was checked with PIL after the image viewer could not open it.

Key measurement facts:

- Job `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg` completed at `2026-05-13T22:17:11` with final counts `44.184 kcps`; status elapsed time `5256 s`; no terminal error code.
- Scan was `tau = 0..8 us`, `41` points, `0.2 us` step, `8 x 50000` repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- FFT bin spacing from the sampled array is `121.95 kHz`; Nyquist is `2.5 MHz`.
- Mean reference readout was `49.31 kcps`, mean signal readout was `44.58 kcps`, mean signal/reference was `0.9042`.
- Average 7 had low common brightness, `0.816` of median, but within-average scan-order end-minus-start fractions were only `-0.039..+0.105`; no large monotonic in-average drop by the local drift check.

Frequency checks:

- Expected carrier at `1.000 MHz`, expected 13C sidebands near `0.615` and `1.385 MHz`, prior scout artifact/check frequency near `0.884 MHz`.
- Signal/reference fixed-frequency fit at `1.000 MHz`: amplitude `0.00944 +/- 0.00651`, `1.45 sigma`, `p = 0.354`, `R2 = 0.055`.
- Signal/reference fixed-frequency fit at low sideband `0.615 MHz`: amplitude `0.01347 +/- 0.00657`, `2.05 sigma`, `p = 0.137`, `R2 = 0.102`.
- Signal/reference fixed-frequency fit at high sideband `1.385 MHz`: amplitude `0.01036 +/- 0.00665`, `1.56 sigma`, `p = 0.308`, `R2 = 0.062`.
- Prior `0.884 MHz` feature is not reproduced: signal/reference amplitude `0.00958 +/- 0.00612`, `p = 0.305`; raw-signal amplitude `0.264 +/- 0.271 kcps`, `p = 0.627`.
- FFT top ratio peaks are exploratory near `1.098 MHz` and `1.220 MHz`; best grid-search ratio fit is near `1.173 MHz` with amplitude `0.0214`, but raw/refline-normalized observables prefer about `0.461 MHz`. This mismatch argues against a physical claim.
- Per-average signal/reference fits are not coherent enough: at the carrier, per-average `R2` values are all `<= 0.077`; low-sideband phase resultant is only `R = 0.43`.
- Excluding the lowest-brightness average does not recover the carrier. It can make the low-sideband-like component nominally stronger, but the carrier and high sideband remain unsupported and the average consistency remains weak.

## Plausible interpretation

The run produced usable terminal data, but it did not validate the planned Ramsey carrier. The expected `1.0 MHz` carrier is weak in raw, ratio, and reference-line-normalized checks, and the expected 13C sideband pair is not jointly present. The prior non-claim-grade `~0.884 MHz` feature from the first scout also does not reproduce, which makes a fixed artifact/noise explanation more plausible than a stable physical Ramsey component.

There may be weak oscillatory structure in the ratio near `1.1..1.2 MHz`, and raw/refline-normalized data show exploratory low-frequency structure near `0.46..0.49 MHz`, but the frequency disagreement across observables and scattered per-average support make these descriptive only.

## Claims not yet supported

- No supported T2star value from this dataset.
- No supported 13C coupling or sideband conclusion.
- No supported claim that the `1.17 MHz` ratio feature or `0.46 MHz` raw feature is physical.
- No supported claim that the accepted pODMR center gives a working Ramsey carrier under this sequence/settings.
- Do not discard average 7 just to promote the low-sideband-like feature; that would be post-selection without enough corroboration.

## Recommended next action

Do not run another long T2star/13C Ramsey scan blindly. First do a short carrier/sequence diagnostic on the same r03 branch after confirming tracking and the pODMR center: use a shorter tau window with dense enough sampling to verify that a programmed detuning produces a coherent carrier in raw and signal/reference data with stable per-average phase. If that succeeds, then run the longer T2star/FFT measurement. If it fails again, debug the Ramsey phase path, pi/2 calibration/readout roles, and count stability before making any T2star or 13C claim.
