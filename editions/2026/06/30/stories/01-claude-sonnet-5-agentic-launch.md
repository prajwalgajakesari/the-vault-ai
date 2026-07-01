---
headline: Anthropic Launches Claude Sonnet 5, a Cheaper, More Agentic Model That Rivals Opus
category: llms-genai
story_number: 01
slug: claude-sonnet-5-agentic-launch
date: 2026-06-30
---

# Anthropic Launches Claude Sonnet 5, a Cheaper, More Agentic Model That Rivals Opus

Anthropic is betting that the next race in artificial intelligence will be won not by the model that thinks hardest, but by the one that works cheapest. On June 30, the company released Claude Sonnet 5, the most agentic version of its midsize model to date, and priced it aggressively enough to undercut its own flagship, Opus 4.8, as well as competing models from OpenAI and Google. Starting Tuesday, it became the default model for Free and Pro users of Claude.

The pitch is straightforward: Sonnet 5 can do the autonomous work that only larger, pricier models could handle a few months ago, and it can do it for a fraction of the cost. Anthropic said the model can make plans, use tools like browsers and terminals, and run autonomously for long stretches without human oversight. The company is positioning it as a workhorse for developers building AI agents, where every million tokens of input and output translates directly into an operating expense.

## Priced to move

At launch, Sonnet 5 costs 2 dollars per million input tokens and 10 dollars per million output tokens, an introductory rate that holds through August 31, 2026. After that, pricing rises to 3 dollars and 15 dollars. Even at the higher post-promotion rate, Sonnet 5 remains dramatically cheaper than Opus 4.8, which runs 5 dollars per million input tokens and 25 dollars per million output tokens, and it comes in below OpenAI GPT-5.5 and Google Gemini 3.1 Pro. Anthropic said developers can push costs down further, citing up to 90 percent savings with prompt caching and 50 percent with batch processing.

The model is available immediately across Anthropics full lineup: Free, Pro, Max, Team, and Enterprise plans, plus Claude Code and the Claude Developer Platform. Alongside the launch, the company also introduced Claude Science, an AI research workbench designed to help scientists analyze data, manage computing workflows, and produce auditable artifacts.

## Closing the gap with Opus

What makes Sonnet 5 notable is not just its price but how close it lands to Anthropics most capable model. On a knowledge-work benchmark (GDPval-AA v2), Sonnet 5 scored 1,618 to Opus 4.8s 1,615, a razor-thin margin that puts the cheaper model slightly ahead on tasks associated with subtle judgment calls and deep research. On Humanitys Last Exam with tools, Sonnet 5 hit 57.4 percent against Opus 4.8s 57.9 percent. On computer use (OSWorld-Verified), it posted 81.2 percent, up from Sonnet 4.6s 78.5 percent.

Opus still leads where it counts most for engineers. On agentic coding (SWE-bench Pro), Sonnet 5 scored 63.2 percent, well ahead of the 58.1 percent that predecessor Sonnet 4.6 managed in February, but short of Opus 4.8s 69.2 percent. Anthropic was candid about the tradeoff. "Opus 4.8 is still the model of choice for higher accuracy on these tasks, but Sonnet 5 provides developers with lower-priced options that are of much higher quality than what was previously available," the company said. "Between Sonnet 5 and Opus 4.8, users can adjust the effort level to find the right balance of cost and performance."

Early testers pointed to the models ability to finish jobs that older versions would abandon midway. "We handed Claude Sonnet 5 a two-part job - update Salesforce account tiers, send a launch announcement to enterprise contacts - and it finished end to end," said Daniel Shepard, a senior engineer at Zapier. "That used to stall halfway. For day-to-day automation, its a no-brainer."

## Why it matters

Sonnet 5s release is a signal about where the industry is heading. When Anthropic frames a midsize model around planning, tool use, and autonomy, it echoes the language OpenAI used for its GPT-5.6 Sol preview and Google used for Gemini 3.5 Flash. Agentic capability, once a premium feature reserved for flagship models, is now the baseline expectation at every price tier. The competitive frontier is shifting from who can perform agentic work best to who can do it most cheaply and most reliably without a human watching.

That shift favors buyers. For companies deploying fleets of AI agents that run continuously, a model that approaches flagship quality at less than half the price changes the math on what is economically viable to automate. It also pressures rivals to justify premium pricing when a cheaper model scores within a rounding error on knowledge work.

Anthropic paired the launch with a safety pitch, which matters as agents gain autonomy. The company said Sonnet 5 shows lower rates of undesirable behaviors like deception and cooperation with misuse than its predecessor, hallucinates less, and is better at resisting prompt-injection attacks. "At Lovable, were putting powerful tools in the hands of millions of builders," said co-founder Fabian Hedin, who said the model refuses unsafe requests cleanly and consistently. "A model that knows when to say no is just as important as one that knows how to build." Anthropic noted the model still trails Opus on certain misalignment measures and has a much lower ability to perform dangerous cybersecurity tasks.

## What to watch

The introductory pricing expires August 31, and the 50 percent jump in output costs will test how sticky Sonnet 5 proves once the discount ends. Watch, too, whether developers migrate agent workloads down from Opus to Sonnet in bulk, which would validate Anthropics cost-first strategy but could cannibalize its flagship revenue. And with OpenAI and Google shipping their own agentic models on similar timelines, the real contest will be measured not in benchmark points but in how many autonomous tasks these models can complete unattended, and how cheaply.