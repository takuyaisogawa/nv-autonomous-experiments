The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. In the provided sequence XML, readout 1 is the initial detection after polarization and before the microwave pulse, so it is the bright/0-state reference. full_expt is 0, so the optional 1-level reference block is inactive. Readout 2 is the detection after the modulated Rabi pulse.

The pulse used for the swept measurement is length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate to 52 ns. The provided XML and exported variable values indicate mod_depth = 1.

The combined data show readout 2 dropping well below readout 1 around 3.875 to 3.885 GHz: the largest contrasts are about -7.1 counts at 3.875 GHz and -5.9 counts at 3.880 GHz. Away from that region, readout 2 is mostly close to readout 1. The same central suppression appears in both individual averages when comparing readout 2 against readout 1, despite opposing slow baseline drifts in the raw per-average traces.

Decision: a pODMR resonance is present.
