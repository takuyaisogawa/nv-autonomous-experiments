# Ramsey Review: short-tau high-SNR diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- New measurement run: `measurement/m001.json` raw export, `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Run identity: `nv23_ramsey_20260513_230331_auto_ramsey`, saved experiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Measurement settings from the job contract/result: accepted r03 target, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 48 ns..1.968 us` in 41 points at 48 ns spacing, `12 averages x 90000 repetitions`, final text counts `35.122 kcps`.
- Generated local analysis artifacts: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis_summary.json`, `ramsey_shorttau_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- Parsed the two readout channels from `measurement/m001.json`; treated the lower, oscillatory channel as raw Ramsey signal and the upper channel as reference/control readout.
- Calculated raw signal, reference, signal/reference ratio, per-point SEM across 12 averages, per-average mean counts, least-squares sinusoid amplitudes, and a dense exploratory LS frequency screen from 0.1 to 8 MHz.
- Checked target frequencies from the prior plan/context: programmed carrier `1.000 MHz`, nominal 13C sideband positions `0.615 MHz` and `1.385 MHz`, plus prior non-claim features near `0.884 MHz` and `1.178 MHz`.
- Tried a descriptive ratio fit with linear baseline plus a fixed-`1.0 MHz` exponentially decaying cosine. This was used only as a shape check, not as a claim-grade T2star fit.

Key quantitative results:

- Aggregate raw signal: mean `44.655 kcps`, range `40.698..47.197 kcps`, median SEM `1.138 kcps`.
- Aggregate reference: mean `48.573 kcps`, range `47.568..49.744 kcps`.
- Aggregate signal/reference ratio: mean `0.91946`, range `0.83960..0.98287`, median SEM `0.01271`.
- Exploratory combined-spectrum maximum: raw signal near `1.198 MHz` with amplitude `1.64 kcps`; ratio near `1.204 MHz` with amplitude `0.0354`.
- Target LS checks:
  - `1.000 MHz`: raw amplitude `1.282 kcps`, ratio amplitude `0.0274`, ratio `R2 = 0.447`.
  - `0.615 MHz`: raw amplitude `1.103 kcps`, ratio amplitude `0.0243`, ratio `R2 = 0.411`.
  - `1.385 MHz`: raw amplitude `1.220 kcps`, ratio amplitude `0.0271`, ratio `R2 = 0.438`.
  - `0.884 MHz`: raw amplitude `0.582 kcps`, ratio amplitude `0.0126`, ratio `R2 = 0.203`.
  - `1.178 MHz`: raw amplitude `1.678 kcps`, ratio amplitude `0.0362`, ratio `R2 = 0.704`.
- Per-average frequency screens are not consistent: top ratio frequencies include clusters near `0.42 MHz`, `1.13..1.30 MHz`, and one at `2.12 MHz`.
- Common-mode counts changed substantially by average: per-average signal means span `37.47..51.21 kcps`; the minimum is `15.95%` below the median. Reference means span `42.02..55.19 kcps`; the minimum is `14.39%` below the median. Ratio means are more stable but still span about `6.83%` of the median.
- The fixed-`1.0 MHz` decay fit returned `T2star ~0.162 us` with reduced chi-square `3.41` and an unphysically large ratio amplitude (`-0.267`), so it is not a reliable T2star estimate.

## Plausible interpretation

- The short-tau/high-SNR run improved visibility relative to the prior non-claim Ramsey runs: the aggregate trace has measurable oscillatory structure, and a `1.0 MHz` component is now detectable at roughly the raw-signal SEM scale.
- The strongest aggregate component is still displaced from the programmed carrier, landing near `1.20 MHz`, close to the earlier `~1.178 MHz` screen feature rather than exactly at `1.0 MHz` or at the expected `0.615/1.385 MHz` 13C sideband positions.
- Because the aggregate trace is short-window and the LS peaks are broad/correlated, the `1.0 MHz`, `1.18..1.20 MHz`, and sideband checks are not cleanly separable by frequency evidence alone.
- The per-average inconsistency and late-run common-mode count drop argue that the aggregate oscillation may include drift, contrast/baseline changes, or other readout/systematic effects, not only coherent Ramsey precession.
- The data are consistent with a very short effective Ramsey contrast envelope being possible, but the attempted fixed-carrier decay fit is not physically stable enough to support a numeric T2star.

## Claims that are not yet supported

- Do not claim a well-supported T2star value from this run.
- Do not claim a nearby 13C coupling or resolved 13C sideband structure.
- Do not claim the `1.20 MHz` aggregate feature as a physical detuning/frequency without an independent control, because per-average screens disagree.
- Do not claim that the previous Ramsey failures were solved purely by short-tau/high-SNR sampling; this run improved aggregate visibility but did not produce claim-grade consistency.

## Recommended next action

Avoid another blind Ramsey repeat on r03. The next action should be a diagnostic that distinguishes real Ramsey phase evolution from drift/systematic structure. Best immediate choice: run a phase-cycled or detuning-shifted short-tau Ramsey control on the same r03 settings, keeping the short tau window and high shots, but changing the programmed detuning in a way that forces a true Ramsey carrier to move predictably. If that is not available in the current sequence route, switch to an alternate coherence protocol or close the r03 Ramsey/13C branch as unsupported under current conditions.
