Case podmr_026_2026-05-16-182622.

The provided sequence XML is Rabimodulated.xml with mw_freq as the swept variable. The active instructions first acquire a true 0-level optical reference using adj_polarize followed by detection, then skip the optional 1-level reference block because full_expt is 0, then apply a rabi_pulse_mod_wait_time pulse and acquire the second detection readout. Thus readout 1 is the reference/background readout and readout 2 is the post-microwave-pulse signal readout.

From the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 5.2e-08 s, rounded at the 250 MHz sample rate, i.e. 52 ns. The scan spans 3.825 to 3.925 GHz in 5 MHz steps with two averages.

The raw traces fluctuate at roughly the same scale as any possible contrast. The post-pulse readout does not show a consistent, localized pODMR dip or peak relative to the reference across the sweep, and the per-average traces show that the larger excursions are not reproducible between averages. There is no clear resonance feature supported by the combined readouts.

Decision: resonance absent.
