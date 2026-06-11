# DiffusionGemma: Google DeepMind bets on text diffusion for 4x faster local generation

Google DeepMind on June 10 released DiffusionGemma, an experimental open-weights model that throws out the cardinal rule of modern large language models: it does not generate text one word at a time. Instead, the roughly 26-billion-parameter model drafts entire blocks of text at once and refines them over several passes, an approach the company says delivers up to 4x faster generation on dedicated GPUs. It is the most prominent attempt yet to bring "text diffusion" — long an academic curiosity — into a production-grade open model.

The release, announced on Google's Keyword blog by DeepMind research scientists Brendan O'Donoghue and Sebastian Flennerhag, lands under a permissive Apache 2.0 license with day-one weights on Hugging Face and Kaggle. "Today, we're introducing DiffusionGemma, an experimental open model that explores text diffusion, an exceptionally fast approach to text generation," the authors wrote, framing it as a research artifact rather than a replacement for the mainstream Gemma 4 line.

## What it is, by the numbers

DiffusionGemma is a Mixture of Experts (MoE) model with 26 billion total parameters that activates only 3.8 billion during inference — the architecture Google labels "26B-A4B." That sparsity is what keeps it nimble: quantized, it fits within roughly 18GB of VRAM, putting it within reach of high-end consumer cards. Google cites throughput of more than 1,000 tokens per second on a single NVIDIA H100 and more than 700 tokens per second on a GeForce RTX 5090. The DeepMind model page goes slightly further, claiming "up to 4x-5x faster" output on NVIDIA hardware.

The model is built on the Gemma 4 backbone and what Google calls its Gemini Diffusion research, with a "novel diffusion head designed to maximize generation speed." Each forward pass generates 256 tokens in parallel.

Notably, Google is candid about the trade-off. "While autoregressive Gemma 4 models remain the standard for high-quality production outputs, DiffusionGemma is designed for researchers and developers exploring speed-critical, interactive local workflows," the blog states, adding that the model's "overall output quality is lower than standard Gemma 4." Google explicitly recommends standard Gemma 4 "for applications that demand maximum quality." DeepMind did not publish a head-to-head benchmark table in the announcement materials reviewed, so quality claims are best treated as directional rather than precise; readers should wait for independent evaluations.

## Text diffusion vs. autoregressive, in plain terms

Almost every chatbot you have used is autoregressive: it predicts the next token, appends it, then predicts the next, marching left to right like a typewriter. Each keystroke waits on the one before it. That is efficient in the cloud, where servers batch thousands of users together to keep the hardware busy — but for a single user on a local GPU, the chip spends most of its time idling between keystrokes.

Diffusion flips the process. Borrowing from AI image generators that start with visual static and sharpen it into a picture, DiffusionGemma begins with "a canvas of random placeholder tokens," makes multiple passes locking in the tokens it is confident about, and uses those as context to refine the rest until the block "converges into high-quality output," per Google's description. Because the model sees the whole paragraph as it works, it uses bi-directional attention — every token can attend to every other — enabling what Google calls "intelligent self-correction" and tasks autoregressive models handle poorly. In one demo, partner Unsloth fine-tuned the model to solve Sudoku, a problem where each answer depends on cells that come later.

## Why it matters

The headline is speed, but the deeper story is hardware economics. DiffusionGemma shifts the bottleneck "from memory-bandwidth to compute," which is precisely the resource that sits underused when a single person runs a model on a local GPU. That makes it a wedge for real-time, on-device applications — in-line code editing, rapid iteration, infilling — where latency, not raw quality, is the constraint.

The ecosystem support signals intent. Google coordinated with NVIDIA on optimized kernels, including native NVFP4 4-bit support on Blackwell, and shipped day-zero integrations across vLLM, Hugging Face Transformers, MLX, NeMo and Unsloth. An open Apache 2.0 license means anyone can fine-tune and redistribute it — a deliberate move to seed research into a generation paradigm that, until now, larger labs had mostly kept experimental.

There are real caveats. Google itself notes the speedup is strongest at "low-to-medium batch sizes on a single accelerator"; in high-throughput cloud serving, autoregressive models still win on cost, and parallel decoding can even raise serving costs. And a footnote warns that unified-memory machines like Apple Silicon Macs — which are memory-bandwidth-bound — "may not see the same acceleration." This is a tool sharpened for a specific job, not a universal upgrade.

## What to watch

Three things. First, independent benchmarks: until third parties quantify the quality gap against Gemma 4, the "lower quality" disclaimer is doing a lot of work. Second, whether the diffusion approach scales — DiffusionGemma is explicitly experimental, and the open question is whether Google folds these gains into future flagship Gemma or Gemini models. Third, ecosystem uptake: with llama.cpp support "arriving soon" and a Hackable Diffusion JAX toolbox released for fine-tuning, the test will be whether developers build the speed-critical, non-linear workflows Google is betting exist.
