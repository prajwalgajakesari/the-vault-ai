---
headline: "Critical Vulnerability in Hugging Face LeRobot Enables Unauthenticated Remote Code Execution"
slug: huggingface-lerobot-critical-rce-flaw
category: llms-genai
story_number: "07"
date: 2026-04-28
---

# Critical Vulnerability in Hugging Face LeRobot Enables Unauthenticated Remote Code Execution

A critical security flaw in Hugging Face's open-source robotics framework LeRobot would allow any attacker with network access to execute arbitrary code on GPU-backed inference servers, with no credentials required. The vulnerability, tracked as CVE-2026-25874 and carrying a near-maximum CVSS score of 9.8, exposes a disturbing pattern in the AI ecosystem: the very company that built a safe serialization alternative continues to ship dangerous code in its own products.

## The Flaw

The vulnerability resides in LeRobot's asynchronous inference architecture, specifically in the PolicyServer component that offloads policy computation to GPU-backed servers via gRPC. Security researcher Valentin Lobstein discovered that two critical RPC handlers in the PolicyServer -- SendPolicyInstructions and SendObservations -- use Python's notoriously unsafe pickle.loads() function to deserialize data received directly from the network, with zero authentication or encryption.

The gRPC service is configured using add_insecure_port(), meaning all communications lack Transport Layer Security and any form of access control. An attacker who can reach the exposed port needs only to send a crafted pickle payload to achieve full remote code execution on the host machine. The attack requires no authentication, no user interaction, and no special privileges.

"The async inference module exposes a gRPC server that calls pickle.loads() on attacker-controlled data in two separate RPC handlers, without any authentication. The gRPC channel uses add_insecure_port() -- no TLS, no auth, nothing," Lobstein wrote in his detailed technical disclosure. "Anyone with network access to the port gets code execution on the server."

Lobstein confirmed the vulnerability against a stock installation of lerobot version 0.4.3 from PyPI, demonstrating that a 61-byte payload was sufficient to achieve arbitrary command execution. The proof-of-concept exploit sends the malicious pickle through the SendPolicyInstructions endpoint; the server deserializes and executes the payload before any type validation occurs. A post-deserialization isinstance() check exists in the code, but by the time it runs, the damage is already done.

## Scope and Impact

LeRobot is not a fringe project. With more than 21,500 stars on GitHub, it is Hugging Face's flagship platform for real-world robotics, providing tools for training robot policies using machine learning. The async inference module is designed for production deployments where a robot sends camera observations to a remote GPU server and receives motor actions in return. In these deployments, the PolicyServer must be network-accessible, and users routinely bind the service to 0.0.0.0 to enable communication with external hardware.

The consequences of exploitation are severe. Because LeRobot is designed for GPU-backed robotics environments, successful attacks can lead to full server compromise, theft of sensitive credentials and proprietary model weights, disruption of robotic operations, and potential safety risks where physical hardware is involved. Researchers at Resecurity, who published an independent analysis of the vulnerability, warned that the flaw "highlights a recurring issue in the machine learning ecosystem where rapid prototyping is prioritized over secure coding practices" and that GPU inference servers "often run with elevated privileges, access to robotics hardware, internal networks, datasets, and expensive compute resources."

The vulnerability affects LeRobot through version 0.5.1. No official patch has been released as of publication. According to the GitHub Advisory (GHSA-f7vj-73pm-m822), a fix is expected in version 0.6.0, but no timeline for that release has been announced.

## A Pattern of Neglect

What makes CVE-2026-25874 particularly striking is the context. Hugging Face is the creator of safetensors, a serialization format designed specifically because pickle is dangerous for machine learning data. The company's own documentation, blog posts, and library all warn against using pickle for untrusted data. Yet their own robotics framework deserializes attacker-controlled network input with pickle.loads().

The developers were not unaware of the risk. Both vulnerable code paths are annotated with # nosec comments -- directives that suppress warnings from Bandit, Python's automated security linter. The tool flagged the danger. The developers silenced it.

"The irony here is hard to overstate," Lobstein wrote. "HuggingFace created safetensors -- a serialization format designed specifically because pickle is dangerous for ML data. And yet their own robotics framework deserializes attacker-controlled network input with pickle.loads(), with # nosec comments to silence the tool that was trying to warn them."

This was not even the first warning. Another researcher, identified as Chenpinji on GitHub, submitted a private vulnerability report through GitHub's Security tab in December 2025. A LeRobot maintainer acknowledged on January 7, 2026, that "this does pose a security risk" and that "that part of the codebase needs to be almost entirely refactored." No fix followed. The last interaction in that thread dates to January 12, with no further response.

## The Broader AI Supply Chain Problem

CVE-2026-25874 is not an isolated incident. It is symptomatic of a systemic weakness in the AI and machine learning supply chain, where frameworks built for research convenience are increasingly deployed in production environments with real security requirements.

Python's pickle module has been a known attack vector for over a decade. Its documentation explicitly warns that "it is possible to construct malicious pickle data which will execute arbitrary code during unpickling." Yet pickle remains pervasive across the ML ecosystem because it handles the complex nested data structures -- tensors, model configurations, training state -- that machine learning workflows produce. The convenience comes at the cost of security, and the bill is now coming due as these frameworks move from research notebooks to production robotics and inference infrastructure.

Organizations using LeRobot should take immediate action. Resecurity recommends replacing pickle with secure alternatives such as JSON, native protobuf fields, or safetensors for tensor data; enabling encrypted communication by switching from add_insecure_port() to add_secure_port() with TLS; and enforcing authentication using gRPC interceptors and token-based access controls. In the absence of an official patch, any deployment of LeRobot's async inference server on anything other than a fully isolated, trusted network should be considered compromised by default.

## What to Watch

The critical question now is how quickly Hugging Face will ship version 0.6.0 with a fix. The timeline so far -- from the first private disclosure in December 2025 through the CVE publication on April 23, 2026, with no patch in sight -- does not inspire confidence. For an organization that positions itself as the central hub of the open-source AI ecosystem, the gap between its security advocacy and its security practice is becoming difficult to ignore.
