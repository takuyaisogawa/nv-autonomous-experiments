Case podmr_042_2026-05-16-225623.

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825e9 to 3.925e9 Hz. The active instructions first polarize and detect, giving readout 1 as the true 0-level/reference readout. Because full_expt is 0, the optional 1-level reference block is skipped. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and switch_delay = 1e-07 s, followed by detection; this second detection is the microwave-pulse signal readout.

The raw data have a common downward baseline drift in both readouts across the scan, so the reference role of readout 1 matters. Even with that drift, readout 2 shows a localized low point near 3.875e9 Hz, with the signal below the reference at that point and the feature visible in both per-average traces. Nearby points recover, making this look more like a pODMR dip than a purely monotonic drift artifact.

Decision: resonance_present.
