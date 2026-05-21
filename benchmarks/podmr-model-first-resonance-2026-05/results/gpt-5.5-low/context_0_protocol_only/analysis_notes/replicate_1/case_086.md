Active sequence: Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction path has full_expt = 0, so the optional 1-level reference block is inactive. Each cycle first performs polarization and a detection giving the true 0 / bright reference readout, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 for this exported run, followed by the signal detection. Thus the two readouts are reference/bright and post-microwave-pulse signal, not separate independent resonance channels.

The combined raw traces and the signal/reference comparison are noisy. The signal-reference difference changes sign repeatedly across adjacent frequency points and there is no stable, isolated ODMR-like contrast feature that is reproduced by the two per-average traces. The strongest high-frequency variation near 3.91-3.925 GHz is not a clean resonance shape and is comparable to other fluctuations in the scan.

Decision: resonance_absent.
