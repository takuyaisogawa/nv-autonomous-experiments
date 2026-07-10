# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior calibration/planning evidence: `evidence/e004.json`, `evidence/e005.json`, `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`.
- New Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal bridge result; `measurement/m004.json` final run status; `measurement/m005.json` control state.
- Generated local outputs: `analyze_ramsey.py`, `ramsey_analysis_results.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the new Ramsey raw export: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, 8 averages x 50000 repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Confirmed terminal run metadata: completed, not aborted, safe shutdown ok, final counts `44.184 kcps`.
- Used the project working model from the fine pODMR center:
  - `B ~= (3.8759 GHz - 2.87 GHz) / 2.8 MHz/G = 359.25 G`.
  - `13C` Larmor estimate `f13C ~= 384.6 kHz`.
  - Expected Ramsey carrier `1.000 MHz`; expected 13C sidebands `0.615 MHz` and `1.385 MHz`.
- Checked raw/reference behavior:
  - Reference mean/std: `49.31 / 0.87 kcps`.
  - Signal mean/std: `44.58 / 1.34 kcps`.
  - Signal at `tau=0`: `39.31 kcps`, versus edge median `45.07 kcps`.
- Checked scan-order drift from saved snake order:
  - No average had a common-mode drop larger than 15%.
  - Average-to-average brightness varied substantially (`ref` means `40.47..55.53 kcps`, `signal` means `36.20..50.27 kcps`), so normalization is useful but not sufficient by itself.
- FFT/least-squares checks on `signal / fitted reference line`:
  - Top FFT bins: `1.220`, `1.098`, `0.488`, `0.122`, `0.610`, `1.341 MHz`.
  - Exact-frequency normalized LS amplitudes: `0.615 MHz -> 0.0097`, prior scout `0.884 MHz -> 0.0059`, programmed `1.000 MHz -> 0.0056`, `1.385 MHz -> 0.0054`.
  - Per-average phase-coherence ratios: `0.615 MHz -> 0.73`, prior `0.884 MHz -> 0.47`, `1.000 MHz -> 0.56`, `1.385 MHz -> 0.37`.
- Dense LS scan found the largest descriptive normalized component near `0.469 MHz` (`amp ~= 0.0187`; excluding `tau=0`, `amp ~= 0.0150`), not at the programmed carrier or expected sidebands.
- Descriptive free decaying-cosine fit to normalized data returned `f ~= 0.457 MHz`, `T2star ~= 1.59 us`, `R2 ~= 0.52`; this is not used as a claim because it does not match the expected carrier/sidebands and is strongly influenced by the early-time depression.
- Fixed-frequency fit at `1.000 MHz` was not claim-grade: including `tau=0` drove the decay time to the lower-bound region (`T2star ~= 0.24 us`), while excluding `tau=0` left amplitude `~0.003` and an unconstrained upper-bound decay.

## Plausible interpretation

The measurement completed cleanly and the data are analyzable, but the new Ramsey run still does not support a well-defined Ramsey carrier. There is a robust early-time signal depression and weak spectral structure, but the exact `1.0 MHz` carrier is small, per-average phase alignment is weak, and the descriptive best component is closer to `0.47 MHz` than to the programmed detuning.

The previous scout's `~0.884 MHz` component is not reproduced as a strong signal feature here. The reference readout itself has comparable spectral peaks near `0.85..1.10 MHz`, so weak features around that range should be treated as possible reference/baseline/analysis artifacts unless a future diagnostic shows det-tracking behavior in the signal readout.

The low 13C sideband region near `0.615 MHz` has a weak component, but without a clean carrier and with no matching high-sideband support, it is not enough for a 13C conclusion.

## Claims not yet supported

- No supported numeric `T2star` value from this Ramsey run.
- No supported nearby `13C` coupling conclusion.
- No supported claim that the Ramsey carrier is exactly the programmed `1.0 MHz`.
- No supported physical assignment of the fitted `~0.46..0.47 MHz` component.
- No supported physical assignment of the prior scout's `~0.884 MHz` component.

The supported project status remains: r03 is an aligned, trackable candidate with clear pODMR resonance evidence, but T2star and 13C conclusions remain unresolved.

## Recommended next action

Do not run a blind higher-shot Ramsey repeat. First run a targeted Ramsey phase-ramp diagnostic on r03, preferably after a fresh weak-pi pODMR center check if the resonance may have drifted. The diagnostic should avoid letting the `tau=0` point dominate the fit, for example by starting at `tau >= 0.2 us`, and should compare at least two deliberate detunings. The claim criterion should be that a coherent signal-readout carrier shifts with programmed `det` and has reasonable per-average phase consistency before any T2star fit or 13C sideband interpretation is promoted.
