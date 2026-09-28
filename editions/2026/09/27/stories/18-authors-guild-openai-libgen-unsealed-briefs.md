# Unsealed Briefs in Authors Guild v. OpenAI Allege Executives Knew LibGen Use Was Legally Risky

OpenAI's own Slack messages now sit at the center of the biggest book-copyright fight in AI. Newly unsealed filings from the authors suing OpenAI and Microsoft allege that researchers and executives knew the pirate library Library Genesis, or LibGen, was a legally and reputationally risky source. The filings say staff trained early GPT models on it anyway, gave it a vague name in a research paper, and later deleted it in a cleanup effort called "Project Clear."

These are allegations. They come from the plaintiffs' motion for partial summary judgment, not from any ruling. The case is the authors' class action, *Alter v. OpenAI and Microsoft*, which is part of the multidistrict litigation over OpenAI and copyright that Judge Sidney Stein is overseeing in the Southern District of New York. No court has decided whether OpenAI's conduct was unlawful.

## What the Filings Allege

On September 17, the class plaintiffs filed a memorandum supporting partial summary judgment and a 162-page Rule 56.1 Statement of Undisputed Material Facts. Both quote internal messages, emails, presentations and deposition testimony, most of it dated 2018 to 2022. The named plaintiffs include the Authors Guild, George R.R. Martin, John Grisham, Jodi Picoult, Jonathan Franzen, David Baldacci and Michael Connelly. According to coverage of the filings, the motion covers 194 of their books.

The numbers in the brief are large. It alleges that an OpenAI researcher downloaded about 117,500 books from LibGen in late 2018. Between September 2019 and January 2020, it says, employees torrented about 35 terabytes from the site, which the plaintiffs say matches LibGen's full collection of roughly 4.6 million books. A document that Sam Altman allegedly shared with Bill Gates in April 2019 said OpenAI had "added another ~11B words from Library Genesis (LibGen)." Microsoft invested $1 billion two months later. The Authors Guild says Microsoft therefore knew about the LibGen use "as early as April 2019," because Microsoft CTO Kevin Scott also received the presentation.

The line that sent the story to the top of Hacker News dates from July 2019. According to the brief, OpenAI researcher Sam McCandlish wrote: "I was just worried about optics – i.e. 'openai uses copyrighted data from sketchy russian website' showing up on [Hacker News] would be unfortunate." Dario Amodei, then OpenAI's research director and now Anthropic's CEO, allegedly replied that "as a training set [LibGen is] a bit sketchier."

The plaintiffs also allege that OpenAI hid the source when it published the GPT-3 paper in May 2020, where the LibGen-derived sets appeared as "Books1" and "Books2." In May 2020, according to the filing, Amodei asked colleagues in Slack whether it was "sketchy" to use those names "and not say what they are." An employee allegedly explained that one description was "deliberately vague since it's libgen."

The deletion comes next in the brief's account. On June 15, 2022, VP of Research Bob McGrew allegedly wrote: "Given how much OpenAI is in the news, now is the right time to excise Libgen from our systems and storage." The plaintiffs say the Slack channel for the work, first named #excise-libgen, was renamed #project-clear. They also say McGrew acknowledged that removing the data would stop OpenAI from reproducing GPT-3 or GPT-3.5 "but would be very valuable for legal reasons." According to the brief, these are the only two training corpora OpenAI has ever deleted.

The Authors Guild did not hold back. CEO Mary Rasenberger said the filings "reveal shocking disdain for writers and their work through repeated, intentional decisions to steal books rather than pay for them with full knowledge that their products will destroy the careers of authors."

## OpenAI's Position

In the coverage reviewed for this story, we found no new public statement from OpenAI about the unsealed messages. Its position in the case is set out in its own summary judgment motion, filed with Microsoft on September 4. That motion argues the use was fair because it was "highly transformative" and says ChatGPT has "an alleged regurgitation rate of 0.00007%." According to the defendants, the longest continuous passage the plaintiffs' expert could extract was a 1,899-word section of *A Game of Thrones*, or 0.62% of the book. OpenAI and Microsoft rely on the fair-use wins in *Authors Guild v. Google* and *Kadrey v. Meta*.

## Why It Matters

The authors are trying to recreate the argument that worked against Anthropic. In *Bartz v. Anthropic*, Judge William Alsup ruled in June 2025 that training on lawfully purchased books was fair use but that keeping pirated copies was not. Anthropic then settled for $1.5 billion, about $3,000 per book. That split between how a company acquired its data and what it did with the data is the core of the authors' strategy here. They argue that the download itself was the infringement, whatever the models later produce.

That is why the Slack messages matter. Fair use is a legal question, but willfulness affects damages, and statutory damages for willful infringement can reach $150,000 per work. If a court accepts that employees saw LibGen as risky and hid it, OpenAI's exposure could be much larger than its fair-use arguments suggest. The filings also involve Microsoft directly, which weakens any claim that the company was a passive investor.
## What to Watch

The Authors Guild says more briefing will come over the next couple of months, with a hearing expected in early 2027. Watch for OpenAI's and Microsoft's replies to the plaintiffs' statement of facts, which will show which of these characterizations they dispute. The key question is whether Judge Stein treats acquisition from LibGen separately from training, as Judge Alsup did. If he does, the Anthropic settlement could become the benchmark for a much larger OpenAI payout, and every AI lab with shadow-library data in its history will need to recheck where its training data came from.
