On July 8, Elon Musk did what has become a familiar ritual: he announced a frontier AI model with a social-media post rather than a technical report. "Based on strong positive feedback from customers in our beta test program, @SpaceXAI will make Grok 4.5 available to the public tomorrow," Musk wrote on X, the platform his own company now owns. "It is an Opus-class model, but faster, more token-efficient and lower cost."

The claim is bold, and the framing is deliberate. "Opus-class" measures Grok 4.5 against Claude Opus 4.8, the model widely regarded as the high-water mark for complex reasoning and agentic coding. What Musk did not provide alongside the boast was the evidence enterprises typically demand before betting production workloads on a new model: no formal system card, no independently reproducible benchmark table, no published context-window specification, and, at the moment of the announcement, no per-token price sheet from the company itself.

## What SpaceXAI actually shipped

Grok 4.5 went public on July 9, roughly two weeks after a private beta that began June 28 across SpaceX and Tesla. It is the first major model release since xAI rebranded to SpaceXAI on July 6, the final step in an absorption that started with SpaceX's February 2 acquisition of xAI and continued with its roughly $60 billion, all-stock purchase of Cursor maker Anysphere in June.

That acquisition is baked directly into the product. Grok 4.5 is built on the V9 foundation model, a 1.5-trillion-parameter base that triples the scale of the V8 series behind Grok 4.3 and shifts the training emphasis toward coding and agentic tasks. Crucially, SpaceXAI supplemented that base with training data drawn from Cursor, the AI code editor it now owns, positioning the model squarely at software developers.

The pricing that emerged tells the real story of the launch. Through the API, where the model ships under the ID `grok-4.5` on an OpenAI-compatible endpoint, SpaceXAI is charging $2 per million input tokens and $6 per million output tokens, with cached input at $0.50. Set against Opus 4.8 at $5 and $25, that is a discount of more than 60 percent on input and roughly 75 percent on output. Consumers reach the model through SuperGrok Heavy (a $99-per-month promotional rate rising to $149 standard) or X Premium+ at around $16 per month.

## The benchmark that wasn't

SpaceXAI did circulate a marketing chart on launch day suggesting Grok 4.5 edges past rivals on selected coding and agentic tests. But a promotional graphic is not a system card, and the gaps are conspicuous. As one review of the release put it bluntly: "There is no system card, no benchmark sheet, and no API note from xAI for Grok 4.5" - a problem for "any regulated workload that needs a model card to clear review."

The independent numbers that have trickled in complicate the Opus-class narrative. On the Artificial Analysis Intelligence Index, Grok 4.5 scored 54 and ranked fourth, behind Claude Fable 5, Claude Opus 4.8, and GPT-5.5, though it topped the field on agentic tool use and posted 51.4 percent on the AutomationBench-AA agent test, ahead of Opus 4.8's 48.5 percent. More troubling for a model pitched at enterprise work: its accuracy on the AA-Omniscience Index climbed from 35 to 52 percent over Grok 4.3, but its hallucination rate jumped from 25 to 54 percent. Grok 4.5 is more often right, and, when wrong, more confidently so. Cursor was also forced to strike its own CursorBench scores from the launch after an earlier snapshot of its codebase turned up in the training data, handing the model an unearned edge.

Musk himself dialed back the headline in a follow-up post: "Our internal assessment is that Grok 4.5 is roughly comparable to Opus 4.7, but much faster." That is a notably softer claim than "Opus-class" against the newer 4.8.

## Why it matters

The strategy is legible even without the paperwork. In a market where token cost has become the dominant procurement concern, SpaceXAI is buying attention with price and speed rather than winning it on raw capability. If Grok 4.5's "twice greater token efficiency" holds in real workloads, the effective cost gap versus Opus widens further, and for high-volume coding agents that math can matter more than a few benchmark points.

But the credibility gap is real, and it is not only about missing charts. Skeptics have flagged a trust problem specific to this vendor. "How can you trust their models to be reliable in a business setting," one asked, "with the foreknowledge that their models are being nudged around in the backend?" For risk-averse enterprises, an undocumented model from a company with a history of steering Grok's outputs is a hard sell, however cheap the tokens.

## What to watch

Three things over the coming weeks. First, whether SpaceXAI publishes an actual system card, benchmark methodology, and context-window spec - the absence of which currently blocks regulated buyers. Second, how Grok 4.5 fares against OpenAI's GPT-5.6, which was slated to arrive within a day of the launch, turning the week into a direct frontier collision. And third, whether independent evaluators confirm or puncture the "Opus-class" label. Until then, the claim rests where Musk left it: on a post, not a paper.