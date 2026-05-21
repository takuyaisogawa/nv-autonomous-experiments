Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From inputs/sequence.xml, full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive even though do_adiabatic_inversion is set. The executed readouts are:

1. Readout 1: true 0-level reference, after adj_polarize and before any microwave pulse.
2. Readout 2: signal readout after rabi_pulse_mod_wait_time with length_rabi_pulse.

The pulse settings used for the active signal branch are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the round(length_rabi_pulse * sample_rate) step leaves the pulse at 13 samples, i.e. 52 ns.

For a pODMR resonance, I expect the post-microwave signal readout to show a reproducible fluorescence decrease relative to the 0-reference at a consistent microwave frequency. The combined signal/reference ratio fluctuates broadly, with isolated low points near several different frequencies and adjacent high points rather than a coherent dip. The per-average overlay also shows noisy point-to-point variation without a stable resonance-shaped feature.

Decision: resonance_absent.
