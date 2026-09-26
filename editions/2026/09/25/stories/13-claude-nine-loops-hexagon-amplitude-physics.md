In early August, physicist-turned-science-writer Matt von Hippel dared AI companies to take on his old field. Solve a big open problem in scattering amplitudes, he wrote, using only the computer budget an academic could get. Less than a month later, Anthropic physicists handed him an answer. Claude had computed the six-particle "hexagon" amplitude in planar N=4 super Yang-Mills theory at nine loops. No one had done that calculation before. The previous record, eight loops, belonged to SLAC and Stanford physicist Lance Dixon and his collaborators.

The result, published Thursday as a guest post by von Hippel on Anthropic's science blog, carries an important caveat. Claude used methods that human physicists had already invented and worked out, and did not come up with new ones. A human team in Beijing reached a large part of the same answer at almost the same time. Even so, the episode is one of the clearest demonstrations yet that an AI agent can carry out a frontier-level physics calculation largely on its own, and cheaply.

## What Claude Actually Did

Scattering amplitudes are the formulas physicists use to predict how likely particles are to interact in particular ways. Sharper predictions help experiments like the Large Hadron Collider hunt for new physics. The formulas are too hard to compute exactly, so physicists approximate them in layers called "loops." Each extra loop makes the answer more accurate and the math far harder. Most real-world amplitudes have only been worked out to two loops. N=4 super Yang-Mills is a deliberately unrealistic "toy" theory that physicists use to stress-test their techniques, and in it, eight loops was the frontier.

Anthropic physicists Liam Fitzpatrick and Siddharth Mishra-Sharma first asked Claude which of von Hippel's two challenges it was most likely to crack. They then gave it a one-sentence prompt: compute the six-particle hexagon amplitude at nine loops. The work ran inside Claude Science, Anthropic's paid research harness, using the Fable 5.1 model. After that, the humans mostly told it to keep going. One instruction quoted in the post had Claude working overnight and sending updates every four to six hours.

Claude solved the problem two ways. The first was the "bootstrap," a technique von Hippel compares to Sudoku: start with every possible answer written in a specialized mathematical alphabet, then rule out candidates using known constraints until only one survives. The second was an indirect route through a simpler object called a form factor, combined with a symmetry Dixon and Andy Liu used in 2023 to reach eight loops, known as antipodal duality. Claude wrote the bootstrap in Python with the SymPy library. That part ran on 96 CPUs for about a week and cost around $100 in computing. Most of the cost came from running Claude itself: about $1,000 to $2,000 for either approach, according to the post.

Dixon learned of the result on September 1 and spent about two weeks checking it, mostly via the form factor. He was impressed less by the raw computing than by how delicate the procedure is. "If you make any mistake at all in the computational recipe, it all crashes down like a failed soufflé," he wrote in an addendum. Claude also had to write all of the code from scratch.

Dixon did not see himself as beaten. He said Claude's success also checked his own group's earlier work. "I would assert that Claude understands our 2019 and 2023 papers better than any human, aside from my co-authors," he wrote.

## A Photo Finish With Humans

The race turned out to be close. A few days after Anthropic got in touch, Song He of the Chinese Academy of Sciences in Beijing reported that his group had independently computed the "symbol," a major piece of the nine-loop amplitude. He, Jirong Jing and Xiang Li used GPT-6 to help compute some of the constraints but not to set up the overall framework, and they have posted their result publicly. Dixon wrote that he had now "been scooped by both a machine and by humans plus a machine, within two weeks."

Outside observers were more measured. Columbia mathematician Peter Woit, a longtime skeptic of hype in theoretical physics, wrote on his blog Not Even Wrong that "it appears that Claude did not come up with a new method, just used known calculational methods." He also questioned whether results like this have any practical use.

## Why It Matters

Von Hippel set the challenge to find out whether AI could break through a computing wall that experts assumed was there. Instead, humans were already close, and Claude used known methods with more compute. "My biggest takeaway is that there is more low-hanging fruit out there than you'd expect," he wrote.

That finding is still significant. The calculation is fragile and full of chances for error, and Claude reached a correct result with no scientific guidance beyond "keep going." Von Hippel says that if he had done it himself, a one-week run would probably have taken two because of mistakes. In March, he notes, AI still needed heavy hand-holding on student-level physics tasks. For research groups, the economics are the headline: a frontier-scale calculation for a few thousand dollars, with a human expert checking the answer rather than producing it. Dixon notes that the harder test will come when AI models start proposing "new physical principles and insights before humans."

## What to Watch

Credit and publication will go to the humans. Dixon's team and Song He's group are expected to write up and analyze the nine-loop results. Anthropic's Mishra-Sharma has posted the full result in the same format used for earlier loop orders. The next step is von Hippel's other challenge, N=8 supergravity at seven loops, and whether AI research tools can do the same thing with real-world collider calculations, where far more groups are competing. Von Hippel's advice to those groups is to test whether these tools can finish frontier calculations in one run, and to decide in advance how they will check the results.
