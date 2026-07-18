For two years, the record industry has been trying to prove how Suno got its music. On Wednesday, a criminal did it for them.

404 Media reported on July 15 that a hacker breached the AI music generation startup and walked away with internal source code that appears to document, in the company's own engineering comments, where Suno's training audio came from: YouTube Music, Deezer, Genius, the stock libraries Pond5, Jamendo and Freesound, the sheet-music archive IMSLP, and podcasts pulled through RSS feeds.

The material is dated — Suno says it is "outdated source code that is no longer in use" — but its timing is the point. The Recording Industry Association of America has spent months alleging Suno obtained its training corpus by "stream ripping" audio out of YouTube in violation of the Digital Millennium Copyright Act. The leaked code, if authentic, speaks to the one question that theory turns on: not whether Suno copied music, which it has conceded, but how it got the files.

## What the code appears to show

The scale in the comments is the kind of number that usually only surfaces in discovery. One file inventories Suno's datasets: "113,879 hours of youtube_music," "152,162 hours of ytm_tagged," "62,117 hours of pond5_music," "19,514 hours of imslp," "17,615 hours of genius_hq," "12,287 hours of deezer," "3,726 hours of jamendo," plus smaller pulls from Freesound and MuseScore. A file named "youtube_music" logged 2,013,545 ingested music clips as of its last update. Another comment lists the intended sources — "genius_hq, youtube_music, freesound, jamendo, imp, deezer, ytm_tagged" — and notes "non-music will be filtered out."

Taken together, that is decades of audio. Pond5, a Shutterstock-owned library that sells tracks individually or by subscription, claims roughly 2.5 million music tracks; Suno's files suggest a substantial fraction of it. Genius doesn't host audio at all.

Two details matter more than the raw hours. Per 404 Media, some code searched YouTube specifically for a cappella versions — which is to say it hunted for isolated vocals. And the code indicates Suno routed its YouTube scraping through proxies sold by Bright Data, a commercial scraping vendor.

## Why the "how" is the whole case

Suno has never seriously contested the copying. In a court filing it said its training data "includes essentially all music files of reasonable quality that are accessible on the open internet, abiding by paywalls, password protections, and the like." Its defense is fair use — a fact-intensive doctrine that has gone both ways in AI litigation.

But the labels' amended complaint, filed in September 2025, added a claim fair use cannot touch. Section 1201 of the DMCA bars circumventing technological protection measures, independently of whether the underlying use infringes. If Suno defeated YouTube's rolling cipher to extract audio, fair use is no defense to the circumvention itself.

"For Suno specifically, this process involved copying decades worth of the world's most popular sound recordings and then ingesting those copies into Suno's AI models so they can generate outputs that imitate the qualities of genuine human sound recordings," the RIAA wrote in its complaint. "And to make matters worse, Suno obtained those copies in the first instance by unlawfully 'stream ripping' them from the popular streaming platform YouTube, and circumventing the technological measures designed specifically to prevent such unauthorized copying."

Suno moved to dismiss in October 2025, arguing YouTube's rolling cipher is a copy control rather than an access control, and that §1201 reaches only the latter. The court has not ruled; in the parallel Udio case, a judge declined in May 2026 to toss the equivalent claim. The labels seek $2,500 per act of circumvention, stacked on statutory copyright damages that can run to $150,000 per work — against a corpus the leaked files measure in millions of clips.

## The evidentiary irony, and a second problem

There is something uncomfortable here. Discovery is the mechanism the legal system built for exactly this question, and it has been grinding: Sony and UMG sued in 2024 over 560 works, then moved this spring to add more than 61,000 after discovery showed training on millions of their recordings. A stranger with stolen credentials produced a cleaner answer in an afternoon.

That is not a vindication of the hack. Stolen evidence carries real admissibility problems, and the hacker — who told 404 Media they had no particular motive, saying "I like to hack anything and everything" — is not a whistleblower by any definition the law recognizes. What the breach does is make the shape of the record harder to argue about.

The second problem is separate and touches more people. The intrusion dates to November 2025 and reached customer emails, phone numbers and Stripe payment details for what 404 Media describes as hundreds of thousands of users. Suno never told them. "Based on the limited nature of the customer information believed to be involved, we determined that individual notifications were not warranted under applicable privacy laws," a spokesperson said, adding that Suno "does not have access to customers' full credit card numbers in Stripe." Customers 404 Media contacted confirmed they had signed up with phone numbers and had never heard of a breach. State breach-notification statutes are not uniform, and that judgment call is the company's to defend.

## What to watch

Three things. Whether the labels try to put any of this in front of the court, and whether a ruling on the pending §1201 motion lands before fact discovery closes on September 30. Whether any state attorney general takes an interest in a November 2025 incident disclosed by a reporter in July 2026. And whether investors care: Suno raised a $400 million Series D on June 3 at a $5.4 billion valuation — up from $2.45 billion seven months earlier, on roughly $200 million in revenue and more than 7 million songs generated a day.

Warner Music settled and signed a licensing deal last November. Sony, UMG and GEMA did not. The gap between those two outcomes is now worth several billion dollars, and it may hinge on comments an engineer typed into a file in 2023.
