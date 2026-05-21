Case: podmr_065_2026-05-17-071421

I used the provided sequence XML before deciding. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The instruction block first polarizes and detects a true 0-level reference. The full_expt variable is 0, so the optional 1-level reference branch is inactive. The active microwave operation is therefore a single rabi_pulse_mod_wait_time call followed by the second detection, making readout 1 the bright reference and readout 2 the post-MW signal readout.

The pulse settings in the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns. At the 250 MHz sample rate this pulse length is already an integer 13 samples after rounding.

I compared the post-MW signal against the reference rather than using the raw traces alone, since both raw readouts drift upward over the scan. The readout2/readout1 contrast has several point-to-point excursions, including negative deviations near the low-frequency edge and near about 3.89 GHz, but these features are not a clean, reproducible resonance line shape over the two averages. The per-average overlays show comparable inconsistent fluctuations and baseline changes, so the apparent dips are not strong enough to identify a pODMR resonance.

Decision: resonance_absent.
