Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided XML sets length_rabi_pulse to 52 ns and mod_depth to 1. The full_expt variable is 0, so the optional 1-level reference block is inactive. The readout roles are therefore: first detection after optical polarization as the true 0-level/reference readout, then a rabi_pulse_mod_wait_time pulse followed by the signal detection.

In the combined readouts, readout 1 stays near 28-31 counts without a narrow central loss. Readout 2, the post-microwave-pulse signal, drops from about 29 counts to about 24 counts around 3.875-3.880 GHz and then recovers toward about 29 counts, producing a localized dip relative to the reference. The individual averages have strong opposing slow drift, so the absolute per-average traces are not independently clean, but the averaged signal channel shows a frequency-localized contrast feature in the active readout role.

Decision: resonance_present.
