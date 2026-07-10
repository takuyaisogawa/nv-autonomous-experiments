# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- New Ramsey job artifacts: `measurement/m002.json` job request, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Raw exported data: `measurement/m001.json`, savedexperiment path `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Prior measurement context from project state/evidence: accepted r03 candidate, fine weak-pi pODMR grid-supported `mw_freq = 3.8759 GHz`, second Ramsey planned at `det = 1.0 MHz` with expected 13C sidebands near `0.615` and `1.385 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs written under `ramsey_analysis/`: `summary.json`, `analysis_output.json`, `ramsey_traces.png`, `ramsey_fft_ratio.png`.
- Checks performed:
  - Parsed `ExperimentData` shape `[1, 2, 41]` and `ExperimentDataEachAvg` shape `[1, 8, 2, 41]`.
  - Confirmed scan parameters: `tau = 0..8 us`, `41` points, `0.2 us` step, `8` averages, `50000` repetitions, `ramsey.xml`.
  - Reviewed raw signal, reference, signal/reference ratio, and per-average ratio traces.
  - Used scan-order information to compare first/last acquired signal blocks per average.
  - Ran detrended Hann-window FFT checks on raw signal and signal/reference ratio.
  - Ran fixed-frequency least-squares sinusoid checks at `1.000 MHz`, `0.615 MHz`, `1.385 MHz`, and prior scout component `0.884 MHz`.
  - Ran bounded descriptive damped-cosine fits to raw signal and ratio; these are used as diagnostics only.

## Quantitative results

- Job completed without abort; terminal final counts were `44.184 kcps`; safe shutdown was reported OK.
- Combined signal range: `46.95..51.24 kcps`; reference range: `39.31..47.03 kcps`.
- Combined signal/reference range: `1.0287..1.2461`, peak-to-peak contrast about `19.6%` of mean. Raw signal peak-to-peak contrast was about `8.7%`.
- FFT checks:
  - Ratio top bins are clustered near the programmed carrier region: `1.098 MHz`, `1.220 MHz`, and `0.976 MHz`.
  - Raw signal top bins include `0.854 MHz`, `0.976 MHz`, and `1.098 MHz`; this is closer to the programmed `1.0 MHz` detuning than the prior scout's non-claim-grade `~0.884 MHz` feature.
  - No uniquely dominant peak appears at the expected 13C sideband positions `0.615 MHz` or `1.385 MHz`.
- Fixed-frequency least-squares amplitudes on the ratio:
  - `1.000 MHz`: amplitude `0.0120`, amplitude/residual RMS `0.34`.
  - `0.615 MHz`: amplitude `0.0135`, amplitude/residual RMS `0.39`.
  - `1.385 MHz`: amplitude `0.0107`, amplitude/residual RMS `0.30`.
  - `0.884 MHz`: amplitude `0.0095`, amplitude/residual RMS `0.27`.
- Per-average ratio carrier amplitudes vary from `0.0053` to `0.0305`, with phases spread broadly rather than locked.
- Scan-order first/last acquired signal blocks vary by average from about `-6.0%` to `+8.3%`, indicating nontrivial common-mode/run variation even though the combined trace is analyzable.
- Descriptive free fits are not claim-grade:
  - Ratio fit: frequency `1.202 MHz`, `T2* ~0.95 us`, `R2 = 0.50`.
  - Raw signal fit: frequency `0.930 MHz`, `T2*` hit the upper bound near `100 us`, `R2 = 0.32`.

## Plausible interpretation

The second Ramsey produced analyzable data and shows modulation power in the intended `~1 MHz` carrier region. This is a useful improvement over the first scout because spectral content is now closer to the programmed detuning after the detuning was changed to `1.0 MHz`.

However, the fixed-frequency amplitudes are small relative to residual structure, per-average phases are not coherent, and descriptive fits disagree between raw signal and ratio. The data support "Ramsey-like modulation is present near the programmed carrier region" better than they support a precise decay or sideband model.

The `0.884 MHz` feature from the prior scout is not strengthened in this run; it is weaker than the carrier-region FFT cluster in the ratio check. That makes a fixed physical interpretation of the prior `~0.884 MHz` feature less plausible, but does not by itself identify the source of the present spectral structure.

## Claims not yet supported

- No well-supported numerical `T2*` value should be claimed from this run.
- No well-supported nearby `13C` coupling claim should be made; the expected sidebands near `0.615` and `1.385 MHz` are not uniquely resolved or per-average coherent.
- Do not claim sub-grid or fit-refined resonance precision beyond the prior fine pODMR grid-supported `3.8759 GHz`.
- Do not claim the prior `~0.884 MHz` component is physical; this det-shifted run does not provide that support.

## Recommended next action

Before repeating Ramsey blindly, run a targeted Ramsey/phase diagnostic on the same r03 branch: keep `mw_freq = 3.8759 GHz`, use a shorter high-SNR tau window that samples several cycles around the `1 MHz` carrier, and include explicit quadrature/phase or repeated identical blocks if available so carrier phase coherence can be tested across averages. If the system only supports the current Ramsey route, repeat with increased averages and use the same fixed-frequency/per-average coherence checks as the acceptance criterion; only fit `T2*` after the carrier is coherent and stable.
