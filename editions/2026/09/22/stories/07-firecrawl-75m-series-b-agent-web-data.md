# Firecrawl Lands $75M Series B to Build the Web Layer for AI Agents

Firecrawl, the San Francisco startup whose scraping and search APIs have become default plumbing for AI agents that need to read the web, has raised a $75 million Series B. The company is betting that the next phase of the business is not scraping more pages but paying the people who own the data agents want.

The round, announced September 22, was led by Smash Capital, with participation from Altos Ventures, Nexus Venture Partners, Y Combinator, Freestyle and Offline Ventures. Alongside the raise, Firecrawl launched Alexandria, a service that puts official data providers, Firecrawl's own curated indexes and the live web behind a single API. In a blog post announcing the deal, CEO Caleb Peffer was blunt about where the money is headed: “We’re going to spend a good chunk of it buying knowledge from people, which takes some explaining.”

## From scraper to library

Firecrawl grew out of Mendable, an earlier chat-with-your-docs product from the same founders, Peffer, CTO Nicolas Silberstein Camara and Eric Ciarla. Building Mendable, the team concluded that pulling clean, reliable information off the web was the hardest part of the stack. Firecrawl was the answer, and it now counts more than 1.5 million users, according to the company. Its open-source repository has passed 183,000 stars on GitHub.

The core product handles the mechanics that trip up conventional scrapers. As SiliconANGLE reported, many pages load in multiple phases, and naive scrapers grab content before rendering finishes; Firecrawl uses a smart wait feature to avoid those data-quality errors. It can also scroll, click and submit forms to expose content that only appears after interaction, with developers describing the desired behavior in plain-language prompts. It extracts data from PDFs, Word documents and other hosted files, monitors pages for changes, and offers an agent-oriented search engine that filters results by creation date and file type.

Alexandria sits on top of that. At launch its provider network spans 88 official data providers, registries and publishers offering 504 capabilities across 28 categories, plus more than 113 million indexed sources. Firecrawl's Research Index holds tens of millions of scientific paper abstracts, its Developer Index covers tens of millions of documentation files, READMEs, issues and merged pull requests, and a Government Index covers laws, regulations and ordinances. Search Engine Watch noted that named sources include company financials from Fiscal.ai and podcast transcripts from Particle. Discovery is free; each tool call costs the credits listed for it. In internal testing across 845 tasks using the same model and prompts with blind AI judging, Firecrawl says agents using Alexandria scored 21 percent higher on answer quality than those relying on built-in web tools.

## Paying for what agents read

The most consequential part of the announcement is the payment model. Firecrawl already pays Wikimedia Enterprise for direct access to Wikipedia data rather than scraping it. When Wikimedia announced that partnership in March, it said Firecrawl was handling 2 million to 3 million Wikipedia requests a month. The company now plans to open a self-service system that lets individuals, content creators and organizations contribute knowledge and get paid based on demand from AI agents.

“People have licensed data for training, but almost no one gets paid when an AI agent actually uses what they know,” Peffer said in the company's press release. Smash Capital founder and partner Brad Twohig pointed to adoption as the reason for the bet: “Over 1.5 million users build with Firecrawl because it solves a problem everyone working with AI runs into.”

The details, however, are still thin. Search Engine Watch pointed out that the provider sign-up page is currently a waitlist, and that the launch materials publish no payout rates or revenue split for new contributors. Developers can see what a request costs, but would-be providers cannot yet calculate what they would earn.

## Why It Matters

Firecrawl is raising at a moment when the open web is becoming less open to machines. Cloudflare began blocking AI crawlers by default for new customers in 2025 and introduced a pay-per-crawl model that lets publishers charge bots for access, and publishers have spent the past year fighting over whether AI companies should compensate them for content. A company whose original value proposition was getting past the friction of scraping now faces a web where more of that friction is deliberate.

Alexandria is Firecrawl's hedge against that shift. By paying providers for structured, maintained feeds, as it does with Wikimedia, the company moves from being a tool that extracts data to a marketplace that brokers it. That is a stronger position if publishers keep locking down their sites, and it gives Firecrawl a story to tell rights holders that pure scrapers cannot. It also puts the startup in a crowded lane alongside agent-focused search and data players, where the moat will be the breadth and quality of licensed sources rather than rendering tricks.

## What to Watch

The key test is the self-service contributor program. Until Firecrawl publishes revenue shares, publishers have little basis to judge whether per-use agent payments beat blocking crawlers or signing bulk licensing deals directly with model makers. Watch, too, for how quickly the provider count grows past 88, whether the 21 percent quality gain holds up in independent benchmarks, and how Firecrawl's core scraping business coexists with infrastructure providers like Cloudflare that are increasingly deciding which bots get through the door.
