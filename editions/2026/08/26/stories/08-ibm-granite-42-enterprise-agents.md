The most interesting number in IBM's Granite 4.2 release is not a benchmark score. It is zero — zero dollars, zero licensing gate, zero API metering. IBM has put a 30-billion-parameter reasoning model trained specifically to drive software agents on Hugging Face under Apache 2.0, and the pitch is blunt: download this, run it inside your own firewall, fine-tune it, and never call anyone's API again.

Released on August 25, Granite 4.2 spans three sizes — 3B, 8B and 30B — all decoder-only dense transformers pre-trained from scratch on roughly 15 trillion tokens. Every model ships with a thinking/non-thinking switch plus a low-effort mode that spends a short reasoning budget on easy questions, and every model does native tool calling in OpenAI function-calling format, dropping into existing agent harnesses without glue code. The architecture table lists a 131,072-token (128K) sequence length; IBM says the five-phase pre-training run included a long-context stage extending to 512K.

## What IBM actually built

The capability split across sizes comes from post-training, not scale. After supervised fine-tuning on about 7.2 million samples — roughly 100 billion tokens, 31.6 percent agentic, with software engineering making up 69 percent of that agentic slice — the models enter a multi-stage reinforcement learning chain. Each stage is a separate asynchronous GRPO run warm-starting from the previous checkpoint: foundational RL with verifiable rewards, targeted skill boosters, then, for the 8B and 30B only, an agentic block running software engineering, terminal and search environments in sequence.

Those environments are real, not simulated. The SWE stage drops the model into a live repository sandbox driven by the OpenHands harness, where the reward is binary: do the hidden tests pass? The terminal stage puts it in an actual shell via Harbor/Terminus-2, with rollouts spanning up to 64 environment turns. The search stage sends it out to make live web queries, judged by an LLM. The 3B skips all of it — the single decision that explains most of the gap between sizes.

The published results are respectable rather than dominant. The 30B scores 57.00 on SWE-Bench Verified, 33.29 on SWE-Bench Pro, 29.24 on Terminal-Bench 2.1, 62.00 on τ³-bench and 61.39 on BFCL v4. Reasoning is stronger: 89.17 on AIME25, 66.41 on GPQA, 77.60 on MMLU-Pro, 81.38 on RULER 128K. The 8B lands closer to its bigger sibling than the parameter count suggests — 47.67 on SWE-Bench Verified, 58.06 on τ³-bench — and runs on a single modern GPU. One oddity: the 3B beats the 8B on BFCL v4, 52.41 to 50.29, a reminder that agentic RL optimizes for trajectories, not single-call tool selection.

Training ran on an NVIDIA GB200 NVL72 cluster hosted by CoreWeave using NVIDIA's open NeMo-RL and NeMo-Gym stack, with 1 trillion tokens of synthetic code from IBM's CodeAlchemy pipeline folded in. FP8, NVFP4 and GGUF quantizations shipped alongside.

## The architecture reversal nobody is talking about

One widely repeated detail about this release is wrong, and it matters. Granite 4.2 is not a hybrid Mamba-2/transformer model. IBM went hybrid with Granite 4.0 — dense, dense-hybrid and hybrid mixture-of-experts variants, pitched hard on GPU memory savings — then reversed course with Granite 4.1, returning to an all-attention dense transformer because, IBM said, the newer models outperformed the prior generation "while using a simpler — and therefore more flexible — architecture for fine-tuning for downstream tasks." While NVIDIA's Nemotron 3 family pushes toward hybrid Mamba/attention designs, IBM has bet that enterprises who intend to fine-tune care more about tooling compatibility than KV-cache economics.

The competitive read is less flattering. "Qwen 3.8 27B, especially, beats the Granite models across the board, especially when it comes to coding, where the IBM models deliver inconsistent results overall," wrote Frederic Lardinois, senior editor for AI at The New Stack. Granite 4.2 is also text-only, while the Qwen, Gemma 4 31B and Muse Glimmer 30B models in its weight class are all multimodal.

## Why It Matters

If raw capability were the whole game, Granite would be a footnote. IBM is playing a different one. Granite is the first open model family certified under ISO/IEC 42001, the international AI management standard, audited by Schellman in under three months with zero non-conformities. Every checkpoint is cryptographically signed so buyers can verify provenance, and IBM's lakehouse tracks more than 2.7 petabytes of training data with license controls.

"We're honored to earn ISO 42001 certification for our flagship Granite models," said David Cox, VP of AI Models at IBM. "Granite is now the first open model family to meet that bar, and it is a testament to the care that goes into building and maintaining them."

That is not a benchmark, but for a bank, hospital or public-sector agency it is closer to a procurement requirement. The buyer who cannot send customer data to a third-party API, cannot accept unauditable training provenance, and cannot tolerate a vendor deprecating an endpoint mid-contract is not choosing between Granite 4.2 and a frontier model. They are choosing between Granite 4.2 and Qwen — a calculus involving geopolitics and compliance paperwork at least as much as SWE-bench.

The deeper shift is what "good enough" now means. A 30B model that resolves 57 percent of SWE-Bench Verified issues and drives a terminal for 64 turns handles a large share of routine enterprise automation. Owning it outright, at fixed cost with no per-token meter, changes the economics of high-volume agentic work more than a few points of benchmark headroom do.

## What to watch

The near-term test is adoption in harnesses, not leaderboards. IBM published configs for OpenCode, OpenHands and Pi, signaling it expects Granite to serve as an agent backbone rather than a chatbot — watch whether developers wire it in, and whether the 8B becomes the practical default. Also worth tracking is IBM's partnership with Hirundo to apply machine unlearning to undesirable outputs post-training, a governance capability no frontier lab currently sells. The open question is whether ISO certification and signed checkpoints outweigh a real capability gap, or whether compliance credentials lose to a Qwen model that simply codes better. IBM has spent two generations betting on the former. The 30B is the clearest test yet.
