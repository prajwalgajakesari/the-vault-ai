When Epoch AI launched FrontierMath Tier 4 on July 11, 2025, it was built to be unbeatable. Math professors and postdocs were each contracted to spend weeks turning a research project into a single problem. The best model in the world solved 5% of them. On September 10, 2026 — fourteen months later — Epoch announced that every remaining Tier 4 problem had fallen, with OpenAI's GPT-6 Astra taking the last one standing.

“Every FrontierMath Tier 4 problem has now been solved by AI, with GPT-6 Astra solving the last problem standing,” Epoch wrote in its announcement. “Mathematicians often commented that AI found unintended shortcuts when solving their Tier 4 problems. Not so for this last one, which was created by Jay Pantone.”

That second sentence is the more interesting one, and it cuts both ways.

## What was actually measured

Two claims are being run together in the coverage, and they are not the same. The first is that the top Tier 4 score now sits at **98%**. Astra's leaderboard number is 97.6%, against 83.0% for GPT-5.6 Sol and 68.3% for GPT-5.6 Terra. Tier 4, after Epoch's June 2026 revision, contains **43 problems**. 97.6% is 42 of 43 — the best model in the world still misses one.

The second claim is that *every* Tier 4 problem has now been solved by AI at least once. That is a union across models and runs. Astra cracked the Pantone problem that had defeated everything before it; something else, somewhere else, got the one Astra misses. Neither fact means a model sat down and solved the benchmark.

The June revision matters too. Epoch's v2 update corrected errors in 42% of FrontierMath problems, rewriting 12 Tier 4 items and deleting 7 outright. The wall that just fell is seven problems shorter than the wall that was built.

And Tier 4 is not a proof benchmark. Models submit a Python function returning an answer object, checked programmatically, inside a sandbox with sympy, numpy and a computer algebra stack. Getting the right number is the whole task — which is precisely what produces the shortcut problem Epoch flagged. A research-grade question with a closed-form answer can sometimes be brute-forced or numerically cornered without touching the mathematics the author had in mind.

## Benchmark saturation is the story of 2025-2026

FrontierMath was supposed to be the durable one, announced in late 2024 on the reasoning that research mathematics is where reasoning genuinely bottoms out. Its hardest tier lasted fourteen months. And there is an unavoidable asterisk on the scoreboard. Epoch's own benchmark page carries the disclosure in plain text: “FrontierMath was developed with funding from OpenAI, who has exclusive access to a subset of the benchmark.” That relationship was not disclosed at launch. When it surfaced in January 2025, more than sixty contributing mathematicians learned at once that they had written problems for a test the funder could see, and several said they would not have participated had they known. Epoch's associate director said the organization had been “restricted from disclosing the partnership until around the time o3 launched.” Epoch has been far more transparent since; the structural fact has not changed.

The deeper issue is what saturation tells you. If a benchmark is solved partly by reasoning and partly by exploiting the answer format, the score at 5% and the score at 98% are not measuring the same thing. Epoch's note about Pantone's problem concedes the first happened routinely and argues it did not happen at the end. Only the mathematicians who wrote the problems can adjudicate that, and most of Tier 4 remains private.

## Erdős is a different kind of test

Epoch has already moved the target. FrontierMath Erdős, launched September 1, is 68 problems selected by Thomas Bloom — who maintains erdosproblems.com, cataloguing 1,217 Erdős problems, 652 still unsolved — as his favorites among the hard and significant ones. All were open as of August 2026 and all are formalized in Lean, with models required to produce a machine-checkable proof or disproof within $300 and 72 hours. There is no answer to guess at, and no shortcut that survives a Lean checker.

Astra scored **3%**: 2 of 68 on the official run. GPT-5.6 Sol, GPT-5.5, Claude Fable 5.1 and Claude Fable 5 scored zero. It disproved problem 74 for $218, and proved problem 126 for $247. In larger-budget runs Epoch refuses to count as a score, Astra solved three more — five total, at over **$220,000** in compute, against roughly $20,000 for the official benchmark. On 172 further attempts, it solved nothing.

Epoch's framing is deliberately unglamorous: Astra solved about 3% of significant open problems in this scaffold at this budget, a data point on AI-driven math breakthroughs that is, in its words, “real but still fairly uncommon.”

Bloom's caveat on his own curation is worth keeping too: “No doubt every mathematician will see some problems on this list and think ‘why on earth did they include that?' — but as long as they also see others and think ‘naturally that should be included, it's a deep and important problem', then I think we have done a good job.”

Formalization also imposes a tax unrelated to insight. When an OpenAI model resolved the Erdős unit distance conjecture, the natural-language proof ran 18 pages; formalizing it in Lean took **1.2 million lines** of code, mostly rebuilding a deep result the standard library lacked.

## What to watch

Whether the mathematicians who authored Tier 4 problems publish assessments of Astra's solutions — the shortcut question is empirical and currently unanswered. Whether Erdős scores move off the low single digits next generation, or whether $220,000 for five proofs is the shape of the curve. And whether Epoch's contamination plan holds: the Erdős problems are public, and the measure of an honest benchmark now is how fast its own results poison it.

Astra's 98% on Tier 4 and its 3% on Erdős were produced by the same model in the same month. The gap between those two numbers is the actual state of AI mathematics.
