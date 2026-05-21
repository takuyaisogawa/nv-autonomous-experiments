The sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path polarizes and detects a true 0-level reference, waits, skips the optional 1-level reference because full_expt is 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before a second detection. Thus the relevant comparison is the frequency dependence of the reference readout and the post-pulse signal readout, with two averages available.

The raw combined readouts fluctuate at the count level but do not show a clear, repeatable ODMR-like contrast feature. The two readout channels cross and wander, and the per-average traces show substantial average-to-average structure and drift rather than a stable dip or peak at a common microwave frequency. There is no consistent resonance-shaped depression in the signal relative to the reference over the swept range.

Decision: resonance_absent.
