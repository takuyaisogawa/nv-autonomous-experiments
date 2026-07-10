# Ramsey review: det=1.0 MHz follow-up on r03

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`.
- Follow-up model/context: `evidence/e007.json` for the planned det=1.0 MHz Ramsey model and expected 13C sidebands.
- New measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal bridge result; `measurement/m004.json` terminal status; `measurement/m005.json` control state.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed raw data shape `(slice=1, averages=8, readouts=2, points=41)`.
- Used the recorded/readout-role context for `ramsey.xml` with `full_experiment=0`: readout1 is the reference and readout2 is the Ramsey signal.
- Built tau axis `0..8 us` in 41 points, `dt=0.2 us`, Nyquist `2.5 MHz`, nominal span resolution `125 kHz` and DFT bin spacing `121.95 kHz`.
- Reviewed combined raw readouts, per-average `readout2/readout1` ratios, scan-order half deltas, Hann FFT of the linear-detrended mean ratio, exact least-squares amplitudes at `0.615423`, `0.884000`, `1.000000`, and `1.384577 MHz`, plus an exploratory single-frequency scan.
- Ran exploratory damped-cosine sensitivity checks with exponential and Gaussian envelopes, including 50 bootstrap resamples over averages.

## Key quantitative checks

- Job completed safely: `2026-05-13T20:49:36` to `22:17:11`, final counts `44.184 kcps`, `8 x 50000` shots, safe shutdown true.
- Combined readouts: reference mean `49.31 kcps`, signal mean `44.58 kcps`; combined ratio range `0.803..0.972`.
- Per-average common-mode brightness is not perfectly stable: average 7 is `18.4%` below the median brightness and is the only `>15%` brightness flag. Per-average ratio means are less extreme, `0.891..0.926`.
- FFT of the per-average-normalized mean ratio has its strongest bins at `1.098 MHz` and `1.220 MHz`, bracketing an exploratory best single-frequency fit at `1.177 MHz`.
- Exploratory best ratio fit: `1.177 MHz`, amplitude `0.0223 +/- 0.0056` ratio units, residual z about `4.0`, `R2=0.303`; per-average phase resultant `0.91`.
- Exact planned/model checks on the mean ratio are weak: `1.000 MHz` carrier amplitude `0.0094 +/- 0.0066` (`z=1.43`), low 13C sideband `0.0112 +/- 0.0066` (`z=1.71`), high 13C sideband `0.0082 +/- 0.0066` (`z=1.25`), prior scout component `0.0074 +/- 0.0067` (`z=1.11`).
- Exploratory decay fits are model-dependent: exponential nominal T2* `2.27 us` at `1.187 MHz`; Gaussian nominal T2* `4.76 us` at `1.181 MHz`. Bootstrap medians are `2.26 us` and `1.38 us`, with broad lower tails and model disagreement.

## Plausible interpretation

The new Ramsey is analyzable and likely contains a real oscillatory component near `1.18 MHz` in both raw and normalized views. This is close to, but not exactly, the programmed `1.0 MHz` phase-ramp expectation; it could reflect residual detuning, a grid-limited frequency offset, or early-tau/normalization structure. The prior scout's `~0.884 MHz` feature is not reproduced as a strong exact component here, so it should not be treated as a persistent physical frequency.

The current data do not show claim-grade 13C sidebands at the model positions `0.615/1.385 MHz`. The strongest feature is a single component near `1.18 MHz`, not a matched carrier-plus-sideband pattern.

## Claims not yet supported

- No well-supported T2* value yet. Damped fits can be made, but the extracted T2* is envelope-model-dependent and bootstrap-sensitive.
- No supported nearby 13C coupling conclusion yet.
- No supported claim that the Ramsey carrier is exactly the programmed `1.0 MHz`.
- No supported claim that the prior `~0.884 MHz` scout feature was physical.

## Recommended next action

Update the project state with this terminal review, then plan one bounded validation Ramsey on the same accepted r03 using a deliberate det shift that should move a real Ramsey carrier away from `~1.18 MHz` while keeping expected 13C sidebands within Nyquist. Before submission, run the advisory/runtime check because the completed job's expected per-average window was about `630 s`. If the shifted validation reproduces a moving coherent carrier, fit T2* jointly or consistently across the validation pair; if sidebands remain weak/absent, move toward a no-supported-13C conclusion at this SNR instead of blind repeats.
