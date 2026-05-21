# Analysis note

Active sequence: `Rabimodulated.xml` using the provided `sequence.xml` instructions. The sequence first polarizes and detects a true 0-level reference, skips the 1-level reference block because `full_expt = 0`, then applies `rabi_pulse_mod_wait_time` and detects again. Therefore readout 1 is the 0-level/no-pulse reference and readout 2 is the pODMR signal after the microwave Rabi pulse.

Parameters from the provided XML: `mod_depth = 1`, `length_rabi_pulse = 5.2e-08 s` (52 ns), and the 250 MHz sample-rate rounding leaves the pulse duration at 52 ns.

Decision: resonance_present. The signal-minus-reference trace is noisy, but the post-pulse readout has localized negative contrast relative to the reference near 3.855 GHz and 3.895 GHz, and those negative contrasts are present in both per-average traces. That is consistent with pODMR resonance dips rather than a flat no-resonance scan.
