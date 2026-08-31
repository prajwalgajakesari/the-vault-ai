Anthropic needed about ninety minutes to answer the biggest question in developer tooling this week, and it answered with compute.

On Friday, August 28, OpenAI notified SpaceX that it intends to wind down the contract supplying its models to Cursor, proposing a shutoff date of **November 12, 2026**. Before the news cycle had finished absorbing it, Anthropic co-founder and chief compute officer Tom Brown posted a thirty-four-word reply on X that has since become the most-quoted line of the episode.

**"Cursor has been a trusted partner of Anthropic since Sonnet 3.5,"** Brown wrote. **"We'll continue to increase compute to support Claude models in Cursor and are excited for what comes next with them at SpaceX."**

Two frontier labs looked at the same customer, the same owner and the same terms of service, and moved in opposite directions on the same afternoon.

## The clause and the counter-offer

The mechanism behind OpenAI's exit was contractual, not competitive. SpaceX closed its **$60 billion all-stock acquisition** of Anysphere, Cursor's parent, on **August 14**, paying 389.3 million shares of SpaceX Class A stock according to the 8-K filed with the SEC. That ownership change opened a narrow change-of-control window in OpenAI's supply agreement, and OpenAI used it, giving the maximum notice the contract allowed — seventy-six days.

OpenAI framed the decision as a matter of assurance rather than rivalry. **"We are making this choice because we cannot be confident that SpaceX will use our technology within our terms of service, based on our experience with Elon Musk's companies violating contracts,"** the company wrote.

What makes Anthropic's response remarkable is that the same argument was available to it with considerably more precedent attached. Anthropic's commercial terms bar customers from building products that compete with its services — a broader restriction than the training-data limits OpenAI and Google typically rely on. And Anthropic has enforced aggressively. It cut Windsurf off from Claude in June 2025 on less than five days' notice while OpenAI was circling the company. It revoked OpenAI's own Claude API access that August over unauthorized benchmarking. In January 2026 it cut xAI's engineers off from Claude entirely — and it found them precisely because they were coming in through Cursor.

Cursor is now owned by the company that owns xAI. Anthropic stayed anyway, and offered more capacity as it did.

The offer has substance behind it. Anthropic's capacity posture changed materially on **May 6, 2026**, when it announced a compute partnership with SpaceX covering the entirety of the Colossus 1 data center — **more than 300 megawatts and over 220,000 NVIDIA GPUs** delivered within a month. Anthropic tied that deal directly to user-facing limits: it **doubled Claude Code's five-hour rate limits** for Pro, Max, Team and seat-based Enterprise plans, removed the peak-hours limit reduction on Claude Code for Pro and Max accounts, and raised API rate limits considerably for Claude Opus models. Brown's pledge to keep increasing compute inside Cursor is an extension of that same capacity story, aimed at the developers who will spend the fall deciding which model tab to default to.

Cursor, for its part, is projecting indifference to the loss. Co-founder and chief executive Michael Truell — now a SpaceX executive — put a number on it within a day: **"OpenAI models serve about 5% of Cursor user traffic, and we're speaking with the OpenAI team to resolve this."**

## Why it matters

Strip out the Musk-Altman feud and what remains is a clean illustration of two business models diverging under pressure.

OpenAI's center of gravity is ChatGPT. Its revenue, its brand and its political weight all run through a consumer product it owns end to end. Losing a first-party slot inside a third-party editor with roughly $4 billion in annualized revenue costs OpenAI a channel, not a business — which is why it could credibly call the decision a matter of trust rather than money.

Anthropic does not have that cushion, and has never pretended to want one. It sells the model itself, through the API and through partners, and coding is its single strongest category. Cursor is one of the largest rooms full of paying professional developers that Anthropic does not own. Walking away to make a point about Musk would have handed several billion dollars of annualized coding demand to Google's Gemini and to whatever SpaceX's own labs ship next. Model-as-infrastructure businesses do not get to fire their biggest retail channels over the identity of the acquirer.

There is a second, less flattering reason, and it explains why the announcement drew a sharp reaction from people who build on these APIs. Since May, Anthropic has been renting Colossus 1 from SpaceX. SpaceX supplies Anthropic's compute and, as of August 14, also owns Anthropic's distribution. Enforcing terms of service against Cursor would mean enforcing them against a landlord. The higher Claude limits developers enjoy today were, quite literally, paid for with Musk's GPUs.

That circularity was not lost on the industry. Replit chief executive Amjad Masad publicly reminded Brown of Windsurf. Docker executive Mat Velloso was blunter: **"This was a great opportunity to stay quiet."**

## What to watch

The first test is whether Brown's post becomes policy. A tweet promising more compute is not a published rate-limit change; watch for a formal announcement with numbers attached before November 12.

The second is whether November 12 arrives at all. OpenAI called the date proposed, Truell says talks are underway, and a renegotiated agreement with tighter compliance terms remains plausible.

The third is the one that will actually strain Anthropic's position. Cursor is training its own in-house model on Colossus, drawing on traffic from developers writing code inside the editor every day. When that model ships and competes directly with Claude Code, Anthropic's competitive-products clause stops being theoretical — and the lab that has cut off three partners in fourteen months will have to decide whether loyalty survives contact with a rival trained on its own supplier's hardware.
