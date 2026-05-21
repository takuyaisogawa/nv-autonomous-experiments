Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz. The XML sets full_expt = 0, so the optional 1-level reference block is inactive despite do_adiabatic_inversion being true. The active detections are therefore: readout 1 after adj_polarize only, serving as the true 0-level / laser-only reference; readout 2 after rabi_pulse_mod_wait_time followed by detection, serving as the microwave-pulse-affected pODMR signal.

Relevant pulse parameters from the provided sequence are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), with switch_delay = 100 ns.

The microwave-affected readout shows a clear, localized fluorescence dip near the center of the scan, dropping from roughly 38-39 counts to about 29-32 counts around 3.875-3.880 GHz. The reference readout does not show a comparable centered dip and remains mostly near 37-40 counts with ordinary scatter. The per-average overlay shows the same dip in readout 2 for both averages, indicating the feature is reproducible rather than a single-average fluctuation.

Decision: pODMR resonance present.
