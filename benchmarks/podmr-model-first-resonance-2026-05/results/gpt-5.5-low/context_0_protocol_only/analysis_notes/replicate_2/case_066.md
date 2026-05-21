Active sequence and roles:

- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active variables in the raw export give length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, and mod_depth = 1.
- full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true.
- The executed detections are therefore: first, a true 0-level/pre-pulse reference readout after polarization; second, the signal readout after the 52 ns rabi_pulse_mod_wait_time microwave pulse.

Resonance assessment:

The two averaged readout traces are noisy and drift with frequency. The post-pulse signal readout does not show a localized, reproducible ODMR-like dip or peak relative to the pre-pulse reference near a single frequency. The per-average overlay shows strong opposite baseline drift between the two averages, indicating that much of the apparent structure is average-to-average drift rather than a stable spectral feature. There is no coherent resonance signature that persists across readout roles and averages.

Decision: resonance_absent.
