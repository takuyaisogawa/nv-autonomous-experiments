Active sequence and pulse settings:

- The sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave pulse is rabi_pulse_mod_wait_time after the initial reference detection.
- full_expt = 0, so the optional 1-level reference block is skipped. The do_adiabatic_inversion variable is set but the active instructions do not execute an adiabatic inversion.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the applied pulse is 52 ns.

Readout roles:

- Readout 1 is the polarized 0-level/reference readout immediately after adj_polarize.
- Readout 2 is the signal readout after the 52 ns modulated Rabi microwave pulse.

Resonance assessment:

For a pODMR resonance in this sequence, the post-pulse signal readout should show a coherent frequency-dependent contrast relative to the 0-level reference. The combined readout2/readout1 ratio ranges roughly from 0.976 to 1.041, with isolated extrema rather than a stable dip or peak shape. The two averages do not reproduce the same contrast pattern: some apparent features change sign or appear only in one average. The readouts are jagged and comparable to average-to-average noise/drift, so I do not see a reliable pODMR resonance in this scan.
