Sequence inspection:

The provided XML defines the active sequence as Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is rabi_pulse_mod_wait_time after the initial reference detection. The XML variables give length_rabi_pulse = 5.2e-08 s, so the pulse duration is 52 ns, and mod_depth = 1. full_expt = 0, so the optional 1-level reference branch is skipped even though do_adiabatic_inversion is true.

Readout roles:

Readout 1 is the first detection after optical polarization and serves as the bright/0-level reference. Readout 2 is the detection after the 52 ns modulated Rabi pulse and is the pODMR signal readout.

Data assessment:

The combined raw readouts show a pronounced contrast at about 3.860 GHz: readout 1 is high while readout 2 is the lowest point in the scan, giving the largest negative signal-reference difference. The per-average traces also support this feature, since both averages show readout 2 lower than readout 1 at that same frequency. Other points are noisy and drift is present, but the 3.860 GHz feature is consistent enough with a microwave-frequency-dependent pODMR response to call a resonance present.
