Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the pulse length is already on the 4 ns sample grid, so the active modulated Rabi pulse duration is 52 ns.

Readout roles from the active instructions:
- Readout 1 is the true 0-level reference: adj_polarize, then detection, then wait_for_awg.
- The optional 1-level reference block is inactive because full_expt = 0.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), followed by detection.

Decision:
The raw traces show a noticeable decline at the high-frequency end, but this decline appears in both the reference readout and the post-pulse signal readout. The signal-minus-reference and signal/reference contrast are noisy, with no reproducible localized dip across the two averages. Because the prominent feature is common-mode rather than specific to the post-pulse readout, I classify this case as resonance_absent.
