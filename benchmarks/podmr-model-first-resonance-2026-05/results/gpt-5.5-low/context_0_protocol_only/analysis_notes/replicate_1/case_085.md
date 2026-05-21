Sequence review:

The provided XML and raw export identify the active sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect the true 0-level reference, then wait, then apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detect again. The full_expt variable is 0, so the optional 1-level reference block is not active. Thus readout 1 is the pre-microwave 0-level reference detection and readout 2 is the post-microwave-pulse signal detection.

The XML variable values for this case give length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, and mod_depth = 1. The pulse duration is rounded to the 250 MHz sample rate, which leaves it at the nearest 4 ns grid value; 52 ns is already on that grid.

Data assessment:

Both readouts trend upward across the scan, and the point-to-point differences between readout 2 and readout 1 change sign several times. The ratio r2/r1 has local low points near 3.850, 3.860, 3.890, and 3.905-3.915 GHz, but these are isolated or broad noisy fluctuations rather than a consistent pODMR resonance feature. The per-average overlay shows substantial average-to-average scatter, with thin traces crossing and drifting in ways comparable to the apparent excursions in the combined averages.

Decision:

I do not see a reproducible, localized pODMR resonance in this single-NV sweep. The modulation sequence and 52 ns microwave pulse are active, but the measured readout contrast is dominated by drift and noise rather than a clear resonance response.
