The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the optional one-level reference block is skipped. The active detections are therefore:

1. Readout 1: true 0-level reference after adj_polarize and before the microwave pulse.
2. Readout 2: signal readout after rabi_pulse_mod_wait_time.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The XML variable mod_depth is 1.

For a pODMR decision I compare the post-pulse signal to the reference, not the raw traces alone. The normalized contrast 1 - readout2/readout1 is mostly small but has repeatable positive excursions near 3.880 GHz and 3.890 GHz. At those points the signal readout is lower than the reference by about 7 percent in the combined averages, and both individual averages show positive contrast at the same scan points. There is noise and drift, but the localized, repeated signal/reference depression is consistent with a pODMR resonance.

Decision: resonance_present.
