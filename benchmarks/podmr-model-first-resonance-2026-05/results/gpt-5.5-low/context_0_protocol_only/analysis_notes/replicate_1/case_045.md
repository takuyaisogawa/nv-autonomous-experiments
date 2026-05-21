Sequence XML / raw export review:

- Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Pulse structure: polarize, detection for the true 0-level reference, wait, then because full_expt = 0 the optional 1-level reference block is skipped, followed by a rabi_pulse_mod_wait_time pulse and detection.
- Readout roles: readout 1 is the polarized 0-level reference; readout 2 is the post-rabi/modulated pulse signal readout.
- mod_depth: 1 from the applied variable values.
- Pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns, rounded at 250 MS/s but unchanged.

Resonance assessment:

The two combined raw readouts fluctuate by several counts across the scan, but the signal readout does not show a clean localized ODMR feature relative to the reference. The per-average overlay indicates substantial average-to-average offsets and point noise, with the apparent low/high excursions not repeating as a stable spectral feature in both averages or as a consistent contrast feature between the reference and signal. I therefore classify this case as resonance absent.
