Sequence review:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse sequence first acquires a true 0-level reference after polarization and detection, then because full_expt = 0 it skips the optional 1-level reference block.
- The measured signal readout is then acquired after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns.
- Readout role interpretation: readout 1 is the pre-pulse 0-level/reference detection, and readout 2 is the post-Rabi-pulse signal detection.

Data assessment:

The combined raw readouts show fluctuations and a stronger negative contrast at the high-frequency edge, but the reference itself is not flat and the per-average traces show large opposing drift between the two averages. When comparing readout 2 to readout 1, the contrast minima are not consistently reproduced at the same scan point across averages. The largest combined reduction occurs at the final scan point, where there is no right-side recovery to establish a resonance line shape. Other depressions are scattered and comparable to the noise/drift structure.

Decision:

I do not see a reliable pODMR resonance in this scan. The data are better described as drift/noise with an edge fluctuation than as a coherent microwave-frequency-dependent dip.
