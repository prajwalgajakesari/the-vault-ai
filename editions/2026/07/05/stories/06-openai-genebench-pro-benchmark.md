OpenAI has built a test its own best model flunks. On June 30, the company released GeneBench-Pro, a research-level benchmark that confronts AI agents with the messy, judgment-heavy analysis real computational biologists perform daily — and reported that its strongest model, GPT-5.6 Sol, solved fewer than one in three problems, even at maximum compute.

The benchmark comprises 129 problems spanning ten domains of computational biology, from statistical genetics and cancer somatic genomics to clinical pharmacogenomics and forensic genetics. Each pairs a realistic, deliberately noisy dataset with a target estimand tied to a downstream scientific or clinical decision. Reviewers estimated that a single problem would take a human expert 20 to 40 hours to complete.

The scores are humbling. GPT-5.6 Sol reached a 28.7% pass rate at its highest reasoning level, rising to 31.5% with Pro mode enabled. Anthropic's Claude Opus 4.8 managed 16.0%, the best result among non-OpenAI models, while Gemini 3.5 Flash trailed at 8.1%. When OpenAI first built the original, easier GeneBench, its best frontier model, GPT-5, scored below 5%. The climb is real — but roughly 70% of problems remain beyond the reliable reach of today's most capable systems.

## What the Benchmark Actually Measures

What GeneBench-Pro probes is not knowledge retrieval but what OpenAI calls "research taste": the chain of judgment calls that shape an analysis — which questions a dataset can support, when early warning signs should change your model, and when the initial plan should be thrown out. An agent must explore the data, catch quality-control problems like mislabeled samples, ancestry swaps, or ancient-DNA biases, choose an appropriate analytical approach, iterate when early results suggest the plan was wrong, and deliver a numerical answer.

Because every problem is generated synthetically from a fully known causal structure, correctness is graded deterministically against a verified ground truth — sidestepping the rubric variability that weakens many long-horizon science benchmarks. OpenAI sent 82 of the 129 problems to external domain experts, from graduate students to professors, to confirm realism.

Those experts pinpointed a consistent failure pattern the paper calls the "noticing-to-acting gap." Models frequently flag a local diagnostic signal — an artifact, a confounder, a QC failure — but fail to propagate that observation into the correct downstream decision. "It seemed like most of the agents failed on [data discrepancies, such as ancestry swaps]," said Lex Flagel, Director of Data Science at Gencove. "They aren't cautious enough about data issues. Maybe that highlights a weakness of current models. And a lot of biological data has irregularities."

The difficulty is genuine. Alexander Strudwick Young, an assistant professor in human genetics at UCLA, said the problems would have been challenging even for a graduate student to complete without iterated feedback from an experienced supervisor — requiring thoughtful analysis and awareness of pitfalls rather than an off-the-shelf method.

## An Arms Race in Lab Coats

GeneBench-Pro did not arrive in a vacuum. The same day, Anthropic launched Claude Science, an AI workbench wired to more than 60 curated scientific databases across genomics, proteomics, and cheminformatics, with a coordinating agent and a reviewer agent that checks citations and calculations. It follows days behind Anthropic's VirBench, opening what observers are already calling a biology benchmark arms race.

The split reveals two strategies aimed at the same target. Anthropic is shipping a product for daily lab use and betting on integrated engineering. OpenAI is trying to define the standard for what good AI-for-science looks like, publishing benchmarks and dedicated models. "One company shipped a tool for scientists to use today," as one account of the dual release put it. "The other built a yardstick for how far the technology still has to go."

## Why It Matters

Benchmarks have quietly become the competitive battleground of frontier AI. As models converge on saturated tests for coding and math, whoever owns the yardstick shapes the narrative of progress — and GeneBench-Pro lets OpenAI plant a flag in high-value scientific territory while foregrounding its own model's lead. But the more consequential story is the judgment gap. The results suggest today's agents can retrieve methods but cannot yet be trusted to decide which method the data demands, the exact capability that separates an assistant from an autonomous scientist. That distinction matters enormously in genomics and drug discovery, where a confidently wrong analysis is worse than no analysis at all.

The economics still push toward adoption. A problem that costs thousands of dollars in expert labor runs a few dollars in inference, so even partial automation — an agent handling what it can and escalating the rest — could reshape research pipelines.

## What to Watch

OpenAI is providing a 50-question subset to Artificial Analysis for independent benchmarking; until those results land, the leaderboard reflects internal evaluation by the same firm that built both the test and its winning model. Watch, too, whether OpenAI's prediction that GeneBench-Pro could be saturated by the end of 2026 holds — and whether Anthropic, Google, and fast-rising Chinese labs answer with benchmarks of their own.