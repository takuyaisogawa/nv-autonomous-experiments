Case podmr_066_2026-05-17-072831

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions set the microwave frequency, polarize, detect the true 0-level reference, wait, then because full_expt is 0 the optional 1-level reference block is skipped. The executed experimental readout is then produced after a rabi_pulse_mod_wait_time pulse followed by detection.

Readout roles: readout 1 is the initial 0-level/reference detection after polarization. Readout 2 is the detection after the modulated Rabi pulse. The optional 1-level reference is not active in this run.

Key pulse parameters from the provided inputs: length_rabi_pulse is 5.2e-08 s, i.e. 52 ns, rounded at 250 MS/s but unchanged. The variable table gives mod_depth = 1 for the executed pulse. The scan uses two averages and 100000 repetitions per point.

Assessment: the two readouts fluctuate by a few counts across the sweep and the per-average traces show substantial average-to-average structure. There is no consistent ODMR-like resonance feature: the post-pulse readout does not show a reproducible narrow dip or peak at a common frequency relative to the reference. Apparent excursions, such as near 3.875 GHz or near the high-frequency end, are comparable to baseline drift and noise and are not consistent across averages. Therefore I classify this case as resonance absent.
