Sequence-aware analysis for case podmr_017_2026-05-16-132945

The active sequence is Rabimodulated.xml while sweeping mw_freq. The sequence first performs adj_polarize followed by detection, so readout 1 is the pre-microwave true-0 reference. Because full_expt is 0, the optional 1-level reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s (52 ns), mod_depth = 1, and switch_delay = 1e-07 s before a second detection, so readout 2 is the microwave-pulse signal readout.

Across the sweep from 3.825 GHz to 3.925 GHz, readout 1 stays near the low-to-mid 40s without a matching central feature. Readout 2 shows a strong, repeatable drop centered around 3.875 GHz: the combined trace falls to about 34.17 counts at that point, and both individual averages show the same local minimum. The signal then recovers on either side. This sequence-specific contrast in the post-pulse signal readout, not present in the reference readout, is consistent with an ODMR resonance.

Decision: resonance_present.
