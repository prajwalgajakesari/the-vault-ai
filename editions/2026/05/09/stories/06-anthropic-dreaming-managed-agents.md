---
headline: "Anthropic Introduces Dreaming to Let Claude Agents Learn and Self-Improve From Past Sessions"
slug: anthropic-dreaming-managed-agents
category: llms-genai
story_number: "06"
date: 2026-05-09
sources:
  - name: Anthropic Blog
    url: https://claude.com/blog/new-in-claude-managed-agents
    domain: claude.com
  - name: VentureBeat
    url: https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes/
    domain: venturebeat.com
  - name: The New Stack
    url: https://thenewstack.io/anthropic-managed-agents-dreaming-outcomes/
    domain: thenewstack.io
  - name: SiliconANGLE
    url: https://siliconangle.com/2026/05/06/anthropic-letting-claude-agents-dream-dont-sleep-job/
    domain: siliconangle.com
  - name: Digital Trends
    url: https://www.digitaltrends.com/computing/anthropic-just-taught-claude-to-dream-between-tasks-and-it-makes-agents-meaningfully-smarter/
    domain: digitaltrends.com
  - name: 9to5Mac
    url: https://9to5mac.com/2026/05/07/anthropic-updates-claude-managed-agents-with-three-new-features/
    domain: 9to5mac.com
  - name: The Decoder
    url: https://the-decoder.com/claudes-new-dreaming-feature-is-designed-to-let-ai-agents-learn-from-their-mistakes/
    domain: the-decoder.com
---

# Anthropic Introduces Dreaming to Let Claude Agents Learn and Self-Improve From Past Sessions

AI agents forget everything the moment a session ends. Anthropic thinks that is the single biggest thing holding them back -- and on May 6, the company shipped its answer: a feature called "dreaming" that lets Claude agents review up to 100 past sessions overnight, extract patterns from their own mistakes, and write those lessons into persistent memory before the next workday begins.

The feature, launched in research preview as part of a broader update to Claude Managed Agents, represents one of the most concrete attempts yet to give AI systems a form of experiential learning -- not by retraining the underlying model, but by building a structured reflection loop on top of it.

## How dreaming works

Dreaming is a scheduled background process that runs between active agent sessions. Rather than storing raw interaction logs indefinitely, it reviews prior sessions and memory stores, merges duplicate information, removes outdated entries, and highlights recurring patterns such as repeated mistakes, workflows that agents converge on, and preferences shared across a team.

The key architectural choice is separation of concerns. Memory, which Anthropic launched earlier for Managed Agents, captures what an agent learns as it works. Dreaming refines that memory between sessions, pulling shared learnings across agents and keeping the memory store high-signal as it evolves. Developers control how much autonomy the system gets: dreaming can update memory automatically, or teams can review every proposed change before it lands.

"Dreaming surfaces patterns that a single agent can't see on its own, including recurring mistakes, workflows that agents converge on, and preferences shared across a team," Anthropic wrote in its announcement. The company positions the combination of memory and dreaming as forming "a robust memory system for self-improving agents."

## Real-world results: Harvey sees 6x improvement

The most striking early result comes from Harvey, the legal AI company that uses Managed Agents to coordinate complex legal work including long-form drafting and document creation. With dreaming enabled, Harvey's agents began retaining filetype workarounds and tool-specific patterns between sessions. The result was dramatic: completion rates increased approximately sixfold in their tests -- not from a model upgrade, but purely from agents carrying institutional knowledge across sessions.

Wisedocs, a document processing company, reported that its quality-check agent now runs 50 percent faster while maintaining alignment with internal review standards. Netflix's platform team, meanwhile, built an analysis agent that processes logs from hundreds of builds, using multiagent orchestration to analyze batches in parallel and surface only the patterns worth acting on.

## Beyond dreaming: outcomes and multiagent orchestration

The dreaming launch arrived alongside two other features moving from research preview to public beta. Outcomes lets developers write a rubric describing what success looks like for a given task. A separate grader model evaluates the agent's output against those criteria in its own context window -- isolated from the agent's reasoning -- and sends the agent back for another pass when something falls short. In Anthropic's internal benchmarks, outcomes improved task success by up to 10 points over standard prompting, with file-generation quality jumping 8.4 percent on Word documents and 10.1 percent on PowerPoint files.

Multiagent orchestration, the third piece, allows a lead agent to break complex jobs into pieces and delegate each to a specialist with its own model, prompt, and tools. Up to 20 specialist agents can work in parallel on a shared filesystem. Spiral, a writing tool built by the newsletter company Every, uses this architecture with a Haiku-based lead agent delegating drafts to Opus-powered subagents, with outcomes enforcing editorial quality standards on every output.

## What it means for the industry

Dreaming tackles a problem that has quietly frustrated every company deploying AI agents at scale: the absence of institutional memory. Today's agents are brilliant amnesics. They can reason through novel problems in a single session but start from zero the next time. Human workers accumulate judgment over weeks and months; agents have had no equivalent mechanism -- until now.

The approach is notably conservative by design. Dreaming does not modify Claude's weights or fine-tune the model. It operates entirely at the application layer, curating a memory store that sits alongside the model rather than inside it. That means the improvements are auditable, reversible, and under the developer's control -- properties that matter enormously in regulated industries like law and healthcare where Harvey and Wisedocs operate.

The competitive implications are significant. OpenAI, Google, and other major labs have invested heavily in agent frameworks, but none have shipped a comparable reflection-and-learning loop for production agents. If dreaming delivers on its early promise, it could become a meaningful differentiator for Anthropic's platform business.

There are open questions. The feature is still in research preview, and Anthropic has not disclosed how dreaming handles conflicting patterns across agents or how it scales beyond 100 sessions. The company also has not published independent benchmarks -- the 6x figure from Harvey, while striking, comes from a single customer's internal tests.

Still, the underlying insight feels sound: the gap between a capable model and a capable agent is not just about reasoning -- it is about remembering. Dreaming is Anthropic's bet that bridging that gap at the memory layer, rather than the model layer, is the fastest path to agents that actually get better at their jobs over time.

*Dreaming is available in research preview for Claude Managed Agents. Outcomes and multiagent orchestration are now in public beta. Developers can request access through the Claude Platform.*
