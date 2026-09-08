On September 2, the U.S. Cybersecurity and Infrastructure Security Agency did something that would have looked exotic a year ago. It ordered every federal civilian agency to patch an AI gateway.

CVE-2026-59822, an improper authentication flaw in Berri LiteLLM’s Model Context Protocol (MCP) Streamable HTTP endpoint, was one of seven vulnerabilities CISA added to its Known Exploited Vulnerabilities catalog that day, sitting alongside a SonicWall SMA 1000 bug rated CVSS 10.0 and a JFrog Artifactory authentication flaw at 9.8. The LiteLLM entry carries a CVSS v4 base score of 8.8 (NVD also lists a CVSS v3.1 score of 8.2), and it earned its place the hard way: Wiz Threat Research watched attackers try it against live honeypots.

The bug itself is almost embarrassingly small. According to the maintainers’ advisory, GHSA-7488-6r32-c95q, published June 30, 2026, LiteLLM’s MCP auth handler supported OAuth2 passthrough for upstream MCP servers, but the fallback path “could replace failed LiteLLM key validation with an empty UserAPIKeyAuth() object.” When the gateway failed to validate a key, it did not reject the request. It handed back a permission object with nothing in it and waved the caller through. Wiz put the consequence more bluntly: “Any Bearer token (even just a single character, e.g., x) grants full MCP access.”

## What MCP Is, and Why That Matters Here

The Model Context Protocol is the plumbing that lets AI agents reach outside their own context window. An MCP server exposes a set of tools — a database query, a code repository, a Slack workspace, an internal API — and an agent calls them the way a program calls a function. LiteLLM, an open-source proxy with more than 52,000 GitHub stars, sits in front of that arrangement: it routes model traffic to OpenAI, Anthropic, Azure, or Gemini, holds the API keys for all of them, and increasingly brokers MCP tool access for the agents behind it.

That makes an authentication bypass on the MCP endpoint far worse than one on an ordinary web app. The advisory spells out the reach: an attacker could use the flaw “to list and call configured MCP tools and access connected services exposed through MCP.” The gateway is not the prize. Everything downstream of it is. Wiz calls the problem credential concentration, noting that a single LiteLLM proxy “can hold keys for every model provider it routes to.”

Affected versions are everything prior to 1.84.0, and the fix shipped in 1.84.0. For operators who cannot upgrade immediately, LiteLLM’s guidance is to disable MCP routes or block the MCP endpoints at a reverse proxy or API gateway.

## From Honeypot to Catalog

Wiz researcher Yaara Shriki, credited as the reporter on the LiteLLM advisory, published 90 days of AI-infrastructure honeypot telemetry on August 27. The team observed exploitation of CVE-2026-59822 in the wild, with requests carrying single-character bearer tokens to probe model enumeration endpoints — reconnaissance aimed at working out which upstream provider a given proxy was fronting.

The LiteLLM ecosystem was already under pressure. CVE-2026-42271, a command-injection flaw in LiteLLM’s MCP server test endpoints scored at CVSS 8.7, was added to the KEV catalog in June 2026; chained with CVE-2026-48710, a Starlette host-header validation bypass rated 6.5 that CISA also listed on September 2, it yields fully unauthenticated remote code execution. Wiz says external researchers have linked the Qilin (Agenda) ransomware group to active exploitation of that chain, and its honeypots caught attackers using it to plant a Monero miner.

Microsoft, in an August 26 report, described attackers harvesting upstream provider key material and proxy-issued virtual keys from LiteLLM-backed PostgreSQL tables. “Across the cases, telemetry showed credential collection, durable access mechanisms, and resource monetization, even though the execution path differed by product,” Microsoft said.

Under Binding Operational Directive 26-04, federal civilian agencies had until September 5 to remediate five of the seven new entries. The Starlette and LiteLLM flaws carry a deadline of September 16, 2026.

## Why It Matters

The KEV catalog is the closest thing American cybersecurity policy has to a must-patch list, and until recently its contents read like an inventory of the conventional enterprise perimeter: VPN concentrators, file transfer appliances, groupware, hypervisors. AI infrastructure is now on that list on the same terms, judged by the same criterion — someone is actually exploiting it — and subject to the same federal clock.

That is a quiet but real milestone. An open-source Python proxy that most organizations installed as a convenience layer, often without a named owner or a patch cadence, is being treated as production infrastructure. Wiz’s State of AI in the Cloud 2026 report found that 90 percent of cloud environments run self-hosted AI software — roughly the exposure profile of a technology everyone deployed and nobody inventoried.

The supply-chain shape of this is worth sitting with. The bypass was not in a model. It was in the authentication glue between an agent and its tools, and it was reachable because MCP’s design premise is that an agent should be able to call things. Every additional MCP connection widens the blast radius of a single gateway compromise, and CVE-2026-59822 shows how little needs to go wrong for that radius to expand.

## What Defenders Should Watch

Upgrade to LiteLLM 1.84.0 or later, and if that cannot happen this week, block MCP endpoints at the proxy. Then assume the window was open. Anyone who ran a vulnerable version reachable from an untrusted network should treat every credential the gateway touched as potentially exposed, and audit the permissions granted to each connected MCP tool.

Beyond that, the useful shift is one of category. Wiz’s advice is to “patch on the assumption that the exploit is already in the wild,” because attackers targeting open-source AI infrastructure frequently weaponize fixes as soon as they land in public code. An AI gateway is a credential vault with an HTTP interface. Watch it like one: process-ancestry alerts when an AI server spawns a shell, tight egress restrictions, and an inventory of every MCP server your agents can reach.
