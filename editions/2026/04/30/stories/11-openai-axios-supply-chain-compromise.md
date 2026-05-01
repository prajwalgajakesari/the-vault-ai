---
headline: "OpenAI Revokes macOS Certificates After Axios Supply Chain Attack Compromises Code-Signing"
slug: openai-axios-supply-chain-compromise
category: policy
story_number: "11"
date: 2026-04-30
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html
  - name: OpenAI
    url: https://openai.com/index/axios-developer-tool-compromise/
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/openai-rotates-macos-certs-after-axios-attack-hit-code-signing-workflow/
  - name: Google Cloud Blog
    url: https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package
  - name: Palo Alto Unit 42
    url: https://unit42.paloaltonetworks.com/axios-supply-chain-attack/
  - name: SC Media
    url: https://www.scworld.com/news/openais-macos-app-signing-process-hit-by-axios-supply-chain-attack
---

# OpenAI Revokes macOS Certificates After Axios Supply Chain Attack Compromises Code-Signing

A North Korea-linked supply chain attack that poisoned one of the most popular JavaScript libraries on the internet has forced OpenAI to revoke all of its macOS code-signing certificates, setting a May 8 deadline for millions of users to update their desktop applications or risk being locked out entirely.

The incident, which OpenAI disclosed on April 11, traces back to March 31, when threat actors hijacked the npm account of a maintainer of Axios, the widely used HTTP request library that averages over 100 million weekly downloads. The attackers pushed two malicious versions, v1.14.1 and v0.30.4, each containing a hidden dependency called "plain-crypto-js" that functioned as a cross-platform remote access trojan.

OpenAI's GitHub Actions workflow, which handles code-signing for macOS applications, automatically downloaded the compromised Axios package during a routine build. That workflow had access to the certificate and notarization material used to sign ChatGPT Desktop, Codex, Codex CLI, and Atlas, the company's suite of macOS applications.

## How the Attack Unfolded

Google's Threat Intelligence Group attributed the compromise to UNC1069, a financially motivated North Korean threat actor active since at least 2018. Microsoft independently linked the operation to the group it tracks as Sapphire Sleet, an offshoot of the BlueNoroff cybercrime operation known for targeting cryptocurrency platforms and developer infrastructure.

The attackers gained access through a highly targeted social engineering campaign against the Axios maintainer. Once inside the npm account, they changed the associated email address to an attacker-controlled Proton Mail account and published the poisoned packages. The malicious dependency exploited npm's postinstall hook to silently execute an obfuscated JavaScript dropper called 'setup.js," which deployed WAVESHAPER.V2, an updated version of a backdoor previously attributed to North Korean operations. The payload worked across Windows, macOS, and Linux.

The tainted versions were live for approximately three hours between 00:21 and 03:20 UTC on March 31 before being detected and pulled. But in the npm ecosystem, three hours is an eternity. Any CI/CD pipeline that ran during that window and pulled a floating version of Axios, rather than a pinned commit hash, was potentially exposed.

## OpenAI's Response

OpenAI said its own analysis concluded the signing certificate was "likely not successfully stolen," based on the timing of the payload execution and how the certificate is injected into the build job. But the company chose not to take chances.

"Out of an abundance of caution, we are treating the certificate as compromised and are revoking and rotating it," OpenAI wrote in its disclosure. The company confirmed that "no evidence was found that OpenAI user data was accessed, that systems or intellectual property was compromised, or that software was altered." User accounts, passwords, and API keys were not impacted.

The practical consequence is significant. Once OpenAI fully revokes the certificate on May 8, macOS security protections will block new downloads and first-time launches of any application signed with the old certificate. Users who do not update before the deadline may find their ChatGPT Desktop app simply refuses to open. OpenAI is giving users a 30-day window to minimize disruption, but older versions of all macOS desktop apps will lose updates and support permanently.

## A Root Cause That Should Alarm Every Engineering Team

The root cause was a misconfiguration in OpenAI's GitHub Actions workflow. The action used a floating tag to reference the Axios dependency rather than a specific commit hash, and did not have a configured minimumReleaseAge for new packages. In other words, OpenAI's build system was set to automatically trust the latest version of a third-party package, with no delay or verification buffer.

This is not a novel vulnerability. Security researchers have warned for years that floating version tags in CI/CD pipelines are an open invitation for supply chain attacks. The SolarWinds compromise of 2020, the Codecov incident of 2021, and the ua-parser-js hijack later that year all exploited similar trust assumptions. Yet the practice remains endemic across the software industry.

"The Axios incident is a textbook example of why pinning dependencies to commit hashes and enforcing release age minimums should be non-negotiable for any pipeline with access to signing material," said researchers at Palo Alto Networks' Unit 42 in their threat brief on the attack. "The blast radius of a three-hour window in a package with 100 million weekly downloads is effectively unbounded."

## Implications for the AI Industry

The attack carries particular weight for the AI sector, where the stakes of compromised software distribution are escalating rapidly. AI desktop applications increasingly have deep access to user systems, clipboard data, file systems, and in the case of coding assistants like Codex, direct access to development environments and source code. A successfully signed and distributed trojanized update to any of these tools could have provided attackers with a foothold in thousands of developer workstations.

The incident also highlights how the AI industry's breakneck shipping pace can collide with security fundamentals. Companies racing to deploy new models and features may be cutting corners on build pipeline hygiene, treating it as an infrastructure concern that can be addressed later. The Axios compromise demonstrates that "later" can arrive without warning, delivered through a dependency five layers deep in your build graph.

For organizations that depend on AI desktop tools, the lesson is immediate and concrete: audit your own dependency chains, pin your versions, enforce release age gates, and assume that any package in your supply chain, no matter how popular or well-maintained, can be weaponized overnight. OpenAI learned this the hard way. The next company in the crosshairs may not be as fortunate in its timing.