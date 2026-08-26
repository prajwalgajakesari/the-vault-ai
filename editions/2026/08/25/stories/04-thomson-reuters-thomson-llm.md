Thomson Reuters spent about $40 million over two years to build its own large language model. The number it wants the industry to sit with is far smaller: roughly $450,000, the cost of the final training run that produced the model it launched on August 24.

The model is called Thomson — formally Thomson 1.0 — and it is the first proprietary LLM in the 175-year history of the Toronto-based content and technology group. It was not built from scratch: Thomson Reuters started from an open-source foundation, most recently Alibaba's Qwen 3.5, then mid-trained and post-trained it on decades of proprietary material from Westlaw, Practical Law, Checkpoint and Reuters, with hundreds of in-house lawyers and tax professionals shaping the training objectives and grading the outputs. The result, the company says, is a specialist that competes with models that cost several orders of magnitude more to produce.

“For years, the AI industry has treated scale as the answer: bigger models, more compute, more money. Thomson shows there is another path,” said Joel Hron, chief technology officer at Thomson Reuters, in the launch announcement. “Start with a strong foundation, specialize it deeply for the work that matters, and you can build intelligence that is highly capable, far more efficient and entirely under your control. We think that changes the economics of professional AI.”

## The $450,000 line item

The $40 million figure covers talent and compute across the full program, which traces back to Thomson Reuters' 2024 acquisition of the UK AI startup Safe Sign Technologies. The $450,000 is narrower and more provocative: it is what it cost, in compute, to run the final training pass on the version shipping now. Hron disclosed it during a press briefing ahead of the launch.

“This $450,000 number I think is indicative of what we were able to do with our data and content on top of world-class open source models,” Hron said.

That framing matters because the open-source starting point is disposable by design. Hron said the team has swapped its base model “close to a half dozen times” as better open weights appeared. Jonathan Schwarz, Thomson Reuters' head of foundational research, argued the durable asset is the pipeline, not the checkpoint: “The bigger finding here is less the individual model and more the model factory we built.”

Thomson's first production job is Tabular Analysis in the next release of CoCounsel Legal, a feature that reviews up to 10,000 documents against up to 100 questions at once and returns a filterable table with every answer traceable to source. Thomson will be the default model there, though administrators can switch it out. CoCounsel stays multi-model, still routing other work to OpenAI, Anthropic and Google systems.

## The benchmark picture, with caveats

Thomson Reuters says Thomson performed competitively with Claude Opus 4.8 and ahead of GPT-5.5, Claude Sonnet 5 and Gemini 3.1 Pro across its evaluation suite, which spans more than 100 legal-domain benchmarks. Its headline result is a 0.352 top score on PrBench Legal Hard, which the company says leads every frontier model it tested.

The fuller picture is more mixed, and Thomson Reuters published enough to see it. The model trails Gemini 3.1 Pro and GPT-5.5 on Stanford's LegalBench, sits just behind Opus 4.8 on the Harvey Legal Agent Benchmark, and falls off sharply on coding. On its internal Deep Research benchmark, Thomson scored 0.53 on factuality with web access only against 0.65 for a GPT-5 series comparator, and pulled ahead 0.83 to 0.82 only once both could query Thomson Reuters content.

Andrew Bean, who leads evaluations, was candid about the web-only result: Thomson was “within the scope of the other models, but certainly not the leader yet.” The uplift, he said, “comes from being able to train on and practice with your own tools.” Independent validation is pending; the company has begun handing the model to academics and is releasing a small open-weight variant on Hugging Face under a non-commercial academic license.

## Why It Matters

This is the clearest data point yet for a thesis that has been circulating for a year: vertical incumbents do not need to buy frontier API tokens forever. They need three things — an exclusive corpus, a standing army of experts who can generate preference data and judge outputs, and workflows where quality is objectively measurable. Thomson Reuters has all three. Westlaw alone spans more than 40,000 databases and 150 years of editorial curation.

The economics follow. High-volume, structured work like document review is where per-token frontier pricing hurts most and where a smaller specialist pays for itself. Owning the model also turns product work into compounding capital: every expert review becomes training data, which Hron likened to “renting a house versus buying a house.” Rented intelligence leaves that value at the provider.

The caution is that the moat is narrower than the headline suggests. Thomson Reuters' own numbers show a general-purpose model improves nearly as much once given the same content. That is still a moat — the content is proprietary — but it is a licensing moat as much as a modeling one, and the playbook is copyable by any regulated-industry incumbent: post-train open weights on a corpus nobody else can buy.

## What to Watch

Three things. First, the technical report and the academic evaluations now underway at Queen's and Washington University, which will show whether the benchmark claims survive outside scrutiny. Second, whether Thomson takes what Hron predicts will be “a bigger and bigger share of the tokens” inside CoCounsel, or stays parked in one feature. Third, licensing: Thomson Reuters says it is in early talks with large law firms and corporations about direct access, and Hron's line that it “could also become infrastructure for others” is a quiet declaration of war on the very frontier labs whose APIs still run most of CoCounsel. If a legal publisher can build a competitive domain model for $40 million, the question every vertical software company will be asked next quarter is why it hasn't.
