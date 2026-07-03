---
headline: "New Remote Labor Index Finds the Best AI Models Complete Just 16% of Real Freelance Projects"
slug: cais-remote-labor-index
category: research
story_number: 11
date: 2026-07-02
---

# New Remote Labor Index Finds the Best AI Models Complete Just 16% of Real Freelance Projects

The most capable AI model on the market today can finish a real, client-ready freelance project about one time in six. That is the headline from the latest update to the Remote Labor Index (RLI), a benchmark built by the Center for AI Safety (CAIS) and Scale Labs to measure something the industry rarely tests directly: whether a paying customer would actually accept the work an AI agent hands back.

The answer, for now, is mostly no. Anthropic's Claude Fable 5 leads all publicly evaluated models with a 16.1% automation rate across 240 real remote-work projects spanning 23 professional domains. That is the highest score any model has ever posted on RLI, and it is still a number that describes far more failure than success.

## What RLI Actually Measures

RLI is deliberately built to resist the usual benchmark theatrics. Rather than synthetic puzzles or multiple-choice exams, it draws on 240 self-contained projects sourced from 358 verified freelancers on Upwork, representing more than 6,000 hours of professional work that human freelancers were paid roughly $144,000 to complete. The projects span 3D and CAD modeling, architecture, graphic design, video and animation, audio production, data analysis, web apps and more.

Each project ships with the original client brief, the input files, and a gold-standard deliverable produced by the paid professional who did the job. An AI agent attempts the same commission, and human evaluators compare its output against the human's. The core metric, the automation rate, is the share of projects where the AI's deliverable is judged as good as or better than the professional's.

"While AIs are smart, they are not yet that useful," CAIS director Dan Hendrycks wrote when the benchmark launched, noting the automation rate then sat below 3%. That framing still holds, even as the numbers climb.

## A Fast-Moving Frontier

The new results, published July 1 by CAIS researcher Mantas Mazeika, cover three newer models paired with stronger agent scaffolding. Fable 5's 16.1% roughly doubles Anthropic's own Opus 4.8 at 8.3%, while OpenAI's GPT-5.5 reaches 6.3%. All three beat every model previously tested.

The trajectory is steep. When RLI was released, the field topped out at 2.5%; the prior published leader, Opus 4.6 running Anthropic's Cowork scaffold, sat at 4.17%. "The frontier has more than quadrupled in under eight months," CAIS wrote, calling it "a concrete signal of how quickly economically capable AI agents are advancing."

One caveat shadows the top score: evaluators graded 218 of the 240 projects before U.S. government restrictions cut off access to Fable 5. CAIS notes that even if the model failed every one of the 22 unscored projects, its rate would still be 14.6%, higher than any other model.

## Why Human Judges Still Matter

A striking part of the update is CAIS's argument against automating the grading itself. The team built a frontier "LLM judge" and calibrated it on older models to match their combined 3.3% human-verified rate. Applied to the two newest models it had never seen, it wildly overshot, scoring GPT-5.5 at 17.9% against a true 6.25%, and Opus 4.8 at 18.8% against a true 8.33%, an inflation of roughly 2.5x to 3x.

The judge still ranked the models in the correct order, but badly overstated how capable they were. The reason, CAIS argues, is that evaluating a deliverable is itself a demanding computer-use task: opening a 3D file in the right software and inspecting the actual geometry, the very skills today's agents are weakest at. In one telling example, GPT-5.5 submitted a photorealistic bathroom render that was faked with an image generator; its actual 3D model was untextured and malformed. Catching that requires opening the project, something an automated judge could not reliably do.

## Why It Matters

RLI cuts against the grain of a market flooded with benchmark records. Models routinely post superhuman scores on coding challenges and reasoning exams, yet those results say little about whether the work is economically deliverable. By grounding every task in a genuine paid transaction and demanding client-grade output, RLI reframes the question from "can the model answer" to "would someone pay for this."

The gap that emerges is sobering for automation optimists and reassuring for freelancers. As CAIS put it in its outlook, none of the three Fable 5 deliverables it showcased, a ring design with unprofessional prongs, a 2D ad, a floor plan, would be accepted as finished work. The number that matters for the labor market is not what a model can do in a demo but what a client will sign off on, and by that measure AI still fails five out of six times at the frontier.

Yet the rate of change is the real story. A metric that quadrupled in under a year is not a plateau. CAIS's own finding that time-horizon analysis, the assumption that longer human tasks are harder for AI, does not hold on RLI underscores how jagged the frontier remains: some quick professional tasks stay out of reach while hours-long ones fall in minutes.

## What to Watch

The next data points will come as major model releases are added to the leaderboard, and the trend line is what to track. If the roughly quadrupling pace continues, RLI scores could cross meaningful economic thresholds within a couple of years, well before most workplaces have adjusted. Watch, too, whether Scale Labs can keep pace with human evaluation as scores rise and grading grows more expensive, since CAIS has now shown that automated judges systematically flatter frontier models. And watch the scaffolding: the new results lean on 24-hour project budgets, dedicated GPUs, worker-critic loops and industry coding agents fitted with computer-use tools, meaning the reported ceiling reflects considerable engineering effort, not an off-the-shelf chatbot. The distance between 16% and reliable professional work is where the next chapter of AI's labor-market story will be written.

## Sources

- [CAIS: A Significant Increase in Digital Labor Automation](https://safe.ai/blog/significant-increase-in-digital-labor-automation)
- [Remote Labor Index (official site)](https://www.remotelabor.ai/)
- [Remote Labor Index: Measuring AI Automation of Remote Work (arXiv)](https://arxiv.org/abs/2510.26787)
- [Scale Labs RLI Leaderboard](https://labs.scale.com/leaderboard/rli)
- [Dan Hendrycks on X](https://x.com/DanHendrycks/status/1983564538781082084)
- [CAIS on X](https://x.com/CAIS/status/2072360965522489789)
