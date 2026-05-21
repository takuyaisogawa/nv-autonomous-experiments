Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence uses length_rabi_pulse = 52 ns and mod_depth = 1, with full_expt = 0. Because full_expt is zero, the optional 1-level reference block is inactive. The active readouts are therefore:

- readout 1: detection immediately after optical polarization, serving as the true 0-level/reference readout.
- readout 2: detection after rabi_pulse_mod_wait_time using the swept microwave frequency, serving as the microwave-affected signal readout.

The signal readout shows a pronounced, reproducible dip near 3.875-3.880 GHz, dropping to about 30.3 counts while surrounding signal points are mostly in the mid-to-high 30s. This dip appears in both per-average traces and is not mirrored as a comparable reference dip in readout 1. The feature is frequency-localized and consistent with a pODMR resonance in the microwave-affected readout.

Decision: resonance_present.
