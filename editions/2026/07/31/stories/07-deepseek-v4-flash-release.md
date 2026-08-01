---
headline: "DeepSeek Ships V4-Flash, a Cheaper, Faster Model in the Open-Weight Price War"
slug: deepseek-v4-flash-release
category: llms-genai
story_number: "07"
date: 2026-07-31
sources:
  - https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
  - https://mlq.ai/news/openai-slashes-gpt-56-luna-prices-80-undercutting-deepseek-as-ai-price-war-intensifies/
  - https://llm-stats.com/llm-updates
  - https://pricepertoken.com/news/model-releases
---

# DeepSeek Ships V4-Flash, a Cheaper, Faster Model in the Open-Weight Price War

DeepSeek pushed a new weapon into the open-weight price war on Thursday, publishing DeepSeek-V4-Flash-0731 to Hugging Face under a permissive MIT license and moving the matching API into public beta the same day. It is the cheaper, faster sibling in the company's V4 lineup, and it arrived in the same week that OpenAI cut the price of its GPT-5.6 Luna tier by roughly 80 percent, a coincidence that neatly captures who is setting the terms of competition in mid-2026.

The headline for developers is cost. DeepSeek's pricing page lists deepseek-v4-flash at $0.14 per million input tokens on a cache miss, a fraction of a cent ($0.0028) on a cache hit, and $0.28 per million output tokens, according to a detailed breakdown by MarkTechPost. That output rate is roughly a third of the $0.87 that the larger DeepSeek-V4-Pro charges. Paired with a 2,500-request concurrency ceiling, the price puts sustained agent loops within reach of seed-stage startups and indie developers who have no GPU budget at all.

What V4-Flash is not is a new architecture. The 0731 model card is explicit that this build supersedes the April preview but leaves the design and parameter count untouched; the gains come from re-post-training, not a redesign. Under the hood it is a 284-billion-parameter Mixture-of-Experts model that activates only 13 billion parameters per token, with a 1-million-token context window and output up to 384K tokens at higher reasoning effort. Each MoE layer pairs one shared expert with 256 routed experts, of which six fire per token, and DeepSeek's technical report describes hybrid attention (its Compressed Sparse Attention and Heavily Compressed Attention schemes) plus more than 32 trillion pre-training tokens. The Hugging Face repository lists 304 billion parameters because it ships with an attached DSpark speculative-decoding module; DeepSeek's DSpark paper reports 60 to 85 percent faster per-user generation versus its previous baseline.

On DeepSeek's own agentic benchmarks, the story the company wants to tell is that a small, cheap model can beat its own flagship. V4-Flash-0731 posts 82.7 on Terminal Bench 2.1, 54.4 on DeepSWE, 76.7 on Cybergym and 70.3 on Toolathlon-Verified, topping the V4-Pro preview on every agentic test DeepSeek published while costing a third as much to run. Those figures put it in the neighborhood of Zhipu's GLM-5.2 and within striking distance of Anthropic's Claude Opus 4.8 on several tasks, though not on the hardest ones. The important caveat is that every number is vendor-reported, and some were run on a "minimal mode" of DeepSeek's harness that has not been released.

That caution matters more than usual here. "All benchmark numbers are vendor-reported on an unreleased harness, so run your own evals first," MarkTechPost's Asif Razzaq warned in his analysis of the release, noting that agent scores are highly sensitive to the harness they run on and that independent runs may diverge. It is a reminder that the leaderboard theater around these launches is exactly that, and that the durable claim is the price, not the podium finish.

The competitive backdrop is what makes a mid-tier Chinese model a front-page event. Reporting compiled around the launch points to Chinese open-weight models capturing a large and growing share of US enterprise token usage on aggregators such as OpenRouter, with V4-Pro already trading at heavily discounted rates. OpenAI's response, dropping GPT-5.6 Luna to about $0.20 per million input and $1.20 per million output tokens, undercut DeepSeek on input pricing even as it stayed pricier on output. DeepSeek answered within the same week by shipping V4-Flash. The pattern is now familiar: a US lab cuts prices, a Chinese lab ships weights, and the floor drops again.

The strategic difference is the license. GPT-5.6 and Claude live only behind an API; V4-Flash's weights are MIT-licensed and ungated, which means an enterprise can pull them down and run inference on its own hardware with no vendor in the loop. The catch is that self-hosting a 284B MoE is not trivial, because every expert must stay resident in memory even though only 13 billion activate per token. DeepSeek's reference setup serves the model on a four-GPU GB300 node, and community quantizations from Unsloth shrink it to roughly 110 GB of combined memory at 3-bit precision. That is out of reach for hobbyists but very much in reach for any mid-size company with a serving cluster, which is precisely the audience US labs would prefer to keep on metered APIs.

For now, DeepSeek left its V4-Pro API, app and web models unchanged, and added native support for the Responses API format plus Codex adaptation on the Flash endpoint, a clear pitch at agent and coding workloads.

What to watch: whether independent evaluations confirm the agentic gains once the harness is public; whether US labs answer with further cuts or with open weights of their own; and whether "cheap, open, good enough" keeps eroding the premium that closed frontier models have long commanded. On current evidence, the pressure is running one direction.
