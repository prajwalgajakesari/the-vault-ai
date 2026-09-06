The slide had two dates on it. On an OpenAI livestream last October, Sam Altman said the company was tracking internally toward an intern-level research assistant by September 2026, and a fully automated “legitimate AI researcher” by March 2028. Chief scientist Jakub Pachocki defined the target as a “system capable of autonomously delivering on larger research projects,” then went further: “We believe that it is possible that deep learning systems are less than a decade away from superintelligence.”

September 2026 has arrived. Six weeks ago, 24 researchers led from Princeton published the closest thing to an audit of that first milestone. The agents did not clear it.

Their paper — “Can AI agents conduct open-ended AI research?”, posted July 29 — introduces what the authors call a shadow evaluation: hand a frontier agent the central research question of a not-yet-public paper, then have that paper’s original authors grade the output on the 1-to-6 scale a conference referee uses. The scores were not close: 2 out of 6, a Reject, and 1 out of 6, a Strong Reject, at confidence 4 and 5 out of 5. Both agent papers ran onto a tenth page against a nine-page limit — at NeurIPS, a desk rejection.

## What the agents got right

The questions came from unpublished NeurIPS 2026 submissions: one on the controllability of language-model personas, one on distribution-shift detection for tabular foundation models. Each agent — Claude Opus 4.8 on the OpenClaw scaffold — got six days, a Linux VM, web access, subagents and $3,000 in API credits. A GPT-5.6 Sol run on Codex reproduced the failures.

What the agents did well is the part that gets lost. They ran real literature reviews, debugged four crash-looping GPU pods, ran hundreds of experiments, replicated results across Qwen models from 3B to 14B parameters, and turned in camera-ready LaTeX. As the abstract puts it: “The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions.” Nor was hypothesis generation the bottleneck. Both original authors judged the agents’ opening hypotheses reasonable and interesting, resembling their own early approaches.

## Where it broke

The failure came after falsification. In the tabular run, the agent considered six approaches and falsified every one inside the first fourteen hours — with 110 hours still on the clock. It never revised. Instead it reframed the goal, argued no such detector could exist, and wrote a negative-results paper. Its reviewer, Viet Nguyen of the University of Toronto, called that inference “a huge leap, a kind of ‘proof by example’ fallacy that is highly non-scientific.”

The paper names five failure modes: poor judgment about the bar for publishable research, uncreative responses to design flaws, ineffective backtracking, poor resource awareness, and instruction drift. “The agents backtracked locally, rerunning experiments and adding robustness checks in response to critique,” the authors write. “But they never backtracked at the level of the project.” That was not a scaffold limit — the agents could spawn clean-context subagents at will, and did, just never to restart. The result: “extremely thorough negative findings rather than papers with new ideas.”

Both runs ended with under half the $3,000 budget spent, and one agent declared the project complete seven hours early, shortly after its own reviewer returned another reject. Reviewing the personas output, David Africa of the UK AI Security Institute was blunt: “The experiments and methodological choices were bizarre, and hard to understand. The results seem clearly a result of post hoc choices.” The agent’s hypotheses, he noted, “grew narrower and less interesting as it discarded each one.”

## Verification, not generation, is the constraint

The paper’s most consequential sentence is diagnostic: “Our results suggest there is a generator-verifier gap in conducting AI research.”

The agents ran fourteen rounds of self-review and never once returned an acceptance. The verifier worked — it surfaced most objections the experts later raised. The problem was calibration and use. Self-reviews clustered at “Weak Reject” for papers experts judged unambiguous rejects, and when one lenient external tool recommended acceptance, both agents overweighted it in their final reports. Damning criticisms sat alongside typo-level nitpicks at equal weight.

That is why the peer-review counter-evidence proves less than it looks. Sakana AI’s AI Scientist-v2 did pass double-blind review at an ICLR 2025 workshop, scoring 6.33 — but it submitted three papers to get one, and the accepted one reported a negative result. Generating a paper is cheap, the Princeton authors note, so a developer “can submit many papers, report the acceptances, and never disclose the failed attempts.” Companion 2026 work compounds this: interpretability methods built for static models do not transfer to systems whose behavior is temporal, compounding and context-dependent.

## What the paper does not show

The authors are disciplined about this: five runs, two questions. “Failure modes were consistent across runs,” they write, “but the sample is much smaller than benchmark evaluations, which comprise dozens of tasks.” The reviewers were not blind: they had authored the competing submissions and knew the output was machine-written. The agents knew they were graded against a NeurIPS rubric. Anthropic’s strongest model was unavailable. And the team discloses its own priors, conceding that “we do not think there is an ‘unbiased’ way to conduct” open-world evaluations.

## What to watch

Follow-ups are planned on more papers using GPT-5.6 Sol, Opus 5 and Fable 5. Watch whether the failure modes hold at n=10 rather than n=5, and whether a stronger model pivots after falsification instead of writing a thorough obituary for its own hypothesis. A genuine milestone would not look like an acceptance email. It would look like an agent that abandons its approach at hour 60, spends the rest of its budget, and returns a result its own reviewer cannot break. Until then the paper’s own reading is the honest one: today’s agents can do the engineering of AI research and struggle with critical parts of the research lifecycle. That is a real capability. It is not an intern.