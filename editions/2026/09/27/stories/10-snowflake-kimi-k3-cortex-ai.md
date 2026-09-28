# Snowflake Opens Private Preview of Moonshot's Kimi K3 in Cortex AI, Following AWS and Databricks

Snowflake has added Kimi K3, the 2.8-trillion-parameter open-weight model from Chinese startup Moonshot AI, to its Cortex AI platform in private preview. That makes Snowflake the third major U.S. data and cloud platform in two months to offer a Chinese frontier model to enterprise customers. It is doing so while Washington is still weighing whether Moonshot should face sanctions.

The announcement came in a September 24 post on Snowflake's AI and ML blog by senior product manager Ali Taha, ML software engineer Danmei Xu and AI product marketer Arun Agarwal. Preview customers can call the model, under the ID kimi-k3, through Cortex AI Functions such as the SQL-based AI_COMPLETE and through Cortex Inference. The model also supports the Chat Completions request format, so developers can reach it with the OpenAI SDK through Snowflake's Cortex REST API. Snowflake says support in its CoCo coding tool, Cortex Agents and Snowflake CoWork is "coming soon."

Snowflake's pitch is about convenience. "Open-weight models at this scale used to require dedicated infrastructure and a team to run it. Now they're a model ID swap," the authors wrote. The company also tells customers that "all inference runs within the Snowflake perimeter, so your data remains secure and within your governance boundary."

## A Very Large Model With Caveats

Moonshot launched Kimi K3 on July 16 and released the weights on July 28. It is a mixture-of-experts model that activates 16 of its 896 experts per token, about 50 billion active parameters. It handles images natively and has a 1-million-token context window. Moonshot reports a 2.5x improvement in scaling efficiency over Kimi K2. Snowflake's post reprints Moonshot's own benchmark table, including 93.5 on GPQA Diamond, 88.3 on Terminal-Bench 2.1 and 91.2 on BrowseComp. Those figures come from Moonshot and have not been independently verified.

Self-hosting the model is a big job. According to Thunder Compute's September guide to open-weight models, K3's native MXFP4 weights take up about 1.56TB, and serving frameworks such as vLLM target 16 Nvidia B200 GPUs. Few enterprises want to run that hardware themselves, and that is the gap managed platforms like Cortex are trying to fill.

Snowflake's post is also more cautious than most launch announcements. It warns that K3 "can be proactive" and may act on a user's behalf rather than ask for clarification. It also says switching into K3 in the middle of a session from another model can hurt output quality. And it repeats Moonshot's own admission that K3's overall user experience "still trails the most powerful proprietary models, Claude Fable 5 and GPT 5.6 Sol."

Some key details are still missing. As Creati.ai noted in a September 26 analysis, Snowflake's announcement does not cover pricing, rate limits, regional availability or when general availability will come. The post does not say which cloud regions host the model, which matters for customers with data-residency requirements.

## Snowflake Is Late to This

Snowflake is not the first to offer K3. Databricks announced it on August 6. Databricks hosts the model in the U.S. through its Foundation Model API, with zero data retention and governance through its Unity AI Gateway, and plans to add more regions. Databricks also pitched K3 on price. "Frontier quality no longer requires frontier pricing," the company wrote, and it claimed K3 delivers "50–72% lower cost-per-task than comparable proprietary models."

Amazon made K3 generally available on Bedrock on September 18, in every Bedrock region through cross-Region inference. AWS said K3 runs "within the same security boundary as proprietary models" and is the first open-weight model on Bedrock to support explicit prompt caching.

All three companies make the same argument: because the weights are open, the platform runs the model itself. Customer prompts go to Snowflake, Databricks or AWS infrastructure, not to Moonshot's servers in China.

## Why It Matters

That argument is about to be tested. Caixin reported that on July 22, a week after K3 launched, White House science and technology adviser Michael Kratsios alleged that Moonshot had built K3 by distilling Anthropic's Fable model. The next day, Treasury Secretary Scott Bessent said the U.S. could consider sanctions or adding companies to the Entity List if Chinese firms were found to be running large-scale distillation attacks. China's Ministry of Commerce rejected the allegations as lacking factual and legal basis.

The industry has mostly pushed back against broad restrictions. According to Caixin, an open letter led by Nvidia CEO Jensen Huang in support of open-source models went from 25 initial signatories, including Meta and Microsoft, to 132 within days, with Amazon, Google and OpenAI among them.

For enterprise buyers, the choice is between cost and compliance. Hosting open weights on U.S. infrastructure keeps data away from Moonshot. But it does not protect customers from sanctions, reputational fallout or a procurement policy that bans models by where they were made. Snowflake's decision to start with a private preview, not general availability, leaves it room to change course if policy shifts.

## What to Watch

The first thing to watch is whether Snowflake publishes pricing, hosting regions and a date for general availability, and whether those match Databricks' U.S.-only hosting or Bedrock's global reach. After that, the key question is whether Treasury or Commerce acts on the distillation allegations. Being placed on the Entity List would force all three platforms to decide quickly whether a model they host themselves still counts as doing business with Moonshot. Microsoft is worth watching too. It signed the Huang letter, but this reporting found no announcement that it offers K3 on Azure.
