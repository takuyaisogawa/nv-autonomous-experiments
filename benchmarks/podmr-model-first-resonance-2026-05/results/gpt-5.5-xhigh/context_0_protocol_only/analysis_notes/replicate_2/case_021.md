Case podmr_006_2026-05-16-011837.

The provided sequence XML is Rabimodulated. The scan varies mw_freq from 3.825 GHz to 3.925 GHz. In the active instructions, the sequence first polarizes the NV and performs detection for the true 0-level reference. The optional 1-level reference block is inactive because full_expt is 0. The active signal arm then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth before the final detection.

Readout role interpretation:
- readout 1: polarized 0-level reference detection before the Rabi pulse.
- readout 2: final detection after the modulated Rabi pulse, carrying the pODMR signal response.

Key sequence parameters from the provided XML:
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, i.e. 52 ns.
- sample_rate = 250 MHz, so the 52 ns pulse is exactly 13 samples after rounding.

Decision:
The signal readout shows a strong localized fluorescence decrease around 3.875-3.880 GHz, dropping from roughly 39 counts to about 31 counts. This feature is present in both averages and is much larger than the surrounding point-to-point variation. The reference readout does not show a matching dip at the same frequency, so the feature is consistent with microwave-frequency-dependent pODMR contrast rather than a common readout artifact.

Prediction: resonance_present.
