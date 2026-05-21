Case podmr_065_2026-05-17-071421.

The provided XML sequence is Rabimodulated.xml. It varies mw_freq and executes an initial polarization/detection readout as the true 0-level reference, then waits, then applies rabi_pulse_mod_wait_time followed by detection. The optional 1-level reference block is inactive because full_expt = 0. Therefore the plotted two readouts are the initial reference readout and the post-Rabi-pulse measurement readout, not a full three-readout normalization sequence.

Key sequence parameters from the provided XML:
- active pulse sequence: Rabimodulated
- readout 1 role: true 0-level optical reference after polarization, before the scanned Rabi pulse
- readout 2 role: signal readout after the scanned microwave Rabi pulse
- mod_depth: 1
- pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns
- scan: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps

The raw readouts show a slow upward drift across the scan and noticeable average-to-average offsets. The post-pulse readout does not show a clear, localized and reproducible ODMR-like dip relative to the reference. The lowest point near 3.845 GHz is isolated and coincides with strong baseline/average variation rather than a coherent resonance feature, while both channels generally trend upward and cross at high frequency. I therefore judge the resonance as absent in this measurement.
