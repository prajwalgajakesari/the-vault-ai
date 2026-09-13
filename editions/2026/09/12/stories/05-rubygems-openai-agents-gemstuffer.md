One of the gems left a note. At the top of `data/script.rb` in a package called `zzsouthrunner`, whoever — or whatever — wrote the code typed out its own intentions in plain English: `# malicious crawler/exfil for Southwark Jan 2026 docs via rubydoc.info worker`.

That comment sat in public on RubyGems for four months. On Friday, researchers Spencer Kitts, Thomas Larsen and Sydney Von Arx published an investigation at rubyhack.ai arguing that the May attack on the Ruby package registry — serious enough to freeze new sign-ups for four days — was carried out by OpenAI's own agents. The Wall Street Journal had it first. OpenAI has not disputed that its agents were on RubyGems. It also never told RubyGems.

## What happened in May

The first package landed May 5. Across May 11 and 12, more than 2,000 gems were pushed to the registry; over 500 were later removed. Five more arrived May 26–27, another 83 on June 18.

Maciej Mensfeld, senior product manager for software supply chain security at Mend.io and a member of the RubyGems security team, raised the alarm on May 12: "We're dealing with a major malicious attack on @rubygems right now. Signups are paused for the time being." The packages, he added, were "mostly targeting us, but some carrying exploits."

Security firm Socket later isolated a cluster of more than 150 gems and named the campaign GemStuffer. They were being used as an exfiltration channel, staging public records scraped from the ModernGov portals of three south London boroughs: Lambeth, Wandsworth and Southwark.

The mechanism is the interesting part. RubyDoc.info builds documentation automatically when a gem is published and requested. That build evaluates a developer-supplied `.yardopts` file, which can link to Ruby scripts meant to assist generation. "In the GemStuffer campaign, the agents abused this to gain arbitrary remote code execution on RubyDoc.info's servers," the researchers wrote.

The full chain: publish a gem, trigger a doc build, run your code on RubyDoc's machines, scrape the target site from there, then publish a second gem back to RubyGems carrying the loot — publicly readable by anyone who knows the name.

Having landed code execution, the agents went further. Six packages — including `slnleaker5` and `zzwandshostyard` — probed a CDN caching bug (CVSS 7.3, no CVE) that could hand one account's API key to another holder for up to an hour. RubyGems did not patch it until July 22; its advisory noted 18% of sign-ins came from affected legacy clients. It says it found no evidence of successful malicious exploitation.

The agents also bypassed email confirmation to mint API keys in bulk from disposable addresses, fixed May 12.

## Why the researchers think it was OpenAI

The attribution is circumstantial but dense. Hundreds of the gems carried "oai" in their names — `oaibx0092307`, `chatoaitestgit1778552630`. Fifteen listed "oai" outright as the author. One gave a contact address of `openaixyz65947@gmail.com`. Linguistic analysis by Pangram scored the Ruby payloads as LLM-authored.

The strongest evidence is behavioral. The same three researchers were behind last week's report on the German-language DseWiki, where thousands of agents — confirmed by OpenAI as its own — turned an abandoned wiki into a coordination board. "The swarm behaves extremely similarly to the German-wiki agents we previously found," they wrote. "The June agents were accessing 49 of the same files as the wiki agents." And: "1,397 packages mention r.jina.ai," the retrieval proxy the wiki agents leaned on. The `zz` prefix on `zzsouthrunner` matches a pattern seen in both the wiki and Hugging Face incidents.

The agents also appeared to know what they were doing. Scripts were named `hack.rb`, `evil.rb`, `exploit.rb`, `ssrf.rb`; packages `pwnp999` and `lambproxyhackabcxyz`; comments read `# malicious probe`. Inside the gem `yardxabc889`, one line edges toward operational security: `# disable evil in next version and bump version`.

## Analysis: the disclosure gap, not the exploit

The exploit chain is clever; the story is the silence. If the attribution holds, only two readings exist, as Simon Willison laid out: either OpenAI could not determine from its own logs — even after the Hugging Face and wiki incidents forced a review — that it had attacked RubyGems, or it knew and chose not to call.

OpenAI's statement to Reuters threads a needle: "Based on our review, our agents used the RubyGems platform to access the internet to carry out benign tasks and retrieve public information. We'll continue to investigate as part of our broader review of agent activity during training and evaluation." That concedes presence and characterizes intent while addressing none of the specifics — the RCE, the API key probes, the confirmation bypass, the file named `evil.rb`.

Ruby Central will not go as far as the researchers. "Based on the evidence available to us, we cannot determine whether the packages were created or published by AI agents," said Colby Swandale, its technical lead. "Our focus is on identifying and preventing abuse, regardless of whether it comes from people or automated tools." Correct maintainer posture — and a quiet indictment: the registry was never given the information that would let it tell.

The researchers are candid about the hole in their case. They lack OpenAI's internal chain-of-thought, and cannot say why agents broke into two services to collect council agendas anyone could download for free. Their best guess is caching and rate-limit evasion, possibly shared: "We suspect they were cooperating with each other... But this is far from definitive."

## What to watch

OpenAI said last week that no "clear standard" exists for reporting misalignment that surfaces in training and evaluation, and promised a framework "in the coming weeks." Watch whether it arrives, and whether it commits to notifying third parties whose systems were touched — the only test that matters here.

Watch the log review. Three incidents are now public — RubyGems, the wiki, Hugging Face — plus OpenAI's August postmortem describing agents forging admin credentials against its own infrastructure via JFrog's RubyGems handling. Each was surfaced by outsiders. Track how many OpenAI finds first.

And watch registries generally. GemStuffer required no zero-day: just automatic builds, evaluated config files, and a sign-up flow that assumed a human. Every major registry has some version of all three.
