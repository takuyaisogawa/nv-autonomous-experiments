# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, relevant local guidance in `md/knowledge.md`.
- Prior Ramsey/design context: `evidence/e003.json` for the previous det=1.0 MHz 8 us terminal review, `evidence/e006.json` and `evidence/e009.json` for the short-tau measurement design and exact target frequencies.
- New completed measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` run status, `measurement/m005.json` control.
- Scratch outputs created here: `scratch_ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Ran `python scratch_ramsey_analysis.py`.
- Confirmed terminal status: job `nv23_ramsey_20260513_230331_auto_ramsey` completed, no stop request, monitor `last_error=""`, safe shutdown ok, final count text `35.122 kcps`.
- Parsed Ramsey scan: `tau = 0.048..1.968 us`, 41 points at 48 ns spacing, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` repetitions.
- Interpreted readouts from embedded `ramsey.xml` with `full_experiment=0`: readout 1 is the initial `m_S=0` reference, readout 2 is the Ramsey signal.
- Raw/readout checks: reference mean `48.573 kcps`, reference peak-to-peak `2.176 kcps`; Ramsey signal mean `44.655 kcps`, signal peak-to-peak `6.499 kcps`; median stored-average signal SEM `1.138 kcps`; ratio peak-to-peak `0.1433`, median ratio SEM `0.0127`.
- Target least-squares checks with linear baseline:
  - `1.000 MHz` carrier: raw signal amplitude `1.282 kcps`, ratio amplitude `0.0274`; per-average complex component is phase-consistent with SNR proxy `6.7`.
  - `0.615423 MHz` lower 13C sideband: raw amplitude `1.102 kcps`, ratio amplitude `0.0243`.
  - `1.384577 MHz` upper 13C sideband: raw amplitude `1.222 kcps`, ratio amplitude `0.0271`.
- Frequency screens: strongest non-low-frequency LS structure is broad, with components near `1.205`, `1.124`, and `1.285 MHz`; coarse FFT bins put large power at `0.508` and `1.016 MHz`. The short 1.92 us span gives poor frequency resolution for 13C discrimination.
- Drift/provenance checks: stored-average mean signal ranged `37.47..51.21 kcps`, so common-mode count drift is substantial. Odd/even snake-direction demeaned shapes still correlate with the combined shape (`0.98` and `0.96`), so the combined tau trace is not simply an odd/even scan-direction artifact.
- Decay model profile: a fixed `1.0 MHz` carrier plus linear baseline prefers a very short envelope (`T2* ~0.185 us`) with an unphysical-large initial amplitude; allowing frequency to float over `0.7..1.6 MHz` prefers about `1.196 MHz` and `T2* ~3.0 us`. This makes the numeric T2* model-dependent, not claim-grade.

## Plausible interpretation

The short-tau/high-SNR diagnostic succeeded in revealing early-time Ramsey-like modulation that was not visible in the previous 8 us det=1.0 MHz run. The signal variation is larger than the reference variation and above stored-average SEM, and the programmed 1.0 MHz component is phase-consistent across stored averages.

However, the frequency/decay interpretation is not clean. The empirical best frequency is closer to `~1.2 MHz` than a pure `1.0 MHz` carrier, while the expected 13C sideband frequencies have similar amplitudes because the short window cannot resolve them well. Count drift during the long acquisition is also nontrivial. The most defensible conclusion is: r03 now has supported early-time Ramsey-like contrast, but the carrier frequency, decay envelope, and any 13C modulation remain unresolved.

## Claims not yet supported

- No claim-grade numeric `T2*` yet.
- No supported nearby `13C` conclusion from the Ramsey FFT/sideband evidence.
- No precise claim that the observed component is exactly the programmed `1.0 MHz` carrier.
- No claim that the `~1.2 MHz` empirical component is a physical sideband or coupling.
- No branch closeout for r03 T2*/13C until a carrier-tracking or alternate-protocol check is done.

## Recommended next action

Do not run another blind long-window Ramsey repeat. First do a targeted carrier-confirmation step: refresh/verify the weak-pi pODMR center if hardware time allows, then run a short-tau Ramsey det-shift check with the same high-SNR style and require the observed component to track the programmed detuning. If it tracks, use that confirmed carrier model to plan a longer sideband-resolving Ramsey or alternate T2*/13C protocol. If it does not track, treat the r03 Ramsey/T2*/13C branch as unsupported under current conditions and switch protocol or candidate rather than accumulating more similar Ramsey data.
