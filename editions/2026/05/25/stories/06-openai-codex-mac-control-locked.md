---
headline: "OpenAI Codex Now Controls Your Mac While Locked, Expanding Agent Autonomy"
slug: openai-codex-mac-control-locked
category: llms-genai
story_number: "06"
date: 2025-05-25
author: The Vault AI
sources:
  - https://www.macrumors.com/2026/05/22/codex-use-mac-apps-when-locked/
  - https://opentools.ai/news/openai-codex-locked-mac-control
  - https://www.macworld.com/article/3147024/openai-codex-can-now-run-with-locked-macbooks.html
  - https://developers.openai.com/codex/app/computer-use
---

# OpenAI Codex Now Controls Your Mac While Locked, Expanding Agent Autonomy

Your Mac no longer needs you sitting in front of it for an AI agent to get work done. OpenAI announced on May 21 that its Codex desktop agent can now operate macOS applications even after the screen is locked and the display goes dark -- a capability the company calls "Locked Use" that marks a significant escalation in the race to build truly autonomous AI agents.

The update means developers can fire off a task from their phone, lock their laptop, walk away, and let Codex keep clicking through windows, navigating menus, and typing across whichever apps they have explicitly approved. When the work is done, the results are waiting.

## How It Works

Locked Use is not a brute-force workaround. According to OpenAI's developer documentation, the feature integrates directly with Apple's trusted security architecture through an authorization plug-in that participates in the standard macOS unlock flow. When Codex needs to interact with an application after the screen has locked, the plug-in temporarily unlocks the machine while blocking local access and preserving the locked-screen protections for anyone physically near the computer.

"Locked use is intentionally narrow," OpenAI's documentation states. "It is not a general-purpose remote-unlock path for your Mac, and it does not let other apps or local processes unlock the computer."

The safeguards are layered. The unlock window is scoped to the current Codex task and expires quickly. Only Codex can trigger it -- no other apps or local processes gain access. Every connected display is covered while the desktop is temporarily unlocked, preventing bystanders from seeing screen content. And if the system detects any physical keyboard or mouse activity, the Mac immediately re-locks and pauses automatic unlock until the user manually intervenes.

To enable the feature, users need the Codex desktop app with the Computer Use plugin installed, along with Screen Recording and Accessibility permissions granted in macOS System Settings.

## The Bigger Picture

The locked-screen capability shipped alongside several other updates in what OpenAI internally calls "Codex Thursday." A new Appshots feature lets users press Command-Command to instantly inject a screenshot and text from any Mac app window into a Codex conversation. Goal Mode, which allows developers to assign broad objectives like increasing test coverage to 90 percent and lets Codex plan and execute across session breaks, graduated from experimental to general availability.

These features collectively transform Codex from a tool that requires constant human supervision into something closer to an autonomous collaborator. Developer Theo Browne captured the sentiment on X, quipping: "At this point I think OpenAI has more macOS engineers than Apple does."

The numbers underscore the momentum. OpenAI reported more than 4 million weekly Codex users as of mid-May, up from 3 million in April and 1.6 million in early March -- a growth trajectory that has roughly tripled the user base in under three months.

## Why It Matters

Until now, developers running long AI agent tasks on their Macs resorted to workarounds: terminal commands like caffeinate to prevent sleep, third-party utilities to disable lock-screen triggers, or even hardware display dongles to trick the system into thinking an external monitor was attached. Locked Use eliminates those hacks with a native, Apple-integrated solution.

The feature also represents a philosophical shift in how AI agents relate to the computers they operate. Federico Viticci of MacStories called Codex's Computer Use "the best computer use feature I have ever tested in any LLM or desktop agent," noting that it reads the macOS accessibility hierarchy rather than relying on the screenshot-and-coordinate-click approach used by competitors. That architectural choice gives Codex structural understanding of UI elements -- buttons, text fields, nested menus -- rather than just pixel-level guessing.

When paired with Locked Use and Goal Mode, this means Codex can now run substantial overnight workflows without a human ever touching the keyboard. The implications extend well beyond coding: any repetitive GUI-based task that currently requires a human to babysit a screen is now a candidate for delegation.

## What to Watch

Several constraints keep this from being a free-for-all. Locked Use does not work when a MacBook lid is closed, since clamshell mode triggers a different sleep path that the authorization plug-in cannot intercept. The feature is macOS-only, with no Windows or Linux support. And it is unavailable at launch in the European Economic Area, the United Kingdom, and Switzerland -- a nod to regional regulatory sensitivities around automated desktop access. Terminal apps, Codex itself, and system-level admin prompts are also off-limits.

The regional exclusion is telling. As AI agents gain the ability to operate computers without direct human oversight, regulators in Europe are likely to scrutinize these capabilities under the EU AI Act's provisions for high-risk AI systems. How OpenAI navigates that regulatory landscape will shape whether Locked Use -- and features like it from competitors -- become globally available or remain fragmented by jurisdiction.

For now, the competitive pressure is intensifying. Anthropic's Claude and Google's Gemini have their own computer-use capabilities, but neither currently offers locked-screen operation. OpenAI's willingness to push this boundary first could establish an early standard for what autonomous desktop agents are expected to do -- and force the rest of the industry to follow or explain why they will not.
