Amazon Web Services will deploy 2 million additional Nvidia GPUs across its global infrastructure in 2027 and 2028, the companies announced Wednesday - roughly double a commitment AWS made only months ago, and by some distance the largest single customer allocation Nvidia has ever disclosed.

The more interesting sentence came four sections later, under a heading most coverage skipped: Amazon's Annapurna Labs will build future Trainium chips using Nvidia's custom high-bandwidth memory. The chip Amazon has spent years positioning as the affordable alternative to Nvidia will now reach for Nvidia's memory architecture, and Nvidia's interconnect, to hit its performance targets.

## What was actually announced

The 2 million figure covers Blackwell Ultra, Rubin and Rubin Ultra parts, deployed across AWS Global Infrastructure including what both companies now call AI factories. It stacks on top of the more than 1 million GPUs AWS committed to at Nvidia GTC earlier this year. The stated reason for the upgrade is blunt. "Since then, demand has exceeded those expectations," the release says.

"Customers want the freedom to choose the best tools for their AI workloads, and they want confidence that everything works seamlessly together," said Matt Garman, CEO of AWS. "That's why we've invested deeply with NVIDIA to make AWS the best place to run NVIDIA AI technologies, optimizing performance across our infrastructure from networking and security to deployment."

Jensen Huang was less diplomatic about who is driving whom. "NVIDIA and AWS have built one of the great growth engines of the AI era, and demand is running ahead of every forecast," the Nvidia founder and CEO said. "This expansion reflects customers' demand for NVIDIA's platform on AWS."

Read that last line twice. It is a supplier telling a cloud provider's customers, in the cloud provider's own announcement, that they asked for Nvidia by name.

The rest of the package is substantial. Nvidia Vera CPUs are coming to AWS for agentic workloads that need heavy CPU alongside accelerators. RTX PRO 4500 Blackwell Server Edition GPUs land in new EC2 G7 instances, which AWS says deliver 4.6x the inference performance of G6. Nemotron open models stay on Bedrock and SageMaker. cuDF-accelerated processing on EMR claims 3.7x faster speeds and 30% better price-performance, and GPU vector indexing on OpenSearch claims 9x faster indexing at a quarter of the cost. Amazon Robotics is adopting Nvidia's Jetson, Omniverse and Isaac stack for warehouse automation.

Then the government tranche: AWS and Nvidia plan to build AI factories for the U.S. government, including 100,000 GPUs on AWS secure infrastructure for federal and national-security workloads classified at Impact Level 6 and above. Both releases say "plan to." There is no contract value, no named agency, no timeline.

## The Trainium problem

Amazon has told a consistent story since Trainium2 shipped: use Nvidia if you must, but AWS silicon gives you better price-performance, and AWS controls its own supply. Andy Jassy said on the Q2 2026 earnings call that the chips business now runs above a $25 billion annual revenue run rate, growing triple digits year over year. Anthropic runs Claude on more than a million Trainium2 chips and has committed to up to five gigawatts. OpenAI committed to two gigawatts of Trainium capacity beginning in 2027.

Those are real numbers. They are also bundled. The $25 billion covers Trainium, Graviton and Nitro together, and Graviton is a mature general-purpose CPU line used by 98% of the top 1,000 EC2 customers and carrying more than half of all new compute AWS adds. Amazon has never broken out Trainium on its own. Set the bundled figure against AWS revenue of $42.2 billion in Q2 alone and custom silicon of every kind is meaningful, but nowhere near displacing the incumbent.

The honest reading is not that Trainium failed. It is that hyperscalers run two books. Custom silicon serves internal workloads, anchor tenants negotiating multi-gigawatt deals, and price-sensitive inference. Nvidia serves everyone else - the enterprises, the startups and the frontier labs whose code is written against CUDA and who will not port it for a 30% discount. AWS is not choosing between them. It is billing both.

What changed this week is the direction of the plumbing. NVLink Fusion support in next-generation Trainium was announced at re:Invent 2025. NVHBM is the escalation. Amazon's differentiated accelerator now taps Nvidia memory technology inside a common rack-scale architecture shared with Nvidia GPUs. That is a strategic concession packaged as a partnership win.

## What 2 million GPUs implies

Neither company attached a dollar figure, so here is the arithmetic. Rack-scale Blackwell systems price out somewhere in the range of $40,000 to $55,000 per GPU before land, power and cooling. Two million GPUs is therefore roughly $80 billion to $110 billion in accelerator systems alone, spread across two years. Amazon has already guided 2026 capex to about $220 billion, a $20 billion increase it attributed largely to memory costs - the same memory inflation Nvidia flagged in its own results a day earlier.

Power is the harder constraint. Blackwell Ultra parts draw well over a kilowatt each and Rubin Ultra will draw more. At a conservative two kilowatts per GPU including networking and cooling overhead, 2 million GPUs implies something near four gigawatts of continuous demand. For scale, Anthropic's entire Trainium agreement with Amazon tops out at five gigawatts. AWS is committing to Nvidia capacity in the same order of magnitude as its single largest custom-silicon customer commitment, and it has about 24 months to find the electricity.

## What to watch

First, whether AWS ever breaks out Trainium revenue separately. While it stays bundled with Graviton, the custom-silicon narrative is effectively unfalsifiable.

Second, whether the 100,000-GPU federal deployment converts into a named, funded program. IL6 build-outs are slow and expensive, and "plan to" is carrying a lot of weight in both releases.

Third, whether the 2027-2028 window holds. AWS revised its previous GPU commitment upward within months. The next revision will tell you whether demand is still outrunning forecasts, or whether the forecasts finally caught up.
