Foundation models are supposed to be enormous. The one Samsung Research America just put on a smartwatch has about 1.2 million parameters in its base configuration — small enough that the whole thing runs on the watch's CPU and returns an answer in under a millisecond. No cloud round trip. No network at all.

That model is HiMAE, and it is one of two health foundation models Samsung detailed in a Newsroom post published August 14. The other, xMAE, attacks the same underlying problem from the opposite direction: how to extract clinically meaningful signal from the noisy optical pulse readings that wrist wearables collect passively, all day, from tens of millions of people. Both came out of the Digital Health Team at Samsung Research America. HiMAE was accepted to ICLR 2026, xMAE to ICML 2026.

## Teaching a Cheap Signal to Behave Like an Expensive One

The clinical gold standard on a wearable is the electrocardiogram, which reads the heart's electrical activity directly. Its problem is friction: on a Galaxy Watch, an ECG requires the user to stop and take an active measurement. Photoplethysmography — the green LEDs on the underside of the watch — measures blood volume changes optically and continuously, but observes the cardiovascular system only downstream, after the heartbeat has fired and the pulse wave has reached the wrist.

Samsung's Newsroom post frames the gap in one line: the two signals "originate from the same cardiac activity, but they appear with a certain time difference, much like thunder is heard after lightning is seen."

xMAE turns that delay into a training signal. During pretraining the model sees synchronized ECG and PPG together, hides chunks of the ECG, and forces the network to rebuild them using the visible PPG. Crucially, the ECG is a scaffold, not a product. After pretraining the ECG branch is discarded entirely and the PPG encoder goes to work alone. Samsung pretrained it on roughly 3.4 million synchronized 10-second recordings — about 9,400 hours of paired data from approximately 2,400 subjects — then evaluated the resulting PPG encoder across six studies, 19 downstream tasks, 2,300 hours of PPG and 12,500 subjects. It beat unimodal and existing multimodal baselines on 15 of 19 tasks, including hypertension prediction in both lab and free-living settings, premature ventricular contraction detection, abnormal blood-lab prediction, and sleep-stage classification.

The takeaway researchers Hao Zhou and Sharanya Arcot Desai draw in the Samsung Research blog is a rebuke to scale maximalism: "in wearable health AI, the pretraining objective and physiological inductive bias can be as important as model scale."

## What Masked Autoencoding Is Actually Doing

Both models are trained by deletion. Take a stretch of biosignal, chop it into short patches, throw some away, and ask the network to reconstruct exactly what was removed. Error is measured only on the hidden parts. Nobody labels anything — the signal supervises itself, which is what makes it possible to train on the vast archive of unlabeled wearable data that would be prohibitively expensive to annotate with clinical outcomes.

This produces useful representations because guessing the missing piece requires understanding the rules the signal obeys. To fill a gap in a pulse waveform you need an internal model of beat morphology and rhythm variability. Reconstruction is a pretext; the encoder's internal features are the actual output.

Getting the pretext right is where the engineering lives. As Samsung's xMAE writeup notes, masking scattered individual points in a smooth physiological signal is too easy — the model interpolates from neighbors within the same modality and learns nothing cross-modal. So xMAE masks continuous blocks of ECG instead, and uses directional cross-attention where masked ECG tokens query the PPG tokens, making the inference direction explicit: infer upstream electrical timing from downstream peripheral flow.

## Resolution as the Variable Nobody Was Tuning

HiMAE tests a different hypothesis: that the right temporal zoom level differs per health outcome, and that models collapsing everything into one embedding throw that away. It pairs masked autoencoding with a U-Net-style hierarchical convolutional encoder-decoder, then exposes every intermediate layer as its own embedding rather than pooling them. Pretraining used roughly 80,000 hours of wearable green PPG from tens of thousands of participants across multiple devices, on 10-second windows sampled at 100 Hz.

Probing each depth separately produced exactly the pattern predicted. Cardiovascular outcomes such as hypertension and arrhythmia peaked at deeper, coarser layers. Sleep staging favored intermediate-to-coarse scales. Lab abnormalities like hemoglobin or electrolyte imbalance peaked at the finest resolutions, apparently depending on subtle high-frequency distortions in waveform morphology that downsampling washes out. Because convolutional hierarchies scale linearly in sequence length rather than quadratically like self-attention, the model stays tiny while matching or beating transformer foundation models orders of magnitude larger.

## Why It Matters

Health inference that never leaves the device changes the privacy calculus at its root. Continuous PPG is among the most revealing data a consumer product collects, and the standard architecture — stream raw signal to a server, infer there, send results back — creates a permanent repository of it. Samsung's researchers make the connection explicit: compact on-device models support "continuous, private health monitoring," and offer "a new lens for interpretability: not which feature matters, but at what temporal scale information emerges."

Samsung claims HiMAE demonstrates the potential of on-device health foundation models "for the first time." The claim is narrow and worth reading precisely: Apple and Google have both published wearable foundation models trained on far larger corpora, but those are evaluated as server-side systems. Sub-millisecond edge inference is the differentiator, not the underlying method.

The regulatory ceiling is the harder constraint. Individual wearable features clear as medical devices one indication at a time; a general-purpose encoder that happens to predict hypertension, arrhythmia, and abnormal blood chemistry from a passive optical sensor does not fit that framework cleanly, and none of these results are clinical validation. Samsung's own HiMAE writeup says so: "Clinical validation of discovered resolution-specific signals is required before translation."

## What to Watch

Whether any of this reaches a shipping Galaxy Watch, and under what label — wellness insight or cleared indication. HiMAE's stated limitations are its 10-second windows and its PPG-only scope, with extensions to longer contexts and to ECG, accelerometer and EEG flagged as future work. The HiMAE code is public on GitHub, which means the sub-millisecond claim is checkable by anyone with a watch-class CPU and the patience to try it.
