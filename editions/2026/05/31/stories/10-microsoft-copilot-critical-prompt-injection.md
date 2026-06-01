Microsoft disclosed and remediated three critical information disclosure vulnerabilities in Microsoft 365 Copilot and Copilot Chat on May 7, publishing security advisories for CVE-2026-26129, CVE-2026-26164, and CVE-2026-33111. The vulnerabilities, all rated Critical severity, demonstrated that prompt injection attacks against enterprise AI assistants remain a serious and evolving threat.

The disclosures represent the first time Microsoft has issued formal CVE identifiers for prompt injection vulnerabilities in its Copilot products, a significant step toward treating AI security flaws with the same rigor applied to traditional software vulnerabilities.

"These advisories reflect our commitment to the cloud CVE transparency initiative," said Vasu Jakkal, Microsoft's Corporate Vice President for Security. "By publishing CVEs for AI-specific vulnerabilities, we are establishing a framework for how the industry should handle AI security disclosures."

## The Three Vulnerabilities

CVE-2026-26129 affects Microsoft 365 Copilot's Business Chat feature and stems from improper neutralization of special elements in output. An attacker could craft inputs that cause Copilot to leak sensitive information from the user's connected documents, emails, and chat history.

CVE-2026-26164, classified as an improper neutralization vulnerability affecting a downstream component, carries a CVSS score of 7.5 with a network-based attack vector requiring no privileges or user interaction. This makes it particularly dangerous in enterprise environments where Copilot has broad access to organizational data.

CVE-2026-33111 targets Copilot Chat embedded in Microsoft Edge and is classified as a command injection vulnerability. Like the others, it requires no privileges or user interaction to exploit, meaning a malicious webpage or email could potentially trigger data exfiltration without the user's knowledge.

## The Broader Pattern

The Microsoft disclosures arrived against a backdrop of escalating concerns about AI assistant security. Earlier in 2026, researchers demonstrated a "Reprompt" attack technique that exploited Microsoft Copilot's data access to steal sensitive information through carefully crafted indirect prompt injections.

The pattern is consistent: as AI assistants gain deeper integration with enterprise data systems, the attack surface expands proportionally. Every document, email, and database that Copilot can access becomes a potential target for extraction through prompt manipulation.

"We are seeing a fundamental shift in the threat landscape," said Johann Rehberger, an independent security researcher who has documented multiple Copilot vulnerabilities. "Prompt injection is not a theoretical risk anymore. It is a practical attack vector that sophisticated adversaries are already exploring."

## Microsoft's Response

Microsoft confirmed that all three vulnerabilities were fully mitigated on the server side before the CVE disclosures were published, meaning customers did not need to take any action. The company's ability to patch AI vulnerabilities through cloud updates represents an advantage over on-premises software, though it also raises questions about vulnerabilities that might exist between discovery and remediation.

The company also published a companion blog post on May 7 titled "When Prompts Become Shells," which analyzed broader patterns of prompt injection leading to remote code execution in AI agent frameworks -- signaling that Microsoft views prompt injection as a systemic issue rather than a series of isolated bugs.

## What to Watch

The issuance of formal CVEs for AI prompt injection sets a precedent that other companies will likely follow. Watch for similar disclosures from Google, Anthropic, and other providers of enterprise AI assistants. The key question is whether the industry can develop standardized defenses against prompt injection that scale across different AI architectures and deployment patterns.