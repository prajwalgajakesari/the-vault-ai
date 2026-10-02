Google spent the past year trying to show it could still build the best model in the world. Within hours of unveiling Gemini 4 Argon on Wednesday, it was answering an awkward question from inside its own walls: does the model hold up once engineers stop running benchmarks and start shipping code with it?

Bloomberg reported Wednesday, September 30, that some Google employees with direct access to Gemini 4 are skeptical of how it performs on real work. The model scores well on the standard industry tests, they said, but does noticeably worse once employees put it to work, and it struggles with certain coding tasks. Google rejects that account. The report still landed at a bad moment for a company that needs its flagship model to win back developers.

## What Insiders Told Bloomberg

According to people familiar with Google's internal evaluations, Gemini 4's coding is uneven. One person singled out front-end design, the work that decides how apps and websites look and feel, as a particular weakness. Two people said the model appears affected by "benchmaxxing," the industry habit of tuning models to post high test scores rather than to do a user's job well.

Opinion inside the company is split. Some employees believe the rival models they call Fable (Anthropic) and Astra (OpenAI) are improving faster than Gemini, and that Gemini 4, even at its best, will still trail them in some areas. Others think Google has caught up with the leading labs.

The report also confirmed a costly detour. Google announced Gemini 3.5 Pro at its I/O conference in May and promised to release it in June. That deadline passed, and the company abandoned the model. Bloomberg Intelligence analyst Mandeep Singh estimates that a training run for a model of that class can cost as much as $400 million, before counting the time of highly paid researchers. Argon, which this newsletter covered at launch, is Google's first proprietary model above the Flash tier in more than seven months.

Edwin Chen, founder of the data-labeling startup Surge AI, told Bloomberg that leaning on benchmarks can push labs toward models that write code in a particular language rather than build apps that are well designed and easy to use. "An analogy would be, 'Oh yeah, my kid got a really good score on the SAT' - but the SAT doesn't translate into real-world performance," Chen said. "It's an incredibly pernicious problem."

## Google Pushes Back

Google said it would be "inaccurate" to describe Gemini 4 as underperforming in areas such as coding. It pointed Bloomberg to remarks made the previous week by Koray Kavukcuoglu, who took over day-to-day leadership of Google DeepMind in August when Demis Hassabis became chairman.

"I have the utmost trust in the team," Kavukcuoglu said at a conference hosted by The Information. "In my mind, it's a certainty that we are always gonna be at the frontier."

A Google employee familiar with model development told Bloomberg there is "large consensus" internally that Gemini 4 is at the frontier. The person said the company had tested the model rigorously and denied that it struggles with messy, real-world coding. Tulsee Doshi, who leads Gemini products at DeepMind, said many Googlers were "relying on it for their hardest coding and research problems." Google also highlighted a launch example in which Argon agents replaced 32,000 lines of SIMD code in a Rust port of its libgav1 video decoder, producing a decoder 2.7 times faster.

Independent results are mixed. On the Artificial Analysis Intelligence Index, Argon scored 53, level with GPT-6 Astra and Claude Fable 5.1 but behind Claude Opus 5.5 at 58. On Terminal Bench 4, an agentic coding test, it scored 57%, behind Claude Sonnet 5.5 (64%), Opus 5.5 (60%) and GPT-6 Astra (59%). Yet in Google's own comparison it led on DeepSWE v1.1 with 77.9%. On Arena's web-development leaderboard, the area insiders flagged, it placed eighth.

Investors reacted quickly. Alphabet shares were up more than 2% on Wednesday before the report and closed up just 0.5%.

## Why It Matters

For Google, coding is now a strategic problem, not a niche one. AI coding agents have become one of the industry's most profitable products, and Anthropic and OpenAI are using them to move beyond selling models toward owning developer platforms. Google is behind in that market. Bloomberg reported in April that some DeepMind teams, including some working on Gemini, had been using Anthropic's Claude Code.

Distribution is Google's advantage. Gemini models power Search, Maps, Gmail and Chrome, and each of those has more than a billion users. But distribution does not win developers if the model loses when they compare outputs side by side. If Argon ranks at the top in Google's launch charts but feels second-tier inside an IDE, the gap will show up in API revenue and in where agentic startups choose to build.

The episode also adds to the industry's growing distrust of benchmarks. When a lab's own engineers question whether the scores reflect real use, every leaderboard claim gets discounted a little more. That pushes buyers toward hands-on trials, human-preference arenas and task-specific evaluations, where Argon's results are already more mixed than its headline numbers.

## What to Watch

Most developers still cannot test Argon on their own work. Access goes first to partners in Google's Fairwind cybersecurity program, with paid API customers and AI Ultra subscribers next "as soon as possible" and no firm date. The real verdict will come when that wider release happens: watch front-end and agentic coding results on independent leaderboards, developer adoption in tools like Gemini CLI and Jules, and whether Google ships a coding-tuned variant. Watch too for any sign of further leadership churn at DeepMind, which has already lost Jeff Dean, John Jumper and Noam Shazeer.
