Active sequence and readout interpretation

The provided sequence is Rabimodulated.xml. The active instructions set the microwave frequency, polarize the NV, acquire a detection immediately after polarization as the true 0 level reference, wait, apply a rabi_pulse_mod_wait_time pulse, then acquire the detection used as the pODMR signal. The optional 1-level reference block is inactive because full_expt = 0.

Key active parameters from the provided sequence XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave pulse before the signal detection is therefore a 52 ns modulated rabi pulse with full modulation depth.

Readout roles

Readout 1 is the pre-microwave true 0 reference detection. It should not carry the ODMR contrast from the scanned microwave pulse and is used mainly as a reference for fluctuations.

Readout 2 is the post-microwave-pulse signal detection. This is the readout expected to show a pODMR resonance if the microwave frequency drives the NV transition.

Data assessment

Readout 1 remains roughly around 46-49 counts across the sweep with no sharp, isolated dip at the feature frequency. Readout 2 is near 46-47 counts over much of the sweep but drops strongly and reproducibly around 3.875-3.880 GHz to about 39.6 counts in the averaged trace. The per-average overlay shows the same localized depression in the post-pulse readout in both averages, while the reference readout does not show a corresponding feature.

Decision

The frequency-localized dip in the post-pulse signal readout, absent from the reference readout and repeated across averages, is consistent with a pODMR resonance.
