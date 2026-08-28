Nvidia has agreed to buy Hugging Face for $12.9 billion, The Information reported Wednesday night, citing a person familiar with the deal. Reuters relayed it. Business Insider, which first reported over the weekend that Hugging Face was fielding takeover interest, said the same night that the talks had not yet produced a signed agreement and could still fall apart. Neither company has confirmed anything, and neither responded to comment requests from Reuters, CNBC, TechCrunch or Fortune.

That silence is the interesting part. As TechCrunch editor-in-chief Connie Loizos noted, Nvidia has a history of moving fast to knock down reports it considers inaccurate. It has not knocked this one down.

Treat the number as reported rather than final. The strategic logic is legible enough that a denial would be the bigger surprise.

## What $12.9 billion buys

Hugging Face is the closest thing open-source AI has to a public square. Model weights, datasets, benchmarks, the Transformers and Diffusers libraries, and millions of developer accounts live there. Everyone publishes on it: Meta, Alibaba, Mistral, DeepSeek, Moonshot AI, Google. It is infrastructure Nvidia cannot fabricate on a wafer.

The price is the eye-watering part. Hugging Face last raised in August 2023, a $235 million round led by Salesforce Ventures at a $4.5 billion valuation, with money from Alphabet's GV, IBM Ventures, Amazon, Intel, AMD, Qualcomm and Nvidia itself. The Information puts current annualized revenue at roughly $150 million, up from about $100 million two months earlier. At $12.9 billion, that is a multiple of about 86 times revenue. Nvidia is not buying a P&L. It is buying a chokepoint.

The timing sits inside a larger pattern. Nvidia reported fiscal Q2 2027 revenue of $96.2 billion, up 106 percent year over year, with data center revenue of $89 billion and profit of $59.7 billion. It has been converting that cash into position across the stack: a reported $6 billion deal to license technology from Poolside and hire more than 100 of its engineers, continued investment in its own Nemotron open models, and reported moves on Groq and Perplexity. Hugging Face would also hand it a second run at cloud, roughly a year after it scaled back DGX Cloud.

## The neutrality problem

Here is the part that should make developers uneasy, and it is not hypothetical.

Late last year, Hugging Face turned down a $500 million investment from Nvidia that would have valued it at $7 billion. According to the Financial Times, the company declined because it did not want a single dominant investor able to sway its decisions. That was the neutrality argument, made by its own management, about this specific counterparty. Nine months later, the same counterparty is reportedly buying the whole thing.

Neutrality is not an abstraction on Hugging Face. Its Optimum libraries support Nvidia's TensorRT-LLM alongside Optimum AMD, Optimum Intel and AWS accelerators. Nvidia's NIM containers already pull models directly from hf:// repository paths. Under Nvidia ownership, nobody needs to delete AMD support to tilt the field. They only need to make the CUDA path require fewer steps.

Analysts are split. Sid Nag, founder and chief research officer at Tekonyx, told Fierce Network the deal would give Nvidia "direct access to the developers, models, datasets and deployment activity driving AI adoption." But he flagged the cost. "It is positive for open-model funding and adoption but potentially negative for ecosystem neutrality," Nag said. "The concern is that an important neutral marketplace could gradually become an Nvidia-centered distribution channel."

Others are blunter about fit. David Linthicum, founder of Linthicum Research, wrote on LinkedIn that this is "two very different companies trying to come together to create a 1+1=3 scenario, when I believe the end state is going to be 1+1=1.2." Patrick Moorhead of Moor Insights and Strategy was more neutral, calling it "a way for Nvidia to get more closely aligned with developers."

Jensen Huang, asked on the earnings call whether open models help or hurt Nvidia, gave the answer that explains the whole deal. "The world will need both closed models and open models," he said. "Both closed models and open models are skyrocketing in use. So long as models succeed, I'm very happy."

That is the real thesis. Every closed lab that matters, OpenAI, Google, Amazon and Anthropic, is building its own silicon. OpenAI this week published results for its Jalapeño accelerator claiming 1.5 to 1.9 times more work per watt and up to 3.6 times lower end-to-end latency on large open-weight models. A thriving open ecosystem is Nvidia's hedge against the labs that want to leave. Owning the distribution hub for that ecosystem is how you make sure the hedge stays profitable.

## What to watch

Antitrust review is the first gate. Nvidia's $40 billion bid for Arm collapsed in 2022 under global regulatory pressure, and the structural objection there was similar: a dominant player acquiring neutral ground everyone else depends on. Hugging Face's $150 million in revenue makes the usual market-share math awkward, but merger authorities in the US, EU and UK have grown more willing to reason about ecosystem control rather than revenue share.

Second, watch the publishers. If AMD, Intel and AWS keep funding engineering work on integrations maintained inside a competitor-owned platform, neutrality survives in practice. If that work quietly migrates elsewhere, the moat Nvidia paid 86 times revenue for starts draining.

Third, watch Clem Delangue. He has spent the year publicly aligned with Nvidia's open-weight lobbying, co-signing a letter with Huang and more than 20 other companies urging Washington not to restrict open models, and warning in a CNBC interview that China is clearly dominating open-source AI. He also told TechCrunch last month the company was close to profitability, which means he was not selling from weakness.

Hugging Face is having an otherwise cheerful week: it and Pollen Robotics opened preorders Thursday for Microduck, a $399 open-source biped with an Apache 2.0 stack. That is the company developers thought they were getting. The question is who owns it in six months.
