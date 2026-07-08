When the AI-agent startup Lindy quietly moved 100% of its production traffic off Anthropic's Claude models and onto China's DeepSeek in June, it was not making a geopolitical statement. It was doing math. The switch, first reported as part of a broader shift in the market, captured a trend that CNBC laid out in detail on July 7: American companies, squeezed by climbing token costs from OpenAI and Anthropic, are increasingly routing real workloads through open-weight models built in China.

The numbers are no longer a rounding error. The share of tokens U.S. developers send to Chinese models through OpenRouter has stayed above 30% every week since early February 2026 and has spiked as high as 46% — up from roughly 11% over the prior year, and under 2% a year ago. By April, the combined weekly volume of Chinese providers including Zhipu (Z.ai), DeepSeek, Alibaba, MiniMax, Xiaomi and StepFun topped 45% of OpenRouter's total.

## The economics that broke the dam

The driver is blunt: price. Open-weight Chinese models run roughly 60% to 90% cheaper than the flagship offerings from Anthropic and OpenAI, and at the extremes the gap is staggering. DeepSeek V3.2 lists around $0.28 per million input tokens against roughly $10 for GPT-5.2 — a 35x difference for teams whose inference bills scale with every agent loop and every retry.

The model that turned heads is Z.ai's GLM-5.2, released June 13 under a permissive MIT license. It is a Mixture-of-Experts system with roughly 744 billion total parameters (about 40 billion active), a genuine 1-million-token context window, and pricing near $1.40 input / $4.40 output per million tokens on Fireworks — five to seven times cheaper than Opus 4.8 or GPT-5.5 on output. The performance is what unsettled competitors. On the FrontierSWE dominance benchmark, GLM-5.2 scored 74.4%, edging out GPT-5.5 (72.6%) and landing within a point of Claude Opus 4.8 (75.1%). On the MCP-Atlas tool-use evaluation it hit 77.0, just shy of Opus 4.8's 77.8. On one closely watched agentic benchmark it finished within a percentage point of Opus 4.8 at roughly a fifth of the cost.

It also spread faster than anything else this year. GLM-5.2 saw the quickest adoption of any model Vercel tracked in 2026, with daily token volume growing about 27x and its customer count roughly 80x in its first full week. Vercel's CEO said he was "almost shocked" by the coding output.

"U.S. companies were prioritizing AI adoption regardless of model," Yacine Jernite, head of machine learning at Hugging Face, told CNBC. "Now they're getting more cost-conscious."

## A crowded, fast-moving field

GLM-5.2 is not alone. DeepSeek remains the household name after its early-2025 debut. Moonshot's Kimi and MiniMax models are in heavy rotation. And on June 30, Meituan open-sourced LongCat-2.0, a 1.6-trillion-parameter agentic coding model — also MIT-licensed — that scored 59.5 on SWE-Bench Pro, beating GPT-5.5's 58.6. Its more provocative detail: it was trained end-to-end on more than 50,000 domestic Chinese ASICs, with no Nvidia GPUs, and had quietly topped OpenRouter for two months under the alias "Owl Alpha," racking up roughly 10.1 trillion monthly tokens before anyone knew its origin.

That anonymity cuts to the heart of the American discomfort. Open weights mean a model can be self-hosted, and self-hosting is precisely why cost-sensitive enterprises are willing to look past the "made in China" label. Run GLM-5.2 or DeepSeek on your own AWS or GCP infrastructure and the data never touches Chinese jurisdiction — a configuration that lawyers increasingly view as the only viable path for HIPAA, GDPR, and financial-services compliance.

## The security asterisk

The caveats are real. Hosted Chinese endpoints remain a compliance minefield: China holds no GDPR adequacy decision, DeepSeek has no standard contractual clauses in place, and Italy banned it within 72 hours of reviewing its practices. A Booz Allen Hamilton report flagged the risk of Chinese models writing, debugging and reviewing American software at scale, and survey data shows 76% of enterprises would likely switch providers over data-sovereignty fears — a figure that climbs to 87% in the United States. The open-weight route defuses much of that, but only for teams disciplined enough to keep everything self-hosted and audited. Convenience-seeking developers hitting the cheap hosted APIs directly are the exposure most security leaders worry about.

For OpenAI and Anthropic, the strategic bind is sharper than a single lost customer. Their premium is justified by a quality lead that is now measured in fractions of a benchmark point, against rivals that give the weights away. Zhipu's founder has reportedly suggested a Fable-class Chinese model could land before the end of 2026 — a claim that, a year ago, would have been dismissed.

## What to watch next

Three things. First, whether the U.S. frontier labs answer with price cuts or with a capability jump big enough to re-justify the premium. Second, whether Washington moves from advisory warnings — the Booz Allen and AEI-style alarms — toward procurement restrictions that would force enterprises to choose sides. And third, whether that 46% peak in developer token share becomes a ceiling or a floor. If self-hosted open weights keep closing the quality gap at a fifth of the cost, the question stops being why American companies use Chinese models and becomes why they wouldn't.
