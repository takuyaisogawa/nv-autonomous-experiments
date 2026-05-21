Active sequence: Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from inputs/sequence.xml:
- sample_rate is 250 MHz, so the requested 52 ns Rabi pulse is rounded to 52 ns.
- mod_depth is 1.
- full_expt is 0, so the optional 1-level reference block is inactive.
- readout 1 is the initial polarized/reference detection after adj_polarize, before the microwave Rabi pulse.
- readout 2 is the detection after rabi_pulse_mod_wait_time using length_rabi_pulse, mod_depth, and switch_delay.

Data assessment:
The post-microwave readout is generally lower than the polarized reference, but the normalized contrast does not form a clear pODMR line. The largest negative excursions are isolated or occur at the scan edge, and comparable point-to-point fluctuations are visible between the two averages. A resonant response for this 52 ns, fully modulated pulse would be expected to appear as a more coherent localized dip in readout 2 relative to readout 1. I therefore classify this case as resonance absent.
