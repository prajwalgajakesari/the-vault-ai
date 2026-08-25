Every agent framework shipping today assumes the same thing: if you hand a model a written-down procedure — a SKILL.md, a workflow memory, a distilled playbook — you are giving it knowledge it didn't have. A paper that dominated research chatter this past week says that assumption is wrong, and it has 8,135 trial records to back the claim.

"Demystifying Agent Skills: Why They Work—Until They Don't" (arXiv:2608.14036) went up on August 14 from a nine-author group led by Zhiyuan Jiang, with co-authors listed across Princeton, UC San Diego, Stanford, USC and Johns Hopkins, including Princeton's Mengdi Wang. It topped Hugging Face's trending papers list on August 19 and spent the rest of the week getting picked apart on X. The headline result: when a skill helps an agent, the mechanism is almost never "the skill told it something it didn't know." In the paper's mechanism labels, explicit knowledge injection accounts for **4.5%** of cases. Procedural anchoring accounts for **65.7%**.

As the authors put it: "skills usually do not work by supplying missing facts. They work by stabilizing action: which setup steps to run, which tool sequence to follow, what intermediate checks to perform, and which recurring pitfalls to avoid."

## What they actually measured

The design isolates representation rather than content. The team built 528 matched triples across SkillsBench (144), Terminal-Bench 2.0 (186) and Terminal-Bench-Pro (198), each running the same task under three arms: raw execution with no prior experience; workflow memory, meaning the raw prior trajectories injected directly; and a distilled skill. Critically, the workflow memory and the skill are built from *the same source trajectories*. Any gap between them is a representation effect, not an information effect. Two agent-model pairings were used — Codex with GPT-5.3-Codex, and Gemini CLI with Gemini-3.1-Pro-Preview — with retrieval evaluated separately using Qwen3-Embedding-0.6B.

Aggregate success is unremarkable. Skill arms hit 61.9% oracle-status success, raw execution 59.1%, workflow memory 55.9%. The real spread is skill over workflow memory: **+6.06 percentage points, 95% bootstrap CI [+0.76, +11.36]**. Same experience, different packaging, a gain whose confidence interval barely clears zero on the low end.

Where skills earn their keep is operational fragility. Execution-layer and verification failures fall from 37.3% of raw-arm labels and 33.3% of workflow-arm labels to 23.5% of skill-arm labels. Environment and infrastructure failures collapse from 5.3% (raw) to 1.7% (workflow) to **0.2%** (skill). Output-format mismatches drop 7.4% to 3.2%; background-service lifecycle failures, 2.7% to 0.8%.

And where they don't: algorithmic logic errors sit at 8.3% raw, 11.0% workflow, 7.4% skill — essentially flat. Static verification without runtime checks: 12.5%, 12.5%, 11.7%. A skill will stop your agent from botching the Docker setup for the ninth time. It will not stop it from writing the wrong algorithm.

## The new failure surface

Skills also create problems that didn't exist before. The mode the authors label `skill_guidance_misapplied_or_ignored` shows up in 10.0% of skill-arm cases versus 0.8% for raw and 0.4% for workflow memory. "A skill is not self-executing," the paper notes. "The agent must decide whether it applies, which parts to follow, how to adapt it, and when to abandon it."

Workflow memory fails in the opposite direction — process overload. Timeout and budget exhaustion appears in 10.6% of workflow-memory runs against 1.7% raw and 4.4% skill. Dumping raw traces on an agent buries the decisive procedure under failed branches and debugging residue.

## The retrieval result is the uncomfortable one

This is the number that should worry anyone building a skill library. As the candidate pool grows from 5 to 100 skills, average actual-use precision — how often the agent's invoked skills match the ground-truth annotation — falls from **29.6% to 3.3%**. Per-pairing, Codex drops 42.3% to 5.9%; Gemini drops 16.9% to 0.7%.

Downstream task success over that same sweep goes from 36.4% to 39.3%. It gets slightly *better*.

The authors' reading: "exact ground-truth skill invocation is neither sufficient nor strictly necessary for success." Agents inspect and invoke multiple candidates rather than the annotated one; recall stays at 54.3–73.6% at k=100 even while precision is 0.7–8.1%. Related-but-wrong skills apparently still supply usable procedural scaffolding. Offline diagnostics degrade more gently — top-1 embedding precision 88.3% to 76.9% — and the dominant stressor there is semantic confusability, not pool size: on similar-distractor pools, top-1 precision runs 70.5% down to 53.4%, versus 97.7% to 84.1% on random pools.

## What's solid, what isn't

The controlled matched-triple design is the strongest thing here, and the taxonomy validation is unusually careful for this genre: 95.8% exact agreement and Cohen's κ = 0.952 on the human check. The team also ran the obvious skeptic's ablation — maybe any compact hint works? On 26 Terminal-Bench-2 tasks, an instruction-derived short plan hit 47.7% and a workflow-derived test-first template 59.2%, against 62.3% for workflow memory and 79.2% for skill injection. Not just any hint.

The caveats are real and the authors state them plainly. From the limitations section: the study "evaluates a limited number of agent–model configurations, so the findings may not generalize to other scaffolds, model families, or model versions," and "the mechanism taxonomy is derived from a stratified open-coding sample covering approximately 3% of the normalized records rather than exhaustive labeling, so rare behavioral modes may be underrepresented."

Add two more. First, an LLM judge assigns the taxonomy modes — the 65.7%-versus-4.5% split is a model's read of what happened, validated against humans on a sample, not a direct measurement. Second, everything is terminal- and tool-use benchmarks. Nothing here covers long-horizon web agents or open-ended collaboration, which is exactly where "the agent lacks knowledge" might actually be the binding constraint.

## What to watch

The practical implication is blunt: if your skill library is growing, retrieval precision is falling off a cliff and your success rate isn't telling you. The paper's own framing is that skill use is "a lifecycle problem rather than a single memory-injection mechanism" — generate, retrieve, invoke, adapt — and the field currently measures only the last box.

One more from the same week worth tracking: *Le Critique: Privileged Value Functions for LLM Reinforcement Learning* (arXiv:2608.16739, August 17) from Siddarth Venkatraman, Matthieu Dinot and Laurence Aitchison, which argues learned value functions were prematurely written off in favor of critic-free methods like GRPO. Two papers, one week, same underlying move: stop reporting aggregate success, start reporting where the credit actually comes from.
