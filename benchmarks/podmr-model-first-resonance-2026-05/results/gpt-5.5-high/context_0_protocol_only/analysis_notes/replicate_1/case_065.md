Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz.

The provided sequence uses adj_polarize followed by detection as the first active readout, giving a true 0-level / bright-state reference. The full_expt variable is 0, so the optional 1-level reference block is skipped. The second active readout occurs after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, so readout 2 is the frequency-dependent post-microwave signal.

Because the reference readout is not expected to contain the resonance, I focused on the post-pulse signal relative to the reference rather than on the plotted labels alone. The combined data are noisy, but the strongest signal loss relative to reference occurs at about 3.895 GHz: readout 1 is about 50.0 while readout 2 is about 45.38, a roughly -9% contrast. This feature is also present in both individual averages for the signal channel, so it is not solely from one average. There are other noisy point-to-point fluctuations and the feature is narrow with limited sampling, but the readout-role-aware contrast supports a weak pODMR resonance.

Decision: resonance_present.
