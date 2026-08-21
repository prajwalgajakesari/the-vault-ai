# Generated Video Falls Apart After a Few Seconds. A Training-Free Method Stretches It to Two Minutes.

Ask a modern video model for five seconds of footage and you often get something close to photoreal. Ask for a full minute and you can watch it die. The sky slides toward magenta. A jacket changes colour, then changes back. Motion thickens into a loop that replays the same half-second of walking forever. By the end, the frame is a smear with no obvious relationship to the prompt.

The cause is structural. The fastest streaming video generators work autoregressively: they produce a short chunk of frames, then generate the next chunk conditioned on the chunk they just made. Every small error is inherited, amplified and fed forward, unflagged. A paper posted to arXiv on 29 July 2026 states the problem in its opening lines: errors introduced during self-rollout accumulate over long horizons, in the authors words, “manifesting as color drift, motion stagnation, and eventual visual collapse.”

The paper is **FreqForcing: Autoregressive Long Video Generation via Spectral Self-Anchoring** (arXiv:2607.27110), by Jiatong Li, Leo Liang, Linghe Kong and Yulun Zhang. Its claim is narrow and testable. Take Self-Forcing, an existing streaming generator trained only on five-second clips. Add no training at all. Generate stable two-minute video, a 24-fold extrapolation past anything the model saw in training.

## The diagnosis: drift lives in the low frequencies

The more interesting contribution is arguably the diagnosis rather than the fix. The authors ran 60-second generations through a short-time Fourier transform to find where in the spectrum the degradation shows up. Energy in the direct-current and low-frequency bands, which encode colour tone, layout and identity, drifts steadily away from its starting values, while high-frequency bands carrying local motion and fine texture become unstable. That maps onto what viewers see: colour and identity are low-frequency properties, which is why long clips wash out or change palette.

The mechanism is the rolling key-value cache these models use to stay fast. As the paper puts it, the cache “only retains recent imperfect frames, which deviate significantly from the initially generated high-quality frames, and this mechanism ultimately leads to visual collapse.” The model's memory of what it is making is always a memory of its own recent mistakes. A common patch, the attention sink borrowed from long-context language models, pins a few early frames permanently in the cache. The authors find it helps but cannot reverse a trajectory once recent frames are already corrupted.

## The fix: two attention branches, fused in frequency space

Spectral Self-Anchoring runs two attention paths side by side at inference time. In the authors words: “a local branch preserves high-frequency details and recent changes, while an anchor branch supplies stable low-frequency guidance. The two outputs are fused in the frequency domain, suppressing low-frequency drift without sacrificing dynamic visual content.”

Concretely, the system keeps an anchor cache of six latent frames, appending one of every three generated frames until it fills, then freezing it. At each step it takes a 3D Fourier transform of both branches, applies a Gaussian low-pass filter, and blends the anchor's low frequencies into the local branch's output before transforming back. It does this only during the first two of the base model's four denoising steps, when coarse structure is decided, which is what keeps it cheap.

On the VBench-Long benchmark the gains are largest at the longest horizon. At 120 seconds, FreqForcing scores **58.97** on Dynamic Degree against Self-Forcing's 27.42, roughly twice as much genuine motion rather than a frozen or looping scene. Aesthetic Quality rises from 51.22 to 60.68, Imaging Quality from 61.40 to 68.89, Overall Consistency from 16.17 to 20.98. The cost is what the paper calls “only about a 16.5% increase in inference latency over Self-Forcing” on NVIDIA RTX A6000 GPUs, with no retraining and no extra data.

## What a benchmark gain does not prove

FreqForcing does not beat the training-based systems it is measured against. At 120 seconds it trails LongLive on motion smoothness (98.22 to 98.79) and subject consistency (97.38 to 97.83), and Rolling Forcing leads on imaging quality (70.72 to 68.89). The abstract claims only to remain competitive with training-based approaches. What is new is that this arrives free, at inference, on a model somebody else trained.

The method's own control knob has a published cost. As anchoring strength rises from 0.2 to 0.8, the Repetitive Rate climbs from 0.675 to 0.794: anchoring harder to a frozen snapshot of the past makes video more stable and more boring. The authors also note that once frames drift far enough from the pinned anchors, the model exceeds its pretrained positional range and “eventually produces unnatural artifacts.”

There is also no FVD score and no human evaluation win rate in the results. A Dynamic Degree of 59 does not distinguish meaningful narrative motion from energetic jitter. This matters because the systems dominating the category, from OpenAI, Google DeepMind and the fast-moving Chinese video labs, are increasingly marketed as world models rather than clip generators. Long-horizon stability is the load-bearing assumption under every claim that video generation is learning physics. A patch that stops the palette sliding is useful engineering. It is not evidence that anything underneath has learned object permanence.

One note on provenance: this story began as a report on a Meta AI paper on temporal grounding said to extend coherence to 45 to 60 seconds. We could not find it. Meta publishes on video temporal grounding, but that is a video *understanding* task, not generation. We are treating the original claim as unverified.

## What to watch next

Three things. Whether training-free spectral corrections survive contact with much larger base models, or are an artifact of a small distilled four-step student. Whether anyone publishes human preference studies at the two-minute mark, where benchmark scores and viewer patience most obviously diverge. And whether the field converges on a long-horizon benchmark measuring narrative persistence and scene memory rather than frame-to-frame smoothness. Until then, the honest summary is that a five-second model has been coaxed into two minutes that do not collapse. That is a real result, and a smaller one than it sounds.
