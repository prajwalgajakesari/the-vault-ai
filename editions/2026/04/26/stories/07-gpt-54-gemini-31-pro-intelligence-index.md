# GPT-5.4 and Gemini 3.1 Pro Tie for Top Spot on Artificial Analysis Intelligence Index

The AI benchmarking race just produced its most dramatic photo finish yet. As of April 18, GPT-5.4 (xhigh) and Google's Gemini 3.1 Pro Preview are tied at exactly 57 on the Artificial Analysis Intelligence Index v4.0 -- the most widely cited composite leaderboard for frontier AI models. Anthropic's Claude Opus 4.7 joins them at the same score, making it a three-way deadlock at the top of the 356-model index. But underneath that single number, each model wins a different race, and the implications for developers, enterprises, and the broader AI industry are anything but tied.

The Intelligence Index, now in its fourth major revision (v4.0.4, patched March 2026), aggregates performance across 10 evaluations spanning four equal-weighted categories: Agents, Coding, General Knowledge, and Scientific Reasoning. Each category contributes 25 percent to the final composite. The evaluations include GDPval-AA, tau-squared-Bench Telecom, Terminal-Bench Hard, SciCode, AA-LCR, AA-Omniscience, IFBench, Humanity's Last Exam, GPQA Diamond, and CritPt. The index publishes its composite with a sub-plus-or-minus-one-percent confidence interval, which means the three-way tie is effectively within noise -- statistically, no single model can claim an outright lead.

That has not stopped each lab from claiming victory in its own backyard.

## Where GPT-5.4 Leads

OpenAI's GPT-5.4, released March 5, dominates knowledge work and coding. It scores 83 percent on GDPval-AA, which Artificial Analysis describes as above human expert level, and ranks second overall out of 106 models on BenchLM's composite. On SWE-bench Verified, the gold-standard test for real-world software engineering, GPT-5.4 scores 71.7 percent -- an eight-point gap over Gemini 3.1 Pro's 63.8 percent, meaning it resolves roughly one in eight more real-world GitHub issues correctly. Perhaps most notably, GPT-5.4 is the first model to surpass the human baseline on OSWorld, scoring 75 percent on desktop automation tasks against a 72.4 percent human benchmark. For developers building agentic workflows that require a model to operate software interfaces, that milestone matters.

## Where Gemini 3.1 Pro Leads

Google's entry takes a different crown. On GPQA Diamond, the graduate-level science reasoning benchmark, Gemini 3.1 Pro scores 94.3 percent -- 1.5 points ahead of GPT-5.4's 92.8 percent. On ARC-AGI-2, the abstract reasoning test designed to resist memorization, Gemini leads 77.1 percent to 73.3 percent. Its multimodal capabilities are even further ahead: on Video-MME, Gemini posts 78.2 percent versus the next-best model at 71.4 percent. Add a two-million-token context window -- double GPT-5.4's one-million-token limit -- and Gemini 3.1 Pro becomes the clear pick for researchers processing long scientific papers, video analysis, and multi-document synthesis.

## The Pricing Gap

Cost compounds the strategic difference. Gemini 3.1 Pro is priced at $2.00 per million input tokens and $12.00 per million output tokens. GPT-5.4 costs $2.50 and $15.00, respectively. For high-volume inference workloads, that 20-to-25-percent discount adds up. And the equation shifted further on April 23, when OpenAI released GPT-5.5, which broke the three-way tie by scoring 60 on the Intelligence Index -- three points clear -- but at $5.00 and $30.00 per million tokens, more than doubling GPT-5.4's cost. The result is a new tiering: GPT-5.5 for maximum capability at premium pricing, GPT-5.4 for the best balance of performance and cost, and Gemini 3.1 Pro for budget-conscious deployments that prioritize reasoning and science.

## Three Labs, Three Profiles

The convergence at 57 obscures what Artificial Analysis has called fundamentally different model profiles. Claude Opus 4.7 matches the other two on composite score but takes yet a third path -- its hallucination rate on AA-Omniscience sits at 36 percent, compared to 50 percent for Gemini 3.1 Pro and a striking 86 percent for GPT-5.5 (which answers confidently even when wrong). For enterprise deployments where factual reliability outweighs raw benchmark performance, that gap is significant.

The broader pattern is unprecedented convergence at the frontier. Three models from three different labs, built on different architectures, trained on different data, all landing on the same composite score. As the SmartChunks analysis noted, "these are within noise more than these three are tied at the top" -- a reminder that single-number rankings can flatten meaningful distinctions into false equivalences.

## Why This Matters

For developers and enterprises choosing a foundation model, the tie is both clarifying and complicating. It is clarifying because it confirms there is no single best model -- the right choice depends on the workload. Coding-heavy agentic pipelines favor GPT-5.4. Scientific research and long-context analysis favor Gemini 3.1 Pro. Applications demanding low hallucination rates favor Claude Opus 4.7. It is complicating because multi-model strategies -- routing different tasks to different providers -- add architectural complexity, vendor management overhead, and latency variability that most engineering teams are not yet equipped to handle.

## What to Watch Next

The three-way tie lasted five days before GPT-5.5 disrupted it. The next version of the Intelligence Index (v4.1) is expected to add agentic evaluation weight, which could reshuffle the leaderboard again. Google has signaled that Gemini 3.1 Pro will exit preview status in the coming weeks, and Anthropic's next model update is widely expected before mid-year. In the meantime, the April 2026 snapshot will be remembered as the moment the frontier became a plateau -- and the competition shifted from who is smartest to who is smartest at what.
