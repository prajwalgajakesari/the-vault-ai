# COMPASS Uses Evolving Context to Push AI Agents Through Long-Horizon Tasks

When you ask an AI agent to do something genuinely hard — track a soccer player's yellow-card pattern across two halves of a season, cross-check it against referee records, and reconcile the timing — the agent doesn't fail because it can't search the web. It fails because, twenty steps in, it has forgotten what it was looking for. The critical clue is buried somewhere in a mountain of accumulated tool output, and the model is now distracted by noise it collected along the way.

That failure mode is the target of COMPASS, a framework from researchers at the University of Virginia and Google (the work was done during an internship at Google). In their paper, "COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving Context," authors Guangya Wan, Mingyang Ling, Xiaoqi Ren, Rujun Han, Sheng Li, and Zizhao Zhang argue that the bottleneck for long-horizon agents isn't reasoning power — it's context management. Their fix is to stop feeding agents raw history and instead maintain a distilled, evolving brief of what actually matters.

## The Long-Horizon Context Problem

Long-horizon tasks (LHTs) demand sustained reasoning across many tool calls while the agent maintains a coherent plan and adapts to surprises. The problem is that small errors compound. An ambiguous search result or a faulty API call early on can cascade into systematic failure, and even the most capable closed-source models struggle to keep a plan coherent over extended horizons.

The paper pins this on how agents handle their own transcripts. As the history grows, the model either overlooks critical evidence it already found or gets pulled off course by irrelevant material. It stops replanning. It stops reflecting on earlier mistakes. The raw context window becomes a liability rather than an asset — the agent is, in effect, drowning in its own notes.

## How COMPASS Works

COMPASS — short for Context-Organized Multi-Agent Planning and Strategy System — is described as a lightweight hierarchical framework that splits three jobs that a single agent normally tries to juggle at once:

- A **Main Agent** does the tactical work: reasoning and calling tools.
- A **Meta-Thinker** provides strategic oversight, monitoring progress and issuing interventions — telling the agent when to persist with a plan, when to pivot, and when to conclude.
- A **Context Manager** curates the evolving context, maintaining concise, relevant progress briefs tailored to different reasoning stages.

The key move is architectural separation. Rather than bolting "think about your reasoning" and "keep the relevant context" onto one model as tools, COMPASS externalizes those roles into dedicated agents. The Context Manager continuously distills the growing transcript into a compact brief, so the Main Agent reasons over what matters instead of the full raw log — the "evolving context" at the heart of the method.

## Results

The team evaluated COMPASS on three benchmarks built for deep-research-style tasks that typically require 20-plus reasoning-action steps: GAIA, BrowseComp (1,266 web-navigation tasks with entangled facts to verify), and Humanity's Last Exam (HLE). Across all three, COMPASS improves accuracy by up to 20% relative to both single-agent and multi-agent baselines.

On Gemini 2.5 Pro, COMPASS reached 35.4% on BrowseComp, 67.8% on GAIA, and 31.7% on HLE — compared with 16.8% / 58.6% / 14.8% for a plain search-and-browse single agent, and beating stronger multi-agent baselines like Agent-as-a-Tool (31.8% on BrowseComp). Gains were most pronounced on BrowseComp, where sustained multi-source navigation is hardest.

The researchers also introduce a test-time scaling extension, COMPASS-TTS, that uses parallel sampling to push results to 43.7% on BrowseComp, 72.1% on GAIA, and 35.2% on HLE — competitive with established deep-research agents. Separately, a post-training pipeline distills the context-management role into a smaller model (Context-12B), achieving roughly 30% token reduction while matching the accuracy of a larger model.

## Why It Matters

The industry has largely tried to make agents better at long tasks by making the base model bigger or handing it more tools. COMPASS points to a cheaper, orthogonal lever: treat context as something to be actively engineered, not passively accumulated. If a distilled, evolving brief can deliver up to 20% accuracy gains — and if the curation itself can be offloaded to a 12B model at 70% of the token cost — that reframes context management as a first-class design problem for anyone building agents that run for dozens of steps.

## What to Watch

The authors are candid that their evaluation emphasizes controlled QA-style reasoning environments as a proof of concept, rather than open-ended real-world workflows. The open questions: does the Meta-Thinker plus Context Manager split hold up on messier, tool-heavy tasks like software engineering or operations, where "the relevant context" is far harder to define? And how much of the gain survives when the base agent is already strong, as the narrower Gemini 2.5 Flash margins hint? Watch whether distilled context managers like Context-12B become a standard component in agent stacks.
