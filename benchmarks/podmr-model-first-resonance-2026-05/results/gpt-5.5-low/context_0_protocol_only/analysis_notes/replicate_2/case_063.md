Sequence inspection:

The active sequence is Rabimodulated.xml, sweeping mw_freq across 3.825e9 to 3.925e9 Hz with 21 points. The sequence first performs adj_polarize and detection to acquire the true 0-level reference. The optional 1-level reference block is disabled because full_expt = 0, even though do_adiabatic_inversion is true. The active signal operation is rabi_pulse_mod_wait_time followed by detection. The pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to the same 52 ns duration. The active modulation depth is mod_depth = 1. The final wait is 1 us.

Readout interpretation:

Readout 1 is the reference fluorescence after polarization/detection without the microwave pulse. Readout 2 is the fluorescence after the 52 ns rabi-modulated microwave pulse. A pODMR resonance should appear as a reproducible frequency-localized contrast feature in the signal readout relative to the reference, not merely as broad drift or average-to-average offset.

Data assessment:

The combined traces are noisy and show broad variations over the scan. Readout 2 is not marked by a stable, localized dip or peak relative to readout 1. The difference between signal and reference changes sign several times, with a positive excursion near the upper-middle of the scan but no consistent resonance-shaped feature. The per-average overlay shows large average-to-average offsets and fluctuations, so the apparent features in the combined traces are not robust enough to identify a pODMR resonance.

Decision:

Resonance absent.
