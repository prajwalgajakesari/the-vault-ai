# Claude Opus 5.5 Takes the Top Spot on Andon Labs' Blueprint-Bench 2 Spatial Reasoning Test

Anthropic's Claude Opus 5.5 is now the best AI model at one of the hardest tests of machine spatial reasoning. On Andon Labs' Blueprint-Bench 2, where AI agents turn interior photos of apartments into 2D floor plans, Opus 5.5 posts a normalized connectivity score of **0.512**. That puts it just ahead of OpenAI's GPT-6 Astra at **0.497** and within reach of the human baseline of **0.586**.

It is a sharp jump for Anthropic's flagship line. Its predecessor, Claude Opus 5, scores 0.304 on the same leaderboard and ranks 15th. The new result is roughly 68% higher, and it moves Opus 5.5 past Anthropic's own Claude Fable 5.1 (0.419). According to a BenchmarkList snapshot of the leaderboard taken on September 4, Fable 5.1 had been the top AI entry until then.

## What the benchmark actually measures

Andon Labs released Blueprint-Bench 2 in May 2026. It updates an earlier eval in which, by the lab's own account, model outputs were "essentially noise." Each agent works through **50 apartments** one after another. For each apartment it studies about **20 interior photographs** and then draws a floor plan showing the rooms, the doors between them and their rough relative sizes. Agents also keep a notepad that carries over from one apartment to the next, so the strongest models can write down layout patterns and improve their strategy as they go.

The scoring focuses on topology, not on how the plan looks. Andon Labs turns each floor plan into a connectivity graph and compares it with the ground truth. **Jaccard similarity** of room-to-room connections makes up 50% of the composite score. Degree similarity (how many doors each room has) counts for 20%, graph density for 10%, room count for 10%, and door count and orientation for 5% each. Scores are normalized so random guessing maps to zero. Counting rooms is easy, with all models at about 90%. What separates them is working out which rooms connect to which.

In its announcement of the benchmark, Andon Labs explained why it cares about the result: "3D spatial intelligence is not something AI models are trained for." Its eval page makes a bolder claim: "In Blueprint-Bench 2, we see the first signs of genuine spatial reasoning from 2D photographs." In one example trace, a model uses a washer and dryer seen in two photos to work out which way the camera was facing.

## How the field stacks up

Anthropic and OpenAI dominate the top of the table. After Opus 5.5, GPT-6 Astra and Fable 5.1, Claude Fable 5 and Google's Gemini 3.8 Flash tie at 0.386. GPT-5.5 follows at 0.362 and GPT-6 Sol at 0.338. The best xAI model is Grok 4.6 at 0.332, and last week's Grok 4.7 lands slightly lower at 0.325. Gemini 3.1 Pro, one of the leaders when the benchmark launched, now sits at 0.265.

At the bottom, GPT-6 Luna scores 0.017, and five models score at or below random, including Claude Haiku 4.5 and Gemini Robotics-ER 1.6. The Gemini Robotics result stands out because that model was built for embodied and spatial reasoning. Andon Labs noted that its "spatial specialization does not translate to improved floor plan generation."

Opus 5.5's lead over GPT-6 Astra is small. Andon Labs publishes standard-error bars for every model, and a 0.015-point gap is narrow enough that the two should be seen as roughly tied at the top. The human comparison also needs a caveat: people were tested on only 12 of the 50 apartments.

## A mixed week of third-party evals

Blueprint-Bench is one of several independent tests of Opus 5.5 published since its September 22 launch, and the results vary. Vals AI puts it **#1 of 63 on the Vals Index** at 69.69% and first on its RSI Index. Vals said the result marks "a major step forward for long-horizon agentic work." On Andon Labs' own Vending-Bench 2, however, Opus 5.5 averaged **$9,235** over a simulated year. That is less than Opus 5 earned, and it trails GPT-6 Sol and Grok 4.7.

A developer's account adds a hands-on view. Priyan R has spent 2026 asking each new frontier model to port the 1989 *Prince of Persia* to C#. He writes that Opus 5.5 found a documented reconstruction of the original room-drawing routine, ported it, and then checked the output pixel by pixel against the real DOS game. On the first screen of level one, the number of mismatched pixels fell from **8,429 to 2**. "For the first time, the levels look like Prince of Persia," he wrote.

## Why It Matters

Spatial reasoning is still one of the weakest skills of language models, and it matters for robotics, property tech and any agent that has to act in a real building. Blueprint-Bench 2 can't be passed by recognizing what's in a photo. A model has to build a consistent mental map from scattered views. Andon Labs' chart of performance against release date fits a line through the best model at each point with an R² of 0.78, rising about **0.04 points per month**. On that trend, the lab projects that frontier models will pass the human baseline around **November 2026**.

Progress is also uneven: Opus 4.8 scored below Opus 4.7, and Opus 5.5 lags Opus 5 on Vending-Bench. That is why independent evaluators like Andon Labs and Vals AI now matter as a check on launch claims.

## What to Watch

The obvious next milestone is the 0.59 human line. If Andon Labs' trend holds, the next round of frontier releases from Anthropic, OpenAI or Google could reach it before the end of the year, though the human baseline will need to be measured on the full 50-apartment set before any "superhuman" claim holds up. Also watch whether Google's next Pro-tier Gemini wins back the ground it has lost since spring.
