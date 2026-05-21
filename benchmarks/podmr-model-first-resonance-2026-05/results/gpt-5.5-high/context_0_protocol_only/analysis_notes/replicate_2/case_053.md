Sequence inspection:
- Active sequence file/name is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation is rabi_pulse_mod_wait_time after the initial polarization/reference detection.
- full_expt is 0, so the optional 1-level reference block is skipped.
- Readout 1 is the initial true 0-level reference detection after adj_polarize and before the microwave pulse.
- Readout 2 is the signal detection after the modulated Rabi microwave pulse.
- mod_depth from the provided sequence XML/variable values is 1.
- length_rabi_pulse is 52 ns; at 250 MS/s this rounds to 13 samples, still 52 ns.

Resonance decision:
The post-pulse signal readout has some low points, especially near the high-frequency end, but the per-average traces show substantial scatter and the depression is not consistently reproduced across averages. Readout 1 also has comparable frequency-dependent fluctuations, including its own low point near 3.89 GHz. The signal-reference contrast does not form a clean, reproducible pODMR dip over the scan; the apparent features look noise-dominated rather than a clear resonance.
