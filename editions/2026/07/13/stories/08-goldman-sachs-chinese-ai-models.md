# Goldman Sachs Tells Clients Which Chinese AI Models to Use, Marking Their Enterprise Normalization

When one of Wall Street's most conservative institutions starts handing clients a shopping list of Chinese AI models, the question is no longer whether Western enterprises will run open weights from Hangzhou and Beijing. It is which ones, and how soon.

On July 12, Goldman Sachs published a competitive framework ranking China's large-language-model developers and named its preferred picks, CNBC reported. The bank's analysts scored labs on time-to-market, LMArena crowd rankings, valuation and pricing, and landed on three favorites: Zhipu (the Hong Kong-listed developer of GLM, also known as Knowledge Atlas), the privately held DeepSeek, and ByteDance. Goldman initiated coverage on Zhipu with a price target of 1,880 Hong Kong dollars, and its analysts found that Zhipu's GLM and DeepSeek's models generally outranked those from Alibaba, Tencent and MiniMax, especially on speed to market and arena score.

The report is less a stock call than a signal. A bulge-bracket bank telling clients that specific Chinese open-weight models belong in their consideration set is a milestone in the quiet normalization of those models inside Western enterprise stacks.

## The field Goldman is ranking

The Chinese open-weight roster is genuinely strong, not a discount alternative. On BenchLM's Chinese-model leaderboard as of July 2026, DeepSeek V4 Pro (Max) leads at 87, followed by GLM-5.1 at 83, with Kimi K2.6 from Moonshot and GLM-5 (Reasoning) tied at 81 and Alibaba's Qwen3.5 at 79. On Vellum's open-weight leaderboard, GLM-5.2 and Kimi K2.6 sit at the top, and GLM-5.2 posts the leading open-weight score on the Artificial Analysis Intelligence Index (51) and 62.1% on SWE-bench Pro.

Four of the world's top five open-weight positions now belong to Chinese labs: DeepSeek, Moonshot, Zhipu and Alibaba. Alibaba pushed Qwen3.6-Max-Preview out this month. Goldman's own analysis put the gap starkly, finding that China's open models have reached rough parity with top proprietary systems while achieving comparable capability at 2% to 10% of the parameter size, and at far lower cost.

## The cost arithmetic

The economics are what make this more than a benchmark curiosity. DeepSeek V4-Pro is priced at roughly $0.435 per million input tokens and $0.87 per million output; its Flash tier runs as low as $0.14/$0.28. Compare that to the frontier US tier: GPT-5.5 lists at $5 input and $30 output per million tokens, with Pro configurations reaching $30/$180.

That is a 30-to-100x spread on output tokens, for models that independent leaderboards peg at roughly 80% to 90% of frontier capability. For an enterprise running high-volume, latency-tolerant workloads — document processing, code generation, agentic pipelines that burn tokens by the billion — the math is brutal. As DataCamp's pricing analysts framed it, the gap is large enough that "even a meaningful quality difference would need to be justified task by task." For most tasks, it can't be.

Open weights compound the advantage. Because these models ship with downloadable parameters, enterprises can self-host behind their own firewalls, sidestepping the data-residency and vendor-lock concerns that dog API-only frontier models — the same dynamic Goldman flagged when it noted open-weight releases are "accelerating developer adoption and creating ecosystem lock-in."

## The geopolitical whiplash

Here is where the story gets uncomfortable. Goldman's endorsement lands weeks after the three leading US labs moved to wall the same Chinese developers off from their systems.

In April, OpenAI, Anthropic and Google began coordinating through the Frontier Model Forum to detect and block "adversarial distillation" — the practice of feeding prompts to a powerful model, harvesting the outputs, and using them to train a cheaper imitator. Anthropic publicly named DeepSeek, Moonshot and MiniMax as having distilled its Claude models, alleging the three generated more than 16 million exchanges through roughly 24,000 fake accounts. By Bloomberg's account on July 13, those warnings had spilled into a full "distillation debate" in Washington, with US officials estimating the practice costs American labs billions annually.

So within a single week, the same DeepSeek and Moonshot models that Anthropic accuses of intellectual-property theft are the ones Goldman is recommending to institutional clients. The contradiction is the point: capital markets are treating capability and cost as facts on the ground, largely indifferent to the provenance fight consuming the labs.

The chip-policy angle sharpens the irony. Washington has spent years tightening export controls to slow Chinese AI by starving it of advanced silicon. Yet the efficiency those constraints forced — Chinese labs squeezing frontier-class results from smaller, cheaper models — is exactly what now makes them attractive to cost-conscious Western buyers. The policy meant to contain Chinese AI helped produce the parameter-efficient models a Wall Street bank is now urging clients to adopt.

## What Goldman is really betting on

Read carefully, Goldman's thesis is structural, not tactical. The bank has separately urged clients to take long-term exposure to China's AI value chain, noting global funds remain underallocated to it. Naming preferred models is the retail-facing edge of that call: if Chinese open weights are going to underpin a meaningful share of enterprise inference, the infrastructure, developer ecosystems and equities around them are undervalued today.

For enterprise buyers, the framework offers cover. "Which Chinese model should we use?" has been a question CIOs asked privately, wary of the compliance and reputational optics. A Goldman ranking makes it a defensible line item.

## What to watch next

Three things. First, whether US regulators respond to normalization with new friction — procurement bans, data rules, or restrictions on hosting Chinese-origin weights, any of which could freeze the enterprise thaw Goldman is betting on. Second, whether the distillation dispute escalates from terms-of-service enforcement to litigation, which would force buyers to weigh legal exposure alongside price. Third, whether US labs respond with cheaper open-weight tiers of their own — the only durable counter to a 30x cost gap. If they don't, Goldman's list won't be the last one clients see. It will be the first of many.
