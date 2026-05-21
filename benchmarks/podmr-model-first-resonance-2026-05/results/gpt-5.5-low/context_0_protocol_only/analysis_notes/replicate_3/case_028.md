Active pulse sequence: Rabimodulated.xml / Rabimodulated sequence, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from inputs/sequence.xml:
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive.
- The active acquisition first does adj_polarize, then detection, then wait_for_awg. This first detection is the true 0 level reference and corresponds to readout 1.
- The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s (52 ns), mod_depth = 1, and switch_delay = 1e-07 s, followed by detection. This second detection corresponds to readout 2, the microwave-pulse-dependent signal.

Data assessment:
Readout 1 stays relatively flat near the low-to-mid 40s across the scan, while readout 2 shows a pronounced, localized drop from about 42-45 down to about 34 around 3.875-3.880 GHz, then recovers. The dip is visible in both per-average traces, although the baseline differs between averages. Because the reference readout does not show the same feature and the post-pulse readout has a clear frequency-localized contrast dip, this is consistent with a pODMR resonance.
