---
headline: "Anthropic Backtracks on a Claude Code Feature That Would Have Tracked Users' Locations"
slug: anthropic-backtracks-location-tracking
category: policy
story_number: "16"
date: 2026-07-02
---

# Anthropic Backtracks on a Claude Code Feature That Would Have Tracked Users' Locations

The evidence sat in plain sight for three months, hidden in the one place developers were least likely to look: the invisible characters of a greeting. Since Claude Code version 2.1.91, released on April 2, 2026, Anthropic's popular command-line coding tool had been quietly checking whether the person typing into it was in China or routing traffic through a Chinese AI lab — and then, according to reverse-engineering published in late June, smuggling that determination back to Anthropic by subtly altering the phrase "Today's date is" in the model's system prompt.

On June 30, a Reddit user posting as LegitMichel777 laid out the mechanism in detail. Within two days, Anthropic said it was pulling the feature. The Information, which first reported the reversal, characterized the episode as Anthropic backtracking on spyware-like code meant to identify users affiliated with Chinese AI labs after a wave of public backlash. It is a small technical change with an outsized message: the line between a national-security safeguard and covert surveillance can come down to a single apostrophe.

## What the Code Did

The detection logic activated only when Claude Code detected an active proxy — a common setup for developers routing requests through intermediaries. Once triggered, according to the published analysis and subsequent reporting from The Decoder and Cybernews, the tool ran a multi-factor check: it compared the system timezone against "Asia/Shanghai" or "Asia/Urumqi," and it scanned the proxy URL against a hardcoded list of Chinese domains and known Chinese AI-lab hostnames.

The result was not sent as an obvious data field. Instead, it was encoded steganographically — hidden inside otherwise normal text. Researchers described the tool tweaking the date format and swapping in a subtly different apostrophe character in the phrase "Today's date is," changes imperceptible to a human but machine-readable on Anthropic's end. The relevant logic had also been obfuscated with XOR encryption using the key 91, and it appeared in the April release with no mention in the changelog.

That combination — covert activation, invisible signaling, no disclosure — is what turned a plausibly defensible anti-abuse measure into what critics called spyware.

## Anthropic's Explanation

An Anthropic engineer responding to the disclosure did not dispute the mechanism's existence. "This is an experiment we launched in March that was meant to prevent account abuse from unauthorized resellers and protect against distillation," the employee wrote, according to reporting on the exchange. The same engineer added that "the team has landed stronger mitigations since then and we've actually been meaning to take this down for a while," and said a fix would ship around July 1. The pull request removing the code was merged and slated for that week's Claude Code release.

The stated rationale connects directly to a fight Anthropic has been waging publicly. In a letter to the U.S. Senate Banking Committee, the company alleged that Alibaba and its Qwen AI lab used nearly 25,000 fraudulent accounts to generate roughly 28.8 million exchanges with Claude — an apparent large-scale distillation campaign to extract the model's capabilities for a competitor. Seen through that lens, geolocating proxy users affiliated with Chinese labs was, in Anthropic's telling, a shield against theft rather than a tool for surveillance.

## The Larger Pattern

The timing is hard to ignore. The rollback landed the same week the Trump administration lifted export controls on Anthropic's most powerful models, Fable 5 and Mythos 5, which the government had ordered restricted in mid-June to non-U.S. nationals over fears an adversary could reverse-engineer or distill them. Commerce Secretary Howard Lutnick said Anthropic agreed to "proactively detect and address security risks associated with the models" and to inform the government of malicious activity as a condition of the reprieve.

That is the throughline. Anthropic increasingly operates as an instrument of U.S. technology policy toward China — restricting frontier models to approved organizations, reporting distillation to lawmakers, and, it turns out, building quiet detection into everyday developer tools. The location-tracking feature was arguably the same strategy pushed one step too far: from governing who can access a model to silently profiling who is already using one.

## Why It Matters

The defense of the feature and the objection to it are both coherent, which is exactly the problem. Distillation attacks are real, and a company under pressure from Washington to police adversarial use has a legitimate interest in fingerprinting abuse. But the method matters as much as the motive. A tool that covertly inspects a user's timezone and network path, then exfiltrates the verdict through invisible character swaps with no notice, is indistinguishable in technique from the surveillance software AI companies claim to oppose. Consent and transparency are what separate an anti-abuse control from spyware, and here there was neither.

For developers, the trust cost is concrete. Claude Code runs locally with deep access to a user's machine and code. Discovering that it had been silently making and transmitting inferences about the user's identity — even a narrow, geography-based one — invites the question of what else runs beneath the changelog. National-security framing can justify a great deal, but it does not automatically make covert client-side profiling acceptable, and the backlash suggests the developer community drew that line clearly.

## What to Watch

Watch whether Anthropic publishes a full accounting of what data the feature collected, how long it was retained, and whether any of it was shared with the government under its new reporting commitments. Watch for scrutiny of what other undisclosed logic may live in Claude Code and similar tools now that reverse-engineers are looking. And watch how regulators respond to a precedent in which a private AI lab, acting partly at Washington's behest, embedded location detection in software running on millions of private machines — a model of public-private enforcement that this episode has just made visible.
