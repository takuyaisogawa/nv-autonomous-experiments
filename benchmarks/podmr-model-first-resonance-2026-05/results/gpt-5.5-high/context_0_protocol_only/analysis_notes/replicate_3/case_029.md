Active pulse sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML variables set length_rabi_pulse to 5.2e-08 s, which remains 52 ns after rounding at the 250 MHz sample rate. The XML sets mod_depth to 1. The full_expt variable is 0, so the optional 1-level reference branch is skipped even though do_adiabatic_inversion is true.

Readout roles from the active instructions:
- readout 1: after adj_polarize, before the microwave test pulse; this is the true 0-level/reference readout.
- readout 2: after rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth, so this is the microwave-dependent signal readout.

The scan shows readout 2 dropping sharply around 3.875 to 3.880 GHz, reaching about 39 counts, while readout 1 remains in its usual mid-to-high 40 count range without a matching dip. The same readout-2 depression is visible in both per-average traces, so it is not just a single-average fluctuation. Because the signal readout has a localized microwave-frequency-dependent contrast feature while the reference readout does not, this is consistent with a pODMR resonance.
