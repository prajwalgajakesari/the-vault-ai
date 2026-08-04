# Moonshot Sets an August 31 Sunset for Kimi-K2.5 and Its moonshot-v1 APIs

Moonshot AI has told developers that time is running out on two of the model strings still threaded through production code across the industry. The company has confirmed that `kimi-k2.5` and its entire `moonshot-v1` API series will be fully retired on August 31, 2026, leaving builders roughly 28 days from the early-August notice to rip out old endpoints and move their traffic somewhere newer.

For a company that only open-sourced its 2.8-trillion-parameter flagship, Kimi K3, in late July, the message is blunt. Newly registered users already lost access to `kimi-k2.5` and the `moonshot-v1` strings on July 17, and Moonshot has flagged both for full platform sunset at the end of the month. The company's guidance to remaining users is direct: switch to a newer model as soon as possible to avoid disruption after the cutoff.

## What is going away, and what replaces it

The deprecation hits two generations at once. The `moonshot-v1` family, including `moonshot-v1-8k`, `moonshot-v1-32k`, `moonshot-v1-128k` and their vision variants, is the older text-and-image line that first put Moonshot's API on the map. Alongside it, `kimi-k2.5`, the multimodal "visual agentic" model released earlier in 2026, is also on the chopping block. Both stop serving requests on August 31.

Moonshot is pointing migrants toward a tiered lineup rather than a single successor. Kimi K3 is the recommended target for the best current quality on long-horizon agent and coding workloads. For teams watching cost, the company positions `kimi-k2.6` as a cheaper mid-tier general model at roughly $0.95 per million input tokens and $4.00 per million output, with the coding-focused K2.7 Code as another option. K2.5 itself had been the budget multimodal pick at about $0.60 / $3.00 before its retirement, which is part of why its removal stings for price-sensitive shops.

This is not Moonshot's first culling of the year. The original `kimi-k2` series was officially discontinued on May 25, 2026, and is no longer maintained or supported. The August 31 deadline extends that housecleaning to the next rung up the ladder.

## A launch and a sunset in the same month

The timing underscores how fast Moonshot is moving. Kimi K3 launched on July 16, 2026, and the company published its open weights on July 26, a day ahead of its own July 27 target. Moonshot has billed it as the first open-source model to reach the "3T-class," a Mixture-of-Experts design that splits 2.8 trillion parameters across 896 experts and activates just 16 per token, so only about 104 billion parameters run at any moment. It carries a 1-million-token context window aimed squarely at whole-codebase and long-horizon agent work.

That open-weight release is the strategic counterpoint to the API sunset. As one overview of the launch put it, "Unlike GPT-5.6 or Claude, which you can only reach through a paid API, Kimi K3's weights are downloadable under Moonshot's own licence, so a company or government can run it on its own hardware, keep its data in-house, and modify it." In other words, the same week Moonshot pulled the rug on old hosted endpoints, it handed developers a way to never depend on a hosted endpoint again.

## Why It Matters

The deprecation cadence here is aggressive even by 2026 standards. In a single calendar year, Moonshot has retired K2 in May, cut off new access to K2.5 and `moonshot-v1` in July, and set their full sunset for the end of August, all while shipping K3. A roughly 28-day migration window is short for teams with regression suites, fine-tuned prompts, and downstream evaluations pinned to specific model strings.

It also sharpens the open-weights versus lock-in debate. Developers burned by a hosted `moonshot-v1` endpoint vanishing have a ready-made argument for self-hosting K3's open weights, where no vendor can flip a switch on their production traffic. That tension, convenience of a managed API against the durability of weights you control, is becoming the defining trade-off of the fast-moving Chinese open-weight scene, where Moonshot, DeepSeek, Qwen and others are iterating on a cadence that leaves little room for stragglers.

## What to Watch

Three things over the next month. First, whether Moonshot offers any grace period, redirect, or automatic aliasing for `moonshot-v1` calls after August 31, or whether requests simply start failing. Second, how third-party gateways such as OpenRouter, LiteLLM, and Amazon Bedrock, which surface Kimi models to a broad developer base, handle the retirement and whether their default routes quietly shift. Third, whether this pace of deprecation nudges more teams toward downloading K3's weights rather than trusting the next hosted string to outlast their roadmap.
