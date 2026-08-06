---
headline: "Simon Willison Ships LLM 0.32, Deepening the Open-Source CLI's Tools and Fragments"
slug: llm-032-cli-release
category: llms-genai
story_number: "07"
date: 2026-08-05
---

# Simon Willison Ships LLM 0.32, Deepening the Open-Source CLI's Tools and Fragments

When Simon Willison pushed version 0.32 of his open-source `llm` tool to PyPI on the morning of August 4, he did not reach for the usual reserved language of a point release. He called it "the most significant new version of LLM since the initial launch of the project" — a striking claim for software that has quietly become a load-bearing piece of infrastructure for developers who talk to large language models from the command line. The release folds reasoning traces, provider-run server-side tools, a Git-inspired logging store and out-of-the-box support for the GPT-5.6 model family into a single `pip install -U llm`, and it nudges the humble CLI unmistakably toward being an agent framework.

## From prompt printer to reasoning window

The most immediately visible change is that `llm` now surfaces what reasoning models are actually thinking. Run a prompt against a reasoning-capable model and the model's intermediate reasoning trace streams to standard error, tinted grey in the terminal, while the final answer lands on standard output. The split is deliberate and practical: pipe the output of `llm` into another tool and you get only the clean answer, not the model's internal monologue. Developers who want silence can add the new `-R/--hide-reasoning` flag.

That design choice — separating thinking from output at the stream level — captures what makes `llm` durable. It treats the model as one more Unix citizen, composable with pipes, redirects and shell scripts rather than trapped behind a chat window.

## Tools that run on the provider's side

The headline capability for power users is server-side tools. Rather than orchestrating a tool-calling loop locally, `llm` can now ask the provider to execute tools inside its own environment. OpenAI exposes a code-execution sandbox and a web-search tool, invoked as simply as `llm --tool CodeInterpreter 'Show current python and SQLite versions'`. The companion `llm-anthropic 0.26` plugin, shipped alongside the core release, adds `WebSearch`, `WebFetch`, `CodeExecution` and an `AnthropicMCP` connector that lets Claude reach out to a Model Context Protocol server as part of a single request-response round trip.

A new `llm openai endpoint` command rounds out the tooling story, letting users fire a one-off prompt at any OpenAI-compatible endpoint — including a local LM Studio server — without configuring a model first. Those calls are deliberately not logged, making the command a fast scratchpad for experiments against local or self-hosted models.

## A logging store modeled on Git

Underneath the surface, 0.32 rebuilds how conversations are stored. The old SQLite schema duplicated the full message history on every turn, which grows unwieldy when a client keeps appending to a message array. The new content-addressable message store, explicitly "modeled after Git," deduplicates repeated content by hashing it, while `llm logs` and `llm logs --json` transparently reassemble the stored fragments into readable transcripts. The Python API gains a matching overhaul: a new `model.prompt(messages=[])` interface accepts a full message list directly, and `stream_events()` yields typed events — `reasoning`, `text`, tool calls, image attachments — instead of a flat stream of strings.

## Why a CLI keeps mattering

It is easy to overlook a command-line tool amid a market obsessed with polished chat products, but `llm` occupies a specific and increasingly valuable niche. It is provider-agnostic by design, speaking to OpenAI, Anthropic, Google, Mistral, OpenRouter and locally hosted models through a common plugin interface. That neutrality is the whole point: as the frontier labs ship new models at a cadence that now resembles software patch releases — GPT-5.6 Luna is already the new default model in this version — a stable, scriptable abstraction over all of them saves developers from rewriting integration code every few weeks.

The broader open-source LLM tooling ecosystem has coalesced around exactly this idea. Where vendors ship SDKs that lock you to one API, tools like `llm` compete on composability and reach. Willison's decision to expose server-side tools, MCP connectors and structured streaming events through the same one-liner grammar is a bet that the interesting work is increasingly in wiring models to tools, not in the models alone.

## What to watch

Willison himself concedes the trajectory in the release notes, writing under the heading "I guess LLM is an agent framework now" that the tool is "beginning to look very agent-shaped." Tool chains can now pause for human approval and resume from stored history — features driven by his Datasette Agent project. He floats baking a first-class "agent" concept into the core library next, while admitting he is "still trying to figure out what that would look like." For a project that spent years refusing to use the word "agent" at all, that is the release to watch for.
