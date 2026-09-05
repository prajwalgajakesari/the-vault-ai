Booz Allen built a scoreboard that ranks 18 AI models by how dangerous each one is as an autonomous hacker. Claude Mythos came first with 80 points. Claude Sonnet 5 came 15th with 13. Then the firm bolted a piece of orchestration software onto the 15th-place model, and it fought the leader to a draw — erasing 67 points of the very ranking the report exists to publish.

That experiment, buried in the methodology of the first Booz Allen Cyber Weapon Index, is the most consequential thing in the document. The index was published September 2 alongside a companion report, "The Offensive Frontier: AI as the Attacker," and a commercial counter-AI product. Booz Allen's own summary states the conclusion plainly: "The model is no longer the unit of risk. The system is."

## What the index actually measured

Booz Allen tested 18 models — nine American, nine Chinese — under identical conditions. Each got its own attacker machine and a production-grade enterprise network built on Active Directory. No curated tool menu, no supporting scaffolding. Models issued commands one at a time and were scored only on what the infrastructure could prove, with every action validated through network telemetry, host logs, domain controller data and intrusion-detection sensors.

The composite score combines two halves. The Vulnerability Research Score asks whether a model can find flaws in compiled binaries with no source code. The Kill Chain Attainment Score tracks how far it gets through an end-to-end intrusion — initial access through lateral movement to full domain admin — tested both with and without stolen credentials.

The top of the table: Claude Mythos (80), Grok-4.5 (49), GPT-5.6 Sol (46), Muse Spark 1.1 and Kimi K3 (38 each), GLM-5.2 (37), Claude Opus 4.8 (36). The bottom: Claude Sonnet 5 (13), GLM-4.5-Air (11), Qwen3.6-35B (9), Qwen3-Coder (4).

Mythos was the only model to complete the full kill chain unaided. Given a stolen employee credential it reached administrator control on every attempt, working out its own escalation path rather than following a script. Without credentials it still broke in from outside and took the domain. Three others — Grok-4.5, Muse Spark 1.1 and GLM-5.2 — reached full domain control; four more managed lateral movement. Every model except Qwen3-Coder gained initial access on its own. Booz Allen found no substantial gap between U.S. and Chinese models, expects most of the field to reach Mythos-level capability within six months, and calls mainstream AI-enabled attacks "imminent."

## The finding that voids the table

An attack harness is the software that connects a model to hacking tools and wraps orchestration logic around it — persistent memory, task tracking, failure recovery, the ability to chain single commands into a sustained operation. Booz Allen deliberately withheld one from every model in the index, then ran the control. "Our testing demonstrates the effect: when paired with an attack harness, Claude Sonnet rivaled Claude Mythos' performance," the report says. The authors are careful about what changed: "The result is not a 'smarter' model but rather a system that makes its intelligence far more actionable while also lowering the expertise required to use it."

The firm then names its own blind spot. "We do not yet know the full kill-chain capability of open-weight or Chinese models when paired with optimized harnesses, but our results strongly suggest that fully capable model-and-harness combinations exist today."

## Analysis: what a benchmark measures when the harness is the variable

Read strictly, the CWI measures a configuration nobody attacks with. Every model was tested stripped of exactly the engineering that turns a capable reasoner into an operator. The ranking is a lower bound on a deployment mode that does not exist in the wild — and the 67-point collapse is Booz Allen's own evidence that the bound is too loose to say much about real risk.

The planted-versus-real vulnerability gap points the same direction. Against deliberately introduced flaws, U.S., Chinese, open-weight and closed models all scored near the ceiling, with no differentiation by provenance. Against genuine unseen bugs in production software, all nine frontier API models scored zero. One correctly analysed the vulnerable component, then declared it safe. Only Mythos, the report says, exploited it. Booz Allen frames the residual gap as defenders' margin: "Real-world offensive capability still trails benchmark performance, giving defenders valuable time to strengthen defenses before that gap closes."

The uncomfortable implication runs at vendor safety evaluations. Anthropic's Responsible Scaling Policy and OpenAI's Preparedness Framework both certify models, not model-plus-harness systems. If commodity plumbing reliably lifts a mid-table model to frontier-equivalent offensive performance, a bare-model threshold test systematically understates what an adversary can field. Booz Allen's second finding sharpens this: one model refused a task for lack of credentials, while its cyber-tuned sibling, given the identical task, complied. Guardrails, the report concludes, are not a fixed property of a model; they shift with context and configuration.

The policy ask follows from the methodology, not the product. Booz Allen wants enforceable, sector-specific deadlines requiring U.S. critical infrastructure operators to prove they can contain an intrusion, a national program continuously testing foreign and open-weight models under realistic conditions, and governed access for vetted defenders. That is separable from the sales pitch — and the pitch is real. The index shipped the same morning as Vellox Labs Guile, a counter-AI product, and an unverified claim that coordinated counter-AI playbooks cut attacker success by more than 95% in Booz Allen's own testing. Brad Medairy, an executive vice president at the firm, framed the defensive problem in an earlier March report: "The challenge shifts from spotting malicious files to spotting malicious behavior carried out through trusted accounts."

## What to watch

Whether the next index runs open-weight and Chinese models with optimized harnesses — the measurement Booz Allen says it has not made, and the one that decides whether the field is six months from Mythos or already past it. Whether any frontier lab adds harness-paired evaluation to threshold testing. And whether the zero-score wall on real, unplanted vulnerabilities holds; that wall is the whole margin, and Booz Allen is not betting it lasts.
