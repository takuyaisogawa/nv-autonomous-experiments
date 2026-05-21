Sequence context:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825e9 to 3.925e9 Hz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is skipped.
- Readout 1 is the initial post-polarization 0-level/reference detection.
- Readout 2 is the signal detection after the active rabi_pulse_mod_wait_time pulse.
- mod_depth is 1 from the active variable values.
- The active pulse duration is length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, already aligned to the 250 MHz sample clock.

Data assessment:

Readout 1 remains comparatively flat around the mid-30s over the sweep. Readout 2 has a pronounced dip centered around 3.875e9 to 3.880e9 Hz, dropping to about 29 and 28 counts, with the same feature visible in both per-average traces. Because the dip appears in the signal readout after the microwave pulse and not as a corresponding reference fluctuation, this is consistent with a pODMR resonance.
