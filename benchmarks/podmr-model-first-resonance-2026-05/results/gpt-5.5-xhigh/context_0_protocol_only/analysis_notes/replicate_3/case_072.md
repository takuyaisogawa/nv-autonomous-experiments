Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is set true. The active detections are therefore:

1. adj_polarize followed by detection: readout 1, the pre-microwave 0-level/reference readout.
2. rabi_pulse_mod_wait_time followed by detection: readout 2, the post-microwave signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The exported values give sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1. The pulse duration rounds to 52 ns exactly at this sample rate, i.e. 13 samples.

Data assessment:

Because readout 1 is the reference and readout 2 is the post-pulse signal, the relevant contrast is readout2/readout1 or readout2 - readout1. The combined ratio reaches clear local lows at 3.885 GHz and 3.890 GHz, both about 0.931, with readout2 - readout1 = -3.23 counts at both points. There is another negative feature near 3.910 GHz and a negative endpoint at 3.925 GHz. The 3.885 GHz dip is present in both individual averages, and the 3.910 GHz point is also negative in both averages. Other points fluctuate, but these repeated localized drops in the post-pulse readout relative to the pre-pulse reference are consistent with pODMR contrast.

Decision:

A pODMR resonance is present.
