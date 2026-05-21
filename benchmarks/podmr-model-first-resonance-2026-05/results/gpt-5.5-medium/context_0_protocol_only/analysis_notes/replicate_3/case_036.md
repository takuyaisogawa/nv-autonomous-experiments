Case podmr_021_2026-05-16-171244.

The provided sequence is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active branch has full_expt = 0, so the optional 1-level reference block is skipped. The executed sequence is: polarize, detection, wait, rabi_pulse_mod_wait_time, detection, final wait. Therefore readout 1 is the true 0-level reference acquired before the microwave pulse, and readout 2 is the signal readout acquired after the modulated Rabi pulse.

The relevant pulse settings from the XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate, giving a 52 ns pulse. The active microwave frequency is mw_freq + detuning, with detuning = 0.

The combined traces show both readouts varying over the scan with noticeable average-to-average drift. Readout 2 has a low region near 3.88-3.885 GHz, but readout 1 also trends low in the same neighborhood, and the readout-2 minus readout-1 contrast is not a clean, isolated, reproducible ODMR-like feature. The per-average overlay shows large baseline changes between the two averages, which makes the apparent dip insufficiently reliable as a pODMR resonance.

Decision: resonance_absent.
