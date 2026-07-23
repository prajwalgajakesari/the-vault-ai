Anthropic wants you to stop typing instructions to your AI and start showing it what to do instead.

On July 21, the company quietly began rolling out a feature inside its Claude "Cowork" desktop app that lets users record their screen while narrating a task out loud, then have Claude convert the recording into a reusable "skill" it can perform on its own later. The option, labeled "Record a Skill" and surfaced in the app's early messaging as "Teach Claude a skill," appears under the plus (+) menu in Cowork's chat box, alongside existing tools for adding files, browsing skills, and connecting apps. It is live now for Pro, Max, and Team subscribers.

The pitch is disarmingly simple. You hit record, do a task the way you normally would — organizing invoices in a spreadsheet, renaming a folder of image files, assembling a weekly sales report — and explain your reasoning as you go. Claude watches the screen activity, the clicks, and the keystrokes, listens to the commentary, and synthesizes all of it into a structured skill saved to your library. The next time the job comes up, you ask Claude to run the skill rather than re-explaining every step.

"It's a little like training a new coworker who keeps forgetting the workflow," Android Authority's Shimul Sood wrote of the status quo the feature is meant to replace, describing the familiar cycle of re-typing instructions, saving detailed prompts, and uploading documents full of steps only to watch the model miss one anyway. Sood, who tested the feature on a Pro account, reported it was already live and accessible in a few clicks.

That framing — teaching by demonstration rather than specification — is the heart of the update. Anthropic's existing Skills system, launched in October 2025, already lets Claude load reusable, filesystem-based instructions packaged in a `SKILL.md` file that turns a general-purpose model into a specialist for a given task. But building those skills has largely meant writing them: describing a workflow in structured text or code. The new recorder collapses that authoring step. Instead of documenting a process, you perform it once and let the model write the skill for you.

## The enterprise angle

Anthropic has spent months positioning Cowork as a "digital teammate" rather than a chatbot, and the recording feature leans hard into a workplace problem that has dogged AI adoption: most of what employees actually do is never written down. Companies run on thousands of undocumented micro-processes — the quirky way one team reconciles a report, the specific order in which files get renamed and filed, the tacit rules for what "done" looks like — all of it locked in individual heads and impossible to hand to an AI through a prompt.

Learning by demonstration is a bet that this tacit knowledge is easier to show than to describe. An analyst framing that circulated alongside the launch put it plainly: the bottleneck to workplace AI has never been raw model capability so much as the labor of translating human routines into machine-readable instructions. A screen recorder with a microphone sidesteps that translation entirely.

There is precedent for the ambition. Since Anthropic introduced Agent Skills, the company says more than 30 AI tools have adopted the open standard, so a single skill file can, in principle, travel across Claude, Cursor, and other environments. Turning demonstrations into that same portable format is a natural extension.

## Why it matters

The gap between what AI can theoretically do and what it actually does inside real companies has always been an adoption problem, not just a capability one. Enterprises have spent the past two years discovering that a brilliant model is useless if nobody can be bothered to write down how their job works — and knowledge workers, reasonably, do not want to spend hours documenting processes they perform on autopilot.

Learning by demonstration attacks that friction directly. If teaching an AI a workflow costs one narrated run-through instead of an afternoon of prompt engineering, the economics of automating long-tail internal tasks change. A finance clerk who has never touched code could, in theory, hand off a recurring reconciliation. The skill, once captured, becomes an asset the organization owns rather than institutional knowledge that walks out the door when an employee leaves. That is a meaningfully different value proposition from a faster autocomplete.

It also reframes the competitive field. Meta shipped Muse Spark 1.1 on July 9, an agentic model built for multi-app desktop workflows with computer-use capabilities, undercutting rivals on price. OpenAI has been consolidating its products toward a single "super app." Anthropic's answer is not a flashier agent but a cheaper on-ramp for teaching one — a distribution strategy as much as a technical one.

## What to watch

The obvious hurdle is trust. Recording your screen — with everything visible on it — and narrating your reasoning means handing an AI vendor a rich stream of exactly the sensitive material enterprises are most nervous about. How Anthropic handles storage, redaction, and whether demonstrations are used for training will shape whether IT departments greenlight the feature at all.

Watch, too, for reliability. A demonstration captures what a user did once; it does not guarantee Claude generalizes correctly to the messy edge cases of the tenth run. And with Meta and OpenAI racing to make computer-use agents both cheaper and more capable, the differentiator may not be who can watch your screen — but who employees actually trust to.
