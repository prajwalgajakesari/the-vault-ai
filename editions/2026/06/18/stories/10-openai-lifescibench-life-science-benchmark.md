# OpenAI's LifeSciBench Grades AI on Real Life-Science Research — and the Best Model Passes Just 36%

When OpenAI handed its most capable models a stack of 750 research problems written by working biotech and pharma scientists — the kind of messy, multi-step questions a lab actually wrestles with — the best system in the world cleared barely a third of them.

That is the headline finding of **LifeSciBench**, a benchmark OpenAI released on June 17, 2026, built to measure how well AI supports real-world life-science research rather than how well it answers tidy textbook questions. The top scorer, OpenAI's own GPT-Rosalind, passed **36.1%** of tasks. Every other model tested did worse. Put plainly, nearly two of every three research-grade tasks still defeat the most advanced AI available.

It is an unusually candid result for a lab that more often markets near-saturated scores, and it reframes a question the industry tends to skate past: not whether a model can recall biology, but whether it can do the judgment-heavy work of science.

## What LifeSciBench Actually Measures

The benchmark was developed with **173 PhD-level scientists** drawn from biotechnology and pharmaceutical research, many of them active in drug-discovery programs. Together they authored 750 tasks spanning seven research workflows — evidence handling and analysis, design and optimization, scientific reasoning, validation and operations, translation, and scientific communication — across seven biological domains running from genomics to medicinal chemistry to clinical and translational science.

What sets it apart from earlier AI-for-biology evaluations is the refusal to use multiple-choice questions with clean reference answers. LifeSciBench tasks are free-response. Each is graded against a detailed, task-specific rubric averaging **25 criteria** — roughly 19,020 grading criteria in total — that break an expected answer into discrete scientific claims, calculations, decisions, justifications, and caveats. A model does not get credit for landing near the right answer; it has to demonstrate the reasoning a reviewer would expect from a competent scientist.

The tasks are deliberately hard. **79%** require multiple reasoning or decision steps, averaging about four steps each. And they are not text-only: the benchmark ships with **1,062 attached artifacts** — figures, PDFs, tables, sequence and structure files, chemical files, and web references — with over half the tasks requiring a model to interpret or synthesize information from those materials.

## The Numbers Behind the Headline

GPT-Rosalind's 36.1% topped a field that fell off sharply behind it. According to results reported by MarkTechPost, GPT-5.5 reached 25.7%, Gemini 3.1 Pro scored 23.6%, GPT-5.4 hit 20.7%, and Grok 4.3 trailed at 13.0%.

The most revealing split is internal to the leader. GPT-Rosalind passed **45.1%** of text-only tasks but just **28.1%** of tasks that came with attached data files — a 17-percentage-point collapse the moment the work resembled real research, where the answer lives inside a figure, a chromatogram, or a sequence file rather than in the prompt. That gap is arguably the benchmark's sharpest signal: today's models are markedly weaker precisely where lab work concentrates.

OpenAI also invested heavily in making the grading trustworthy. Accepted tasks averaged six automated review cycles and at least two rounds of expert review, with at least 90% agreement among reviewers in the relevant domain. A separate cohort of **453 independent expert reviewers**, predominantly PhD holders, validated that the tasks reflect genuine research and meaningfully test scientific reasoning rather than trivia recall.

## Why Scientific Judgment Is So Hard

The design choices read as an argument about what AI benchmarks have been missing. As OpenAI framed it, scientists spend their days analyzing conflicting evidence, interpreting incomplete datasets, designing experiments under uncertainty, troubleshooting failed assays, weighing risks, and communicating findings — work that demands judgment and domain expertise that conventional benchmarks rarely capture.

A multiple-choice biology test can be aced by a model that has memorized the literature. It says little about whether that model can reconcile two contradictory Western blots, decide which follow-up experiment is worth the reagents, or flag the caveat that would stop a researcher from over-interpreting a noisy result. LifeSciBench's rubric-graded, artifact-laden format is built to reward exactly that kind of reasoning — and the low scores suggest the models are not there yet.

One reading of the 36.1% figure, echoed in early coverage, is reassuringly concrete: a model that passes roughly a third of expert-designed research tasks can meaningfully assist a skilled scientist, but it cannot replace the human judgment required to safely interpret what it produces. In a domain where a confidently wrong answer can send a drug program down a dead end, the gap between "useful assistant" and "trusted colleague" is the whole story.

## The Gap Between Benchmark Hype and the Bench

LifeSciBench lands at a moment when AI labs routinely tout scores in the 80s and 90s on coding, math, and reasoning evals. Against that backdrop, a flagship model topping out at 36% on the work it is increasingly marketed for is a useful corrective. The benchmarks the industry leans on for headlines have, in many cases, been saturated; the messy, multimodal, judgment-dependent reality of research has not.

There is an obvious caveat: OpenAI built the benchmark, and its own model leads it. A company releasing an eval that its top system "wins" while still failing most of the time is making a more interesting bet than a simple victory lap — it is staking out the frontier it intends to climb, and inviting rivals onto a battlefield where everyone currently looks weak. The breadth of independent expert validation makes the tasks harder to dismiss as a home-field construction, but the field would still benefit from third-party labs running their own models against it and from OpenAI publishing the full methodology and, ideally, the tasks.

## What to Watch

The first thing to track is movement on the data-file tasks. If models close the 45-to-28 gap between text and attached artifacts, it will signal real progress on the multimodal, figure-reading skills that lab work actually requires — and not just better prose. The second is whether competitors publish LifeSciBench results of their own, or whether the benchmark stays an OpenAI showcase. And the third is whether any lab can push past the mid-30s at all in the coming year. A jump into the 50s would suggest AI is genuinely encroaching on scientific judgment; another year stalled near a third would suggest that the hardest part of science — knowing what an ambiguous result means and what to do next — remains stubbornly human.
