I used the provided sequence XML and raw readout data only.

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and perform a detection, then wait, then apply rabi_pulse_mod_wait_time, then perform a second detection. Since full_expt = 0, the intermediate "1 level reference" block is inactive.

Readout roles: readout 1 is the true 0-level/reference detection before the microwave pulse. Readout 2 is the signal detection after the modulated Rabi microwave pulse.

Pulse settings: mod_depth = 1. The Rabi pulse duration is length_rabi_pulse = 5.2e-08 s, which is 52 ns; with the 250 MHz sample rate this is 13 samples and remains 52 ns after rounding.

Assessment: The raw channels drift and the scan is noisy with only two averages, so the raw signal channel alone is not a clean ODMR-shaped dip. However, using the intended readout roles, the signal/reference contrast shows its strongest positive suppression feature at about 3.900 GHz, and both averages show the same sign there. That is enough evidence for a weak pODMR resonance being present.
