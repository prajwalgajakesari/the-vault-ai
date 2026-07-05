## A crackdown aimed at the fine print, not the law

Anthropic is done treating Chinese access to Claude as someone else's enforcement problem. The company is now hunting the workarounds — the offshore subsidiaries, personal-subscription reimbursements and cloud proxies that let Chinese technology firms reach its models without technically breaking any law, according to a Financial Times report published July 3, 2026 and confirmed by several outlets.

The distinction matters. Anthropic's terms of service prohibit Chinese companies, and foreign entities they control, from using its models. But the methods reportedly used by firms including Ant Group and ByteDance don't run afoul of US or Chinese statute. They breach a contract, not a border. That gap — between what is illegal and what is merely against the rules — is exactly the space Anthropic is now trying to close through detection rather than litigation.

## The specific workarounds

The reporting lays out a menu of evasion techniques, each engineered to make prohibited corporate use look like something permissible.

Ant Group reportedly issued employees corporate Claude accounts tied to a Singapore-based subsidiary, routing developers inside mainland China through a legally separate overseas entity. ByteDance took a consumer-shaped approach: it reimbursed engineers who bought personal Claude subscriptions and reached the service over VPNs, dressing up corporate usage as individual retail activity. Other groups reportedly purchased Claude access through foreign-incorporated units running on cloud infrastructure — including Microsoft Azure — which adds a layer of intermediary that makes tracing the real user harder.

What ties these together is jurisdictional laundering. A Singapore shell, a personal card, an Azure tenant abroad: none of them is illegal, and each blurs the line of accountability that Anthropic's terms depend on.

## How Anthropic is trying to catch it

The new enforcement leans on behavioral and account-level signals rather than paperwork. According to the reporting, Anthropic is monitoring indicators such as users' computer time zones and usage patterns to flag accounts that behave like relays for China-linked firms. A person briefed on the policy said the company specifically wants to dismantle a growing network of Singapore subsidiaries being used to acquire US AI technology with less scrutiny.

Anthropic is also targeting so-called "transfer station" relay services — intermediaries that resell or proxy access — and is scrutinizing ownership structures rather than just billing addresses. That mirrors a policy update the company published on restricting sales to unsupported regions, which extends its ban to entities more than 50% owned, directly or indirectly, by companies headquartered in places like China, regardless of where those entities physically operate.

## Distillation is the real fear

Underneath the terms-of-service enforcement sits a sharper anxiety: distillation. Anthropic frames some large-scale, systematic querying as "distillation attacks" — an effort to extract a frontier model's capabilities and fold them into a competitor's training data.

The company made this concrete in a letter to US senators. It described what it called the largest known distillation campaign it had identified, attributing it to operatives linked to Alibaba's Qwen lab: roughly 25,000 fraudulent accounts generating more than 28.8 million interactions with Claude between April 22 and June 5, 2026. (That Alibaba fake-accounts allegation is a related but distinct matter from the offshore-workaround crackdown; the two share a threat model but not a set of defendants.) The logic of distillation is what makes access control feel existential to labs: feed millions of structured queries into a stronger model, harvest its answers, and fine-tune a cheaper domestic system to approximate its reasoning — cloning capability at a fraction of the cost of building it.

## The geopolitics: where private terms meet public policy

This crackdown does not happen in a vacuum. In mid-June 2026, the US government reportedly ordered Anthropic to block non-US nationals from accessing its most powerful models on national-security grounds, partly over concerns a China-linked group had reached a new model. Anthropic has publicly backed strong export controls, arguing that maintaining America's compute advantage is a national-security priority.

The result is a firm doing frontier-model diplomacy through its own terms of service. Where chip export controls govern hardware, Anthropic's account-level enforcement is trying to govern access to capability — a domain no export regime cleanly covers. The limits are obvious. Time-zone signals can be spoofed with cloud VMs; ownership can be restructured; a new relay can replace a shuttered one. Enforcement here is a cat-and-mouse game, and the mouse has the resources of some of the world's largest technology companies.

## What to watch

Watch whether Anthropic names or bans specific corporate entities, which would move this from quiet detection to public confrontation. Watch Microsoft and other cloud partners: if proxy access runs through Azure, enforcement may require provider cooperation Anthropic can't compel alone. Watch for a policy response — whether Washington tries to codify model-access rules the way it has codified chip rules. And watch the other labs. If distillation defense becomes table stakes, OpenAI and Google will face the same offshore workarounds, and the same uncomfortable question of how far a private company's contract can substitute for public law.
