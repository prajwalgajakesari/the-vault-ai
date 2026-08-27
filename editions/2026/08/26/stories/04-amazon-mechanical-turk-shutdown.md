Amazon spent 21 years running a marketplace built on one premise: there are still things people do better than computers. On September 30, that marketplace closes — and the premise is the reason why.

AWS Mechanical Turk will shut down on September 30, 2026, Amazon told workers and requesters in a notice posted to mturk.com. "We regularly evaluate our programs, tools and services and make adjustments based on those assessments," the notice reads. "Following an assessment, we've made the decision to close AWS Mechanical Turk, effective September 30, 2026." Amazon has not publicly tied the decision to advances in AI. It did not have to.

MTurk launched in 2005 as a place where companies and academics could break large projects into Human Intelligence Tasks, or HITs, and scatter them across the internet at a few cents apiece: label this image, transcribe this clip, answer this survey, decide whether this comment violates policy. Amazon said the platform counted more than 500,000 workers at its peak. Jeff Bezos called the whole arrangement "artificial artificial intelligence," a joke about the 18th-century chess automaton that was secretly operated by a human hidden in the cabinet. Two decades later, the human is climbing out of the box and the machine is running itself.

## The warning came in July

The shutdown notice was not the first signal. Amazon stopped accepting new MTurk customers on July 30, 2026 — the same day it closed Amazon SageMaker Ground Truth and Amazon Augmented AI (A2I) to new sign-ups, along with a batch of other SageMaker features including Studio Lab, Clarify, Debugger and Model Monitor. Read together, the moves look less like retiring one aging product than like AWS stepping back from the human-data business it helped invent.

Workers read the July cutoff exactly that way. Krista Pawloski, a data worker and organizer with the advocacy group Turkopticon, told CNBC that MTurk had been "in decline" for years as Amazon invested less in the platform and competing labeling services pulled people away. Pawloski started turking in 2008 while on maternity leave, then moved to it full time in 2012 after losing a job while caring for a son with special needs. She says the platform still carries people who have nowhere obvious to go.

"There's some people that still pretty much still do it full time," Pawloski said. "They're concerned now."

The economics were never generous. A 2018 CHI study by Kotaro Hara and colleagues tracked 2,676 workers across 3.8 million tasks and found a median effective wage of roughly $2 an hour once unpaid time — hunting for HITs, completing work that got rejected — was counted. Only 4 percent of workers cleared the $7.25 federal minimum.

## The dataset that made deep learning possible

What MTurk lacked in wages it made up for in consequence. In 2007, Stanford's Fei-Fei Li was struggling to assemble a labeled image dataset large enough to train a serious vision model when a graduate student mentioned Amazon's new crowdsourcing platform. "He showed me the website, and I can tell you literally that day I knew the ImageNet project was going to happen," Li later told Quartz. Roughly 49,000 workers across 167 countries went on to sort more than 3.2 million images into 5,247 categories in under two years. ImageNet became the benchmark that AlexNet won in 2012, the result that kicked off the deep learning era. The pipeline that produced today's models ran through MTurk first.

By 2023, that pipeline had folded back on itself. Researchers at EPFL — Veniamin Veselovsky, Manoel Horta Ribeiro and Robert West — reran a standard abstract-summarization task on MTurk and used keystroke detection plus synthetic-text classification to estimate that 33 to 46 percent of crowd workers were quietly using large language models to do it. They titled the paper "Artificial Artificial Artificial Intelligence." Their conclusion was blunt: the results "call for platforms, researchers, and crowd workers to find new ways to ensure that human data remain human." A marketplace created to supply human answers where software fell short had started relaying software's answers back.

## Why It Matters

MTurk's death is not the end of human labor in AI. It is a repricing of it. The bottom of the market — binary classification, basic tagging, sentiment scoring — is now cheaper to run through a model than through a person, and the models were trained on exactly that kind of work. What survives is the top: Scale AI, whose data business Meta valued at $14.3 billion when it bought 49 percent in 2025; Mercor, which recruits doctors, lawyers and engineers to grade frontier-model output at rates approaching consulting fees; Prolific, which supplies vetted research participants. Same function, inverted labor market. The generalist earning pennies is out; the credentialed specialist billing by the hour is in.

That inversion has a cost the balance sheets do not capture. MTurk was accessible in a way its successors are not — no résumé, no interview, no credential, a phone and an internet connection. For disabled workers, caregivers and people locked out of conventional employment, it asked nothing about who you were. Its replacements ask for a lot.

The 2023 EPFL finding also leaves a harder question on the table. If a meaningful share of crowd annotations were already model-generated, the "human gold standard" that AI labs benchmark against was contaminated before anyone was checking. Every evaluation built on that foundation inherits the problem.

## What to Watch

Three things. Whether MTurk's remaining requesters — Pawloski says insurance and travel companies were still active right up to the notice — land at Prolific and Mercor or simply switch to synthetic data. Whether Turkopticon or any labor group extracts transition support for workers losing income on September 30. And whether AWS reverses course on Ground Truth, which Fast Company reports is still being offered to existing customers as an MTurk alternative even as it stops taking new ones. Amazon built the human-in-the-loop economy. It is now the most visible company walking away from it.
