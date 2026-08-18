For three years the deal every AI developer had to accept was simple: you could have the smart model or the fast one. Pick. On August 13, OpenAI said it no longer intends to make anyone choose. The company opened a limited API preview of **Ultrafast**, a service tier that runs GPT-5.6 Sol — its most capable model — at **up to 750 output tokens per second**, or up to **14 times** Standard throughput. The silicon underneath is not Nvidia's. It is Cerebras.

Both companies were careful about the same claim: this is a speed change, not a model change. "GPT-5.6 Sol Ultrafast powered by Cerebras runs with the same intelligence as GPT-5.6 Sol Standard," Cerebras (NASDAQ: CBRS) said. OpenAI framed it as a direction, not a product line: "Until now, getting real-time speed typically meant choosing a smaller or more specialized model. Ultrafast points to progress in a new direction: *more useful work per second.*"

## What was actually announced

Ultrafast is a service tier in the OpenAI API, available today only to a select group of preview customers, with a signup form for everyone else. OpenAI has **not disclosed pricing**, has not published rate limits for the tier, and has not committed to a general-availability date. It has also not announced Ultrafast access in ChatGPT or Codex. Third-party trackers list GPT-5.6 Sol's Standard pricing at $5 per million input tokens and $30 per million output, but The Vault could not corroborate any official Ultrafast rate — whether it carries a premium is, as of this writing, unknown.

The 14x multiple implies a Standard baseline around 50 to 55 tokens per second, roughly where independent trackers place frontier reasoning models. Cerebras put harder numbers on the wall with its own benchmarking. On **Humanity's Last Exam**, a 2,500-question set spanning graduate-level chemistry, economics and literature, GPT-5.6 Sol on Ultrafast finished the full battery in **11 hours and 11 minutes**. Claude Fable 5 needed **78 hours and 27 minutes** — more than three days of continuous compute — to reach comparable accuracy, making Ultrafast nearly **7x faster** to the same answer. On **GDP-Val**, a benchmark of economically valuable knowledge work, Cerebras reports a **5.6x end-to-end speedup with no quality degradation**.

A caveat belongs on those figures: both were run by Cerebras, not a neutral third party, and the HLE comparison used different harnesses on different dates. The cross-vendor claims Cerebras cites separately — 5x faster than Claude Opus 4.8 in Fast mode, 11x faster than Claude Fable 5 — do lean on Artificial Analysis's published output-speed measurements.

The architecture argument is the durable part. Frontier inference is bottlenecked by memory bandwidth: on GPUs, weights shuttle repeatedly between on-chip memory and off-chip storage to emit each successive token. Cerebras packs **44 GB of SRAM onto each wafer-sized chip**, keeps weights resident, and pipelines tokens through layers spread across wafers — an approach it says "scales smoothly with model size."

## The partnership behind it

Ultrafast is the first customer-visible output of a deal signed in January. On January 14, the two companies announced a multi-year agreement to deploy **750 megawatts** of Cerebras wafer-scale systems in stages through 2028 — reported by Bloomberg and CNBC at **more than $10 billion**, and billed by Cerebras as the largest high-speed AI inference deployment in the world.

"GPT-5.6 Sol on Ultrafast is proof that speed and intelligence are no longer mutually exclusive," said **Andrew Feldman**, CEO and co-founder of Cerebras. "Together with OpenAI, we're putting frontier intelligence in the hands of users at unprecedented speed and changing what's possible with AI."

OpenAI's framing was noticeably more measured. "By combining GPT-5.6 Sol with Cerebras' inference technology, we're exploring what becomes possible when customers can get the intelligence of our most capable models with significantly lower latency," said **Sachin Katti**, VP of Compute Strategy & GPT-Infra at OpenAI. "We're starting with a small group of customers to learn where that speed creates meaningful value, and we'll use those learnings to inform how we expand the service over time." Notably, Sam Altman did not appear in either company's announcement materials.

## Why It Matters

Inference speed is becoming the competitive axis that benchmark scores were two years ago. When every frontier lab clusters within a few points on reasoning evals, the differentiator shifts to how much of that intelligence you can spend per second — a hardware and systems question, not a training question. Cerebras's bet is that wafer-scale SRAM gives it a structural lead there that GPU roadmaps cannot close by iterating.

What sub-second agent loops unlock is a change in product shape, not just responsiveness. "Ultrafast allows us to create synchronous experiences for users that were previously limited by intelligence," said **Mitch Troyanovsky**, co-founder of Basis. "Oftentimes the barrier to truly fast products is not just tokens per second, but also model intelligence, and ultrafast combines both." **Alex Wang** of Rogo's applied AI team put it plainly: "Speed doesn't just make the product feel better. It changes what people can realistically use it for."

The internal evidence is the most telling. OpenAI says its own engineers use Ultrafast for incident response — reading logs, analyzing traces and preparing fixes while an outage is still unfolding — and that overnight experiment batches are collapsing into same-day iteration loops. Jane Street, Podium and Rogo are testing it in coding, voice and financial research. Each is a workflow where a model that answers in four minutes is a report generator, and one that answers in fifteen seconds is a participant.

## What to Watch

Three things. First, price: OpenAI's silence on Ultrafast rates is the biggest unknown, and a steep premium would confine this to high-margin verticals rather than making speed a default. Second, capacity — both companies tie expansion to buildout, and the 750 MW deployment runs through 2028, so the preview's ceiling is physical, not commercial. Third, whether rivals answer. Anthropic and Google have their own accelerator relationships, and if 750 tokens per second becomes the expectation for frontier-class output, the pressure to match it lands on Nvidia's roadmap as much as anyone's.
