# Gemini 2.5 Pro Deep Think Resets the Science Leaderboard With 82.4% GPQA

Google has retaken the lead in machine scientific reasoning. On June 22, the company shipped Gemini 2.5 Pro with a new extended-reasoning mode called Deep Think, and the model promptly posted a 82.4% score on GPQA Diamond, the toughest standardized test of graduate-level science reasoning the field has. That number edges past Fable 5 at 79.1% and leaves OpenAI's GPT-5.5 at 76.3%, and it does something more symbolically loaded than win a leaderboard row: it pushes a frontier model past the roughly 81% accuracy that human PhDs in the relevant fields achieve on the same questions.

GPQA Diamond is not a trivia test. It is a curated set of 198 multiple-choice questions in biology, physics and chemistry, written and validated by domain experts and deliberately engineered to be "Google-proof." Skilled non-experts with full internet access score around 22%, barely above the 25% random baseline. The benchmark has become, in the words of its own documentation, "the standard test for can this model reason at a graduate science level." Crossing the human-expert line on it is the kind of result Google was always going to lead with.

## What Deep Think Actually Does

Deep Think is the headline feature, and it is best understood as a mode rather than a separate model. Where a standard query gets a fast, single-pass answer, Deep Think lets Gemini 2.5 Pro spend more time and compute exploring a problem before it commits. Google describes the technique as parallel reasoning: the model "explores multiple hypotheses simultaneously," then critiques and prunes them before converging on a final answer.

"Deep Think enables Gemini to creatively produce multiple hypotheses and carefully critique them before arriving at the final answer," Google has said of the approach, and that description maps cleanly onto where the mode pays off. It is built for complex mathematics, multi-step scientific analysis, hard coding challenges and decisions with many interdependencies, the situations where a first instinct is often wrong and the value is in the second, third and fourth look.

That design choice is also the model's defining tradeoff. Deep Think is slower and more expensive than standard inference, which is why Google is pricing it as a premium tier rather than the default.

## The Benchmark Scorecard, In Full

GPQA is the marquee result, but the rest of the card is where the competitive nuance lives. On MMLU-Pro, the broad knowledge-and-reasoning suite, Gemini 2.5 Pro Deep Think lands at 89.8%. On HumanEval+, the function-level coding benchmark, it posts 94.1%, which Google is calling a record.

Then the picture gets more interesting. On SWE-bench Verified, the benchmark that measures whether a model can resolve real GitHub issues in real repositories, Gemini comes in at 76.4%. That is comfortably ahead of GPT-5.5's 67.2%, but it sits well below Fable 5's 88.6%. In other words, Gemini can write a correct function as well as anything on the market, but Fable 5 is still meaningfully better at the messier, agentic work of navigating an existing codebase, locating a bug and shipping a fix that passes the tests.

The split is the story. Gemini 2.5 Pro Deep Think is, on these numbers, the strongest science-and-reasoning model available and a top-tier pure-coding model, while Fable 5 retains the crown for end-to-end software engineering and GPT-5.5 trails both on this particular battery.

## Pricing and Availability

The model is available now through the Gemini API, Google AI Studio and Vertex AI, putting it in front of both individual developers and enterprise buyers from day one. Standard Gemini 2.5 Pro inference is priced around $2.50 per million input tokens, competitive with the rest of the frontier. Deep Think, because it burns substantially more compute per query, is estimated to run roughly four times that. The pricing structure makes the intended usage explicit: run standard mode by default, reach for Deep Think when a problem is hard enough to justify the bill.

One point worth clarifying, because the naming invites confusion: this is Gemini 2.5 Pro, not the still-unshipped Gemini 3.5 Pro with its anticipated 2-million-token context window. Deep Think is a reasoning mode layered onto the 2.5 line, and it should be read as Google's answer to Claude's Extended Thinking and OpenAI's o-series reasoning models rather than as a generational jump in the base model.

## The Competitive Read

Strip away the leaderboard theater and the positioning is coherent. Reasoning modes that trade latency and cost for accuracy on hard problems have become table stakes at the frontier; every major lab now ships one. Google's pitch with Deep Think is that for science, research and engineering analysis, the parallel-hypothesis approach plus a record GPQA score makes Gemini the default choice, even if it is not the cheapest or fastest option for routine work.

The timing matters too. Deep Think arrives with OpenAI widely expected to ship GPT-5.6 in the near term, and Google's move reads partly as an attempt to plant a flag on the science-reasoning narrative before that launch reframes the conversation. Whether 82.4% on GPQA still looks like a lead in a month is an open question.

## What to Watch

Three things. First, independent verification: benchmark numbers reported by labs have a way of softening when outside evaluators run them, and the human-expert-crossing claim invites scrutiny. Second, real-world reasoning versus benchmark reasoning, particularly whether Deep Think's GPQA strength translates into trustworthy performance on novel scientific problems that are not multiple-choice. And third, the SWE-bench gap, because if agentic coding is where the enterprise budget is going, Gemini leading on science while trailing on software engineering is a meaningful asterisk on an otherwise dominant week.
