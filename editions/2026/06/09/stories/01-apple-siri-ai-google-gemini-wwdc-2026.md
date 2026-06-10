---
headline: Apple Rebuilds Siri as Siri AI on a Custom Google Gemini Model
slug: apple-siri-ai-google-gemini-wwdc-2026
category: llms-genai
story_number: '01'
date: 2026-06-09
---

# Apple Rebuilds Siri as “Siri AI” on a Custom Google Gemini Model

*The most consequential overhaul in Siri’s 15-year history arrives with a trillion-dollar-class model, a billion-dollar price tag, and antitrust clouds gathering on the horizon.*

Apple walked onto the WWDC 2026 stage on June 8 and did something it has resisted for years: admitted, in front of the world, that it needed Google’s help. The result is Siri AI — a fully conversational, deeply personal assistant rebuilt from the ground up on a custom 1.2-trillion-parameter model derived from Google’s Gemini architecture and running inside Apple’s own data centers. It is the most significant product pivot Apple has made in the AI era, and it may also be its most legally precarious.

## What Was Built — and How

The Gemini-based model at the heart of Siri AI is not an off-the-shelf product. Apple does not use the same Gemini models Google deploys to its own customers, nor does it run on Google’s cloud servers. Instead, Apple fine-tuned the architecture — internally called Apple Foundation Models v10 — on proprietary data, refined it using reinforcement learning, and deployed it on Apple Silicon hardware inside Apple’s Private Cloud Compute infrastructure, now extended to NVIDIA B200 Blackwell GPUs hosted in Google’s data centers. The mixture-of-experts design means only the most relevant parameter subset activates per query, keeping latency competitive even at this scale.

On-device tasks — parsing a message, summarizing a notification, recognizing a face in Photos — still run on Apple’s smaller, locally trained models. Cloud queries route through Private Cloud Compute or, for the most demanding reasoning tasks, the Gemini backbone. The cost of that arrangement, according to reporting from multiple outlets, runs to approximately $1 billion per year.

Craig Federighi, Apple’s senior vice president of software engineering, was direct about the partnership’s depth. “We partnered deeply with Google to co-create next-generation Apple Foundation Models,” he said during the keynote, describing an integration that goes well beyond a licensing agreement. In a post-keynote briefing with press, Federighi added that “Siri AI possesses vast global knowledge, providing the latest answers on almost any topic, while also maintaining on-screen awareness and understanding personal context to help users perform actions across various applications in an unprecedentedly natural way.” Privacy, he insisted, remains non-negotiable: “We believe privacy in AI is non-negotiable” — and he positioned the system orchestrator as the linchpin of Apple’s entire privacy architecture.

## The Regulatory Minefield

Siri AI arrives already carrying significant legal baggage. Apple and Google are parties to a roughly $20 billion annual agreement that makes Google the default search engine on Safari — a deal the U.S. Department of Justice has been fighting to unwind. In February 2026, the DOJ filed an antitrust appeal challenging a September 2025 ruling that left that search agreement intact. Layering a $1 billion AI model partnership on top of that existing arrangement is almost certain to accelerate scrutiny from regulators in Washington and Brussels.

The EU problem is already concrete: Apple confirmed at WWDC that Siri AI will not ship on iPhone or iPad in the European Union when iOS 27 launches this autumn, citing its ongoing dispute with regulators over the Digital Markets Act. That decision cuts off an estimated 450 million European users from the flagship feature of Apple’s most ambitious software release in years.

## Why It Matters — The Broader AI Landscape

Apple’s Gemini deal is a landmark moment in the consolidation of the frontier AI market. For years, the assumption was that the major platforms — Apple, Microsoft, Google, Meta — would each build sovereign AI stacks. Microsoft broke ranks first by embedding OpenAI deeply into its product suite. Apple has now made a parallel bet, and the counterpart is its oldest rival in mobile.

What the move signals is that even a company with Apple’s engineering resources, hardware advantage, and $3-trillion market cap has concluded that training and maintaining a frontier-scale language model — the kind that can hold a genuinely useful, contextual, multi-turn conversation — requires a depth of AI research infrastructure it does not yet possess alone. The partnership is less an admission of failure than a pragmatic acknowledgment that the gap between a capable on-device model and a frontier cloud model remains enormous, and that closing it independently would take years Apple does not have.

For Google, the deal is equally significant. It transforms Gemini from a consumer-facing product competing with ChatGPT into critical infrastructure embedded in over a billion active Apple devices. That reach, and the fine-tuning data that flows from it, could accelerate Gemini’s capabilities in ways that compound over time.

## What to Watch Next

iOS 27 developer betas are available today, with a public release expected in September 2026. Siri AI will ship as a beta at launch, in English only, with additional languages to follow. The DOJ antitrust proceedings will be the immediate legal flashpoint to monitor: if the appeals court moves to force a separation of the Google search deal, it will force difficult questions about whether the AI partnership can survive independently. Longer term, watch for whether Apple uses the Gemini partnership as a bridge — buying time to build out its own frontier model capability — or whether the economics of the arrangement lock it into a deepening dependency on its most formidable competitor in the smartphone market.

Tim Cook, making his final WWDC appearance as CEO before a widely anticipated leadership transition, called it a moment of transformation. Whether it is remembered as Apple’s masterstroke or its most complicated gamble will depend on courtrooms as much as on the quality of Siri’s answers.

---
*Sources: TechCrunch, 9to5Mac, CNBC, The Next Web, TechTimes, Tech Insider*
