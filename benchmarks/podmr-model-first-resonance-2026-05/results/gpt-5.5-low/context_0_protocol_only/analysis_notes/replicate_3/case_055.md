Sequence inspection:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The variable values used for this run include length_rabi_pulse = 5.2e-08 s, mod_depth = 1, full_expt = 0, and do_adiabatic_inversion = 1.

Because full_expt is 0, the conditional "Acquire 1 level reference" block is skipped. The active readout roles are therefore:

- readout 1: true 0-level reference after optical polarization and before the microwave pulse.
- readout 2: signal readout after a modulated Rabi pulse with duration 52 ns and modulation depth 1.

Data assessment:

The reference readout is comparatively flat around 46 to 47 counts across the sweep. The microwave-pulse signal readout has a clear frequency-dependent depression through roughly 3.88 to 3.915 GHz, including its lowest values near 3.895 GHz and 3.915 GHz, while recovering at nearby points. The two per-average traces are noisy but show the same role separation: the signal readout carries the larger frequency-dependent contrast while the reference does not show a matching baseline collapse.

Decision:

This is consistent with a pODMR resonance being present.
