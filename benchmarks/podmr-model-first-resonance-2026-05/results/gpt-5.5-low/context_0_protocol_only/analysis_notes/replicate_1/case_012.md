Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq over 3.825e9 to 3.925e9 Hz in 5 MHz steps.
- The XML executes adj_polarize followed by detection for the true 0-level reference, then waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detects the signal.
- full_expt is 0, so the conditional 1-level reference branch is not active despite do_adiabatic_inversion being true.
- Readout role: readout 1 is the initial reference detection before the swept microwave pulse; readout 2 is the detection after the modulated Rabi pulse.
- mod_depth is 1 from the exported variable values, and the Rabi pulse duration is 5.2e-08 s (52 ns), rounded consistently at the 250 MHz sample rate.

Resonance decision:
The two averaged readouts are noisy and do not show a stable pODMR-like resonance feature across the sweep. The post-pulse readout has point-to-point fluctuations and isolated excursions, but there is no reproducible dip or contrast feature relative to the reference readout, and the two individual averages shown in the overlay do not support a consistent resonance. I classify this case as resonance absent.
