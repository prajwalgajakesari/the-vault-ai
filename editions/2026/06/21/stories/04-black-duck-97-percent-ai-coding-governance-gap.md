Artificial intelligence has won the developer. The question now is whether anyone is watching what it writes.

A new study from application-security firm Black Duck finds that 97% of enterprise developers now use AI coding assistants, an adoption rate so close to universal that the tools have crossed the line from competitive edge to baseline expectation. But the same survey exposes a yawning gap on the other side of the ledger: only 30% of organizations have a full governance framework in place to track, review, and secure the code those tools produce. In other words, AI is writing software at nearly every company surveyed, and roughly two-thirds of them are merging it without a complete set of guardrails.

The report, *The State of AI-Powered Software Development*, released June 9, is based on a survey of 831 enterprise software engineers and DevOps professionals at organizations with 500 or more employees, conducted in March 2026 with independent research firm UserEvidence. It lands as a clear warning that the productivity story everyone has been telling about AI coding has a less flattering second act.

## The numbers: adoption is total, oversight is partial

The headline figures describe a market that has already tipped. GitHub Copilot leads at 83% of teams, and Anthropic's Claude Code has climbed to 63% adoption, a striking figure for a product that is barely a year old in its current form. Most organizations are running more than one assistant at once.

The benefits are real and measured. Some 92% of development teams report improved productivity and release velocity, with 58% calling the improvement major. Developers reclaim an average of eight hours a week, and more than half (53%) say their total code volume has grown by over 25%.

But the same engineers describe the cost. Nearly 90% of teams encounter problems with AI-generated code, with the biggest bottlenecks appearing in manual code review (52%), security testing (51%), and code rework (48%). As Black Duck frames it, AI does not so much reduce work as relocate it, shifting effort from writing code to validating, testing, and remediating it.

## The governance gap

That relocation is precisely where the danger sits, because the validation stage is the one most companies have not formalized. Black Duck found that 68% of developers consider it extremely important to have a clear, automated system for tracking AI-generated code and measuring its impact for debugging, security, and accountability. Yet fewer than one in three teams actually has full governance in place.

The practical translation: at many organizations, AI-written code is being merged into production systems without established review policies, intellectual-property ownership frameworks, or dedicated security scanning for AI output. Each of those omissions carries a distinct risk. Without IP frameworks, companies cannot be certain their AI assistant did not reproduce licensed or copyrighted code, a live legal exposure. Without security scanning tuned to AI output, vulnerabilities ship at the same accelerated pace as everything else. And without review policies, accountability for a defect becomes a question no one can answer.

Black Duck CEO Jason Schmitt put the stakes bluntly. "AI coding assistants have permanently changed the economics of software development, and the productivity numbers make that undeniable," he said. "But the data also clearly shows that speed without governance is a liability, not an advantage. As AI-generated code volume and expectations increase, the winners with AI are the ones building automated security and governance guardrails that scale alongside their development velocity."

## Why this matters: the attack surface is growing faster than the controls

The report's most consequential finding may be the one that links volume to vulnerability. Nearly two-thirds of teams (64%) say they are moderately or extremely concerned that AI assistants are introducing security defects, and the most worried respondents tend to be the heaviest users. Among that subgroup, 51% rely on AI for most new development. The people closest to the tools, in other words, are the most anxious about what the tools are shipping.

The logic is uncomfortable but simple. As code generation accelerates and code volume scales, the attack surface expands in step, and manual security processes were never built to keep pace with machine-speed output. A governance gap is not a paperwork problem; it is ungoverned, unreviewed, potentially insecure code flowing into live systems at organizations that move fast precisely because AI lets them.

Black Duck, which sells exactly the kind of security and governance tooling the report says is missing, has an obvious commercial interest in framing the gap as urgent. The numbers, however, are independently collected, and the company makes a defensible case that governance pays for itself. Teams with full governance in place are 55% more likely to report a major improvement in efficiency, which reframes oversight not as a brake on velocity but as a multiplier of it.

## What the developer wants: AI to check AI, with a human nearby

The survey also sketches how engineers expect the workflow to evolve. An overwhelming 86% believe an AI agent or model should evaluate AI-generated code, and 56% would prefer a dedicated AI security agent separate from the tool that wrote the code in the first place. Even so, 84% want to keep a human in the loop through pull requests or real-time IDE suggestions. The role of the developer is not vanishing; it is migrating toward review, architecture, and security verification, the judgment-heavy work AI is least equipped to own.

## What to watch

The June study turns a familiar slogan, that AI coding boosts productivity, into a sharper and more demanding claim: productivity without governance is borrowed time. The 97% adoption figure is settled. The open question for the second half of 2026 is whether the 30% governance number climbs fast enough to close the gap before a high-profile breach or IP dispute forces the issue.

Watch for three signals. First, whether enterprises start treating AI-code governance as a board-level risk rather than a developer-tooling preference. Second, whether the vendors driving adoption, from GitHub Copilot to Claude Code, build security and provenance features directly into their products to differentiate. And third, whether regulators in the EU and elsewhere begin to treat ungoverned AI code as a compliance failure. The economics of software have changed permanently. Whether the controls catch up is the story of the year still being written.
