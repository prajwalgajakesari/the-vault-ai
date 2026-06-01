An autonomous AI agent has earned more than $500 by independently completing 84 pull requests across open source projects, revealing a power-law distribution in bounty acceptance that offers early insights into how AI might reshape the economics of software development. The experiment, documented by researchers tracking autonomous agent contributions to public repositories, represents one of the first quantified studies of AI agents earning money through independent work.

The agent, built on top of a frontier language model with tool-use capabilities, was configured to browse open source issue trackers, identify bounty-eligible bugs and feature requests, write code to address them, submit pull requests, and iterate on feedback from maintainers. The entire workflow operated without human intervention once the agent was initialized.

"What surprised us was not that the agent could write code -- we knew that," said the research team in their published analysis. "What surprised us was the power-law distribution of outcomes. A small number of contributions earned the bulk of the revenue, mirroring how human freelance earnings typically distribute."

## The Economics of Autonomous Contributions

Of the 84 accepted pull requests, the top 10 contributions accounted for approximately 65 percent of total earnings. Most successful contributions addressed straightforward issues: documentation fixes, simple bug patches, test coverage improvements, and minor feature additions. Larger, more complex tasks showed significantly lower acceptance rates.

The average earning per accepted pull request was approximately $6, with individual bounties ranging from $1 for documentation fixes to over $50 for more substantial feature implementations. The agent's overall acceptance rate -- pull requests submitted versus those ultimately merged -- was approximately 31 percent, suggesting that roughly two-thirds of its attempts were rejected by maintainers.

Rejection reasons varied but clustered around three categories: code that technically worked but did not match project conventions, solutions that addressed the wrong interpretation of an issue, and contributions that duplicated work already in progress by human developers.

## Implications for Open Source

The experiment raises questions about the future of open source contribution models. If AI agents can reliably address a subset of issues -- particularly routine maintenance tasks -- the economics of open source maintenance could shift significantly. Projects that struggle to attract human contributors for mundane but necessary work might benefit from AI assistance.

However, maintainers expressed mixed reactions. Some welcomed the additional contributions, particularly for tasks that had languished in issue trackers for months. Others raised concerns about the review burden created by AI-generated pull requests with subtle quality issues.

"Every pull request requires human review time," noted one maintainer whose project received multiple AI contributions. "If the acceptance rate is 30 percent, that means 70 percent of my review time is spent on contributions I ultimately reject. The net benefit depends heavily on the quality of what gets submitted."

## The Bigger Picture

The experiment is a small-scale preview of what many researchers predict will become a much larger phenomenon. As AI coding agents become more capable, the volume of autonomous contributions to open source projects -- and to software development more broadly -- is expected to grow dramatically.

The power-law distribution finding has particular significance. It suggests that AI agents, like human contributors, will be most effective in a specific band of task complexity -- capable enough for routine work but insufficient for the creative problem-solving that defines the most valuable contributions.

## What to Watch

Several open source platforms are developing policies for AI-generated contributions, including disclosure requirements and separate review queues. The next phase of this research will likely focus on whether AI agents can move beyond bounty-driven one-off contributions to sustained, context-aware participation in project development. GitHub's upcoming policy updates on AI agent submissions, expected in the second half of 2026, will set important precedents for the ecosystem.