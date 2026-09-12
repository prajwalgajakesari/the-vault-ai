# A Robot Foundation Model Hit $100M in Revenue Ten Months After Its First Deployment

Ten months after Skild AI first loaded its software onto a robot inside a paying customer's facility, the Pittsburgh startup says that business is now running at $100 million a year.

Skild disclosed the milestone to *Bloomberg* on September 10, paired with a customer count that has gone from eight companies earlier in 2026 to more than 60. Its models run on hundreds of robots across manufacturing, logistics, inspection, security and food preparation — cafes in Japan, warehouses in the United States, and a Foxconn production line where dual-arm manipulators handle high-precision assembly of NVIDIA Blackwell systems. The company declined to name customers.

"This is a major milestone for us as it signifies a new chapter for robotics, moving from an era of demos to an era of deployments," said Deepak Pathak, Skild's co-founder and chief executive.

## What Skild Actually Sells

The product is not a program for one task. Skild sells what it calls the Skild Brain — a single model meant to run across many robot bodies and many jobs — and its newest version, **S1**, launched in an August 18 research post, is the reason the company is being talked about this week.

S1 is built as an *in-context learner*. An operator records a video of a person doing the task, hands it to the model as a prompt, and the robot attempts it. No retraining. No weight updates. In one plant-potting test, Skild's team went from recording the demonstration to autonomous execution on hardware in 11 minutes. The model has handled unfamiliar jobs running past ten minutes and dozens of manipulation steps: potting plants, brewing pour-over coffee, assembling kits, making pancakes.

"The first time it flipped a pancake, we could not believe it," Pathak told *TNW*, describing a task absent from the training data.

Skild puts S1 at **96% success on tasks it has seen** during pretraining and **66% on tasks it has not** — the latter roughly seven times better than a language-prompted baseline that managed 9%. The company also estimates that a single demonstration video does the work of about 380 hands-on training episodes, a volume it says would take a person 50 to 100 hours of teleoperation to collect.

The research ran on NVIDIA infrastructure, part of a collaboration spanning synthetic data generation, simulation and real-world deployment. "Learning by experience, and not preprogramming, is the step change that has happened in robotics," Pathak said in an NVIDIA post published the same day.

## The Money Behind It

Skild raised roughly **$1.4 billion in January 2026** at a valuation above **$14 billion** — more than triple the $4.5 billion it carried seven months earlier. SoftBank led the round; NVentures, Macquarie Capital, Jeff Bezos, Samsung, LG, Schneider and Salesforce Ventures participated. The company was founded by Carnegie Mellon researchers Deepak Pathak and Abhinav Gupta.

Gupta, now Skild's president, told *TNW* last month that 2025 revenue was around **$30 million**. Skild has also been buying rather than only selling: in April it acquired Zebra Technologies' robotics automation business, a detail Bloomberg's account did not mention.

## What the 96-to-66 Gap Actually Means

The headline number that matters here is not $100 million. It is 66%.

That figure is the strongest public evidence to date that a robot foundation model generalizes to work it was never trained on — and it is also the reason to stay cautious. Read NVIDIA's description carefully and S1 succeeded about 66% of the time *at each step* of a new multistep task. On a twenty-step assembly, naive compounding takes that to effectively zero. Skild's answer is that the model recovers from errors and re-plans when objects move, which breaks the compounding math. But the company has not published task-level completion rates on unseen long-horizon work, and that is the number a factory buyer actually underwrites.

The 30-point drop from seen to unseen is the honest measure of how far generalization has come. A 96% model on known tasks is a very good automation product. A 66% model on novel ones is a research result that is *becoming* a product. The gap is the distance the entire field still has to close, and Skild is simply the first company to put a price on it.

Then there is the multiple. **$100 million against a $14 billion valuation is 140x revenue** — rich even by 2026 AI standards, and richer than it first looks. Run rate is an annualized snapshot, not booked revenue. S1 only shipped in August, which means most of that $100 million was earned by predecessor deployments and, plausibly, by the acquired Zebra automation business, which carries integration-services economics rather than software margins. Going from eight customers to more than 60 inside a year is genuinely fast. Whether those 60 renew and expand is the thing nobody can see yet.

The competitive picture complicates it further. Physical Intelligence is shipping steadily more general vision-language-action models. Figure has raised more than $1 billion at a $39 billion post-money valuation. And NVIDIA — Skild's compute partner and, through NVentures, an investor — gives away GR00T N1.7, an openly licensed 3-billion-parameter VLA that lowers the floor for every hardware maker that might otherwise buy a brain. Skild's moat has to be deployment data, not architecture.

## What to Watch

Three things. First, whether Skild publishes task-completion rates rather than per-step rates on unseen work; that disclosure alone would settle most of the generalization argument. Second, renewals — eight-to-60 is a land number, and the expansion number arrives next year. Third, Brussels. Europe's Machinery Regulation replaces the machinery directive on **January 20, 2027**, covering machinery with self-evolving behaviour for the first time and requiring assessment by a notified body rather than a manufacturer's own declaration. A model whose entire selling point is performing work absent from its training data sits close to the center of that definition. Nobody has been assessed under it yet. Skild has not said whether it sells into Europe.
