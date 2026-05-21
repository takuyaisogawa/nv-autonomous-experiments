Active sequence: Rabimodulated.xml / rabi_pulse_mod_wait_time while sweeping mw_freq from 3.825 GHz to 3.925 GHz.

Sequence parameters used before deciding:
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The first active detection occurs after adj_polarize and is the true 0-level/reference readout.
- The second active detection occurs after the modulated Rabi microwave pulse and is the signal readout.
- mod_depth = 1 from the provided sequence XML variable values.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- do_adiabatic_inversion is true, but the adiabatic inversion calls are inside comments or the inactive reference block, so they are not part of the active sequence.

Data assessment:
The combined readouts vary only weakly around roughly 48 to 52 counts. The signal readout does not show a coherent, repeatable ODMR-like dip or peak relative to the reference across the microwave sweep. The per-average traces are noisy and the apparent extrema are not consistent between averages. Because the active post-pulse readout lacks a stable frequency-localized contrast feature, I classify this case as resonance absent.
