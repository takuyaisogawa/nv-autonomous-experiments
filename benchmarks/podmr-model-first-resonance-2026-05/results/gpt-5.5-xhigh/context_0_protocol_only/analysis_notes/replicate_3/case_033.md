I used the provided sequence XML before deciding.

The active sequence is Rabimodulated.xml with mw_freq as the swept variable. The instruction block first acquires a true 0-level reference: adj_polarize, then detection, then wait. The optional 1-level reference block is skipped because full_expt = 0. The second acquired readout is therefore the signal readout after the active rabi_pulse_mod_wait_time pulse followed by detection.

Relevant sequence settings from the provided XML: sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, delay_wrt_1mus = 200 ns, and length_last_wait = 1 us. The 52 ns pulse is already an integer 13 samples at 250 MHz, so rounding leaves it at 52 ns.

The scan covers 3.825 to 3.925 GHz in 5 MHz steps. Readout 1, the 0-level reference, stays broadly near the high-40 count level through the central region. Readout 2, the post-pulse signal readout, shows a clear localized dip: about 42.9 at 3.870 GHz, 39.8 at 3.875 GHz, and 39.0 at 3.880 GHz, recovering afterward. The same central suppression is visible in both averages, so it is not a single-average artifact.

Decision: a pODMR resonance is present, centered near 3.875 to 3.880 GHz.
