Meta shipped a coding model on August 5 and published three benchmark charts alongside it. Anthropic's Claude Opus 5 wins all three, including the one Meta built itself.

Meta did not hide this. Muse Spark 1.2, a coding-focused update to July's Muse Spark 1.1, scored 82.9% on Terminal-Bench 2.1 running inside Muse Code, the terminal coding agent Meta shipped the same day. Opus 5 at max effort in Claude Code scored 86.7%. On DeepSWE 1.1, Muse Spark 1.2 posted 59.3% against Opus 5's 65.0%, third behind OpenAI's GPT-5.6 Terra at 64.8%. On Meta Internal Coding Bench, a test Meta designed and grades, Muse Spark 1.2 hit 70.6% to Opus 5's 79.4%, a gap of nearly nine points.

The announcement claims no placements at all. In a category where every launch post is a victory lap, the reticence is the message. Meta is not selling the best coding model. It is selling the cheapest credible one.

Muse Spark 1.2 holds 1.1's rates: $1.25 per million input tokens, $4.25 per million output, cached input at $0.15, for a blended $5.50 per million. Claude Opus 5 lists at $5 and $25, or $30 per million. Meta is asking developers to give up 3.8 points on Terminal-Bench for a bill roughly five and a half times smaller.

Then there is the second tier, where the strategy stops being subtle. Meta's contributor tier prices Muse Spark 1.2 at $0.10 per million input and $0.20 per million output, 12x and 21x below standard, in exchange for permission to train on your prompts and completions. It is the cheapest frontier-class coding rate on the market, and the default on-ramp Mark Zuckerberg steers users toward. "It's easy and low-cost to get started," he wrote on X. "Install Muse Code with one line and you can start on our contributor tier."

Cheap is accurate; free is not. VentureBeat's Carl Franzen found the installer stopped short, reporting payment was "required to finish setting up your account."

## The Harness Is the Argument

Muse Code is a real design bet. Most harnesses spawn helper agents per task and discard them. Muse Code keeps specialized background agents alive for an entire session, which Meta says helps "avoid redundant information gathering" - an agent that already knows the repository does not re-explore it on every request. Large jobs fan out to parallel sub-agents, each in an isolated git worktree. "In testing we had it build six features for a game simultaneously with no collisions," Zuckerberg wrote.

The runtime appends every model call, tool run, approval and edit to a local event log, which Meta says makes it "replay-exact and restart-safe": crash at hour 20 of a long task and it resumes where it stopped. Meta demonstrated the point with a GPU-kernel study: past 1,000 tool calls over up to 24 hours on NVIDIA Hopper hardware, writing Triton KDA and MLA kernels from scratch.

Meta co-trained Spark 1.2 with Muse Code on rejection-sampled harness trajectories, tuning the model to this specific tool. It also ran a self-improvement loop: Muse Spark 1.1 generated hard coding environments and instruction-following templates, then graded candidate solutions against them, producing training data for its successor. The generational gain is 6.7 points on Terminal-Bench and 6.3 on DeepSWE - but a caveat sits in Meta's own chart labels. The 1.1 scores were recorded in the generic mini-swe-agent harness while 1.2 ran in Muse Code. Some of that lift belongs to the tool, not the model.

## Why It Matters

The late-entrant framing needs a correction. Meta's proprietary pivot began April 8, when Meta Superintelligence Labs shipped the original Muse Spark and closed the Llama era. But the paid Meta Model API only opened in public preview on July 9, alongside Spark 1.1. Muse Code landed four weeks after Meta began charging for tokens at all - three Muse Spark releases in four months, against rivals with two years of paid-API muscle memory.

A latecomer cannot win on capability. Nothing moves a team off Claude Code when Claude Code tops every chart, including the challenger's own. What a latecomer can do is reprice the category. Saoud Rizwan, CEO of Cline, named the wedge at the 1.1 launch: "Meta is clearly building for serious agentic coding - strong tool use at a price point that makes it viable to run real coding workloads at scale. That combination is rare, and it's exactly why we wanted Cline developers to have access early."

Five days after Muse Code, Meta added the other half. On August 10 it released Muse Glimmer, a 29.6-billion-parameter dense model distilled from Muse Spark, under Apache 2.0 - a more permissive license than Llama ever carried. "Just like much larger models, muse glimmer can operate as a fully capable agent via planning, tool calls, checking its own results, and failure recovery," chief AI officer Alexandr Wang wrote, adding that it "can run on 24GB of VRAM without losing agentic reliability." That holds for Meta's roughly 4-bit quantized build; full-precision BF16 weights need about 64GB.

Price and openness are the two axes on which Anthropic does not compete. Claude Code is proprietary, and Opus 5 is the most expensive frontier coding model on the board. Meta is attacking exactly there.

## What to Watch

Whether Muse Spark 1.2's weights actually ship. Zuckerberg promised them - "Soon we'll also release the weights for Muse Spark 1.2, our latest foundation model" - with no date, no license and no size, and Wang made a similar promise in April that four months produced nothing on. If they land under Apache 2.0, Meta would put a U.S. flagship frontier model into open circulation, something no American lab has done at that tier. Watch also whether enterprises with proprietary codebases register that the default tier feeds their code into Meta's training pipeline, and whether independent Terminal-Bench runs outside Meta's harness reproduce 82.9%. Co-training a model to its tool is a legitimate optimization. It also makes every number Meta published harness-dependent by construction.