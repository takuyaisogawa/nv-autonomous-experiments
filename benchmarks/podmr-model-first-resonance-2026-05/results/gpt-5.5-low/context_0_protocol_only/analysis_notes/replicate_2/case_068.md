Active sequence: Rabimodulated.xml / Rabi-modulated pODMR while sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, full_expt is 0, so the optional 1-level reference block is inactive. The executed detections are:
- readout 1: detection immediately after optical polarization, before the microwave pulse, serving as the true 0-level / baseline reference.
- readout 2: detection after the Rabi-modulated microwave pulse, serving as the pODMR signal readout.

The microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so the pulse duration is 52 ns. The provided sequence XML sets mod_depth = 1.

The combined raw readouts do not show a clear resonance feature. Readout 2 relative to readout 1 fluctuates above and below baseline at isolated scan points, but the extrema are not organized into a consistent frequency-localized dip or peak. The per-average overlay shows substantial average-to-average drift and opposing trends, which can explain the apparent point-to-point variations in the combined traces. Because the signal readout lacks a reproducible ODMR contrast feature over the sweep, I classify this case as resonance absent.
