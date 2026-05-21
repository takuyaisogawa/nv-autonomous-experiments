Active sequence: Rabimodulated pODMR, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The XML program first polarizes and detects immediately, so readout 1 is the true 0-level/reference fluorescence before the microwave manipulation.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The active signal readout is readout 2, taken after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- The exported variable values indicate mod_depth = 1 for this run.

Resonance assessment:
Readout 1 stays comparatively flat around the low-to-mid 40s across the scan, while readout 2 has a strong, localized fluorescence dip centered near 3.875-3.880 GHz, falling from about 42-45 counts to about 34 counts. The same dip is visible in both averages, so it is not just a single-average artifact. Because the signal readout drops selectively while the reference readout does not show a matching dip, this is consistent with a pODMR resonance.
