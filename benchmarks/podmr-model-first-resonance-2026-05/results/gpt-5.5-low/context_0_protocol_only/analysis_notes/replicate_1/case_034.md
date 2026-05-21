Sequence XML inspection:

- Active sequence: Rabimodulated.xml / Rabimodulated frequency sweep.
- Swept variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The pulse program first acquires a true 0-level reference with polarization and detection.
- full_expt is 0, so the optional 1-level reference block is not active.
- The active microwave-dependent measurement is a rabi_pulse_mod_wait_time call followed by detection.
- Readout roles: readout 1 is the initial 0-level reference; readout 2 is the post-microwave Rabi-modulated readout.
- mod_depth is 1 in the variable values used for this run.
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns, rounded at the 250 MHz sample rate.

Resonance assessment:

The combined readouts fluctuate over the scan, but the feature is not a clear pODMR resonance. Readout 1 and readout 2 do not show a consistent, localized, reproducible dip or peak with matching behavior across the two averages. The largest changes look comparable to run-to-run noise and baseline variation rather than a resolved resonance contrast. I therefore classify this case as resonance absent.
