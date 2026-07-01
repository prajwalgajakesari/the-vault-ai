# Google’s AI Coding Strike Team Pivots to Midtraining After Losing Six Researchers in Five Months

*Tuesday, June 30, 2026 | 5 min read | 842 words*

**Key Takeaway:** Google DeepMind has restructured its emergency AI Coding Strike Team to add a dedicated midtraining phase built on its proprietary codebase, even as six named researchers defected to Meta, OpenAI, and Anthropic since February.

---

Ten weeks after Sergey Brin scrambled an emergency "strike team" to rescue Google from Anthropic’s runaway lead in AI coding, the effort has already been redrawn — and the redesign is an admission of how deep the hole runs. According to a June 25 report from The Information, Google DeepMind has reorganized its AI Coding Strike Team to insert a dedicated midtraining phase, a technically significant escalation that lands as the lab bleeds senior talent to its fiercest rivals.

The Strike Team was assembled in April 2026 as a direct response to Anthropic’s dominance in agentic, long-horizon programming — the kind of work where a model must read an entire codebase, infer developer intent, and autonomously build working software. It is led by Sebastian Borgeaud, who previously ran pretraining for Google’s Gemini models, and is overseen by Brin himself alongside DeepMind CTO Koray Kavukcuoglu. By late June, its remit had expanded from agent-layer engineering into midtraining, the stage that sits between the massive, general pretraining run and the narrower post-training that shapes a model’s behavior.

The urgency is spelled out in an internal memo from Brin. "To win the final sprint, we must urgently bridge the gap in agentic execution and turn our models into primary developers of final code," he wrote, a line that frames coding not as one feature among many but as the decisive front in the AI race.

## Why midtraining, and why now

Midtraining is where a lab can pour domain-specific data — in this case, code — into a model after the broad pretraining phase but before the reinforcement learning and instruction-tuning that finish it. The bet is that Gemini’s coding weakness is baked in too early to be patched with post-training tricks alone, so Google is rebuilding the pipeline upstream. Reports indicate the Strike Team is drawing on Google’s own proprietary internal codebase to do it, a move that could complicate any public release of the resulting model given the sensitivity of that source material.

The competitive math is stark. Google CFO Anat Ashkenazi has noted that Anthropic writes roughly 100% of its code with AI assistance, versus about 50% at Google — a gap that is both a symptom of the model quality problem and, increasingly, a driver of it. The company whose engineers ship almost entirely through AI compounds its advantage with every release. Meanwhile, Google’s frontier models, Gemini 3.5 Flash and Gemini 3.1 Pro, have slipped outside the top five on several public leaderboards, trailing not only Anthropic and OpenAI but Chinese labs such as Zhipu AI and MiniMax.

## A talent exodus that keeps compounding

The reorganization is unfolding against a backdrop of departures that would rattle any lab. Since February, Google has lost six named researchers: Denny Zhou, who founded Google Brain’s reasoning team, left for Meta; Noam Shazeer, co-author of the foundational "Attention Is All You Need" paper and a Gemini co-lead, announced his move to OpenAI on June 18; Nobel laureate John Jumper, of AlphaFold fame, said he was joining Anthropic on June 20; and senior Gemini contributors Jonas Adler and Alexander Pritzel both departed for Anthropic on June 24. A sixth researcher left for a startup.

The market noticed. Alphabet shares fell more than 5% on June 22 as the Shazeer and Jumper news landed within 48 hours of each other. As Fortune’s Jeremy Kahn put it, "That giant sucking sound you hear? That’s the woosh of talent streaming out of Google DeepMind and flowing to OpenAI and Anthropic. There was a time when I can remember DeepMind bragging about how no one ever left the storied AI lab. That’s certainly not the case anymore."

Money is the obvious lure — Anthropic and OpenAI are both approaching IPOs, and pre-IPO equity at a company valued in the hundreds of billions can dwarf even a senior Googler’s vested stock. But Axios and Fortune both report a subtler pull: researchers want to be at the lab they believe will reach AGI first, and several who left had grown frustrated with a culture insiders describe as bureaucratic and risk-averse. Shazeer, notably, made the same critique when he first left Google years ago.

## What to watch

Google’s pivot to midtraining is a genuine engineering bet that its coding gap is structural, not cosmetic — and rebuilding a training pipeline mid-race is not the move of a lab that thinks a quick patch will do. The near-term tell will be whether Gemini 3.5 Pro, targeted for a June general-availability window, shows measurable gains on agentic coding benchmarks, and whether Google can ship a coding-tuned model at all given the proprietary-codebase entanglement. The longer-term question is retention: a strike team is only as good as the researchers running it, and Borgeaud’s group is trying to close a gap while the people best equipped to close it keep walking out the door. If the next Anthropic recruiting announcement carries a Strike Team name, the sprint may be lost before the finish line.

---

**Sources:**
- [The Information](https://www.theinformation.com/articles/google-revamps-new-ai-coding-strike-team-amid-struggle-catch-anthropic)
- [Neowin](https://www.neowin.net/news/google-reshuffles-its-ai-coding-team-as-it-struggles-to-catch-anthropic/)
- [TechTimes](https://www.techtimes.com/articles/319219/20260628/google-deepminds-coding-pivot-lost-six-researchers-meta-openai-anthropic.htm)
- [Fortune](https://fortune.com/2026/06/23/google-deepmind-ai-researcher-departures-raise-doubts-about-ability-to-win-the-ai-race-shazeer-jumper-eye-on-ai/)
- [Axios](https://www.axios.com/2026/06/23/ai-lab-agi-google-deepmind-departures)