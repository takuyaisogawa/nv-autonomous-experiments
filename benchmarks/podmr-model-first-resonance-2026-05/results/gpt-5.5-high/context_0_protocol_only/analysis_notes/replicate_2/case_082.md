Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz. The sequence first polarizes and detects a zero-level/reference readout, then because full_expt = 0 it skips the one-level reference branch. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection. Thus readout 1 is the pre-microwave reference and readout 2 is the post-pulse signal readout.

The raw traces do not show a clear pODMR resonance. Both readouts share a broad downward drift at the high-frequency end, including the reference readout that occurs before the microwave pulse. The signal-minus-reference contrast is noisy and lacks a consistent localized dip or peak tied only to the post-pulse readout. The apparent end drop is therefore more consistent with common-mode drift or readout variation than with a resonance.

Decision: resonance_absent.
