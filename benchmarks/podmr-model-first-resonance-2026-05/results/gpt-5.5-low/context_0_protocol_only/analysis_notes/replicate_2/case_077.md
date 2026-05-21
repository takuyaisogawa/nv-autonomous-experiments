Active sequence review:

The provided XML and the embedded sequence in raw_export.json identify the active sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse before the signal detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 in the variable values for this run. full_expt = 0, so the optional 1-level reference block is skipped. The two active readout roles are therefore the initial polarized/dark-reference-style detection after adj_polarize, followed by the detection after the 52 ns modulated Rabi pulse.

Resonance assessment:

Both raw readouts show a broad downward drift toward higher microwave frequency. The second readout does not show a stable, localized pODMR resonance feature relative to the first readout. The signal-reference difference and ratio fluctuate point-to-point, with alternating signs and isolated excursions near 3.84, 3.85, 3.86, 3.87, 3.88, and 3.905 GHz rather than a coherent resonance-shaped dip or peak. The per-average traces also show comparable scatter, so the apparent variations are not convincing as a reproducible resonance.

Decision: resonance_absent.
