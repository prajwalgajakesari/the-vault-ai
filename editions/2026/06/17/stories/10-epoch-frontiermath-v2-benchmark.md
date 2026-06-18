# Epoch Releases FrontierMath v2, Rebuilt After Flawed Problems Were Pulled

When a benchmark built by dozens of elite mathematicians turns out to have been wrong about nearly half of its own questions, the more interesting story is rarely the new leaderboard. On June 12, 2026, Epoch AI shipped FrontierMath v2, an error-corrected rebuild of its flagship hard-math benchmark, after an internal audit found small but critical errors in 42% of the problems in the original set. The update corrected 135 problems and removed 12 — and in doing so, quietly invalidated the absolute scores that had been treated as ground truth across the industry for more than a year.

The release was announced in The Epoch Brief, the organization's newsletter, alongside a headline that most outlets ran with: Anthropic's newest model, Claude Fable 5, now tops the leaderboard, reaching roughly 87% on Tiers 1–3 and 88% on the benchmark's hardest tier, Tier 4. But the leaderboard is the easy part of this story. The harder part is what a 42% error rate says about how AI's most rigorous evaluations actually get built — and whether anyone should have trusted the prior numbers at all.

## What v2 changed

FrontierMath launched in November 2024 with contributions from more than 60 mathematicians, including holders of International Mathematical Olympiad gold medals and a Fields Medalist among its advisors. Every problem was designed to be "guessproof," using large numerical answers or complex mathematical objects that leave under a 1% chance of a correct guess without genuine work. It was, by construction, one of the most demanding evaluations in the field.

That rigor is exactly what makes the v2 corrections striking. Following the audit, Epoch corrected 123 problems in Tiers 1–3 and 12 in Tier 4, and removed a further 5 from Tiers 1–3 and 7 from Tier 4. The full dataset dropped from 350 problems to 338 — a base set of 295 in Tiers 1–3 plus a 43-problem Tier 4 expansion set. The remaining questions keep their automatic verification and strict compute limits, which is what gives the benchmark a cleaner read on whether frontier systems can actually do hard mathematics.

Epoch was careful to frame the error rate as routine rather than scandalous, describing it as "comparable to error rates in other major ML benchmarks like ImageNet" — the dataset that helped launch the modern deep-learning era and which carried its own well-documented label errors for years. Notably, early human quality reviews had flagged something closer to 1 in 20 problems as needing fixes. It was a later AI-assisted audit that surfaced the much higher rate of small but critical slips across the set — a detail that says as much about how good models have become at scrutinizing hard math as it does about the original errors.

These were not mistakes a casual reader could catch. The problems were authored to sit past the edge of human expertise.

> "The first thing to understand about FrontierMath is that it's genuinely extremely hard. Almost everyone on Earth would score approximately 0%, even if they're given a full day to solve each problem."

— Matthew Barnett, AI researcher

## Why the scores went up — and rankings held

The most analytically useful line in Epoch's release is its own framing of the results: model rankings on v2 are similar, but scores are higher across the board. Read carefully, that tells you what kind of errors the audit found. Had the corrections simply removed easy problems or added harder ones, scores would have fallen. Instead they rose — which points to a benchmark that had been marking correct answers as wrong.

The clearest illustration is the same model measured before and after the fix. GPT-5.5 in its high-effort mode scored roughly 35% on Tier 4 against the uncorrected set; on v2 the same model scores about 72.5%. A near-doubling on an unchanged model is not a capability leap. It is the benchmark no longer penalizing the model for answers it had right all along. Google's AI co-mathematician saw a similar jump, though its earlier figure was achieved without the compute caps applied to other models, making it not strictly comparable.

That pattern is the genuinely reassuring finding. A benchmark can carry a high error rate and still be useful for ranking models, provided the errors hit all of them proportionally. What it cannot support is confident claims about absolute capability. "The model solves 35% of the hardest math problems" was simply the wrong number, and no amount of hedging would have rescued it.

## The controversy that invited the scrutiny

FrontierMath did not arrive uncontested, and that history is hard to separate from why it now faces such close inspection. OpenAI funded the benchmark's development and had access to most of the dataset — all but a holdout set — under what Epoch described as a verbal agreement not to use it for training. The arrangement became a flashpoint in December 2024, when OpenAI reported roughly 25% on the benchmark with its o3 model. Several mathematicians who had contributed problems said they were unaware at the time of OpenAI's funding or its level of access, and some indicated they were not sure they would have participated had they known.

Epoch's then-defense leaned on the verbal training agreement and a separate holdout set for independent verification. It later built in structural safeguards, holding back a portion of Tier 4 problems from OpenAI so that some slice of the test always stays uncontaminated. It is reasonable to draw a line from that contested launch through to the v2 audit: public scrutiny of a high-profile benchmark tends to invite exactly the kind of close inspection that surfaces a 42% error rate. A benchmark that publishes its own error rate, names the correction, and survives the version change with stable rankings is, paradoxically, more trustworthy after the audit than before it.

## Why a rebuilt hard-math benchmark matters

The stakes extend well past the math-benchmark community. Engineering teams pick models, justify budgets, and ship architectures partly on numbers like these. If the underlying test carried a 42% error rate, the procurement signal it sent was noisier than anyone treating those scores as ground truth assumed. The correction did not change who was winning; it changed how much confidence the numbers deserved.

It also reframes a remarkable trajectory. At FrontierMath's launch in November 2024, all six models evaluated solved fewer than 2% of problems. Today's top scores sit near 88% on the hardest tier — a more-than-fortyfold improvement in well under two years. That pace is precisely why Epoch expects the benchmark's useful life to be short.

> "There are easier math benchmarks that are already obsolete, several generations of them. FrontierMath will probably saturate within the next two years — could be faster."

— Greg Burnham, Senior Researcher at Epoch AI

## What to watch

Two threads are worth tracking. The first is saturation: if Fable 5 is already near 88% on Tier 4, the headroom Epoch built into its hardest tier is closing fast, and the organization will need a harder successor or new tiers to keep the benchmark diagnostic. The second is governance. The v2 audit is a useful template — publish the error rate, name the corrections, show that rankings survive — but it is also a reminder that even painstakingly built evaluations carry measurable error. The durable lesson for anyone reading a leaderboard is to treat every score as a claim with a provenance: which version, which effort setting, who ran the eval, and whether the ordering holds when the test is fixed. FrontierMath v2 is the case study for why each of those questions matters.
