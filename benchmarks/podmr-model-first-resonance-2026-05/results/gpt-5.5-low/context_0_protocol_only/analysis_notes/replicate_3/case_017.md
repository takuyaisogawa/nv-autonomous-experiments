Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first performs polarization and detection before the microwave pulse. This is the true 0-level/reference readout.
- The optional 1-level reference block is inactive because full_expt = 0, so it does not add an extra reference readout.
- The measurement readout follows rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detection.
- Therefore readout 1 is the pre-pulse/reference readout and readout 2 is the microwave-pulsed signal readout.

Data interpretation:

Readout 2 has a pronounced dip centered around approximately 3.875-3.880 GHz, falling from the mid/high 30s to about 27 counts in the combined trace. The dip is visible in both averages in the per-average overlay. Readout 1 does not show a matching dip of comparable size at the same scan position, so the feature is tied to the microwave-pulsed measurement channel rather than common drift or normalization artifact.

Decision:

A pODMR resonance is present.
