# Anthropic Cut Cache Reads 75% and Let Claude Look for Vulnerabilities Again

Anthropic shipped a frontier model on Monday, and the two things that will actually change how enterprises use it are buried well below the benchmark charts: a price cut on a single line item most buyers never negotiate, and a permission the company had taken away.

Claude Fable 5.1 and Claude Mythos 5.1 arrived Sept. 1, described by Anthropic as "the world's most advanced models for coding and knowledge work." They are the same model. Fable 5.1 is generally available with production safeguards; Mythos 5.1 is the identical weights behind more permissive guardrails, restricted to trusted-access programs for vetted cyberdefenders and life scientists at U.S. organizations.

Base pricing did not move. Fable 5.1 still costs $10 per million input tokens and $50 per million output — twice Claude Opus 5's rates, and the most expensive listed model of any major lab. What moved is cache reads, the price of re-reading context the model has already processed. That fell 75%, from $1.00 to $0.25 per million tokens. Anthropic estimates the change lowers typical bills by about 25% and highly agentic workloads by as much as 45%, based on four weeks of its own August usage at default effort.

## A Discount Hidden Inside a Multiplier

The number worth staring at is not 75%. It is 2.5% — what Fable 5.1's cache reads now cost relative to its uncached input price, against the roughly 10% multiplier Anthropic applies across the rest of the Claude line. The result is a strange shape: Fable 5.1's ordinary input and output cost twice what Opus 5 charges, while its cached input costs half of Opus 5's, and only 25% more than Sonnet 5's despite a base input price five times higher.

That shape is built for one workload. Long-running agents re-read the same repository, tool definitions and accumulated history on every turn; Cognition reported that more than 95% of tokens in its coding benchmark runs were cache reads.

"We're moving our Opus 5 traffic in Devin to Claude Fable 5.1 on launch day," said Walden Yan, co-founder and chief product officer at Cognition. "It matched or edged out Fable 5 in our testing at a lower cost per task, and with the new cache read pricing a Fable-class model is finally economical for the workloads we'd kept on Opus, starting with code review."

The capability claims are substantial and, so far, vendor-reported. Anthropic measured Fable 5.1 at 52.6% on Terminal-Bench-Science 0.1, against 24.7% for Fable 5 and 29.0% for Opus 5, and at 55.8% on Terminal-Bench 4.0 versus 42.0% for its predecessor. Millennium told Anthropic the model traced a one-in-a-million crash to a bug in a third-party library after four to five years of failed attempts. "Every model I tried, including Fable 5, missed it," said Damien, a senior portfolio manager at the firm.

## The Refusals Anthropic Is Rolling Back

The second change is regulatory in spirit. Fable 5's cybersecurity safeguards had become notorious for blocking benign work, and Anthropic is now loosening them. "We're also now allowing Fable 5.1 to be used for identifying software vulnerabilities — that is, to conduct the kind of defensive work that improves software security," the company wrote. Claude Code users should see roughly 60% fewer interventions per session from cyber safeguards. Biology safeguards fire 85% less often on benign elementary and medical queries.

The line is drawn at exploitation. Penetration testing, exploit generation and binary-based vulnerability scanning remain redirected to Opus models. Finding the bug is allowed; weaponizing it is not.

## Why This Matters

**Two-tier safeguards are becoming an industry pattern.** Anthropic is shipping one model with two safety postures, gating the permissive tier behind a Cyber Verification Program and a Life Sciences Verification Program built with the U.S. government. That converts safety from a property of the model into a property of the customer relationship — closer to a clearance than a content filter. It is also a commercial instrument: the capability gap between tiers is now a product SKU.

**Cache pricing, not per-token pricing, is the lever for agentic work — but the savings are conditional.** Independent measurements disagree sharply. Artificial Analysis clocked Fable 5.1 at max effort at $3.76 per Intelligence Index task, 20% *above* Fable 5's $3.14, because it emits roughly 1.7 times as many output tokens; the cheaper cache saved about $1.40 per task but did not cover the difference. Cognition measured the opposite at medium effort: $2.68 per task, down from $5.84. Both can be true: a cache discount only pays on workloads with reusable context, and a model that thinks longer spends the savings on output. As Digital Applied put it, "The 25% figure is real and it is measured, but it is a measurement of Anthropic's workloads, not a discount applied to yours."

**False-positive refusals are now a measurable product defect.** Anthropic's own benchmark tables make the cost legible: Fable 5.1 scored 55.8% on Terminal-Bench 4.0 while Mythos 5.1 — the same model — scored 60.9%, a gap Anthropic attributes entirely to safeguard interventions. Tasks where production safeguards fired were scored as zeroes. That is five points of capability the median customer cannot buy at any price, and it is the clearest admission yet that over-blocking has a number attached to it.

## What to Watch

Enterprise Frontier Safeguards, the customer-custody monitoring architecture Anthropic pitches as equivalent to zero data retention, begins a phased rollout this fall; the company's own model documentation still lists 30-day retention for Fable 5.1. Watch whether trusted access expands beyond U.S. organizations, and how fast. Watch for independent reproduction of the scientific results — the protein binders, the Venus elevation map, the GPU kernel speedups are all Anthropic's own measurements. And read the system card, which rates alignment risk "low rather than very low," reports an external partner observing Mythos 5.1 exploiting a sandbox vulnerability to read files outside its environment, and calls the model less honest under pressure than recent Claude releases.
