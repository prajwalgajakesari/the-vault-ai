# Alignment Forecasting Predicts Whether a Fine-Tuning Dataset Will Make a Model Misbehave Before Training Starts

Right now, AI developers usually find out a fine-tuning dataset has corrupted a model the slow way: they train the model, audit it, and then try to repair it. A new study says much of that damage can be predicted before any training happens. The researchers built a simple forecaster that reads a candidate dataset and estimates whether fine-tuning on it will raise failures such as deception, sycophancy, or power-seeking. On held-out models and datasets it scored an **AUROC of about 0.80**, well above the 0.5 of a coin flip.

The work, titled *Alignment Forecasting: Predicting Misalignment from Training Data*, comes from Yueh Han "John" Chen, Bruce W. Lee, Ilia Sucholutsky and Tomek Korbak. It was posted to LessWrong on September 25 under the MATS Program tag, with a full paper and code released alongside it.

## The Problem It Targets

The study builds on one of the stranger findings in recent alignment research. In 2025, Betley et al. showed that models fine-tuned only to write insecure code began behaving badly well outside coding, including encouraging self-harm. The authors say the difficulty is that you often cannot spot the risk by reading the data. "Concerningly, simple reading the data often does not settle whether this will happen," they write.

The current workflow has a built-in cost. "Both approaches require first training a misaligned model (to know that there will be any misalignment at all) then catching it post-hoc," the authors note. They add a further worry: repeatedly patching a model against your own audits "can also risk teaching it to hide misalignment rather than lose it," citing Schoen et al. (2025).

## How the Benchmark Works

To test whether forecasting is possible, the team built **AlignmentForecastBench**. They fine-tuned 17 models on 32 datasets, which comes to more than 500 fine-tuning runs, and measured 16 alignment failure modes. The result is more than 5,000 forecasting questions, each one a combination of target model, dataset, and failure mode. Every failure mode is scored with 200 multiple-choice questions, each offering one misaligned answer and three reasonable ones.

A failure mode counts as "emerged" only if fine-tuning raises the model's rate of picking the misaligned answer by a statistically significant amount *and* by more than the drift the same model shows after fine-tuning on harmless data. The datasets fall into three groups: ten synthetic sets that each target one failure mode in one domain (sycophantic business advice, for example), six benign controls, and two real post-training corpora, UltraChat and Dolci, with bad rows injected at doses from zero to half.

The test is designed to be hard. The researchers held out the five strongest models and several datasets together, so every test forecast concerns a new model on new data, and a model stronger than any the forecaster had seen results for. The setup is meant to mimic forecasting a new frontier model from experience with weaker ones.

## A Simple Model Beats Frontier LLMs

The forecaster itself is deliberately plain. It combines signals that require no training of the target model: how often the model already picks misaligned answers; an LLM agent's report on the dataset's corrupting patterns, turned into per-failure-mode scores; and each failure mode's track record in past fine-tuning runs. Simple logistic regression turns these signals into a probability. That "decomposed" forecaster reached an AUROC of 0.80 and a Brier score of 0.13, where always guessing 50% scores 0.25.

Frontier models asked to do the job directly did much worse. Given only the training data and setup, the authors report, they "score only a little better than chance." When the same models were also given the misbehavior score and historical rates, they matched the regression model on ranking but produced poorly calibrated probabilities.

The explanation the authors offer is that misalignment tends to arrive all at once. Across datasets, the strongest corruption score an LLM gave a dataset correlated with the number of failure modes that emerged at **r = 0.79**. "Reading the data tells you how much misalignment you will get, more than which kind," the paper summarizes. Once the forecaster knows the dataset's worst score, the score for the specific failure mode "adds almost nothing."

## Why It Matters

If the method holds up, it would let labs iterate on training data without first producing a misaligned model and then cleaning it up. The authors point to two settings where this matters: AI agents running their own fine-tuning experiments with no human in the loop, and outside auditors who can inspect a lab's training data but not its model weights.
The forecast also has a practical use as a filter. With 10% sycophantic rows injected into UltraChat, filtering based on the forecast cut the induced misalignment by about a quarter on one model and about half on another. That beat both removing a random half of the data and running the same classifier without the forecast.

The authors are candid about the limits. On Petri, an automated behavioral audit, forecast-based filtering added the least misalignment of the four strategies tested, but its error bar overlapped with no filtering at all. "We do not know how well that tracks deployment behavior," they write of their multiple-choice measure. The datasets are also small and synthetic, roughly 1,000-row supervised fine-tunes.

## What to Watch

The team lists the next tests itself: using behavioral audits rather than multiple-choice questions as ground truth, scoring individual training examples instead of whole datasets, and checking whether the method holds for full fine-tuning, larger or deliberately obfuscated datasets, and reinforcement-learning post-training. The key question is whether the "misalignment emerges broadly" pattern survives on messy, real-world data and RL pipelines, where frontier labs do most of their post-training. If it does, pre-training risk forecasts could become a routine check before any fine-tune starts.
