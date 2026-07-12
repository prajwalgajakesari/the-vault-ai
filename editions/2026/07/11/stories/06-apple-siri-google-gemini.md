A single line buried in Apple's blockbuster lawsuit against OpenAI settled a question the company had spent six months dancing around: the Siri that Apple ships this fall will not think with OpenAI's models. It will think with Google's.

In the trade-secret complaint Apple filed July 10 in the Northern District of California, the company states plainly that its updated Siri assistant, arriving this fall, is "based on Google's Gemini AI models" rather than the ChatGPT technology Apple once championed. It is a small clause in a hostile filing, but it is the clearest on-the-record confirmation yet of one of the most consequential vendor swaps in consumer technology.

## The deal Apple tried not to describe

The arrangement itself is not new. In January, Apple confirmed it would license a custom version of Google's Gemini to rebuild Siri and power the next generation of Apple Intelligence, after concluding that its own foundation models could not close the gap with the market fast enough. Bloomberg reported Apple would pay Google roughly $1 billion a year for the privilege.

What sets the model apart is its scale. The Gemini variant Apple is licensing is reported at around 1.2 trillion parameters, roughly eight times larger than the approximately 150-billion-parameter cloud model Apple had been running for Apple Intelligence. It uses a mixture-of-experts architecture tuned for summarization, planning and natural-language understanding, the kinds of multi-step tasks the old Siri handled poorly.

Apple executives have gone out of their way to frame the deal as a licensing relationship rather than a surrender. On Apple's fiscal Q4 2025 earnings call, CEO Tim Cook told analysts, "We basically determined that Google's AI technology would provide the most capable foundation for Apple Foundation Models." The phrasing was deliberate: Apple Foundation Models, not Siri, and certainly not Google.

## Where the model actually runs

Apple's public message is that Gemini's weights run inside its own Private Cloud Compute, the Apple Silicon server system it built to process complex requests without exposing user data. In Apple's telling, the model operates behind end-to-end encryption in hardware-isolated enclaves, no user data is shared with Google, and nothing is retained after a query is answered.

That account has not gone entirely unchallenged. On Alphabet's own earnings call, Sundar Pichai described the arrangement differently, saying, "We are collaborating with Apple as their preferred cloud provider and to develop the next generation of Apple Foundation Models, based on Gemini technology." The phrase "preferred cloud provider" set off a round of speculation, reported by 9to5Mac and others, that at least the heaviest reasoning workloads may route to Google's own infrastructure. Reporting since has pointed to a tiered system: simple requests handled on-device, moderate ones on Private Cloud Compute, and the most demanding queries running on Google hardware, with Apple anonymizing and tokenizing requests at each hop.

The rollout is staggered. Early Gemini-assisted features began appearing in the iOS 26.4 cycle this spring; the full Siri rebuild, previewed at WWDC in June, is slated to land with iOS 27's public release in September, alongside the new iPhone lineup.

## What an Apple-Google AI axis means

The strategic subtext is hard to miss. Google already pays Apple an estimated $20 billion a year to remain Safari's default search engine. Now money flows the other way too, binding the two companies more tightly at the exact moment regulators are scrutinizing their search arrangement. For Google, winning the most valuable distribution channel in consumer AI, more than a billion iPhones, is a coup that instantly reframes Gemini as an enterprise-grade product Apple was willing to bet its flagship feature on.

The clearest loser is OpenAI. Eighteen months ago, ChatGPT was the marquee integration inside Apple Intelligence. Today OpenAI has been displaced from Apple's roadmap and is being sued by the company, a stunning reversal for a partnership once presented as the future of the iPhone. Anthropic, which Apple also evaluated during its model search, is left watching a competitor capture the platform prize. The assistant wars, briefly a three-way contest, now look like a Google-anchored duopoly with Apple as the kingmaker distribution layer.

## What to watch next

The open questions are technical and contractual. Watch whether Apple and Google finally reconcile their conflicting descriptions of where inference runs, because privacy-conscious users and regulators alike will want a straight answer. Watch the September iOS 27 launch for whether the rebuilt Siri actually delivers the reliability Apple has promised twice before. And watch the antitrust dimension: two companies this entangled in both search and AI will invite the attention of enforcers already circling their existing deal.
