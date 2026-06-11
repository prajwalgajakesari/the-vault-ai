# NVIDIA and ServiceNow Push Autonomous Agents From the Desktop to the Data Center

Enterprise AI has learned to generate text, then to reason. At ServiceNow Knowledge 2026, NVIDIA and ServiceNow set out to answer the harder question now facing every CIO: how should AI act — and who is accountable when it does?

The two companies announced a significant expansion of their partnership to deliver governed, long-running autonomous agents that span the full enterprise stack, from individual employee desktops to the large-scale "AI factories" running in corporate data centers. NVIDIA founder and CEO Jensen Huang joined ServiceNow chairman and CEO Bill McDermott on the opening keynote stage in Las Vegas to frame the next phase of enterprise AI, one defined less by what models can say than by what agents can safely do.

The centerpiece is Project Arc, which ServiceNow describes as an enterprise autonomous desktop agent that "thinks, writes code, executes, and adapts when things don't go as expected," completing complex, multi-step work across enterprise tools without requiring pre-built workflows. Unlike standalone agents, Project Arc connects natively to the ServiceNow AI Platform, can access local file systems, terminals and installed applications, and runs every action inside NVIDIA OpenShell — an open-source, sandboxed runtime that contains what an agent can see, which tools it can use, and how each action is logged.

## The Governance Layer

The pitch is that autonomy without auditability is a non-starter for enterprise security teams. Project Arc's actions are governed by ServiceNow AI Control Tower, which sets policies, monitors behavior, and logs the files an agent reads, the commands it executes, and the APIs it calls. The agent is grounded in ServiceNow's Configuration Management Database and powered by ServiceNow Action Fabric, giving it operational context about how work actually flows through an organization.

"ServiceNow and NVIDIA set out to make AI real for the enterprise, and today we're showing the proof of that work," said Joe Davis, executive vice president of AI Engineering and Delivery at ServiceNow. "Whether it's autonomous AI agents that can be trusted on the desktop, governance that extends to the data center, or open benchmarks that hold the entire industry accountable, this is enterprise AI that's built to last."

NVIDIA framed the move as a control problem at scale. "Long-running, autonomous agents are rapidly changing the game for enterprise AI, and delivering them securely at scale requires governance that spans models, software and AI infrastructure," said Kari Briski, vice president of generative AI for enterprise at NVIDIA. "Together, NVIDIA and ServiceNow are bringing enterprises agents that feature the security of the NVIDIA OpenShell runtime and the power of NVIDIA AI factory solutions with the ServiceNow AI Control Tower, providing the control layer necessary for trusted, autonomous operations across the business."

That governance now reaches the infrastructure layer. ServiceNow AI Control Tower has been folded into the NVIDIA Enterprise AI Factory validated design — an integration previewed at NVIDIA GTC in March and now generally available — extending lifecycle management, compliance monitoring, and real-time observability to the data centers where large model workloads run. Added capabilities include regulatory content packs, enterprise access maps for major cloud providers, and a runtime cost-and-ROI framework that tracks monthly value indicators.

## The Economics and the Benchmarks

Cost is the throughline. As agents become always-on across millions of workflows, token economics becomes central, and NVIDIA leaned on hardware math to make the case: the NVIDIA Blackwell platform delivers more than 50x greater token output per watt than the prior Hopper generation, translating to nearly 35x lower cost per million tokens. ServiceNow, for its part, says more than 100 billion workflows run on its platform each year — the surface area these agents are meant to automate.

The partnership also produced an attempt at industry accountability. The companies are advancing NOWAI-Bench, an open benchmarking suite released as open source and being integrated into NVIDIA's NeMo Gym. It comprises EnterpriseOps-Gym, a multi-step agentic evaluation spanning IT service management, customer service and HR workflows, and EVA-Bench, a voice-agent evaluation framework. NVIDIA says its Nemotron 3 Super open model currently posts leading performance among open-weight models on EnterpriseOps-Gym, while EVA-Bench is serving as a primary benchmark for the in-development Nemotron VoiceChat model.

One caveat for buyers: Project Arc is available only as an early preview. The AI Control Tower integration with the Enterprise AI Factory design and the NOWAI-Bench releases are generally available, but the headline desktop agent has not yet reached broad production availability — a reminder to weigh demo-stage capability against deployment-ready maturity.

## Why It Matters

The enterprise agentic-AI race has shifted from who has the smartest model to who can make autonomous agents safe, auditable and cheap enough to run at scale. By pairing ServiceNow's workflow and governance footprint with NVIDIA's compute, open models and OpenShell runtime, the two are staking out an integrated "control layer" position against Microsoft, Salesforce, Google and a field of agent startups all chasing the same prize: agents that do real work without exposing the enterprise to ungoverned risk. The bet is that governance, not raw capability, becomes the gating factor for production deployment — and that owning the control plane is as strategically valuable as owning the model.

## What to Watch

Watch for Project Arc to move from early preview toward general availability, and for the first named enterprise customers with measurable productivity results. Track whether NOWAI-Bench gains adoption beyond NVIDIA and ServiceNow as a genuine cross-industry standard or remains a vendor-aligned yardstick. And watch how rivals respond — whether competing platforms embrace OpenShell's open runtime or push proprietary alternatives will shape whether enterprises get an interoperable agent ecosystem or another set of walled gardens.
