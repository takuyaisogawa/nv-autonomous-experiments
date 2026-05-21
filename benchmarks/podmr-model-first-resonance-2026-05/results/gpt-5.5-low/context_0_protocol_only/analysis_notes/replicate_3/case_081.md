Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active instructions first acquire a true 0-level reference with polarization followed by detection. Because full_expt = 0, the optional 1-level reference block is skipped. The remaining active measurement applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then performs the signal detection after the microwave pulse. Thus readout 1 is the no-microwave reference and readout 2 is the pulsed pODMR signal readout.

The combined readouts fluctuate around roughly the same level, and the per-average traces show large point-to-point scatter with only two averages. There is no reproducible, frequency-localized contrast feature that persists across averages or forms a convincing resonance lineshape. Isolated low or high points are comparable to the raw noise and drift between averages.

Decision: resonance_absent.
