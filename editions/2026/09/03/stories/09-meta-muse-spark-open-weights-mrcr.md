# Meta Says Muse Spark Scores 98.1% at a Million Tokens. The Weights Are Coming, the Paper Is Not.

Mark Zuckerberg promised on X on Wednesday, September 2, that Meta will release an open-weights version of Muse Spark, the model at the top of its lineup, "soon." He did not give a date, a parameter count, a license or a technical report. What he did give the open-model community, in the same day's launch materials for Muse Spark 1.3, was a number: 98.1 on MRCR at context lengths between 512,000 and one million tokens.

That is the figure that lit up r/LocalLLaMA, where the open-weights post drew 530 upvotes and 148 comments, much of it arguing over whether Meta has finally beaten "context rot," the tendency of models to lose the thread of information buried deep in a long input. It is also the figure most worth handling with tongs.

## What Meta Actually Shipped

Muse Spark 1.3 went live on September 2 on Meta's model API and its Muse Code CLI, roughly four weeks after 1.2. It carries a 1M-token context window, accepts text, image and video input, and sits at #6 of 636 models on the Artificial Analysis Intelligence Index. Meta's pitch is behavioral as much as numerical. "Muse Spark 1.3 asks clarifying questions when prompts are ambiguous, invokes help from the user when stuck, and confirms before taking consequential actions," the company wrote in its launch blog post.

Meta's own four-model scorecard put 1.3 at 98.5 on MRCR in the 256K-512K band and 98.1 in the 512K-1M band, against 91.5 and 73.8 for OpenAI's GPT-5.6 Sol. Anthropic's Claude Opus 5 posted no MRCR number at all. On coding, 1.3 took DeepSWE v1.1 at 75.4 and tied GPT-5.6 Sol at 88.8 on Terminal-Bench 2.1. On the six agent benchmarks in Meta's own table, however, Opus 5 beat it on four.

The promise lands on top of a real shipment. On August 10, Meta released Muse Glimmer, a 30-billion-parameter dense model, under an Apache 2.0 license -- a break from the bespoke Llama community license, whose 700-million-monthly-user cap the Open Source Initiative says disqualifies it from the term "open source." Spark is a different animal: currently listed as proprietary, far larger, and by most community estimates well beyond what a 24GB consumer GPU will hold.

## What MRCR Actually Measures

MRCR, or multi-round coreference resolution, was open-sourced by OpenAI as a harder successor to a Google eval. The test builds a long synthetic conversation in which a user repeatedly asks for a piece of writing, hides two, four or eight identical requests inside it, then asks the model to return a specific one: return the second poem about tapirs. It measures whether a model can disambiguate near-identical items scattered across a huge context. It does not measure reasoning, synthesis, or whether a model can usefully hold a real codebase in working memory.

It is also unusually easy to game. The eight-needle variant is dramatically harder than the two- or four-needle version, and Meta's scorecard does not say which it ran -- a distinction that has produced roughly two-to-one score gaps in past vendor materials. And the training signal is cheap. "only including this as a long context benchmark is somewhat misleading since meta likely overfit very hard on it," the AI researcher Elie Bakouch wrote on X, pointing to a Microsoft MAI technical report indicating that on the order of a thousand training samples can move an MRCR score from around 60% to above 90%. Anthropic stopped publishing MRCR results months ago, having concluded the benchmark did not correlate with how customers actually use long context.

The surrounding numbers underline how large a claim 98.1 is. On MRCR v2's eight-needle variant at 1M tokens, Claude Opus 4.6 -- the strongest publicly documented result -- scores 76%. GPT-5.4 scores 36.6%. Gemini 3 Pro scores 26.3%. A jump to 98.1 would not be an improvement. It would be a discontinuity.

A more mundane explanation is available. Meta's scorecard compares 1.3 in its "max" reasoning mode against 1.2 in the faster "xhigh" mode -- different tiers, not a clean generational delta. And max was still gated behind safety testing at launch, so the mode carrying the headline scores was not the one developers could call. "It's kind of dishonest that the benchmark only shows max reasoning," one commenter, sunaookami, wrote on Hacker News.

## Why This Matters

The gap between open weights and the frontier has been closing on capability and widening on evidence. Llama arrived with papers. Glimmer arrived with a permissive license. Spark, so far, is arriving with a scorecard and a promise -- and for an open-weights model, the scorecard is effectively the whole prospectus. Nobody outside Meta can replicate a training run; the license and the eval numbers are all outsiders have. An unaudited, easily-overfit benchmark is a weak foundation for a release this size.

Glimmer was built to run on a laptop. Spark is not. An open-weights model too large for consumer hardware is "open" mainly to people who already rent GPUs at scale, which shifts the release from democratization to price pressure on OpenAI, Anthropic and Google. Meta's contributor endpoint -- roughly $0.10 per million input tokens against $1.25 standard, in exchange for letting Meta train on your traffic -- makes the strategy legible: undercut on price, take data as payment, and make closed-lab margins harder to defend.

The long-context claim is the hinge. If 98.1 survives independent replication, Meta has something genuinely new to hand out, and the reliability race Anthropic has led for a year gets a free entrant. If it is a benchmark artifact, Meta will have released weights whose headline selling point evaporates on contact with real work.

## What To Watch

Four things. Whether Meta publishes the MRCR variant and needle count behind 98.1. Whether independent evaluators reproduce it under standardized settings rather than vendor ones. Whether the release carries Apache 2.0, as Glimmer did, or reverts to a bespoke Meta license. And whether the released checkpoint is the max tier that produced the headline number or the cheaper xhigh tier. Zuckerberg said "soon." Until a date and a needle count arrive, 98.1 is a marketing figure that may well turn out to be true.