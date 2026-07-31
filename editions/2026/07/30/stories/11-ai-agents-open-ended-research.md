# Can AI Agents Do Open-Ended Science? New Case Studies Offer Early Evidence

For years, the case that AI is about to accelerate its own development has rested on a specific bet: that AI agents will eventually take over the research that improves AI systems, kicking off a feedback loop that compresses decades of progress into a handful of years. A paper posted to arXiv on July 29, 2026 tries to put that bet to an unusually honest test — and the early answer is a qualified no.

The study, "Can AI agents conduct open-ended AI research? Early evidence from two case studies," was led by researchers including Sayash Kapoor and Arvind Narayanan of Princeton, the pair behind the book *AI Snake Oil*. Its more than twenty co-authors span Georgetown's Center for Security and Emerging Technology, Johns Hopkins, Stanford, and the UK AI Security Institute, among others. The paper is part of a project the group calls CRUX, and it climbed to the top of arXiv's cs.AI daily listing within hours of publication.

## What the researchers actually did

The team's central complaint is that existing ways of measuring AI research ability are broken in opposite directions. Benchmarks with known answers — the paper cites a lineage that includes PaperBench, EXP-Bench, and MLR-Bench — can be graded automatically but are, in the authors' framing, easy to optimize toward without acquiring the underlying skill. Submitting AI-generated papers to blind peer review, the other common approach, is described as "overstretched, stochastic," and prone to poor review quality.

Their proposed "third way" is what they call a shadow evaluation. An AI agent is handed the central, open-ended research question of a genuinely unpublished, high-quality paper, given the tools and data a researcher would normally have, and then graded by the paper's original authors — the only people positioned to judge work on a question whose answer is not yet known.

The researchers ran this on two unpublished NeurIPS 2026 submissions. They gave frontier agents six days and thousands of dollars of compute per run to make progress on the real research question behind each paper.

## What the case studies found

According to the abstract, the agents "completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions." Both attempts were, in the authors' words, "unambiguously rejected" by the original scientists who graded them.

The paper catalogs five recurring failure modes: poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift. A robustness check using a second model and a different scaffold reproduced the same failures, suggesting the problems are not idiosyncratic to one system. The team says it is releasing the expert reviews, survey responses, agent repositories, and logs.

The headline conclusion is narrow but pointed: today's agents can handle the engineering of AI research, but stumble on the critical, judgment-heavy parts of the research lifecycle.

## Why It Matters

The stakes here are less about a leaderboard than about which forecasts of AI progress deserve to be taken seriously. Scenarios in which AI recursively improves itself depend on the premise that agents can conduct open-ended research, not merely grind out well-specified tasks. This paper is an attempt to test that premise directly rather than infer it from benchmark scores.

It also sharpens a long-running worry about evaluation itself. Any task precise enough to grade automatically is, the authors argue, precise enough to optimize for — an echo of Goodhart's law, in which a measure stops being useful the moment it becomes a target. That critique reframes a wave of prior "AI Scientist"-style work, from automated experiment pipelines to research benchmarks, as informative about engineering competence but potentially misleading about genuine scientific capability. For comparison, the University of Michigan's EXP-Bench found that agents completed fully executable research experiments just 0.5% of the time even on tasks with known answers.

Finally, the makeup of the author list signals that this is being positioned as a governance instrument as much as an academic one. Co-authors include Helen Toner of Georgetown CSET and Gillian Hadfield of Johns Hopkins, both prominent in AI policy — a hint that independent, lab-external measures of research capability are seen as inputs to regulation, not just science.

## What to Watch

The obvious caveat is scale. Two case studies are not a body of evidence, and the authors say as much. Shadow evaluations trade the reproducibility and model-ranking power of benchmarks for realism: run-to-run variability on such open-ended tasks may exceed the gap between two capable models, and the method demands scarce expert graders. Whether this small-sample design can accumulate into a trustworthy signal is itself an open question.

The team plans to keep testing. Reporting on the CRUX project indicates it intends to release new evaluations every one to two months, which would slowly build the kind of longitudinal record that a single snapshot cannot provide. Watch, too, for whether frontier labs adopt or resist author-graded evaluation, and whether the five failure modes identified here prove durable or start to close as models improve. If agents begin making real headway on genuinely unresolved questions, that would be a far more meaningful milestone than another saturated benchmark — and this framework is built to notice it.
