Active sequence: Rabimodulated.xml / Rabimodulated frequency scan.

From the provided sequence XML, the experiment first polarizes the NV and takes a detection readout before any Rabi pulse. Because full_expt is 0, the optional 1-level reference block is skipped. The active microwave operation is then rabi_pulse_mod_wait_time followed by the second detection. Therefore readout 1 is the 0-level reference, and readout 2 is the post-pulse signal readout.

The XML gives mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded active pulse duration remains 52 ns.

I compared the post-pulse readout against the 0-reference over the mw_freq sweep. The combined readout 2 / readout 1 ratio shows its strongest depressions near 3.855 GHz and 3.895 GHz, with ratios about 0.887 and 0.910 respectively. These same two frequencies are below the reference in both individual averages, so they are more consistent with real pODMR contrast than with a single-average excursion. The trace is noisy and sparse, but the repeated post-pulse depressions support a resonance-present decision.
