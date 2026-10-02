Most deepfake detectors check videos one at a time on power-hungry GPUs. A team at UCLA has built one that checks 15 at once, and a large part of the work is done by light passing through optics, not by electronics. In lab experiments, the hybrid optical-neural processor flagged manipulated videos with 97.79% average accuracy. It caught 99.86% of the fakes it was shown.

The work comes from the lab of Aydogan Ozcan, a UCLA professor who has spent years building "diffractive" optical processors. These are surfaces that do neural-network-style computation as light moves through them. The study, "Scalable, energy-efficient optical-neural architecture for multiplexed deepfake video detection," appears in the journal *eLight*. Its authors are Parnian Ghapandar Kashani and Shiqi Chen, who contributed equally, with Ozcan as senior author. ScienceDaily covered the findings on October 1, and a preprint first appeared on arXiv in May.

## How a Deepfake Detector Runs on Light

The system splits the job into two halves. First, a lightweight digital encoder reads each video and condenses it into a compact summary of its spatial, spectral and temporal features. That summary becomes a phase pattern, which is shown on a programmable spatial light modulator, a device that shapes a beam of light pixel by pixel.

In a conventional detector, a large digital neural network would decode that summary. Here the wavefront travels through a passive, free-space optical decoder instead. At the far end, paired photodetectors read out an authenticity score for each video. Many videos' patterns sit side by side on the modulator, so the decoder handles all of them in a single pass of light. The researchers call this spatial multiplexing.

The authors argue that the gains go beyond speed. In the paper's abstract, they write that "integrating optical computation into AI inference enables simultaneous gains in throughput, energy efficiency, and adversarial robustness—three properties that are difficult to achieve together in purely digital systems."

## The Numbers

In visible-light experiments on the Celeb-DF benchmark, a standard dataset of face-swap deepfakes, the processor tested 15 videos per optical pass. It averaged 97.79% accuracy, 99.86% sensitivity and 95.72% specificity. The sensitivity figure works out to a false-negative rate of about 0.14%, meaning almost no manipulated clips were passed as authentic. The specificity is lower, so some real videos were wrongly flagged.

The team then packed 18 videos into each pass. Accuracy fell to 96.13%, which the paper blames partly on "increased optical cross-talk among video channels."

The researchers also tested whether adding physical depth to the optics improves results. For harder manipulations, two extra optimized diffractive layers raised accuracy by about 6.8%. These layers are static, phase-only structures, so they draw no extra electrical power during inference. The extra computing power essentially comes for free once the layers are made. The paper also explores trade-offs on the digital side. With one extra optical layer and an encoder using 148.16 millijoules per video, the system reached 98.76% accuracy.

The team also tested footage from Google's Veo 3, a newer video generator whose output lacks many of the telltale artifacts of older face-swaps. After only minimal fine-tuning, the processor scored 94.80% accuracy and 97.61% sensitivity on Veo 3 videos it had never seen.

## Harder to Fool

Deepfake detectors face constant adversarial pressure. Attackers can add small, carefully designed perturbations that push a fake past a digital classifier. The UCLA system resisted black-box adversarial attacks in testing. According to the researchers, it also offers inherent protection against white-box attacks, in which an attacker knows the model's internals. Part of the model lives in physical optical hardware, and those parameters are hard to measure, copy or reverse-engineer. That makes it harder to build a perturbation tailored to beat the detector. The processor also held up against noise, blur, JPEG compression and experimental misalignment.

## Why It Matters

Detecting deepfakes is quickly becoming a problem of scale. State-of-the-art digital detectors can need hundreds of billions of floating-point operations per analysis, and they usually process videos in sequence. As a result, compute cost and energy use rise in step with the amount of content. For a platform screening millions of uploads a day, that is a real cost.

The UCLA team is not claiming to replace those detectors. The paper describes the optical system as "an energy-efficient and highly sensitive first-stage screening module." In practice, the optical processor would screen huge volumes of video quickly and cheaply, leaning toward flagging. Only the suspicious clips would go on to heavier digital models for a final verdict. A sensitivity near 100% is exactly what a first-pass filter needs, and the lower specificity matters less when a second stage catches the false alarms.

The work also adds to a wider argument that some AI inference may be cheaper in photons than in electrons. The paper ends by noting that "this paradigm is applicable to a wider class of high-throughput inference tasks, including real-time surveillance, large-scale content moderation, and other security-critical AI systems."

There are caveats. Celeb-DF is an academic benchmark, and the Veo 3 result needed fine-tuning. The system still depends on a digital encoder that uses energy on the order of 100 millijoules per video. Results from a lab optical bench also do not show how the processor would hold up inside a data center.

## What to Watch

The main open question is whether the approach can scale beyond 15 to 18 channels without cross-talk wearing down accuracy. Another is whether it can keep up as new video generators appear every few months, ideally with as little retraining as the Veo 3 test needed. Look for follow-up work on more compact, integrated hardware from the Ozcan lab, which has a track record of turning diffractive prototypes into new applications. Content platforms facing new provenance and labeling rules will also be watching for a screening layer that is fast, cheap and hard to game.
