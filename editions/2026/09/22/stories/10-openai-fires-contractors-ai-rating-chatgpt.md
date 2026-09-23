# OpenAI Fires Contractors Caught Using AI to Rate ChatGPT's Answers

The humans OpenAI pays to keep ChatGPT honest have been quietly handing the job back to the machines, and some of them have lost their jobs for it. Multiple contractors hired to read, rate and critique ChatGPT's responses have been fired or offboarded after reviewers caught them using AI tools to do the work, according to an investigation published September 22 by 404 Media.

The report, by journalist Joseph Cox, draws on internal documents and interviews with three contractors working across OpenAI training projects, two of them through Mercor, the AI-training labor platform that supplies expert reviewers to frontier labs. One internal document says those projects can include more than ten thousand contractors. The irony is hard to miss: a company whose business depends on convincing workers to use AI is now enforcing a strict no-AI rule on the people shaping its flagship model.

"Do not use AI detection tools, or AI yourself," reads one internal document written for contractors who review the work of other contractors. "Do not use GPTZero or any other AI detection tool. They are not reliable. Reviewers may not use AI either, including Grammarly and AI translation, to review, write feedback, or write comments."

Instead of software, reviewers are told to rely on pattern recognition. The tell-tale signs include repetitive wording, AI-style punctuation such as an overzealous use of the em dash, and submissions completed suspiciously fast. The guidance also instructs reviewers to keep their methods secret. "Do not tell evaluators why you suspect AI. It is easier for them to hide if they know what you look for. Judge the overall pattern, not one clue," the document says.

The practice appears to be widespread. One contractor told 404 Media that colleagues use AI "all the time and people are let go for it all the time, it's pretty much the one thing that will get you kicked off ASAP." In internal Slack channels, workers routinely post samples asking whether a piece of feedback was machine-written. "Usually the answer is yes," the contractor said.

Another contractor shared what they described as their termination letter, which cited issues with the "authenticity" of their work. "I'm not a bad person or worker. I just needed a little boost and turned to AI to help me which eventually led to my downfall," they told 404 Media, adding that they felt no joy in the work.

Mercor confirmed its policy in a statement. "Our contracts strictly prohibit the use of LLMs to complete projects and we enforce that," a Mercor spokesperson said. "When we confirm an expert has used AI to complete a task, we immediately remove them from the project." OpenAI declined to comment.

The story follows 404 Media's reporting last week on Project Lily, in which hundreds of OpenAI contractors read real ChatGPT users' prompts and conversations, which can include personal information, and grade the chatbot's replies, including checking that responses are not overly sycophantic and do not anthropomorphize ChatGPT. A fourth contractor, who has worked across several AI companies, told 404 Media they sometimes chose the worst outputs deliberately to sabotage training, saying it can feel like being paid to make AI worse.

## Why It Matters

Human feedback is the ingredient that turns a raw language model into a usable assistant. Reinforcement learning from human feedback depends on the assumption that the preferences being recorded are actually human. When a rater pastes a response into another chatbot and submits its verdict, the model ends up learning from its own reflection, and any quirks or blind spots in the helper model get baked in as if they were human judgment.

That loop is the mechanism behind model collapse. A 2024 study published in Nature found that "indiscriminate use of model-generated content in training causes irreversible defects in the resulting models." OpenAI does use synthetic data deliberately and under controlled conditions, as Tom's Guide noted, but a rater secretly swapping in a chatbot is a different problem: uncontrolled, unlabeled contamination in exactly the data meant to anchor the model to human taste. There is no public evidence the contamination measurably degraded ChatGPT, but the scale matters. With projects spanning more than ten thousand workers, even a small share of AI-assisted ratings could add up.

The timing also shows how valuable authentic human judgment has become. On the same day the 404 Media report ran, Snorkel AI raised $350 million at a $3.5 billion valuation, with its annualized revenue run-rate climbing past $350 million from roughly $20 million a year earlier, according to TechCrunch and Reuters. Micro1 raised more than $100 million at a $4 billion valuation, per Forbes, on annual recurring revenue above $500 million. Investors are pricing expert human data as a scarce commodity. The OpenAI firings show how easily that commodity can be quietly diluted.

There is a detection problem too. OpenAI's own guidance concedes that AI detectors like GPTZero are unreliable, leaving enforcement to human reviewers hunting for em dashes and fast turnaround times. Those heuristics risk false positives against careful writers, and as contractors learn the rules, the signals get easier to hide.

## What to Watch

Expect data vendors to tighten verification, with more keystroke logging, timed and proctored tasks, and screen monitoring, which will raise costs and privacy questions for a workforce that is already poorly protected. Watch whether OpenAI or Mercor disclose how many workers were removed and whether affected training runs were audited or rolled back. And watch the pay question: contractors describing joyless, repetitive work are the people labs now rely on to keep models grounded. As Snorkel, Micro1 and Mercor compete for expert raters, whether they pay enough to make honest human work worth doing may matter as much as any detection tool.
