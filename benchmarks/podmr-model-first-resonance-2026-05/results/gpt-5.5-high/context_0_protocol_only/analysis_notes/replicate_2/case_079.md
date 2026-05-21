Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. In the provided sequence XML, full_expt is 0, so the optional 1-level reference block is inactive. The executed readouts are therefore: first detection after optical polarization, serving as the true 0-level/reference readout; then a modulated microwave Rabi pulse followed by the second detection, serving as the pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, i.e. 52 ns. The provided sequence XML and exported variable values identify mod_depth = 1.

The two raw readouts both have drift over the scan, so I used the relationship of the post-pulse signal readout to the preceding reference readout rather than the absolute raw levels. The signal/reference contrast is noisy and not a clean textbook dip, but both individual averages show a local reduction of the post-pulse readout relative to the reference near 3.89 GHz, and the combined trace has its strongest interior negative contrast in that same region compared with nearby scan points. Similar low contrast appears near the low-frequency edge, but that edge feature is less useful as a centered resonance decision.

Decision: weak pODMR resonance present.
