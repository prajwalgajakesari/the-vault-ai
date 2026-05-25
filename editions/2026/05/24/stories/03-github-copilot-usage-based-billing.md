---
title: "GitHub Copilot Shifts to Usage-Based Billing With AI Credits Starting June 1"
slug: github-copilot-usage-based-billing
category: business
story_number: "03"
date: 2026-05-24
sources:
  - name: "GitHub Blog"
    url: "https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/"
    domain: "github.blog"
  - name: "The Register"
    url: "https://www.theregister.com/2026/04/28/microsofts_github_shifts_to_metered/"
    domain: "theregister.com"
  - name: "CodePick"
    url: "https://codepick.dev/en/guides/copilot-ai-credits-billing/"
    domain: "codepick.dev"
  - name: "Visual Studio Magazine"
    url: "https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx"
    domain: "visualstudiomagazine.com"
  - name: "GitHub Docs"
    url: "https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals"
    domain: "docs.github.com"
---

# GitHub Copilot Shifts to Usage-Based Billing With AI Credits Starting June 1

The all-you-can-eat era of AI coding assistance is ending. Starting June 1, GitHub Copilot will retire its fixed-allotment premium request model and replace it with GitHub AI Credits — a token-metered virtual currency that ties what developers pay directly to what they consume. For millions of Copilot subscribers, the change signals something bigger than a billing tweak: it is an admission that the economics of subsidized AI assistance have become unsustainable.

## The End of the Flat-Rate Buffet

GitHub Chief Product Officer Mario Rodriguez did not mince words when announcing the change on April 27. "Today, a quick chat question and a multi-hour autonomous coding session can cost the user the same amount," he wrote in a company blog post. "GitHub has absorbed much of the escalating inference cost behind that usage, but the current premium request model is no longer sustainable."

The diagnosis is widely shared across the industry. Anthropic, Google, and OpenAI have all moved to tighten usage limits or introduce premium tiers in recent months as agentic AI workflows — sessions that can run for hours, iterate across entire codebases, and chain together dozens of model calls — push compute costs far beyond what flat subscription fees were designed to cover.

Under the old system, GitHub used Premium Request Units (PRUs) as a rough abstraction over model usage. The problem: a deceptively short prompt sent to a thinking-heavy model like Anthropic's Opus could consume far more inference compute than a long but simple completion, yet both cost the user the same number of PRUs. GitHub ate the difference. With agentic usage exploding in late 2025 and early 2026, that arbitrage became untenable.

## How GitHub AI Credits Work

The new system replaces PRUs with GitHub AI Credits, where one credit equals $0.01 USD. Consumption is calculated based on actual token usage — input tokens, output tokens, and cached tokens — at model-specific API rates. The abstraction layer of credits lets GitHub normalize pricing across its growing model catalog without forcing subscribers to track raw token counts.

Crucially, base subscription prices are not changing:

- **Copilot Pro:** $10/month, including $10 in monthly AI Credits (1,000 credits)
- **Copilot Pro+:** $39/month, including $39 in monthly AI Credits (3,900 credits)
- **Copilot Business:** $19/user/month, including $19 in monthly AI Credits
- **Copilot Enterprise:** $39/user/month, including $39 in monthly AI Credits

Code completions and Next Edit Suggestions remain unlimited on all paid plans and do not consume credits — a meaningful carve-out for developers whose Copilot usage is primarily inline assistance. The metered model applies to Copilot Chat, the CLI, agentic coding sessions, Copilot Spaces, Spark, and third-party coding agents.

To ease the transition, existing Business and Enterprise customers will receive promotional credits through August: $30/month for Business subscribers and $70/month for Enterprise — roughly 1.5 to 1.8 times their standard allotment.

## Who Gets Hit — and Who Doesn't

The impact of the shift is sharply uneven. Developers who rely primarily on code completions and inline suggestions will see little day-to-day change. Those who have built workflows around Copilot Chat, long-context code review, or autonomous coding agents are in different territory entirely.

