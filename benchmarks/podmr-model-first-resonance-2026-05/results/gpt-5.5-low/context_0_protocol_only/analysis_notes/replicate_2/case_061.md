Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed path first polarizes and records a detection used as the true 0/reference readout, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the signal detection. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, even though do_adiabatic_inversion is true. The active pulse duration is length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate, and mod_depth is 1 from the provided sequence variables/values.

Readout roles:

Readout 1 is the reference detection after polarization before the microwave pulse. Readout 2 is the post-pulse detection after the 52 ns modulated microwave pulse. Since the 1-level reference block is disabled, there are no additional active reference detections.

Data assessment:

The raw readouts are noisy with only two averages, and readout 1 drifts upward over the upper half of the frequency sweep. Looking at the post-pulse readout relative to the reference, the strongest negative contrast occurs near 3.905 GHz and remains negative through about 3.920 GHz. The feature is not a clean isolated Lorentzian in raw counts, but the reference-normalized contrast shows a plausible microwave-frequency-dependent suppression in the signal readout. With the active pODMR pulse in place at 52 ns and mod_depth 1, this supports calling a resonance present rather than absent.
