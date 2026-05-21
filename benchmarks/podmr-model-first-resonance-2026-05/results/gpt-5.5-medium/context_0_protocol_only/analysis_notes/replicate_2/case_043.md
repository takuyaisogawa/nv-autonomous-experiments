Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Relevant XML settings: length_rabi_pulse = 5.2e-08 s, which is 52 ns and exactly 13 samples at the 250 MHz sample rate after rounding. mod_depth = 1. full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is set. The active detections are therefore the initial polarized reference readout before the microwave pulse and the signal readout after the modulated rabi pulse.

The combined raw readouts and per-average overlay do not show a convincing pODMR resonance. There are point-to-point fluctuations, including an isolated readout difference around 3.855 GHz, but the feature is not a clear, reproducible resonance-shaped dip or peak across the scan. The two readouts often share common-mode variation, and the differential/ratio signal has excursions comparable to the two-average scatter rather than a stable frequency-localized contrast response.

Decision: resonance_absent.
