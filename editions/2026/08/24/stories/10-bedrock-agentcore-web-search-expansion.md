Grounding an AI agent in the live web now has a sticker price: $7 per 1,000 queries. On August 19, AWS expanded Web Search on **Amazon Bedrock AgentCore** to Europe (Ireland) and Asia Pacific (Tokyo), joining US East (N. Virginia), and shipped per-call domain and published-date filters alongside it. The features are unglamorous — an include list, an exclude list, two ISO-8601 timestamps. The economics are not. Two months after AWS put a meter on retrieval, the industry has a rate card for a capability most agent teams still budget as a rounding error.

## What actually shipped

The August release is connector version 1.2.0 of the Web Search tool, which runs as a built-in MCP target on AgentCore Gateway. Two new objects appear in the input schema: `filters.domainFilter` takes `include` and `exclude` lists — up to 100 domains each, counted independently — and `filters.publishedDateFilter` takes inclusive `from` and `to` bounds in UTC. Both are optional, enforced server-side, and backward compatible with 1.1.0 targets already in production.

The interesting design choice is the merge logic. AWS layers admin policy under runtime policy so a caller can narrow the search space but never widen it. Include lists combine by intersection; exclude lists by union. As AWS's engineering team put it: **"A runtime caller can't search a domain the admin hasn't allowed and can't unblock a domain the admin has denied."** If the admin allows `[a.com, b.com, c.com]` and the agent asks for `[b.com, c.com, d.com]`, `d.com` is silently dropped. With filters on, the tool prefers precision over recall — results without a recognizable domain or parseable publication date are excluded outright, so you get fewer hits but every hit is verifiable.

That is not a search feature. It is an audit feature, and AWS's examples say so plainly: a pharma agent restricted to `fda.gov`, `nih.gov` and `clinicaltrials.gov`; a trading desk confined to the past seven days; a SaaS platform applying 200 tenant source policies through one gateway target. AWS is explicit that telling the model to filter via system prompt "isn't hard enforcement" — only the `tools/call` payload is.

## Do the arithmetic

$7 per 1,000 queries is $0.007 a search. That sounds like nothing until you remember agents don't search once. A research agent that decomposes a question into four searches spends $0.028 per task before a token of inference. Run 100,000 tasks a month at 3.5 searches each and you are at 350,000 queries — roughly $2,450 in grounding alone, plus Gateway's separate `InvokeTool` meter at $5 per million.

AWS publishes its own worked example: 200,000 research queries a month costs $1,403.00 — $1,400 of search plus $3.00 of Gateway calls. That second meter is the tell. Web Search isn't a standalone endpoint but a connector target, so the bill arrives in two places, and egress from Gateway to a customer VPC adds $0.006 per GB in commercial regions.

Against the field, $7 is aggressive but not the floor. As of early August: Brave Search API at $5.00 per 1,000 requests, Exa at $7 (with a per-result overage above 10 results that can double a bill), Anthropic's web search tool at $10 per 1,000 searches plus the input tokens the results consume, Grounding with Bing at $14 per 1,000 transactions, and Grounding with Google Search at $14 per 1,000 queries on Gemini 3 — but $35 per 1,000 grounded prompts on Gemini 2.5, a rate teams inherit by default without changing a line of code. On the same 200,000-query workload, that spread runs from $1,000 to $5,425.

## The thing that actually closes the deal

Nobody claimed better results. Both named customers in AWS's June GA post talked about custody, not relevance. Iskander Sanchez-Rola, Senior Director of AI & Innovation at Gen Digital: **"What we value most is that AWS uses its own search index and keep queries within our trusted AWS environment."** Nicholas Larus-Stone, Head of AI Agents at Benchling, framed it the same way: **"Because we're using the Web Search tool on Amazon Bedrock AgentCore, customers have a secure, governed environment to bring that high quality published data into their workflows without compromising how they manage their data."**

That is the pitch. AgentCore's zero-egress architecture means the query never leaves AWS — no third-party vendor sees the string your planner generated. Compare Microsoft's documentation for Grounding with Bing, which states that "your data flows outside the Azure compliance and Geo boundary" and that the Data Protection Addendum does not apply. For a healthcare or banking agent whose queries derive from account context, the query string *is* the sensitive payload. Ireland and Tokyo close the last gap: EU and APAC customers no longer route grounding traffic across the Atlantic to get it.

## Who loses

Independent search API vendors. Brave, Exa and Tavily built businesses on being the retrieval layer hyperscalers didn't offer. Now the largest AI platforms bundle grounding into the agent runtime, priced at or below the independents' self-serve rates, with IAM-native auth and no new vendor to push through procurement. Worse: zero data retention — the one feature that would neutralize AWS's custody argument — is an Enterprise-plan item at both Brave and Exa, meaning the $5 and $7 headline rates aren't what a regulated buyer would actually pay. As eCorpIT's Manu Shukla put it in an August cost analysis: **"In a market where six vendors return broadly similar snippets, the differentiator being marketed is custody of the query."**

The counter-argument is lock-in. Web Search only works through AgentCore Gateway, so adopting it is an architectural commitment, not an endpoint swap — the same trap Microsoft sprung when it retired the standalone Bing Search APIs in 2025.

## What to Watch

Three things. Whether AWS moves off flat pricing — every metered utility eventually grows volume tiers, and $7 is a launch number. Whether the billing unit shifts: AWS bills a query today, but Google bills each individual search a model decides to issue, and a verbose planner is a budget decision nobody is modeling. And the region roadmap — Ireland and Tokyo are the obvious residency wins; Frankfurt, London, Sydney and Mumbai will tell you whether AWS thinks grounding is a compliance product or just another API.
