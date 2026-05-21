Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence sets full_expt = 0, so the active acquisition is a true 0-level reference detection after laser polarization, followed by one modulated Rabi pulse and a second detection. The conditional 1-level reference block is inactive. Thus readout 1 is the reference/0-level fluorescence channel and readout 2 is the signal after the microwave pulse.

Sequence parameters used for interpretation:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mod_depth = 1 in the provided sequence XML.
- mw_freq is the swept variable; detuning is 0.

The combined raw readouts show readout 2 dropping strongly around 3.875-3.880 GHz, reaching about 26-27 counts while neighboring points are mostly in the mid-30s. Readout 1 stays comparatively flat in the same region and does not show a matching drop. The per-average overlay shows the same readout-2 depression in both averages, so the feature is repeatable rather than a single-average outlier.

Decision: resonance_present. The frequency-localized fluorescence decrease appears in the microwave-pulse readout relative to the reference readout, which is consistent with a pODMR resonance.
