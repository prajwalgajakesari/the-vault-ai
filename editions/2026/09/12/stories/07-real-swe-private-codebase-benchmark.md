Ten tickets. Eight attempts each. Eight frontier coding agents, every one running in its maker's own harness. The best of them — Anthropic's Fable 5.1 inside Claude Code — resolved 38.8%.

That is the top line of Real-SWE, a benchmark Specific Labs published this month that runs agents against private production codebases licensed from their owners. The same model leads SWE-bench Pro at 81.2% on BenchLM's September 10 snapshot. The gap between those two numbers is the point of the exercise.

Behind Fable sat OpenAI's GPT-6 Astra in Codex CLI at 33.8% and Google's Gemini 3.8 Flash in Gemini CLI at 31.2%, then GLM 5.3 at 28.8%, Grok 4.6 and Muse Spark 1.3 at 23.8%, Kimi K3 at 18.8%, and GPT-5.6 Sol at 16.2%. Resolution rate is pass@1 averaged over eight runs per task.

## The tickets are the product

Specific Labs — a two-person, Y Combinator-backed outfit founded in 2025 by Siddhant Paliwal and Janak Sunil, whose day business is turning enterprise data into agent training sets — licensed repositories from companies it describes as having "substantial usage, strong engineering teams, and demanding production workloads." Among them: an events platform with 200K-plus users, and a consumer fintech that has processed over 100,000 bank statements.

The work is billing, tax, and customer migration. One published sample asks an agent to fix invoice taxation in a NestJS service where each business settles tax differently — some hold a self-maintained rate, some price against the buyer's destination through a third-party tax authority in sandbox or production, some collect nothing — while a separately exempted customer is charged nothing regardless. Rate, tax and gross go onto the issued invoice; the settled sale is filed back to the authority under that invoice number; intra-European invoices show both parties' VAT registrations.

That shape shows up in the measurements. The median instruction is 1,742 characters; the median reference solution edits 11 files, against six for both FrontierCode and DeepSWE. Verifiers are injected at grading time and, per the report, are "inspired by existing test suites in the codebase or use those tests verbatim."

Difficulty is lumpy. Six of the ten tasks resolved below 15%. A multi-region sweep hit 67.2%; a tax jurisdiction task landed at 3.1% and an analytics stream reducer at 0.0% — zero passes in 64 attempts. No model solved every task.

## Missed requirements, not broken code

The failure taxonomy is the most useful thing on the page, and it does not say what the "AI writes buggy code" narrative predicts. Regressions were rare: 4.1% of Fable's 49 failed runs, 3.8% of Astra's 53, zero for GLM 5.3, Grok and Kimi. Delivering the change to a file the application never calls was rarer still.

What dominated was missed requirements: leaving out behavior the instruction demanded. It was the largest category for five of the eight configurations, and catastrophic for some. Grok 4.6 missed requirements in 41 of its 61 failures (67.2%); Kimi K3 in 35 of 65 (53.8%). Gemini 3.8 Flash failed differently — 49.1% integration errors, the right idea wired into the surrounding system wrong, plus the field's highest regression share at 10.9%. GPT-5.6 Sol's signature was guessing: 43.3% unverified assumptions.

Fable 5.1 and GPT-6 Astra, the two strongest, had no single failure mode above 37%. Their errors spread across all three big categories — worse for anyone designing a review gate, because no single check catches them.

More time did not help. Rollouts under ten minutes failed 71.4% of the time; longer ones failed 73.4%. Neither did spend: estimated cost per rollout ran from $2.50 for Gemini 3.8 Flash to $6.96 for Fable 5.1, which inverts the ranking on cost per resolved task — roughly $8 for Flash against $18 for Fable. Specific Labs does not say how it estimated cost, or whether prompt caching was counted.

## The contamination argument, and its limits

Real-SWE exists because the public sets stopped discriminating. OpenAI retired SWE-bench Verified on February 23, having audited 138 problems its models consistently failed and found at least 59.4% had tests that reject functionally correct patches. It also caught GPT-5.2, Claude Opus 4.5 and Gemini 3 Flash Preview reproducing gold patches — variable names, inline comments — from memory. Its conclusion: "improvements on SWE-bench Verified no longer reflect meaningful improvements in models' real-world software development abilities."

Specific Labs' pitch follows directly: "Tasks on private codebases are natively out of distribution." There is precedent. Scale AI's SWE-Bench Pro carried a commercial subset of 276 instances from 18 startup codebases; Claude Opus 4.1 fell from 22.7% on the public set to 17.8% on the commercial one, GPT-5 from 23.1% to 14.9%.

But privacy buys uninspectability. Nobody outside Specific Labs can check a single score, and the sample is thin: 640 rollouts across ten tasks. Fable's 49 failures imply 31 resolved of 80; Astra 27; Flash 25. First and third are six resolved rollouts apart. Eight attempts at one task are not eight independent observations, so the true interval is wider than the naive one — which already spans the top three.

"So TL;DR benchmarking in a completely non-reproducible manner?" asked Hacker News commenter traceroute66. Sunil replied that the team manually vets codebases and companies and intends to open-source some tasks and trajectories. And note the incentive: a benchmark showing frontier models flailing on private code is a sales argument for a company selling private-code datasets.

## What to watch

Whether the tasks and trajectories actually get released, and how large the full set is — ten tasks is a demo, not an evaluation. Whether other labs adopt private-code reporting now that OpenAI has told the field to stop citing Verified and has flagged about 30% of SWE-bench Pro's public split as broken too.

And whether the failure taxonomy travels. Developer Tess Ainsley drew the operational conclusion this week: "measure the acceptance rate per agent, per area of the codebase, and adjust the review depth from that, per path." If missed requirements really are the dominant frontier failure on production work, the constraint on agentic engineering is not code generation. It is whether anyone can tell, quickly, that a plausible-looking eleven-file diff quietly skipped the exemption rule.
