Google DeepMind has built a research assistant for mathematicians that does not just answer questions — it sits beside them through the messy, weeks-long arc of a proof. And in the benchmark numbers buried in its launch paper, the system did something no AI had done before: it solved nearly half of the hardest problems in mathematics' most punishing AI test.

In a paper posted to arXiv on May 7 ([arXiv:2605.06651](https://arxiv.org/abs/2605.06651)), a DeepMind team led by Daniel Zheng and capped by the lab's science chief Pushmeet Kohli introduced the "AI co-mathematician," an interactive workbench of cooperating AI agents that scored **48% on FrontierMath Tier 4** — described in the paper as "a new high score among all AI systems evaluated."

To understand why that figure has mathematicians paying attention, you have to understand the benchmark. FrontierMath, built by the research nonprofit Epoch AI, is a set of original, unpublished problems written by professional mathematicians and graded all-or-nothing: a model gets one point for the exact correct answer and zero for anything else. Tier 4 is the apex. Epoch describes its roughly 40-plus Tier 4 problems as research-level challenges crafted by professors and postdocs — the kind of work an expert "would expect to need weeks or even months" to finish. Some, Epoch has suggested, may resist AI for years.

The prior baselines make the leap stark. As of mid-2025, the world's strongest reasoning systems — OpenAI's o4-mini, Anthropic's Claude Opus 4, Google's own Gemini 2.5 Pro — were all stuck in the single digits on Tier 4. By late 2025, GPT-5 Pro set a record at roughly 13%. Against that backdrop, 48% is not an incremental gain; it is a different regime. According to coverage of the paper, the underlying Gemini 3.1 Pro model on its own scores about 19% on the same set, and the nearest competing system, GPT-5.5 Pro, lands near 40%.

## How it works

The headline number, though, is almost the least interesting part of the paper. DeepMind frames the co-mathematician not as an autonomous prover but as a collaborator — what the authors and early users call a "mathematician-in-the-loop" tool.

"We introduce the AI co-mathematician, a workbench for mathematicians to interactively leverage AI agents to pursue open-ended research," the paper's abstract reads. The system is built to "provide holistic support for the exploratory and iterative reality of mathematical workflows, including ideation, literature search, computational exploration, theorem proving and theory building."

Crucially, it keeps state. Rather than the stateless one-shot prompting of a chatbot, the co-mathematician offers what the authors describe as "an asynchronous, stateful workspace that manages uncertainty, refines user intent, tracks failed hypotheses, and outputs native mathematical artifacts" — LaTeX write-ups with marginal notes and provenance, dead-end logs, the texture of an actual research notebook. Under the hood, according to the paper and secondary coverage, a coordinating agent steers a hierarchy of specialized sub-agents that pursue different proof strategies in parallel and critique one another's work.

That critique loop produced the launch's most cited anecdote. Marc Lackenby, a topologist at the University of Oxford, used the system to tackle Problem 21.10 from the Kourovka Notebook, a famous running collection of open group-theory questions that has circulated among mathematicians since 1965. The AI's first proof attempt had a flaw — but a reviewer agent inside the system caught it, and the gap turned out to be one Lackenby knew how to fill. He called the AI's approach "really, really clever," per coverage of the work, and the back-and-forth was what carried the problem to a finished proof.

## Why It Matters

For years, the debate over AI in mathematics has fixated on a binary: will machines replace mathematicians, or merely autocomplete their LaTeX? DeepMind's bet is that the more consequential near-term path is neither. The co-mathematician is explicitly designed around collaboration, and the team's early testers reported that it works best precisely when a domain expert is in the loop to steer it — all three early users noted the system shines when the mathematician already knows the terrain.

That reframing matters for how the 48% should be read. A jump from low-teens to nearly half on research-grade problems suggests that agentic architectures — parallel search, persistent memory, internal review — can extract dramatically more from a base model than single-shot prompting does. It is a result about systems design as much as about raw model intelligence. And by anchoring the launch in a real, resolved open problem rather than only a benchmark, DeepMind is making a claim that the tool already produces mathematics professionals consider genuine, not just answers that happen to match a hidden key.

There are reasons for caution. FrontierMath itself has had a turbulent stretch: in June 2026 a major data update corrected errors affecting a large share of problems, a reminder that even gold-standard benchmarks are moving targets. All-or-nothing scoring rewards correct final answers, not the soundness of the reasoning that produced them — and a self-reported state-of-the-art figure inside a launch paper still awaits independent replication.

## What to Watch

The first test will be reproducibility: whether Epoch AI or outside groups confirm the 48% on a stable, error-corrected Tier 4 set, and how the co-mathematician fares against problems written after its training cutoff. Watch, too, for access — DeepMind has described a workbench, not a public product, and whether and how it reaches working mathematicians will shape its real impact.

The deeper question is provenance. As AI moves from solving textbook problems to co-authoring proofs, the math community will have to decide how to credit, verify, and publish results that emerged from a human-AI session. Lackenby's Kourovka proof is an early case study in that negotiation. Expect many more — and expect the journals, not the benchmarks, to be where the next argument plays out.

---

**Sources:** [arXiv:2605.06651 — AI Co-Mathematician](https://arxiv.org/abs/2605.06651); [Epoch AI — FrontierMath Tier 4](https://epoch.ai/benchmarks/frontiermath-tier-4); [OfficeChai](https://officechai.com/ai/google-deepmind-releases-ai-co-mathematician-that-creates-new-high-score-on-frontiermath-benchmark/); [EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/google-unveils-ai-co-mathematician-as-research-agents-move-beyond-chat).
