Case podmr_077_2026-05-17-100811 analysis

The provided sequence XML is Rabimodulated.xml. The active instructions polarize the NV, acquire a detection readout as the true 0-level/reference readout, wait, skip the 1-level reference block because full_expt is 0, then apply rabi_pulse_mod_wait_time and acquire the post-microwave signal readout. Thus readout 1 is the reference before the microwave pulse and readout 2 is the signal after the microwave pulse.

From the provided XML and variable values, the microwave sweep is over mw_freq, mod_depth is 1, and length_rabi_pulse is 5.2e-08 s, rounded at the 250 MHz sample rate to 52 ns. The sequence uses freqIQ = 50 MHz, mw_ampl = -5 dBm, ampIQ = 5 dBm, delay_wrt_1mus = 0.2 us, and length_last_wait = 1 us.

The combined raw traces do not show a clean pODMR resonance. A resonance would appear as a localized decrease in the post-microwave signal relative to the reference, preferably visible consistently across averages. Here readout 2 fluctuates around readout 1, the normalized contrast changes sign across the scan, and the largest apparent negative contrasts are not a stable interior resonance feature. The low point near the high-frequency end is shared by both readouts, which is more consistent with baseline/readout variation than microwave-driven contrast. The per-average overlays also show large average-to-average offsets and no consistent dip at the same frequency.

Decision: resonance_absent.
