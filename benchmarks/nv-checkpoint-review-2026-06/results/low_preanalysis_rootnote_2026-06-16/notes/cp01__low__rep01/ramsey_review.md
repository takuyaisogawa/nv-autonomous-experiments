# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Derived local artifacts: `analyze_ramsey.py`, `ramsey_review_analysis.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json` as a 31-point `tau` scan from `0` to `6 us`, `dt = 200 ns`, `4` averages, `50000` repetitions per average.
- Treated readout 1 as the reference and readout 2 as the Ramsey signal provisionally, consistent with the local sequence convention noted in project memory.
- Checked raw readouts, `readout2/readout1`, and `readout2 / linear-fit(readout1)`.
- FFT check used linear detrending plus a Hann window. The numpy FFT grid has `161.3 kHz` bin spacing and `2.5 MHz` Nyquist.
- Fit checks used empirical damped cosine models on raw signal and normalized views:
  - exponential envelope: `c + a exp(-tau/T2*) cos(2 pi f tau + phi)`
  - Gaussian envelope: `c + a exp(-(tau/T2*)^2) cos(2 pi f tau + phi)`

## Quantitative checks

- Terminal Ramsey run completed normally: `measurement/m003.json` reports savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`, no abort, no incomplete run, final count text `38.249 kcps`.
- Counts changed substantially during the targeted follow-up context: fresh r03 track was `43.535 kcps`, weak-pODMR final text was `43.890 kcps`, and Ramsey post-run final count was `38.249 kcps`. This is not a hard failure, but it is drift/count provenance.
- Readout means/ranges:
  - readout 1 mean `45.318`, range `44.038..47.942`
  - readout 2 mean `42.098`, range `38.096..45.846`
  - `readout2/readout1` range `0.859..0.995`
  - linear reference trend changes by only about `-0.68%` over the tau span.
- FFT peaks:
  - raw signal strongest bin: `0.968 MHz`; low-frequency bins at `0.161` and `0.323 MHz` are also large.
  - point-wise ratio strongest bins: `0.968`, `0.806`, `0.323`, `1.935`, `1.774 MHz`.
  - reference-line normalized signal strongest bins: `0.968`, `0.161`, `0.323`, `0.806`, `1.129 MHz`.
- Fits:
  - Best normalized exponential fit gives `f = 0.964 MHz`, `T2* = 2.04 us`, amplitude about `-0.071` in normalized units, but only `R2 = 0.481`.
  - Best point-wise ratio exponential fit gives `f = 0.944 MHz`, `T2* = 2.39 us`, amplitude about `-0.067`, but only `R2 = 0.439`.
  - Best raw-signal exponential fit gives `f = 0.962 MHz`, `T2* = 2.05 us`, but only `R2 = 0.483`.
- Per-average FFT top frequencies are not consistent enough for a strong spectral claim:
  - average 1 ratio peaks near `0.968` and `0.806 MHz`
  - average 2 ratio peaks near `1.452`, `1.935`, and `1.613 MHz`
  - average 3 ratio peaks near `0.323`, `1.129`, and `1.290 MHz`
  - average 4 ratio peaks near `0.806`, `0.161`, and `0.323 MHz`

## Plausible interpretation

- The run likely contains a real Ramsey-like oscillatory contrast in the first few microseconds; the raw and normalized views all support an oscillatory component, and the empirical fits converge near `0.94..0.96 MHz`.
- The observed dominant frequency is not the programmed `det = 1.5 MHz`. A plausible explanation is an effective microwave-resonance offset during the Ramsey run, with the actual Ramsey beat near `0.95 MHz`; this would imply a detuning mismatch of roughly `0.54 MHz` relative to the intended beat. That scale is compatible with the project context warning that several-hundred-kHz resonance shifts can occur, but this run alone does not prove the cause.
- A descriptive `T2*` scale of about `2 us` is plausible from the best empirical fits, but the low `R2`, strong low-frequency FFT content, count drift provenance, and per-average frequency inconsistency mean it should be treated as a scout estimate rather than a supported T2star conclusion.
- The expected 13C scale from project context was about `0.385 MHz`; for a `1.5 MHz` carrier, sidebands would be expected around `1.115` and `1.885 MHz`. The FFT has bins near those frequencies, but the main carrier is not cleanly at `1.5 MHz`, and per-average behavior is inconsistent. The data do not support a nearby-13C conclusion.

## Claims not yet supported

- A final, well-supported numeric `T2*`.
- A confirmed Ramsey carrier at the programmed `1.5 MHz` detuning.
- A confirmed 13C coupling or sideband assignment.
- A claim that the frequency mismatch is specifically caused by temperature, magnetic-field drift, resonance drift, sequence timing, or analysis convention. It is only evidence for mismatch in this scout run.
- A no-13C conclusion; the current data are too non-claim-grade to exclude weak sidebands.

## Recommended next action

Run a targeted resonance/frequency diagnostic before repeating a long Ramsey:

1. Re-check or repeat a short weak-pi pODMR around the accepted r03 resonance to determine whether the resonance shifted from `3.876 GHz`.
2. If the resonance is still usable, repeat Ramsey with the microwave frequency updated from that check and choose the deliberate detuning/grid so the expected carrier and `~0.385 MHz` sidebands are resolvable within Nyquist.
3. Keep per-average tracking windows under the current drift advisory cap; if runtime is tight, preserve the `6 us` span but consider more averages with fewer repetitions per average rather than extending untracked windows.
