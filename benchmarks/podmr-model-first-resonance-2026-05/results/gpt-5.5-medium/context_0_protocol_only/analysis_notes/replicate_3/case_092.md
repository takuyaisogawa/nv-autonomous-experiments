Active sequence:
- Sequence file: Rabimodulated.xml.
- Scan variable: mw_freq, swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Pulse path: polarization, first detection, wait, then a Rabi-modulated microwave pulse, second detection, final wait.

Readout roles:
- Readout 1 is the true 0-level/reference readout acquired immediately after optical polarization.
- The 1-level reference block is inactive because full_expt = 0.
- Readout 2 is the pODMR signal readout acquired after the Rabi-modulated microwave pulse.

Pulse parameters from the provided sequence XML:
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- delay_wrt_1mus = 0.2 us.
- wait_time = 2 us.
- length_last_wait = 1 us.

Decision:
The signal/reference behavior shows a reproducible contrast loss at multiple adjacent microwave frequencies, most clearly around 3.905-3.920 GHz in the combined readouts, with supporting low signal/reference points in the individual averages. The feature is noisy and not a clean symmetric dip, but it is broader than a single-point fluctuation and appears in the expected readout role after the microwave pulse. I therefore classify this case as resonance_present with low confidence.
