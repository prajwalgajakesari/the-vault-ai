Google has decided that Kubernetes, the system it invented to run the world’s containers, is the wrong place to keep an AI agent’s to-do list. The v0.3.0 release of AX (Agent Executor), the company’s open-source agent orchestrator, rips task state out of Kubernetes custom resources and drops it into Redis Streams, on the grounds that etcd, the key-value store under every Kubernetes cluster, was never built to absorb millions of short-lived agent tasks being created and destroyed every few seconds.

The release landed on Sept. 21 and took the top AI slot on Hacker News, where the thread sat at 481 points when AI Weekly flagged it and had climbed past 629 points and 288 comments by the next morning. The repository at github.com/google/ax shows roughly 2,000 stars, 116 forks and 623 commits, and the project remains Apache-2.0 licensed.

## Three services instead of one binary

Until this release, AX shipped as a single CLI with an embedded harness and a SQLite event log. Version 0.3.0 breaks that into three services: ax-server, an API front end that accepts kubectl-style manifests; ax-controller, a reconciler that drives desired state toward reality; and ax-task-runner, a sandboxed process that boots inside each agent’s isolated environment and does the work. The old Python harness, the ATE client, the SQL event log and the bundled skill examples are gone, so anyone on v0.2.x faces a real migration rather than a version bump.

The bigger shift is where state lives. Earlier versions modeled each task as a Kubernetes custom resource, so every create, update and delete flowed through the API server into etcd. That works for Deployments, not for coding agents that spawn a sandbox, run for ninety seconds and vanish, thousands of times a minute. Per the release commit, AX now stores resource state in Redis and distributes reconciliation work through Redis Streams, and controllers scale horizontally by adding replicas.

The developer surface stays deliberately Kubernetes-shaped. Four primitives define the API: Task for isolated execution with CPU and memory limits, Workspace for the Git repos, MCP servers and skills an agent needs, Gateway for an outbound allowlist of hosts and ports plus credential injection, and Model for centralized provider and secret configuration. You write YAML, run ax apply, then ax watch, ax suspend and ax resume as if the task were a Pod. The project’s site states the rationale plainly: “Agents are a new kind of workload. They are neither microservices nor batch jobs. They accumulate state, need strict isolation, call out to model APIs and tool servers, and can waste resources if nobody is watching.”

## The Substrate dependency and the pushback

AX does not run on bare Kubernetes. It sits on Agent Substrate, Google’s actor-style compute layer for GKE that multiplexes many suspended agent sessions onto a small pool of pods. Google’s public demo showed 250 stateful sessions on eight pods. The “billions of tasks per cluster” figure on the AX homepage remains a design target, not a benchmark anyone outside Google has reproduced.

That stack drew the sharpest criticism on Hacker News. The top comment set the site’s promise of “joyful workflows” against a quickstart that requires a Kubernetes cluster, the ko build tool, a container registry and a reachable Agent Substrate Control API, and concluded: “Call me old-fashioned but I don’t find this ‘easier’.” Another commenter, hhh, objected to the density trick itself: “I don’t really like the oversubscription of agent pods though, as you can no longer trust the k8s pod identity as being from a singular workload.” A Google engineer posting as ahmedtd replied that Substrate is being made an OIDC and SPIFFE identity provider so per-actor credentials can be injected at the egress gateway, work he said is in flight and due within weeks.

Kevin Riedl of Wavect, who reviewed the code at the commit just before release, flagged a gap the Redis migration does not touch. “A sandbox can contain an agent without containing its bill,” he wrote, noting that the TaskSpec field once reserved for budget and approval policies is now marked removed, that the sample Gateway allows every host on port 443, and that the control plane does not yet read back a task command’s exit status.

## Why it matters

The etcd decision is the most honest thing in the release. For a decade the reflex among platform teams has been to model every new workload as a custom resource and let the Kubernetes control loop handle it. Google, which knows etcd’s limits better than anyone, is saying out loud that agent tasks are too numerous and too ephemeral for that pattern, and that the right split is a thin Kubernetes-flavored API over a fast streaming store. Expect that argument to reappear in every rival runtime, from kagent to OpenAI’s hosted Agents API, which went to public beta on Sept. 10 with no cluster required.

The strategic play is familiar: open-source the orchestration layer while the density and snapshot machinery that makes it cheap lives in GKE. Give away the kernel, sell the cluster.

The risk is the org chart. Much of the thread debated whether AX will survive, citing Gemini CLI’s replacement by Antigravity CLI this year and noting that Google Cloud ships a second, structurally different answer to the same problem in Scion. As one commenter put it, Substrate is still in beta, “so this is a beta on another beta.”

## What to watch

Three signals will show whether AX is a durable bet or a launch-week artifact: whether the SPIFFE identity work lands in Substrate within the promised weeks, since without it the multiplexing model is a non-starter for regulated shops; whether Google reopens external pull requests, which remain paused during what the maintainers call a significant architectural redesign; and whether DeepMind’s own tooling, Antigravity and the managed agents API, routes through AX or builds something parallel. Barry Norman’s framing is the right one: the tell is not launch enthusiasm but who owns the roadmap two quarters from now.
