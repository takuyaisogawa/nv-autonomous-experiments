Sequence inspection:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is not active.
- The executed sequence first polarizes and detects the true 0-level reference, then applies rabi_pulse_mod_wait_time and detects the signal.
- Readout 1 is therefore the pre-microwave polarized reference detection.
- Readout 2 is the detection after the modulated Rabi microwave pulse.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MHz sample rate, i.e. 52 ns.
- mod_depth is 1 in the variable values used for this run.

Data assessment:
Readout 1 stays comparatively flat around 42-46 counts across the scan. Readout 2 shows a pronounced, localized reduction near 3.875-3.880 GHz, dropping to about 34 counts while neighboring points recover toward the low-to-mid 40s. The dip is visible in the combined readout and in both per-average overlays, and it occurs only in the microwave-affected signal readout rather than the initial reference.

Decision:
This is consistent with a pODMR resonance being present.
