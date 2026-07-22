# The Last Week of July Is Shaping Up to Be the Biggest Open-Model Drop Ever

The calendar for the final stretch of July 2026 reads less like a release schedule and more like a coordinated assault on the closed-model business. On July 24, DeepSeek is set to graduate its V4 family from preview to a stable, officially supported release. Three days later, on July 27, Moonshot AI is due to publish the full open weights for Kimi K3 — at 2.8 trillion parameters, the largest open-weight model anyone has shipped. Bracket those two dates with early-access drops from Mistral, Thinking Machines, and MiniMax, and the last week of July is on track to be the densest run of free, downloadable frontier-class models the industry has seen.

The two anchors of the wave both come from Chinese labs, and both are unusually capable.

## DeepSeek V4 finally goes stable

DeepSeek first shipped V4 as a preview on April 24, 2026, in two tiers: V4-Pro, a 1.6-trillion-parameter mixture-of-experts model with roughly 49 billion active parameters, and V4-Flash, a leaner 284-billion-parameter model with about 13 billion active. Both carry a 1-million-token context window and ship under the permissive MIT license, with weights already mirrored on Hugging Face and ModelScope.

What lands on July 24 is the graduation to a stable release. DeepSeek has scheduled the retirement of its legacy `deepseek-chat` and `deepseek-reasoner` aliases for 15:59 UTC that day, folding them into the V4 lineup as the default. On Artificial Analysis's Intelligence Index, V4-Pro scores 52 — up sharply from V3.2's 42 — placing it among the top open-weight reasoning models. V4-Flash trails at 47 but undercuts nearly everything on price, at roughly $0.14 per million input tokens and $0.28 per million output. V4-Pro output runs near $0.87 per million, an order of magnitude below comparable closed frontier APIs.

## Kimi K3, the biggest weights ever

If DeepSeek is the volume play, Kimi K3 is the spectacle. Moonshot unveiled it at Shanghai's World AI Conference on July 16, going live in its apps and API the same day, with the full weight dump promised for July 27. K3 is a sparse mixture-of-experts model that activates just 16 of 896 experts per token, pairs a 1-million-token context window with an always-on "thinking mode," and lands on the Artificial Analysis index at roughly 57 — third overall, behind only Claude Fable 5 and GPT-5.6 Sol, and narrowly ahead of Claude Opus 4.8.

That makes K3 the first Chinese model to sit inside the frontier pack rather than a generation behind it. It is not, however, the cheap option: at $3 per million input and $15 per million output, K3 costs several times more than DeepSeek V4 and roughly five to six times its own predecessor, Kimi K2.6. The surprise, as one Bloomberg headline put it, is that China's frontier model isn't the budget one.

One caveat is worth flagging. At launch, the open-weights claim was still a claim. As independent researcher Simon Willison noted, at unveiling there was no downloadable checkpoint, license file, or model card — the open release is a promise pinned to July 27, not yet a shipped artefact. Whether Moonshot hits that date is the single biggest variable in the week's narrative.

## Why it matters

The framing that mattered a year ago — open weights lag closed frontier models by several generations — no longer holds. By the independent numbers, the gap now reads as roughly one model generation, and on price the comparison isn't close. Enterprises evaluating a closed API against a self-hostable MIT- or Apache-licensed model that scores within a few points on public benchmarks, at a fraction of the token cost, face a genuinely different calculus than they did in 2025.

The cadence is the other half of the story. Chinese labs — DeepSeek, Moonshot, Zhipu, MiniMax — are shipping frontier-adjacent open weights on a rhythm that US labs have largely ceded, with OpenAI and Anthropic still anchored to closed, premium-priced APIs. That puts sustained downward pressure on inference pricing and hands regulated industries, sovereign deployments, and cost-sensitive startups a credible alternative to renting intelligence.

The counterpoint, voiced this week by an Anthropic executive who argued the company's technology remains six to 12 months ahead of Chinese rivals, is that raw benchmark position understates the closed labs' lead on reliability, tool use, and safety. K3's higher measured hallucination rate lends that view some weight.

## What to watch

Three things: whether Moonshot actually ships K3's weights on July 27 and under what license; whether DeepSeek's July 24 stable release holds its benchmark standing once the preview caveats drop; and how — or whether — the US frontier labs respond to a competitor cohort that is giving away models this good, this often.
