# An AI Model Uncovered Two Unknown Chrome V8 Zero-Days, and Google Patched Them

An AI model went looking for weaknesses in the software that runs on more than three billion browsers, and it found two nobody knew about. On August 10, OpenAI disclosed that its new GPT-5.6-Cyber model had analyzed V8, the JavaScript engine at the heart of Google Chrome, and surfaced two previously unknown vulnerabilities that could be chained together to corrupt memory and break out of V8's heap sandbox. Google has since patched them, bundling the fix under a single identifier: CVE-2026-15903.

The disclosure landed as part of OpenAI's expansion of Daybreak, its cybersecurity program, and it is one of the more concrete demonstrations to date that frontier models can find real, exploitable flaws in hardened, heavily-audited code rather than just toy bugs in demo apps.

## What the model found

According to OpenAI, GPT-5.6-Cyber's researchers pointed the model at V8 and it identified a defect in the engine's optimizing compiler: a safety check was skipped during an integer conversion, allowing an out-of-bounds array index that an attacker could use to read or overwrite memory. Chained with a second bug, that primitive was enough to escape the V8 heap sandbox — the isolation layer specifically designed to contain exactly this class of memory-corruption bug.

OpenAI says its researchers validated the findings and reported them to Google through coordinated disclosure. Google fixed the issue and credited it as CVE-2026-15903.

The public CVE record captures how serious the underlying flaw is. It is described as an "out of bounds read and write in V8 in Google Chrome prior to 150.0.7871.128," allowing a remote attacker to "execute arbitrary code inside a sandbox via a crafted HTML page." It carries a CVSS v3.1 score of 8.8 (High), with a network attack vector, low attack complexity, no privileges required, and only user interaction — visiting a malicious page — needed to trigger it. The weaknesses map to CWE-125 (out-of-bounds read) and CWE-787 (out-of-bounds write). The CVE was reserved on July 15 and published July 20, 2026, and Google shipped the fix in a mid-July Chrome Stable channel update. Its EPSS exploitation-probability score currently sits low, around 0.3%, reflecting that there is no evidence of in-the-wild abuse.

## A model built to refuse less

GPT-5.6-Cyber is not OpenAI's general-purpose model. It is a specialized variant, based on GPT-5.6 Sol, released through a new "Daybreak Red" tier gated behind identity verification, monitoring, and legal declarations, with hardware security keys becoming mandatory for all Daybreak accounts on September 1, 2026. The company split the program in two: Daybreak Blue for defensive work like malware analysis and incident response, and Daybreak Red for offensive research — vulnerability discovery, exploit validation, and penetration testing.

The design goal was a model that says yes to sensitive security questions other models reflexively block. On OpenAI's internal "Advanced Cybersecurity Completion Rate" benchmark, GPT-5.6-Cyber answered 95% of queries covering scenarios like exploit-chain development and authentication bypass, versus 1.5% for GPT-5.6 Sol with standard safeguards and 57.3% for the earlier GPT-5.5-Cyber. The Chrome bugs were not the model's only find: OpenAI says it also contributed to identifying at least five vulnerabilities in an unnamed popular mobile operating system, three critical flaws in a database, and hundreds of privilege-escalation bugs in an operating-system kernel.

OpenAI framed the whole effort around timing. "As these capabilities spread, defenders have a narrowing window to prepare," the company wrote in its announcement, arguing that "democratizing access to frontier intelligence for defenders is crucial to accelerating and automating cyber defense."

## The offense-defense problem, out in the open

This is the uncomfortable core of the story. A model trained to be exceptionally good at finding zero-days is exceptionally good at finding zero-days regardless of who is holding it. OpenAI rated GPT-5.6-Cyber "High" for cybersecurity capability under its Preparedness Framework — capable, but short of the "Critical" threshold it expects a future model to reach.

The V8 result cuts both ways. It shows AI-assisted disclosure working as intended: bug found, validated, reported, patched before any known exploitation. Google's own Big Sleep effort has previously used AI to surface Chrome and V8 flaws, so the direction of travel is not new. What is new is the pace and the productization — a commercial model, sold to vetted defenders, generating patchable findings in one of the most scrutinized codebases on the planet. The same throughput in less scrupulous hands is the scenario the whole Daybreak vetting apparatus exists to slow down.

## What to watch

Three things. First, whether independent researchers or Google publish technical detail on the second bug in the chain — the sandbox-escape half is the part that matters most and remains the least described. Second, whether other labs follow with comparable disclosures against major targets, which would signal AI vulnerability discovery is becoming routine rather than a headline. Third, real-world telemetry: CVE-2026-15903's exploitation probability is low today, but proof-of-concept work tends to follow public disclosure. If you run Chrome, confirm you are on 150.0.7871.128 or later — the patch is the entire point.
