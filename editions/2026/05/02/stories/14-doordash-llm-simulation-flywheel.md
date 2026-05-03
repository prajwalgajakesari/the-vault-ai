---
headline: "DoorDash Builds LLM Simulation Flywheel to Test AI Customer Support at Scale"
slug: doordash-llm-simulation-flywheel
category: research
story_number: "14"
date: 2026-05-02
---

# DoorDash Builds LLM Simulation Flywheel to Test AI Customer Support at Scale

Every company deploying a large language model in production faces the same unsolved problem: how do you test a system whose outputs are non-deterministic, context-dependent, and capable of failing in ways no one anticipated? Unit tests cannot cover the combinatorial explosion of real conversations. Manual QA does not scale. And waiting for production failures means real customers absorb the damage. DoorDash, which handles hundreds of thousands of customer support contacts per day across consumers, merchants, and Dashers, decided the answer was to build an entire simulation environment where AI customers argue with AI agents -- and then let another AI grade the results.

In a detailed engineering blog post published in January 2026, DoorDash engineers Lewis Warne, Chenran Gong, and Aditi Bamba described what they call a simulation and evaluation flywheel -- a closed-loop system that generates synthetic multi-turn conversations, automatically evaluates them against policy and quality criteria, and feeds the results back into prompt and retrieval improvements. The approach represents one of the most thorough public accounts of how a major technology company is industrializing LLM testing for customer-facing applications.

## Simulating Customers at Scale

The core of the system is a conversation simulator. An LLM plays the role of a customer, complete with a specific intent, emotional state, and behavioral profile derived from historical support transcripts. The production chatbot responds exactly as it would in a real interaction. The simulated customer then adapts dynamically -- pushing back on unsatisfying answers, escalating frustration, asking clarifying questions, or introducing new complications mid-conversation.

Backend dependencies are not hand-waved away. DoorDash mocks the service APIs that the chatbot relies on -- order lookups, refund workflows, account status checks -- so that the simulated conversation exercises the same retrieval-augmented generation pipeline and tool-calling logic that a real interaction would trigger. This is not a prompt-in, text-out test. It is a full-stack simulation of the operational environment.

The scale is striking. The team reports running more than 200 simulated conversations in under five minutes, each one a multi-turn exchange that can span the full complexity of a real support interaction. That throughput transforms testing from a bottleneck into a commodity, allowing engineers to iterate on prompt changes, retrieval strategies, and context engineering with rapid feedback.

## LLM-as-Judge: Automated Evaluation That Works

Generating synthetic conversations is only half the problem. The other half is knowing whether the chatbot performed well. DoorDash built an LLM-as-judge evaluation framework that classifies each conversation against predefined criteria: policy compliance, hallucination detection, tone appropriateness, and task completion accuracy.

The team made a critical design decision that other organizations would do well to copy: they use binary pass/fail evaluations rather than arbitrary numerical scoring scales. A 1-to-5 rating system introduces subjective drift and makes it nearly impossible to calibrate LLM judges against human reviewers. Binary judgments -- did the chatbot hallucinate or not, did it follow the refund policy or not -- are far more reliable and far easier to validate against human ground truth.

Each evaluation is calibrated against human judgment before it enters the automated pipeline. When the team identifies a new failure mode in production or simulation, they write a targeted evaluation, validate it against human-labeled examples, and add it to the growing suite. The evaluation library becomes a living specification of what good looks like.

## The Flywheel Effect

The simulation and evaluation components reinforce each other in a continuous development loop. Engineers identify a failure pattern -- say, the chatbot incorrectly offering refunds on non-refundable orders. They write an evaluation to detect that specific failure. They generate targeted simulations that stress-test refund scenarios. They adjust the prompt, retrieval context, or guardrails. They re-run the simulations. If the evaluation passes, they deploy with confidence. If not, they iterate.

This flywheel has delivered measurable results. Context engineering improvements validated through the framework reduced hallucination rates by roughly 90 percent before those changes ever reached a live customer. That is the core value proposition: catching failures in simulation rather than in production, where each mistake erodes customer trust and generates costly escalations to human agents.

## Why This Matters for Enterprise AI

DoorDash's approach addresses what may be the single largest gap in enterprise LLM deployment: the absence of reliable, scalable testing infrastructure. Most companies shipping LLM-powered features rely on some combination of vibes-based evaluation, small manually curated test sets, and crossed fingers. That approach works when the stakes are low and the surface area is small. It collapses when you are handling hundreds of thousands of daily contacts across dozens of issue types, multiple user personas, and constantly changing business policies.

The simulation flywheel pattern is particularly significant because it is not DoorDash-specific. Any company with historical conversation data, a chatbot in production, and backend APIs can build a version of this system. The architectural components -- an LLM-based customer simulator, mocked backend services, binary LLM-as-judge evaluations calibrated against human labels -- are generalizable building blocks.

The timing also matters. As AI agents move from single-turn question answering into multi-turn, tool-using, action-taking systems, the testing problem compounds exponentially. A chatbot that can look up orders, process refunds, and modify accounts has a vastly larger failure surface than one that simply answers questions. Simulation environments that exercise the full action space become not just useful but essential.

## What to Watch

DoorDash has signaled continued investment in this infrastructure, and the engineering team has published a series of related posts on RAG quality, user-generated content integration, and Dasher support automation. The next frontier is likely closing the loop between simulation insights and automated prompt or retrieval tuning -- moving from a human-in-the-loop flywheel to one where the system self-corrects based on evaluation signals. For now, DoorDash has published one of the clearest blueprints available for testing LLM systems at production scale, and every team shipping an AI chatbot should be reading it.
