# Moonshot's Revenue Went From $300M to $1B in Two Months

*The Vault — AI Edition | September 12, 2026 | 4 min read | 912 words*

**Category:** business

**Key Takeaway:** Moonshot AI tripled its annualized revenue to more than $1 billion in eight weeks on the back of one open-weight model release, proving that giving away frontier weights and selling inference can be a business — but not yet that it is a profitable one.

---

Moonshot AI told investors its annualized revenue crossed **$1 billion in August**, up from roughly **$300 million in June**, Bloomberg reported — a tripling in eight weeks that the Beijing lab attributes almost entirely to a single model release. The company is now telling backers it expects to double again, to **$2 billion in annualized revenue by the end of 2026**, a target that would put a three-year-old Chinese startup within shouting distance of the revenue scale of the US labs it was supposed to be trailing.

The disclosure lands nine days after Moonshot filed confidentially for a Hong Kong initial public offering, seeking roughly $3 billion at a valuation above $50 billion, with Goldman Sachs, CICC and Deutsche Bank running the books. It is, in other words, a number produced for an audience.

The driver is **Kimi K3**, announced July 16 and released as downloadable weights on Hugging Face on July 27. At **2.8 trillion parameters**, it is the largest open-weight model ever published — a mixture-of-experts system with 896 experts that activates only 16 per token, roughly 1.8 percent of the pool, or about **104 billion active parameters** per forward pass. It ships with a **1 million token context window** and native vision, built on two in-house architectural pieces Moonshot calls Kimi Delta Attention and Attention Residuals.

The benchmarks explain the revenue curve better than the parameter count does. On Arena's Frontend Code leaderboard — blind, developer-voted — K3 took first place globally with **1,679 points**, ahead of Anthropic's Claude Fable 5 at 1,631 and OpenAI's GPT-5.6 Sol at 1,618. On Artificial Analysis's Intelligence Index it scored **57**, sitting just below both of those closed models. Moonshot's own published tables put K3 at 77.8 on ProgramBench against 77.6 for GPT-5.6 Sol and 76.8 for Fable 5, and at 42.0 on SWE-Marathon against 40.0 for Claude Opus 4.8 — company-provided figures, and worth reading as such.

Analysts have been careful not to overstate it. *"While K3 constitutes progress, we'd hesitate to ascribe it near-parity with American frontier models, such as Fable 5, in real-world tasks,"* said **Malik Ahmed Khan**, senior equity analyst at Morningstar. Wei Sun, principal AI analyst at Counterpoint Research, has put the general gap between Chinese and American models at three to six months, varying sharply by task.

## The Cognition proof point

The most commercially interesting evidence that K3 is being *used*, not just downloaded, arrived on September 10. Cognition shipped **SWE-2**, the coding model behind its Devin agent, and disclosed that it is post-trained directly from Moonshot's weights. *"SWE-2 is post-trained from Kimi K3, a 2.8T-parameter model that had already undergone extensive RL for agentic coding,"* the company wrote, adding that its own reinforcement-learning pass added five to six points on many benchmarks.

The result: SWE-2 scores **50.0 percent** on Cognition's FrontierCode 1.1 Main benchmark against 50.9 percent for Fable 5.1 and 53.3 percent for GPT-6 Astra — at what Cognition says is **64 percent lower cost**. Base Kimi K3 scored 44.2 percent on the same test. An American startup took a Chinese open-weight model, spent its own compute on it, and landed within a point of Anthropic's flagship. That is the open-weight flywheel working exactly as designed, and none of that inference revenue flows back to Moonshot.

## Why this matters

Here is the wrinkle in the popular framing. Kimi K3's API list price is **$3 per million input tokens and $15 per million output**, with cached input at **$0.30**. That undercuts US *frontier* pricing meaningfully. It does not undercut China. Alibaba's Qwen3.8-Max runs $2/$6; DeepSeek's V4-Flash runs $0.14/$0.28. Moonshot priced K3 into flagship territory rather than into the bargain bin its predecessor K2 occupied — a deliberate bet that capability, not cheapness, is what enterprises will pay for.

Whether that bet produces margin is a separate question, and the honest answer is that nobody outside Moonshot knows. Counterpoint Research framed the structural problem bluntly in July: China has the best software, it wrote, but the hardware is crippled. Moonshot reportedly runs inference on Nvidia's older H20 systems, the ones still legal in China, and Kimi had to **suspend new subscriptions** at one point this summer because it could not serve demand. Serving a 2.8-trillion-parameter model on constrained silicon at $15 per million output tokens, while a model that is *"hungry"* — developers consistently report K3 burning more tokens than Fable to finish equivalent tasks — is not obviously a gross-margin-positive activity.

Counterpoint's read is that this was never the point: open models are a distribution strategy, and the lab captures less revenue per token while creating more ecosystem value around the model. That works beautifully for market share and terribly for an IPO prospectus.

Context matters on scale, too. Moonshot is not even China's revenue leader — Z.ai's ARR reportedly hit **$1.6 billion** in August, and MiniMax reached $800 million. Against Anthropic's roughly **$65 billion** and OpenAI's **$40 billion** annualized run rates by mid-2026, the entire Chinese frontier cohort is a rounding error.

Three things to watch. First, whether the $2 billion target holds without discounting away the economics investors are pricing into a $50 billion valuation. Second, the Hong Kong listing window, which could open as early as Q4 with a dual Shanghai listing under consideration. Third, Washington: Treasury Secretary Scott Bessent has floated adding Moonshot to a trade blacklist over allegations it trained K3 on restricted Nvidia Blackwell chips and distilled Anthropic's models. A blacklist would not touch Moonshot's Chinese revenue. It would touch every SWE-2 built on top of it.

---

**Sources:**
- [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-11/china-ai-star-moonshot-eyes-2-billion-annualized-sales-in-2026)
- [AI Weekly](https://aiweekly.co/alerts/moonshot-ai-tells-investors-arr-topped-1b-in-august-targets-2b-by-end-of-2026)
- [Cognition](https://cognition.com/blog/swe-2)
- [Counterpoint Research](https://counterpointresearch.com/en/insights/Moonshot-AI-Kimi-K3-shockwave-chinese-dominate-open-frontier-models)
- [CNN Business](https://www.cnn.com/2026/07/23/tech/china-ai-moonshot-kimi-explainer-intl-hnk)
