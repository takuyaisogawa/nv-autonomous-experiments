Active sequence: Rabimodulated.xml. The XML sets sample_rate = 250 MHz, full_expt = 0, mod_depth = 1, and length_rabi_pulse = 5.2e-08 s. The pulse length is rounded by the sequence to round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Readout roles from the active instructions:
- The first active detection occurs immediately after adj_polarize and is the true 0-level reference.
- The optional "Acquire 1 level reference" block is skipped because full_expt = 0, despite do_adiabatic_inversion being true.
- The second active detection occurs after rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth = 1, so it is the microwave-pulse signal readout.

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. Comparing the post-pulse signal to the 0-level reference shows a pronounced localized dip near 3.875-3.880 GHz: the signal/reference ratio reaches about 0.837 at 3.875 GHz and 0.833 at 3.880 GHz, with signal minus reference about -6.96 counts at both points. Neighboring points recover by about 3.890 GHz, and the reference channel does not show the same dip. The per-average overlay also supports a real spectral depression in this region rather than a single isolated point.

Decision: a pODMR resonance is present.
