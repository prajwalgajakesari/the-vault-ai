A pair of AI agents has resolved a mathematical question that sat open for more than a decade — and, in an unusual twist for the field, the machine did not ask anyone to take its word for it. Every step of the argument was rewritten into Lean 4, a formal proof language, and checked line by line by a compiler that accepts nothing on faith.

The result comes from the AI4Math team at Peking University's Beijing International Center for Mathematical Research, working under the FrenzyMath banner. In a paper titled "Automated Conjecture Resolution with Formal Verification" (arXiv:2604.03789), posted in April 2026 and revised the following months, the authors describe a two-agent framework that searches for a proof in natural language and then mechanically verifies it. They report doing so "with essentially no human involvement."

## How the system works

The framework splits the labor that a human mathematician normally does alone. The first agent, **Rethlas**, plays the role of the working researcher: it constructs toy examples and counterexamples, decomposes a problem into subgoals, and hunts the literature for techniques it can borrow. Crucially, it is wired to a semantic theorem-search engine the team calls **Matlas**, which indexes roughly 13.6 million mathematical statements pulled from arXiv into a vector database, letting the agent retrieve relevant results by meaning rather than keyword.

The second agent, **Archon**, is the skeptic. It takes Rethlas's informal proof and translates it into a complete Lean 4 project — main theorem, supporting lemmas, and definitions — all grounded in Mathlib, the community library that now spans over 267,000 theorems and 127,000 definitions. Archon runs as two cooperating subagents: a Plan Agent that decomposes the task in a fresh context, and a Lean Agent that fills in proofs, scattering `sorry` placeholders and discharging them one by one until the whole project compiles with no gaps, no extra axioms, and no escape hatches.

That division addresses a problem the authors are blunt about. "Mathematical proofs demand complete rigor, yet even expert-written proofs may contain subtle flaws, and proofs produced by LLMs, which are prone to hallucination, are far less reliable," they write. Formal verification is the answer: once an argument passes the compiler, "verifying correctness reduces to checking that the top-level statement and its supporting definitions faithfully capture the intended mathematical content."

## The problem it solved

The target was a question posed by the late University of Iowa algebraist D. D. Anderson in 2014: does *weak quasi-completeness* imply *quasi-completeness* for Noetherian local rings? Both are technical conditions on how chains of ideals behave in the topology of a ring.

Rethlas answered in the negative by building a counterexample — a weakly quasi-complete ring that is not quasi-complete. The decisive move was retrieval: Matlas surfaced a 2006 result by Jensen on when a ring can be realized as the completion of a local unique factorization domain with trivial generic formal fiber, a connection the authors call "very challenging to uncover without domain expertise and is not obviously related at first glance." From there the construction T = C[[x,y,z]]/(x² − yz) yielded the counterexample.

The formalization is where the scale shows. Archon produced roughly 19,000 lines of Lean 4 across 42 files, formalizing not just the main argument but key results drawn from six external papers, in about 80 hours of agent runtime on three Claude Code Max subscriptions. Based on interviews with Mathlib contributors, the team estimates an expert formalizer writes 150–250 lines a day, putting the output at "several person-months of expert effort." Human input, they say, was limited to downloading paywalled PDFs that the agent could not fetch; "no mathematical judgment was required from the human operator."

The paper also documents Archon filling non-trivial gaps the source literature left implicit — implementing a transfinite recursive construction described only as "recursively define {R_α} and take unions at limit ordinals," and, when its first approach via Zorn's lemma broke down, diagnosing that the argument secretly assumed the Continuum Hypothesis and refactoring across sessions to a clean cardinal-arithmetic version. In one case it found a route via Kaplansky's criterion that "does not explicitly appear in any of the reference papers."

## Why It Matters

The headline is not that an AI did mathematics — frontier models have been climbing research benchmarks for a year. Google DeepMind's AI Co-Mathematician work and the broader FrontierMath race (where the leading system now posts 38% on the unpublished Tier 4 problems, against 4% a year earlier) show natural-language reasoning is improving fast. The problem is trust: an LLM that produces a convincing-looking proof may be hallucinating, and even peer review at top journals lets errors through.

This framework attacks that directly. By routing every claim through the Lean 4 compiler, it converts "the model says so" into "the machine checked it." The team further ran the output through Comparator, a sandboxed tool that confirms the formalized statement matches a human-reviewed specification and uses only standard axioms. For a discipline where correctness is the entire point, machine-checked-by-construction is a meaningfully different guarantee than a high benchmark score.

## What to Watch

Several caveats temper the result. The autonomy was real but narrow — one problem, with humans still semantically reviewing the final statement. The authors note Archon's Lean code is verbose, non-idiomatic, and far from Mathlib's contribution standards, so the proof is verified but not yet a reusable library asset. They also flag "overthinking" on hard obligations as a tendency that could become a bottleneck on bigger projects.

The open questions now are generality and reach. The team frames retrieval-driven, cross-domain proof discovery as a paradigm that should extend beyond commutative algebra, and all three components — Rethlas, Archon, and the Anderson-Conjecture formalization — are open-sourced. Whether the approach scales to harder conjectures, and whether agent-generated Lean can be cleaned up into upstreamable mathematics, will determine if this is a milestone or a one-off. For now, it is a concrete demonstration that an open problem can be solved and verified end to end with humans mostly watching.
