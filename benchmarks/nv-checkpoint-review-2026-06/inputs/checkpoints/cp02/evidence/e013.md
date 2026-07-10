# Fine pODMR review and second Ramsey start

Question: after the fine weak-pi pODMR terminal result, what is the next safe step toward T2star and 13C conclusions for accepted r03?

Inputs read:
- Fine pODMR terminal bridge result/status/job and final savedexperiment raw export.
- Fine pODMR drift diagnostic.
- Active `Rabimodulated.xml` and `ramsey.xml` / validated `auto__ramsey` manifest.
- First Ramsey raw/FFT review and current project state/human advice.

Action taken:
- Completed the fine-pODMR experiment intent and copied terminal bridge artifacts into `work/bridge_jobs/`.
- Reviewed terminal fine-pODMR raw signal, point-wise ratio, fitted-reference-line normalization, per-average minima, and drift.
- Authored and verified a new Ramsey intent, recorded the model/advisory, and submitted a managed `auto__ramsey` execute job.

Result:
- Fine pODMR supports a refined grid center at `mw_freq_hz = 3.8759e9`; raw drop is about 11.9% vs edge median and drift flags no averages.
- The second Ramsey/T2star/13C follow-up is running as `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- It scans `tau = 0..8 us` in 41 points with `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`, and `8 x 50000` shots.
- The model expects a carrier near 1.0 MHz and possible 13C sidebands near 0.615/1.385 MHz; the det shift also tests whether the prior non-claim-grade ~0.884 MHz component is fixed artifact/noise.
- Pre-enqueue advisory had no blockers and estimated 554.768 s per average under the 600 s cap. Live status after materialization is running, average 1/8, final-count text `Final = 43.445 kcps`.

Checks actually performed:
- `verify-experiment-intent` returned verdict `verified` with bridge idle.
- Advisory JSON was parsed and had `ok=true`, no blockers, and no recommended actions.
- Bridge running status was read after submission and project copies of job/status/batch state were written.

Remaining uncertainty:
- The bridge batch runner process was terminated by the tool timeout after the bridge job had materialized; the live bridge job is the source of truth, and the copied batch state may not contain the final queue-submit event.
- Runtime status estimated 629.8 s per average after execute materialization, higher than the pre-enqueue advisory's 554.8 s but with no monitor anomaly. Do not stop solely for this; review terminal drift/count evidence.

Next pointer:
- Wait for terminal result. Then copy terminal artifacts, complete intent `image145844_reimage_r03_ramsey_det1p0_8us_8avg_20260513_2042`, raw-export, run drift analysis, and review raw/FFT evidence before any T2star or 13C claim.
