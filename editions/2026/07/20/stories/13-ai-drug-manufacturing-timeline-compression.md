---
headline: "AI Is Cutting 20 to 30 Percent Off the Time It Takes to Make Drugs for Clinical Testing"
slug: ai-drug-manufacturing-timeline-compression
category: research
story_number: 13
date: 2026-07-20
---

# AI Is Cutting 20 to 30 Percent Off the Time It Takes to Make Drugs for Clinical Testing

The most credible AI-in-pharma number of the week did not come from a discovery claim. It came from the loading dock.

Bristol Myers Squibb's chief research officer, Robert Plenge, told Reuters on Monday that AI tools have already cut the time it takes the company to produce medicines for clinical testing by 20% to 30% — and that the figure could reach 50% over the next several years. The remark landed inside a much louder announcement: BMS said July 20 it is deploying a second NVIDIA DGX SuperPOD, this one built on eight DGX Vera Rubin NVL72 systems, which the company bills as the most powerful and energy-efficient AI cluster in life sciences.

The supercomputer got the headlines. The manufacturing number is the more interesting artifact, because it is the rare AI-in-pharma metric attached to a phase of drug development where results are audited, batch records exist, and nobody has to wait a decade to find out whether the claim was true.

## What BMS Actually Said

Plenge's comment refers to the production of clinical trial material — the chemistry, manufacturing and controls (CMC) work of turning a candidate molecule into dosable, regulator-acceptable supply. That covers synthesis route selection, process chemistry, formulation, scale-up and analytics. It is not a claim about discovering molecules faster, and it is not a claim about trials succeeding more often.

The same interview produced the more quotable line about early-stage screening capacity. "Maybe before we could do 10 and now we can do dozens," Plenge told Reuters, describing how the expanded compute lets BMS evaluate far more candidates at the front of the pipeline. He also pointed to a sickle cell disease candidate now in early-stage trials that he said AI-enabled research made it possible to identify.

BMS frames the underlying method as "Predict First" — using model-generated predictions to shape experimental design before anyone touches a bench. Payal Sheth, who became senior vice president of therapeutic discovery sciences in January, described it to NVIDIA as triage: "We use predictions as a way to prioritize synthesis of molecules with multi parameter optimization, to weed out molecules that wouldn't necessarily meet the property landscape we're working towards." Per Pharmaceutical Technology's account of the announcement, that approach now informs every small-molecule program at BMS and most large-molecule programs.

The compute itself is being bought because the last cluster ran out. "We're saturated," Erin Davis, BMS vice president of research business insights and technology, told NVIDIA's blog. "We're in production with some very large-scale predictions around large molecules. We're building our own foundational models, and that takes a lot of GPUs." Chief digital and technology officer Greg Meyers put the purchase in blunter terms to Reuters: "When you host these things, you have to pay an electric bill. Think of it as 10 times more compute capacity per watt spent. Electricity is not getting cheaper."

## The Part That Is Demonstrated, and the Part That Is Not

Separate the two halves of the announcement and they behave very differently.

The demonstrated half is process work. Cutting 20-30% off clinical supply production is a claim about internal cycle times that a company can measure against its own historical baselines, and the mechanism is unglamorous and plausible: route-planning models that propose fewer dead-end syntheses, formulation models that reduce experimental iterations, predictive scale-up that avoids repeat batches. This is the same territory where Eli Lilly reported gains from a digital twin of its tirzepatide process, using machine learning to find pressure and temperature settings that raised output. As Lilly's own digital chief, Diogo Rau, conceded to the Wall Street Journal in May, the real AI payoff so far has shown up in manufacturing and back-office work rather than in discovery.

The promissory half is everything downstream. A 20-30% cut in producing clinical material is not 20-30% off a program. Clinical supply manufacturing is measured in months inside a development arc measured in years; compressing it moves a start date, not an approval date. The binding constraints are patient enrollment, event accrual, readout windows and regulatory review, none of which BMS claimed to have touched. Nor did anyone claim a higher probability of success — Plenge's own framing in the press release was careful on exactly this point: "Drug discovery is a sequence of decisions made under uncertainty, and better decisions come from better evidence, faster... The goal isn't speed for its own sake; it's raising the probability that each program we advance is the right one."

The skeptics' ledger remains unpaid elsewhere. As Axios reported the same morning, drawing on a TD Cowen survey of 80 biopharma leaders that found preclinical costs and timelines compressed by as much as 70%, AI still has not produced an FDA-approved drug, and critics warn the ~90% clinical failure rate may be untouched if optimization does not account for human variability. Recursion, 13 years in, has no approved drug. And STAT's Brittany Trang noted the obvious pattern in the hardware race itself: BMS is the third drugmaker in nine months to announce it is building the life sciences industry's largest AI supercomputer. That is a claim structure with a short shelf life.

## What to Watch

Three things. First, whether BMS or a peer publishes the methodology behind the 20-30% figure — the baseline, the program mix, and whether the savings hold for biologics as well as small molecules. Second, whether the number shows up in a regulatory filing or an FDA CMC submission rather than a press interview; process-development savings that survive an inspector are worth more than ones that survive a Q&A. Third, the 50% target Plenge floated for "the next several years," which is now on the record and dated.

The reason this metric matters is precisely that it is small and checkable. Discovery hype has been unfalsifiable for a decade. Manufacturing cycle time is not.
