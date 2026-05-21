Active sequence and readout interpretation:

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns. Although do_adiabatic_inversion is true, no adiabatic inversion pulse is executed in the active instruction path. full_expt = 0, so the optional 1-level reference block is skipped.

Readout roles:

Readout 1 is the first detection after adj_polarize, so it is the true 0-level optical reference. Readout 2 is the detection after the 52 ns modulated Rabi pulse, so it is the microwave-affected pODMR signal readout. Since only two detections are active, there is no separate acquired 1-level reference in this run.

Resonance assessment:

The microwave-affected readout does not show a localized, reproducible pODMR dip or peak across the swept frequency range. The combined readout 2 trace rises broadly from the low-frequency side toward the high-frequency side, and the per-average traces show strong average-dependent baseline drift rather than a stable resonant feature at a common frequency. The apparent structure is broad and comparable to readout/reference drift, not a clear single-NV pODMR resonance.

Decision: resonance absent.
