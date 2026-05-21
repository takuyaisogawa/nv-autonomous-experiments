Sequence inspection:
The active sequence is Rabimodulated.xml. It sweeps mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The pulse used before the signal detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns after sample-rate rounding and mod_depth = 1. The full_expt variable is 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is set.

Readout roles:
Readout 1 is the detection immediately after optical polarization, so it is the true 0-level/bright reference. Readout 2 is the detection after the modulated Rabi microwave pulse, so it is the pODMR signal readout. Since the 1-level reference block is skipped, there are only these two active readouts.

Decision:
The post-pulse signal readout shows a downturn relative to the bright reference over the high-frequency portion of the scan, especially around 3.900 to 3.920 GHz, where readout2/readout1 is mostly below 1 with minima near 0.969 to 0.979. The feature is not a single sharp point and the two averages are noisy, but the reference-corrected depression is broad enough and aligned with the microwave-swept signal role to count as a pODMR resonance.
