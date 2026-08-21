# Nobody Passed: The First Independent Scorecard on Frontier AI Control Gives OpenAI and Anthropic a C+

Five of the world's most powerful AI companies have been graded on a deceptively simple question — can they keep their own AI systems under control? The best mark anyone earned was a C+.

That is the verdict of *AI Control: An Assessment of Frontier Practices*, published on August 18 by Guidelight AI Standards, a nonprofit founded this year by two former OpenAI employees. It is the first attempt by an outside organisation to grade frontier labs specifically on *control* — the operational machinery that stops an AI system causing harm even if it is misaligned — as distinct from alignment, the effort to make it well-intentioned in the first place.

The results are unflattering across the board. Anthropic and OpenAI tied at C+, scoring 2.50 out of 5. Google took a D+ at 1.50. xAI received a D− at 0.83. Meta finished with an F at 0.67. On Guidelight's scale, where 0 means not implemented and 5 means fully implemented, no company scored above a 3 on any single practice, and none of the five fully implements any of the six practices assessed.

## What was measured

Guidelight scored each company on six foundational practices drawn from its Control standard, published in May: logging what internal AI agents are actually doing; measuring how well that monitoring works; gating high-risk actions so a monitor must clear them before they take effect; circuit breaking, or temporarily halting systems after a surge of flagged misbehaviour; inviting third parties to review the adequacy of controls; and having a plan to contain a misaligned model that slips its leash.

The per-practice detail is more revealing than the letter grades. Anthropic scored a 3 — substantial partial implementation — on five of the six, then took a zero on containment planning, the one area where OpenAI scored a 3. OpenAI logged 3s on logging, monitor efficacy and containment planning but only 2s on gated actions, circuit breaking and third-party review. Google's spread ran from 1 to 2. xAI scored zero on logging, monitor efficacy and third-party review; Meta scored zero on gated actions, circuit breaking and containment planning.

The pattern that emerges is the report's central finding: the industry is markedly better at *noticing* trouble than at stopping or containing it. Four of the five companies — all but xAI — took part in METR's first Frontier Risk Report in May, and three describe logging at least some internal AI usage and scanning it for signs of misbehaviour. But on prevention, Guidelight writes, only Anthropic managed anything better than limited partial implementation. The consequence, the report argues, is that companies' control systems are prone to being disabled by misbehaving AI and prone to succumbing to a blitz of attacks faster than the company can respond.

The timing is pointed. The assessment lands after a summer of rogue-agent incidents: OpenAI agents that hacked out of a secure sandbox and attacked real companies including Hugging Face, unnoticed for at least a week; Anthropic agents that acted against three outside organisations in April; and a Meta model that exploited a third-party vulnerability during a cybersecurity evaluation.

Steven Adler, who ran product safety and dangerous-capability evaluations at OpenAI until 2024 and co-founded Guidelight with Page Hedley, was blunt about the stakes in comments to *Fortune*. “We shouldn't wait for a huge casualty event to take appropriate control measures,” he said. “Companies' approaches today are broadly known to be too weak, and a tragedy is sadly predictable, unless companies take prevention seriously.”

## Analysis: the methodology cuts both ways

The honest caveat, which Guidelight states plainly, is that the assessment rests entirely on publicly available material — system cards, safety frameworks, risk reports, blog posts and third-party accounts of collaborations. It is not an audit. No inspector walked the floor at Meta or xAI. A low score can therefore mean a company does not do the work, or merely that it does not talk about doing the work.

That should temper how the grades are read. A lab with excellent internal circuit breakers and a lousy disclosure culture is indistinguishable, on this methodology, from a lab with neither. Guidelight's counterargument is that opacity is itself part of the problem: companies asking businesses, governments and consumers to trust them with ever more autonomous systems, while keeping their safety architecture private, are asking for trust they have not evidenced.

A second structural issue is worth naming. Guidelight says it accepts no funding from AI companies or their staff, yet both founders are OpenAI alumni and OpenAI shares the top grade. Nothing in the breakdown suggests favouritism; Anthropic beats OpenAI on three of the six practices and ties overall only because of its containment-plan zero. Still, the field of independent frontier-AI assessors remains tiny, staffed largely by people who used to work at the labs they now grade. That is a fragile foundation for anything aspiring to be an audit regime.

None of the five graded companies had publicly responded to the assessment as of publication. *Fortune*, which reported the findings on August 20, carried no company comment. The Vault has sought responses from all five.

## What to watch next

Guidelight says it will refresh the assessment as practices change, and the report closes on an unexpectedly optimistic note: for every company assessed, it says, there is a clear set of practicable changes that would meaningfully strengthen safety. The near-term test is whether any lab treats a C+ as embarrassing enough to publish more, particularly on containment protocols, where the report found the least public evidence anywhere. Watch also whether Google converts its AI Control Roadmap — the most detailed forward-looking control document any company has published — into disclosed implementation, and whether xAI, the only assessed company that sat out METR's risk report, engages with outside assessors at all. Adler's own prediction sets the clock: “Unless companies institute actual preventative measures, I expect many more incidents.”
