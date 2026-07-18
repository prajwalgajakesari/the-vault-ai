Sometime on the evening of July 16, with no keynote, no press conference and not even a public model card, Moonshot AI flipped a switch on kimi.com. When it lit up, the Beijing startup had quietly shipped the largest open-weight language model the world has ever seen — a 2.8-trillion-parameter system called **Kimi K3** that, by several independent measures, now sits shoulder-to-shoulder with the closed flagships from Anthropic and OpenAI.

That combination — frontier-class performance, open weights, and a Chinese lab building it under U.S. compute export controls — is why K3 has become the most-discussed model release of the summer. It is not an incremental update. It is a statement.

## The biggest open model ever built

K3 is a sparse mixture-of-experts (MoE) model with roughly **2.8 trillion total parameters**, more than 2.5 times the size of its 1-trillion-parameter predecessor, K2.6. That dwarfs every other Chinese release to date: DeepSeek's V4-Pro (1.6 trillion) and Zhipu's GLM-5 series (744 billion) are both a fraction of its size.

But the raw parameter count is misleading, and deliberately so. Because K3 is a MoE model, only a sliver of those parameters fire on any given token. According to a technical breakdown published by *Fello AI*, K3 activates just **16 of its 896 experts** per token — roughly 1.8 percent of the pool, an unusually aggressive sparsity ratio that keeps inference costs far below what 2.8 trillion parameters would otherwise imply. Moonshot credits three architectural pieces for making that ratio trainable at all: *Kimi Delta Attention* (KDA), a hybrid linear attention mechanism the company says enables up to 6.3x faster decoding at million-token lengths; *Attention Residuals* (AttnRes), which it claims delivers about 25 percent higher training efficiency for under 2 percent added compute; and a *Stable LatentMoE* framework. Together, Moonshot says, they yield roughly a 2.5x improvement in scaling efficiency over K2.

The model ships with a **1-million-token context window** — four times K2.6's 256K — plus native multimodal input (text, image and video) and always-on reasoning, tuned by a `reasoning_effort` parameter that currently offers only its highest "max" setting. Independent developer Simon Willison tested the vision stack directly and reported that "vision works well: the alt text it generated is very good."

## The benchmarks — and the caveats

The headline results are genuinely striking. On the blind human-preference platform Arena.ai, K3 seized the number-one spot in the **Frontend Code Arena** with 1,679 points, edging past Claude Fable 5 (1,631) and GPT-5.6 Sol (1,618) — a 17-place leap from where K2.6 had ranked. On Artificial Analysis's evaluations, the firm reported that "Kimi K3 reaches an overall Elo of 1547, +732 points from Kimi K2.6 and behind only Claude Fable 5," and slotted the model at #3 on its composite Intelligence Index, comparable to Claude Opus 4.8 and GPT-5.5. No open-weight model has ever placed that high.

Two caveats matter. First, many of the eye-catching numbers are Moonshot's own; the company's self-reported suite has K3 "mostly beating Claude Opus 4.8 max and GPT-5.5 high, while losing out to Claude Fable 5 and GPT-5.6 Sol," as Willison summarized. Second, at launch there was no downloadable weights file, no license and no formal model card — meaning the broader research community cannot yet independently reproduce the claims.

The pricing is its own signal. K3 is listed at a reported **$3 per million input tokens and $15 per million output tokens** (with cache-hit input as low as $0.30). That undercuts Western flagships like Opus 4.8, but it is roughly five times the uncached input price of K2.6 and, as Willison noted, makes K3 "the most expensive model released by a Chinese AI lab to date." The era of dirt-cheap Chinese models, in other words, may be ending — a sign these labs now believe their output is worth frontier money.

## What a frontier-class open model changes

The strategic weight of K3 is inseparable from three years of U.S. semiconductor export controls designed to slow exactly this. Moonshot built a 2.8-trillion-parameter model anyway. The subtext of the launch — landing just before the World Artificial Intelligence Conference in Shanghai — is that GPU and lithography restrictions have not prevented Chinese labs from reaching, or nearing, the frontier.

Wall Street noticed. **Morgan Stanley** analysts wrote that K3 signals "an all-round catch-up of Chinese LLMs with US leaders in model size, performance, and pricing," adding that they "do not view K3 as an overnight miracle but rather as the result of cumulative progress across China's AI model industry." Bernstein's Robin Zhu was blunter about what convergence means for the economics of the closed labs: *"Convergence of reasoning capabilities at the frontier is directionally negative for AI model lab terminal margins."*

That is the deeper story. An open-weight model at this scale is something any developer, company or government can download, inspect, fine-tune and self-host — with no API dependency on a Western vendor. When K2.6 went open in April, it climbed to become the second most-used model on OpenRouter. Extending that playbook to a model that trades blows with Opus 4.8 pressures the entire pricing structure of frontier AI, and hands the open ecosystem a ceiling it has never had before.

## What to watch

The pivotal moment is still ahead. Moonshot has promised to publish K3's full open weights **by July 27**. If the download lands with a real license and a model card, the research community will finally be able to verify — or puncture — the benchmark claims, and K3 could become, overnight, the most capable freely available model on Earth. Until then, the sensible posture is the one Tom's Hardware's comment threads captured well: impressive, plausibly historic, and unverified. In nine days, everyone will know for sure.