Preview billing data shared in GitHub's community forum has alarmed some heavy users. One developer reported that their April 2026 usage, which would have cost $39.07 under the old PRU model, came back at $902.72 in GitHub's preview billing tool — a 23-fold increase. While this figure likely represents extreme agentic usage rather than typical behavior, it has amplified concerns about cost predictability.

"You will get less, but pay the same price," became the rallying cry in developer communities, as reported by Visual Studio Magazine. The complaint points to something real: the fallback experience that previously kicked in when PRUs were exhausted — dropping users to a less capable model but keeping them working — is being eliminated entirely. Under the new model, once credits run out, usage is simply capped until the next billing cycle, unless administrators configure additional spending budgets.

VS Code's development team moved quickly in response, rolling out token-use throttling in late April to limit background context consumption and help users conserve their monthly credit allotments ahead of the June 1 deadline.

## A Broader Industry Reckoning

GitHub's pivot is part of a broader repricing wave hitting the AI tools market. The explosive growth of agentic coding agents — systems that can run continuously, spawn sub-agents, and consume enormous context windows — has stress-tested every flat-rate subscription model in the space.

The Register noted the dynamic bluntly, comparing GitHub's position to Red Lobster's infamous Endless Shrimp promotion, which contributed to the seafood chain's 2024 bankruptcy: the math of unlimited consumption at a fixed price eventually catches up with any provider.

The comparison is apt. The economics of unlimited AI access look very different when the marginal user is a developer running 24-hour autonomous coding agents rather than one asking occasional inline questions. GitHub is not alone in recalibrating: OpenAI has floated ending unlimited ChatGPT plans and launched a $100/month Pro tier for heavy Codex users; Anthropic has tightened Claude usage limits; and cloud providers including AWS and Azure have grappled with capacity constraints driven by AI demand. The agentic inflection point of late 2025 — when models became capable enough for extended autonomous workflows to become mainstream — appears to have triggered a simultaneous cost crisis across the industry.

## What Subscribers Should Do Now

GitHub has released a preview billing dashboard accessible through the Billing Overview page at github.com, giving users and administrators a projected cost estimate before June 1 arrives. The company is also introducing pooled credits for organizations — unused credits from one user can offset consumption by another, eliminating the stranded capacity problem that plagued per-seat PRU models.

Administrators gain new budget controls at the enterprise, cost-center, and individual user levels. When included credits are exhausted, organizations can either allow overage spending at published rates or hard-cap usage — a meaningful governance improvement over the previous model, where the only real lever was restricting which models users could access.

Users on annual Pro or Pro+ plans are not immediately migrated; they remain on PRU-based billing until their plan expires, after which they will transition to Copilot Free with the option to purchase a monthly plan. Annual plan holders who want to switch early can convert to monthly billing and receive prorated credits for remaining plan value. Those who stay on annual plans will face sharply higher model multipliers starting June 1 — Anthropic's Opus 4.7, for example, jumps from a 7.5x PRU multiplier to 27x, and OpenAI's GPT-5.4 rises from 1x to 6x.

## The Bottom Line

GitHub's move to usage-based billing is a milestone in the maturation of the AI tools market. The flat-rate, premium-request era was a land-grab phase: price to drive adoption, absorb the losses, and figure out sustainable economics later. Later has arrived.

For most Copilot users, the June 1 change will be largely invisible. For power users who have made agentic coding sessions and extended Copilot Chat sessions central to their workflows, the math is about to get significantly harder. The question now is whether competitors — Cursor, Windsurf, Amazon Q, and others — can sustain their own flat-rate economics long enough to capture developers who find GitHub's new pricing model uncomfortable. Based on the industry trajectory, the answer is probably not for long.

---

*Sources: [GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/), [The Register](https://www.theregister.com/2026/04/28/microsofts_github_shifts_to_metered/), [CodePick](https://codepick.dev/en/guides/copilot-ai-credits-billing/), [Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx), [GitHub Docs](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals)*
