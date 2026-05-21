Active sequence and roles:

The provided XML/raw export identifies the active sequence as Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first performs adj_polarize followed by detection, which is the true 0-level optical reference readout. Because full_expt = 0, the optional 1-level reference block is inactive. The active experimental readout is then produced after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.

Readout interpretation:

readout 1 is the reference detection after optical polarization, without the scanned Rabi pulse immediately before it. readout 2 is the signal detection after the 52 ns modulated microwave pulse. The relevant pODMR signature should therefore appear as a frequency-dependent contrast between the signal readout and the reference, not merely as a shared drift in both channels.

Resonance decision:

Across the scan, both readouts show noisy point-to-point variation and a broad downward drift toward higher microwave frequency. The signal readout is often below the reference, but the separation is not localized into a clear dip or peak at a particular microwave frequency, and the two averages do not show a stable, repeatable narrow resonance feature. The strongest low points occur near the high-frequency edge where the reference also drops, which is more consistent with baseline drift/noise than a distinct pODMR resonance.

Decision: resonance_absent.
