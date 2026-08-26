MiniMax pushed the weights for a complete song generator onto Hugging Face on August 13, and the detail that made engineers stop scrolling was not the vocals. It was the shape of the output: one WAV file, 32 kHz, 16-bit stereo, up to five minutes long, produced in a single pass — no stitching of 30-second clips, no crossfade seams where a chorus is supposed to land.

MiniMax-Music3 takes two inputs and returns a finished track. The first is lyrics, with structural tags such as [Verse], [Pre-Chorus], [Chorus], [Bridge] and [Solo] on their own lines. The second is a music description, which MiniMax recommends writing as a Structured Caption in three parts: Global Metadata (genre, BPM, key, emotional progression, production profile), Vocal Details (gender, timbre, performance style, harmony, effects) and Arrangement (instruments, section-level instrument evolution, groove, percussion, spatial effects). The company also ships a music-caption-rewriter agent skill that expands a one-line description into that format.

“Music 3.0 focuses on the aspects of music creation that are hardest to capture with a simple prompt,” MiniMax wrote in its research post: “understanding the creator’s expressive intent; sustaining that intent across a complete song of up to five minutes; rendering instruments with clarity and physical realism; and generating vocals that sound performed rather than synthesized.”

## Two Models and a Continuous Tail

The architecture is a split-brain language stack feeding a continuous synthesis path. An 8B Global LLM predicts the first residual vector quantization (RVQ) codebook frame by frame and carries the song’s long-range structure; a 0.6B Local LLM fills in the remaining acoustic codebooks inside each frame. The training tokenizer runs eight RVQ layers — a 16,384-entry semantic codebook plus seven acoustic codebooks of 1,024 entries each.

The interesting move happens at the end. Rather than decoding from discrete tokens, Music3 fuses the final hidden states of both language models and conditions a 2.4B flow-matching module on them, with a 123M Flow-VAE decoder — inherited from MiniMax Speech, retrained for musical dynamic range — reconstructing the waveform. At inference the discrete tokenizer’s decoder is not loaded at all. “Vocals are often where the synthetic character of generated music is most apparent,” the company wrote, arguing that continuous features preserve articulation and breath detail that quantized tokens throw away. One detail stays unsettled: the model card and license say the Global LLM was initialized from Qwen3-8B, while MiniMax’s research post says Qwen3.5-8B.

It also actually runs. SGLang-Omni is the reference server; a diffusers pipeline fits full precision under 24 GB of VRAM, and down to 8 GB with group offloading and a heavy latency penalty. ComfyUI shipped a native text-to-music template on day one. “Another big day for the open source community!” wrote Rob at Comfy Org. The limits are concrete: CUDA required, no streaming generation, prompts capped at 5,000 tokens, audio capped at 9,000 frames at 25 frames per second. “Would be helpful if I could train on LoRA on this… seems to take everything I make and turn it into a rap song,” one commenter posted under Comfy’s announcement on release day.

## The License Says a Lot, and Nothing

The MiniMax-Music3 Community License grants broad rights to use, copy, modify, distribute and sublicense the weights. Commercial use is permitted so long as you “prominently display ‘MiniMax-Music3’ on the user interface” of the product, and any organisation whose aggregate yearly revenue from those products exceeds US$20 million must obtain separate prior written authorisation from MiniMax.

Clause 4 pushes the harder problem downstream. Anyone offering a hosted service that generates outputs must “implement, maintain, test, and periodically review reasonable and proportionate technical and organizational safeguards designed to prevent and mitigate” outputs that “infringe, misappropriate, or otherwise violate any third party’s intellectual-property or other rights.”

What the license does not do is say what the model was trained on. It credits Qwen3-8B (Apache 2.0), Stable Audio’s code for the DiT and Descript’s audio codec for the VAE (both MIT). That is code provenance, not music provenance. There is no dataset disclosure, no opt-out statement, no licensing partner named.

## Why It Matters

That silence arrives in a specific legal moment. Warner Music Group settled with both Suno and Udio in November 2025 and signed licensing deals; Universal settled with Udio on a per-generation royalty reported at $0.002 to $0.005. Sony and Universal are still litigating against Suno, and in May 2026 moved to expand their case from 560 recordings to 61,026 after discovery. A Munich court in the GEMA case found works had been memorised in Suno models and could be substantially reconstructed from short prompts.

The industry’s answer so far has been to license the platform. Music3 is not a platform. It is roughly 11 billion parameters of files that run on a single consumer GPU, and once downloaded it cannot be deprecated, retrained under a settlement, or audited by a plaintiff. Suno’s current models are slated for deprecation in 2026 as licensed replacements arrive; nobody deprecates anything sitting on a hard drive in Lagos or Lisbon. Hands-on comparisons put Music3 roughly in the range of an older Suno V3.5 — clearer on vocals and lyric timing than prior open-source music models, thinner than Suno V5 on instrumental texture. For background scoring, game audio, ad beds and demo tracks, that is past the threshold that matters.

Note also what MiniMax chose not to do. Its omni-modal video model H3 launched July 31 and open-sourced base weights on August 3 under a license excluding open-weight use in the United States, European Union, United Kingdom and South Korea. Music3’s license carries no such territorial carve-out.

## What to Watch

Whether any rightsholder tests Clause 4 — the safeguards obligation is the only infringement backstop in the document, and it has never been litigated. Whether MiniMax publishes anything at all about training data, which it has so far declined to do. And whether fine-tunes appear: the model card documents no fine-tuning procedure, and the first request in the ComfyUI comments was for LoRA support. The moment someone trains one to imitate a named artist on weights nobody controls, this stops being a tooling story and becomes a legal one.
