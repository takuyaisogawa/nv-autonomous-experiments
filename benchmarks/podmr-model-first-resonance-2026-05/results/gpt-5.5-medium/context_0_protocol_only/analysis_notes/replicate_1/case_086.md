Sequence inspection:

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active readout structure is a polarized reference detection followed by, because full_expt is 0, no optional 1-level reference branch, then a modulated Rabi pulse and a post-pulse detection. Therefore readout 1 is the bright/polarized reference and readout 2 is the signal after the microwave pulse.

Relevant pulse settings:

- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the pulse duration is 52 ns.
- mod_depth = 1.
- do_adiabatic_inversion is true in the variable list, but the adiabatic inversion branch is inside the skipped full_expt block and is not active for the measured signal.

Data assessment:

The signal-reference contrast fluctuates around a small negative offset with no smooth, reproducible resonance-shaped feature. Neighboring points do not form a consistent dip or peak; the largest negative differences occur at isolated frequencies and comparable positive excursions also appear. With only two averages and visible per-average scatter, the apparent variations are consistent with noise rather than a resolved pODMR resonance.

Decision: resonance_absent.
