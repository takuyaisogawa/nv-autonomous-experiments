Sequence review:

The active sequence is Rabimodulated.xml. The instructions first polarize the NV and take a detection window, which makes readout 1 the true 0-level optical reference. The optional 1-level reference block is inactive because full_expt is 0, so the adiabatic inversion setting is not used in the active readout path. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and switch_delay = 1e-07 s, followed by the second detection window. Thus readout 2 is the signal after a 52 ns modulated microwave/Rabi pulse.

Resonance assessment:

The microwave frequency scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps. Since readout 2 is the post-pulse signal, a pODMR resonance should appear as a frequency-localized reduction of readout 2 relative to the optical reference. The combined signal/reference ratio is lowest near the upper end of the scan, especially at 3.920 GHz and 3.925 GHz, where readout 2 is below readout 1 in both individual averages. There is substantial scatter elsewhere, including isolated positive and negative fluctuations, but the high-frequency negative contrast is the clearest consistent feature and is compatible with a resonance lying near the scan edge.

Decision: resonance_present.
