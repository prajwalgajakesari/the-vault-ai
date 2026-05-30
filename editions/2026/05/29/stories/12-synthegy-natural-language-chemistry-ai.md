---
headline: "New AI System Synthegy Lets Chemists Plan Reactions Using Natural Language Commands"
slug: synthegy-natural-language-chemistry-ai
category: research
story_number: 12
date: 2026-05-29
author: The Vault AI Edition
sources:
  - name: EPFL News
    url: https://actu.epfl.ch/news/ai-helps-chemists-design-molecules-step-by-step/
  - name: ScienceDaily
    url: https://www.sciencedaily.com/releases/2026/05/260504023844.htm
  - name: Decrypt
    url: https://decrypt.co/367048/ai-chemistry-instructions-build-molecule
  - name: Matter (Cell Press)
    url: https://doi.org/10.1016/j.matt.2026.102812
---

# New AI System Synthegy Lets Chemists Plan Reactions Using Natural Language Commands

*An EPFL-led framework turns plain-English instructions into ranked synthesis strategies, matching expert chemists 71% of the time.*

---

For decades, planning how to build a complex molecule has been one of the most intellectually demanding tasks in all of science. A chemist synthesizing a new drug candidate or advanced material must reason backward from a target molecule through dozens of possible reaction sequences, weighing trade-offs at every step: which bonds to form first, when to protect vulnerable functional groups, and how to avoid dead-end pathways that could waste months of laboratory work. It is a process that has historically required years of accumulated intuition.

Now, researchers at the Swiss Federal Institute of Technology in Lausanne (EPFL) have built an AI framework that lets chemists steer that entire process using plain language. The system, called Synthegy, was published in the journal *Matter* on April 24, 2026, and it represents a fundamentally different approach to applying large language models in the sciences: rather than asking AI to generate chemical structures, the team uses it to evaluate and rank the synthesis routes that traditional software already produces.

## How It Works

The workflow begins when a chemist types a strategic instruction in ordinary English. The request might be as specific as "form the pyrimidine ring in the early stages" or as broad as "avoid unnecessary protecting groups." Existing retrosynthesis software then generates dozens or hundreds of candidate pathways, each representing a different sequence of reactions to reach the target molecule from commercially available starting materials.

Synthegy converts every candidate route into a textual description and passes it to a large language model. The LLM scores each pathway on how well it satisfies the chemist's stated goals, assigns numerical rankings, and produces written explanations of its reasoning. The best routes rise to the top of the list, accompanied by justifications that a human expert can audit.

"When making tools for chemists, the user interface matters a lot, and previous tools relied on cumbersome filters and rules," said Andres M. Bran, first author of the study and a researcher in Philippe Schwaller's laboratory at EPFL. "With Synthegy, we are giving chemists the power to just talk, allowing them to iterate much faster and navigate more complex synthetic ideas."

The framework also tackles a second fundamental problem: reaction mechanism elucidation. Here, the question is not which reactions to run but why a particular reaction works at the electron level. Synthegy breaks each reaction into elementary electron movements and explores multiple mechanistic possibilities, with the language model assessing each step and guiding the search toward chemically plausible explanations. Additional context, such as specific reaction conditions or expert hypotheses, can be fed in as text to further refine the analysis.

## Validation Against Human Experts

The researchers subjected Synthegy to a rigorous double-blind evaluation. Thirty-six independent chemists, ranging from PhD students to senior professors, reviewed 368 pairs of synthesis routes and selected the option that better matched a given strategic instruction. Their choices aligned with the system's rankings 71.2% of the time on average, a figure that is roughly on par with the rate at which experienced chemists agree with one another on the same tasks. Notably, senior researchers such as professors and research scientists agreed with Synthegy more frequently than graduate students did, suggesting the system captures the kind of strategic intuition that typically comes only with years of bench experience.

The team benchmarked several frontier language models, including GPT-4o, Claude, DeepSeek-r1, and Gemini-2.5-pro. Gemini-2.5-pro scored highest in the overall evaluation, while DeepSeek-r1 emerged as a strong open-source alternative capable of running on local hardware. Smaller models, by contrast, performed no better than random guessing, underscoring that the reasoning capabilities required for chemical strategy evaluation remain an emergent property of scale.

## Practical Economics and Limitations

One striking detail buried in the paper is the cost: evaluating 60 candidate synthesis routes with Synthegy takes roughly 12 minutes of compute time and costs approximately two to three dollars in API fees. For a pharmaceutical company that might otherwise spend weeks having senior chemists manually sift through computer-generated route proposals, that represents an extraordinary compression of both time and expense.

The system is also designed to be modular. It can plug into any retrosynthesis engine on the backend and work with any sufficiently capable LLM on the reasoning side, making it adaptable as both chemistry software and language models continue to improve.

The paper does acknowledge current limitations. Language models sometimes misread the directionality of a reaction in its text representation, leading to incorrect feasibility assessments. Routes longer than 20 steps become harder for the model to track coherently. And while the framework excels at evaluating and ranking existing proposals, it does not yet generate novel reaction pathways on its own.

## Bridging Two Worlds

What makes Synthegy noteworthy in the broader landscape of AI for science is its philosophical approach. Rather than attempting to replace human chemists or automate discovery end-to-end, it positions language models as a reasoning layer that translates between human strategic intent and computational search. The chemist remains in the loop, articulating goals in natural language and reviewing the AI's explanations before committing to a synthesis plan.

"The connection between synthesis planning and mechanisms is very exciting: we usually use mechanisms to discover new reactions that enable us to synthesize new molecules," said Bran. "Our work is bridging that gap computationally through a unified natural language interface."

The code and benchmarks have been released publicly on GitHub, and the research was funded by the Swiss National Science Foundation through the NCCR Catalysis program, with additional support from Intel and Merck KGaA. If the framework proves robust in real laboratory settings, it could accelerate drug discovery timelines, democratize access to expert-level synthetic planning, and establish a template for how language models can augment, rather than replace, deep scientific expertise.
