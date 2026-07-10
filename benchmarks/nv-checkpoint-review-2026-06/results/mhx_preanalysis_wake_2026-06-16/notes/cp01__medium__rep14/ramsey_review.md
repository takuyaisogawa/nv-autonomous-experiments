# Ramsey review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal bridge result; `measurement/m004.json` final status; `measurement/m005.json` run control.
- Prior local context used for frequency basis: `evidence/e003.json`/`evidence/e004.json` weak-pi pODMR review inputs and `evidence/e005.json` Ramsey model/advisory.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`; outputs are `ramsey_analysis_summary.txt` and `ramsey_analysis.png`.
- Confirmed Ramsey settings from `measurement/m001.json`: `ramsey.xml`, tau `0..6 us`, 31 points, `dt=0.2 us`, `4 x 50000`, `mw_freq=3.876 GHz`, `det=1.5 MHz`, `full_experiment=0`, `length_pi_pulse=52 ns`.
- Interpreted readouts from the active sequence path: readout 1 is the mS=0 reference; readout 2 is the Ramsey signal.
- Basic readout checks: reference mean `45.318 kcps`, span `3.904 kcps`; signal mean `42.098 kcps`, span `7.750 kcps`; signal/reference mean `0.929192`, span `0.135513`.
- Per-average means show drift/common-mode variation: reference means `46.437, 43.682, 46.593, 44.558 kcps`; signal means `43.365, 40.553, 42.797, 41.677 kcps`. Terminal result final count was `38.249 kcps`, below the pre-Ramsey weak-pODMR final count `43.890 kcps`.
- FFT check used a line-corrected signal/reference trace with Hann window. Sampling gives Nyquist `2.5 MHz` and FFT bin spacing `161.3 kHz`.
- Model scale from the local frequency basis: `B ~ 359.286 G`; expected 13C Larmor `~0.385 MHz`; expected bins around det at about `1.115, 1.500, 1.885 MHz`.
- FFT amplitudes at nearest target bins: `1.129 MHz: 0.110859`, `1.452 MHz: 0.070509`, `1.935 MHz: 0.076919`. The largest FFT bins were instead `0.968 MHz: 0.170883`, `0.161 MHz: 0.166754`, and `0.323 MHz: 0.148686`.
- Fixed-frequency per-average sine components are weak/inconsistent: at `1.5 MHz`, amplitudes `0.0115, 0.0066, 0.0056, 0.0207` with R2 `0.08, 0.13, 0.01, 0.25`.
- A bounded decaying-cosine diagnostic fit returned `freq=1.456 MHz`, `T2*=0.101 us`, `R2=0.119`, with enormous uncertainties (`df ~271 MHz`, `dT2 ~2.04 us`), so the fit is not physically usable.

## Plausible interpretation

The Ramsey run completed normally and produced analyzable data, but the expected programmed Ramsey carrier near `1.5 MHz` is not dominant and the expected 13C sideband bins are not a coherent feature. The trace is better described as noisy/drift-contaminated scout data with low-frequency structure and average-to-average variation. A very short apparent fit time is not credible because the fit is underconstrained and explains little variance.

This result does not invalidate the r03 alignment evidence from pODMR. It says the first bounded Ramsey scout is not sufficient for a well-supported T2star or 13C conclusion.

## Claims not yet supported

- No supported numeric T2star value.
- No supported nearby-13C coupling or sideband assignment.
- No supported claim that r03 lacks 13C coupling; the scout SNR/drift/fit quality are insufficient for a negative conclusion.
- No supported claim that the pODMR resonance/frequency basis is wrong solely from this Ramsey measurement.

## Recommended next action

Do not blind-repeat the identical Ramsey settings. First perform a short frequency/phase diagnostic or a redesigned Ramsey repeat that improves claim quality: re-check or refresh the weak-pi pODMR center, then run a Ramsey with either a stronger deliberate detuning/phase diagnostic to verify the carrier is recoverable, or increased averages/quality controls while keeping per-average tracking windows within the advisory cap. If the carrier is recovered cleanly, then use a longer/higher-SNR Ramsey grid for T2star and FFT sideband analysis.
