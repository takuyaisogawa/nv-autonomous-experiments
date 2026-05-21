The provided sequence is Rabimodulated.xml. In the active instructions, the first detection occurs immediately after adj_polarize and is the true 0-level reference readout. Because full_expt is 0, the optional 1-level reference block is skipped. The second active detection occurs after rabi_pulse_mod_wait_time, so readout 2 is the microwave-pulse measurement readout.

From the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 5.2e-08 s. With the 250 MHz sample rate, the rounded pulse duration remains 52 ns.

The microwave frequency sweep spans 3.825 to 3.925 GHz in 5 MHz steps. The combined post-pulse readout has a deep localized drop around 3.875 to 3.880 GHz: readout 2 falls to about 39.1 and 39.6 while most off-resonance points are around 46 to 48. The reference readout 1 stays in its usual range at the same frequencies, including about 48.5 at 3.875 GHz and 47.0 at 3.880 GHz. The same readout 2 dip is visible in both averages, so it is not just a single-average fluctuation.

Decision: resonance_present. The active microwave-modulated readout shows a frequency-localized fluorescence reduction while the reference readout does not show a matching artifact.
