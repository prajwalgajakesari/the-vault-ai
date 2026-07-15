Anthropic spent the first two years of the generative-AI boom selling Claude as a brilliant solo assistant, a chat box you talked to alone. On July 14, the company finished dismantling that framing. In a bundle of updates rolling out across Team and Enterprise plans, Anthropic turned Claude Artifacts into a shared workspace: interactive outputs can now be published to public links that anyone can open without a Claude account, teammates can edit the same Claude Code artifact together, and users can spin up those artifacts by summoning the model directly inside Slack with Claude Tag.

The through-line is a bet that the future of workplace AI is not private, but collaborative. Or, as Slack general manager Rob Seaman framed the strategy behind the Slack integration when it debuted, the goal is "making AI multiplayer. Instead of a private back-and-forth, Claude Tag shows up in the open."

## What actually shipped

The July release breaks into three connected pieces. First, public sharing: Claude Artifacts, the live interactive outputs the model generates, can now be published beyond an organization's walls. A user can build a dashboard, a lightweight internal app, or an interactive HTML page and hand out a link that renders for viewers who have never logged into Claude. Crucially for nervous IT departments, public sharing is off by default on Team and Enterprise plans. Members can share artifacts only inside the organization until an account Owner flips the switch.

Second, collaborative editing. The same Claude Code artifacts now support true multiplayer iteration, so multiple team members can work on one shared project rather than emailing files back and forth or pasting outputs into a doc. Administrators keep control over who can touch what through organization-wide settings.

Third, and tying it together, is Claude Tag, the feature that lets anyone in a Slack channel pull the model into a thread by typing @Claude. That agent, running on Anthropic's Opus 4.8 model, can now build and modify artifacts inside the conversation where the work is already happening, drawing on shared organizational context, connected tools, and code repositories.

## From a research preview to a workspace

Claude Tag itself is not brand new. Anthropic launched it in beta on June 23 for Enterprise and Team tiers, positioning it as a persistent AI teammate rather than a chatbot you visit. In a channel, any member can delegate a task, review the model's output, and pick up a thread someone else started. With an "ambient" configuration switched on by an admin, the agent monitors threads asynchronously, flags priority items, and tracks unresolved work across multi-day stretches without a human prompting it each step.

Cat Wu, who leads product for Claude Code at Anthropic, has argued the shift is less about new model capability than about the interface. "The form factor of being able to tag it the same way that you would a coworker is really powerful," Wu said, describing how the tag turns a capable model into something that behaves like a colleague you can hand something off to. Wu has said she connected her own Claude Tag agent to her email archive so it could triage incoming messages, categorize urgent ones, and ping her in Slack.

Anthropic is also eating its own cooking, and it keeps saying so. The company reports that Claude now generates 65% of the code used internally by its own product teams, a figure it cites as proof that AI-authored, team-shared artifacts are already a working practice rather than a demo. The July updates arrived alongside a broader push, including expanded Claude Code and Cowork access on web and mobile and fresh Microsoft 365 integrations, meaning Claude now reaches into both Slack and Microsoft's productivity suite.

## Why this matters

The strategic logic is about stickiness. A personal chatbot is easy to swap out. A workspace where dashboards live, where the whole team edits shared artifacts, and where an agent sits inside the channel tracking tasks is far harder to rip out. That directly targets the same enterprise ground OpenAI is courting with ChatGPT Enterprise and its Canvas collaborative editor, and Google is defending with Gemini baked into Workspace's enormous installed base.

Anthropic is playing from a position of momentum. Ramp's May 2026 AI Index put Anthropic's enterprise adoption at 34.4%, edging past OpenAI's 32.3%, and the company's recent $65 billion Series H lifted its post-money valuation to roughly $965 billion. Emphasizing admin controls, scoped identities, and audit logs is a deliberate signal that Anthropic wants to win the buyers who care about governance, not just the developers who love the model.

There is an irony worth noting. Claude Tag rides on Slack, which is owned by Salesforce, itself an AI competitor. Anthropic's most intimate workplace foothold sits on a rival's platform.

## What to watch

The open questions are about trust, not capability. As always-on agents gain the ability to read chat histories, connect to email, and modify shared code repositories, a single misconfigured permission boundary could leak proprietary context into the wrong channel, and asynchronous execution removes a human check from intermediate steps. Watch whether Anthropic extends public sharing and multiplayer editing to lower tiers, whether large enterprises actually enable public links or keep them locked down, and how Salesforce responds to a competitor becoming the default AI teammate inside its own product.

## Sources

- [Crypto Briefing: Anthropic enhances Claude with public sharing and team editing features](https://cryptobriefing.com/anthropic-claude-sharing-team-editing-features/)
- [Progressive Robot: Anthropic Enables Public Artifact Sharing and Team Editing in Claude](https://www.progressiverobot.com/2026/07/14/anthropic-enables-public-artifact-sharing-and-team-editing-in-claude/)
- [AI News: Anthropic drops 'workplace AI agents' directly inside Slack](https://www.artificialintelligence-news.com/news/anthropic-slack-workplace-ai-agents/)
