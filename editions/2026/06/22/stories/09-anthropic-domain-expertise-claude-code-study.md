The conventional wisdom about coding assistants has been that the better a programmer you are, the more you get out of them. Anthropic just published evidence that the conventional wisdom is wrong.

In a report released June 16, the company's economic research team analyzed roughly 400,000 Claude Code sessions recorded between October 2025 and April 2026 — drawn from about 235,000 people — and found that what separates the users who extract the most autonomous work from the model is not coding ability. It is domain expertise: a firm grasp of the problem being solved, the business logic, and the constraints that make an answer right or wrong.

"Coding agents are not substituting for domain expertise," the authors write. "The more understanding a worker brings to an agent, the more quality work the agent is able to do."

## What the numbers show

The study, titled "Agentic coding and persistent returns to expertise," used a privacy-preserving classification pipeline — no researcher read individual transcripts — to rate each session on a five-point expertise scale and sort it into one of nine "work modes." Crucially, the expertise rating is task-specific, not a proxy for seniority. The paper offers a sharp illustration: a senior engineer asking their first Rust question is a beginner at Rust, while "an accountant who has never used Python, but tells Claude exactly which reconciliation rules a Python script must enforce and catches the edge case it mishandles at month-end close, is an expert at that task."

The expertise gradient turned out to be steep. In typical novice sessions, each prompt set off about five Claude actions and roughly 600 words of output. In expert sessions, a single prompt triggered action chains more than twice as long — about 12 actions — carrying five times the output, around 3,200 words. That gap, the authors note, "appears within every kind of work and every band of task value."

Success followed the same curve. A novice-rated session reached the study's strictest bar, "verified success" — judged successful with hard evidence like passing tests, commits, or pull requests — just 15% of the time. Intermediate and expert sessions hit that bar 28% to 33% of the time. The pattern was even starker when sessions ran into trouble: among sessions that hit errors or repeated failures, only 4% of novice sessions still ended in verified success, versus 15% for experts. And 19% of struggling novice sessions were simply abandoned with zero lines of code written, against 5% to 7% for everyone else.

"Part of the value of expertise appears to be the ability to steer the agent in the right direction," the researchers write.

## Coding background, by contrast, barely mattered

The most striking control in the study compares occupations. Anthropic inferred each user's job from session context and mapped it to Bureau of Labor Statistics categories, explicitly instructing the classifier not to treat the act of coding as evidence of a coding profession. The result: in sessions that produced code, every one of the ten largest occupation groups landed within seven percentage points of software engineers on success. Users in software occupations reached verified success about 34% of the time in code-producing sessions; users from other professions, 29%. Management occupations actually edged out software engineers on the verified-success measure — possibly, the authors speculate, because management skills transfer to directing an agent.

The picture is one of a clear and stable division of labor. Across sessions, people made roughly 70% of the planning decisions — what to build, which approach to take, what counts as done — while Claude made about 80% of the execution decisions: which files to change, what code to write, which commands to run. "People decide what to build," the report summarizes, "and the agent decides how to build it."

The seven-month window also captured the work itself shifting. The share of sessions spent fixing broken code fell from 33% to 19%, nearly in half. In its place, operating software grew from 14% to 21%, and writing and data analysis roughly doubled, from about 10% to 20%. By Anthropic's freelance-marketplace-calibrated estimate, the value of the average session rose about 27% over the period — the authors caution those dollar figures are coarse and best read as relative comparisons.

## Why It Matters

The finding rewrites the staffing math for anyone deploying Claude Code at scale. The dominant mental model — that you need a senior engineer in the loop reviewing every line — is, on this evidence, the wrong constraint. The expert in the chair needs to deeply understand the domain and its constraints, not necessarily the language the agent is writing in.

That has a direct operational implication: if a Claude Code deployment is underperforming, the likeliest fix is not a better prompt or a newer model, but a genuine domain expert in the review seat. A team shipping financial reconciliation tooling is better served by an accountant who knows the edge cases than by a generalist engineer who knows TypeScript. It also reframes who can do technical work at all. As the authors put it, "A person with such command, in any field, may now be able to do technical work they previously could not. A person without any such expertise will get far less from the same tool."

There is a caveat worth holding onto for hiring and training: the gains come "mostly from competence, not mastery." A working grasp of a domain captured most of the benefit; the jump from intermediate to expert added comparatively little.

## What to Watch

Anthropic flagged the returns to expertise as a signal to track over time. If that premium begins to shrink in future reports, it would mean models are starting to supply the judgment users currently bring — and that the benefits are broadening beyond domain experts. If success rates for non-software occupations keep climbing, it could mean software production is becoming ordinary work in every field rather than the province of one profession.

The study has limits the authors are candid about: it cannot observe real-world outcomes (whether code was actually shipped or discarded), it excludes substantial non-interactive and headless usage, and every classification rests on a model reading the transcript. But as an early read on where knowledge work is heading as agents spread beyond code, the message is unusually clear. The scarce input is understanding the problem — and that has never been a programming skill.

## Sources

- [Agentic coding and persistent returns to expertise — Anthropic](https://www.anthropic.com/research/claude-code-expertise)
- [What 400K Claude Code Sessions Reveal About Domain Expertise and Model Tier Routing — TheRouter.ai](https://therouter.ai/news/anthropic-claude-code-expertise-routing-session-data-2026/)
- [Anthropic releases economic research on Claude Code usage — Crypto Briefing](https://cryptobriefing.com/anthropic-claude-code-economic-research/)
