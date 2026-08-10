# 'WebUncertainty' Gives Autonomous Web Agents a Sense of Their Own Doubt

Ask a modern AI agent to book a flight, file a bug report, or dig a product out of an online catalog, and it will happily start clicking. The problem is what happens when it should hesitate. Today's web agents tend to act with the same breezy confidence whether they are on solid ground or hallucinating a button that does not exist. A new paper from researchers at Hefei University of Technology and the Academy of Cyber, CETC Group, proposes a fix that sounds almost human: teach the agent to notice when it is unsure.

The system, called **WebUncertainty**, is described in "WebUncertainty: Dual-Level Uncertainty Driven Planning and Reasoning For Autonomous Web Agent." Its core idea is that an agent should estimate its own confidence at two different altitudes at once, the strategic level of planning and the tactical level of individual actions, and let that doubt reshape what it does next.

## Why Overconfident Web Agents Fail

The authors identify two failure modes that plague long, multi-step web tasks.

The first is rigid planning. An agent using "one-shot" explicit planning maps out every step in advance, then marches through the list even when reality diverges. The paper gives a concrete example: an agent decides to use a "Publication Year" filter to select 2024, never noticing that the Amazon sidebar offers no such option. The plan is doomed, but the agent cannot tell. Swing too far the other way, toward reactive "implicit" planning that decides each step on the fly, and the agent gets distracted by whatever is in front of it, chasing the highest-rated book on the current page while forgetting the global filter it was supposed to apply.

The second failure mode is hallucination during reasoning. In long-horizon tasks, one wrong action snowballs. An agent may operate on a nonexistent element because it lacks domain knowledge, or select the wrong element simply because language models are probabilistic. Crucially, most systems accept whatever action the model generates without asking how confident it actually was.

## How WebUncertainty Works

WebUncertainty attacks both problems with a dual-level uncertainty framework built from cooperating agents.

At the **planning level**, a Task Uncertainty-Driven Adaptive Planning Mechanism decides how to plan before it plans. An Analysis Agent scores the task's uncertainty given the current page state and how far the task has progressed. A Planning Agent then picks the appropriate mode: explicit decomposition when the environment is familiar and global coherence matters, implicit step-by-step reasoning when the environment is throwing surprises. Instead of committing to one philosophy, the agent switches based on how much it does not know.

At the **reasoning level**, an Action Uncertainty-Driven Monte Carlo Tree Search (MCTS) mechanism governs individual moves. During the search's expansion phase, a Reasoning Agent generates several candidate actions along with confidence scores. The paper's signature contribution, the Confidence-induced Action Uncertainty (ConActU) strategy, splits that confidence into two flavors that uncertainty researchers care about: aleatoric uncertainty (AU), the genuine ambiguity of a situation with several plausible correct actions, and epistemic uncertainty (EU), the model's own ignorance. High AU tells the agent to keep exploring rather than commit prematurely. High EU flags a likely hallucination that should be pruned before it executes. An Evaluation Agent scores the candidates, and the two signals feed a predictor-corrected upper confidence bound (PUCT) that steers the tree search toward robust choices.

## The Results

On **WebArena**, a simulated benchmark of 812 tasks across six domains including Shopping, GitLab, Map, and Reddit, WebUncertainty set a new state of the art. Using GPT-4-Turbo, it reached a 46.9% overall success rate, ahead of the strong AgentOccam baseline (43.1%) and well ahead of the search-based WebPilot (37.6%). The gains were largest where ambiguity runs high: in the intent-heavy Reddit domain it hit 67.0%, nearly doubling WebPilot's 37.7%. On the long-horizon GitLab workflows it managed 40.0% against WebPilot's 33.3%.

The framework held up across model backbones, too. With the weaker Qwen-Max model it scored 40.1% overall, still beating AgentOccam (38.4%) and, notably, edging past the GPT-4-Turbo version of WebPilot, evidence that explicitly flagging epistemic uncertainty lets a weaker model catch its own mistakes.

On **WebVoyager**, a 129-task subset run against live sites like Amazon and Google Maps, WebUncertainty again led, reaching 65.9% with GPT-4-Turbo (versus AgentOccam's 64.3%) and 63.6% with Qwen-Max (versus 58.9%). The authors also report that the framework cut inference time by 56% compared with WebPilot, tempering the usual cost of tree search.

## Why It Matters

Calibration, knowing what you do not know, is the quiet prerequisite for trust. An agent that fails confidently is worse than useless because it gives no signal that a human should step in. By turning uncertainty into a first-class control signal, WebUncertainty points toward agents that can gather more information, back off, or escalate to a person at exactly the moments a well-calibrated colleague would. For anyone considering handing real tasks, and real credentials, to an autonomous browser, that difference between a system that hedges and one that bluffs is the whole ballgame.

## What to Watch

The authors are candid about the cost. Running MCTS and generating multiple candidate actions adds computational overhead, and even with the 56% speedup, they note it may still hinder real-time or low-cost deployment. Watch for whether the dual-level idea can be distilled into something cheaper, whether the AU/EU split holds up on multimodal agents that read screenshots rather than DOM trees, and, most importantly, whether calibrated confidence translates into agents that actually ask for help. The code has been released, which should let the field test how far a sense of doubt can travel.