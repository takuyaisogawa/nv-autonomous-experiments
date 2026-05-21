Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this is exactly 13 samples, so the active microwave pulse duration is 52 ns. The instruction flow first performs adj_polarize followed by detection, which is the true 0-level reference readout. The optional 1-level reference branch is inactive because full_expt = 0. After that, the active measurement applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then performs detection; this is the microwave-pulsed signal readout.

The combined raw signal readout shows a clear dip centered around 3.875-3.880 GHz, falling from about 22 counts off resonance to 16.98 counts at 3.880 GHz. The reference readout does not show a matching dip and remains roughly in the 20-22 count range through this region. The signal/reference ratio reaches about 0.80 at the minimum, then recovers toward unity on the high-frequency side. This is consistent with a pODMR resonance rather than only shared fluorescence drift.

Decision: resonance_present.
