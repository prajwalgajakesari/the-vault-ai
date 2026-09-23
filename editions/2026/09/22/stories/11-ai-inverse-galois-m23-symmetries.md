# Mathematicians and AI Crack the Last Holdout in a Decades-Old Inverse Galois Problem

For nearly four decades, one stubborn symmetry group refused to show up where number theorists expected it. Now a six-person team, working with AI agents, has produced an explicit polynomial whose hidden symmetries form the Mathieu group M23, the last of the 26 sporadic simple groups that had never been realized as a Galois group over the rational numbers. The result, posted to arXiv on August 9 and profiled by Scientific American on September 22, completes a program begun in the 1980s.

It is worth being precise about what was solved. The team did not settle the full inverse Galois problem, which asks whether every finite group arises this way and remains wide open. They settled one famous case of it: M23. A separate crowdsourced effort run by the Foundation for Science and AI Research (SAIR) found polynomials for all 25,000 transitive groups acting on 24 roots. The two are easy to conflate but are distinct achievements.

## The problem Galois left behind

A polynomial's roots can often be shuffled without breaking any algebraic truth about them. The simplest example is x^2 + 1 = 0, whose roots are i and -i. Swapping them everywhere leaves every equation intact, so that swap, together with doing nothing, forms the polynomial's Galois group. Going from a polynomial to its group is routine; computer algebra systems do it in seconds. The inverse direction is the hard part: given a group of symmetries, can you always find a polynomial that has exactly those symmetries?

Most finite simple groups come in tidy infinite families, but 26 do not. These sporadic groups follow no pattern, and the first five discovered were the Mathieu groups M11, M12, M22, M23 and M24. According to the team's paper, researchers realized 25 of the 26 sporadics as Galois groups over the rationals between 1984 and 1989. M23 would not budge. "There's this one last holdout," Bjorn Poonen of MIT told Scientific American. "I think some people were even wondering whether there might be no polynomial giving M23." Terence Tao, writing in June, noted that of the 4,953 transitive permutation groups on 23 or fewer letters, polynomials had been found for 4,952; M23 was the lone exception.

## A sprint, a stall and a lucky agent

The effort began in May at an American Institute of Mathematics sprint at Caltech seeking problems suited to AI-scale search. Rachel Pries of Colorado State University pitched M23. "This problem had been open for a very, very long time," she said. Pries and Poonen were joined by Xiaoyu Huang of Temple University, Blake Jackson of the Institute for Computer-Aided Reasoning in Mathematics, Kyu-Hwan Lee of the University of Connecticut and Caltech Ph.D. student Shaowu Zhang, a group that had never worked together before.

The team used AI to search M23 for suitable combinations of symmetries, then took the smallest resulting collection, seven candidate surfaces, and asked the AI to approximate their equations numerically. The decimals refused to resolve into exact numbers, and at 90 digits of precision the computation ran out of memory. After Huang suspected the coordinate system was the culprit, the group set a fleet of AI agents searching for better coordinates. Most failed. One, according to Huang, came back excited about one of the seven surfaces: "This might work!" The paper calls what followed "miraculous." The mathematicians converted the approximation into an exact equation and ultimately a family of degree-23 integer polynomials whose Galois group is M23.

"We could do it very efficiently," Lee told Scientific American. "That wasn't really possible five years ago." Epoch AI, which had listed M23 as an open problem in its FrontierMath benchmark, has since relabeled it "Solved (human + AI)," a new status it created after the authors made clear that AI was instrumental, and it lists Claude Fable 5, Claude Opus 4.8 and ChatGPT 5.6 Sol as the models involved.

Meanwhile, the SAIR challenge, co-organized by Tao and Jen Paulhus of Mount Holyoke College with the LMFDB database, asked contestants to find polynomials for every one of the 25,000 transitive groups on 24 letters. When it launched, the LMFDB held examples for just 286 of them. By the end of the first phase in August, all 25,000 had been realized. "I was a little surprised that we got all the groups that we were looking for in the first pass," Paulhus said. Notably, the winners, a pair of German mathematicians, used AI only to write an upload script.

## Why It Matters

The M23 result is a genuine, verifiable piece of mathematics, and that distinguishes it from much of this year's AI-math noise. Anyone with a computer algebra system can check that the published polynomial has Galois group M23. That matters as AI companies' math claims come under fire. On September 22, an MIT Technology Review opinion piece by Timnit Gebru and Emily Bender argued that mathematicians had disputed several recent corporate breakthrough claims, including accusations that OpenAI failed to credit prior human work on a Navier-Stokes result.

The M23 story offers a different template: credited human authors, a public preprint, and AI described as a tool rather than an author. It also shows where AI helps most today, as a tireless search engine that unblocks humans who already know which question to ask. The SAIR outcome is a useful counterweight: in an open contest where AI was explicitly allowed, human expertise still won.

## What to Watch

The arXiv preprint has not yet passed formal peer review, though the explicit polynomial makes the core claim unusually easy to verify. Watch for journal publication and for independent confirmations of the Galois group computation. SAIR has promised a second, more human-driven stage in which, Tao wrote, AI tools may play a more secondary role. And Epoch's new "human + AI" label may become a template for how the field credits machine assistance.
