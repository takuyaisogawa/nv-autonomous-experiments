The active sequence is Rabimodulated.xml. The standalone sequence XML sets sample_rate to 250 MHz, length_rabi_pulse to 5.2e-08 s (52 ns), mod_depth to 1, full_expt to 0, and do_adiabatic_inversion to true, but the adiabatic/1-level-reference branch is inactive because full_expt is 0.

Instruction flow:
- adj_polarize followed by detection gives the first readout. This is the polarized 0-state/bright reference and should not itself encode the microwave-frequency resonance.
- The inactive full_expt block means there is no separate 1-level reference acquired.
- rabi_pulse_mod_wait_time then applies the 52 ns modulated microwave pulse at the swept mw_freq with mod_depth 1.
- A second detection follows; this is the signal readout after the microwave pulse.

The scan sweeps mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The combined post-pulse readout is depressed relative to the polarized reference around the middle of the sweep, with the strongest contrast at 3.875 GHz: readout 1 is about 42.12 while readout 2 is about 38.25, giving roughly -9.2% normalized contrast. Neighboring points at 3.870 GHz are also negative, and the per-average traces show the post-pulse readout falling below the first readout in the same central region. There is drift and noise in the raw readouts, including some edge fluctuations, but the central frequency-localized negative contrast is consistent with microwave-driven spin contrast from a pODMR resonance.

Decision: resonance_present.
