Case: podmr_039_2026-05-16-221215

Provided sequence XML / raw export identify the active sequence as Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path is:

- Polarize, then detection: this is readout 1, the bright/0-level reference.
- Wait.
- Apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- Detection: this is readout 2, the post-microwave-pulse signal.

The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so do_adiabatic_inversion is not used for an acquired readout in this run. The sample rate is 250 MHz, so 52 ns corresponds to 13 samples and remains 52 ns after rounding. Other relevant timing is delay_wrt_1mus = 0.2 us, switch_delay = 0.1 us, wait_time = 2 us, and length_last_wait = 1 us.

For a pODMR resonance in this sequence, I would expect readout 2 to show a reproducible fluorescence depression relative to readout 1 at the resonant microwave frequency. The combined data have possible negative excursions around 3.845-3.850 GHz and near the high-frequency edge, but the 3.845-3.850 GHz depression is immediately followed by a strong positive excursion at 3.855 GHz in both averages, and the high-frequency dip is mainly driven by one average rather than being consistently reproduced. Readout 1 also fluctuates on a comparable scale, so the readout-2/reference contrast does not form a clean resonance-shaped feature.

Decision: resonance_absent.
