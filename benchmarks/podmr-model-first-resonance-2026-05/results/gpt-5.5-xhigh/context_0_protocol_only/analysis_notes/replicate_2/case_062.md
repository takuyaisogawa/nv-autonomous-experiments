Sequence inspection:

- The scan uses Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz.
- The active pulse sequence first polarizes and records a detection used as the true 0-level reference.
- The optional 1-level reference block is inactive because full_expt is set to 0, so that intermediate readout is skipped.
- The active microwave operation before the signal readout is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- The modulation depth used for that pulse is mod_depth = 1.
- Therefore readout 1 is the 0-level reference, and readout 2 is the post-microwave-pulse signal readout.

Data assessment:

The post-pulse signal readout falls below the reference over a contiguous region near 3.895 to 3.910 GHz. In the combined data, the signal-reference contrast is about -4.2%, -3.6%, -2.1%, and -4.9% at 3.895, 3.900, 3.905, and 3.910 GHz respectively, with recovery on the high-frequency side. Both individual averages show negative signal-reference contrast through most of this same region, which makes it more consistent than isolated single-point excursions elsewhere in the scan.

Decision:

A pODMR resonance is present.
