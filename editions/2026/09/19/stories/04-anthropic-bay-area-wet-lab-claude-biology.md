Anthropic, the company that spent last week urging the industry to slow down over risks including AI-enabled bioterrorism, has confirmed it is quietly operating a physical biology laboratory in the San Francisco Bay Area where its Claude models help run real experiments. The disclosure, first reported by Reuters on September 18 and confirmed by Eric Kauderer-Abrams, Anthropic’s head of life sciences, drops the AI lab into a debate it helped start: whether the people most vocal about biological risk should be the ones putting pipettes in the hands of their own models.

“We believe that to do biology, the final test is still and will be for a while in real lab work,” Kauderer-Abrams told Reuters. “We absolutely are doing that today.”

A company spokesperson followed up to say the facility is “not for drug discovery specifically,” then declined to elaborate. Anthropic later told TechCrunch the focus is fundamental biology. It would not disclose the lab’s size, headcount, opening date, or biosafety level, the last of which would say the most about what the room is equipped to handle.

## What ‘Claude tests biological theories’ actually means

Reuters reported, citing two people familiar with the effort, that Anthropic wants Claude to coordinate robotic laboratory equipment so experiments can run with minimal human intervention. In practice, that means a model proposing a hypothesis, writing the automation script that tells liquid handlers, plate readers and sequencers what to do and in what order, monitoring the run for errors, and feeding results back into the next round of design. The connective tissue is the Model Hardware Standard, the lab-instrument protocol Anthropic previewed in August with the Howard Hughes Medical Institute, which we covered in a prior edition.

The clearest public example is protein design. During evaluation of Claude Mythos 5.1 ahead of its release this month, the model generated 12 candidate protein binders, small molecules engineered to latch onto a specific target, and Anthropic reported a 50 percent hit rate when they were tested experimentally, against a typical 10 to 15 percent for protein design campaigns. A computer can score a design in silico; only a wet lab can tell you whether it actually binds.

On September 17, a day before the lab became public, Anthropic said Claude had optimized more than 30 open-source biology models in under four weeks, speeding them up roughly 4x on average, and that a single Claude instance with one GPU and 24 hours could now match its earlier binder-design results for about $150 in compute and tokens. The company is co-sponsoring a protein design competition with Adaptyv Bio that includes wet lab validation for more than 5,000 community designs.

“We’re in the very early innings of using AI to automate the execution of lab work,” Kauderer-Abrams said, calling it “an area that has the potential to bring about meaningful acceleration in so many different processes.”

## A year of quiet build-out

In April, Anthropic acquired Coefficient Bio, a stealth AI biotech with fewer than ten employees, for roughly $400 million in stock. The same month, Novartis chief executive Vas Narasimhan joined Anthropic’s board via its Long-Term Benefit Trust. Reuters reported that life sciences is now among Anthropic’s largest areas by headcount and spending.

Genentech and Bristol Myers Squibb use Anthropic’s tools, and Novo Nordisk agreed to a joint drug discovery arrangement two days before the lab surfaced. That explains the careful language. Kauderer-Abrams told Reuters the company is not competing with pharma and biotech firms that bring drugs to market, and Anthropic has drawn a line at running clinical trials for now.

On September 17, Anthropic launched its Life Sciences Verification Program, which gives vetted researchers access to Mythos, Opus and Sonnet models with looser biology safeguards than its generally available Fable models. Vetted applicants get either a Standard Use license, renewed annually, or a project-specific High-risk Use grant that removes all life-science blocks and must be renewed every six months. Anthropic said it has onboarded dozens of organizations and expects hundreds within the first week.

## Why It Matters

The strategic logic is simple: every frontier lab is chasing revenue that does not depend on chatbots, and biology is where Dario Amodei has staked his loudest claims, including the assertion last week that AI could cure most major diseases within five to ten years. A wet lab is the only way to convert a language model’s hypotheses into evidence a pharmaceutical partner will pay for. Owning that loop is what separates a tooling vendor from a research collaborator with proprietary data, and it is why a ten-person startup was worth $400 million to Anthropic.

The tension is equally simple. The same week Anthropic disclosed it had shut down suspected bioweapons-related activity by Claude users and its CEO called for the industry to pace itself, it confirmed a robot-operated biology facility running on its own models, with no public biosafety level. Asked how it squares the two, Kauderer-Abrams offered only that “we’re always balancing these things,” adding that deployment is managed carefully to reduce risk. Investor Chamath Palihapitiya was blunter on X, noting that the group warning about existential risk is now building a wet lab in San Francisco, and that he does not recommend it. For regulators deciding whether AI-driven biology is a lab-safety question or an AI-safety question, Anthropic has just made the case that it is both.

## What to Watch

The key unknowns are the lab’s biosafety classification and how much autonomy Claude actually has over instruments today. Watch for whether Anthropic publishes experimental results generated inside the facility, whether the Model Hardware Standard moves from research preview to general availability, and how quickly High-risk Use grants for Mythos expand beyond the small set of entities cleared with the US government. The Adaptyv competition, once 5,000 designs are physically validated, will be the first public scoreboard for how well Claude’s theories hold up at the bench.