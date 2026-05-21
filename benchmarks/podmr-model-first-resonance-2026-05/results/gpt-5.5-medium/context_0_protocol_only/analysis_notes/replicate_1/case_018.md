Sequence inspection:

- The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse path has full_expt = 0, so the optional 1-level reference block is skipped.
- Readout 1 is the initial detection after optical polarization, serving as the true 0-level/no-microwave reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1.
- The sequence therefore supports comparing a reference-like readout against the microwave-modulated pODMR readout.

Data assessment:

The reference readout stays roughly flat in the mid/high 30-count range without a matching central dip. The microwave-modulated readout has a pronounced localized decrease from about 33.4 at 3.870 GHz to 29.3 at 3.875 GHz and 28.1 at 3.880 GHz, recovering by about 3.890-3.895 GHz. This feature is present in both averages in the per-average data and is much larger than the typical point-to-point fluctuations elsewhere. The final point also trends low, but the central feature is the clearest resonance-like contrast and is consistent with pODMR response in the active microwave readout.

Decision: resonance_present.
