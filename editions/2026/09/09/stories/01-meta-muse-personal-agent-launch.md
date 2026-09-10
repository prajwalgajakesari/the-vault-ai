# Meta Launches Muse, a Personal AI Agent Spanning Web, Phones and WhatsApp

Meta on Tuesday introduced Muse, a personal AI agent that can send emails, book travel, negotiate bills and buy things on a user's behalf — the company's largest consumer AI bet yet, and one that asks Americans to hand a Meta product more of their private lives than Facebook or Instagram ever did.

Announced September 8, 2026, Muse is available immediately in the United States to users 18 and older through a standalone iOS and Android app, the web at muse.ai, and directly inside WhatsApp chats. Support for Meta's AI glasses is coming soon. The agent is free for most everyday use, with two subscription tiers layered on top: Power at $20 a month and Maximum at $100 a month.

The pitch is that Muse does not merely answer questions. In Meta's framing, it takes work off the user's plate — opening a browser, filling out forms, coordinating calendars, and continuing to grind on long-running projects after the app is closed, returning only when something changes or when it needs sign-off before an email goes out or money moves.

## What Meta Actually Shipped

Muse is powered by Muse Spark, the model family Meta describes as its most capable to date, developed under chief AI officer Alexandr Wang and first unveiled in April. Rather than running on a user's device, each Muse instance lives inside what Meta calls the Muse Secure VM — a dedicated virtual machine in Meta's cloud that houses both the agent and the user's connected data and credentials, with its own visible browser.

A second system called Sentinel runs on that same machine but is isolated from Muse at the system level. Muse can propose an action; Sentinel decides whether it is allowed, blocked, or escalated to the user. Nothing Muse does reaches the open internet without passing through it. Meta says the agent has no visibility into passwords or payment credentials, and that conversations and VM data are not shared with Meta's advertising systems. Users can revoke any connector, opt out of model training, and tell Muse to forget things it has learned.

Payments run through Link, built by Stripe, which issues a one-time-use card so real card numbers stay hidden. Meta says Muse is the first AI agent covered by Link's purchase protections, which include no-fee returns, coverage for lost or damaged items, and price-drop refunds. Shop Pay and 1Password integrations are slated to follow.

Wang framed the pricing as a compute-cost story rather than a growth lever. “For the vast majority of users, they should be able to do what they need to within the free tier,” he told Axios. “But for real power users, you know, those subscription tiers help us cover the compute costs.” There is no advertising inside Muse, though Wang said Meta is exploring commerce opportunities that could generate additional revenue.

Meta is explicit that this is a waypoint, not a destination. “The full vision in the future is we want to develop personal superintelligence that helps people accomplish their goals, pursue their passions, build things that they never would have built if they didn't have the technology,” Wang said. The product was a centerpiece of Mark Zuckerberg's 6,500-word AI manifesto published in August, in which he wrote that “everyone will have an exceptionally capable personal agent that understands you, your goals, and everything you care about.”

## Analysis: The Trust Tax on Agentic AI

Muse arrives in a crowded field. Google has Gemini Spark, Anthropic has Claude Cowork, and startups are wiring agents into browsers and messaging apps. What distinguishes Meta's entry is distribution: WhatsApp alone puts an agent inside a messaging surface used by billions, and the AI glasses roadmap extends it to a wearable Meta already sells at scale.

The problem is that reach is not the binding constraint — trust is. Muse launched less than two weeks after Meta agreed to an $18 billion multistate settlement over social media harms to children, and roughly a month after a New Mexico court ordered the company to pay $942 million in a related child-safety case. Meta paid a then-record $5 billion FTC penalty in 2019 over privacy violations, was charged with breaching that same order in 2023, and remains shadowed by Cambridge Analytica. An agent that wants read-and-write access to email, calendars, health apps, smart homes and payment rails is asking for far more than a news feed ever did.

That is why the engineering story — Secure VM, Sentinel, confidential computing — is also a trust-marketing story. Meta has published technical documentation, but those claims will need independent scrutiny from security researchers. The company has also hedged against approval fatigue, gating genuinely sensitive actions while letting previously authorized low-risk tasks proceed, an acknowledgment that a prompt users reflexively tap through protects no one.

The risks are not hypothetical. Meta's own researcher Summer Yue went viral after an OpenClaw agent deleted files from her Mac once she gave it access to her email. Services are already defending themselves: the restaurant platform Resy has said it will delete accounts caught using automated agents.

There is also a business logic beyond subscriptions. Meta built its advertising machine on knowing what people want. An agent that books the travel and completes the checkout sits one step closer to the transaction than any ad unit ever has. Meta insists Muse data stays away from its ad systems, and Wang says commerce is the revenue path being explored. Both can be true today and still describe a very different company in three years.

## What to Watch

Three things. First, whether Muse Confidential VM — the fully encrypted version Meta says only the user can unlock, promised before year-end — ships on time and survives outside audit. Second, whether third-party services welcome or block Muse's agentic traffic, which will determine how much of the launch demo actually works in the wild. And third, the conversion rate from the free tier to $20 and $100 plans: the clearest signal yet of whether consumers find an agent useful enough to pay for, and trust Meta enough to hand over the keys.
