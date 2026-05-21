Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. The provided sequence has full_expt = 0, so the optional 1-level reference block is inactive.

Readout roles: readout 1 is the first detection immediately after adj_polarize and is the true 0-level / bright reference. Readout 2 is the detection after rabi_pulse_mod_wait_time and is the microwave-pulse pODMR signal. The active microwave pulse uses length_rabi_pulse = 5.2e-08 s (52 ns, already on the 250 MHz sample grid) and mod_depth = 1.

Decision: resonance_present. The post-pulse readout develops a contiguous negative contrast relative to the reference over the high-frequency end of the sweep, especially around 3.910 GHz and continuing toward 3.925 GHz. The data are noisy with only two averages and the feature is near the scan edge, but the active pulsed ODMR sequence and the repeated below-reference signal trend support a real resonance rather than only isolated readout scatter.
