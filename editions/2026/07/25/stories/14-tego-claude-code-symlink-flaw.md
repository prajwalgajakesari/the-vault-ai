# Researchers Say a Booby-Trapped Repo Can Make Claude Code Leak Files Silently

A security firm says an ordinary-looking code repository can be rigged to make Anthropic\s Claude Code read a sensitive file from outside a project and ship its contents to the network before the AI even starts working, no code execution and no cooperation from the model required. Anthropic says that behavior falls inside the tool\s documented threat model, and closed the report without a fix.

The disclosure, published July 24, 2026 by Tel Aviv-based Tego AI, is the company\s second piece of Claude research in a week, and it lands squarely on a question the industry has been circling for months: as developers hand more autonomy to agentic coding tools, where exactly should the security boundary sit?

## What Tego says it found

Claude Code is Anthropic\s agentic command-line coding assistant. It reads a project\s files, plans changes, and can edit code and run commands on a developer\s behalf. To orient itself, it loads a memory file named CLAUDE.md at startup, and that file can pull in other content through an @import directive.

According to Tego, an attacker can commit a normal-looking CLAUDE.md whose @import points at a symbolic link stored in the repository, an innocuous file that GitHub itself openly labels as a symlink to a path such as /etc/passwd. When a developer clones the repo and launches Claude Code, the tool follows the link to whatever file it resolves to, including files well outside the project directory, and folds that file\s contents into the very first request it sends to the model.

The result, Tego says, is that the out-of-project file leaves the machine as part of that outbound request. No tool call fires, no file-edit approval appears, and the dialog Claude Code normally uses to catch out-of-project reads never shows, because the check inspects the in-repository link name rather than the external path the link actually resolves to. Tego adds that a repository-committed settings file can redirect Claude Code\s outbound endpoint to a server the repo author controls, meaning the leaked data need not even go to Anthropic.

"Context is whatever gets sent to the model, and the model is a network endpoint like any other," said Tomer Niv, Head of Research at Tego AI, in the company\s disclosure. "Clone a repo, answer the same 	rust this folder?\ question you always answer, and a file from outside that repo can leave your machine on the first request, with no code execution, no cooperation from the model, and no server the attacker has to run."

The exposed file only needs to be readable by the developer\s own account, a realistic condition, Tego notes, in CI runners, containers, and standardized developer images where sensitive paths are predictable. The company says it confirmed the behavior against Claude Code v2.1.x.

## An old bug class on a new code path

Tego frames the finding less as a novel exploit than as a gap in earlier fixes. The same underlying defect, a security check reading one path while the filesystem follows a symlink to another, was patched in Claude Code twice before, tracked as CVE-2025-59829 and CVE-2026-25724, both reported through HackerOne and resolved in the permission subsystem. Tego says the same flaw survived on a third code path the earlier patches never reached: the startup memory loader, which is also the path that places what it finds onto the network before the model acts.

Tego reported the issue to Anthropic through HackerOne in July 2026. Anthropic closed it as "Informative," a HackerOne status that acknowledges a report without treating it as a vulnerability warranting a fix.

## Anthropic\s position

Anthropic\s rationale, as relayed in Tego\s write-up, was consistent: under the Claude Code threat model, the "trust this folder" dialog is the security boundary, and accepting it already grants a project broad read, edit, and execute access. By that logic, a trusted folder reading a file the developer\s account can already access is not a boundary violation. Notably, Tego does not dispute that Anthropic applied its stated model consistently, its argument is with the terms of that model, not with whether Anthropic followed them.

"We understand the model. Our disclosure is an argument about its terms," Niv said. "A single 	rust this folder\ click is being asked to carry an enormous amount of weight, at the least informed moment possible, before you have seen anything the repository does." A single click, he argued, "cannot tell the difference between un my code\ and ead my SSH key and mail it out," and in many setups that trust decision was inherited from a parent directory and never shown for the specific repository at all.

## Why it matters

The dispute is a clean illustration of the central tension in agentic tooling. These assistants are useful precisely because they act with the user\s privileges, but that same breadth makes a single up-front consent a blunt instrument. Symlink attacks are decades old, and Tego credits Anthropic with hardening Claude Code against them in good faith more than once. What is new is the delivery vehicle: a Git clone, one of the most routine actions in software development, combined with a coding agent that treats repository files as trusted instructions. That is the same supply-chain and prompt-injection surface researchers have warned about across the agent ecosystem, and it echoes Tego\s prior finding that Claude\s Slack integration could be steered by plain "@Claude" text, which Anthropic also disputed.

Both companies may be right on their own terms, and that is the uncomfortable part. Anthropic is defending a documented, internally coherent boundary. Tego is arguing that the boundary, as documented, asks users to authorize too much with too little information.

## What to watch

Watch whether Anthropic revisits how the "trust this folder" prompt is presented, especially inherited trust and out-of-project reads, and whether enterprise buyers start demanding runtime authorization layers that sit between an agent and sensitive systems, the market Tego is building for. Tego, which says it operates in stealth, has signaled more disclosures are coming. The larger question its research keeps pressing is authorization: who, or what, is allowed to instruct an AI agent, and reach the data it can touch.