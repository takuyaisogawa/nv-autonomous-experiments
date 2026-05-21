Case podmr_028_2026-05-13-100213.

The provided sequence is Rabimodulated.xml with mw_freq as the swept variable from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active branch has full_expt = 0, so the optional 1-level reference block is skipped. The two active detections are therefore:

1. Readout 1: true 0-level reference after adj_polarize and before the microwave pulse.
2. Readout 2: signal readout after rabi_pulse_mod_wait_time.

The pulse uses length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns, with mod_depth = 1 from the provided XML. The microwave pulse is applied before readout 2, so a pODMR resonance should appear as a frequency-localized reduction of readout 2 relative to readout 1.

The combined readouts show the strongest signal/reference contrast at 3.905 GHz: readout 1 is about 27.62 while readout 2 is about 24.12, a difference of about -3.5 counts and the lowest readout2/readout1 ratio in the sweep. This feature is also present in the per-average data: at 3.905 GHz both averages have readout 2 below readout 1, including a large contrast in the second average. The neighboring points recover, making the dip frequency-localized rather than a simple monotonic drift.

Decision: resonance_present.
