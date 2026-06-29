Nvidia spent the better part of a decade selling the picks and shovels of the AI gold rush. On June 4, it shipped a gold bar of its own — and gave it away.

Nemotron 3 Ultra, the largest open-weights model the company has ever released, is a roughly 550-billion-parameter mixture-of-experts system built on a hybrid Mamba-Transformer architecture, with a 1-million-token context window and an Artificial Analysis Intelligence Index score of 47.7. That figure makes it the most intelligent open-weights model ever released by a U.S. lab — and a pointed reminder that, on the open-weights leaderboard, American labs are still chasing China.

## What Nvidia actually shipped

The headline numbers are unusually transparent for a frontier release. Nemotron 3 Ultra carries approximately 550 billion total parameters but activates only about 55 billion per token — roughly 10 percent sparsity — a mixture-of-experts design that keeps inference cost closer to a mid-sized dense model than its parameter count would suggest. The independent benchmarking firm Artificial Analysis, which Nvidia partnered with for pre-release evaluation, scored the recommended NVFP4-quantized weights at 47.7 on its Intelligence Index, with the higher-precision BF16 version reaching 48.2.

The architecture is the more interesting story. Rather than a pure Transformer, Nemotron 3 Ultra is a hybrid: most layers use Mamba-style state-space blocks, which scale sub-quadratically with sequence length, while a smaller number of attention layers are retained for precise recall over long contexts. The payoff is speed. Tested on a pre-release BlackBox AI endpoint, the model served at over 400 output tokens per second — slightly faster than gpt-oss-120b despite being more than four times its size. Nvidia frames the model as purpose-built for "long-running agents," the kind of multi-step, tool-using workloads where a million-token window and cheap-per-token throughput compound into real cost savings.

Nvidia released more than weights. The company published base, post-trained, and NVFP4 checkpoints alongside training data and recipes under a permissive license, and the model went live on day zero across more than two dozen platforms including Hugging Face, OpenRouter, Together AI, Perplexity, and Amazon SageMaker JumpStart. The post-training relied on a technique Nvidia calls Multi-teacher On-Policy Distillation, compressing the strengths of more than ten specialized teacher models into a single student.

## Why a chip company is building open models

The obvious question is why the world's most valuable hardware company is investing in software it gives away. Kari Briski, Nvidia's vice president of generative AI software, has been blunt about the strategic logic.

"Open source AI has become a global force for innovation," Briski said in announcing Nvidia's expanded open model families. "NVIDIA open model families extend intelligence beyond language, enabling developers worldwide to build intelligent agents and power breakthroughs across digital and physical industries."

The deeper motive is ecosystem control without ownership. "You don't want one person winning, [because] then they decide all the rules," Briski has said. "You need a big open ecosystem for everybody to come along." Every open model optimized for NVFP4 and Nvidia hardware is, in effect, a demand-generation engine for the GPUs that run it. A thriving open-weights field — even one Nvidia doesn't dominate — sells more silicon than a closed market cornered by two or three labs.

That logic also explains the relentless focus on inference efficiency. The Mamba-Transformer hybrid is not just an academic curiosity; it is a bet that the next phase of AI economics will be won on tokens-per-second-per-dollar, not raw benchmark peaks. The broader industry is converging on the same view — hybrid state-space designs have moved from research papers to shipping frontier models in under two years, precisely because attention's quadratic cost becomes punishing at million-token scale.

## The China gap nobody can paper over

For all the firsts, Nemotron 3 Ultra lands in a leaderboard that remains stubbornly tilted. Its 47.7 Index score leads every U.S. open-weights rival — Gemma 4 31B at 39.2, Nemotron 3 Super at 36.0, gpt-oss-120b at 33.3 — but trails the Chinese-led frontier, with Moonshot's Kimi K2.6 at 53.9. By mid-June, GLM-5.2 had pushed the open-weights ceiling higher still. The pattern is now familiar: the most capable open models in the world keep coming from Chinese labs, and the strongest American answer is a fast, efficient second.

Nvidia's framing leans into where it does win. The model sits on the Pareto frontier for both speed-versus-intelligence and performance-versus-latency on agentic benchmarks like Terminal-Bench v2.1, completing tasks far faster than larger, slower peers. It also posted a strong 71 percent on AA-Omniscience Non-Hallucination, reflecting a low tendency to bluff on factual questions. For agent builders weighing latency and serving cost against a few points of raw intelligence, "fastest credible open model" is a defensible position to own.

## What to watch

The release reframes Nvidia from arms dealer to combatant in the open-weights race, and the question now is cadence. The Nemotron 3 line scaled from Super to Ultra in six months; if Nvidia can compress that loop further while holding its efficiency edge, the U.S.-China gap could close on throughput even if it persists on peak intelligence. Watch whether the hybrid Mamba-Transformer design becomes the default for long-context agents, whether the published training recipes spawn meaningful community fine-tunes, and whether any American lab — Nvidia included — can finally take the top of a leaderboard that Beijing has owned for the better part of a year.
