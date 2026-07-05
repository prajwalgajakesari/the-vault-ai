When the US government slapped export controls on Anthropic's Fable 5 model on June 12, the trigger was a single research finding: Amazon researchers had coaxed the model into flagging software vulnerabilities in code, and in one case producing a demonstration of how one could be exploited. That was enough to freeze access for 18 days. By Anthropic's own later analysis, it was a borderline case handled as a crisis for a simple reason — nobody in the industry had a shared way to say how bad a jailbreak actually is.

Now the company is trying to build one. In posts published around Fable 5's July 1 global redeployment, Anthropic laid out an early draft of a proposed severity framework for AI jailbreaks, developed with what it calls its Glasswing partners — a group that includes Amazon, Microsoft, and Google. The stated goal is a common vocabulary that lets AI developers and governments describe the same vulnerability in the same terms.

## A four-axis rubric

At the center of the draft is a scoring system Anthropic calls the Cyber Jailbreak Severity (CJS) scale, which runs from CJS-0 ("Informational") through CJS-4 ("Critical"). The bands are meant to be exponential, so each step up is several times more serious than the last.

A jailbreak is scored on four axes. The first two describe what an attacker actually gains: *capability gain* (how far the technique takes an attacker beyond tools they already have) and *breadth of capability gain* (how many distinct offensive tasks the same trick works on). The second two describe how quickly it becomes a real-world problem: *ease of weaponization* (how much human skill it takes to turn the recipe into a working attack) and *discoverability* (how easily a threat actor could obtain the technique in the first place).

The logic maps onto intuition that anyone in security recognizes. A technique that is hard to find and hard to reproduce but unlocks catastrophic capability sits at the dangerous end and, in Anthropic's model, warrants emergency mitigation the moment severity is confirmed. A trick that is trivially public but only surfaces embarrassing or already-available behavior lands near the bottom, handled through routine patching. Scores are summed into a provisional CJS band that acts as a floor — reviewers can raise a rating if the rubric understates real-world danger, but not lower it.

## Re-scoring June 12

The most revealing part of the draft is what it implies about the incident that started everything. Anthropic's testing found that many weaker models — including Claude Opus 4.8, GPT-5.5, and Kimi K2.7 — could identify the same vulnerabilities the Amazon researchers extracted from Fable 5, and that every model tested could reproduce the single exploit demonstration. On the framework's own terms, that collapses the capability-gain axis: if publicly available tools reach an equivalent result, the technique "adds no new attacker capability." Anthropic describes the flagged behavior as routine defensive cybersecurity work that its safeguards blocked out of an abundance of caution, not a unique offensive super-power.

In other words, scored against the draft rubric, the June 12 jailbreak would have registered as a low-severity finding — not the kind of event that justifies emergency export controls. That is a striking admission from a company that spent nearly three weeks with two of its flagship models offline.

## Why a shared scale matters

The closest analogy, and one Anthropic reaches for explicitly, is the Common Vulnerability Scoring System (CVSS), the standard the traditional security world uses to rate software flaws. CVSS is imperfect and often gamed, but it gives defenders, vendors, and regulators a shared number to argue over. AI jailbreaks have had nothing equivalent — which means every headline that a model "got jailbroken" carries the same alarming weight regardless of whether the underlying finding is a party trick or a genuine uplift for attackers.

That ambiguity is precisely what turned a borderline report into a government shutdown. As AI Weekly noted, a shared severity scale, if it holds together, would let researchers and buyers talk about jailbreaks the way they already talk about CVSS scores. For governments, it offers something more consequential: a basis for proportionate response, so that a low-severity finding does not automatically escalate to the nuclear option of export controls.

Anthropic frames the effort in exactly those terms. "Our hope is that this collaboration, along with our proposed consensus industry framework, will serve as the basis for systematic rules for the whole industry," the company wrote.

## What to watch

The caveats are real. This is Anthropic's own draft, published in its own post; there is no named lead author, no timeline for finalization, and no stated mechanism for how rival labs will resolve disagreements when they score the same jailbreak differently. Anthropic is collecting public comment via a new HackerOne program and email before finalizing with the government. Watch for whether Microsoft, Google, and Amazon formally adopt the CJS scale in their own products — and whether regulators treat a low CJS score as a reason to hold their fire next time.
