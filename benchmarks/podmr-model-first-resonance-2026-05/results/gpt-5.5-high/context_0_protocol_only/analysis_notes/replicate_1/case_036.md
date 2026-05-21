Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first acquires the true 0 / bright-state reference by polarizing and detecting before any microwave pulse. The optional 1-level reference block is inactive because full_expt is 0. The measurement readout is then acquired after rabi_pulse_mod_wait_time with length_rabi_pulse. Therefore readout 1 is the bright reference and readout 2 is the post-pulse signal.

Key pulse settings from the provided sequence XML: mod_depth = 1, length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns.

Assessment: the two raw readouts share broad drift and crossings, but the signal relative to the reference does not form a clear, localized pODMR dip or peak. The signal-reference contrast varies irregularly, with extrema appearing at multiple unrelated frequencies, and the two averages do not show a consistent resonance-like feature. I therefore classify this as resonance absent.
