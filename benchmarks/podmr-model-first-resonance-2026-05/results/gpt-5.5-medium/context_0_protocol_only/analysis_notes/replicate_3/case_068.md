Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence uses sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1. The pulse duration rounds exactly to 52 ns at this sample rate. full_expt = 0 disables the optional 1-level reference block, so the active readout roles are:

- readout 1: reference detection after polarization, before the microwave pulse
- readout 2: signal detection after the modulated Rabi microwave pulse

For a pODMR resonance I would expect a frequency-localized and reproducible contrast feature in the signal readout relative to the reference, normally a dip or peak that stands out against point-to-point noise and is reasonably consistent across averages. Here the two averaged traces fluctuate by about the same scale as their apparent differences, and the per-average overlay shows strong average-to-average drift rather than a stable frequency-localized feature. The signal/reference contrast changes sign at multiple adjacent points and does not form a convincing resonance over the scanned 100 MHz window.

Decision: resonance_absent.
