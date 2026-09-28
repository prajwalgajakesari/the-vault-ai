# Microsoft and KAIST's ProgramDistill Finds Frontier Agents Still Fail Most Full Web-App Workflows

Give the best coding agent available a working web app, a bare scaffold and a browser, and ask it to rebuild the product. It will get about half of the end-to-end workflows right. That is the result of **ProgramDistill**, a new benchmark from KAIST, Microsoft Research Montréal and Microsoft AI. When agents had to rebuild whole applications, OpenAI's GPT-6 Astra passed **49.2%** of cumulative workflows. Anthropic's Claude Opus 5 passed **28.8%**.

The paper, *ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE Tasks*, is led by KAIST's Jeonghye Kim, who did the work as a research intern at MSR Montréal. Co-authors include Minseon Kim, Matheus Pereira, Marc-Alexandre Côté, Alessandro Sordoni, Xingdi Yuan and Zhengyan Shi of Microsoft Research Montréal, and Young Jin Kim of Microsoft AI. It targets a gap in how coding agents are tested today.

"Coding agents are typically evaluated with desired behavior specified through issues or instructions," the authors write in the abstract. "In practical web development, however, agents may need to infer behavior from working software and implement it in an incomplete application."

## How the Benchmark Works

In ProgramDistill, the agent can click through a live reference app but cannot see its source code. It then has to reproduce the same behavior in an editable copy. Grading looks only at behavior, not code. The rebuilt app passes if it does the same thing as the reference when the same browser actions are replayed, even if its code looks nothing like the original.

The tasks are built automatically by a multi-agent pipeline the team calls **mine-craft-patch**. In the *mine* stage, LLM agents explore a working app and record replayable traces of browser actions and success signals. In the *craft* stage, other agents delete the code behind selected behaviors. Build and replay checks then confirm three things: earlier behaviors still work, the target behavior now fails, and the original "gold patch" fixes it. In the *patch* stage, the coding agent under test tries to repair the app. The team's blog post says the same replay mechanism checks the original app, the masked app and the repair "without LLM intervention."

Across 26 open-source applications, the pipeline found **1,975 replay-verified behaviors** and built **4,063 tasks** "without human intervention," according to the paper. Of those, 2,862 are atomic tasks that remove a single behavior. The other 1,201 are cumulative tasks that remove a chain of dependent behaviors. For example, a card has to exist before it can be moved, and a board has to exist before the card. The number of chained behaviors is called restoration depth, and it is the benchmark's difficulty setting.

## The Results

The team tested nine frontier models from OpenAI, Anthropic, Google DeepMind and xAI on **ProgramDistill-300**, a 300-task suite at depths 1 through 8. Scoring is binary: a cumulative task passes only if every target in the chain passes.

Astra led with **84.3%** overall, ahead of Opus 5 at 68.7% and Sol at 60.7%. Performance fell steeply with depth. Astra solved every depth-1 task but only **64.0%** at depth 8. Opus 5 dropped from 96% to **32%**, and Sol from 92% to 32%.

The harder test is rebuilding a whole application. Here the agent gets only a minimal scaffold, a product-level description of what the app should do, and browser access to the reference. Across 12 apps, each agent was scored on 590 individual behaviors and 413 cumulative workflows. Astra recovered 58.98% of behaviors and 49.15% of workflows. Opus 5 recovered 42.03% and 28.81%, and Sol 33.39% and 21.07%. These runs averaged about 700 agent steps and went as high as 1,921.

The researchers also studied why agents fail. They looked at 977 failed behaviors across 36 reconstruction runs. In **59.2%** of cases, the agent never observed the behavior in the reference app at all. In 27.9%, it produced the wrong state, route or result, and in 11.1%, the output had the wrong observable form. Only 1.8% were behaviors the agent saw but never built. "An application that runs is not necessarily an application that matches the reference," the team writes.

How the agents worked also mattered. Astra checked far more and edited far less than the others, averaging 96.3 observations of its own app per task but only 9.9 edit or write steps. Claude Opus 5 got more browser-state feedback than Astra yet recovered fewer behaviors, suggesting that what counts is re-checking the right workflow after the final change.

## Why It Matters

Most well-known coding benchmarks give an agent a written issue and a test suite. ProgramDistill measures something closer to how software actually gets built. Developers often work from a prototype, an earlier version or a competitor's product, not a complete spec. By that measure, today's best agents still come up short. Building individual features that work is much easier than getting those features to work together as a whole product.

The failure breakdown shows where to improve: most misses come from shallow exploration of the reference, not from an inability to write code. From depth 1 to depth 8, the code to restore grows more than 9x, yet agents spend less observation and editing effort per behavior.

Because tasks are generated automatically and difficulty can be tuned, ProgramDistill can also be used to train agents, not just test them. Restoration depth gives a natural curriculum, and replay checks give a reward signal that does not depend on an LLM judge.

## What to Watch

The team links a Hugging Face dataset under Microsoft's organization and a public leaderboard, though the abstract says a full public release is still in progress. The authors plan depth-based curriculum training with replay-based rewards, and an extension to multimodal agents graded on visual accuracy as well as behavior. The next frontier model launches will show whether the 49.2% ceiling on full-app workflows starts to move.
