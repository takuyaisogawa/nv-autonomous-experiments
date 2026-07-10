# Ramsey Review: r03 Short-Tau High-SNR Diagnostic

## Files/Data Used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`, `context.json`.
- Prior Ramsey/design context: `evidence/e003.json` terminal det=1.0 MHz 8 us review, `evidence/e006.json` short-tau model/advisory, `evidence/e009.json` verified intent, `evidence/e017.md` start note.
- New terminal measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job/spec, `measurement/m003.json` completed bridge result/status, `measurement/m004.json` completed status, `measurement/m005.json` stop/control.
- Scratch outputs created here: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_review.png`.

## Calculations/Scripts Run

- Ran `python analyze_ramsey_shorttau.py`.
- Parsed the new raw export as one slice, two traces, 41 tau points, and 12 averages. Using the prior local project convention for `ramsey.xml full_experiment=0`, trace 0 is the reference and trace 1 is the Ramsey signal.
- Confirmed scan settings: tau `0.048..1.968 us`, step `48 ns`, `41` points, detuning `1.0 MHz`, `12 x 90000 = 1.08e6` shots per tau point. FFT bin spacing is `0.508 MHz`; nominal `1/span` resolution is `0.521 MHz`.
- Count/stability checks:
  - Final count was `35.122 kcps`, only `0.795x` the pre-run/latest final count `44.184 kcps`, but above the `20 kcps` gate.
  - Mean reference/signal were `48.573/44.655 kcps`; mean signal/reference ratio was `0.9195`.
  - Median point SEM was `1.138 kcps` for signal and `0.0127` for ratio.
  - Per-average common-mode range was large: reference `42.016..55.188 kcps`, signal `37.474..51.213 kcps`; the last 3 averages had only `0.875x` the mean signal of the first 9.
- Fixed-frequency least-squares checks with linear baseline:
  - At programmed carrier `1.0 MHz`: ratio amplitude `0.0274`, signal amplitude `1.282 kcps`, baseline-residual R2 improvement `0.355` ratio / `0.377` signal.
  - Expected 13C sideband targets from the local plan, `0.615423 MHz` and `1.384577 MHz`, gave similar ratio amplitudes (`0.0243` and `0.0271`) and are not separable at this short-window resolution.
  - Top ratio frequency screen was near `1.192 MHz` with amplitude `0.0363` and R2 improvement `0.656`; signal and signal/refline screens similarly peaked near `1.187 MHz`.
  - Linear-detrended ratio FFT bins: `0.508 MHz` amplitude `0.0300`, `1.016 MHz` amplitude `0.0280`, `1.524 MHz` amplitude `0.0136`.
- Direction/per-average consistency checks:
  - Forward/reverse snake groups had mean ratios `0.9088/0.9310`; their RMS difference was `0.0330`, comparable to the carrier-scale ratio amplitude.
  - Forward/reverse carrier amplitudes were `0.0311/0.0232`; top frequencies were broad and shifted (`~1.174` vs `~1.233 MHz`).
  - Individual averages were inconsistent: top ratio frequencies included low-frequency boundary hits (`0.2 MHz`), `~1.13..1.29 MHz`, and one `2.103 MHz`; carrier amplitudes ranged `0.0135..0.0441`.

## Plausible Interpretation

The short-tau/high-SNR run produced stronger early-time carrier-like structure than the previous 8 us det=1.0 MHz Ramsey. The fixed `1.0 MHz` carrier amplitude increased from the prior `0.00916` ratio / `0.277 kcps` signal to `0.0274` ratio / `1.282 kcps` signal, and the first `0.75 us` linear-residual peak-to-peak signal was `5.09 kcps`.

This is plausible evidence that r03 may have a measurable short-time Ramsey response under improved SNR, potentially with a short or otherwise hard-to-fit T2*. However, the evidence is not claim-grade: the strongest screen remains displaced toward `~1.19 MHz`, the short span cannot resolve carrier vs expected 13C sidebands, and the run had substantial common-mode count changes plus direction/per-average inconsistency.

## Claims Not Yet Supported

- No supported numeric T2star should be quoted from this dataset.
- No supported nearby-13C claim should be made; the planned sidebands are below the frequency resolution of this short scan and have amplitudes comparable to the carrier target.
- Do not claim that the `~1.19 MHz` component is a physical detuning or coupling without a det-shift/phase-controlled confirmation.
- Do not treat the final count drop and per-average common-mode movement as harmless; ratio normalization reduces but does not remove the consistency concern.

## Recommended Next Action

Do not run another blind long-window Ramsey repeat. First, record this run as a non-claim-grade but informative short-tau positive/ambiguous result. Next, do a targeted confirmation only if counts/tracking are stable: either a short-tau high-SNR det-shift check that tests whether the carrier follows the programmed detuning, or an alternate Ramsey protocol with stronger drift/phase controls. If that confirmation does not produce a carrier/decay shape that is stable across averages and acquisition directions, close the r03 Ramsey/T2star/13C branch as unsupported under current conditions.
