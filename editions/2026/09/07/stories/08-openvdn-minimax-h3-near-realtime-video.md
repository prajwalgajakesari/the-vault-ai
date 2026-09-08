A research collective calling itself OpenVDN published a set of model weights on Sunday that can render a video clip faster than you can watch it — provided you have eight of Nvidia’s most expensive GPUs on hand, and provided you do not live in the United States, the United Kingdom, the European Union or South Korea.

The release, VDN-MiniMax-H3, landed on Hugging Face on September 6 alongside training and inference code on GitHub. The headline number sits at the top of the model card: on eight Nvidia B200 GPUs, the model denoises a 14.4-second clip at 768p in 11.23 seconds, using eight denoising steps. That is roughly three seconds less than the runtime of the video it just produced.

“In only 11.23 seconds our model can produce a 14.4 second video clip that is visually nearly indistinguishable from the original H3’s output,” the team writes in its technical blog. “In effect, it can stream H3-quality generated content continuously on 8 NVIDIA B200.”

Haocheng Xi, the project’s lead author and a UC Berkeley researcher, put it more bluntly on X: “Open-source video generation is now faster than playback without compromising quality.” The eleven-author paper spans UC Berkeley, the startup Impossible, Inc. and UT Austin.

## What Was Actually Built

VDN stands for Video Delta Net, and the work is surgery performed on someone else’s model. The backbone is MiniMax H3, the omni-modal video-and-audio generator that MiniMax launched July 31 and open-weighted days later. OpenVDN did not retrain it. It attacked the single dominant cost in video diffusion: attention. By the team’s measurement, softmax attention over long token sequences accounts for more than 85 percent of H3’s total runtime.

The fix is a hybrid. VDN splits video attention into two branches — a sliding-window softmax path that computes exact attention between neighboring latent frames, preserving fine detail and short-term stability, and a bidirectional linear-attention path, Video Delta Attention, that carries long-range context cheaply. The softmax branch gets what the authors call 4-way boundary anchors, letting every frame attend to the first and last frames. That trick adds only 3.57 percent attention density but, per the blog, “substantially improves long-range stability.”

The engineering gains compound. On a single B200, one dense H3 block takes 332.5 milliseconds; the hybrid architecture with tuned kernels and FP8 linear layers brings that to 125.3ms, a 2.65x per-layer speedup. Standard Ulysses sequence parallelism across eight B200s cuts latency to 1.62 seconds per denoising step. Then the team does something unusual: rather than have every GPU run both branches, it splits them, assigning five GPUs to the softmax path and three to the linear path. That shaves another 13.3 percent, to 1.405 seconds per step. An eight-step distillation stage does the rest.

Stacked up, the numbers are stark. Dense MiniMax H3 on one B200 needs 16.74 seconds per step and 13.95 minutes for a 50-step render. VDN-H3 on eight B200s does eight steps in 11.23 seconds — a 74.5x speedup over the dense single-GPU baseline, and still 10.7x faster than dense H3 on the same eight-GPU node. On older H200s, the same workload takes 18.3 seconds: fast, but no longer faster than playback.

The full download runs about 82 GB, of which 72 GB is the H3 base. OpenVDN’s own contribution is small — a 4.3 GB linear branch plus LoRA, and 5.1 GB for the eight-step turbo variant, designed to merge into the backbone at inference without touching its weights. “We don’t just open-source the weights,” the model card notes. “The optimized inference stack and its corresponding training code are released together.”

## Why It Matters

The latency milestone deserves a footnote-sized asterisk. The 11.23 seconds is denoising time only. The model card is explicit: “We exclude model loading, warm-up, VAE decoding, and MP4 encoding.” The team’s own recommendation for a live deployment is to run the prompt rewriter, VAE decode and MP4 conversion on separate machines so the eight GPUs do nothing but denoise. Prompts must also be encoded through a Qwen3-VL-32B vision-language model, and OpenVDN recommends rewriting them through H3-Context-IR, a MiniMax module that remains API-only. Real time here means real time inside a carefully staged pipeline sitting on roughly half a million dollars of Blackwell silicon.

Even so, crossing under playback duration is a category shift. Video generation has been a batch process — submit, wait, review. Sub-playback latency is the precondition for interactive video: live avatars, generated game footage, responsive advertising creative. It is the difference between a render farm and a stream.

The license is the stranger half of the story. VDN-H3 inherits the MiniMax H3 Community License Agreement verbatim, and that agreement grants rights only within an applicable territory defined as worldwide excluding the European Union, the United Kingdom, the Republic of Korea and the United States of America. The model card states plainly that use outside the applicable territory “is not authorized” and invites people in excluded regions to contact MiniMax about a license.

That produces an odd artifact: a Berkeley-led research project, published in English, whose weights are not licensed for use in the country where most of its authors work. The code is cleanly Apache 2.0 — the architecture and training recipe travel freely. The weights do not. It inverts the familiar 2025-era pattern, in which Chinese labs shipped permissive open weights that Western developers adopted enthusiastically, and instead pushes legal exposure onto downstream users in the largest AI markets.

## What To Watch

Three things. First, whether the technique generalizes: Video Delta Attention is a backbone-agnostic idea, and a version grafted onto a permissively licensed model would sidestep the territory problem entirely. Second, whether community ports outrun the license — ComfyUI wrappers and Hugging Face Spaces built on the checkpoint appeared within a day of release, and none of them enforce geography. Third, whether MiniMax revisits its exclusions now that outside researchers are producing the most interesting work on its model. The speedup is impressive engineering. The open question is who is legally allowed to use it.
