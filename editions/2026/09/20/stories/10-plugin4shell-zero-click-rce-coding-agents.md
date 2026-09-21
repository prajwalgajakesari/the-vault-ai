All four major AI coding agents built the same safeguard against a compromised plugin: pin it to a 40-character git commit hash and only run the code at that hash. All four then skipped the same step. None checked, after checkout, that it had actually landed on the commit it asked for. A branch named after the hash walked straight through.

That is Plugin4Shell, disclosed September 17 by Or Nevo, Dor Granat and Niv Hoffman of AIR Security, a Tel Aviv startup that left stealth September 1 with $50 million in seed funding and sells, not coincidentally, plugin vetting for enterprise agents. AIR built exploits against Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI in May and disclosed in June. The scorecard: two patches, one deprecation, one vendor arguing the bug is not its problem.

"The agent checks out the exact commit the marketplace pinned but never verifies it landed there, so an attacker who controls the plugin's repo makes the checkout resolve to malicious code while the pin still looks honored," they wrote. "The result is zero-click remote code execution."

## The bug is git, and it is old

Claude Code, Codex and Copilot install a marketplace plugin by cloning its repository and checking out the pinned SHA. Git treats a 40-hex string as either a commit object or a ref name, and when both exist it prefers the ref, printing an ambiguity warning and checking out the branch anyway. An attacker who controls the repository creates a branch named for the pinned hash, makes it the default, and fills it with whatever they like. The agent reports a successful install at the reviewed commit. The working tree holds something else.

Gemini CLI reaches the same place by a different road. It fetches the pinned commit and then checks out FETCH_HEAD, git's reserved name for what was just fetched. If the repository's default branch is itself named FETCH_HEAD, the checkout resolves to the branch and the fetched commit is discarded. Rules against hash-shaped names do nothing here.

AIR's recommended fix is a single assertion: after checkout, compare the commit actually in the working tree to the pin and abort on mismatch. OpenAI's public Codex fix describes the same failure: git "can interpret a requested commit SHA as a branch name," which can make a plugin source "materialize a different commit than the one it pinned." That shipped in Codex 0.146.0, verified August 12. Anthropic confirmed a fix in Claude Code 2.1.179 on June 17; its release notes do not mention it.

Auto-update makes this zero-click. Claude Code and Codex refresh installed plugins in the background by default. Ship a benign plugin, wait for adoption, push a still-benign version bump the marketplace re-pins, then create the poisoned branch named for the new pin. The re-pin triggers everyone's background update on machines whose owners never saw a prompt.

## Google deprecates, Microsoft goes quiet

Google told AIR on August 4 that Gemini CLI is deprecated and will get no fix; users are pointed to Antigravity, which has no marketplace SHA pinning to bypass. Existing installs stay vulnerable. Microsoft, per AIR, never answered the June disclosure. GitHub did. "To prevent abuse of SHAs, GitHub does not allow users to create branch or tag names that resemble commit SHAs," a spokesperson said. "This mitigation ensures the reported vulnerability cannot be exploited on GitHub."

That matters more than AIR's headline suggests. The Hacker News found every plugin in the built-in catalogs for Claude Code and Copilot points to a GitHub repository, and auto-update is on by default only for those catalogs. A developer using only stock marketplaces is not exposed to the branch-name variant.

AIR's rebuttal is that the agents officially support other hosts. "Marketplaces can also be hosted in other platforms such as Bitbucket," the team told The Register, and Anthropic's documentation lists Bitbucket and self-hosted git as valid backends; Copilot supports them too. A host's naming rule is a mitigation on one platform, not a client fix, and it does not touch the FETCH_HEAD variant. As of September 18, no CVE had been assigned, no vendor had published an advisory, and there was no evidence of in-the-wild exploitation.

## Why It Matters

This is the third act of a campaign AIR has run all year. In June it planted a skill that passed marketplace review and reached roughly 26,000 agents. In SkillJacking it found 925 skills already in use whose upstream repositories had been hijacked, reaching 134,000 agents. SHA pinning was the industry's answer to exactly that rug-pull. Four engineering teams implemented the answer without the step that gives it meaning.

The people most exposed are the ones who did the most. A team that hand-reviews each plugin and pins the reviewed commit is relying entirely on the pin, and because the pin is resolved inside the agent, no marketplace can enforce it. The only complete fix lives in the client, and for two of four clients there is none.

The response pattern is its own lesson. Anthropic fixed it in 11 days. OpenAI took about two months. Google retired the product. Microsoft, whose Copilot reaches almost 90 percent of the Fortune 500 by its own count, did not reply; its platform arm narrowed the question to repositories it hosts. Four vendors, four definitions of "handled."

"Millions of agents affected" is AIR's estimate, and the company selling the remedy wrote the severity language. The bug is real; OpenAI's patch confirms it. But the blast radius is narrower than the branding implies, and wider than GitHub's statement does.

## What to Watch

The immediate job is inventory: upgrade Claude Code below 2.1.179 and Codex below 0.146.0, prune unused plugins, and check every plugin's repository host, since anything outside GitHub gets no help from naming rules. Then watch whether Microsoft ships a Copilot client fix now that the disclosure is public, whether Google's enterprise Gemini CLI channel quietly backports one, and whether a CVE lands. The longer question is whether marketplaces start requiring post-checkout verification, or whether AIR's fourth act writes itself.
