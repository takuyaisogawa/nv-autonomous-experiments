Sequence interpretation:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive.
- Readout 1 is the optical 0-level reference acquired after polarization and before the microwave pulse.
- Readout 2 is the signal readout acquired after a rabi_pulse_mod_wait_time microwave pulse.
- mod_depth is 1 in the provided sequence XML.
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns.

Resonance decision:
The signal readout does not show a clean, reproducible ODMR-like dip relative to the reference across the scan. There are isolated downward points, especially near 3.845 GHz and 3.910 GHz, but the per-average overlay indicates that these features are not consistently repeated between averages and are comparable to readout scatter. The expected pODMR signature would be a coherent frequency-localized contrast feature in the post-pulse signal relative to the reference; this trace is too noisy and irregular for a reliable resonance call.

Decision: resonance_absent.
