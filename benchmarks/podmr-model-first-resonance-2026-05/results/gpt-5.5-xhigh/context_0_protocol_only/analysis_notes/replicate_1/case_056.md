Case podmr_042_2026-05-16-225623.

Sequence details used before deciding:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- inputs/sequence.xml has full_expt = 0, so the optional "1 level reference" block is inactive.
- The active detection order is: polarize, detection of the true 0-level reference, wait, modulated Rabi pulse, detection of the MW-applied signal, final wait.
- Readout 1 is therefore the post-polarization true 0-level reference with no active MW pulse immediately before detection.
- Readout 2 is the signal after rabi_pulse_mod_wait_time.
- mod_depth = 1 from the provided sequence XML and variable values.
- length_rabi_pulse = 5.2e-08 s; with sample_rate = 250 MHz the rounding step leaves a 52 ns pulse.

Data assessment:
Both raw readouts share a slow downward drift across the scan, so I compared the MW-applied readout against the reference rather than using either trace alone. The combined readout2/readout1 ratio has a localized low point near 3.875 GHz: about 0.960 at 3.875 GHz, compared with about 1.006 at 3.870 GHz, 0.981 at 3.880 GHz, and 1.038 at 3.885 GHz. In both individual averages, readout 2 is below readout 1 at 3.875 GHz, with ratios about 0.951 and 0.968. The feature is noisy and the reference also dips somewhat there, but the MW-applied readout shows an additional localized depression consistent with a pODMR resonance.

Decision: resonance_present.
