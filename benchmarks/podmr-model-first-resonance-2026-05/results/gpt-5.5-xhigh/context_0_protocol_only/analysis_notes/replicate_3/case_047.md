Sequence XML review:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true. The executed timing is therefore:

1. Polarize and detect a true 0-level reference.
2. Wait for AWG.
3. Apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
4. Detect the post-pulse signal.
5. Wait length_last_wait.

The readout roles are readout 1 as the no-MW/bright reference after polarization, and readout 2 as the measurement after the active microwave pulse. The active pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The modulation depth is mod_depth = 1.

Data assessment:

For a pODMR resonance in this sequence, the post-pulse readout should show a coherent contrast feature relative to the first reference readout, typically a dip in readout 2 versus readout 1 around the resonant microwave frequency. The combined readout-2 minus readout-1 values fluctuate around zero and are often positive. The negative excursions are isolated rather than forming a stable line shape, and the two individual averages do not show the same negative feature at the same scan positions. The large positive excursion near 3.915 GHz is also not a resonance-like dip.

Decision:

No reliable pODMR resonance is present in this scan.
