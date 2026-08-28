For two years, the story of AI scarcity had a single face: the GPU. On Thursday, Kioxia and Sandisk made the case that it now has another. The longtime joint-venture partners announced they anticipate investing more than $31 billion — roughly 5 trillion yen — in Japan through 2032, expanding flash-memory production and funding next-generation semiconductor technology. It would rank among the largest memory commitments ever made in a single country. It is also, in the companies' own wording, "contingent upon government support."

The money runs through the two sites that have defined the partnership for a quarter century: the Yokkaichi Plant in Mie Prefecture and the Kitakami Plant in Iwate. The single largest piece is a new fabrication facility at Kitakami, priced at about 1.8 trillion yen — roughly $11.3 billion — and targeted to begin operating in the fiscal year starting April 2029. That would be the site's third fab. Its second, Fab2, only entered production in September 2025.

The two companies have already put more than $50 billion, about 9 trillion yen, into Japan over the past 25 years through a joint venture that is, by almost any measure, one of the most durable in the semiconductor industry. In January they extended the Yokkaichi JV framework through December 2034. Thursday's announcement is the capital plan that framework implies.

"This joint investment further strengthens our longstanding partnership with Sandisk and underscores Kioxia's strong commitment to contributing to the advancement of an AI-driven society," said Hiroo Ota, President and CEO of Kioxia. He was notably direct about the conditionality: "We sincerely appreciate the support of the Japanese government to date and recognize the importance of its continued strategic support in maintaining further strengthening our global competitiveness."

Sandisk framed it as geopolitics as much as capex. "For decades, Sandisk and Kioxia have jointly developed world-class NAND flash memory technology," said David Goeckeler, Chairman and CEO of Sandisk. The planned spending, he said, would provide "new economic opportunities for the communities we operate in" while "serving as a premier example of U.S.-Japan economic collaboration." Ota and Goeckeler met Prime Minister Sanae Takaichi in Tokyo on the day of the announcement; she called the plans "very encouraging" and said the government "strongly welcomes them."

## What is actually committed

Less than the headline suggests. The release describes "anticipated" investments. The companies did not disclose how the $31 billion splits between them, did not name a subsidy figure, and did not commit to a spending schedule beyond the 2029 Kitakami start. A welcome from the prime minister is not a budget line.

The precedent is worth holding up against the number. In February 2024, the same joint venture — then with Western Digital — secured up to 150 billion yen in Japanese government subsidies for these same two plants. That is roughly 3% of the sum now on the table. Tokyo has treated advanced semiconductors as a strategic economic and national-security priority and has written very large checks for Rapidus and TSMC's Kumamoto fabs, so the money is plausible. It is not yet appropriated.

## NAND is not HBM

Here is where precision matters, because the announcement is being read as a fix for a bottleneck it does not touch.

High-bandwidth memory — the stacked DRAM sitting on the same package as an AI accelerator — is the constraint strangling GPU output right now. It is made by SK hynix, Samsung and Micron. Kioxia and Sandisk make neither DRAM nor HBM. They are pure-play NAND flash producers. Thirty-one billion dollars at Yokkaichi and Kitakami buys flash bits and the cleanrooms to make them. It does not add a single HBM stack.

That does not make it irrelevant, because AI has become memory-hungry at every tier at once. Model weights and KV caches — the per-token attention state that grows with context length and with the number of concurrent users — live in HBM, and running out of it is why inference providers cap context windows and batch sizes. But everything one layer down lands on flash: training checkpoints for trillion-parameter models, written repeatedly at terabyte scale; multi-petabyte training corpora; vector indexes for retrieval; and, increasingly, KV-cache offload, where prefix caches spill from HBM to NVMe so a long conversation does not have to be recomputed from scratch. Industry estimates put roughly 16TB of NAND behind each high-end AI GPU and on the order of 1,150TB behind a standard AI server rack.

The two bottlenecks are also linked by the physics of the fab floor. As DRAM makers reallocated cleanroom space and capital toward higher-margin HBM, conventional DRAM supply tightened, and buyers pushed demand down the stack onto flash. TrendForce has NAND contract prices rising 55-60% quarter over quarter in Q1 2026 and 70-75% in Q2; conventional DRAM was revised up to 90-95% in Q1. Consumer 1TB SSDs that sold near $45 in late 2025 now clear around $90. This is not a normal cycle. It is a reallocation of the world's wafer capacity toward AI.

## What to watch

Three things. First, whether Japan's Ministry of Economy, Trade and Industry converts Takaichi's enthusiasm into an actual subsidy line, and how large — that determines whether the 2029 Kitakami fab is real. Second, memory contract pricing through the back half of 2026: if NAND and DRAM increases hold at these rates, every AI buyer's cost structure resets upward, and capacity announced today does not arrive until 2029 at the earliest. Third, Nvidia's gross margin. The company's supply commitments more than doubled to $279 billion last quarter, with as much as $160 billion earmarked for memory, and management guided margins down to 74% this quarter and a 71-72% trough after that.

The GPU shortage taught the industry to build fabs. The memory shortage is teaching it that a GPU without something to feed it is an expensive space heater. Nvidia is currently eating that squeeze in its margins. Kioxia and Sandisk are betting it will not be the last company that has to.
