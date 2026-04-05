Anthropic's Claude Opus 4.6 has independently discovered over 500 high-severity zero-day vulnerabilities in widely-used open-source software, many surviving decades of expert human review. The MAD Bugs Initiative, launched in March 2026, marks the first time an AI system has demonstrated the capability to autonomously identify and exploit critical vulnerabilities at this scale.

Claude delivered a working remote kernel exploit for FreeBSD CVE-2026-4747 in approximately 8 hours. The AI also discovered remote code execution vulnerabilities in Vim (CVE-2026-34714, CVSS 9.2) and GNU Emacs. One Linux kernel vulnerability had remained hidden for 23 years.

Claude's approach reads and reasons about code like a human researcher, looking at past fixes to find similar unaddressed bugs, spotting patterns that cause problems, and understanding logic well enough to know what input would break it.

Anthropic coordinates responsible disclosure with affected maintainers. While Vim patched in version 9.2.0272, Emacs maintainers declined to fix their vulnerability, leaving users exposed.

The initiative raises urgent questions: if Claude can discover 500+ zero-days in weeks, malicious actors with similar AI capabilities could identify and exploit vulnerabilities before patches become available. Adopting AI-powered security review may be existential for organizations managing critical infrastructure.