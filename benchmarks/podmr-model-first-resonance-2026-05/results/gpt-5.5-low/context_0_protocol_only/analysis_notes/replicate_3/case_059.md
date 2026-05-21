Sequence inspection:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The two acquired readout roles are therefore:
  - readout 1: detection after optical polarization, serving as the true 0-level/reference readout.
  - readout 2: detection after the active modulated Rabi microwave pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- mod_depth = 1 in the provided XML/variable values.

Data assessment:

The combined readouts fluctuate around roughly 48 to 50 counts over the scan. The post-pulse readout does not show a clear, localized, reproducible ODMR-like dip or peak relative to the reference readout. The largest normalized deviations occur near the high-frequency endpoint, but this coincides with a drop in readout 1 and an endpoint trend rather than a resolved resonance feature. The per-average overlay also shows substantial scatter and does not support a consistent resonance signature at a single frequency.

Decision: resonance_absent.
