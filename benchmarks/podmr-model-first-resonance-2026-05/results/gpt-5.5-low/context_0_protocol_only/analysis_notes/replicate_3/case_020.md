Active sequence and roles:

The saved scan uses Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence first performs adj_polarize and detection to acquire the true 0-level reference readout, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the signal detection. The optional 1-level reference block is skipped because full_expt is 0.

Relevant pulse settings:

- length_rabi_pulse: 52 ns
- mod_depth: 1 from Variable_values for this run
- sample_rate: 250 MHz, so the 52 ns pulse is rounded to the sampling grid in the instructions
- mw_freq is the scanned variable

Readout interpretation:

Readout 1 is the reference taken before the Rabi-modulated microwave pulse. Readout 2 is the post-pulse signal readout. A pODMR resonance should primarily appear as a frequency-dependent contrast feature in readout 2 relative to the reference, not merely as common-mode drift.

Decision:

Readout 2 shows a strong, localized fluorescence dip around 3.875-3.880 GHz, dropping from the surrounding high-30s counts to about 30.3-30.6 counts. This dip is visible in both averages and is not mirrored as a comparable dip in the reference readout. The feature is therefore consistent with a pODMR resonance being present.
