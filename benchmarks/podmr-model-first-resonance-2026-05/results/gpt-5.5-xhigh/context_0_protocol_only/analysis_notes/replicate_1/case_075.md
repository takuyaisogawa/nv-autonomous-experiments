Active sequence from inputs/sequence.xml:

- Sequence: Rabimodulated style pODMR scan, with mw_freq varied across the scan.
- Active readout roles: the first detection follows optical polarization and is the true 0-level/bright reference. The full_expt block is inactive because full_expt = 0, so the one-level reference is skipped. The second detection follows rabi_pulse_mod_wait_time and is the microwave-pulse signal readout.
- mod_depth: 1.
- Pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples after rounding, so it remains 52 ns.

Decision:

The signal readout shows a localized fluorescence dip at about 3.880 GHz: readout 2 is 45.79 while adjacent readout 2 values are near 49.2, and the reference readout at the same frequency remains near 49.5. The same point is low in both per-average signal traces, so it is not just a single-average artifact. This is consistent with a pODMR resonance.
