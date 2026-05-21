Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML/inlined sequence has full_expt = 0, so the optional 1-level reference block is inactive. The executed readouts are:
- readout 1: after adj_polarize and detection, before the microwave/Rabi pulse; this is the polarized no-pulse reference.
- readout 2: after rabi_pulse_mod_wait_time and detection; this is the microwave-affected pODMR signal.

Pulse settings used for the active microwave pulse:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mod_depth = 1.
- mw_ampl = -5 dBm, ampIQ = 5 dBm, freqIQ = 50 MHz.

The relevant resonance test is whether readout 2 shows a frequency-localized drop relative to readout 1. It does: readout 2 falls sharply around 3.870-3.875 GHz, reaching about 31.2 at 3.875 GHz while readout 1 remains about 40.9 there. Both averages show a corresponding dip in the microwave-affected readout, with recovery at higher frequency. The feature is localized and much larger than the point-to-point noise or the slower baseline drift visible in the reference.

Decision: pODMR resonance is present.
