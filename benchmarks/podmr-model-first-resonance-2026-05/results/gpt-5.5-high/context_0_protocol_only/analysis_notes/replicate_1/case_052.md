The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. The active experiment has full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true. The two active detections are therefore the polarized bright/0 reference readout first, followed by a detection after one rabi_pulse_mod_wait_time call.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this is exactly 13 samples, so the effective pulse duration remains 52 ns. The active mod_depth value from the provided XML and variable values is 1.

For pODMR, a resonance should appear as a frequency-localized change in the post-pulse readout relative to the reference readout. The combined traces fluctuate around 44-49 counts and the normalized contrast (readout1 - readout2) / readout1 has a mean near 0.007 with scatter around 0.025. The apparent excursions are not coherent: one average has positive contrast near 3.83 and 3.85 GHz while the other has its largest positive point near 3.845 GHz and strong negative excursions near 3.88 and 3.905 GHz. The combined dip/peak structure is therefore dominated by noise and average-to-average drift rather than a stable ODMR resonance.

Decision: resonance_absent.
