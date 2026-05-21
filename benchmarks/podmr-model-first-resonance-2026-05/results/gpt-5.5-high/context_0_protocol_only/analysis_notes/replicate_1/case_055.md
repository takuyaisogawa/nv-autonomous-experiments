Active sequence: Rabimodulated pODMR with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active XML path polarizes and detects first, then waits, skips the optional 1-level reference because full_expt = 0, then applies rabi_pulse_mod_wait_time followed by the second detection.

Readout roles: readout 1 is the polarized true 0-level reference detection. Readout 2 is the measurement detection after the modulated Rabi pulse. There is no separate 1-level reference in this run.

Pulse settings from the provided sequence XML: mod_depth = 1, length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The active microwave pulse is therefore a 52 ns modulated Rabi pulse.

Decision: readout 1 is nearly flat across the sweep, while readout 2 shows a clear reduction relative to readout 1 over the resonance region, with the deepest contrast near 3.895 GHz and adjacent depressed points around 3.88-3.90 GHz. The feature is larger than the reference variation and has the expected pODMR sign, so I classify this case as resonance present.
