Active sequence inspection:

- The saved scan uses Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active variables include mod_depth = 1 and length_rabi_pulse = 52 ns, rounded at the 250 MHz sample rate.
- full_expt = 0, so the conditional 1-level reference branch is skipped.
- The active readout roles are therefore: first detection after optical polarization as the true 0-level/reference readout, then a second detection after the 52 ns modulated Rabi pulse as the microwave-affected readout.

Data assessment:

The two averaged raw readouts stay near 27 counts with substantial point-to-point noise. Per-average traces show strong opposing slow drift between averages, while the combined readouts are comparatively flat and do not show a stable, localized pODMR-like dip across both readout roles. The largest normalized contrast occurs at the final scan point, where readout 1 also jumps upward, making it look like an endpoint/reference fluctuation rather than a resonance feature. There is no consistent resonance-shaped suppression in the microwave-affected readout relative to the reference.

Decision: resonance_absent.
