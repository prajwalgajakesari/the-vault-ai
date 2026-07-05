## A frontier model that no one outside Musk's companies can touch

Elon Musk said on June 28 that Grok 4.5 has entered private beta inside SpaceX and Tesla, marking the first deployment of xAI's new 1.5-trillion-parameter V9 foundation model. Writing on X, Musk claimed early internal evaluations show the model performing "close to, perhaps exceeding, Opus" — a reference to Anthropic's flagship Claude tier. The caveat, easy to lose in the announcement's momentum, is that no one outside his companies can currently verify that claim.

As of July 4, there is no public benchmark data for Grok 4.5. The model has not appeared on LMSYS Arena, Artificial Analysis, Humanity's Last Exam, or any other recognized third-party leaderboard, and xAI has not published its own numbers either. The Opus comparison is an internal claim from the company shipping the product. It should be read as marketing until independent testing exists.

## Inside V9, and the Cursor data flywheel

The technical story underneath the beta is a jump in scale. V9 completed training on May 26, 2026, at 1.5 trillion parameters — a roughly 50 percent increase over the approximately 1-trillion-parameter model behind Grok 4.4, which shipped in late May. A smaller v8-small model of around 500 billion parameters currently powers Grok in X production. V9 is the largest foundation model xAI has fielded to date.

What distinguishes Grok 4.5 from a straight scale-up is its training diet. According to reporting corroborated across multiple outlets, xAI added Cursor coding-session data during supplemental training to sharpen the model's coding and technical reasoning. That data comes courtesy of a corporate maneuver as aggressive as the model itself: SpaceX acquired Anysphere, Cursor's parent company, for roughly $60 billion in June 2026. Cursor is one of the most widely used AI coding environments, and its logs of real debugging, refactoring, and architecture decisions are a rich signal for teaching a model how engineers actually work.

Worth noting is a detail one xAI engineer reportedly conceded: because the Cursor data was folded in during supplemental rather than initial training, its benefit is "not quite as good as having it in initial training." That is an unusually candid admission in an announcement otherwise built on superlatives.

## The strategy: monthly models and captive test labs

The more interesting story may be process, not product. Musk said xAI plans to ship a new model "trained completely from scratch" every month through the end of 2026, all based on the V9 foundation. If that holds, xAI would field roughly six independently trained large models in half a year — a research cadence no rival currently attempts. Internally, a harness called "Grok Build" runs daily improvement cycles, and the parallel training is happening on Colossus 2, xAI's roughly 1-gigawatt Memphis supercluster, which reporting suggests is running seven models at once, including 6-trillion- and 10-trillion-parameter Grok 5 variants.

That cadence is only possible because of the second half of the strategy: SpaceX and Tesla are the test bed. Rather than open a public beta, Musk is using his own companies as controlled evaluation environments, where employees exercise the model against real coding, engineering, and manufacturing problems. It is a shrewd arrangement. Musk gets high-signal feedback from demanding technical users, a captive dataset for the next training run, and total control over what leaks. Grok 4.5 and 4.4 look, in this framing, less like finished products than like infrastructure rehearsals — proving out inference pipelines before the far larger Grok 5 arrives.

The cost is transparency. A model tuned and judged inside the same organization that builds it, on data that same organization owns, evaluated on evals that same organization designs, is a closed loop. It can genuinely improve fast. It can also drift toward the benchmarks its makers happen to care about, and no one outside would know.

## What to watch

The single thing worth watching is whether Grok 4.5 ever faces an independent benchmark. Until it appears on a neutral leaderboard or is tested by researchers with no stake in the outcome, "close to, perhaps exceeding, Opus" remains an assertion, not a result. Musk has a documented history of ambitious timelines, and "perhaps" is doing considerable work in that sentence.

Second, watch the monthly cadence. Shipping a from-scratch frontier model every month is a staggering claim; whether xAI actually delivers distinct, improved models on that schedule — or quietly relabels checkpoints — will reveal how much of this is engineering and how much is narrative. And third, watch Grok 5. If the 4.x line is scaffolding for a 6-to-10-trillion-parameter model on Colossus 2, the private beta at SpaceX and Tesla is best understood not as the headline but as the warm-up act.
