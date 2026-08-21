# Coding Agents Keep Rediscovering the Same Repo. SkillForge Makes Them Take Notes.

Every time an AI coding agent opens a large codebase to fix a bug, it starts from nothing. It greps around, reads files, runs tests, and eventually produces a patch. Then the session ends and everything it worked out about that project evaporates. The next issue in the same repository begins with the same blind exploration, and often the same wrong turns.

A paper posted to arXiv on August 19, 2026 proposes a fix that is less about smarter models than about homework. The system, called *SkillForge* (arXiv:2608.18933), makes an agent practise on a repository before any real bug report arrives, then write down what it learned in a form it can look up later. On SWE-bench Verified, the standard 500-task benchmark built from real GitHub issues, it lifts a DeepSeek-V3.2 agent from 66.4 percent to 72.2 percent solved, a gain of **5.8 percentage points**.

The authors are Silin Chen, Han Li, Xiaodong Gu, Yuling Shi and Haibing Guan, all at Shanghai Jiao Tong University. They frame the problem as a cold start. “This limitation creates a cold-start problem: before project-specific knowledge has been acquired, even a highly capable agent is reduced to a generic repository explorer and can repeatedly fall into the same project-specific pitfalls,” they write.

## Manufacturing your own homework

SkillForge does not wait for real issues. It breaks the repository on purpose.

It starts with the project's own test suite, running passing tests under coverage instrumentation to see which lines each test exercises, then having an LLM pick the most important segments. Next comes the deliberately awkward step the authors call a strict mask: the model must rewrite each segment without ever seeing the original implementation. It gets the surrounding lines, the location, and a description of what the test checks, and writes a plausible replacement. Because a model's generic instincts diverge from a project's local conventions, the tests break. That divergence is the bug.

“Rather than explicitly injecting predefined faults, this strict-mask design exposes the gap between an agent's general coding knowledge and the repository's project-specific knowledge by inducing realistic implementation mistakes under constrained context,” the paper explains.

The broken snapshot is packaged like a real ticket, with an LLM-written problem statement that describes the symptom without leaking the fix. The agent repairs its own sabotage, and the trajectory is distilled into what SkillForge calls skills.

There are two kinds, both anchored to real code entities resolved against an AST-derived index of the repository, which the authors argue keeps the model from inventing interfaces that do not exist. *Global diagnostic skills* record an entity's role, a playbook for reasoning about it, and which other APIs tend to be involved alongside it. *Local intervention skills* record how that entity should be edited, distilled from failed attempts as well as successful ones, so the pitfalls get written down too.

Retrieval happens twice. Before the agent starts, a BM25 search over the issue text pulls the top five diagnostic records into the opening prompt. Then, as the agent works, SkillForge watches which files its shell commands touch, appending the intervention notes for a file the moment the agent opens it.

## The numbers

SkillForge was tested on two backbones, DeepSeek-V3.2 and GPT-5-mini, on the Mini-SWE-Agent scaffold, at temperature zero with a 250-step budget and pass@1 averaged over three runs.

On SWE-bench Verified the base agent scores 66.4 percent with DeepSeek-V3.2 and 55.0 with GPT-5-mini; SkillForge reaches 72.2 and 60.6. The strongest baseline, MemGovern, manages 69.2 and 58.0, while SWE-Exp, SAGE, SWE-Debate and Live-SWE-agent land between 0.6 and 2.8 points above baseline. On the harder, multi-language SWE-bench Pro, SkillForge gains 5.8 points with DeepSeek-V3.2 and 4.1 with GPT-5-mini.

Cost is an amortised figure folding in the offline work, 577 synthesised issues for the Verified run: roughly 7.4 US cents per issue versus 4.9 for the bare agent, against 38.2 cents for SWE-Debate.

Ablations show both skill types carry weight: dropping the diagnostic skills costs 3.8 points, dropping the intervention skills 4.4. Replacing trajectory-distilled skills with plain LLM-written repository summaries actually *hurt* GPT-5-mini, pushing it 0.6 points below baseline.

The most interesting ablation is transfer. A DeepSeek-V3.2 agent running on GPT-5-mini's skills falls from 72.2 to 65.2 percent. A GPT-5-mini agent running on DeepSeek's skills falls to 55.0, precisely its unassisted baseline. Whatever these notes encode, it is partly about the model that wrote them.

## What a 5.8-point gain does and does not prove

Most agent-memory work for software engineering is what the authors call reactive: it mines the repository's issue history, or burns compute exploring at test time for whichever issue is in front of it. “While effective, both paradigms acquire project-specific knowledge reactively,” they note. SkillForge's contribution is the direction of travel, generating the learning signal from code and tests that already exist.

The obvious objection is contamination. Repositories are rolled back before both the gold patch and the gold test patch, and an agent may only retrieve skills from synthetic issues whose commits predate the target instance. The issue types of the synthetic bugs, the authors report, do not overlap the real ones from the same repositories.

Still, a single benchmark family is a single benchmark family. SWE-bench Verified is Python, drawn from a dozen heavily studied projects the field has been optimising against for two years. And the dependence on tests is structural, as the authors concede: “code regions that are rarely exercised by runnable tests contribute fewer learning signals, which may reduce the effectiveness of the learned knowledge in repositories with limited test coverage.” Private enterprise codebases, where project-specific knowledge is scarcest, are exactly the ones with patchy coverage. The cost accounting deserves a squint too: amortising offline pre-computation across 500 instances is fair only if you intend to work in that repository indefinitely.

## What to watch

Whether the gain survives contact with frontier models is the first question, since written-down conventions may matter less to a model that infers them faster on its own. Staleness is the second: skills are pinned to specific files and functions, and nothing here addresses what happens to a module's playbook after that module is refactored. The third is transfer, a quiet warning to anyone imagining a shared, portable library of repository skills.

The code is public, so the first two questions are answerable by anyone with a compute budget and a free weekend.
