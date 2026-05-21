Case podmr_032_2026-05-14-161051.

The provided sequence XML is Rabimodulated-style pODMR with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect a true 0-level reference, then wait. The optional 1-level reference block is inactive because full_expt = 0. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by the second detection. Thus readout 1 is the reference before the microwave pulse, and readout 2 is the microwave-pulse measurement readout.

The combined raw traces show a localized reduction in readout 2 relative to readout 1 around 3.875-3.880 GHz. The strongest point is at 3.880 GHz, where readout 1 is about 35.65 and readout 2 is about 29.31, giving a difference of about -6.35 and a ratio near 0.82. Neighboring points around 3.870-3.875 GHz are also below the reference. The per-average data have substantial baseline drift in opposite directions, but both averages still show negative readout2-minus-readout1 contrast in the 3.870-3.880 GHz region.

Decision: a pODMR resonance is present. The feature is not perfectly clean because of drift and noise, but the reference-normalized dip near 3.88 GHz is sufficiently localized and consistent with the active readout roles.
