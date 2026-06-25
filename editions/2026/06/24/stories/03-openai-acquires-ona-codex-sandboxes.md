OpenAI is buying its way out of one of Codex's most stubborn limitations. The company announced it will acquire Ona — the cloud development platform formerly known as Gitpod — to give its Codex coding agent something it has conspicuously lacked: persistent, long-running cloud sandboxes that can keep working for hours or days, even after a developer closes their laptop.

The deal, first announced June 11 and now moving through closing conditions, is the clearest signal yet that the AI coding race has shifted from raw model quality to execution infrastructure. And it is, unmistakably, a response to Anthropic. Claude Code has used native long-horizon execution to capture more than 40% of the generative-AI coding market, according to industry estimates, while OpenAI's Codex sits at roughly 21%. Ona is OpenAI's attempt to close the structural gap that share figure represents.

## Why Codex needed this

Until now, Codex has largely run inside stateless, short-lived execution contexts — environments that spin up, do a discrete task, and tear down. That model works fine for the kind of bounded request that finishes in minutes. It breaks down for the work enterprises increasingly want delegated: multi-step builds, full test-and-deploy cycles, and validation loops that span more than a single session.

OpenAI framed the problem plainly in its announcement, saying that as Codex grows more capable, its most valuable work is now unfolding over hours or days rather than minutes — and that people should be able to delegate ambitious work without staying tethered to the machine where it started. Ona supplies exactly that substrate. Its sandboxed cloud environments come pre-configured with dependencies and tooling, and feature automatic checkpointing roughly every ten minutes so a long task survives interruptions, network drops, or a closed laptop.

That capability is precisely what Claude Code has offered more or less natively, and it is a large part of why Anthropic's tool became the default for serious agentic engineering work. Persistent state is not a nice-to-have for enterprise teams; it is a prerequisite for any workflow involving deployment, testing, and iterative validation across more than one sitting.

## Who Ona is

Ona is not a fresh startup. It is Gitpod, rebranded in September 2025, with more than five years of history building cloud development environments. Founded and led by CEO Johannes Landgraf, the company pioneered the Cloud Development Environment category — spinning up containerized, ready-to-code workspaces in the cloud to eliminate the hours developers lose configuring local machines. By its own accounting, Ona's platform has served around 2 million developers in secure, reproducible cloud environments.

That heritage matters. OpenAI is not just buying a feature; it is buying a mature orchestration layer with enterprise security guardrails already baked in — the kind of trust-and-control machinery that large customers demand before they let an autonomous agent touch production systems.

The two principals framed the logic in their own words. Ona's Landgraf said agents need more than intelligence — "they need a trusted workspace" — adding that the company built Ona to give agents cloud environments with the context, control and collaboration enterprises require, and that joining OpenAI lets it fold that foundation into Codex. Thibault Sottiaux, OpenAI's core products lead, struck a complementary note: "Enterprises want powerful agents that can do real work while meeting the security and control requirements of their environments. Ona will help us make Codex easier to deploy securely across production workflows for customers operating at the highest standards of trust and scale."

## The terms, and what is not known

Financial terms were not disclosed, and OpenAI did not publish a purchase price. One third-party analysis floated an estimate north of €100 million (roughly $108 million), but that figure is an outside guess, not a confirmed number, and should be treated as such. The acquisition is subject to customary closing conditions, including required regulatory approvals — notable given Ona's German roots, which place the deal within the orbit of European merger review.

What is confirmed is the strategic momentum behind it. OpenAI says more than 5 million people now use Codex each week, a figure it puts at up 400% from earlier this year. Bolting Ona's infrastructure onto that user base is meant to convert casual adoption into the kind of sticky, production-grade deployment that drives enterprise contracts.

## The coding-agent race, reframed

Step back and the Ona deal reads as a concession and a counterpunch at once. For most of the past two years, the AI coding contest was litigated on benchmarks — who scored higher on this or that eval. Anthropic's quiet insight was that the model is only half the product. The other half is the environment the model acts in: whether it can hold state, recover from failure, and grind through a long task unattended. Claude Code's market lead suggests developers agreed.

OpenAI's move says it agrees too. Rather than try to replicate persistent infrastructure in-house from scratch, it bought a team that has spent five years building it. That compresses the timeline considerably — Ona's checkpointing and sandbox orchestration are battle-tested, not theoretical. If the integration goes smoothly, Codex could erase the most-cited reason engineering teams have chosen Claude Code over it.

The open question is whether infrastructure parity is enough. Anthropic's lead is also a habit; teams that have standardized on Claude Code's workflows do not switch lightly, and Anthropic continues to iterate on the agentic experience that built its share. Persistent sandboxes get OpenAI to the table. They do not, by themselves, win the seat.

## What to watch

Three things will tell the story over the coming months. First, integration speed: how quickly Ona's environments become a default Codex capability rather than a bolt-on, and whether OpenAI keeps Ona's existing 2 million developers in the fold or churns them through a messy transition. Second, the regulatory path — a German acquisition by OpenAI may draw EU scrutiny that delays closing. Third, and most telling, the share numbers. If Codex's roughly 21% slice starts climbing toward Claude Code's 40%-plus, the Ona bet will have paid off. If it does not move, OpenAI will have learned that in the coding-agent race, persistent sandboxes were table stakes — not the trump card.
