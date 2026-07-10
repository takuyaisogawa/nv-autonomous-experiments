# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, and `context.json` for the current objective and prior conclusions.
- `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, and `evidence/e013.md` for the fine weak-pi pODMR center and the planned second Ramsey checks.
- `measurement/m002.json` for the executed Ramsey contract: accepted r03, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us` in 41 points, 8 averages x 50000 repetitions.
- `measurement/m003.json`, `measurement/m004.json`, and `measurement/m005.json` for terminal status/control: completed 2026-05-13 22:17:11, final counts `44.184 kcps`, no abort, safe shutdown OK, no stop request.
- `measurement/m001.json` for the exported raw savedexperiment data: two readout channels, per-average data, and snake scan order.
- Generated local scratch outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_analysis_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed raw readout arrays and treated readout1 as reference/readout2 as Ramsey signal, matching the project pODMR readout convention; checked raw signal, signal/reference, and signal divided by a fitted linear reference line.
- Computed sampling checks: `dt = 0.2 us`, Nyquist `2.5 MHz`, FFT grid spacing `121.95 kHz` and nominal 8 us span resolution `125 kHz`.
- Checked least-squares sinusoid amplitudes on the reference-line-normalized trace at:
  - expected low 13C sideband `0.615423 MHz`,
  - prior component `0.884 MHz`,
  - programmed carrier `1.000 MHz`,
  - expected high 13C sideband `1.384577 MHz`.
- Scanned exploratory single-frequency fits from `0.2..2.3 MHz`.
- Tried fixed-frequency exponentially decaying cosine fits only as diagnostics, after checking signal presence.
- Checked per-average means and simple scan-order linear slopes.

## Plausible interpretation

- The measurement itself is usable in the basic execution sense: it completed, counts were healthy (`44.184 kcps` final), and the raw export contains all 8 averages.
- There is no supported Ramsey carrier at the programmed `1.0 MHz`: normalized least-squares amplitude `0.0057 +/- 0.0058`, about `1.0 sigma`, with `R2 = 0.025`.
- The prior `~0.884 MHz` component is not reproduced as a fixed feature: normalized amplitude `0.0058 +/- 0.0058`, about `1.0 sigma`, with `R2 = 0.026`.
- Expected 13C sidebands are not supported. The low sideband check at `0.615423 MHz` is only `0.0098 +/- 0.0057` (`1.7 sigma`, `R2 = 0.072`), and the high sideband at `1.384577 MHz` is `0.0054 +/- 0.0058` (`0.9 sigma`, `R2 = 0.022`).
- The strongest combined exploratory normalized sinusoid is near `0.465 MHz` (`0.0186 +/- 0.0050`, `3.7 sigma`, `R2 = 0.264`). This is interesting because the first Ramsey scout's strongest non-claim-grade component was near `0.884 MHz` at `det = 1.5 MHz`, so the dominant component may move when det is changed. However, per-average frequency/phase support is mixed, with some averages preferring other frequencies, so this is not claim-grade.
- Raw average means vary strongly between averages (`readout2` mean about `36.2..50.3 kcps`; `readout1` about `40.5..55.5 kcps`), while normalized means are tighter (`~0.890..0.925`). This looks mostly common-mode but adds caution for any weak oscillation claim.

## Claims not yet supported

- No well-supported T2star value. The fixed `1.0 MHz` decaying-cosine diagnostic fit is not interpretable as T2star; it hits the lower bound (`0.2 us`) with weak explanatory power. The exploratory best-frequency decay fit gives a numerical value near `1.75 us`, but it is tied to an unsupported frequency and should not be claimed.
- No well-supported nearby 13C conclusion. Neither expected sideband has enough amplitude, consistency, or model support.
- No supported claim that the fine pODMR center is wrong. The Ramsey data suggest possible effective detuning or sequence/phase behavior, but this measurement alone does not overturn the prior pODMR center.
- No supported claim that the old `~0.884 MHz` component was a stable fixed artifact; it was not reproduced here, but the replacement feature is also not definitive.

## Recommended next action

Do not report T2star or 13C yet. Run a compact detuning-linearity Ramsey/control on accepted r03 before spending another high-SNR T2star acquisition: after a fresh track/count gate, use the same fine-pODMR microwave center and a deliberately different `det` that keeps all expected components below Nyquist, then check whether the dominant Ramsey component moves by the programmed det change. A practical next test is `det = 2.0 MHz` with an 8 us span and enough points to keep Nyquist above `det + f13C` (or equivalently adjust point count/span to preserve sampling). If the carrier moves linearly, use that to plan a claim-grade T2star measurement at a well-identified effective carrier; if it does not, inspect the Ramsey det/phase path before more NV time.
