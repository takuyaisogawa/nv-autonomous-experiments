Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided XML has full_expt = 0, so the optional 1-level reference block is inactive. The active acquisition is:
1. adj_polarize followed by detection: readout 1, the polarized/true-0 reference.
2. rabi_pulse_mod_wait_time followed by detection: readout 2, the signal after the microwave pulse.

The pulse settings used for the active microwave pulse are length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns, with mod_depth = 1 and switch_delay = 100 ns. The microwave is set from the scan frequency with freqIQ = 50 MHz.

The raw traces are noisy but readout 2 has a clear isolated suppression at about 3.88 GHz: the combined readout 2 value drops to about 45.8 while readout 1 remains near 49.5. This dip appears in both per-average readout 2 traces, so it is not just a single-average artifact. Other points fluctuate, but the 3.88 GHz feature is the strongest readout-selective contrast in the scan.

Decision: pODMR resonance present.
