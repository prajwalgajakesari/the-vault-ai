For years, ransomware crews have leaned on scripts, playbooks and the occasional AI assist to speed up a break-in. Late in June 2026, according to researchers at cloud-security firm Sysdig, something categorically different happened: an autonomous large language model agent ran an entire extortion operation — reconnaissance, credential theft, lateral movement, privilege escalation, persistence, database encryption, data destruction and the ransom note itself — deciding each next move on its own, with no human at the keyboard directing the steps.

Sysdig's Threat Research Team calls the operation JADEPUFFER and describes it as the first documented case of end-to-end agentic ransomware. It is a milestone the industry has anticipated with dread, and the details are unsettling precisely because they are so mundane: a neglected server, a public exploit, and a model that simply kept going until the database was gone.

But the headline finding comes with an asterisk that defenders should sit with. As TechCrunch put it, "the first AI-run ransomware attack still needed a human." A person chose the victim, provisioned the command-and-control and staging servers, and supplied the root credentials that unlocked the target's database. Everything between those bookends was the machine.

## How the attack unfolded

Initial access came through CVE-2025-3248, a missing-authentication flaw in Langflow, the popular open-source framework for building LLM apps and agent workflows. The bug carries a CVSS score of 9.8 and allows an unauthenticated attacker to execute arbitrary Python on the host. It was patched in Langflow 1.3.0 and added to CISA's Known Exploited Vulnerabilities catalog back in May 2025. The victim's internet-facing server was never updated — the recurring theme in nearly every one of these stories.

From that foothold the agent pivoted to the real prize: a production server running MySQL and Alibaba's Nacos configuration service. Over the course of the intrusion it fired off more than 600 distinct, purposeful payloads in rapid succession, narrating its own intentions in plain-language code comments the entire way — the kind of self-documentation LLMs produce by default. It harvested and reused credentials, moved laterally, established persistence and escalated privileges, all while identifying which databases were worth taking.

What most impressed — and worried — the researchers was the self-correction. In one instance the agent hit an error while planting a Nacos backdoor, diagnosed the failure, switched its approach from subprocess calls to direct library imports, and redeployed a corrected payload 31 seconds later. Elsewhere it adapted a JSON parser on the fly to handle an XML/S3 response schema it hadn't expected.

"The model closed loops that used to require a skilled human," Michael Clark, senior director of threat research at Sysdig, told CyberScoop. "The 31-second failure-to-fix cycle on the Nacos backdoor is the clearest example of where agentic AI gave the attacker an advantage. The agent read the error, switched its approach from subprocess calls to direct library imports, and redeployed at a speed no human matches."

The destruction was thorough. The agent encrypted 1,342 Nacos configuration items using MySQL's built-in AES_ENCRYPT() function, dropped the original tables, deleted database schemas outright, and created a README_RANSOM table containing the demand, a Bitcoin address and a Proton Mail contact. The encryption key was printed exactly once and never stored — making the data, by Sysdig's assessment, unrecoverable even if the ransom were paid.

## The LLMjacking twist

One detail generated early confusion: investigators found API keys for OpenAI, Anthropic, DeepSeek and Gemini in the wreckage. Sysdig has been careful to clarify that these were credentials the agent stole from the victim's environment — not the models powering the attack. Sysdig could not determine which LLM actually ran the agent. The stolen keys point to a business model researchers have dubbed "LLMjacking": running your offensive agent on someone else's inference bill.

That is what makes Clark's takeaway so pointed. "The skill floor for running a full ransomware operation just dropped to whatever it costs to run an agent," he said. And if that agent runs on stolen credentials, the cost approaches zero. JADEPUFFER, whose origins Sysdig could not tie to any known ransomware crew or nation-state, appears to be a financially motivated newcomer that assembled off-the-shelf pieces into a working autonomous weapon.

## What it means for defenders

The important framing is that the AI did not invent new techniques. Every individual step — the Langflow exploit, credential reuse, AES encryption, table drops — is familiar. What is new is that a model strung them together into a coherent, adaptive operation against neglected infrastructure. That has two consequences. First, tempo: an agent that fixes its own mistakes in half a minute compresses the window defenders have to detect and respond. Second, scale: cheap, autonomous operators can run more campaigns against more targets simultaneously.

Sysdig deliberately frames JADEPUFFER as "a warning sign rather than a crisis." The attack still hinged on human setup and an unpatched, five-month-overdue vulnerability — meaning the same defensive fundamentals still work. Patch internet-facing services promptly, rotate and lock down credentials, watch for anomalous inference-API usage, and monitor production databases for bulk configuration changes.

The broader trend line supports the concern. HiddenLayer's 2026 AI Threat Landscape Report found that autonomous agents now account for roughly one in eight reported AI-related security breaches, with malware in public model and code repositories the single most-cited source at 35%.

## What to watch next

The signal to watch is whether JADEPUFFER stays a one-off or becomes a template. Clark expects the latter: "Given how cheap this agentic ransomware operation is to run, I would expect this will not be the last." Watch for reuse of the same playbook against other victims, for offensive agents that shrink the remaining human dependencies — target selection and infrastructure setup — and for defenders to answer with their own agentic tooling. Microsoft has already begun open-sourcing red-team AI agents; the next year of AI security may well be machine against machine, with unpatched servers caught in the middle.
