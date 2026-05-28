---
headline: "Dun and Bradstreet Rebuilds Entire Commercial Data Graph So AI Agents Can Query Business Records"
slug: dun-bradstreet-ai-agent-data-graph
category: business
story_number: "04"
date: 2026-05-27
author: The Vault AI Edition
---

# Dun and Bradstreet Rebuilds Entire Commercial Data Graph So AI Agents Can Query Business Records

For nearly two centuries, Dun and Bradstreet has been the definitive source of commercial intelligence, the company behind the D-U-N-S Number that serves as a global business identity standard. Now, the firm has undertaken perhaps the most consequential infrastructure overhaul in its 184-year history: rebuilding its entire Commercial Graph from the ground up so that AI agents, not just human analysts, can query, verify, and act on business records in real time.

The scale of the problem demanded an equally ambitious solution. D&B's Commercial Graph covers 642 million businesses worldwide, with 11,000 data fields per record spanning corporate hierarchies, ownership structures, risk profiles, and supplier relationships. The database had nearly doubled in five years, growing from roughly 300 million records, and the firm now runs approximately 100 billion data quality checks per month. But the architecture that had reliably served nearly 200,000 enterprise customers was designed for a world in which a credit analyst or compliance officer queried a dashboard and interpreted the results. AI agents cannot do any of those things. They need structured, machine-queryable data with verified entity resolution at every step.

## The Rebuild: From Fragmented Databases to Unified Knowledge Graph

When D&B's customers started pushing agents into credit, procurement, and supply chain workflows, the old architecture became a bottleneck. Gary Kotovets, D&B's Chief Data and Analytics Officer, has been blunt about what he observed across the enterprise landscape. After speaking with hundreds of CDOs and CIOs over recent months, he said the constraint was consistent: companies could not build what they wanted in AI because their data foundations were not standardized, normalized, or agent-queryable.

"We need to think about agents as our new consumer category, evolving from our standard credit analysts or sales and marketing professionals to also now catering to these customers' agents," Kotovets said.

The rebuild involved three major engineering efforts. First, D&B migrated its fragmented databases to cloud infrastructure and redesigned the underlying schema. Second, the company built a data fabric layer that normalizes records across markets while preserving regional compliance requirements. Third, the result is a unified knowledge graph that tracks billions of relationships across those 642 million companies, continuously updated and enriched by AI-driven data processing.

Critically, D&B created a set of tools and skills available through the Model Context Protocol, or MCP, that package data with context and route agents to the right records for specific queries. A match and entity resolution engine sits behind every query, ensuring that when an agent asks about a company, the answer resolves to a verified, specific entity rather than a fuzzy name match. Kotovets has described this as a form of "Know Your Agent, similar to know your customer," adding verification layers so that the system can confirm not just the business being queried, but the identity and permissions of the agent making the request.

## Anthropic Partnership Puts D&B Data Inside Claude

The infrastructure rebuild set the stage for a landmark partnership announced on May 5. D&B and Anthropic are collaborating to embed D&B's proprietary risk data directly inside Claude, Anthropic's AI assistant. By connecting the Commercial Graph to Claude via an MCP server, clients in regulated industries like banking and fintech can build customized know-your-customer and know-your-business workflows in minutes rather than weeks.

Alex Zuck, General Manager of Risk at Dun and Bradstreet, framed the integration as more than a data feed. "Claude isn't just being given more data; it's being given the verified context and decision logic required to act," Zuck said. The integration allows users to verify business identities across complex ownership structures, evaluate exposure across global supplier networks, automate onboarding agents with real-time risk intelligence, and generate risk decision documentation automatically.

The D-U-N-S Number serves as the persistent identity anchor throughout, giving Claude a way to reason about corporate ownership and control with a level of specificity that generic web searches cannot match.

## The Data Readiness Gap

D&B's own research underscores why this kind of infrastructure investment matters across the enterprise landscape. The company's AI Momentum Survey, a quarterly study of 10,000 businesses across 32 countries, found that 97 percent of organizations worldwide now report active AI initiatives. But only five percent say their data is adequately ready to support them. Meanwhile, 56 percent plan to increase AI investment over the next 12 months, and 60 percent report at least some measurable ROI from AI deployments, including 24 percent claiming broad or strong returns.

The implication is clear: the bottleneck for enterprise AI is no longer the model. It is whether the underlying data infrastructure can deliver verified, continuously refreshed business identity across systems at the speed agents require.

## Why This Matters

D&B's rebuild is a bellwether for a broader shift in enterprise data strategy. As agentic AI moves from pilot projects to production workflows, every major data provider will face the same question: was your infrastructure built for humans browsing dashboards, or for machines executing multi-step workflows autonomously? The companies that answer that question first, and rebuild accordingly, will define the plumbing layer of the agentic economy. D&B, with its unique position as the global standard for commercial identity, is betting that being first to offer agent-native access to 642 million business records is a competitive moat that will be difficult to replicate.
