Z.ai published the full weights for GLM-5.3 on Hugging Face on Friday, closing a two-week gap between the moment the model went live for paying subscribers and the moment anyone with enough GPUs could download it. The delay was not paperwork. It was, by the company’s own account, a safety hold — imposed because the model got better at finding and exploiting software vulnerabilities faster than Z.ai’s researchers expected.

That makes GLM-5.3 the first GLM model to ship on a staged schedule, and one of the few open-weight releases anywhere slowed explicitly for cyber-capability reasons.

## What actually shipped, and when

GLM-5.3 launched on 14 August through the GLM Coding Plan subscription and the ZCode agent, with no per-token pricing published on day one. API rates followed on 26 August at $1.40 per million input tokens, $0.26 cached and $4.40 output — matching GLM-5.2 on paper, though not in practice, since GLM-5.3 cannot disable thinking and bills reasoning inside output tokens. The weights landed 28 August under the zai-org organisation on Hugging Face.

One correction to the circulating shorthand: Z.ai has never published an official parameter count for GLM-5.3. The widely repeated 743-billion figure is inherited from GLM-5.2, whose base network GLM-5.3 reuses unchanged — a mixture-of-experts model of roughly 744B total parameters, about 40B active per forward pass, with a one-million-token context. Nathan Lambert of the Interconnects newsletter rounded it to about 750B and flagged the sharper comparison: roughly a third the size of Moonshot’s Kimi K3.

Licensing warrants caution too. GLM-5.1, GLM-5.2 and the smaller GLM-5.3-Flash — a 320B-parameter multimodal model released 26 August — all shipped under MIT, and MIT is what has been reported for the flagship. But Z.ai declined to state terms in advance, and the LICENSE file is the only answer that binds.

## The numbers behind the hold

Z.ai’s framing was blunt. The launch post opened: “Scaling post-training is all we did for GLM-5.3.” No new pretraining run, no new base — just longer reinforcement-learning runs, more task environments and harder objectives on top of GLM-5.2.

The coding gains are large by the company’s own measurements. Terminal Bench 3.0 went from 4.6 to 28.3, DeepSWE v1.1 from 46.2 to 66.9, SWE-Marathon v1.1 from 19.4 to 42.5. On Z.ai’s in-house Code Bench, GLM-5.3 clears 34.5 percent at maximum effort while burning about 75,000 output tokens per task, against GLM-5.2’s 23.4 percent at 96,000. Z.ai says plainly it remains behind Claude Fable 5, at 39.5 percent.

The security results are where the trajectory bent. CyberGym, measuring white-box vulnerability identification, moved from 77.2 to 84.5 — narrowly ahead of Anthropic’s Mythos 5 at 83.8 and OpenAI’s GPT-5.6 Sol at 83.6. ExploitBench, which requires reasoning a flaw through to a working exploit, more than doubled to 54.4, though closed models lead decisively at 78.0. On ExploitGym, completed tasks jumped from 29 to 105 on a two-hour budget.

“We expected this to make the model better at finding and reasoning about vulnerabilities,” Z.ai wrote. “What surprised us was how quickly the capability continued to develop as training scaled.”

Alongside the launch, Z.ai opened a public Security Disclosure Ledger listing 2,436 findings across 269 open-source projects. One widely circulated number needs fixing: the launch prose called 1,097 of those medium-to-high severity, but the dashboard shows 1,097 is the sum of 107 critical and 990 high, with 1,286 medium and 53 low making up the rest. Only 53 entries were publicly inspectable, and the findings are not GLM-5.3’s alone: the programme dates to the GLM-5.2 era, and upstream FreeBSD and Apple advisories credit GLM-5.1 or an unspecified GLM.

## Analysis

The interesting thing is not that a Chinese lab shipped a competitive coder. It is that Z.ai said out loud that release timing was a function of capability.

“They also create clear dual-use risks,” the company wrote of its cyber gains. “We are therefore taking a staged approach to release. Selected security partners will first evaluate GLM-5.3 in controlled settings.” That is close to the posture US frontier labs adopt, arrived at without a regulatory mandate — and it inverts the usual critique that Chinese labs keep pace partly by skipping the pre-release testing that costs OpenAI and Anthropic months.

But a two-week hold is a speed bump, not a control. As Lambert put it: “At the end of the day, this type of safety barely matters when true open-weights are coming. If not GLM-5.3, then another model.” His prescription is structural: “We need industrial-scale guidance led by the government or industry coalitions to immediately prepare for this transition across all software.”

The economics reinforce the point. When the UK AI Security Institute ran open-weight models through a 70-task cyber suite in July, GLM-5.2 landed within months of the closed frontier at roughly half the cost — about $46 versus $85 per 100-million-token run. Near-frontier offensive capability no longer requires a frontier-lab budget, and weights diffuse permanently, with no rate limits and no monitoring. It cuts both ways: defenders and volunteer maintainers get the identical tool, and the embargoed fixes now moving through disclosure are openness’s strongest argument.

The commercial backdrop is less flattering. Z.ai sits on the US Entity List, listed in January near a $7bn valuation, spiked to $128bn after GLM-5.2 and has since fallen back toward $75bn. “This firm remains on a completely unsustainable commercial footing,” Bloomberg Intelligence analyst Robert Lea told Bloomberg. “Rising agentic AI will drive Z.ai’s inference costs and losses higher.”

## What to watch

Three things. The LICENSE file and model card — whether Z.ai shipped MIT, and whether the card documents what hardening changed. Parity — do the public weights reproduce the API model’s cyber scores, or did hardening degrade them? And independent replication: every figure above is vendor-run, and CyberGym already appears as both 84.5 and 83.5 in different Z.ai documents.

Beyond that, the precedent matters more than the model. If a lab under export controls can voluntarily gate an open-weight release on cyber evaluations, the argument that safety holds are a Western luxury gets harder to make.
