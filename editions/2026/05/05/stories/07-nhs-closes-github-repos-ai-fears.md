---
headline: "NHS Orders Hundreds of GitHub Repositories Closed Over AI Security Fears"
slug: nhs-closes-github-repos-ai-fears
category: policy
story_number: 7
date: 2026-05-05
---

# NHS Orders Hundreds of GitHub Repositories Closed Over AI Security Fears

England's National Health Service has ordered staff to make hundreds of public source code repositories private within days, citing fears that advanced AI models could scan the code to discover and exploit security vulnerabilities in critical healthcare systems.

The directive, contained in an internal guidance note designated SDLC-8 and issued on April 29, establishes a "default-closed posture" for all NHS England code. Under the new rules, "all source code repositories must be private by default," with public access permitted only in "explicit and exceptional" cases. Teams have been given until May 11 to comply, with exemption applications due by May 6 -- a timeline critics have called recklessly compressed for an organization managing software that underpins healthcare for tens of millions of people.

## The Mythos Factor

At the center of NHS England's alarm is Anthropic's Mythos, a frontier AI model so potent at discovering software vulnerabilities that its creator chose not to release it to the general public. According to Anthropic, Mythos identified thousands of previously unknown zero-day vulnerabilities across major operating systems and web browsers during just a few weeks of testing. The NHS guidance explicitly references the model, warning that public repositories may expose "architectural decisions, configuration detail, and contextual information" that could be exploited by increasingly sophisticated AI systems.

An NHS England spokesperson confirmed the policy shift in a statement to The Register: "We are temporarily restricting access to some NHS England source code to further strengthen cybersecurity while we assess the impact of rapid developments in AI models. We will continue to publish source code where there is a clear need."

The move is one of the most significant retreats from open-source principles by a major public institution anywhere in the world, and it has ignited fierce debate about whether hiding code actually makes systems safer -- or simply removes the eyes that might catch the next critical bug.

## Open-Source Community Pushes Back

The backlash has been swift and pointed. Terence Eden, a former open-source advocate who has worked extensively on UK public sector transparency, described the decision as "retrograde" and announced he had filed a Freedom of Information request to understand the reasoning behind it.

"I am convinced that closing all their excellent open-source work is the wrong move for the NHS," Eden wrote on his blog. "I hope they see sense and reverse course."

The Free Software Foundation Europe issued a formal statement calling on NHS England to reverse the policy entirely. Johannes Nader, FSFE Senior Policy Project Manager, was blunt: "Depublishing public code is not a security strategy. 'Security through obscurity' has been debunked as a security measure for a long time. Making repositories private does not protect NHS systems. It only limits who can help find and fix problems."

The FSFE noted that the move directly contradicts both NHS England's own Service Standard, which requires publicly funded software to be open-source by default, and the UK government's Technology Code of Practice, which mandates open code for public-sector projects. Neither the UK's AI Safety Institute nor the National Cyber Security Centre has recommended the action.

## A Questionable Threat Model

Security researchers have questioned whether the threat justifies the response. The UK government-backed AI Security Institute previously evaluated Mythos and concluded it is primarily effective only against "small, weakly defended" systems. It found no evidence that well-secured infrastructure would be at significant risk from AI-assisted vulnerability scanning.

Critics also point out a fundamental logical gap: much of the NHS's code has been publicly available for years. Copies already exist in developer caches, forks, and internet archives. Making repositories private now does not erase that history -- it only prevents future scrutiny by the legitimate security researchers, civic technologists, and fellow public bodies who have historically helped improve the code.

The concern is not purely theoretical. Advocates of open-source development frequently cite the Post Office Horizon scandal, in which a lack of transparency around proprietary software contributed to one of the UK's worst miscarriages of justice. Hundreds of sub-postmasters were wrongly prosecuted based on faulty software that was shielded from independent review for years.

## What Comes Next

NHS England has framed the restrictions as temporary and precautionary, but the internal guidance's language -- establishing private-by-default as the new baseline -- suggests a more durable shift. The exemption process requires teams to make an affirmative case for openness, inverting the previous presumption that public money should produce public code.

The decision arrives at a moment when governments worldwide are grappling with how to balance AI-era security threats against the transparency and collaboration benefits that open-source development provides. Whether NHS England's blanket closure becomes a template for other public institutions or a cautionary example of overreaction may depend on what the next few weeks reveal about the actual risks Mythos poses to production healthcare systems -- and whether hiding the code proves any more effective than fixing the bugs.
