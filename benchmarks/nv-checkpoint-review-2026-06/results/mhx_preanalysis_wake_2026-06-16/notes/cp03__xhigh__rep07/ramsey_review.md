# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior local context/evidence: `evidence/e003.json` for the previous det=1.0 MHz 8 us terminal Ramsey review, `evidence/e006.json` for the short-tau/high-SNR design, and `evidence/e017.md` for the short-tau job start note.
- New terminal measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.

## Calculations or scripts run

- Wrote and ran `python scratch_ramsey_analysis.py`; output summary is `scratch_ramsey_analysis_summary.json`.
- Confirmed run integrity: job `nv23_ramsey_20260513_230331_auto_ramsey` completed, no error code/message, no stop request, `safety_aborted=false`, safe shutdown ok, final count text `35.122 kcps`.
- Confirmed scan: `ramsey.xml`, `full_experiment=0`, tau `0.048..1.968 us`, step `48 ns`, 41 points, `12 x 90000 = 1.08e6` shots per tau point, `mw_freq=3.8759 GHz`, programmed `det=1.0 MHz`.
- Used readout 1 as true `mS=0` reference and readout 2 as Ramsey signal, consistent with the local protocol review for this route.
- Scan-order drift check using `ScanOrderEachAvg` snake order found no flagged averages; max common-mode drop score was `0.060`, below the `0.15` flag threshold.
- Raw/readout scatter: reference mean `48.573 kcps`, signal mean `44.655 kcps`, median signal SEM across stored averages `1.138 kcps`, median ratio SEM `0.0127`.
- The short-tau trace has visible early-time structure: first `0.75 us` peak-to-peak is `5.69 kcps` in raw signal and `0.111` in signal/reference ratio.
- Linear-baseline plus sinusoid least-squares checks:
  - Programmed carrier `1.0 MHz`: raw signal amplitude `1.28 kcps`, ratio amplitude `0.0274`, ratio residual improvement `0.355`.
  - Expected 13C sideband targets from prior plan, `0.615 MHz` and `1.385 MHz`: ratio amplitudes `0.0243` and `0.0271`; not dominant or separable with this short window.
  - Prior unexplained second-Ramsey component near `1.178 MHz`: raw signal amplitude `1.68 kcps`, ratio amplitude `0.0362`, ratio residual improvement `0.654`.
  - Combined top ratio LS screen is near `1.192 MHz` with amplitude `0.0363`.
- Damped-cosine checks are model-dependent: forcing `1.0 MHz` gives `T2* ~0.16..0.19 us` but requires a very large initial amplitude (`~9.8 kcps` raw / `0.264` ratio) and fits worse. Letting frequency float gives `f ~1.18..1.21 MHz`, `T2* ~1.75..2.20 us`, and more plausible amplitude (`~2.9 kcps` raw / `0.052` ratio), but the upper T2* bound is broad and frequency is not the programmed carrier.

## Plausible interpretation

- The short-tau/high-SNR diagnostic did what it was designed to do: it improved the practical scatter and revealed an early-time Ramsey-like oscillatory component that was mostly washed out or ambiguous in the previous 8 us scan.
- The dominant component is closer to `1.18..1.21 MHz` than to the programmed `1.0 MHz`. Because the previous 8 us scan also had its largest exploratory component near `1.178 MHz`, this is plausibly a real repeatable beat under current conditions rather than a one-off FFT peak.
- A plausible physical explanation is that the effective Ramsey beat includes a resonance-center offset or drift relative to the fine pODMR center used for `mw_freq`; a route/phase convention or analysis artifact is also still possible.

## Claims that are not yet supported

- Do not claim a final numeric T2*. The data support an oscillatory short-tau feature, but the fitted T2* changes qualitatively depending on whether the frequency is forced to `1.0 MHz` or allowed to float near `1.2 MHz`.
- Do not claim nearby 13C coupling. The short `1.92 us` span has only about `0.52 MHz` nominal resolution and was not designed to resolve the `0.615/1.385 MHz` sideband pair; target sideband amplitudes are not uniquely dominant.
- Do not claim that the `~1.19 MHz` component is definitely the programmed carrier, a 13C sideband, or a hardware artifact. The current data discriminate signal presence better than signal origin.
- Do not use the forced-`1.0 MHz` `T2* ~0.16..0.19 us` fit as a result; it is a worse, highly constrained model with a large initial amplitude requirement.

## Recommended next action

Do not run another blind long-window Ramsey repeat. Run a frequency-discrimination follow-up: first re-check the weak-pi/fine pODMR center near `3.8759 GHz` to test whether a `~0.18..0.20 MHz` resonance shift explains the `~1.19 MHz` Ramsey beat, then use the same short-tau high-SNR Ramsey window with a deliberately changed `det` if needed. The decision criterion should be whether the observed beat tracks the programmed detuning/resonance offset; only after that should a longer decay/13C scan be designed.
