---
headline: "ICML's Distinguished Paper Says Diffusion Language Models' Signature Advantage Is Actually a Trap"
slug: icml-flexibility-trap-diffusion-lms
category: research
story_number: 11
date: 2026-07-20
---

# ICML's Distinguished Paper Says Diffusion Language Models' Signature Advantage Is Actually a Trap

For two years, the pitch for diffusion language models has been the same: unlike GPT-style autoregressive models, which are chained to writing left to right, a diffusion LM can fill in a sentence in any order it likes. Write the conclusion first, backfill the reasoning. That freedom, the argument went, gives diffusion models a solution space that strictly contains everything an autoregressive model can do — and therefore a higher ceiling.

At ICML 2026 in Seoul, the conference's top honor went to a paper arguing that the freedom is the problem.

"The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models," led by Zanlin Ni of Tsinghua University's LeapLab with senior author Gao Huang and collaborators from Tsinghua's NLPLab and Alibaba Group, was named one of two ICML 2026 Outstanding Paper Awards on July 5, alongside "High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions" by Fan Chen, Sinho Chewi, Constantinos Daskalakis and Alexander Rakhlin. Both winners were diffusion papers — an unusual concentration for a conference that fielded a shortlist drawn from eight subject areas. (Note: the award is formally titled "Outstanding Paper," though much of the coverage out of Seoul has referred to it as a Distinguished Paper Award.)

## The claim: models use flexibility to duck the hard parts

The authors' core finding is behavioral, not theoretical. When a diffusion LM decodes in arbitrary order, it picks which token to unmask next based on its own confidence — and it systematically picks the easy ones first.

The tokens it defers turn out to be the ones that matter. Inspecting frequently bypassed positions, the team found the sampler disproportionately postpones logical connectives and transition markers: "Therefore," "Thus," "Since." Prior work has identified these as "forking tokens" — the points where a chain of reasoning branches. By the time an arbitrary-order sampler circles back to fill them in, the surrounding bidirectional context has already locked in an answer, and the uncertainty that would have driven exploration has evaporated. The authors call this **entropy degradation**: global average token entropy stays roughly flat, but entropy specifically at the logical forks collapses.

"The flexibility of arbitrary order serves as a mechanism for inference-time *exploitation* rather than reasoning *exploration*," the authors write. "By bypassing high-uncertainty tokens, the model trades the exploration of diverse reasoning paths for greedy optimization of local consistency."

The measurement they use is Pass@k — how many distinct problems a model can solve given k samples, a standard proxy for how much solution space reinforcement learning has to work with. Across three diffusion LMs (LLaDA-Instruct, Dream-Instruct, LLaDA 1.5) and four benchmarks, arbitrary order is competitive at k=1 but its curve flattens badly as k grows. At k=1024 the picture is stark: on HumanEval, strict left-to-right decoding solves 21.3% of problems that arbitrary order misses, while arbitrary order solves just 0.6% that left-to-right misses. The flexible mode isn't exploring a *different* space. It's exploring a subset.

## The fix: stop trying to preserve the flexibility

That diagnosis has an unusually blunt prescription. Much of the recent RL-for-diffusion literature — ESPO, SPG, GDPO, LLaDOU, d-TreeRPO — spends its complexity budget on machinery to handle arbitrary-order training: combinatorial trajectories, intractable marginal likelihoods, sampler-learner mismatch. Ni and colleagues propose skipping all of it.

Their method, **JustGRPO**, forgoes arbitrary order during RL training entirely, treating the diffusion model as a well-defined autoregressive policy and applying stock Group Relative Policy Optimization with no diffusion-specific adaptations. Trained on LLaDA 8B Instruct with 16 NVIDIA H100 GPUs, it reports 89.1% on GSM8K at sequence length 256 and 45.1% on MATH-500 — against 82.3%/39.0% for ESPO and 82.8%/39.6% for GDPO. On HumanEval at length 256 it posts 49.4% versus 42.1% for ESPO.

Critically, the autoregressive constraint applies only during training. The architecture is untouched, so parallel decoding survives at inference — and the paper reports it survives better than before. Using the training-free EB-Sampler on MBPP, JustGRPO's advantage over the base model *widens* as parallelism increases, from +10.6% at one token per step to +25.5% at roughly five tokens per step. An ablation, JustGRPO-Random, which trains in a fixed random order, drops to 82.2% on GSM8K and produces structurally corrupted LaTeX — evidence that it is sequentiality, not merely order-fixing, doing the work.

## Analysis: why the committee singled this out

The ICML award citation is explicit about what it liked, and it is not primarily the benchmark numbers. "This is a non-obvious failure mode that was far from evident before this work," the program chairs wrote, praising a "refreshingly counter-intuitive view that challenges one of the field's dominant assumptions" and flagging the open question the paper leaves behind: "which sampling strategy should drive RL rollouts in dLLMs."

That framing matters for the commercial race. Diffusion LMs have been marketed on two properties — parallel decoding (speed) and arbitrary order (quality ceiling). This paper doesn't touch the first, which is the one that actually shows up in latency benchmarks. It argues the second was oversold for general reasoning, and that teams have been paying a large complexity tax to preserve a property that hurts them. If it holds, the practical diffusion LM of 2027 looks like an AR-trained model with a non-causal backbone kept purely for fast sampling.

Two caveats the authors themselves raise. The finding is scoped to math and code; for genuinely non-sequential structured tasks like Sudoku and zebra puzzles, arbitrary order retains documented benefits. And JustGRPO is not free — a non-causal model needs one forward pass per token position to compute exact likelihoods, so per-iteration training cost exceeds that of a causal transformer.

## What to watch

The immediate test is whether labs shipping diffusion LMs at scale reproduce the Pass@k collapse on their own models, or find it's an artifact of the 8B-class open checkpoints the paper evaluates. Code and the JustGRPO-trained LLaDA checkpoint are public, which makes that a matter of weeks rather than a conference cycle. Watch also for the counter-argument: the paper measures reasoning potential under RL, and arbitrary order's real payoff may lie in infill, editing and agentic revision workflows that Pass@k on GSM8K doesn't capture. ICML has put its heaviest thumb on the scale; the rebuttals are already being written.

---

**Sources:**
- [Announcing the ICML 2026 Awards](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/) — ICML Blog
- [The Flexibility Trap project page](https://nzl-thu.github.io/the-flexibility-trap/) — LeapLab, Tsinghua University ([arXiv:2601.15165](https://arxiv.org/abs/2601.15165))
- [ArXivIQ technical breakdown](https://arxiviq.substack.com/p/icml-2026-the-flexibility-trap-rethinking) — Grigory Sapunov
- [DeepMind's Classic Masterpiece Reaches New Heights: ICML 2026 Grand Award Winners Announced](https://eu.36kr.com/en/p/3883532461961473) — 36Kr Europe
