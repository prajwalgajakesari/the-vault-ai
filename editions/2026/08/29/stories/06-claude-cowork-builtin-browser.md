Anthropic shipped a Chromium browser inside Claude Cowork on Wednesday, August 26, 2026, and in doing so retired the awkward compromise that had defined Claude's relationship with the web for exactly one year. Until this week, letting Claude touch a live webpage meant handing it *your* browser through the Claude in Chrome extension — your tabs, your cookies, your logins, your risk surface. Claude now has a browser of its own.

The timing is almost too neat. The original Claude Chrome extension launched on August 26, 2025. Anthropic marked its first birthday by declaring it generally available on every paid plan and, in the same news cycle, announcing the feature that makes it optional for most tasks.

**How it works:** when a Cowork task needs a website, a browser opens in the side panel next to the task transcript. Claude loads pages, reads them, clicks, types, and fills forms while the user watches. Links inside the transcript open in that same panel. The company's framing in its announcement post is blunt about why the extension was never the right primitive: a lot of web tasks don't need *your* browser, just *a* browser, and now Claude has one.

## What ships, and to whom

The built-in browser runs in the Claude Desktop app on macOS, Windows, and Linux, with Linux still flagged as beta. It reached **Enterprise plans immediately**, with admins controlling it under Organization settings, and began a staged rollout to **Pro, Max, and Team** plans over the following week. Once it lands on an account it is on by default — give Claude a task involving a website and the panel opens on its own.

The isolation story is the sales pitch. Anthropic's help documentation is explicit that the built-in browser is separate from the user's own browser and that Claude does not see saved logins unless they are deliberately imported. Maximilian Schreiner of The Decoder summarized the boundary this way: “The browser stays separate from your own, so Claude can't see your tabs, bookmarks, or passwords.”

Logins can be carried across, but only site by site and only from certain browsers: **Chrome, Edge, and Firefox on macOS, and Firefox only on Windows and Linux**. Safari import is not supported at all. Banking, email, and single sign-on sites arrive unchecked by default. Frederic Lardinois, senior editor for AI at The New Stack, notes the likely reason for that inconsistent matrix: Chrome and Edge on Windows harden cookie storage against infostealers, while Firefox still uses a plain SQLite database.

There is one meaningful catch buried in the support docs: **anything signed into inside the built-in browser stays available to Claude in future Cowork sessions on that machine**. The session is isolated from your personal browser profile, not from your own future sessions.

## The two browsers, and which one wins

Anthropic is not deprecating the extension — it is splitting the job. The built-in browser is for handing off web work while you keep doing something else: gathering research, pulling invoices from a vendor portal, working a system with no connector. Claude in Chrome is for the page already in front of you, with the accounts you are already signed in to.

If the extension is already installed, it stays the default. Otherwise Cowork uses the built-in browser. Users can flip it in Settings, Cowork, Preferred browser. And because the browser lives in the desktop app, that app must be open and online — though a task started there can be steered from Claude on web or mobile.

Lardinois, who has used the equivalent feature in OpenAI's ChatGPT desktop app, was candid about the old arrangement: “That always felt a bit like a hack, though it worked reasonably well.”

## What agent-controlled browsing does to the web

The safeguards are real and measurable. Anthropic runs the same stack it built for Chrome: permission before Claude acts on a site for the first time, high-risk sites blocked outright, and a classifier that checks every action against what the user actually asked for. The published numbers show the arc — an unprotected browser agent in early red-teaming followed hidden malicious instructions **23.6%** of the time; mitigations in autonomous mode cut that to **11.2%**; and at general availability, with probes and the safety classifier running, Anthropic reports **0%** attack success against Sonnet 5, Opus 5, and Mythos 5, **0.3%** against Fable 5, and under **0.08%** in combined internal testing. The company still says plainly that the risk is not zero, and its own guidance strongly advises against using either browser for financial accounts, medical information, or other people's personal data.

But the deeper shift is economic, not just adversarial. A browser that ships inside an AI app is a browser that visits publisher pages without a human ever seeing the ad slot, the subscription wall, or the newsletter prompt. Every isolated agent profile is a session with no cookie history, no ad identity, and no attribution trail — traffic that looks synthetic to analytics because it is. Publishers have spent two years arguing about crawlers that train models. Agentic browsing is the harder problem: it is not scraping, it is *reading*, at a scale and cadence no human audience produces, on infrastructure publishers pay for and cannot monetize. Bot-detection vendors now face a category they cannot cleanly classify — a request that is automated, authorized by a real paying user, and indistinguishable from a person at the packet level.

Lardinois offered the consolation available today: because Claude's browser is unlikely to be logged into many sensitive sites, if something goes wrong “the blast radius here is hopefully small.” That holds only as long as users resist importing the very logins that make the tool genuinely useful.

**What to watch:** whether Anthropic ships an agent-identifying header publishers can act on; whether cookie import expands to Chrome on Windows, which would change the blast-radius math; and whether that reported 0% injection rate survives contact with researchers who now have a fixed, shippable target.
