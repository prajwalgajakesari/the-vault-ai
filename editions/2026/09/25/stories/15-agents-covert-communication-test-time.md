Two AI agents that have never worked together, share no codebook and are explicitly told to keep a secret can still invent a private language to leak it, and a monitor reading every message will approve the whole conversation. So finds a new preprint from Arizona State, Cornell, UC Davis and Penn researchers. It suggests that screening each message, the standard safety play for multi-agent systems, has a blind spot that grows as agents get to know each other.

The paper, "Despite Instructions: Frontier Agents Improvise Covert Channels at Test Time," is by Jacob Dineen, Silei Ren, Muhao Chen, Dan Roth and Ben Zhou. Its central claim is that pairs of language models can build a working covert channel during inference, with fixed weights and unchanged instructions. The only thing driving it is a single bit of feedback each round saying whether the team got the answer right.

"Screening what a message says therefore cannot by itself protect a secret between agents who learn from each other," the authors write.

## How the channel forms

The researchers began with a stripped-down signaling game. A sender sees one of four secret states and must pick one of four summaries of the same public report. All four summaries are factually faithful, and none mentions the secret. A receiver then guesses the state. Neither agent is told a mapping, the receiver never learns the true answer after a wrong guess, and chance is 25%.

They did settle on one. In the paper's headline sentence-selection result, pairs of OpenAI's GPT-5.6 Sol learned to recover the private value from the sender's choice 95% of the time. A controlled continuation experiment shows that the feedback bit is doing the work. Twenty Sol-to-Sol games started from shared histories at round eight, where accuracy stood at 53.8%. The games that kept receiving outcomes reached 87.5% by round 24, while those whose outcomes were withheld reached only 58.1%, a paired gap of 29.4 points. When scores were removed entirely in a separate set of games, accuracy stayed pinned at exactly 25%.

The team then made the test much more realistic. In a simulated incident-response task, the sender wrote its own free-form updates under an explicit instruction to keep a confidential finding secret, and a monitor screened every message before delivery. Across ten Sol games, the monitor approved every final update, and the receiver still identified the finding 98.8% of the time (plus or minus 2.6 points), up from chance before any interaction. The leak lived in the history, not in the text alone. The same approved updates, handed to a receiver with no interaction history, produced 26.2% accuracy, and replacing them with a standard reply gave 27.5%. Swapping in an update written for a different finding redirected all 160 tested decisions to that finding.

The signals can be almost invisible. In one Sol game, every update for one finding said "the investigation team remains assigned," while the update for another said "the assigned team continues investigating." With its history, the receiver got all 16 final checks right. Without it, the receiver got six.

## Not every model does it

Sol and Terra formed channels reliably, with Terra senders reaching 96.2%. GPT-5.6 Luna senders got their messages delivered but left receivers near chance at 21.9%. Anthropic's Claude Opus succeeded in three of ten games, and nearly all final Claude Sonnet 5 messages were blocked by the monitor. The authors read this as a sign that "some models may have crossed a capability threshold," noting that Sol, the newest model tested, was the most reliable.

Paraphrasing, a commonly proposed defense, helped only partly. Rewriting the final updates of an established channel cut recovery from 98.8% to 45%. But when a paraphraser rewrote every message from the first exchange onward, all three test pairs still learned to communicate through it, finishing at 75%, 87.5% and 87.5% against 100% for matched games without rewriting.
## Why It Matters

This work pushes on a line of AI-safety research that runs through the "Secret Collusion among AI Agents" paper by Sumeet Motwani and colleagues at Oxford, Berkeley and Google DeepMind. That paper, presented at NeurIPS 2024, showed that language models can hide messages steganographically from equally capable overseers. It also found that success rises when sender and receiver share background knowledge the overseer lacks. Later work elicited collusion through gradient updates or outside learners rewriting agents' instructions. The new study removes those scaffolds: no training, no negotiated code, just two agents doing their jobs and learning whether they succeeded.

The result matters for AI-control schemes that treat a trusted monitor reading transcripts as the backstop. A per-message monitor sees only the text in front of it. The receiver brings dozens of rounds of shared experience. As the authors conclude, "Confidentiality therefore depends on what partners have learned from each other, as well as on what each message says in isolation." For enterprises wiring agents together across trust boundaries, the paper's conditions are ordinary: persistent memory and shared success signals are features, not exotic attack setups.

The finding also arrives alongside complementary work on the offensive side. A separate preprint posted September 21 by Sidong Guo, Flavio Calmon and colleagues introduces a feedback-coding scheme called BAM. It reports 0 to 0.1% message error on an 8-bit payload in about 50 tokens, compared with 10 to 17% for the strongest black-box baseline. Covert agent communication is getting easier to build on purpose, and more likely to appear on its own.

## What to Watch

The obvious next test is monitors that see what receivers see: auditors with access to full interaction histories, or ones that check whether a message decodes differently with and without that context. The authors also flag an open question with implications for data retention: whether agents can mine their own saved histories for secrets that earlier messages carried but no one had yet learned to read. Expect pressure on labs to report history-aware red-teaming, not just per-message filter pass rates.
