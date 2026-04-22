---
headline: "OpenAI Launches Chronicle in Codex, Giving AI Coding Assistant Screen-Based Memory"
slug: openai-chronicle-codex-screen-memory
category: llms-genai
story_number: 7
date: 2026-04-21
author: The Vault AI Edition
---

# OpenAI Launches Chronicle in Codex, Giving AI Coding Assistant Screen-Based Memory

OpenAI wants its AI coding assistant to remember what you have been working on — by watching your screen. The company on April 20 released Chronicle, a new opt-in feature for its Codex desktop app on macOS that periodically captures screenshots, processes them into structured text summaries, and stores those summaries as local memory files. The result is an AI pair programmer that can pick up where you left off without requiring you to re-explain your entire workflow every session. But the feature ships with significant privacy trade-offs that are already drawing scrutiny from security researchers and comparisons to Microsoft\u2019s controversial Windows Recall.

## How Chronicle Works

Chronicle runs sandboxed background agents on macOS that periodically take screenshots of whatever is on your display. Those captures are sent to OpenAI\u2019s servers, where ephemeral Codex sessions use OCR and language models to extract relevant context — the projects you are working on, the documentation you are reading, the pull requests you are reviewing. The output is saved locally as plain Markdown files in `~/.codex/memories_extensions/chronicle/`, giving Codex persistent, session-spanning context about your development work.

The raw screen captures are stored temporarily in a local directory and automatically deleted after 6 hours, according to OpenAI\u2019s documentation. The company says captures are not retained on its servers after processing and are not used for model training.

Sam Altman has been characteristically enthusiastic about the feature. \u201cThe internal working name for this was \u2018telepathy,\u2019 and it feels like it,\u201d the OpenAI CEO said, underscoring the company\u2019s ambition to make AI assistants that feel less like tools and more like collaborators who simply know what you have been doing.

Greg Brockman, OpenAI\u2019s president, echoed that sentiment, describing Chronicle as \u201can experimental feature giving Codex the ability to see and have recent memory over what you see\u201d with effects that feel \u201csurprisingly magical.\u201d

## Who Gets It — and Who Does Not

Chronicle is available exclusively to ChatGPT Pro subscribers — the $100-plus per month tier — running macOS 14 or later on Apple Silicon Macs. Users must grant Screen Recording and Accessibility permissions and manually enable the feature through Settings, then Personalization, then Memories, then Chronicle. It is not available in the European Union, the United Kingdom, or Switzerland, a restriction almost certainly tied to GDPR and similar data protection regulations.

The geographic and pricing constraints mean Chronicle reaches a narrow audience. But that audience is substantial: OpenAI says over 1 million developers have used Codex, with usage doubling after the GPT-5.2-Codex model launched in December 2025.

## The Privacy Problem

The comparisons to Microsoft\u2019s Windows Recall are immediate and unflattering. When Microsoft previewed Recall in 2024, the feature was pulled after security researchers demonstrated that its screenshot database could be trivially exfiltrated. Microsoft eventually relaunched Recall with local encryption, device-side processing, and biometric authentication requirements.

Chronicle, by contrast, sends screenshots to OpenAI\u2019s cloud for processing and stores the resulting memories as unencrypted plain-text Markdown files accessible to any process running on the machine. OpenAI\u2019s own documentation acknowledges that \u201cother apps may access these files\u201d and that memories \u201cmight contain sensitive information.\u201d

The prompt injection risk is particularly concerning. Because Chronicle reads whatever is on your screen, a malicious website with hidden instructions could potentially influence Codex\u2019s behavior — the user does not even need to copy-paste the text. As one security analysis put it: \u201cAnything on your screen is a potential injection vector.\u201d

There is also the practical issue of resource consumption. OpenAI warns that Chronicle\u2019s background agents \u201cconsume rate limits quickly,\u201d meaning Pro subscribers paying a premium may find their access to other Codex features constrained while Chronicle is active.

## The Bigger Picture

Chronicle represents a clear bet by OpenAI that the next frontier in AI assistants is not just better models but better memory — persistent, ambient awareness of what a user is doing across their entire computing environment. It is the kind of feature that could genuinely transform developer productivity if it works well and earns user trust.

But trust is exactly what OpenAI needs to build, and launching a screen-monitoring feature with unencrypted local storage, cloud-based processing, and acknowledged prompt injection vulnerabilities is a risky way to do it. Microsoft learned that lesson the hard way with Recall. Whether OpenAI absorbs that lesson or repeats the cycle may depend on how quickly the company moves to address the security gaps that researchers are already flagging.

For now, Chronicle is a research preview — experimental, opt-in, and limited. But the direction is unmistakable: OpenAI wants Codex to know what you know, see what you see, and remember what you forget. The question is whether developers will let it.