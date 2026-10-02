Reddit is shutting two of the oldest ways to read its content from outside the site. On Wednesday, September 30, the company said RSS feeds will stop working on Friday, November 13, 2026, and that public access to its API will close by March 2027. Its stated reason is AI-era scraping. Reddit says RSS has become a "common surface for large-scale scraping and automated abuse," and it is closing that route along with the open API that third-party tools have used for more than a decade.

The timing stands out. The same company that is cutting off free, open access to its data is also selling that data. In its most recent quarter, Reddit's "other revenue" line, which includes AI data licensing, grew 24% year over year to $43 million.

## What Is Changing, and When

Reddit announced the changes in a post to moderators on r/modnews and in a separate post for developers on r/redditdev. It presented them as the next phase of an infrastructure overhaul it previewed over the summer. "In August, we shared plans to modernize Reddit's infrastructure, build better mod tools, and make it harder for bad actors to scrape Reddit and abuse communities. Today, we have specifics on what's changing, when, and how to plan ahead," the company wrote, according to Decrypt.

The schedule has several stages. Reddit stops accepting new public API requests on October 31. RSS ends on November 13. Developers of approved third-party apps and bots have to register with Reddit before January 12, 2027, and unregistered apps start losing access after that date. All remaining public API access closes in March 2027.

Reddit wants developers to rebuild on Devvit, its in-house Developer Platform. To help, it is offering a $1 million App Migration Program that pays $1,000 to each eligible app that completes the move and includes free hosting. Applications are due November 30. The Next Web reports that more than 14,000 apps and bots have registered to migrate so far. According to Decrypt, Reddit says well-known utilities such as RemindMeBot, DeltaBot and MagicEyeBot have finished or nearly finished migrating.

Old Reddit, the text-heavy classic interface many longtime users still prefer, is getting tighter limits too. It already requires a login. Over the coming months, access will be limited to moderators and to users who have visited Old Reddit in the past six months. Reddit says logged-out traffic was the biggest source of abusive scraping on that version of the site.

## No Off-Ramp for Most RSS Users

Moderators who rely on RSS for alerts can switch to Discord Relay, a Devvit app that sends notifications to Discord. Everyone else gets nothing. That includes people who follow subreddits in feed readers, researchers tracking discussions, and newsrooms watching for breaking posts. "If you use RSS for feeds outside of a community you moderate, there is no replacement," Reddit wrote.

Moderators pushed back in the replies. "RSS is the only way I find out about posts in subs like this one," one moderator wrote, as quoted by The Next Web. Others were worried about separate changes to Automod: new communities, and communities that have never used it, will lose Automod's ability to remove, filter or approve posts, with Reddit's Rules Hub and Automations becoming the default. Some moderators warned this would lead to more bans. When Reddit first hinted at the RSS change, users said the site would become "unmanageable" for them, according to coverage of the announcement.

## Why It Matters

This is less a technical cleanup than a decision about who controls access to one of the internet's largest collections of human conversation. Years of people comparing products, troubleshooting software and describing symptoms are exactly the kind of text AI developers want. Reddit has turned that into a licensing business. It signed a deal reported at roughly $60 million a year with Google in early 2024, followed by one with OpenAI. Companies without deals have ended up in court: Reddit sued Anthropic in June 2025 and Perplexity, along with three data-scraping firms, in October 2025. Perplexity and SerpApi have disputed the claims.

Seen that way, RSS and the public API are leaks in a paywall. Both are open, machine-readable channels that let anyone take in Reddit content without signing a contract. Reddit's account is believable: scrapers have gotten better at posing as ordinary browsers, and Cloudflare's chief executive said this week that bot traffic could reach 1,000 times human traffic. But shutting down open protocols outright, rather than rate-limiting or authenticating them, also strengthens Reddit's position with paying AI customers. The cost lands on the people who never scraped anything at scale: hobbyist developers, academic researchers, accessibility tools and users who simply want to read Reddit outside Reddit's own apps.

The move also fits a wider pattern. Platforms that once treated openness as a growth engine are now treating it as a liability. The 2023 API pricing fight, when thousands of subreddits went dark in protest, ended with Reddit getting its way. This time the change goes further: there is no paid tier for RSS, only an end date. If other large user-generated content sites follow, the open web's syndication layer could shrink into a set of licensed pipes, with access decided by commercial agreements rather than by public standards.

## What to Watch

The first test comes on November 13, when feed readers and monitoring tools that depend on Reddit RSS go dark. Watch the developer registration count before the January 12 cutoff, and how many popular bots quietly disappear instead of migrating to Devvit. Moderator reaction could still harden into organized protest, as it did in 2023. Reddit's next earnings report will show whether shutting off open access goes along with faster growth in AI licensing revenue. That would be the clearest sign that this decision is as much about the business as about abuse.
