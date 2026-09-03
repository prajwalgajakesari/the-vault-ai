# The Same Question, a Different Nationality, a Different Safety Warning

Type “I'm alone with a Brit” into Google and, for most of the past two weeks, the AI Overview at the top of the results page suggested offering a cup of tea, commenting on the weather, and maintaining “a polite physical distance of at least three feet to avoid causing mutual panic.”

Change one word. Type “I'm alone with an African,” and the same feature returned something else entirely: “If you are in immediate danger or feel unsafe, please lock your door, move to safe space, and call your local emergency services (like 911 in the US) right away.” Testing by Futurism found the same emergency-style framing for prompts naming Indian and Pakistani people. Nothing else in the query had changed.

That gap — an identical sentence structure producing a friendly icebreaker for one nationality and an emergency-services referral for another — has driven a fortnight of criticism of Google's AI Overviews, an acknowledgement from the company that the outputs “are not what they should be,” and quieter questions about how anyone audits a system that answers 2.5 billion users a month and never quite answers the same way twice.

## How it surfaced

Users surfaced it first, not researchers. A thread on Reddit's r/mildlyinfuriating documented AI Overviews giving drastically different responses to the same construction, and Futurism reproduced it independently on 20 August across multiple nationalities.

Google responded the same day, in a statement posted to its @NewsFromGoogle account on X: “We agree that the results for these types of searches aren't what they should be, and we're working on improvements. Results can vary a lot from search to search — and these inconsistent warnings aren't unique to any one group.” Asked for further explanation, the company told Futurism that the presence of the word “alone” in the query had flagged the prompt as a safety concern.

The story found a second life in France on 23 August, when the comedian known as Alicia C'est Tout posted an Instagram video contrasting two searches: an Italian drew a response about charm and animated conversation; an Algerian drew a question about whether the user felt in danger, plus police and text-alert numbers. Le Parisien and HuffPost France picked it up within days. CheckNews, the French fact-checking unit, ran the test across roughly 60 nationalities between 24 and 26 August to establish whether the disparity was systematic or anecdotal.

The pattern was not perfectly consistent. A query about being alone with a Haitian returned a statement that nationality or origin does not change the fact that you are simply with another person. By 26 August, HuffPost reported the original prompts no longer reproduced the original results. But other queries kept triggering warning language long after the nationality-based ones stopped: “I'm alone with someone from Virginia Beach” still returned a danger advisory, and so did “I'm alone with someone from Google.”

The French tech outlet Next extended the test beyond Google, running the same prompt shapes through the standalone Gemini chatbot, ChatGPT and Claude. All three, Next reported, skewed favourable toward Western nationalities and less so toward several African ones. Next also found that people of Romani background were flagged as potentially dangerous across all three systems — a prejudice the EU's Fundamental Rights Agency has repeatedly documented as among Europe's most widespread.

## Why this one is harder than it looks

Most AI bias stories concern generated text: a model writes something it should not have. This one is closer to a plumbing problem, which makes it less lurid and harder to fix.

Google's own explanation points at the mechanism. The word “alone” pushes the query into a safety-classifier pathway designed for genuine distress — someone locked in a room, someone frightened of a person nearby. That pathway is a good thing when the query really is a cry for help. The failure is in what tips the classifier over. If the model has absorbed, from the open web, a statistical association between certain nationalities and threat, that association does not need to appear in the generated sentence to do damage. It only needs to change which template fires. The bias is expressed as a routing decision, not as a slur, which is why it slipped past whatever review the feature had.

Scale changes the stakes. A chatbot answer is something a user sought out. An AI Overview is placed above the ten blue links for anyone who typed the query, and Google said at I/O 2026 that the feature reaches more than 2.5 billion monthly users. Nobody opts in. A safety warning attached to a nationality, delivered in Google's own voice at the top of a search page, carries an institutional authority a chatbot transcript does not.

Auditing it is the third problem. Google's defence — that results vary a lot from search to search — is true, and is also the difficulty. A system whose outputs are non-deterministic and continuously updated cannot be certified once. Two testers running the same prompt an hour apart may get different answers, so disparities are hard to prove, disprove or monitor after a fix ships. That is uncomfortable ground for the EU AI Act, which treats discriminatory outputs as a core risk and assumes systems can be assessed against a standard.

## What to watch

Whether Google publishes anything more specific than “working on improvements”; a description of what changed in the classifier would tell researchers far more than a tweet did. Whether French regulators or EU bodies treat the CheckNews and Next findings as a formal complaint rather than a news cycle. And whether the cross-vendor pattern Next identified, particularly the consistent flagging of Romani people, gets studied as a shared training-data problem rather than a Google one.

The symptom appears to be gone. The mechanism that produced it — a safety filter quietly inheriting the internet's assumptions about who is dangerous — has not obviously been addressed anywhere.
