Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence sets sample_rate to 250 MHz, enables channels [1 1 1 0 0 0], and uses set_microwave with mw_freq plus detuning. full_expt is 0, so the optional 1-level reference block is inactive. The two active detection events are therefore:

1. A true 0-level reference after adj_polarize.
2. The signal readout after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns.

Thus readout 1 is the polarized reference readout, and readout 2 is the microwave-pulse-affected readout. The signal readout has a pronounced local minimum at 3.895 GHz: readout 2 is about 49.81 while readout 1 is about 52.58, giving the lowest signal/reference ratio in the scan, about 0.947. The neighboring signal points recover strongly at 3.900 GHz and beyond. The per-average traces also show this point as a local depression in readout 2, so it is not solely produced by a single combined-average artifact.

Decision: a pODMR resonance is present, centered approximately near 3.895 GHz in this scan.
