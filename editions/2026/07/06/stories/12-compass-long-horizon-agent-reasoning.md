# COMPASS Tackles the Hardest Problem in AI Agents: Staying Coherent Over Long Horizons

Ask any AI agent to book a flight, and it will manage. Ask it to plan a two-week research trip across a dozen websites, cross-check prices, revise its plan when a hotel falls through, and remember why it made each choice, and it will very likely lose the thread somewhere around step forty. Small errors compound. The model hallucinates a fact it confirmed an hour earlier, gets distracted by a stale search result, and never circles back to fix the mistake that quietly poisoned everything downstream.

That failure mode is the subject of a paper from a team of researchers, several affiliated with Google, that has become one of the more talked-about entries in the agent-reasoning literature since it landed on arXiv on October 9, 2025. Titled "COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving Context," and currently under review for the ACL conference, the work does something refreshingly direct: it names the bottleneck, then builds a system around it.

## The Diagnosis: Context Is the Bottleneck

The authors are blunt about where long-horizon agents break. "Long-horizon tasks that require sustained reasoning and multiple tool interactions remain challenging for LLM agents," they write. "Small errors compound across steps, and even state-of-the-art models often hallucinate or lose coherence."

Their central claim is that the culprit is not raw model capability but the management of the agent's own growing memory. As they put it, "We identify context management as the central bottleneck -- extended histories cause agents to overlook critical evidence or become distracted by irrelevant information, thus failing to replan or reflect from previous mistakes."

This reframes a problem the field has often treated as a matter of scale. The instinct in 2024 and 2025 was to throw longer context windows at the issue: if the agent can hold a million tokens, surely it will not forget. But a bigger window is not the same as a better-organized one. An agent drowning in its own transcript is not helped by being handed a larger bucket. What COMPASS argues is that the history needs to be actively curated as the task unfolds, not merely accumulated.

## The Method: Splitting the Brain Into Three

COMPASS, which stands for Context-Organized Multi-Agent Planning and Strategy System, is described by the authors as a "lightweight hierarchical framework." Rather than asking one model to simultaneously execute, supervise, and remember, it divides those jobs across three specialized components.

The first is a Main Agent that does the actual work: reasoning through the problem and calling tools. The second is a Meta-Thinker, which sits above the Main Agent, monitors progress, and issues what the paper calls "strategic interventions" when the agent appears to be drifting or stuck. The third, and arguably the star of the design, is a Context Manager, which "maintains concise, relevant progress briefs for different reasoning stages."

The division of labor mirrors how a well-run human team operates. One person executes, another watches the strategy, and a third keeps the shared notes clean and current. Critically, the Context Manager is not just summarizing for the record; it is tailoring what the Main Agent sees at each stage so the working memory stays sharp instead of ballooning into noise. This is the "evolving context" of the title: the context is not a static log but a living, pruned artifact.

## The Results

The team evaluated COMPASS on three of the harder benchmarks in the agentic-reasoning world: GAIA, which tests general assistant abilities across multi-step real-world tasks; BrowseComp, a web-browsing benchmark; and Humanity's Last Exam, a notoriously difficult knowledge test. Across all three, the authors report that COMPASS "improves accuracy by up to 20% relative to both single- and multi-agent baselines."

A 20% relative gain is the headline figure, and it is worth being precise about the framing: this is an improvement over baseline agent architectures, not an absolute score, and the paper describes it as an upper bound ("up to"). Readers should treat it as the paper's own reported result pending peer review.

The team also describes two extensions. A test-time scaling variant, they write, "elevates performance to match established DeepResearch agents" -- the class of heavyweight research-oriented systems that have set the bar for autonomous web investigation. And a post-training pipeline "delegates context management to smaller models for enhanced efficiency," suggesting the curation role does not require a frontier-scale model to run and could be offloaded cheaply in production.

## Why This Matters in 2026

The timing is not incidental. Through 2025, the AI industry pivoted hard from chatbots to agents, and the gap between demo and dependability became the defining commercial problem. Agents that dazzle on a five-step task quietly fall apart on the fifty-step ones that actually justify their cost. Enterprises piloting agentic workflows have run into the same wall over and over: coherence decays with horizon length, and no amount of prompt engineering fully patches it.

COMPASS is part of a broader shift toward treating context as an engineered resource rather than a passive buffer -- a discipline some now call context engineering. If the paper's thesis holds, the competitive frontier for agents is moving away from who has the biggest model and toward who manages the agent's attention most intelligently. That is a more architectural, and more tractable, problem than perpetually scaling parameters.

## What to Watch Next

Three things are worth tracking. First, peer review: the paper is still under review for ACL, and independent replication of the up-to-20% figure across labs will determine how durable the result is. Second, the smaller-model context manager -- if a cheap model can reliably do the curation, the approach becomes economically attractive for real deployments, not just benchmarks. Third, whether the three-role decomposition generalizes beyond the research-and-browse benchmarks tested here to messier domains like coding, operations, and multi-day workflows.

For now, COMPASS offers something the agent field has been short on: a clear-eyed diagnosis and a modular, testable fix. The hardest problem in agentic AI is not getting a model to think. It is getting it to keep thinking straight, for a long time, without losing the plot.
