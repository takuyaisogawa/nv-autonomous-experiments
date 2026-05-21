The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt is 0, so the intermediate 1-level reference block is inactive. The active detections are therefore:

- readout 1: polarized true-0 reference detection after adj_polarize.
- readout 2: signal detection after rabi_pulse_mod_wait_time.

The active pulse before readout 2 uses length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns. The provided sequence XML sets mod_depth = 1 for this pulse.

For the combined readouts, the signal/reference ratio averages about 1.007 across the sweep, with a minimum near 0.956 at the low-frequency edge and a maximum near 1.062. The signal trace does not show a reproducible ODMR-like fluorescence dip relative to the reference. The two per-average overlays also put their strongest negative contrasts at different frequencies rather than at a common resonance. The raw traces mostly show point-to-point scatter and slow drift, not a stable resonant feature.

Decision: resonance absent.
