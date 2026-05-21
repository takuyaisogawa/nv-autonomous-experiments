Inputs inspected: inputs/sequence.xml and inputs/raw_export.json.

The active sequence is the Rabimodulated pODMR sequence, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the XML, full_expt is 0, so the optional 1-level reference block is inactive. The executed detections are therefore:

1. Readout 1: detection immediately after adj_polarize, used as the 0-level/bright reference.
2. Readout 2: detection after rabi_pulse_mod_wait_time, used as the microwave-pulse signal readout.

The relevant pulse settings from the provided XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded pulse length remains 52 ns.

The combined readouts show common drift across the scan, but the signal readout has clear negative contrast relative to the reference at 3.880 GHz and 3.890 GHz. At 3.880 GHz readout 2 is 42.596 versus readout 1 at 45.885, and at 3.890 GHz readout 2 is 43.077 versus readout 1 at 46.308. The same negative signal-reference contrast appears in both averages at those scan points, while neighboring off-resonant points mostly recover toward smaller contrast or positive contrast.

Decision: resonance present. The evidence is a repeatable signal-readout fluorescence dip relative to the reference readout at two nearby microwave-frequency points under the active 52 ns modulated Rabi pulse.
