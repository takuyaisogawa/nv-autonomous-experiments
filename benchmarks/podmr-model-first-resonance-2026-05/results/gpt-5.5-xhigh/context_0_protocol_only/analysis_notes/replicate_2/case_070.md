The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt is 0, so the optional 1-level reference block is skipped. The first active detection follows adj_polarize and is the true 0-level reference. The second active detection follows rabi_pulse_mod_wait_time and is the microwave-modulated signal readout.

The relevant pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With a 250 MHz sample rate, that pulse is 13 samples and remains 52 ns after rounding.

For a resonance call, the post-pulse signal should show a coherent fluorescence drop relative to the 0-level reference. The combined signal/reference contrast here is irregular: isolated negative points occur at several frequencies, while neighboring points often jump positive. The two per-average traces do not reproduce a common dip location; for example, one average has a positive feature near 3.870-3.875 GHz and a negative point later, while the other has its largest positive feature near 3.905-3.910 GHz. The reference readout also varies strongly across the scan, so the apparent raw-readout structure is not isolated to the microwave-modulated signal.

Decision: no reliable pODMR resonance is present.
