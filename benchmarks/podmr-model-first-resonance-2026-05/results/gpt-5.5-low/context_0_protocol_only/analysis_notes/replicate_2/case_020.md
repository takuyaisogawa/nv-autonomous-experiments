Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825e9 to 3.925e9 Hz in 5 MHz steps.

Sequence/readout interpretation:
- The XML sets sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz.
- The instruction flow first polarizes and detects a "true 0 level reference"; this corresponds to readout 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive and contributes no readout.
- The active pODMR measurement then applies rabi_pulse_mod_wait_time with the scanned mw_freq, 52 ns pulse duration, and mod_depth = 1, followed by detection; this corresponds to readout 2.

Data assessment:
Readout 1 stays relatively flat near 37-41 counts across the scan and does not show a matching sharp feature. Readout 2 has a strong localized dip near 3.875-3.880 GHz, falling to about 30.3-30.6 counts from a surrounding baseline around 36-39 counts. The dip is also visible in both individual averages, so it is not just a single-average artifact. Since the resonant feature appears in the MW-dependent post-pulse readout while the reference readout remains comparatively stable, this is consistent with a pODMR resonance being present.
