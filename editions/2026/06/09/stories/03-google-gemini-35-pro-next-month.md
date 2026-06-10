---
headline: Google Confirms Gemini 3.5 Pro Arriving Next Month
slug: google-gemini-35-pro-next-month
category: llms-genai
story_number: "03"
date: "2026-06-09"
author: The Vault AI Edition
---

# Google Confirms Gemini 3.5 Pro Arriving Next Month

At Google I/O in May, Sundar Pichai delivered one of the most anticipated — and most immediately frustrating — lines of the conference season. The company had just shipped Gemini 3.5 Flash to general availability. When the crowd expected the flagship Pro tier to follow, Pichai offered a plainspoken deferral: “Give us until next month to get it to you.” The audible groan from the audience was its own editorial comment on the frontier AI arms race — and on Google’s well-documented habit of announcing ahead of delivering.

That “next month” is now July 2026, and with the deadline closing in, the industry is watching to see whether Gemini 3.5 Pro lands as scheduled and whether it can make a credible case against rivals who have not waited around.

## What Google Has Actually Promised

The confirmed facts about Gemini 3.5 Pro, as of early June, are narrower than the pre-launch buzz suggests. Google has confirmed: the model is “coming next month”; it is in internal testing; it shares Gemini 3.5 Flash’s emphasis on coding and agentic capability. That is the totality of on-the-record commitments. No benchmark numbers, no pricing, no model card, no API identifier have been officially disclosed.

What has circulated — sourced to internal preview users and analyst briefings — is considerably more specific. Gemini 3.5 Pro is expected to ship with a 2-million-token context window, double the 1-million-token ceiling on Flash and the largest of any production frontier model entering the market this season. It is expected to include a “Deep Think” reasoning mode, Google’s version of the extended-reasoning chains that OpenAI and Anthropic have each made centerpieces of their flagship offerings. And it is expected to restore the hard-reasoning lead that Flash, by Google’s own implicit admission, gave up.

“Pro targets a 2-million-token context window, a Deep Think reasoning mode, and frontier multimodal understanding,” Tech Times reported on June 6, summarizing what Google has outlined publicly. The Deep Think label points at something specific: a mode that trades latency for accuracy on the hardest problems — the class of tasks where speed-optimized models consistently stumble.

## The Flash Regression That Pro Needs to Fix

The case for Gemini 3.5 Pro is clearest when you look at what Flash did not do. Flash launched with measurable improvements over the prior-generation Gemini 3.1 Pro on coding (Terminal-Bench 2.1: +5.9 points) and agentic benchmarks (Finance Agent v2: +14.9 points). It is faster, cheaper — at $1.50 per million input tokens — and better on the workloads that dominate developer adoption.

But Flash regressed on the benchmarks that define frontier leadership: Humanity’s Last Exam (−4.2 points vs. Gemini 3.1 Pro), ARC-AGI-2 (−5.0 points), and long-context retrieval at 128K+ tokens (−7.6 points). Those are not marginal gaps. Hard reasoning and very long context are precisely where enterprise customers pay Pro-tier prices — and where Anthropic’s Claude Opus 4.8 and OpenAI’s GPT-5.5 are also competing.

“Flash already beats Gemini 3.1 Pro on coding and agentic benchmarks but regressed on hard reasoning — exactly the gap Pro needs to close,” WaveSpeed AI observed after the I/O launch in May. The Pro launch, in other words, is not a new idea; it is the completion of a model family whose faster half shipped first.

## Pricing and Access

Pricing for Pro is expected to track historical ratios between Google’s tiers: approximately $15 per million input tokens and $60 per million output tokens, roughly ten times the cost of Flash. Google plans to roll out the model first through its consumer subscription tiers — the $20-per-month Gemini Pro plan and the $250-per-month Ultra plan — with Ultra subscribers gaining the Deep Think reasoning mode. API and Vertex AI general availability are expected to follow the consumer rollout.

That pricing posture, if accurate, is deliberately competitive. Gemini 3.1 Pro currently lists at approximately $2.50 input and $15 output per million tokens. A Pro 3.5 launch at or above those levels would signal that Google is defending a premium reasoning tier rather than collapsing the Pro category into Flash’s price band.

## Why It Matters

The launch carries weight well beyond Google’s product calendar for three reasons.

First, Gemini is no longer just a standalone AI product. It is the engine powering the rebuilt version of Apple’s Siri, shipping on hundreds of millions of devices as part of Apple Intelligence. The better Gemini’s flagship reasoning capability, the more capable the AI layer across Apple’s entire ecosystem becomes — a feedback loop with consequences for how Google positions itself against both OpenAI and Anthropic for the consumer AI market.

Second, Google simultaneously open-sourced Gemma 4 — the research-grade sibling of the Gemini family — signaling that the company’s strategy combines a proprietary frontier with a freely available open-weight option. That dual-track posture is distinct from OpenAI’s closed approach and more aggressive on openness than Anthropic’s. It puts competitive pressure on the open-model community at the same time the closed flagship competes at the top.

Third, the frontier is compressing fast. GPT-5.5 leads the overall intelligence index as of June, while Gemini 3.1 Pro leads on GPQA Diamond reasoning at 94.3%, and Claude Opus 4.8 holds the default position for production agentic workflows. No single model dominates every category. That fragmentation means Gemini 3.5 Pro does not need to win everywhere — it needs to close the reasoning gap while holding the advantages Flash has already delivered. A model that does both would give Google a genuinely strong claim on the most demanding enterprise use cases.

## What to Watch

Three things will determine whether Gemini 3.5 Pro lands as a milestone or a marginal update.

**The benchmark report.** Google’s I/O restraint on Pro’s numbers means the first independent evaluation will set the narrative. Watch the hard-reasoning scores specifically — Humanity’s Last Exam and ARC-AGI-2 are the metrics Google’s internal teams almost certainly optimized toward, and they will be the first tests journalists and researchers run.

**Whether coding parity holds.** If Pro matches Flash on Terminal-Bench and MCP Atlas while recovering the reasoning gap, it is a strict superset of every model Google has shipped. If it buys back reasoning by sacrificing the agentic gains Flash made, developers will be running two endpoints — and Google’s integration story gets messier.

**The Apple Siri effect.** With Gemini powering Apple’s AI layer, the real-world performance of Gemini 3.5 Pro will be stress-tested at a scale no lab benchmark simulates. How it performs on hundreds of millions of daily Siri queries — complex scheduling, long-form summarization, multi-step reasoning — will matter more than any controlled evaluation. That deployment pressure is both Google’s biggest distribution advantage and its most public quality test.

The audience that groaned at Google I/O will have its answer by the end of July. Whether that answer is a frontier model or a footnote depends on what ships, not what was promised.

---

*Sources: WaveSpeed AI (May 20, 2026); Tech Times (June 6, 2026); Google I/O 2026 keynote; MindStudio AI model analysis; OpenRouter model comparison.*
