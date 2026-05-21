Active sequence and readout roles:

The provided XML and raw export identify the sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables include length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the 250 MS/s sample rate, and mod_depth = 1. The instruction block first performs polarization and detection, then waits. Because full_expt = 0, the optional Acquire 1 level reference block is not executed even though do_adiabatic_inversion is true. The only microwave manipulation in the active measurement path is therefore rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth 1, followed by detection.

Thus readout 1 is the initial post-polarization, no-microwave 0-level/reference readout, and readout 2 is the signal readout after the modulated microwave pulse. A pODMR resonance should appear as a coherent frequency-dependent reduction of the microwave-affected signal relative to the reference, not merely as both readouts drifting together.

Data assessment:

Across the sweep, both readouts fluctuate at roughly the 48-51 count level and both fall together at the high-frequency end. The readout-2 minus readout-1 difference changes sign and has several isolated deviations, but it does not form a stable, localized dip with consistent support from the two averages. The largest high-frequency drop is common-mode in both readouts, which is more consistent with baseline/count-rate drift than a microwave resonance in the post-pulse readout.

Decision: resonance_absent.
