Active sequence: Rabimodulated.xml / Rabimodulated pODMR with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps. In the active instruction path, full_expt is 0, so the optional 1-level reference block is skipped. The executed detections are therefore:

1. adj_polarize followed by detection: bright/0-level reference readout.
2. rabi_pulse_mod_wait_time followed by detection: post-microwave-pulse pODMR signal readout.

The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s (52 ns), with sample_rate = 250 MHz. The raw traces both have an upward baseline over the scan, so the resonance decision should use the signal readout relative to the reference rather than the absolute raw slope.

Comparing readout 2 to readout 1, the normalized signal has localized depressions, with the strongest feature around 3.850-3.860 GHz. At 3.860 GHz the combined signal/reference ratio is about 0.946, lower than neighboring points near 1.048 and 1.034, and both per-average traces have readout 2 below readout 1 there. This looks like a real reference-normalized pODMR dip despite the noisy baseline.

Decision: resonance present.
