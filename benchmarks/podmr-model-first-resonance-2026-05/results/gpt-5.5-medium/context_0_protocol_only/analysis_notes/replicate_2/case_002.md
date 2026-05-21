Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes the NV and detects the true 0-level reference. Because full_expt is 0, the optional 1-level reference block is inactive. The active contrast readout is therefore the detection after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns. Readout 1 is the reference detection; readout 2 is the microwave-pulse readout.

Readout 2 shows a pronounced, localized fluorescence dip across the middle of the sweep, reaching about 34.7 to 35.7 counts near 3.875 to 3.88 GHz while the reference readout remains near 42 counts without a matching dip. The two averages both support reduced microwave readout in this region, although there is additional noise and a low endpoint. This pattern is consistent with a pODMR resonance being present.
