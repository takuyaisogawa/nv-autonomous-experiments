Case: podmr_030_2026-05-16-194429

I inspected inputs/sequence.xml and inputs/raw_export.json, using the provided sequence XML for the active pulse parameters. The sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instructions, the sequence first polarizes and performs a detection before the microwave pulse. The full_expt variable is 0, so the optional "1 level reference" branch is inactive. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection.

Readout roles:
- Readout 1 is the initial post-polarization detection, before the swept microwave Rabi pulse, and acts as the reference / bright-state readout.
- Readout 2 is the detection after the swept microwave modulated Rabi pulse, and is the signal readout sensitive to resonance.

Pulse parameters from the provided sequence XML / variable values:
- Active pulse: rabi_pulse_mod_wait_time
- length_rabi_pulse: 5.2e-08 s, i.e. 52 ns
- mod_depth: 1
- sample_rate: 250 MHz, so the 52 ns duration corresponds to 13 samples and is already on the sample grid.
- full_expt: 0, so no active adiabatic inversion or separate 1-level reference readout is included.

The combined readout 2 trace has its clearest localized minimum at 3.895 GHz: readout 2 is 49.81 while readout 1 is 52.58, giving a readout2/readout1 ratio of about 0.947 and a difference of -2.77 counts. Neighboring signal points recover upward, especially at 3.900 GHz. The per-average traces are noisy, but the first average has its strongest ratio dip at 3.895 GHz, and the second average also has a low post-pulse signal at 3.895 GHz with a nearby low-contrast point at 3.885 GHz.

Decision: resonance_present. The evidence is not a clean high-SNR ODMR dip, but the post-pulse signal readout shows a localized resonance-like depression relative to the reference readout near 3.895 GHz, consistent with a pODMR resonance in this sequence.
