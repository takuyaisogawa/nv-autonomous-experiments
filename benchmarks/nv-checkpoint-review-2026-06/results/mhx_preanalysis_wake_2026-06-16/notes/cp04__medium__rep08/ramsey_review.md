# Ramsey Review: r03 det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- New completed measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior local context for the det-shift rationale: `evidence/e008.json` terminal det=1.0 MHz short-tau review and `evidence/e019.json` det-shift model/start note.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs written: `ramsey_detshift_analysis.json` and `ramsey_detshift_review.png`.
- Checks performed:
  - Parsed readouts as `ramsey.xml full_experiment=0`: readout 1 reference, readout 2 Ramsey signal, per local protocol note in `evidence/e019.json`.
  - Confirmed acquisition: `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 48 ns..1.968 us` in 41 points, 12 averages x 90000 repetitions = 1.08e6 shots per tau, final counts `44.796 kcps`.
  - Built raw signal, raw reference, point-wise `signal/reference`, and `signal / fitted-reference-line` views.
  - Estimated stored-average SEM: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`.
  - Linear-baseline residual peak-to-peak: signal `6.29 kcps`, ratio `0.133`.
  - Ran least-squares sinusoid screens with linear baseline, FFT checks, target-frequency amplitudes, skip-early-time screens, and per-average frequency screens.
  - Ran a simple common-mode stored-average drift proxy; no averages exceeded the +/-15% flag threshold. Scan order was `snake`, saved in tau order.

## Quantitative results

- Prior det=1.0 MHz short-tau run (`evidence/e008.json`): strongest combined ratio screen near `1.192 MHz`, ratio LS amplitude `0.03631`, raw-signal amplitude `1.684 kcps`; no T2star/13C claim was supported.
- Det-shift hypothesis from `evidence/e019.json`: if the `1.192 MHz` feature is a physical Ramsey carrier with an effective +192 kHz offset, changing `det` from 1.0 to 1.5 MHz should move it to about `1.692 MHz`; predicted 13C sidebands are about `1.307 MHz` and `2.077 MHz`.
- New det=1.5 MHz run:
  - Combined ratio all-tau LS top: `1.623 MHz`, amplitude `0.02547`, R2 improvement `0.430`.
  - Ratio amplitude at predicted shifted carrier `1.692 MHz`: `0.02505`, R2 improvement `0.411`.
  - Ratio amplitude at programmed carrier `1.5 MHz`: `0.02399`, R2 improvement `0.359`.
  - Ratio amplitude at old fixed component `1.192 MHz`: `0.00511`, R2 improvement `0.0167`.
  - Predicted 13C sideband amplitudes are weak: low `1.307 MHz` ratio amplitude `0.00953`, high `2.077 MHz` ratio amplitude `0.00614`.
  - Raw signal and fitted-reference-line views do not select the shifted-carrier region: both all-tau screens peak near `0.882 MHz`; skipping tau <= 0.2 us moves them near `0.805..0.806 MHz`.
  - Ratio skip-tau<=0.2 us top moves to `0.746 MHz`, not to `1.5` or `1.692 MHz`.
  - Per-average ratio screens are inconsistent: top frequencies include `0.25`, `0.79..0.90`, `1.20`, `1.54`, `1.66..1.75`, and `3.86 MHz`; only some averages favor the shifted-carrier target.

## Plausible interpretation

The new run is analyzable and does not show an obvious completion/count anomaly. It argues against a simple fixed `1.192 MHz` normalized-feature hypothesis because the old component is small in the combined ratio screen after the det change. The combined ratio view has appreciable power near the predicted shifted carrier region (`1.623..1.692 MHz`), which is qualitatively consistent with some det tracking.

However, the evidence is still mixed. The raw-signal and fitted-reference-line views are dominated by a lower-frequency component near `0.88 MHz`, early-time exclusion changes the preferred frequencies substantially, and per-average screens are not consistent. This looks more like a protocol/baseline/transient-sensitive Ramsey branch than a clean physical carrier plus sideband model.

## Claims that are not yet supported

- A numeric T2star for r03 is not supported from this measurement.
- Nearby 13C coupling is not supported; the predicted sidebands at about `1.307` and `2.077 MHz` are weak and not dominant.
- The `1.623..1.692 MHz` ratio feature should not be claimed as a clean Ramsey carrier because it is not supported consistently by raw signal, fitted-reference-line normalization, skip-early-time checks, and stored averages.
- The earlier descriptive T2star values from prior short-tau fits remain descriptive only.

## Recommended next action

Do not run another blind Ramsey repeat on this same branch. The next useful step is a bridge-free synthesis/closeout of the r03 Ramsey evidence: aligned r03 remains supported, but T2star and 13C remain unsupported under the current Ramsey protocol. If the project requires another experiment rather than closeout, switch protocol or calibration strategy rather than accumulating more same-style short-tau Ramsey data; a Hahn echo or an explicit sequence/readout artifact diagnostic would be more informative than another det-only repeat.
