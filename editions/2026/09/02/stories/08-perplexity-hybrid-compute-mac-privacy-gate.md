# Perplexity Wants Your Mac to Do the Private Half of the Work

For three years, the AI industry's answer to *can I trust you with my tax returns?* has been to build a higher wall around the data center: better encryption, tighter retention terms, a compliance addendum. On September 1, Perplexity proposed something blunter. Don't send the tax returns at all.

The company launched hybrid compute on Mac for Perplexity Computer, its agentic platform, splitting a single task between frontier models in the cloud and a compact open-weight model running on the user's own Apple silicon. A job starts in the cloud, where a large model handles planning, web research and heavy reasoning. When it reaches a step that touches a privileged file or a client record, it delegates that step to a subagent on the Mac -- mid-task, without restarting the job or losing context. Perplexity says no agent has made that handoff dynamically before.

"This will allow Computer to orchestrate local models that can run locally on Mac, particularly for agent steps involving sensitive and private files (eg your bloodwork, tax returns, litigation, etc)," co-founder and CEO Aravind Srinivas wrote on X announcing the rollout.

## How the split works

The architecture behaves like a dispatcher: the cloud orchestrator decomposes a prompt into subtasks, and anything touching local data or on-device actions goes to the Mac. Guarding the boundary is what Perplexity calls the Privacy Gate, an on-device classifier that scans outbound text for personally identifiable information -- names, addresses, account numbers, credentials, government IDs -- before a single token leaves the machine. When it flags something, the gate can keep the content local, mask it, refuse the action, or rewrite the request so the cloud model can proceed without the protected material.

"What we wanted to do is make sure anything that's shared to that cloud orchestrator is safe," said Jon Staff, who leads Perplexity's macOS and iOS engineering teams, in a press briefing. "We built and trained our own PII classifier that integrates directly into the Mac app."

The classifier is not a rebadged frontier model. In a companion research post, Perplexity's Secure Intelligence Institute detailed PII-Tracer, a 0.6-billion-parameter bidirectional encoder adapted from a Qwen3 backbone, covering nine PII categories over a 4,096-token window. It was evaluated on PII-TRACE, a new benchmark of 13,148 synthetic conversations across 13 languages, built to test one failure mode: whether a detector catches *every* recurrence of an identifier across a long dialogue, not just the first. Among 12 systems tested, PII-Tracer posted the highest character F1 at 0.629 and found every mention of 79.4% of recurring identifiers, against 57.0% for GPT-5.6-sol. Perplexity is open-sourcing it on Hugging Face.

Hybrid compute launches with three local models -- Google's Gemma 4 E4B, Alibaba's Qwen3.6 35B-A3B, and a Perplexity post-trained version of Qwen3.6, the recommended pick. It runs on any Apple silicon Mac with macOS 15 or later and at least 24GB of unified memory, though Staff conceded Perplexity recommends 32GB for the better tier and that the smallest option "significantly underperforms" the larger models. It is available to Pro, Max and Enterprise subscribers; Windows and Linux come later.

## Why this matters

Three things are happening at once here, and only one of them is about privacy.

The first is economic. Local tokens are free -- not discounted, free. "You're paying for the electricity, you're paying for the hardware, so we're not charging you for that," Staff said. "The only thing the credits are used for is the orchestration and the delegation." That is a quiet repricing: inference cost shifts onto hardware the customer already bought, while Perplexity keeps metering the thin, high-value layer on top. Srinivas said it plainly: "Mac offers a big opportunity to move token consumption to Apple Silicon (with no price paid for tokens consumed locally) and protect user privacy." Privacy is the pitch; margin is the mechanism.

The second is that the PII classifier is becoming a product layer in its own right. For years, redaction was a compliance checkbox bolted onto data pipelines. Perplexity has turned it into a routing primitive -- the thing that decides which model sees which bytes -- and published a benchmark defining what good looks like. Whoever sets that standard shapes how every hybrid agent gets built.

The third is the moat. Unified memory is why this works, and Apple is the only vendor shipping it at consumer scale. Perplexity is explicitly riding Apple's new Mac mini and Mac Studio as reference platforms, and can run Computer on an always-on Mac mini driven remotely from an iPhone. "Anytime one of these gets better, Perplexity gets better," Staff said of the interplay between local models, frontier models and Apple's chips.

The contrast with Apple Intelligence is instructive. Apple's Private Cloud Compute solves the same trust problem from the opposite end: requests too big for the device go to Apple-controlled servers running verifiable software with no persistent storage. Apple asks you to trust a cryptographic attestation. Perplexity asks you to trust a classifier. One is verifiable in principle; the other is probabilistic by construction.

## What to watch

The Privacy Gate is itself a machine learning model, and models have false negatives -- a miss means privileged data reaches the cloud anyway. PII-Tracer's recall drops from 0.975 on short conversations to 0.687 above 10,000 characters under single-window decoding, roughly the length agentic sessions run. Perplexity's mitigations are transparency and audit logs: users can inspect what the gate flagged, and enterprise admins get device-level records of what left each machine.

Watch three things. Whether enterprise and government buyers accept Chinese-developed open-weight models on their endpoints, notwithstanding Staff's argument that open weights and local execution neutralize the risk. Whether free-local-token economics survive a competitor doing the same. And whether anyone independently reproduces the gate's numbers on real, non-synthetic data -- because on the only human-labeled benchmark Perplexity tested, TAB, PII-Tracer's recall was 0.425.

The wager, at bottom, is that the fix for sensitive AI work was never a higher wall. It was a smarter gate. Gates can be wrong.
