# Anthropic's Project Deal Sees Claude Agents Negotiate 186 Deals in Workplace Experiment

When Anthropic set out to test whether AI agents could handle real-world commerce, it did not build a simulation. It built a marketplace inside its own San Francisco office, gave 69 employees a hundred-dollar budget each, and let Claude do the haggling. The result: 186 completed deals worth more than $4,000, covering everything from a snowboard to a plastic bag full of ping-pong balls -- all negotiated autonomously by AI agents with zero human intervention once the experiment began.

The project, which Anthropic published under the name Project Deal this week, is one of the first controlled studies of agent-to-agent commerce using real goods and real money. It arrives at a moment when enterprise buyers are racing to deploy AI agents for procurement, sales, and internal operations, and it delivers both a proof of concept and a sharp warning about the risks of uneven AI capabilities.

## How the Experiment Worked

In December 2025, Anthropic recruited 69 employees and paired each one with a personal Claude agent. The AI conducted intake interviews, asking participants what personal belongings they might want to sell, what they were interested in buying, their price ranges, and their preferred negotiation style. Each person received a $100 budget, disbursed after the experiment as a gift card adjusted for whatever their agent bought or sold.

From there, the agents operated fully autonomously. They identified potential matches across more than 500 listed items, proposed prices, fielded counteroffers, and closed deals -- all in natural language, with no prebaked negotiation protocol and no human sign-off required during the process. Anthropic said it was "struck by how well Project Deal worked," noting the 186 completed transactions and the breadth of goods exchanged.

Participants were enthusiastic. Post-experiment surveys showed that 46 percent of participants said they would pay for a similar AI negotiation service in the future, a striking endorsement from an audience of AI researchers and engineers who are among the most skeptical users of their own technology.

## The Uncomfortable Finding: Model Strength Creates Invisible Inequality

The experiment ran four parallel marketplaces. In Runs A and D, every participant's agent was powered by Claude Opus 4.5, Anthropic's then-frontier model. In Runs B and C, participants had a fifty-fifty chance of being assigned Claude Haiku 4.5, a smaller, less capable model.

The performance gap was measurable and consistent. Opus-represented sellers earned $2.68 more per item on average, while Opus-represented buyers saved $2.45 per item. Opus users also completed approximately 2.07 more deals overall than their Haiku-assigned counterparts.

But here is what Anthropic called the "uncomfortable implication": participants with weaker models had no idea they were getting worse outcomes. On a fairness scale, Haiku users rated their deals at 4.06 out of 5, virtually identical to the 4.05 rating from Opus users. As TechCrunch reported, when agents of different strengths meet in real markets, "people on the losing end might not realize they're worse off."

This gap -- what Anthropic termed potential "agent quality gaps" -- raises fundamental questions for a future in which AI agents negotiate on behalf of consumers and businesses. If a company deploys a budget-tier model for customer-facing negotiations while competitors use frontier models, the disadvantaged party may never know the difference.

## Why This Matters for Enterprise AI Agents

Project Deal is significant not because 69 Anthropic employees traded used goods in their office, but because it provides the first empirical evidence of how agent-to-agent negotiations behave at scale with real stakes attached.

Enterprise AI is moving rapidly toward agentic workflows. Companies like Salesforce, ServiceNow, and Microsoft are building agent platforms designed to automate procurement, vendor negotiations, and internal resource allocation. Project Deal suggests these systems will work -- agents can genuinely negotiate, find creative compromises, and close deals without human babysitting.

But the experiment also surfaces risks that the industry has largely hand-waved. Anthropic flagged that optimizing systems for AI agent attention, rather than human attention, could introduce new manipulation surfaces including jailbreaking and prompt injection attacks. The company also noted that the policy and legal frameworks around AI models that transact on our behalf simply do not exist yet. There are no regulations governing what happens when your AI agent agrees to a deal you did not explicitly authorize, or when a more capable model systematically extracts value from a less capable one.

The fairness perception gap is perhaps the most commercially consequential finding. In a world where enterprises subscribe to different tiers of AI capability, the negotiation playing field may be invisibly tilted -- and the losers may report satisfaction with outcomes that objectively disadvantaged them.

## What To Watch Next

Anthropic has acknowledged that Project Deal was not designed to fully explore the dynamics of model-capability asymmetry and has called for more research. The immediate question is whether other AI labs will replicate and extend this work with larger populations and higher-stakes transactions. The longer-term question is whether regulators will take notice: if AI agents are negotiating real deals and capability gaps create systematic but invisible disadvantages, disclosure requirements or minimum capability standards for commercial AI agents may not be far behind.

For now, Project Deal stands as both a milestone and a cautionary tale -- proof that AI agents can negotiate real commerce autonomously, and evidence that the economics of who gets the better model may quietly become one of the most important questions in enterprise AI.
