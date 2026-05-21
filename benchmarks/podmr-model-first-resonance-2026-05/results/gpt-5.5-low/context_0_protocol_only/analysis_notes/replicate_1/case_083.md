Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The executed readout roles are therefore:
  - first detection after optical polarization: true 0-level/reference readout before the microwave pulse;
  - second detection after rabi_pulse_mod_wait_time: microwave-affected signal readout.
- mod_depth is 1 from the exported variable values.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MS/s to 52 ns.

Data assessment:

The combined raw readouts and the signal/reference ratio show substantial point-to-point scatter. There is a large isolated signal drop around 3.845 GHz, and another smaller depression near 3.91 GHz, but neither forms a stable, multi-point ODMR-like feature across the scan. The per-average overlay also shows the individual averages are offset and noisy rather than repeating a consistent resonance shape. Since the apparent dips are isolated and comparable to average-to-average fluctuations, I do not identify a reliable pODMR resonance in this measurement.
