Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The sequence first performs adj_polarize and detection, giving the true 0-level reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s (52 ns), mod_depth = 1, and switch_delay = 1e-07 s, followed by detection.
- Therefore readout 1 is the polarized reference and readout 2 is the MW-pulsed pODMR signal.

Data assessment:
Readout 1 stays relatively flat around 41-43 counts over the scan, while readout 2 shows a deep, localized dip from about 3.870 GHz to 3.885 GHz, reaching roughly 33 counts near 3.880 GHz. The dip appears in both averages in the per-average overlay and is not mirrored by the reference readout. This is the expected signature of a pODMR resonance in the signal channel.

Decision: resonance_present.
