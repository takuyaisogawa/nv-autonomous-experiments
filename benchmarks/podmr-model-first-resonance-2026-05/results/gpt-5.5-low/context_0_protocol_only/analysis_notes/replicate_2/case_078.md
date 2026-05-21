Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The executed XML has full_expt = 0, so the optional 1-level reference block is skipped. The two active detections are therefore:
- readout 1: initial post-polarization true 0-level reference detection before the microwave/Rabi pulse.
- readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns.

The pulse uses mod_depth = 1 in the provided sequence variable values and length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

The raw traces fluctuate around about 50 to 52 counts. The readout2-minus-readout1 contrast changes sign repeatedly and does not form a coherent ODMR dip or line shape. The largest feature is a positive readout2 spike near 3.915 GHz rather than a consistent loss of fluorescence at resonance; nearby points do not support a resolved resonance. Per-average overlays show substantial scatter, so isolated excursions are not reliable evidence.

Decision: resonance absent.
