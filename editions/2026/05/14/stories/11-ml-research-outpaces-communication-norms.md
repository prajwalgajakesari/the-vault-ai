---
headline: "Machine Learning Research Has Outpaced Its Communication Norms"
slug: ml-research-outpaces-communication-norms
category: research
story_number: "11"
---

# Machine Learning Research Has Outpaced Its Communication Norms

The machine learning research community has a writing problem. Papers are getting harder to read, acronyms are multiplying faster than the models they describe, and the venues that once set the standard for scientific communication are struggling to keep pace with a field that has grown fifty-fold in under four decades. A new study analyzing millions of papers argues the flagship conference NeurIPS needs to intervene — before the field's own literature becomes unintelligible to the researchers producing it.

The paper, published on arXiv on May 9 by Ajay Mandyam Rangarajan and Jeyashree Krishnan, represents one of the most comprehensive quantitative audits of ML research writing ever conducted. The authors analyzed 2.8 million arXiv papers spanning 1991 to 2025, 24,772 NeurIPS papers from 1987 to 2024, and 24.5 million PubMed papers from 1990 to 2025, applying classical readability metrics, sensational language detection, acronym analysis, LLM-based readability scoring, and citation data from OpenAlex and Semantic Scholar.

The findings are stark. Flesch Reading Ease scores for NeurIPS abstracts have dropped from roughly 24 in 1987 to 13 in 2024 — a decline that pushes the field's flagship venue deep into territory that readability researchers classify as requiring specialized postgraduate training to parse. For context, scientific writing already trends toward the difficult end of any readability scale, and NeurIPS abstracts are getting harder even by that standard.

## The Acronym Epidemic

Perhaps the most vivid finding concerns the explosion of acronyms. Acronym density in NeurIPS titles has surged nearly tenfold, from 0.33 per 100 words in 1987 to 3.21 in 2024. Worse, roughly 89 percent of acronyms appearing in NeurIPS papers are used fewer than ten times across the entire corpus — ten percentage points above the science-wide baseline. The field is not just producing jargon; it is producing disposable jargon, shorthand that serves the authors of a single paper and no one else.

Sensational language has risen by approximately 50 percent in NeurIPS abstracts between 2015 and 2024, a trend that mirrors broader concerns about hype in AI research. The combination of decreasing readability and increasing sensationalism creates a peculiar dynamic: papers are simultaneously harder to understand and more breathless in their claims.

## Readability Correlates with Impact

The study's most provocative finding may be its simplest. More readable NeurIPS papers tend to receive more citations. The correlation suggests that clarity is not merely a stylistic preference but a measurable determinant of research impact. Papers that cannot be easily understood risk being siloed — read by the narrow subcommunity that shares the authors' specific vocabulary and ignored by everyone else.

"Is the target reader a human or an LLM?" Rangarajan and Krishnan pose the question directly in their analysis. Their LLM-based readability scores rated NeurIPS abstracts as roughly stable from 1987 to 2022, with early signs of improvement afterward — a pattern that contradicts every classical readability metric designed for human comprehension. The divergence raises an uncomfortable question for a field increasingly reliant on automated tools for reviewing, summarizing, and synthesizing research.

## A Field Under Structural Strain

The communication crisis does not exist in isolation. NeurIPS received 21,575 valid submissions in 2025, a 61 percent increase over 2024's 15,671 main-track papers. The conference that once received a few hundred submissions per year now processes tens of thousands, placing extraordinary pressure on volunteer reviewers who must read and evaluate work across an ever-widening array of subfields.

The broader ML conference ecosystem is feeling the strain. ICML 2026 introduced its most stringent policies yet, including a two-tier framework governing LLM use in peer review. Under the new system, authors and reviewers choose between a conservative policy that prohibits LLMs entirely and a permissive policy that allows limited AI assistance for comprehension and polishing but bans AI-generated evaluations. The conference detected 795 policy violations — roughly one percent of all reviews — using watermarking techniques embedded in submission PDFs. NeurIPS itself elevated reproducibility to a first-class research activity in May, announcing that the Machine Learning Reproducibility Challenge would become an official conference track for the first time at NeurIPS 2026 in Sydney.

## Seven Standards for NeurIPS 2027

Rangarajan and Krishnan propose seven concrete standards NeurIPS could pilot beginning in 2027: an acronym budget paired with a venue-approved term list, a human readability threshold for accepted papers, stricter citation standards, requirements for standalone visual elements, mandatory plain language summaries, a pre-registered acronym glossary, and open-source audit tooling that would allow authors to check compliance before submission.

The proposals are deliberately incremental. The authors are not calling for a revolution in how ML research is written — they are arguing that a field producing roughly 50 times more papers than it did in the late 1980s needs explicit, enforceable norms that match its current scale. The alternative is a literature that grows increasingly opaque even to its own practitioners, where the gap between what is published and what is understood widens with every conference cycle.

Whether NeurIPS will act remains an open question. But the data makes the case difficult to dismiss: the field's communication infrastructure was built for a different era, and the cracks are no longer subtle.
