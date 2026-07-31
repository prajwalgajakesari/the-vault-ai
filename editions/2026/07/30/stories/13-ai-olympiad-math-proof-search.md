# AI Systems Are Cracking Olympiad Math by Generating and Testing Their Own Proof Strategies

For decades, the International Mathematical Olympiad was a stress test that machines flunked. The problems are short to state and brutal to solve, rewarding the kind of creative leap that resists brute force. That barrier has now fallen twice over. In the summer of 2025, systems from Google DeepMind and OpenAI reached gold-medal standard at the IMO, and a growing body of 2026 research is dissecting exactly how they did it: not by memorizing answers, but by generating candidate proof strategies, judging which look promising, and systematically searching the most plausible ones.

The mechanism is the story. Rather than emitting a single answer in one pass, these systems treat a proof as a search problem. They propose many possible lines of attack, score each for plausibility, expand the strongest, and prune the rest, an approach that turns olympiad problem-solving into something closer to guided exploration than pattern completion.

## From Silver to Gold

The lineage is now well documented. At IMO 2024, DeepMind's AlphaProof, paired with AlphaGeometry 2, reached a score equivalent to a silver medalist, 28 of 42 points, with AlphaProof solving three non-geometry problems including the notoriously hard Problem 6. That work was published in *Nature* in November 2025 under the title "Olympiad-level formal mathematical reasoning with reinforcement learning." AlphaProof is an AlphaZero-inspired agent built around a roughly 3-billion-parameter proof network that operates inside the Lean proof assistant, so every step it produces is machine-checkable. For the hardest problems it leans on Test-Time reinforcement learning, generating and learning from millions of related problem variants at inference time, and it runs a formal tree search, typically bounded to a few hundred simulations, over top-ranked candidate tactics.

A year later the bar moved to gold. At IMO 2025, both Google DeepMind and OpenAI reported gold-medal-level performance, each solving five of six problems for 35 of 42 points within the official 4.5-hour limit. DeepMind's result, produced by an advanced version of Gemini with Deep Think, was graded and certified by IMO officials. Notably, that system worked end to end in natural language, reading the official problem statements and producing human-readable proofs, rather than operating purely in formal Lean code as AlphaProof does.

The formal-verification track kept pace too. Harmonic's Aristotle system, described in a late-2025 paper, reported gold-medal-equivalent performance on the IMO 2025 problems while producing machine-verified formal solutions. Its core is an explicit proof-search algorithm, and like the multi-agent Hilbert system, it separates high-level proof planning from low-level formal elaboration, sketching an informal strategy before translating it into verifiable steps.

## Why It Matters

Mathematics has become the field's cleanest testbed for reasoning precisely because it is unforgiving. A proof is either valid or it is not, and in the Lean ecosystem that judgment is delivered by a kernel rather than a human grader, which sidesteps the hallucination problem that plagues open-ended language tasks. That makes automated theorem proving a rare domain where you can generate enormous amounts of self-verified training signal and trust it.

The generate-and-test paradigm behind these results is spreading beyond competition math. In a 2026 line of work on AI-driven formal proof search, researchers applied AlphaProof-style search as a focused tool inside a larger research agent and reported resolving nine previously open Erdős problems, proving dozens of conjectures drawn from the Online Encyclopedia of Integer Sequences, and improving a bound in convex optimization. Those are not olympiad exercises; they are open questions, some of which had stood for decades.

The competitive backdrop sharpens the significance. Many popular reasoning benchmarks are saturating, with frontier models clustering near the ceiling and leaving little room to distinguish genuine progress. Olympiad-grade mathematics resists that saturation because each problem demands a novel idea, and formal verification means partial credit and lucky guesses do not count. If a system can reliably invent, evaluate, and validate its own multi-step strategies here, that is stronger evidence of general reasoning than another benchmark near 100 percent.

## What to Watch

Three threads are worth tracking. First, the tension between the natural-language and formal-verification approaches. Gemini Deep Think's human-readable proofs are more general and flexible, while Lean-based systems like AlphaProof and Aristotle offer airtight machine verification; the interesting question is whether the two converge into systems that reason freely but check themselves rigorously.

Second, the migration from contests to research. The Erdős and OEIS results hint that proof-search agents could become working tools for mathematicians rather than exhibition performers, and the community is organizing around it, with the sixth MATH-AI workshop accepted for NeurIPS 2026 asking how agentic systems can serve as reliable research collaborators.

Third, reproducibility and grading discipline. DeepMind submitted its IMO 2025 result for official third-party evaluation, while some other announcements were self-reported. As these claims escalate, independent verification, ideally machine-checked, will matter more than headline medal counts.

The through-line is that olympiad math is no longer a wall AI cannot climb. It has become a proving ground, in both senses, for systems that write their own strategies and then test whether they hold.

---

*Sources: [Nature](https://www.nature.com/articles/s41586-025-09833-y); [Google DeepMind](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/); [Aristotle (arXiv)](https://arxiv.org/pdf/2510.01346); [AI-Driven Formal Proof Search (arXiv)](https://arxiv.org/html/2605.22763v1).*
