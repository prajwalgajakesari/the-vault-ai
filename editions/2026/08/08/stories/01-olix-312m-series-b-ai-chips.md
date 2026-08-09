A two-year-old London chip startup has become one of Europe's most richly valued semiconductor bets, raising $312 million and more than tripling its worth in just six months.

OLIX Computing said on August 3 that it had closed a $312 million Series B financing round at a $3.3 billion valuation, roughly €270.5 million at a €2.8 billion valuation. The round was led by Fundomo and drew participation from chip-IP giant Arm, the quantitative trading firm Hudson River Trading, and Netflix co-founder Reed Hastings as an angel investor. In a notable signal of state ambition, the UK government's newly created "Sovereign AI" venture fund also disclosed an investment. Existing backers, including Hummingbird Ventures, Crane, Plural, Creandum, Phoenix Court and Transition, all increased their commitments.

The raise lands barely six months after OLIX collected $220 million at a $1 billion valuation in February, a round led by Hummingbird Ventures. The company, founded in London in 2024 by 25-year-old James Dacombe, has vaulted from unicorn to a $3.3 billion price tag in the span of two quarters, an ascent that captures both the frenzied appetite for AI hardware and investors' hunger for a credible challenger to Nvidia's inference dominance.

## A different bet on inference

OLIX is building chips for AI inference, the stage where trained models actually run and generate output, rather than for training. Its pitch is that the industry has hit an efficiency wall by running every step of the job on the same general-purpose silicon.

"A datacenter is a factory whose product is the token," the company said in describing its approach. "Producing a single token takes hundreds of operations, each placing different demands on hardware. Any other factory would give each stage a machine built for it. Instead, the token factory runs every stage on the same general-purpose chip."

Its answer is the X-1 platform, which "unrolls" a model across a large number of chips so that each handles a single part of the workload, in effect a production line for tokens. The chips are stitched together by what OLIX calls a "slow and wide" optical interconnect that moves data die-to-die using light instead of copper, allowing as many as 10,000 chips to be linked into a single multi-rack scale-up domain. The first product, a decode accelerator called DX-1, holds models in fast on-chip SRAM rather than high-bandwidth memory, and uses no advanced packaging, the two components in shortest supply across the industry. For 100-billion-parameter models, OLIX says DX-1 can deliver more than 10,000 tokens per second per user at higher throughput per watt than general-purpose chips, and that the architecture scales to models of 10 trillion parameters and beyond.

The money is earmarked to get DX-1 into the hands of first customers by the second half of 2027 and to build out the wider custom silicon platform, along with the manufacturing and supply-chain commitments that scaling frontier hardware demands. OLIX is hiring across silicon, photonics, compiler and systems engineering in London, Bristol, Austin, Toronto and San Francisco.

Alongside the round, the company beefed up its leadership. It named Professor Nick McKeown, the Stanford academic who co-invented software-defined networking, OpenFlow and P4 and won the 2025 Marconi Prize, to its board of directors. It also hired Matt Briers, who spent nine years as chief financial officer of the fintech Wise and took it through its 2021 London listing, as CFO. Dacombe, for his part, is also chief executive of CoMind, a brain-monitoring startup he founded as a teenager that has raised $100 million to date.

## Why it matters

The deal is as much a political statement as a commercial one. By putting taxpayer money into OLIX through its Sovereign AI fund, the UK is signaling that it wants a domestic stake in the physical layer of the AI stack, not just in the models and applications built on top of it.

"The future of AI will be built on chips that power models. Countries that build chips will build leverage," said Kanishka Narayan, the UK's AI Minister. "Olix is exactly the kind of ambitious company we want to back through Sovereign AI. In just two years, it has established itself as one of the UK's most exciting AI startups, developing breakthrough chip technology with the potential to help shape the future of AI."

OLIX is wagering that the economics of inference, now the dominant and fastest-growing slice of AI compute spending, will reward specialized architectures that sidestep the HBM and advanced-packaging bottlenecks throttling GPU supply. Arm's participation lends technical credibility, while Hudson River Trading's involvement reflects how latency-obsessed trading firms have become early adopters of novel silicon.

## What to watch next

The hard part is still ahead. OLIX has a valuation that assumes execution, but no shipping product until at least late 2027, and it must prove that photonic interconnects and an SRAM-only design can hold up against Nvidia, AMD and a crowded field of inference-chip startups. Watch for tape-out milestones on DX-1, named customer commitments, and whether the UK's Sovereign AI fund treats OLIX as a one-off or the template for a broader industrial policy in silicon.
