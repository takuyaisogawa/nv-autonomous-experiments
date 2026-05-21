Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional 1-level reference block is inactive. The active readouts are:

1. A reference/bright-state readout immediately after adj_polarize, before the microwave pulse.
2. A signal readout after rabi_pulse_mod_wait_time.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns. The provided sequence XML sets mod_depth = 1 for this pulse.

The combined traces do not show a clear, frequency-localized pODMR resonance. Readout 2 is sometimes below readout 1, but the differences are scattered across the sweep rather than forming a stable dip. The per-average overlay also shows large point-to-point fluctuations and no reproducible resonance feature at the same scan value. The higher-frequency end has a couple of lower signal points, but this is not enough to identify a resonance because similar or larger deviations occur elsewhere and the feature is not well isolated.

Decision: resonance_absent.
