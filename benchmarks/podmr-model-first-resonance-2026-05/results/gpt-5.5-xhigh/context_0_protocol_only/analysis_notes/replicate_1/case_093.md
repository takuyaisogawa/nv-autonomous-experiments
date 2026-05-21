I used inputs/sequence.xml for the pulse sequence parameters. The active sequence is Rabimodulated: after polarization it records a true 0-level reference detection, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, then records the post-pulse detection. full_expt = 0, so the optional 1-level reference block is inactive. At 250 MHz sample rate the 52 ns pulse is already exactly 13 samples, so the rounded pulse duration remains 52 ns.

Readout role interpretation: readout 1 is the initial polarized/reference detection, and readout 2 is the detection after the modulated microwave/Rabi pulse. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The combined raw readouts do not show a stable pODMR resonance. The readout-2/readout-1 ratio has several isolated excursions, with minima near 3.870, 3.905, and the high-frequency endpoint, but these are comparable to the point-to-point noise and often track reference readout fluctuations rather than a clear localized dip in the post-pulse readout. The two averages also show substantial drift, so I do not see a reproducible resonance feature.

Decision: resonance_absent.
