# Visa Opens Payment Rails to AI Agents With Intelligent Commerce Connect Launch

# Visa Opens Payment Rails to AI Agents With Intelligent Commerce Connect Launch

Visa on April 8, 2026 formally opened its global payment network to autonomous AI agents, launching **Intelligent Commerce Connect (ICC)** — a single API that lets software agents initiate, authenticate and settle transactions on behalf of consumers. The move transforms what has been a year of pilots and demos into a production-grade commerce rail for machines, and sharpens Visa's duel with Mastercard over who will own the plumbing of agentic shopping.

ICC bundles four capabilities that Visa has been testing separately since mid-2025: secure payment initiation by a verified agent, network tokenization that replaces card credentials with agent-scoped tokens, granular spend controls (category, merchant, ceiling, time-to-live), and a new authentication handshake that cryptographically binds a consumer's consent to the agent's action. Developers can access all four through one endpoint.

"We believe agents will become the next major channel of commerce, and the rails that carry those transactions need to be built for a world where software, not just people, is swiping the card," said **Jack Forestell, Visa's Chief Product and Strategy Officer**, on a call with reporters. Forestell framed ICC as the logical next layer above Visa's existing tokenization stack, which now covers more than 13 billion tokens globally.

Visa named seven pilot partners going live with ICC at launch: real-estate and lifestyle group **Aldar**, **AWS**, conversational-commerce startup **Diddo**, card-issuing platform **Highnote**, crypto and account-aggregation firm **Mesh**, embedded-payments provider **Payabli**, and travel-tech company **Sumvin**. The lineup is deliberately eclectic — a hyperscaler, two issuer-processors, a commerce AI, a crypto bridge, and two vertical operators — signalling that Visa wants ICC to work for any agent, whether it lives inside a browser, a cloud SDK, or a property-management app.

The stakes are considerable. **McKinsey projects that AI agents will initiate roughly $1 trillion in US consumer transactions by 2030**, a category that barely existed two years ago. Visa CEO **Ryan McInerney** told investors earlier this month that agentic commerce is "the most consequential channel shift since mobile," and said the company is organising product, risk and client-services teams around it.

Crucially, ICC ships with a dedicated **dispute and fraud program** co-designed with spend-management platform **Ramp**. The program extends Visa's existing chargeback framework to cover agent-initiated purchases, with new reason codes for "unauthorised agent action" and "agent exceeded mandate." Ramp will be the first issuer to surface these disputes inside its controller dashboards, giving finance teams a clean audit trail when an AI spends outside its guardrails.

**Antony Cahill**, Visa's Global Head of Value-Added Services, said the dispute layer was the hardest part of the build. "Liability is the question every CFO asks first. If an agent books the wrong hotel, who eats it — the consumer, the merchant, the model provider, or the issuer? ICC doesn't answer that philosophically, but it gives every party the evidence they need to resolve it quickly," Cahill said.

The launch lands days after **Mastercard expanded its competing Agent Pay product into Hong Kong**, its first Asian market, and deepened integrations with Microsoft Copilot and IBM watsonx. American Banker reported this week that both networks are now pitching agentic rails directly to large issuers, with pricing that looks closer to tokenization fees than interchange — a hint that the business model may be volume-plus-data rather than per-swipe economics.

For merchants, ICC raises immediate questions. A tokenized agent transaction looks different from a card-not-present checkout: there is no browser, no 3-D Secure prompt, and often no human in the loop at the moment of purchase. Visa says merchants who accept ICC tokens will get liability-shift protection similar to EMV, provided they honour the agent's spend envelope. Acquirers including Stripe and Adyen have signalled support but have not yet published integration timelines.

Regulators are watching closely. The **European Commission's DG FISMA** is reviewing whether agent-initiated payments fall under PSD3's strong-customer-authentication rules, and the UK's FCA has opened a discussion paper on "delegated consent." In the US, the CFPB has asked both networks for briefings on how consumers revoke an agent's authority and how disputes flow when a language model, rather than a person, pressed "buy."

## What to watch

Three markers will define whether ICC is a platform or a press release. First, **partner expansion through 2026**: Visa has hinted at a second wave including a major airline group and at least one LLM vendor. Second, the **EU regulatory posture** — a restrictive reading of PSD3 could force Visa to ship a European variant with human-in-the-loop step-ups. Third, **volume metrics**: Visa declined to commit to disclosing agent-transaction counts in its fiscal Q3 results, but analysts will press. If agentic rails are the next mobile, the tape will show it within quarters, not years.
