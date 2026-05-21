Sequence review:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive.
- Readout 1 is the true 0-level/reference detection after polarization and before the microwave pulse.
- Readout 2 is the signal detection after the active rabi_pulse_mod_wait_time microwave pulse.
- Active microwave pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, i.e. 52 ns.
- mod_depth is 1, so the active pulse is fully modulated.

Data assessment:

The relevant contrast is readout 2 relative to readout 1, since readout 1 is the pre-pulse reference and readout 2 follows the microwave pulse. The combined trace shows a clear negative contrast at 3.845 GHz: readout 1 is 48.231 and readout 2 is 43.942, giving readout2/readout1 = 0.911 and readout2-readout1 = -4.288. This same point is negative in both individual averages, with differences of -3.808 and -4.769, so it is not just cancellation from one average. Neighboring points at 3.850 to 3.860 GHz are also mostly depressed relative to the surrounding baseline, though noisier.

Decision:

A pODMR resonance is present. The evidence is a coherent microwave-frequency-dependent fluorescence dip in the post-pulse readout relative to the reference readout, centered near 3.845 GHz.
