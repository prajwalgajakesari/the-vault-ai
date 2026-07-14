# Mistral's Leanstral 1.5 Brings Formal Mathematical Proof to Code Verification

*Category: llms-genai — The Vault, AI Edition*

A widely used Rust library had a bug hiding in plain sight. In the `datrs/varinteger` crate, the sign function for zigzag decoding performed a simple `(value + 1)` operation. Feed it the maximum 64-bit unsigned integer and it overflows — a panic and crash in debug builds, silent data corruption in release builds. Years of testing and fuzzing had walked right past it. Then a Mistral model pointed at the code, translated it into formal logic, and mechanically proved the flaw existed.

That result, one of five previously unreported bugs the model surfaced, is the calling card of Leanstral 1.5, an open-source formal-verification model Mistral AI released on July 2 and which anchored AI news roundups through the following week. The pitch is unusually concrete for an AI launch: not a chatbot that sounds confident, but a system that produces mathematical proofs a compiler can independently check.

## What Mistral shipped

Leanstral 1.5 is a mixture-of-experts model with 119 billion total parameters but only about 6 billion active per token, released under a permissive Apache-2.0 license with weights on Hugging Face and a free API endpoint. It targets [Lean 4](https://leanprover.github.io/), the proof assistant increasingly used by mathematicians and, more recently, by engineers who want to prove properties of code rather than merely test for them.

Formal verification is old and famously expensive. Instead of writing test cases and hoping they cover the dangerous inputs, you state a property — "this function never overflows," "this sort always returns a sorted list" — and construct a machine-checkable proof that it holds for every input. Done right, it eliminates entire classes of bugs. Done by hand, it can cost more effort than writing the software itself, which is why it has largely stayed inside aerospace, medical-device, and cryptographic engineering.

Leanstral's bet is that a cheap proof-generating model changes that math. On the benchmark side, Mistral reports that the model saturates miniF2F at 100% on both validation and test sets, solves 587 of 672 problems on PutnamBench, and sets open-source state-of-the-art marks of 87% on the graduate-level FATE-H algebra benchmark and 34% on the doctoral-level FATE-X. It operates as an agent, too: editing files, running bash commands, and querying the Lean language server for goals and type errors in real time. In one case study it proved O(log n) time complexity for a real AVL-tree implementation across 2.7 million tokens and 22 rounds of context compaction.

## The cost story is the story

The headline number may be price. Mistral estimates each PutnamBench solution costs roughly $4 with Leanstral 1.5, against an estimated $300 or more for the proprietary Seed-Prover 1.5 at its high setting and $54 to $68 per problem for Aleph Prover. On FLTEval, a benchmark built from real pull requests to the Fermat's Last Theorem formalization repository, Mistral says the model surpasses Anthropic's Opus 4.6 at one-seventh the cost.

The company frames the release as a democratization play. Leanstral 1.5, it writes, proves "that rigorous formal methods can be both effective and practical for real-world use." On the bug-hunting pipeline — which used the Aeneas tool to translate Rust into Lean before Leanstral inferred correctness properties and tried to prove or disprove them — Mistral argues the results demonstrate "that formal verification can already be applied to real-world codebases and find bugs that some traditional methods overlook."

## Why now, and why Mistral

The timing tracks a growing anxiety in software: AI now writes a large share of production code, and increasingly writes the tests for that code too. When the same model authors both, they can share the same blind spots — an input neither thought to consider is an input neither will catch. A proof, unlike a test, has to account for *every* input, and a Lean proof is checked by a kernel that does not care how the proof was generated. That makes formal verification an appealing backstop precisely as autonomous, AI-driven attack tooling — including self-propagating ransomware — raises the stakes for safety-critical systems in aviation, medicine, and cryptography.

The launch also fits Mistral's emerging strategy of owning narrow, defensible technical niches rather than chasing frontier general models head-on. The Leanstral line sits alongside recent releases like Robostral Navigate, a single-camera robot navigation model — deep, specialized capabilities where open weights and low cost can build a moat that a bigger lab's flagship does not automatically fill.

## What to watch next

The open questions are about reach. Leanstral was trained primarily for mathematics; the code-verification results are promising but early, and the Rust-to-Lean pipeline still leans on translation tooling like Aeneas. Watch whether independent teams reproduce the bug-discovery results across more languages and larger codebases, whether safety-critical shops actually fold a $4-per-proof model into their pipelines, and whether Mistral extends direct verification support beyond Lean 4. If verified software has been waiting for the price to fall, this is the clearest signal yet that it is falling fast.
