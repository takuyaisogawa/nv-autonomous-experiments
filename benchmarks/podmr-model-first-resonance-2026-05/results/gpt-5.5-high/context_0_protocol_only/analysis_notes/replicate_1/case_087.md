Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional 1-level reference block is inactive. The active readouts are:
- readout 1: detection immediately after adj_polarize, serving as the bright/0-level reference.
- readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse, serving as the microwave-pulsed signal.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The provided sequence XML sets mod_depth = 1.

Decision: resonance_present.

Reasoning: A pODMR resonance should appear as a reduction of the post-microwave signal readout relative to the 0-reference readout at the resonant microwave frequency. The combined signal-reference contrast is noisy overall, but the point near 3.910 GHz has a large negative contrast, about -2.37 counts, and this dip is present in both individual averages. There is also a smaller repeated negative excursion near 3.855 GHz. The repeated negative contrast at 3.910 GHz is stronger than the surrounding point-to-point fluctuations and is consistent with a pulsed ODMR resonance.
