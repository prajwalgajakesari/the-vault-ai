# ExpRL Uses Human Reference Solutions to Mid-Train Reasoning Models With On-Policy RL

For the past two years, the recipe for a strong reasoning model has been numbingly familiar: pretrain, mid-train on a hand-curated diet of reasoning traces to teach the model tricks like decomposition and self-correction, then turn it loose on sparse-reward reinforcement learning where the only signal is whether the final answer is right. A new paper out of Stanford and Carnegie Mellon argues that the middle step has been quietly holding everything back — and that you can replace hand-written curricula with reinforcement learning that learns directly from the enormous corpus of human-written solutions already lying around.

The paper, [ExpRL: Exploratory RL for LLM Mid-Training](https://arxiv.org/abs/2606.17024), was submitted to arXiv on June 15, 2026 by Violet Xiang, Amrith Setlur, Chase Blagden, Nick Haber, and Aviral Kumar. Its headline result: after the full pipeline, an ExpRL-primed model reaches roughly **63.41% pass@1 on AIME-2026**, versus 58.75% for the strongest baseline the authors tested. On one of the hardest public math benchmarks, that is a meaningful gap.

## The problem with mid-training as it exists

Sparse-reward RL — the GRPO-style training that powered the last generation of reasoning models — works only as well as the base model's "coverage." If a model never stumbles onto a correct solution path during sampling, a reward that fires only on the final answer has nothing to reinforce. The field's workaround has been mid-training: supervised fine-tuning on curated traces that explicitly demonstrate the primitive skills a model will need later.

The authors' critique, paraphrased from the paper, is that this approach forces researchers to manually specify what the model should learn, and it is unclear whether a fixed menu of primitives is enough for genuinely hard problems that demand combining those skills into entirely new solution strategies. You can teach a model to verify and backtrack, but you cannot easily hand-write the long-horizon strategy that solves an Olympiad problem it has never seen.

## How ExpRL works

ExpRL's core move is a reframe of what a reference solution is for. Conventional SFT treats a human-written solution as a target to imitate — predict the next token, match the gold trace. ExpRL instead treats references as **reward scaffolds**.

Critically, the reference is hidden from the policy. The model still samples its own reasoning from the original problem prompt, exactly as it would in standard RL. The reference is handed only to an LLM judge, which uses it to build a problem-specific grading rubric and then scores the model's on-policy trace against it. The judge can assign either outcome-level rewards (did the trace reach the right place?) or finer-grained process-level rewards (did it make useful partial progress along the way?).

That distinction is the engine of the method. A sparse final-answer reward gives the model nothing for a trace that does excellent work for nine steps and then fumbles the tenth. ExpRL's dense, reference-guided reward can recognize partial progress, productive intermediate reductions, and the right reasoning behaviors even when the final answer is wrong — shifting probability mass toward productive paths instead of waiting for a rare fully-correct rollout. According to the authors, this is what lets RL serve as the mid-training step itself, rather than something that only happens after a hand-built SFT curriculum.

## The numbers

The authors evaluate ExpRL as a *priming* method — a better initialization for the subsequent sparse-reward RL stage — using a 4B Qwen3-Instruct policy on hard math reasoning. Across held-out answer-based benchmarks, ExpRL variants beat three standard alternatives for that priming role: supervised fine-tuning, sparse-reward GRPO, and self-distillation.

The clearest separation shows up on AIME-2026. There, the process-reward variant, ExpRL-Process, reaches about **63.41% pass@1 after downstream RL**, while the best competing baseline (GRPO) lands at **58.75%**. The authors report that ExpRL not only scores higher but also produces qualitatively different behavior, increasing the model's tendency to verify its own work, self-correct, and backtrack — the very skills that hand-built mid-training curricula try to instill explicitly.

Two further results push on the generality question. The paper reports mixed-domain experiments spanning math, science, and coding, suggesting ExpRL is not a math-only trick. And in one configuration, a smaller 4B judge successfully primes a larger 8B policy — a hint that the judge need not be the most capable model in the loop, which matters for the economics of running this at scale.

## Why it matters

The strategic appeal here is data leverage. Curated reasoning-trace datasets are expensive and bounded; human-written question-answer solutions exist in vast, messy abundance — textbooks, problem sets, forum answers, competition archives. ExpRL is a bet that you can convert that raw, unstructured supply into RL signal without first paying humans to distill it into clean demonstration traces. If references become reward scaffolds rather than imitation targets, the bottleneck shifts from "how many perfect traces can we curate" to "how much human solution data can we point a judge at."

It also reflects a broader convergence: the line between mid-training and RL is dissolving. ExpRL essentially argues there was never a principled reason to do imitation first and reinforcement second — that you can run RL from the start, as long as you give it a denser reward than the final-answer signal. That is a meaningful philosophical shift for a field that has treated SFT and RL as separate, sequential phases.

The obvious caveats apply. The judge is now a load-bearing component, and any LLM-as-judge system inherits the judge's biases and blind spots; a rubric built from a flawed reference can reward the wrong thing. The flagship numbers come from a 4B policy, so whether the gap holds at frontier scale remains open. And a roughly five-point edge on a single benchmark, however hard, is one data point.

## What to watch

The questions worth tracking are scale and robustness. Does the ExpRL-over-SFT advantage persist when the policy is a 70B-plus model rather than a 4B one? How much does final performance depend on the quality of the reference solutions and the judge — and can adversarial or low-quality references be detected and discounted? The mixed-domain results invite the bigger prize: if dense, reference-guided rewards transfer cleanly to coding and science, ExpRL stops being a math-reasoning technique and becomes a general recipe for turning human solution data into RL signal. With [code released](https://github.com/violetxi/ExpRL), expect the broader community to start probing those limits quickly.
