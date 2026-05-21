Sequence review:
- The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps.
- sample_rate is 250 MHz, so length_rabi_pulse = 5.2e-08 s rounds to 13 samples = 52 ns.
- mod_depth is 1.
- full_expt is 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true.
- The active readouts are therefore: readout 1 is the initial polarized/no-microwave true 0-level reference, and readout 2 is the detection after the 52 ns modulated Rabi pulse.

Data review:
The combined readout 2/readout 1 ratio ranges from about 0.9635 to 1.0510, with an average close to unity. The most negative contrast-like points occur near 3.845 GHz and 3.890 GHz, but they are isolated and not accompanied by a smooth or repeatable resonance-shaped dip across neighboring frequency points. The two saved averages are noisy, and several nearby or high-frequency points reverse sign with readout 2 above the reference.

Decision:
I do not see a reliable pODMR resonance in this scan. The apparent dips are too isolated relative to the noise and do not form a consistent frequency-localized contrast feature in the active MW-pulse readout relative to the 0-level reference.
