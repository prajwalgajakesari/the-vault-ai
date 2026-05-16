---
headline: "Microsoft Benchmark Reveals AI Agents Corrupt Up to 25 Percent of Documents in Extended Workflows"
slug: microsoft-delegate-52-agent-corruption
category: research
story_number: "09"
date: 2026-05-15
---

# Microsoft Benchmark Reveals AI Agents Corrupt Up to 25 Percent of Documents in Extended Workflows

The AI industry has spent the past year selling a vision of autonomous agents that handle complex knowledge work while you sleep. Microsoft Research just stress-tested that promise across 52 professional domains, and the results should give every enterprise buyer pause: even the best frontier models silently corrupt roughly a quarter of document content when left to manage extended editing workflows on their own.

The findings come from DELEGATE-52, a new benchmark introduced in an April 17 preprint by Microsoft researchers Philippe Laban, Tobias Schnabel, and Jennifer Neville. The benchmark simulates the kind of long-horizon delegated work that AI vendors are aggressively marketing to enterprises: multi-step document editing chains spanning domains as diverse as Python programming, crystallography notation, music composition, and legal drafting. Each simulation runs a document through 20 sequential AI interactions, asking the model to perform a structural edit and then reverse it, chaining these round-trips to approximate the cumulative wear of real-world agent workflows.

The headline numbers are stark. Frontier models, including Google Gemini 3.1 Pro, Anthropic Claude 4.6 Opus, and OpenAI GPT-5.4, degraded document content by an average of 25 percent by the end of these chains. Weaker models fared far worse, with average degradation across all 19 tested models reaching 50 percent. The researchers define "catastrophic corruption" as a benchmark score of 80 percent or less, and found that threshold was breached in more than 80 percent of all model-domain combinations tested.

"Current LLMs are unreliable delegates: they introduce sparse but severe errors that silently corrupt documents, compounding over long interaction," the researchers wrote. The word "silently" carries particular weight. Weaker models tended toward obvious content deletion, but frontier systems produced a more insidious failure mode: documents that appeared superficially coherent while their meaning had quietly shifted. A polished paragraph that changes a clause, a date, or a number can survive long enough to shape later revisions, pass through approval chains, and reach customers or regulators before anyone notices the drift.

Gemini 3.1 Pro posted the highest overall score at 80.9 percent after 20 interactions. Claude 4.6 Opus followed at 73.1 percent, and GPT-5.4 came in at 71.5 percent. But even Gemini's top ranking obscures a more uncomfortable truth: the model cleared the researchers' readiness threshold in only 11 of 52 professional domains. The remaining 41 domains, the vast majority of specialized professional work, remain territory where no current model can be trusted to operate without close human supervision.

Perhaps the most counterintuitive finding concerns agentic tool use, the very capability that AI companies are now racing to build into their products. The researchers tested four models in an agentic configuration with access to tools like web search and code execution, expecting the additional capabilities to compensate for document degradation. The opposite happened. Models with tool access performed worse than those operating without tools, incurring an average of 6 percent additional degradation by the end of simulation. The tools introduced new failure surfaces without solving the underlying document fidelity problem.

"Current LLMs are ready for delegated workflows in some domains such as Python coding, but not in other less common domains," the paper concludes, adding that "users still need to closely monitor LLM systems as they operate and complete tasks on their behalf." Python was the standout exception, the only domain that consistently cleared readiness thresholds across most models, likely because code represents the data type most heavily represented in LLM training corpora.

## Why This Matters

The root cause points to a fundamental architectural limitation. LLMs are next-token predictors, not structured-revision engines. When asked to edit a document, they regenerate text rather than applying discrete, auditable changes. Each regeneration shifts the model's attention across the full document context, and small perturbations accumulate into compounding corruption over successive interactions. This is not a bug that a better prompt or a larger context window will fix; it is a structural property of how these systems process and produce text.

The timing of the paper is pointed. Microsoft itself is the single largest commercial deployer of AI agents through its Copilot product line, which now reaches hundreds of millions of Office users. Google, Anthropic, and OpenAI are all building agent platforms premised on the assumption that AI can reliably manage multi-step professional workflows. DELEGATE-52 suggests that assumption remains unproven for the majority of professional domains, and that the agentic tooling being layered on top of base models is not solving the problem.

For enterprise buyers, the implication is that review checkpoints, escalation rules, approval chains, and sampling audits cannot yet be eliminated from AI-augmented workflows. Teams may save substantial time on first-pass drafting, but the human verification infrastructure must remain intact. Silent corruption is harder to manage than obvious failure, and the 25 percent degradation figure represents an average that masks far worse outcomes in specific domains.

## What to Watch

The research opens several questions that the industry will need to answer. Can retrieval-augmented generation or structured diff-based editing architectures reduce the compounding corruption that pure generative approaches produce? Will model developers begin optimizing explicitly for document fidelity in long workflows, or will benchmark competition continue to focus on single-turn task performance? And will enterprise buyers recalibrate their deployment timelines for autonomous agents, or will commercial pressure override the caution that DELEGATE-52 recommends? The benchmark code is publicly available on GitHub, so independent verification is possible. The data is clear: the agents are not yet ready to work unsupervised.
