I used the provided sequence XML before deciding. The active sequence is Rabimodulated: set the microwave, polarize, acquire the first detection as the true |0> reference, wait, skip the optional |1> reference block because full_expt = 0, then apply rabi_pulse_mod_wait_time and acquire the final detection. Thus readout 1 is the no-microwave bright-state reference and readout 2 is the microwave-pulse signal readout.

The standalone XML sets length_rabi_pulse = 5.2e-08 s; at sample_rate = 250 MHz this rounds to 13 samples, still 52 ns. It sets mod_depth = 1 for the active Rabi-modulated pulse.

The scan sweeps mw_freq from 3.825 GHz to 3.925 GHz. In the combined readouts, the clearest microwave-dependent feature is a dip in readout 2 near 3.900-3.905 GHz relative to readout 1. At 3.905 GHz, readout 1 is about 27.62 and readout 2 is about 24.12, giving the lowest signal/reference ratio, about 0.873. The neighboring points recover by 3.910-3.915 GHz. The per-average traces are noisy, but both averages show negative signal-minus-reference contrast at 3.905 GHz, so the feature is not only a single combined-average artifact.

Decision: resonance_present.
