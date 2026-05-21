Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence uses a polarize/detect block first, then a modulated Rabi pulse followed by detection. Because full_expt = 0, the intermediate "Acquire 1 level reference" block is inactive. Therefore readout 1 is the true 0-level/polarized reference, and readout 2 is the signal after the modulated Rabi pulse.

Relevant pulse settings from the XML/export values: length_rabi_pulse = 5.2e-08 s (52 ns), mod_depth = 1, sample_rate = 250 MHz, and the pulse duration is already an integer 13 samples after rounding.

The reference readout remains relatively flat, roughly 40.2 to 42.5 counts. The post-pulse readout shows a strong, localized dip centered around 3.875-3.880 GHz, falling to about 32 counts while nearby off-resonance values are around 39-42 counts. The dip is visible in both averages and is specific to the post-pulse readout, consistent with a pODMR resonance.
