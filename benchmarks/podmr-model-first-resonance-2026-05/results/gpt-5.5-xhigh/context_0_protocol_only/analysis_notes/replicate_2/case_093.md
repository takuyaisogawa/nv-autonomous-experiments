Sequence XML review:

The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true. The active readouts are therefore:

1. Readout 1: true 0-level reference after polarization and detection, with no microwave pulse immediately before detection.
2. Readout 2: signal readout after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, followed by detection.

The pulse parameters used for the active signal readout are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, i.e. 52 ns.

Data assessment:

The combined signal readout does not show a stable, frequency-localized ODMR dip or peak relative to the reference. The signal/reference contrast changes sign repeatedly across the scan, with local extrema at several separated frequencies. Some apparent contrast dips are caused by high reference points rather than a corresponding coherent signal suppression. The two per-average traces also differ substantially in baseline and do not support a reproducible resonance feature at a single frequency.

Decision: resonance absent.
