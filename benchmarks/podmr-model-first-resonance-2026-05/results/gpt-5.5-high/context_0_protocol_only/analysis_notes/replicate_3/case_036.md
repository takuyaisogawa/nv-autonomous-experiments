Case podmr_021_2026-05-16-171244

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse block first polarizes and detects a true 0-level reference, then skips the 1-level reference because full_expt = 0, then applies rabi_pulse_mod_wait_time followed by detection. Thus readout 1 is the no-microwave reference detection and readout 2 is the signal after the microwave-modulated Rabi pulse.

Relevant pulse parameters from the provided XML / exported variable values:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so 52 ns.
- mod_depth = 1.
- microwave frequency is the scanned value plus detuning, with detuning = 0.
- do_adiabatic_inversion is true as a variable, but the adiabatic inversion block is commented or skipped in the active path.

The combined raw traces have local dips and peaks, including a low region near 3.88-3.885 GHz in readout 2, but readout 1 also changes substantially and the per-average overlays show strong baseline motion between averages. Comparing readout 2 to the readout 1 reference gives alternating positive and negative contrast excursions rather than a consistent localized ODMR-like dip or peak. The apparent features are comparable to the average-to-average drift/noise and are not reproduced cleanly across the individual averages.

Decision: resonance_absent. I do not see a reliable pODMR resonance in the microwave-pulsed readout after accounting for the reference readout and per-average drift.
