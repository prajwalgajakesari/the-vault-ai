In 2023, "agent memory" meant pasting the chat log back into the prompt. In 2026 it is a leaderboard, with gaps wide enough to look like generational leaps. Mem0's April algorithm update claims 92.5 on LoCoMo. Letta's filesystem-based approach sits at 74.0. OpenAI's built-in memory is carried at 52.9. Forty points of daylight on the same test.

Those numbers deserve scrutiny, because over the same eighteen months a second literature emerged: papers whose entire contribution is showing that the memory benchmarks are broken. One found roughly a quarter of LoCoMo is unscorable by construction. Another found that harder questions collapse every system tested — including the leaders — to under 27 percent.

## What the leaderboard says

The field consolidated fast around three tests: LoCoMo (1,540 scored questions over ten long synthetic conversations), LongMemEval (500 questions, six categories), and BEAM, which pushes to 1M and 10M token scales.

Mem0's *State of AI Agent Memory 2026* report is the most-cited scoreboard, and its provenance matters. The headline figures — 92.5 on LoCoMo, 94.4 on LongMemEval, at roughly 6,956 tokens per retrieval call — are vendor-reported for an April 2026 algorithm that postdates the company's peer-reviewed ECAI 2025 paper. The report says so itself, instructing readers that the new numbers "should be attributed to Mem0's ongoing research... not to the 2025 paper itself."

The two gains everyone keeps circling — **+29.6 points on temporal queries and +23.1 on multi-hop** — belong to that same update, measured against Mem0's own previous algorithm. They are a self-comparison, not a head-to-head.

The published post also contains an unedited internal note. Beside OpenAI Memory's 52.9, the competitor table reads: "Figure carried over from Mem0's prior published benchmark content; confirm sourcing before publishing." That instruction shipped.

## Three architectures, three theories of memory

**Vector recall** — the incumbent — extracts facts, embeds them, and retrieves by cosine similarity. Mem0's 2026 revision hedges by fusing semantic similarity, BM25 keyword matching, and entity matching; notably, it *removed* external graph store support, trading a queryable graph interface for deployment simplicity.

**Graph memory** argues that similarity flattens structure. MAGMA, from Dongming Jiang, Yi Li, Guanpeng Li, and Bingzhe Li (ACL 2026 Main), puts it bluntly: existing approaches "largely rely on semantic similarity over monolithic memory stores, entangling temporal, causal, and entity information." MAGMA splits each memory item across four orthogonal graphs — semantic, temporal, causal, entity — and treats retrieval as policy-guided traversal.

**Event-centric memory** goes further. In *Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning* (Findings of ACL 2026), Yuyang Hu, Jiongnan Liu, Jiejun Tan, Yutao Zhu, and Zhicheng Dou of Renmin University segment experience into events and link them by explicit logical relations:

> "This decision process operationalizes our key insight that topology carries logic: relations constrain exploration paths and guide reasoning over structured dependencies, rather than flat and isolated text."

Their CompassMem numbers are modest and honestly reported: average LoCoMo F1 of 52.18 on GPT-4o-mini against HippoRAG's 47.92, with the real gain on temporal questions (57.96 versus Mem0's 48.93). On open-domain questions it *loses* to both. Set that four-point delta beside the forty-point spread on the vendor leaderboard, and something is wrong with one of them.

## The benchmark is the story

It is the vendor leaderboard. LoCoMo has been audited repeatedly, and it keeps failing.

The most damaging finding comes from Samuel Sameer Tanguturi of Kenotic Labs, whose ATANT v1.1 paper traces an empty-gold scoring bug in LoCoMo's reference implementation. Because 444 of 446 adversarial-category questions have empty gold answers, those items cannot be scored at all:

> "A system that refuses correctly is penalized identically to a system that hallucinates an answer."

That is ~23 percent of the corpus. Published LoCoMo "adversarial" rates, he concludes, "are not measurements of refusal behavior; they are measurements of a scoring function applied to a category it cannot score." Meanwhile, open issues on Mem0's own GitHub show practitioners unable to reproduce published scores locally.

The answer key is suspect too. The Mnemosyne team at Kaliber AI audited gold answers and found LoCoMo asserting a character's degree was in political science when the same session shows him holding a certificate in graphic design. Their verdict: "the answers given by LoCoMo can be very inaccurate and the benchmark is inherently flawed."

Then the ceiling problem. ConvoMem, from Salesforce AI Research (Egor Pakhomov, Erik Nijkamp, Caiming Xiong), notes that "simple filesystem operations achieved 74% accuracy on LoCoMo, matching or exceeding sophisticated memory systems," and finds that below 150 conversations, plain full-context prompting hits 70–82 percent while RAG-based systems including Mem0 manage 30–45. Sometimes the expensive memory layer is what's hurting you.

The cleanest demonstration is LoCoMo-Plus (Yifei Li et al., Xi'an Jiaotong University and Tencent), which rebuilds the questions to test implicit constraints rather than stated facts. Every system falls off a cliff: Gemini 2.5 Pro drops from 71.78 to 26.06, Mem0 from 57.24 to 15.80, A-Mem from 59.64 to 17.20. The paper's indictment is unambiguous — task-disclosed prompting and string-matching metrics "can be systematically misleading, even for factual memory, by conflating memory fidelity with prompt adaptation and generation style."

## "Memory" is five different things

Part of the confusion is definitional. The *Always-On Agents* survey (Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang, June 2026) coded 435 works and found the field measuring one slice of the problem. Persistent state, they argue, also includes "task ledgers, permissions, credentials, commitments, provenance and audit records, shared state, trigger conditions, and externally committed effects" — yet the literature "concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it."

No benchmark on the leaderboard scores forgetting, rollback, or provenance. LoCoMo asks whether an agent can recall a fact from session 12. It does not ask whether the agent should have stored it, whether it can delete it on request, or what happens when that fact goes stale — which Mem0's own report lists as an open problem.

## What to watch

Whether the LoCoMo scoring fix gets merged upstream; it had not been accepted as of ATANT's publication. Whether AOEP-v0, the Always-On survey's pilot protocol for scoring state mutation and recovery rather than answer quality, sees adoption. And most telling: whether any vendor publishes a LoCoMo-Plus number. The gap between 92.5 and 15.80 is the real state of agent memory in 2026, and only one of those figures appears in marketing.
