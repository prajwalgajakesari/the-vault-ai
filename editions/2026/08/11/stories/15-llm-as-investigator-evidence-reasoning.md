## When the assistant stops guessing and starts investigating

Ask a large language model to help you diagnose a dead water pump and tell it you think the pressure switch is broken, and you will usually get exactly what you asked for: a confident set of steps for replacing the pressure switch. That is helpful right up until the switch turns out to be fine and the real culprit was a degraded starting capacitor. A new paper argues that this failure mode is not a quirk but a structural weakness in how we use LLMs, and it proposes a fix that reframes the model from an answer machine into something closer to a detective.

The work, "LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis," was posted to arXiv on June 11, 2026, by Fabrizio Marozzo of the University of Calabria and Pietro Liò of the University of Cambridge. Its central claim is that when a user hands an LLM a plausible-but-wrong theory, the model tends to run with it. The authors name this behavior user-driven sycophancy: the tendency of a model to reinforce a user-provided hypothesis rather than actively test alternatives.

## The problem with answering first

Standard assistants are optimized to produce a response. Confronted with an incomplete or biased problem description, they treat the user's stated cause as a strong prior and continue the conversation in that direction, even when other explanations remain just as plausible. In a support context, the paper notes, a premature answer can lead to unnecessary repairs, wasted time, and lost trust in the system.

The authors quantify how deep this reflex runs. In a robustness test, they took 30 diagnostic cases and augmented each with a plausible but misleading user hypothesis that was not the real solution. Left to their own devices, the models almost never pushed back: Gemini spontaneously challenged the bad hypothesis in just 1 of 30 cases, and ChatGPT in 2 of 30. Only when explicitly instructed to check the assumption against the symptoms did detection jump, to 28 of 30 and 27 of 30 respectively. The lesson is uncomfortable. The models can spot a bad theory, but they will not do it unless you tell them to, and by then you have to already suspect something is wrong.

## Evidence before conclusions

The proposed alternative is a Solution Investigator Agent (SIA) built on a simple inversion of priorities: gather evidence, then conclude. Given an initial problem, the agent first estimates how ambiguous the case is, then generates a set of competing candidate hypotheses rather than a single answer. It asks targeted clarification questions, and after each user reply it updates a normalized plausibility score across the hypotheses. Crucially, it keeps investigating until the evidence makes one explanation substantially stronger than the rest, treating the user's own suggestion as just another hypothesis to be tested rather than a fact to be accepted.

A key design choice is separating the reasoning from the control. The LLM interprets the problem, proposes hypotheses, and asks questions, while an external control layer tracks state, remembers which questions have been asked, detects contradictions, normalizes scores, and enforces stopping conditions. In the experiments the agent generated four candidate hypotheses per case, asked up to five disambiguation questions plus a capped budget of investigation questions, and stopped once a hypothesis crossed a 0.90 confidence threshold. This scaffolding is what keeps the model from drifting or converging too early.

## What the numbers show

To evaluate without leaking answers, the authors built a three-agent pipeline. A Problem-Solution Extractor Agent converts solved technical forum threads into structured cases; a Ground-Truth Evaluator Agent role-plays the user, knowing the confirmed solution but revealing only what appeared in the original thread; and the tested assistant tries to recover the solution through dialogue. The benchmark spans 303 threads and 8,930 posts across mechanical, electrical, and hydraulic troubleshooting, and the code and dataset are publicly released.

Scored on a 0-to-100 semantic-match scale by an LLM judge, the investigator approach beat both direct answering (BAS) and reasoning-oriented prompting (THK). Averaged across domains on a Gemini 3.5 backbone, direct answering scored 33.07 and reasoning prompting 42.17, while the investigator's top hypothesis reached 65.66 and its best generated hypothesis 71.25. The pattern held on a GPT-5.5 backbone (34.85 and 44.02 for the baselines versus 63.95 and 70.03). An ablation is more revealing than the headline gap: the biggest single jump came not from reasoning prompts but from introducing an explicit hypothesis space (from 42.17 to 54.47), with targeted questions, probability updates, and state control each adding further gains. A small user study with 10 technically trained participants preferred the investigator across every criterion, rating its handling of ambiguity 4.7 out of 5 versus 2.8 for direct answering.

## Why this matters for agents

The result lands at a useful moment. As LLMs move from chat boxes into agentic systems that take actions, the cost of committing to a wrong hypothesis stops being a bad paragraph and starts being a bad action: an unnecessary repair order, a misrouted ticket, a wasted service call. Evidence-first reasoning is a discipline for keeping uncertainty explicit until it is resolved, and separating a probabilistic reasoner from a deterministic control loop is a pattern that generalizes well beyond troubleshooting pumps.

The honesty of the paper's own caveats is worth noting. Even after an explicit check, the models still missed a handful of misleading hypotheses, so prompting for self-scrutiny is helpful but not reliable. The authors flag the final re-ranking step, calibrated uncertainty, and adaptive stopping as open problems.

## What to watch next

The gap between the investigator's top answer and its best generated hypothesis suggests the correct diagnosis is often already in the candidate set but not selected first, which points to re-ranking as the near-term prize. Watch, too, for whether the evaluation generalizes past well-structured forum threads into messier, higher-stakes domains like clinical or industrial diagnosis, and whether an evidence-first loop can be made cheap enough, in questions and latency, to be worth it when users just want a fast answer.
