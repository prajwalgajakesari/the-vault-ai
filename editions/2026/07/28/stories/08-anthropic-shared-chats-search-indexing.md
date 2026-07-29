It started, as these things often do, with a Reddit thread and a search operator. Over the weekend of July 25, users typing `site:claude.ai/share` into Google discovered they could scroll through a long list of other people's shared Claude conversations: programming sessions, work notes, fake book reviews, erotica, and, more alarmingly, health records, private company documents, API keys, and the names and phone numbers of children. Conversations users assumed were semi-private, visible only to whoever held the link, had quietly become searchable to anyone.

By the time TechCrunch, WIRED, Fortune and 404 Media had picked up the story, the pattern was familiar. Anthropic had not leaked a database or suffered a breach. It had made a subtle configuration mistake that the entire AI industry seems doomed to keep making, one line of missing code at a time.

## Disallow is not noindex

The technical heart of the incident is a distinction that trips up even experienced engineers: the difference between telling a search crawler not to *fetch* a page and telling it not to *index* one.

Anthropic's `robots.txt` file had blocked the `/share` directory since at least September 2025. That sounds protective, and web publishers routinely treat `robots.txt` as a privacy wall. It is not. A `Disallow` rule asks well-behaved crawlers not to download a page's contents. But as Google's and Bing's own developer documentation spells out, a blocked URL can still be indexed and shown in results if the engine discovers it through an external link, a forum post, a social share, an accidental paste, because the crawler learns the URL exists even without reading the body.

The only reliable way to keep a page out of results is a `noindex` directive, delivered in the page's HTML or an `X-Robots-Tag` HTTP header. And here is the trap that closes the loop: if `robots.txt` blocks the page, the crawler never fetches it, so it never sees the `noindex` instruction inside. The two mechanisms actively undercut each other. WIRED reviewed exposed Claude pages and reported finding no `noindex` tag present. Search Engine Journal summarized the lesson bluntly in its headline: "Indexed Claude Chats Show Why Disallow Is Not Noindex."

## "Working as intended," until it wasn't

Anthropic's initial framing did the company few favors. Spokeswoman Amie Rotherham told TechCrunch: "We give people control over sharing their Claude conversations publicly, and in keeping with our privacy principles, we do not share chat directories or sitemaps with search engines like Google. These shareable links are not guessable or discoverable unless people choose to share them themselves." The Next Web ran with a sharper read of that stance under the headline "Anthropic says your leaked Claude chats are working as intended."

The problem is that "unless people choose to share them" glosses over how easily a share link escapes into the open web, and how, once it does, the missing `noindex` tag lets Google turn a private-feeling URL into a public search result. Google, for its part, pushed responsibility back upstream. Spokesperson Ned Adriance told TechCrunch that "neither Google nor any other search engine controls what pages are made public on the web," noting that site owners are given controls over crawling and indexing that Google respects.

Anthropic moved to fix the gap, deploying `noindex` tags and `robots.txt` updates. Reporting indicated Google had cleared most results by around July 26, though Bing lagged, and a GitHub repository had already archived a large volume of exposed messages, a reminder that on the web, removal is rarely the same as erasure.

## The industry keeps rerunning the same episode

If this feels like déjà vu, it is. In the summer of 2025, OpenAI faced almost the identical headline when Fast Company found thousands of shared ChatGPT conversations in Google. There the mechanism differed slightly, ChatGPT offered an opt-in "make this chat discoverable" toggle rather than an indexing gap, but the human outcome was the same: names, email addresses, resumes and intimate disclosures surfaced in search. OpenAI's chief information security officer, Dane Stuckey, called it a "short-lived experiment" and pulled the feature. Anthropic itself had a smaller precursor: Forbes reported last year that search engines had indexed a batch of Claude conversations, a scale Google put at just under 600 before they vanished.

The recurring lesson is not really about one config file. It is that "share" buttons on AI chatbots create a class of URL that users treat as ephemeral and private while the open web treats as permanent and public, and the two mental models collide the moment a link travels. Sensitive material ends up in a chatbot precisely because the interface feels intimate.

## What to watch

Watch whether Anthropic adds friction or clearer warnings to the share flow, not just a backend `noindex` patch, and whether it offers users a way to audit or revoke previously shared links. Watch Bing and the archived GitHub copies, since cached and mirrored content outlives any takedown. And watch whether regulators treat "indexable by default" share features as a privacy design defect rather than user error. Until sharing UX catches up with how people actually confide in these tools, expect this exact story to run again with a different logo on top.
