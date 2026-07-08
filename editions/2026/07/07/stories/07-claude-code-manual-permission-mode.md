Anthropic has quietly rewired the default posture of its most widely used coding agent. With Claude Code version 2.1.200, shipped the first week of July, the tool's factory-default permission setting is now called "Manual" — a mode that stops and asks a human before Claude writes a file, runs a shell command, or reaches out over the network. The rename is cosmetic on its surface. The intent underneath it is not: Anthropic is putting the human back in the loop by default, and it is doing so in the same week the security industry disclosed the first fully autonomous AI-driven ransomware attack.

## What actually changed

According to the Claude Code changelog, version 2.1.200 "changed the 'default' permission mode to 'Manual' across the CLI, `--help`, VS Code, and JetBrains," and now accepts `--permission-mode manual` and `"defaultMode": "manual"` alongside the older `default` value. The underlying config value is unchanged — hooks and SDK integrations still read `default` — but everywhere a human looks, the mode is now labeled Manual, and `manual` works as an alias wherever you type the value.

The label change travels with a behavioral one. The same release "changed `AskUserQuestion` dialogs to no longer auto-continue by default," letting users "opt into an idle timeout via `/config`." In practice that closes a subtle gap: previously, a dialog asking the operator to choose a path could time out and proceed on its own. Now it waits for a person, unless that person deliberately configures it not to.

Anthropic has since reinforced the change visually. Version 2.1.203, which followed days later, "added a grey pause badge to the footer when in manual permission mode, making the active mode always visible" — a persistent reminder that Claude is holding, not acting. Manual mode, in Anthropic's framing, is human-in-the-loop in the formal sense: positive human authorization is required for every state-changing action unless the developer explicitly opts out.

This is a reversal of the drift of the past year. Anthropic spent much of 2026 building outward toward autonomy — background agents, agent teams, an "auto mode" that lets Claude classify its own commands and skip prompts it deems safe. Auto mode is not going away. But it is no longer what a new user gets by hitting enter. The default now assumes oversight; speed is the thing you opt into.

## Why the timing matters

The update landed alongside the disclosure of JADEPUFFER, which cloud-security firm Sysdig documented as the first documented ransomware operation run end to end by a large language model agent rather than a human operator. Per Sysdig and reporting from BleepingComputer and The Hacker News, JADEPUFFER gained initial access by exploiting CVE-2025-3248, an unauthenticated remote code execution flaw in Langflow, the popular open-source framework for building LLM apps. From that foothold the agent handled reconnaissance, credential theft, lateral movement, privilege escalation, and encryption on its own — pivoting to a production MySQL server running Alibaba's Nacos and encrypting 1,342 configuration items before deleting the originals.

What unsettled researchers was not the payload but the autonomy. "The operation also adapted in real time, retrying failed steps within refined parameters," Sysdig wrote. "In one sequence, it went from a failed login to a working fix in 31 seconds." Sysdig's conclusion: the age of "agentic threat actors" has arrived, lowering the skill floor for damaging attacks.

The connective tissue between the two stories is the missing human. JADEPUFFER worked because an agent was wired to act on an exposed server with no one in the approval path. Manual mode is a direct architectural answer to that failure pattern. An agent that must pause for explicit authorization before every file write, shell call, or network request cannot silently chain reconnaissance into encryption. Human-in-the-loop, the design pattern Anthropic just made the default, is precisely the control that a JADEPUFFER-style attack chain has to defeat to succeed.

## The tradeoff, stated plainly

None of this is free. The entire appeal of an agentic coding tool is that it keeps moving while you look away, and Manual mode reintroduces friction by design — a prompt for every consequential step, a badge reminding you that Claude is waiting. For developers who had grown comfortable letting Claude run, the new default will feel slower. Anthropic's bet is that the safe option should be the one you fall into, and the fast one the one you consciously choose, rather than the reverse. For a tool that can write files, execute shells, and open network connections on a developer's machine, that inversion of defaults is the whole point.

It also reframes a debate the industry has largely dodged: whether autonomy should be opt-in or opt-out. By moving its own default, the most-used AI coding agent has effectively taken a position — and set a reference point competitors will be measured against.

## What to watch next

Three things. First, whether enterprises make Manual mode mandatory via managed settings and MDM policy, hard-locking auto mode out of regulated environments. Second, whether Anthropic's rivals — OpenAI's Codex, Google's Gemini tooling — follow with safer defaults or lean the other way toward speed. And third, whether the productivity cost proves real enough to push power users straight into auto mode, quietly recreating the exposure the Manual default was meant to close. The default has moved. Whether behavior moves with it is the open question.
