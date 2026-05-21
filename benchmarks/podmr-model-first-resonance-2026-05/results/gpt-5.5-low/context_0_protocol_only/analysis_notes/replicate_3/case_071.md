Active sequence decision:

The active sequence is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse block first performs optical polarization and detection to acquire the true 0-level reference, then because full_expt = 0 the optional 1-level reference block is skipped, and finally it applies rabi_pulse_mod_wait_time followed by detection. Thus readout 1 is the baseline/reference detection and readout 2 is the post-microwave Rabi-modulated signal detection. The relevant pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns, rounded at the 250 MHz sample rate.

Resonance assessment:

The combined readouts and per-average traces are noisy and show no stable ODMR-like dip in the microwave-modulated readout relative to the reference. There are isolated low points and sign changes in the readout difference, but they are not consistent across neighboring frequency points or across the two averages. The strongest apparent contrast changes look comparable to point-to-point noise and baseline drift rather than a reproducible resonance feature.

Decision: resonance absent.
