Active sequence: Rabimodulated.xml, using the provided sequence XML.

The active variables show mw_freq swept from 3.825e9 to 3.925e9 Hz. The sequence has full_expt = 0, so the optional 1-level reference block is skipped. That leaves two active detections: readout 1 is the initial bright/0-level reference after optical polarization, and readout 2 is the final signal after a modulated Rabi pulse.

The relevant pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). From the provided XML/variable values, length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns, and mod_depth = 1.

Readout 1 is comparatively flat across the sweep, while readout 2 has a clear contiguous depression relative to readout 1 around roughly 3.88-3.90 GHz. The normalized readout2/readout1 ratio drops below the surrounding baseline over several neighboring frequency points, with the strongest point near 3.895 GHz. The two-average overlay is noisy and has per-average offsets, but the combined signal shows a frequency-localized dip in the signal readout rather than a matching dip in the reference.

Decision: pODMR resonance present.
