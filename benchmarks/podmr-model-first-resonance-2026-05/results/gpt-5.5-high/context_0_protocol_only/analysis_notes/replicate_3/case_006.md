Active sequence: Rabimodulated.xml.

The provided sequence XML sweeps mw_freq and uses full_expt = 0, so the active cycle first acquires a true 0-level reference readout after optical polarization, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by the second detection readout. The optional 1-level reference block is inactive because full_expt is zero. The active microwave pulse duration is therefore 52 ns, with full modulation depth.

The combined raw readouts over the mw_freq scan do not show a clear pODMR resonance. The two readout channels fluctuate and cross, and although there is a localized separation near the middle of the sweep, it is narrow and comparable to point-to-point noise and average-to-average drift. The per-average overlays show substantial baseline changes across averages, so the apparent contrast is not a robust resonance-shaped feature in the active post-pulse readout relative to the reference.

Decision: resonance_absent.
