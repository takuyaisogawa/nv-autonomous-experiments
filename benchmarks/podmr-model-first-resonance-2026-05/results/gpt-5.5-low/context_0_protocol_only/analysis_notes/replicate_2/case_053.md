Active sequence assessment:

The sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. The exported variable table gives mod_depth = 1. full_expt = 0, so the optional 1-level reference branch is not executed.

Readout roles:

The first active detection occurs immediately after optical polarization and before the microwave pulse, so readout 1 is the 0-level/reference readout. The second active detection occurs after the modulated Rabi microwave pulse, so readout 2 is the pODMR signal readout.

Resonance decision:

The raw readouts are noisy with only two averages, but readout 2 develops a sustained negative contrast relative to readout 1 at the high-frequency end of the sweep. From about 3.910 GHz through 3.925 GHz, the signal readout remains lower than the reference while the reference is comparatively flat near 49 counts. This looks like a resonance dip partly captured at the upper edge of the scan rather than an isolated single-point fluctuation. There are other noisy excursions earlier in the sweep, but the high-frequency downturn is the most frequency-coherent feature.

Decision: resonance_present.
