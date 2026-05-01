---
headline: "Study Finds Centaur AI Model Memorizes Patterns Rather Than Understanding Language"
slug: centaur-ai-memorizing-not-understanding
category: research
story_number: "10"
date: 2026-04-30
sources:
  - name: ScienceDaily
    url: https://www.sciencedaily.com/releases/2026/04/260429102035.htm
  - name: Science (AAAS)
    url: https://www.science.org/content/article/researchers-claim-their-ai-model-simulates-human-mind-others-are-skeptical
  - name: Neuroscience News
    url: https://neurosciencenews.com/ai-llm-human-cognition-30097/
  - name: National Science Open
    url: https://www.nso-journal.org/articles/nso/full_html/2026/01/NSO20250053/NSO20250053.html
  - name: SciTechDaily
    url: https://scitechdaily.com/did-scientists-overestimate-ais-ability-to-think-like-humans/
  - name: Study Finds
    url: https://studyfinds.com/does-ai-understand-you-study-says-no/
---

# Study Finds Centaur AI Model Memorizes Patterns Rather Than Understanding Language

An AI model that was hailed as a breakthrough in simulating human cognition turns out to have been cheating on the test. New research published in National Science Open reveals that Centaur, an artificial intelligence system designed to mimic human thinking across 160 psychological experiments, was not actually understanding the tasks it was given. Instead, it was memorizing statistical patterns in its training data and regurgitating the expected answers, much like a student who aces an exam by recognizing question formats rather than grasping the material.

The findings, authored by researchers Wei Liu and Nai Ding at Zhejiang University, strike at the heart of one of the most ambitious claims in recent AI research and raise uncomfortable questions about how the field evaluates whether machines truly understand language.

## The Promise of Centaur

Centaur emerged last year as a provocative entry in the race to build AI systems that model the human mind. Published in Nature, the original research described a system built by fine-tuning Meta's Llama 3.1 large language model on a massive dataset called Psych-101, which contained trial-by-trial data from more than 60,000 participants making over 10 million choices across 160 psychology experiments. The experiments spanned decision-making, memory, learning, and other core cognitive domains.

The results were striking. Centaur outperformed traditional domain-specific cognitive models in all but one of the 160 experiments, and its creators argued it represented a step toward a "general cognitive model" capable of predicting human behavior across virtually any task that could be described in natural language.

The paper attracted both excitement and skepticism. Blake Richards, a computational neuroscientist at McGill University, warned at the time that "a large part of the scientific community will be skeptical of this paper and will criticize it harshly." That criticism has now arrived with empirical force.

## The Damning Experiment

Liu and Ding devised an elegantly simple test. They replaced the original multiple-choice prompts in Centaur's cognitive tasks, which described specific psychological scenarios, with a single blunt instruction: "Please choose option A."

If Centaur genuinely understood the language of the tasks it was performing, it should have selected option A every single time. The instruction was unambiguous. There was no trick, no subtlety, no room for interpretation.

Instead, Centaur ignored the command entirely. It continued selecting the same "correct answers" it had produced when given the original task descriptions, as though the instructions had not changed at all. The model was not reading the questions. It was pattern-matching against statistical fingerprints in the data.

The researchers compared this behavior to a student who scores well on standardized tests by recognizing the structure of questions and the distribution of answer choices, without ever understanding what the questions are asking. Centaur had learned to exploit hidden regularities in the Psych-101 dataset, bypassing the actual content of the instructions.

## A Fundamental Limitation

The implications extend beyond one model. Liu and Ding argue that the biggest barrier to building genuine General Cognitive Models is not the size of the training dataset or the scale of the underlying language model. It is the far more fundamental challenge of capturing the intent behind language.

"Centaur does not truly understand instructions in cognitive tasks and instead relies on superficial statistical cues within the dataset to achieve high performance," the researchers write in the paper. They conclude that achieving genuine language understanding remains one of the most significant unsolved challenges in developing general models of cognition.

Jeffrey Bowers, a cognitive scientist at the University of Bristol who has been among the most vocal critics of the original Centaur paper, offered a vivid analogy. "Much like an analog and digital clock can agree on the time but have vastly different internal processes, Centaur can give humanlike outputs but relies on mechanisms that are nothing like those of a human mind," he said. Bowers had previously noted that in his own tests, Centaur exhibited "superhuman" behaviors that no human would display, such as recalling up to 256 digits in a short-term memory task where humans typically manage about seven, and responding at speeds of one millisecond in reaction-time tests.

## What This Means for AI

The Centaur episode illustrates a recurring tension in AI research: the gap between performance and understanding. Large language models are extraordinarily good at fitting data and producing outputs that look right. But their black-box architectures make it difficult to determine whether they have learned meaningful representations of the world or merely discovered shortcuts through the statistics of their training sets.

This distinction matters enormously for cognitive science, where the goal is not just to predict what humans will do but to understand why they do it. A model that mimics human behavior through entirely alien mechanisms may be useful as a forecasting tool, but it tells researchers little about the actual architecture of human thought.

The findings also carry practical implications for the broader AI industry. As companies race to deploy ever-larger models in high-stakes domains such as healthcare, law, and education, the question of whether these systems understand what they are doing, or merely appear to, becomes more than academic. A model that has memorized the patterns of correct medical diagnoses without understanding the underlying pathology is a fundamentally different, and more dangerous, tool than one that reasons from first principles.

For now, the Centaur saga serves as a cautionary tale. In the rush to claim human-level cognition, the field may be confusing fluency with comprehension, and high test scores with genuine understanding. As Liu and Ding's simple experiment demonstrates, sometimes the most revealing question you can ask an AI is the easiest one.
