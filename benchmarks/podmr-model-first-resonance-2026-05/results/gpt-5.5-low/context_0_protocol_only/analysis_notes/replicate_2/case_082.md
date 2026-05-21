Case podmr_068_2026-05-17-075825.

The provided sequence XML is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is
rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at the
250 MHz sample rate to 52 ns. mod_depth = 1. full_expt = 0, so the conditional
1-level reference block is inactive even though do_adiabatic_inversion is true.
The two active detections are therefore the initial post-polarization reference
readout and the readout after the modulated 52 ns microwave pulse.

In the raw data, both readouts fluctuate around about 48 to 51 counts over most
of the scan and both fall together at the highest frequencies. The signal
readout after the Rabi pulse does not show a localized, reproducible dip or
peak relative to the reference readout near a resonance frequency. The largest
feature is a common downward trend near the upper scan edge, visible in both
readout roles and in the per-average overlay, so it is more consistent with
shared drift or readout variation than with pODMR contrast from the microwave
pulse.

Decision: resonance_absent.
