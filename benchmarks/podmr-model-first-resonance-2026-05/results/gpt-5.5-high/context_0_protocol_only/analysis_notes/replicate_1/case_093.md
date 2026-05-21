Sequence XML review:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse path: after initialization and the first detection, the conditional 1-level reference block is skipped because full_expt = 0. The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by the final detection.
- Readout roles: readout 1 is the initial polarized / true 0-level reference detection before the microwave pulse. Readout 2 is the post-Rabi-pulse signal detection.
- mod_depth: 1.
- Pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Data assessment:
The combined readouts are noisy and the post-pulse signal does not show a consistent resonance-shaped dip relative to the reference. The normalized signal/reference contrast has isolated single-point excursions, including around 3.870, 3.905, 3.920, and 3.925 GHz, but these do not form a stable linewidth-scale feature. The two per-average traces do not agree on a coherent resonance position: one average has larger positive contrast near 3.905 and 3.915 GHz, while the other has stronger features at different frequencies such as 3.870 and 3.925 GHz. Given the active 52 ns modulated Rabi pulse with full modulation, a real pODMR resonance should produce a repeatable frequency-dependent contrast feature rather than scattered point-to-point fluctuations.

Decision:
Resonance absent.
