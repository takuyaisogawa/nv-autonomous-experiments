Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the optional 1-level reference branch is inactive despite do_adiabatic_inversion being true. The active detections are the initial post-polarization detection, serving as the bright/0 reference readout, and the detection after rabi_pulse_mod_wait_time, serving as the microwave-modulated signal readout.

Pulse settings used for the active microwave pulse: length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns; mod_depth = 1; switch_delay = 100 ns; mw_ampl = -5 dBm; ampIQ = 5 dBm; freqIQ = 50 MHz.

The combined readouts do not show a clean localized ODMR-like dip or peak that is repeatable across averages. Readout 2 trends upward through much of the sweep and crosses readout 1 near the high-frequency side, but the per-average overlays show large slow drifts in opposite directions between averages. The apparent contrast structure is therefore dominated by drift/average mismatch rather than a stable resonance feature tied to the frequency sweep.

Decision: resonance_absent.
