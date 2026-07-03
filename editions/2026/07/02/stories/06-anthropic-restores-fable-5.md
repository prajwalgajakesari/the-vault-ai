---
headline: "Anthropic Restores Claude Fable 5 After a Government-Triggered Shutdown"
slug: anthropic-restores-fable-5
category: llms-genai
story_number: "06"
date: 2026-07-02
---

# Anthropic Restores Claude Fable 5 After a Government-Triggered Shutdown

For nineteen days, one of the most capable AI models ever released to the public simply did not exist for anyone who wanted to use it. On June 12, three days after Anthropic launched Claude Fable 5 and its more powerful sibling Mythos 5, the U.S. government invoked export-control authority and ordered the company to cut off access for every foreign national, anywhere in the world. Because the order took effect immediately and Anthropic had no way to verify a user's nationality in real time, the company did the only thing it could: it pulled the plug on both models for everyone.

On July 1, Fable 5 came back. The return, announced in an Anthropic post dated June 30, marks the resolution of the most consequential standoff yet between a frontier AI lab and Washington — and a preview of a future in which shipping a model and clearing it with the government are becoming the same act.

## What Actually Happened

Anthropic released Fable 5 and Mythos 5 on Tuesday, June 9. The two share the same underlying model, but Fable 5 shipped with what Anthropic called "the strongest safeguards we've ever applied to a model," while Mythos 5 — which carries far fewer guardrails and can, in Anthropic's words, "find and exploit software vulnerabilities more effectively than any other model" — went only to a small set of trusted Project Glasswing partners for defensive cybersecurity work.

The trouble started with a report from Amazon researchers. According to Anthropic, they found "a method of bypassing Fable 5's safeguards: prompting it so that it identified a number of software vulnerabilities. In one case, the model produced code demonstrating how the relevant vulnerability could be exploited." Amazon CEO Andy Jassy flagged the finding to federal authorities. Within days, Commerce Secretary Howard Lutnick sent Anthropic CEO Dario Amodei a letter directing the company to suspend access for foreign nationals.

White House AI adviser David Sacks laid out the administration's version bluntly: "A highly credible trusted partner of both Anthropic and the USG who was testing Fable came forward with a jailbreak of those guardrails."

Anthropic disputed the severity. Its own testing, the company said, "confirmed that many less capable models — including Claude Opus 4.8, GPT-5.5, and Kimi K2.7 — could identify the same vulnerabilities as Fable 5 did in the report." On the one exploit demonstration, Anthropic said, "every model we tested could produce the same demonstration as Fable 5." In the company's framing, the reported technique reached only a "borderline" case inside a deliberately conservative safety margin, and "involved routine defensive cybersecurity work" — not the Mythos-level offensive capability regulators feared.

## The Fix, and the Return

Whatever the disagreement over stakes, Anthropic moved fast. Working with the government, it trained a new safety classifier that, by its account, blocks the specific technique in the Amazon report "in over 99% of cases." Requests to Fable 5 that trip the classifier are now redirected to the older Opus 4.8. Researchers at the Commerce Department's Center for AI Standards and Innovation (CAISI) tested both the old and new safeguards and, per Anthropic, "agree that they are extraordinarily strong."

Commerce lifted the controls on June 30. Fable 5 returned July 1 across the Claude Platform, Claude.ai, Claude Code, and Claude Cowork, with re-enablement on AWS, Google Cloud, and Microsoft Foundry to follow. To smooth the disruption, Anthropic is including Fable 5 for up to 50% of weekly usage limits for Pro, Max, Team, and select Enterprise plans through July 7, after which access moves to usage credits.

Mythos 5 did not come all the way back. It has been restored only for a set of approved U.S. organizations, following a separate government sign-off on June 26, with Anthropic saying it "continue[s] to coordinate with the government to expand access" through the Glasswing program.

## Why It Matters

The Fable 5 episode is the clearest sign yet that model roadmaps are becoming policy roadmaps. A single external report, escalated through a CEO to a cabinet secretary, took a flagship product offline globally within 72 hours of its debut — and the mechanism was export-control law, the same regime that governs advanced chips and munitions. That is a structural shift: a frontier model can now be treated as a controlled export, and its availability can turn on a government determination rather than a company's own risk assessment.

Anthropic's response is telling. Rather than fight the precedent, it is trying to shape it. The company is proposing, with Amazon, Microsoft, Google, and other Glasswing partners, a consensus framework to score the severity of AI jailbreaks along four axes — capability gain, breadth of that gain, ease of weaponization, and discoverability — explicitly modeled on the Common Vulnerability Scoring System that already governs software bugs. The goal is to give both developers and governments an "agreed-upon standard for when to act," so the next shutdown is triggered by a shared metric rather than an ad hoc phone call.

Anthropic also committed to deeper government collaboration: pre-release access for national-security-relevant models, rapid safeguard information sharing, dedicated joint-research teams, and compute for government testing — all tied to the June 2 Executive Order on "Promoting Advanced Artificial Intelligence Innovation and Security." The company was pointed about the tradeoff it wants in return, arguing that "government involvement in AI releases requires a durable, transparent process" and should "be codified in strong regulation and applied equally across frontier model developers."

That is the real fight underneath the Fable 5 saga. The industry has accepted that governments will have a hand on the release valve. The open question is whether that hand operates through predictable rules applied to everyone, or through opaque, case-by-case interventions that reward whoever has the better line to the Commerce Secretary.

## What to Watch

Three things. First, whether the jailbreak-severity framework gains real adoption — a standard is only as good as the number of labs that agree to be bound by it. Second, whether Mythos 5's access expands beyond approved U.S. organizations, and on what terms, since that is where the genuinely novel offensive capability lives. And third, whether the promised "durable, transparent process" materializes in regulation, or whether the next frontier launch simply invites the next surprise shutdown.

## Sources

- [Redeploying Claude Fable 5 — Anthropic](https://www.anthropic.com/news/redeploying-fable-5)
- [Amazon warning triggered Anthropic's shutdown — AP News](https://apnews.com/article/anthropic-fable-mythos-trump-claude-028db5135128fce6b38c873bf9cb5e09)
- [Anthropic, Fable and the export-control standoff — Financial Times](https://www.ft.com/content/137ddb71-852f-438c-ad76-25e2dc43486b)
- [Claude Fable 5 promotional access — Anthropic Support](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access)
