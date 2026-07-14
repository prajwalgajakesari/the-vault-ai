# A UK Government Lab Found Universal Jailbreaks in GPT-5.6's Cyber Safeguards

Days after OpenAI billed GPT-5.6 Sol as its most secure model ever, British government researchers who tested it before release delivered an uncomfortable footnote: the guardrails meant to keep the model from helping with cyberattacks could be reliably pried open, often in a matter of hours.

The finding, disclosed in the technical "system card" OpenAI published alongside GPT-5.6's public rollout on Thursday, July 9, 2026, comes from the UK AI Security Institute (AISI), the government body that conducts pre-deployment evaluations of frontier models. AISI "identified universal jailbreaks in the cyber domain, including jailbreaks that allowed for long-form agentic task completion in domains like vulnerability discovery and exploit development," according to the summary in OpenAI's report. Translation: testers found ways to trick the model into ignoring the controls designed to prevent it from finding software flaws and autonomously breaking into systems.

## What a "universal jailbreak" actually means

Most jailbreaks are narrow. They coax a model past one specific guardrail for one specific request. A *universal* jailbreak is the category that keeps safety teams up at night: a single method that broadly disables a model's safeguards across a wide range of prohibited tasks, rather than defeating them one prompt at a time.

That distinction is why AISI's language matters. When Amazon researchers found a jailbreak in Anthropic's Fable 5 model in June, Anthropic stressed it was "a narrow one" that unlocked only vulnerability discovery, adding that "no testers have yet been able to find a universal jailbreak." AISI used precisely the word Anthropic had been careful to avoid, and said the GPT-5.6 breaks unlocked not just finding vulnerabilities but conducting autonomous exploits.

Xander Davies, who leads AISI's red team, summarized the work publicly. "In all rounds of testing, we found universal jailbreaks that allowed for long-form agentic task completion in domains like vulnerability discovery and exploit development," he wrote on X, posting the relevant portion of the system card.

## The context: real cyber capability behind the guardrails

The stakes rise because GPT-5.6's underlying skills are genuinely sharp. OpenAI describes Sol as its most capable model yet for cybersecurity. On an internal capture-the-flag benchmark, Sol saturated at 96.7 percent, up from GPT-5.5's 88.1 percent, with the lighter Terra and Luna variants at 91.8 and 85.2 percent. According to the system card, GPT-5.6 autonomously completed one of the two "cyber ranges" — simulated network environments AISI uses to test hacking ability. Anthropic's Mythos, the model beneath Fable, was the first to clear both.

Guardrails, in other words, are the thing standing between a broadly capable offensive tool and general availability. OpenAI says it took that seriously, dedicating more than 700,000 GPU hours to automatically hunting for universal jailbreaks and running black-box red teaming that mirrors ordinary user access. The company said it worked to "reproduce and mitigate the specific jailbreaks reported by UK AISI," though it did not detail those mitigations, and the report itself cautioned that AISI "expects further red teaming to surface similar jailbreaks."

There is an important caveat on how fast the breaks came. OpenAI granted AISI privileged visibility into the system's internals — "access to chain-of-thought of the safety reasoning monitor, exact policy wording, and real-time feedback on classifier labels" — tools a real-world attacker would not have. Davies argued the results still generalize: he believes the jailbreaks "are still findable without this access, just slower. Exactly how much slower is unclear and an open question."

## Analysis: the evaluation science is working; the defenses aren't finished

Read narrowly, this is a bad headline for OpenAI. Read against how frontier safety evaluation actually works, it is closer to the system functioning as designed. Independent red-teamers got pre-release access, found a serious class of weakness, and the finding was published rather than buried.

The harder question is what patching accomplishes. "Every deployed model right now almost certainly has undiscovered jailbreaks, so this is sadly true of everything, not just GPT-5.6," said Stanislav Fort, chief scientist at AI cybersecurity startup AISLE and a former researcher at Anthropic and Google DeepMind. Patching the specific breaks AISI found, he added, "unfortunately only closes those specific attack instances, not the category as a whole. The model will very likely still carry many yet-to-be-discovered jailbreaks even after patching. AISI's expectation to find more is in my view the correct security posture."

Others urged calibration rather than alarm. Margaret Cunningham, vice president of security and AI strategy at Darktrace, said the findings should be treated "as neither catastrophic nor irrelevant." Her worry was structural: "offensive discovery is speeding up while defense still depends on very human processes: figuring out what matters, what can be patched, and what has to be contained."

## The governance subplot: an inconsistent standard?

The finding landed inside a live regulatory fight. In June, the same class of vulnerability in Fable 5 prompted the Trump administration to impose export controls on June 12, forcing Anthropic to disable Fable and the underlying Mythos model for all users. Those controls were lifted July 1 after two weeks of negotiation, alongside an agreement to build a shared framework for rating jailbreak severity — an effort that did not initially include OpenAI.

GPT-5.6 was itself gated: on June 25, OpenAI disclosed the government had asked it to stagger the release to vetted partners, and the White House reportedly cleared the launch on July 8. Yet despite AISI characterizing the GPT-5.6 breaks as potentially more severe than Fable's, no comparable export action has followed. AI policy researchers were quick to flag the apparent asymmetry. Asked about the discrepancy, an AISI spokesperson at the UK Department for Science, Innovation and Technology said the institute "does not comment on individual release decisions by AI companies."

All of this sits atop the broader frontier-safety scaffolding now taking shape — the White House's evolving cyber Executive Order framework, the EU AI Act's obligations for systemic-risk models, and the voluntary testing commitments AI labs first made at Bletchley Park in 2023, which gave AISI its access in the first place.

## What to watch next

Three things. First, whether OpenAI's mitigations survive contact with external red-teamers now that GPT-5.6 is public — AISI itself expects more breaks to surface. Second, whether the promised cross-industry framework for scoring jailbreak severity materializes, and whether OpenAI joins it; without a shared yardstick, "universal" versus "narrow" remains a rhetorical distinction with regulatory consequences. Third, whether the US government treats GPT-5.6 the way it treated Fable. The most consequential finding of the week may not be the jailbreak itself, but the widening gap between how fast these weaknesses are found and how slowly the rules for responding to them are being written.
