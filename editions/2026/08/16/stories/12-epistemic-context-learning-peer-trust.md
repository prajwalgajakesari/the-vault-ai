Put five language models in a room and ask them a hard chemistry question, and something uncomfortable happens: the one that is right often changes its mind. Not because it was argued out of its answer, but because the others sounded sure. Researchers led from the National University of Singapore have measured how bad this gets — an agent whose peers were all wrong went along with them more than 85 percent of the time — and proposed a fix that is less about better reasoning than better bookkeeping.

The paper, **Epistemic Context Learning: Building Trust the Right Way in LLM-Based Multi-Agent Systems** (arXiv:2601.21742), was posted January 29, 2026. Ruiwen Zhou (NUS) and Maojia Song (SUTD) share first authorship, with senior authors Min-Yen Kan of the NUS WING lab and Soujanya Poria of NTU; co-authors span Waterloo, Duke, Penn, Peking University, and Microsoft.

## The problem: grading arguments instead of arguers

Most work on multi-agent robustness asks an agent to evaluate the *content* of what its peers say — is this reasoning chain sound? The authors argue this is often the harder problem. If a question exceeds an agent's competence, it cannot verify a peer's chain of thought either, so it falls back on surface signals: "a confident but hallucinated explanation can dominate a concise yet correct answer." Their alternative changes the question the agent asks itself. As the paper puts it: "When correctness cannot be established from the current interaction alone, the problem naturally shifts from evaluating what is said to evaluating who is speaking."

To show the problem is real, the team ran an "All Wrong" probe on Qwen 2.5-3B and Llama 3.2-3B, forcing every peer to answer incorrectly. Accuracy collapsed below 15 percent when peers reported only final answers, and below 50 percent when they supplied full reasoning. Models, the paper concludes, "tend to over-rely on peer opinions, even when it contradicts their internal knowledge or is factually incorrect."

## How ECL works

Epistemic Context Learning splits the agent's job in two, and the split is the whole trick. In stage one, **epistemic trust estimation**, the agent sees only the interaction history — five prior rounds in which each peer answered a question — and writes a natural-language profile of who was right and how often. The current question and the peers' current answers are deliberately withheld: an information bottleneck forcing the model to compress history into a prior rather than pattern-match on the answer in front of it. In stage two, **trust-informed aggregation**, the raw history is discarded and replaced by that profile; the agent then sees the profile, the new question, and the peers' new answers.

Both stages are trained with GRPO reinforcement learning. Stage two gets a standard outcome reward; stage one gets an auxiliary **peer recognition reward**, a binary signal for correctly naming the reliable peer. The split is load-bearing: bolting that same reward onto a single-stage agent made things worse, dropping Math500 accuracy from 73.0 to 62.2 percent and LiveCode from 75.7 to 55.4 percent. "We observe that this is due to reward hacking," the authors write, "where the model learns to exploit spurious correlations in the current-round input to maximize PRR, rather than reasoning from historical evidence."

## The numbers

Evaluation used MMLU-Pro and GPQA with four peers, under a "natural" regime mixing Gemini 3 Flash with weaker models and an "adversarial" one where all four peers are the same Qwen3-30B thinking model, three prompted to inject subtle errors.

The headline claim holds. On adversarial MMLU-Pro, Qwen 3-4B with ECL scored 90.0 percent, beating a history-agnostic aggregator built on Qwen 3-30B — eight times its size — at 81.1 percent. On natural GPQA, Qwen 3-4B rose from 42.5 to 70.0 percent. Gemini 3 Pro hit 100.0 percent on adversarial GPQA against a 90.0 percent baseline.

The gains concentrate where you would expect. Against adversarial peers, ECL routinely adds 10 to 15 points; in the natural setting with frontier models, margins shrink to noise or vanish, and Gemini 3 Pro's natural MMLU-Pro score under ECL (85.6 percent) sits slightly *below* its plain baseline (87.8 percent). The authors are candid: "while standard aggregation may suffice for helpful peers, explicit trust modeling is critical for maintaining robustness when facing deceptive or unreliable agents."

## Analysis: trust is the new bottleneck, and it is brittle

The most consequential result is one the paper frames as validation rather than warning. In the "Flip" test, a peer's reliability is inverted at evaluation time — the historically dependable agent suddenly answers wrong. ECL agents fall apart: Gemini 3 Flash drops from 96.7 to 46.7 percent on MMLU-Pro, and from 97.5 to 35.0 percent on GPQA. The authors read this as proof the mechanism works. True — but one failure mode has been traded for another. Instead of deferring to whoever sounds confident, the system defers to whoever was right last week.

The impact statement concedes as much: "explicit trust modeling introduces the risk of overreliance on historically reliable peers who may later fail or become compromised... future research must address dynamic reliability shifts to ensure trust mechanisms do not become vectors for manipulation."

Other caveats matter. Test sets are small — 90 MMLU-Pro and 40 GPQA questions — so swings of a few points should not be over-read. Only Qwen 3-4B and 3-8B were RL-finetuned; larger models were inference-only, for compute reasons. The abstract advertises "a strong correlation in trust modeling accuracy and final answer quality," but reports no correlation coefficient — only accuracy split by whether the model named the right peer, with one row running the wrong way. And trust modeling degrades with difficulty: on GPQA, the smaller Qwen models identified the reliable peer just 40 to 52.5 percent of the time. There is no limitations section.

## What to watch

The durable contribution is the reframing, not the leaderboard. As agent frameworks move from debate demos toward persistent systems where the same sub-agents interact for months, reliability becomes something you can accumulate cheaply, without re-deriving every claim. The open question is what happens once reputation is worth attacking: a peer that behaves impeccably for five rounds before defecting is exactly the adversary ECL's own Flip results say it is unprepared for. Watch for work on recency-weighted trust, on reputation that transfers across domains, and on whether any of it survives agents that know they are being profiled.
