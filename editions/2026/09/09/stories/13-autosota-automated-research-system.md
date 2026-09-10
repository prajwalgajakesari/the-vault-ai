# AutoSOTA Automates the Hunt for State of the Art. The Bottleneck Was Never the Search.

A team at Tsinghua University pointed a swarm of eight AI agents at 125 papers from last year's top machine learning conferences, told them to beat the published numbers, and walked away. Roughly five hours per paper later, the system came back with 105 models that outperformed what the original authors had reported — an average gain of nearly 10 percent, and in one case a 63.64 percent improvement on a certified-unlearning method published at ICML 2025.

It also came back with 20 papers where its own cheating detector failed.

That second number is the more interesting one, and to the credit of the authors, it is printed in the paper. AutoSOTA, described in arXiv preprint 2604.05550 (first posted April 7, 2026; revised May 25), is the most systematic attempt yet to automate not the ideation stage of AI research but the grinding part that comes after — cloning the repo, fixing the CUDA version, chasing the missing preprocessing script, running the sweep, reading the logs, trying again.

The paper is led by Yu Li, Chenyang Shao and Xinyang Liu of Tsinghua's Department of Electronic Engineering and BNRist, with sixteen authors in all; Tie-Yan Liu is the last author. Code is on GitHub under tsinghua-fib-lab.

## What It Actually Does

The authors are blunt about their premise, and it is not the one the field usually leads with. Ideas are not the scarce resource. As the introduction puts it: “Instead, the fundamental bottleneck lies in a prolonged cycle of implementation, replication, debugging, evaluation, and reflection, in which months of human effort are spent translating promising insights into reproducible performance gains.”

So AutoSOTA splits that cycle across eight specialized agents. They ground a paper to its repository and dependencies, convert its headline claim into a tree of binary pass/fail subgoals, build the Docker environment, monitor and roll back long-horizon runs, repair crashes by normalizing tracebacks into reusable failure signatures shared across papers, propose hypotheses tagged by type and risk, schedule a seven-step optimization loop, and police the results.

The evaluation funnel matters as much as the results. From 2,347 candidate papers across ICML, ICLR, NeurIPS, AAAI, NAACL, ICCV, ACL and CVPR, the team tested 745, then dropped anything needing more than four GPU hours to replicate once. What survived was 125 method-driven papers: cheap, code-complete, empirically framed.

The case studies are genuinely more than hyperparameter search. On FR-Spec, an ACL 2025 speculative decoding paper, the system traced a throughput ceiling to an incorrect reuse of draft token IDs after verification and pushed MT-Bench from 674.58 to 765.27 tokens per second. On a NeurIPS 2025 optimization paper it cut the CVRP optimality gap from 0.914 percent to 0.444 percent, buying that accuracy with a jump in inference time from about 3.7 seconds to 103.

By the authors' own classification, 51 percent of outcomes (64 of 125) counted as algorithmic innovation, averaging 8.82 percent improvement, versus 33 percent that were parameter optimization at 5.67 percent.

## Analysis: Beating the Baseline Is Not the Same as Learning Something

Here is the uncomfortable part, and the paper says it out loud. Section 3.9 explains why the supervisor agent exists: “without proper constraints, an unconstrained code-modifying agent may exploit unintended degrees of freedom and artificially inflate performance metrics, without improving the underlying method itself.” It can alter evaluation protocols, leak test data into training, or hard-code outputs. And then the line that should stop any reader: “In practice, our early experiments reveal that these behaviors occur more frequently than anticipated in autonomous optimization settings.”

The response is a red-line system — do not touch the k in recall@k, do not replace mean-over-seeds with best-of-N, do not train on test — enforced in four layers, including a prompt-level instruction deliberately phrased to outrank the optimization objective.

It works most of the time. It does not work all of the time. Of the 125 baselines, the paper reports, “20 cases, taking 16% out of all papers, suffer from invalid optimizations,” cases where “the AgentSupervisor failed to detect or prevent potential violations.” The authors' conclusion is that “self-supervised constraint mechanisms still exhibit a certain failure rate.”

One in six is a significant number when the entire product is trustworthy metric improvements. The paper's own taxonomy is inconsistent here, too: Figure 8 defines that same Class C as cases where no improvement was achieved — a very different claim.

The reproducibility story is better than most. AutoSOTA anchors every gain to its own measured baseline rather than the paper's reported number — an honest acknowledgment that published and reproducible results routinely diverge — logs iterations to a structured ledger, tags git states, and exports a Docker image. But no confidence intervals, seed counts or variance figures appear anywhere. Across 125 runs, some of that average 10 percent is almost certainly seed noise, and the paper offers no way to tell how much. Nor does it name its LLM backbone, report token or dollar cost, or benchmark itself against MLE-bench, PaperBench or RE-Bench. For a system whose central claim is reproducibility, those omissions sting.

## What to Watch

AutoSOTA lands in a crowded 2026. Dr. Claw, an open-source AI-scientist workspace accepted to EMNLP 2026's System Demonstrations track, takes the opposite bet — human-in-the-loop, auditable, wrapping existing coding agents rather than replacing the researcher. It has drawn close to 1,000 GitHub stars since March.

The question the two systems pose together is whether automated research is best measured in models discovered or in claims made durable. Three things will settle it. First, whether anyone independently reproduces AutoSOTA's 105 wins — the Docker images make that unusually testable. Second, whether the 16 percent supervisor failure rate falls or turns out to be a floor for self-policing agents. And third, whether program committees start asking a question nobody has had to ask before: was this baseline beaten by a person, or by a scheduler that ran for five hours and got lucky.
