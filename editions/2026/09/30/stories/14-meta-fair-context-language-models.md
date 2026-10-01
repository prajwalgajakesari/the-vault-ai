# UW and Meta Researchers Unveil Context Language Models That Edit Their Own Memory, Beating Hand-Built Harnesses With Less Compute

Agents that run for hours fill up their context windows. The usual fix is a harness, engineer-written code that decides what to summarize, drop or keep. A new paper from researchers at the University of Washington and Meta, with code published under the facebookresearch GitHub organization, tries something simpler. It gives the model its context as a file and lets it make any edit it wants. On long-horizon benchmarks running from hours to a full day, the approach beat the best hand-built strategies the authors tested against, and it usually used less compute.

The paper, "Context Language Models," is dated September 29 and is led by Rulin Shao. Its 13 authors come from UW, Meta Superintelligence Labs, MIT and Trillium Labs, and include Luke Zettlemoyer, Mike Lewis, Wen-tau Yih, Nathan Lambert and Pang Wei Koh. "We introduce Context Language Models (CLMs), language models that natively manage their own context," the abstract states. "We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file."

## How it works

In a standard language model, context only grows, and a harness steps in when it gets too long, usually summarizing older history at a fixed threshold. Newer methods give the agent a few fixed tools for compaction, offloading or retrieval. The CLM approach gets rid of that fixed menu. The researchers copy the live context into a storage space the model can write to. The model can keep appending tokens as usual, or it can use ordinary Bash commands to edit the file anywhere. Each change is synced back into its working context before the next turn. Models can delete stale search results, rewrite their own plans or keep notes updated in place. A swarm of agents is simply several context files, and spawning a subagent means creating one.

The authors connect the idea to Rich Sutton's well-known 2019 essay on AI research. "Our findings echo The Bitter Lesson," they write, arguing that "we should let LMs search for and learn better strategies that go far beyond existing human priors."

The zero-shot results use off-the-shelf models with no extra training. On BrowseComp-Plus, a deep-research benchmark, Qwen3.6-27B running as a CLM with a 32K context limit scored 59.4%. That is 11.4% higher in relative terms than the strongest baseline, Codex-style summarization, and it used 21.5% fewer of what the authors call prefix-reuse FLOPs. On EdgeBench-10, where agents optimize a code repository for up to 12 hours, the CLM scored 44.6 against 42.3 for summarization, using 179 petaFLOPs per trial instead of 437, which is 59% less compute. On Software World, a test running more than 24 hours in which six agents jointly optimize interdependent Python repositories, the CLM swarm delivered 65% greater downstream speedup than a summary-based swarm at the same spend.
## Learning to manage memory

The authors argue that once context management is something the model does itself, it can be taught like any other skill. Adding a single sentence to the task prompt was enough to change the model's policy, for example telling it when to compact or to back up its context first. A skill-evolution loop, in which a proposer model drafts better instructions from the agent's own runs, improved held-out accuracy on the team's ContextBench by up to 35.9 points while cutting compute. ContextBench itself is listed as "coming soon" in the repository.

Training helped further. With online reinforcement learning and a reward that favors successful runs that use less compute, Qwen3.5-9B went from 28.8% to 42.5% on BrowseComp-Plus, a 47.6% relative gain. Before training, the small model trailed a summary harness by six points. After training, it matched a summary harness trained with the same recipe while using 1.34 petaFLOPs per question instead of 2.19.

## Analysis: the caching bill comes due

The idea has a real cost, and the paper says so. Production inference servers save money by caching the computed state for the unchanged beginning of a prompt. An edit in the middle of the context breaks that cache, so every token after the edit has to be recomputed. The paper notes that such edits pose "new challenges for existing serving systems, which typically only reuse cached states for matching prefixes, forcing re-prefilling after in-the-middle edits." This is why the team reports compute in prefix-reuse FLOPs, a metric that counts re-prefilling costs instead of hiding them.

Their answer is Suffix Cache Reuse, released as a patch to the SGLang serving engine. It reuses cached state for tokens that survive after an edit. The authors report that it cuts server-side compute by 35% compared with standard SGLang at matched performance. Self-hosted teams can use that today; teams on hosted APIs, whose caches still assume an unchanged prefix, cannot yet.

For context engineering, much of which today means hand-tuning compaction thresholds and summary prompts, this is a direct challenge. The authors propose a "harness-to-CLM pipeline" that would distill those strategies into model weights, treating harnesses as procedural memory the model later absorbs. If that holds, a lot of orchestration code turns into training data.

The paper also raises a security concern itself. "Editable context can become another channel through which prompt injections or self-generated instructions persist across turns," the authors write. A model that can rewrite any line of its context could be tricked into rewriting its own instructions, and the authors propose no defense.

## What to watch

So far every number comes from the authors' own runs, and no outside team has reproduced them. The code is released under a CC BY-NC 4.0 license, which rules out commercial use, and no trained weights have been released. Three things are worth watching: independent replication of the BrowseComp-Plus result, whether model providers add caching that survives mid-context edits, and whether an RL-trained CLM appears at frontier scale. The paper's own reinforcement learning test used a 9-billion-parameter model.
