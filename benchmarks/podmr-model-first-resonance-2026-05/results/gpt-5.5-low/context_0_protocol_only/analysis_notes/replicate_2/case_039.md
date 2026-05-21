Sequence inspection:
- Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The executed readouts are therefore the initial polarized/detected 0-level reference followed by a modulated Rabi pulse and a second detection readout.
- mod_depth is 1 and length_rabi_pulse is 52 ns after sample-rate rounding at 250 MHz.

Readout assessment:
The two combined raw readouts fluctuate over the scan without a coherent, repeated ODMR-like dip/peak structure. Some points are large, but they are isolated and not consistently shared across the per-average traces. The per-average overlay shows a strong average-to-average baseline offset, and the apparent combined features can be explained by noise or baseline variation rather than a stable resonance tied to microwave frequency.

Decision:
No reliable pODMR resonance is present in this scan.
