Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML sets full_expt = 0, so the "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true. The active sequence performs an initial polarization and detection, then waits, applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then performs the final detection. Thus readout 1 is the initial 0-level/reference readout and readout 2 is the post-microwave-pulse readout.

The two raw readouts are noisy, but the post-pulse readout becomes consistently lower than the reference over the high-frequency side of the scan. The relative contrast is most negative around 3.905-3.920 GHz, with a recovery at 3.925 GHz. This looks like a weak pODMR dip rather than only unstructured noise, though the confidence is limited by two averages and substantial point-to-point scatter.

Decision: resonance_present.
