# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, and `md/memory.md` / `md/knowledge.md` for local NV/Ramsey analysis rules.
- Recent supporting evidence: `evidence/e008.json` through `evidence/e011.json` for the verified Ramsey intent, pre-enqueue advisory, initial run status, and batch state.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Ramsey execution metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, and `measurement/m005.json` run control.
- Generated scratch outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` after switching Matplotlib to the `Agg` backend because the default Tk backend failed in this sandbox.
- Parsed readout 1 as the 0-level reference and readout 2 as the Ramsey signal, consistent with saved `ramsey.xml` and `full_experiment=0`.
- Confirmed scan settings: `tau = 0..6 us`, 31 points, `0.2 us` spacing, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, 4 averages x 50000 repetitions.
- Computed raw/readout summaries: reference mean `45.318 kcps`, signal mean `42.098 kcps`, signal/reference mean `0.9292`; ratio standard deviation over tau was `0.0340`.
- Estimated model scales from the weak-pi center: `B ~= 359.03 G`; expected 13C Larmor `~= 384.34 kHz`; expected Ramsey sidebands around `1.116 MHz` and `1.884 MHz` for a `1.5 MHz` carrier.
- FFT of the linearly detrended signal/reference ratio gave strongest bins at `0.968`, `0.806`, `0.323`, `1.935`, `0.161`, and `1.774 MHz`; many bins are comparable and the programmed `1.5 MHz` carrier is not dominant.
- Least-squares sinusoid checks on detrended ratio gave combined amplitudes of only `0.0058` at `1.5 MHz`, `0.0078` at `1.116 MHz`, and `0.0118` at `1.884 MHz`; per-average phases are not coherent.
- A fixed-`1.5 MHz` damped-cosine fit to ratio gives a descriptive `T2* ~= 0.50 us`, but the fit is weak: `R2 ~= 0.19`, F-test vs linear baseline `p ~= 0.146`, BIC worse than linear (`-200.10` vs `-204.10`), and `T2*` uncertainty is large (`~0.34 us`).

## Plausible interpretation

- The Ramsey scout completed normally and contains nonflat structure, so it is not a hardware/no-data failure.
- There may be a weak Ramsey-like oscillatory component, but the aggregate spectrum is broad and treatment-dependent rather than a clean carrier-plus-sideband pattern.
- The strongest ratio FFT component near `0.97 MHz` could be consistent with an effective detuning shifted by roughly `0.5 MHz` from the expected `1.5 MHz` phase ramp, but this is only a hypothesis; drift or resonance shift after weak-pi pODMR is plausible.
- The final count text dropped from the pre-run/early-run `43.890 kcps` context to `38.249 kcps`, and per-average readout means vary, so drift/tracking quality is relevant provenance.

## Claims not yet supported

- No well-supported numeric `T2*` claim: the damped-cosine fit is descriptive only and not model-selection supported.
- No supported nearby-13C claim: expected sideband locations are not phase-coherent across averages and are not uniquely stronger than neighboring FFT bins.
- No supported claim that r03 lacks 13C coupling: this scout is non-claim-grade, not a negative result.
- No supported claim that the weak-pi pODMR center remained valid during Ramsey; the Ramsey data are compatible with possible resonance/field drift but do not prove it.

## Recommended next action

Refresh the r03 resonance before another T2* attempt: run a short weak-pi pODMR around `3.876 GHz` under current tracking/count conditions, then design a Ramsey repeat from that refreshed center. For the repeat, keep per-average tracking windows within the active drift cap, preserve even snake-ordered averages, and increase claim-grade support by accumulating more averages or splitting into shorter jobs rather than relying on the present scout fit.
