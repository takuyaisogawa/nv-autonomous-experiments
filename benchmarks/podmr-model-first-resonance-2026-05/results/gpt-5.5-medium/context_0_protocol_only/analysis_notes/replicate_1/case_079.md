Case podmr_065_2026-05-17-071421.

I used the provided sequence XML and raw export for the decision. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The variable values show length_rabi_pulse = 52 ns and mod_depth = 1. The instructions first acquire a true 0 level reference with adj_polarize followed by detection, then skip the "Acquire 1 level reference" block because full_expt = 0, then apply rabi_pulse_mod_wait_time with the swept microwave frequency and acquire the signal detection.

Thus readout 1 is the true 0/reference detection and readout 2 is the post-rabi-pulse detection. The raw traces mainly show a slow upward drift over frequency and point-to-point scatter. The ratio and difference between the post-pulse readout and reference fluctuate above and below baseline without a stable localized dip or line shape. The most prominent deviations are isolated and not consistent between the two averages in a way that would support a clear pODMR resonance.

Decision: resonance_absent.
