Active sequence and roles:

The sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active measurement path first polarizes and detects a true 0-level reference, then waits, skips the optional 1-level reference block because full_expt is 0, applies rabi_pulse_mod_wait_time using length_rabi_pulse, and detects again. Thus readout 1 is the pre-microwave 0-level reference and readout 2 is the post-microwave pulse signal.

Pulse settings used for the decision:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, i.e. 52 ns
- microwave sweep variable = mw_freq
- do_adiabatic_inversion is set true, but the adiabatic inversion call is inside commented code and is not active

Assessment:

The combined readouts fluctuate around about 50 to 52 counts with only two averages. The post-pulse signal relative to the reference does not form a reproducible pODMR resonance across the sweep. There are isolated deviations, including a high signal point near 3.915 GHz and several negative signal-reference differences, but these are not supported by a consistent line shape or by agreement between the per-average traces. The strongest-looking excursions are comparable to the readout scatter and appear noise-like rather than a coherent resonance.

Decision: resonance_absent.
