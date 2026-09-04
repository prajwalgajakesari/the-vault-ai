# 4.5 Billion TikTok Records Are Sitting on Hugging Face. The Only Thing Stopping Misuse Is a Dataset Card.

On Hugging Face, the largest public repository of machine learning artifacts on the internet, sits roughly 289 gigabytes of compressed files describing 4.5 billion TikTok videos. One independent researcher assembled it in about three weeks. It is free to download. And the only thing standing between that archive and the uses its own author says are forbidden is a paragraph of text on the dataset card.

That paragraph is the entire safety architecture.

The upload surfaced publicly on September 3, 2026, when AI Weekly flagged it in a breaking alert. The collection is metadata rather than video files, which is how billions of rows fit into a few hundred gigabytes: captions, view and like and comment and save counts, sound identifiers, country codes, posting timestamps. The author acknowledges on the dataset page that the collection violated TikTok terms of service, and imposes restrictions drawn from GDPR and CCPA that prohibit using the data to identify, profile, or target individuals. Accounts circulating on social platforms note the card also tells downloaders that compliance obligations pass to them the moment they pull the files.

**The Vault is deliberately not describing how the collection was carried out.** What matters is not the technique but the governance vacuum it landed in: one person produced a corpus larger than most commercial social listening products, published it on infrastructure designed for open science, and attached a license nobody is positioned to enforce.

## The Data Is Not As Harmless As Metadata Sounds

The instinct is to shrug at metadata. No faces, no videos, no phone numbers. But captions are user-authored text, and creator-linked engagement records at this scale are not a spreadsheet of anonymous statistics. They are a longitudinal map of who posted what, when, from where, and how the platform responded. Privacy scholars have spent a decade arguing that the public-versus-private framing collapses at exactly this scale.

A 2025 legally grounded audit of DataComp CommonPool, one of the most widely downloaded web-scraped training sets, found that its results "provide concrete evidence to support the concern that any large-scale web-scraped dataset may contain personal data" despite curators sanitization efforts. Its authors argued for reorienting how the law treats publicly available information.

Regulators reached a similar place earlier. In an August 24, 2023 joint statement, the Office of the Australian Information Commissioner and eleven counterpart data protection authorities warned that "individuals lose control of their personal information when it is scraped without their knowledge and against their expectations," and added that "even if individuals decide to delete their information from a social media account, data scrapers will likely continue using and sharing information they have already scraped." That statement was sent directly to ByteDance, TikTok parent company, alongside Alphabet, Meta, Microsoft, Sina and X. A follow-up in October 2024, coordinated with the UK Information Commissioner Office and sixteen other authorities, extended those expectations explicitly to platform data used for training AI models.

The people whose posts are in this archive were never asked. Most will never know.

## Hugging Face Is a Host, Not a Referee

Hugging Face has been more deliberate than most platforms here. Its content policy, updated in June 2023, put consent at the center. "In this evolving legal landscape, it becomes increasingly important to emphasize the intrinsic value of consent to avoid enabling harm," the company wrote, framing moderation of machine learning artifacts as distinct from static content moderation. It maintains a public register of takedown notices and has removed scraped datasets before; a large Archive of Our Own corpus came down in April 2025 after a contested rights dispute.

But that model is reactive. Takedowns require a complainant with standing, and the people with the strongest privacy interest here are individual creators, none of whom have the resources to file. The party with both standing and money, TikTok, holds a terms-of-service claim rather than a privacy claim on its users behalf. TikTok has publicly said it deploys detection, rate limiting and other measures against unauthorized scraping, and has sued scrapers before. As of publication, neither TikTok nor Hugging Face has commented on this dataset.

## Why This Matters

The gap here is not new, but the scale makes it impossible to ignore: a dataset license is a promise, and a download is a fact.

Once the files leave the host, the restrictions on the card have no mechanism behind them. No telemetry on how a file is used. No revocation. No audit. A researcher who agrees not to profile individuals and then does it anyway faces the same consequence as one who does not, which is none, absent a lawsuit nobody is positioned to bring. The card functions as liability transfer, not control.

That structure works passably when downstream users are institutions with reputations and compliance departments. It works not at all against the actors regulators actually named: builders of profiling tools, intelligence gatherers, and buyers of bulk personal data. Those actors do not read dataset cards for guidance. They read them for scope.

Meanwhile the economics have inverted. Scraping at this scale used to require a company. The cost of collection has fallen faster than the cost of enforcement, and no part of the current governance stack, whether platform terms, dataset licenses, hub moderation or privacy law, was built for a world in which one individual can do this in three weeks.

## What To Watch

Three things. First, whether Hugging Face acts on its own initiative rather than waiting for a notice. A proactive removal would signal how the hub reads its consent-centered policy when the aggrieved parties cannot show up to complain. Second, whether ByteDance treats this as a contract violation or as a reportable data incident, a distinction regulators have said can matter under notifiable-breach regimes. Third, and most consequential, whether any data protection authority opens an inquiry into the uploader directly. The 2023 joint statement was unambiguous that individuals who scrape publicly accessible personal information are themselves responsible for complying with privacy law. Testing that against a lone researcher, rather than a corporation, would be the first real answer to whether the rule means anything.

Until then, 4.5 billion records remain a click away, governed by a paragraph.