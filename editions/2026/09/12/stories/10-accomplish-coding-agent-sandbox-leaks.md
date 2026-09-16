Turn the sandbox on in Claude Code and it stops asking permission. That is the feature: once Seatbelt wraps the Bash tool, the harness assumes commands are contained and drops the prompts. It is also what made a full escape silent this summer. A researcher at a stealth Tel Aviv startup opened a booby-trapped repository with the sandbox on and permissions set to the strictest mode, sent one short message, and watched a command from that repo execute on his Mac — outside the box, as his own privileged user, no prompt anywhere.

The startup is Accomplish, founded by Or Hiltch, Amit Avner and Guy Zipori. Over the past two months it quietly reported sandbox escapes to Anthropic, OpenAI and Cursor maker Anysphere, and this week began publishing them. Cursor's fix landed in about a week, OpenAI's in August. Anthropic's took roughly 50 days and some 30 releases, per [Upstarts Media](https://www.upstartsmedia.com/p/accomplish-claims-leaky-sandboxes-in-claude-codex-cursor), which broke the story September 10.

"There's a lot of talk about security now," Hiltch, Accomplish's CTO, told Upstarts' Alex Konrad. "It doesn't really reflect in how they actually build products."

## What "sandboxed" actually means

Claude Code and Cursor CLI both use per-tool sandboxes on macOS: a Seatbelt profile wraps the shell tool, confining it to the workspace and denying it `$HOME` and the network. Everything else the harness spawns runs outside that profile — including its own `git`, which both run constantly in the background to index files, resolve `@`-mentions and read repo status.

Git is not an inert reader. A config key called `core.fsmonitor`, read straight from a repository's `.git/config`, is executed as an external program whenever git inspects the working tree. So a repo setting `core.fsmonitor = .tools/fsmon.sh` gets its script run by the agent's own background git, on the host, with the user's full authority. Accomplish named the class Beltdown.

## The escape, step by step

Anthropic had partially anticipated this: most of Claude Code's harness git calls already passed flags blanking `core.fsmonitor`. Accomplish's [write-up](https://www.accomplish.ai/blog/beltdown-escaping-the-claude-code-sandbox/), by principal security researcher Oren Yomtov, chains four misses. The hardening was per-call, and one call was missed — `git ls-files`, the file-index refresh. `.git` is write-protected, but only at the project root; the Seatbelt rule blocking a *nested* folder from being renamed to `.git` was absent, so a setup script could build a poisoned config under another name and rename it in a subfolder. The harness was assumed to run git at the project root; it actually runs wherever the Bash tool last worked. And the refresh doesn't fire on its own — so the script's last line asked Claude to read a build report in that subfolder, which triggered skill auto-loading, which triggered the index refresh, which ran the unhardened git command in the poisoned directory.

Cursor's version, published a day later by Hiltch himself, required none of that. Cursor CLI ships a real sandbox binary, `cursorsandbox`, and applies it to model-generated shell commands. Its internal git spawns went through plain `child_process.spawn("git", …)` with no policy and no hardening flags at all. The proof-of-concept was an unzip and one read-only prompt that told the model not to run shell commands. The payload ran anyway, parented directly by the `cursor-agent` node process, `CURSOR_SANDBOX` unset and `$HOME` writable.

## A week, versus fifty days and a partial fix

Anysphere fixed it structurally. Rather than prepending a flag at each call site, Cursor CLI build `2026.08.04-aaa8809` sets `GIT_CONFIG_COUNT=4` as environment variables on every git spawn, neutralizing `core.fsmonitor`, `core.hooksPath`, `core.attributesFile` and bare-repository handling at once. Command-scope config outranks repo config, so no call site can forget.

Anthropic's timeline is more interesting than the 50-day headline number. Accomplish reported Beltdown on July 13, and says Anthropic triaged it the same day. A first hardening shipped August 6 in Claude Code 2.1.223 — and was incomplete. "It missed some of the git calls, so the escape moved to another one," the write-up notes. The full fix came August 26 in 2.1.247: 44 days from report, with a live bypass in between.

Anthropic and Cursor did not comment on the record to Upstarts. OpenAI, which patched two Codex findings, said: "We thank the researchers for contacting us and sharing their findings. We addressed both issues in August, and we're continually strengthening our sandboxes, including tightening controls on where agents can write files and expanding testing of those protections across platforms."

## The politics of the timeline

Accomplish sells agent isolation — it runs the whole agent, git included, inside a host-controlled VM — so every one of these posts ends in a product pitch. Discount accordingly. But it isn't the first time the startup has hit this wall with Anthropic. Its July 23 SharedRoot report, chaining an unprivileged user namespace, an autoloaded kernel module and a read-write mount of the whole host filesystem into a Claude Cowork VM escape, was closed as "Informative": the CVE fell inside the program's 30-day publication window, and the hardening items were read as defense-in-depth. Defensible bounty triage. Cold comfort to a developer whose laptop is the blast radius.

The pattern is wider than Accomplish. Pillar Security published seven findings in July across Cursor, Codex, Gemini CLI and Antigravity, including CVE-2026-48124 — a workspace-controlled `.claude` hook config in Cursor Desktop, fixed in 3.0.0 — and a Codex CLI allowlist that trusted `git show` by name while the real invocation wasn't read-only, patched in v0.95.0. Google downgraded both Antigravity findings.

## What to watch

First, whether any vendor moves from per-tool sandboxing to process-level confinement, where every child the harness spawns inherits the boundary — the design Antigravity and Grok Build already use. Per-call hardening is a coordination problem that reopens with every spawn added to a fast-shipping codebase.

Second, whether Anthropic's response time compresses. Thirty releases is a lot of velocity to have while a triaged, reproducible host-code-execution path stays open six weeks. Hiltch's sharper question is worth putting to all three labs: "If these frontier models are so good, how come they're not finding these critical vulnerabilities in their own products?"
