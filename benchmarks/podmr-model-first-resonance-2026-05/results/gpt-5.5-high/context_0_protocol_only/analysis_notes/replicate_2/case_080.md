Case podmr_066_2026-05-17-072831.

The provided sequence is Rabimodulated.xml. It first polarizes and performs a detection that serves as the true 0-level reference. The optional 1-level reference block is inactive because full_expt = 0, so the adiabatic-inversion setting does not create an active reference readout here. The active microwave operation for the scanned pODMR measurement is rabi_pulse_mod_wait_time followed by detection.

Sequence parameters used for the decision:
- scanned parameter: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- mod_depth: 1
- length_rabi_pulse: 5.2e-08 s, rounded at 250 MS/s to 52 ns
- readout 1 role: pre-pulse 0-level/reference detection
- readout 2 role: post-pulse signal detection after the modulated Rabi pulse

The raw readouts are noisy and only have two averages, but the signal readout relative to the reference has a localized negative contrast over adjacent points around roughly 3.880-3.895 GHz, with the signal readout dipping while the reference remains higher. The feature is not perfectly clean, but it is more structured than isolated single-point noise and is consistent with a pODMR resonance in this scan.
