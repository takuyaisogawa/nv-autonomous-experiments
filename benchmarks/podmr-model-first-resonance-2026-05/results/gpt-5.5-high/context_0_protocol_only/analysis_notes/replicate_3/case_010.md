Sequence review:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, length_rabi_pulse is 5.2e-08 s and is rounded at the 250 MHz sample rate to 13 samples, so the active pulse duration remains 52 ns. mod_depth is 1. full_expt is 0, so the optional "Acquire 1 level reference" block is not executed even though do_adiabatic_inversion is true.

Readout roles:

The first detection occurs immediately after adj_polarize and is the true 0-level / polarized reference readout. The second active detection occurs after rabi_pulse_mod_wait_time with the 52 ns modulated Rabi pulse and is the pODMR signal readout. There is no active third readout for a 1-level reference in this run.

Resonance decision:

The combined raw readouts and the signal/reference contrast fluctuate point-to-point across the sweep. There are isolated contrast excursions, but they do not form a consistent, reproducible resonance-shaped feature over neighboring frequency points. The per-average overlay mainly shows opposing drift/trend behavior between the two averages rather than a stable frequency-localized ODMR response. Therefore I classify this case as resonance_absent.
