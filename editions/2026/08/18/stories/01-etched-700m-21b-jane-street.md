Etched, the San Jose chip startup founded by three Harvard dropouts, said Tuesday it has raised $700 million at a $21 billion valuation — a fourfold markup in eight months and a doubling in less than four weeks. The round was led by Jane Street, the secretive quantitative trading firm that is also Etched's first paying customer. Etched shipped its first rack of inference hardware to Jane Street last month, and the firm is now deploying it against live workloads inside its own data center.

The valuation curve is the sort that makes even seasoned AI investors blink. Etched was marked at **$5 billion in December 2025**. On July 23 it closed a $300 million Series C led by Sequoia at **$10.3 billion** — at the time the highest valuation ever attached to a Sequoia-led round. Twenty-six days later, investors doubled it again, adding nearly $11 billion of paper value in under a month. Total capital raised now stands at **$1.9 billion**, from a roster including Kleiner Perkins, Andreessen Horowitz, Tiger Global, Bain Capital Ventures, Blackstone, SK Hynix and Peter Thiel.

What changed between July and August was not a pitch deck. It was a delivery.

## From tape-out to trading floor

Etched sells what it calls frontier inference clusters — complete rack-scale systems rather than loose silicon, the same packaging strategy Nvidia uses for what it brands AI factories. The pitch rests on splitting inference into its two distinct phases and building purpose-designed hardware for each.

'Inference is built in two stages,' co-founder and COO Robert Wachen told TechCrunch, 'prefill and decode.' Prefill is the compute-intensive step in which the system ingests a prompt and its context. Decode is the memory-bound step in which the model emits output tokens one at a time.

For prefill, Etched built a chip that operates at low voltage, a technique it markets as Low Voltage Inference, letting it pack in more transistors and clock them harder without hitting the thermal ceiling that constrains conventional accelerators. For decode, it built a hybrid memory and interconnect subsystem it calls Cluster Scale Memory. 'It allows many chips to connect together and use a shared memory pool at a very, very fast, low latency,' Wachen said.

The execution record is unusually compressed for semiconductors. Etched hit first-pass silicon success on TSMC's N4P process in under three years from seed funding, and says it went from receiving test chips to running real inference workloads in **44 days**, against an industry norm of six months. It emerged from stealth on June 30 with a working chip, more than 400 employees and over **$1 billion in signed customer contracts** across frontier AI labs and clouds. Roughly 15% of its staff came from Nvidia.

Jane Street did its due diligence the hard way. 'We tested the chip and are pleased with the early results,' the firm said. 'Etched's unique approach to inference delivers the precision we will need to support our most demanding workloads. We're excited to now have our own rack running in our data center.' A quant shop that buys hardware, installs it, runs it, then leads a $700 million round is a different signal than a growth fund marking up a spreadsheet.

'We've felt the urgency to get our hardware into customers' hands and run real workloads since day one. Jane Street putting this cluster into production is proof of what we've built,' said Gavin Uberti, co-founder and CEO. 'Now, we're sprinting on scaling production for the rest of our customers.'

## Why this matters

For two years the received wisdom in venture capital was blunt. 'Don't back the kids in chips,' as Sequoia's Sonya Huang put it, describing the prevailing view before her firm led the Series C. 'In chips, startups are guilty until proven innocent.' Etched's counterargument is that its silicon worked on the first attempt — and that a customer rack humming in a data center is the only proof that clears the bar.

The bet underneath is that inference, not training, is where the money ends up. Bloomberg Intelligence pegs the inference market at **$1.3 trillion by 2032**, roughly double the training market, with inference expected to consume around 80% of AI compute load by 2030. Etched's own framing puts total AI infrastructure buildout at $7 trillion by the end of the decade.

'Inference is becoming one of the most important infrastructure markets in AI, and the winners will be measured by tokens per dollar and per watt,' said Mamoon Hamid, managing partner at Kleiner Perkins, who has backed Anthropic, Databricks and Together AI. 'Gavin, Rob, Chris, and the Etched team saw this early and have built at a pace rarely seen in semiconductors.'

There is a scoreboard element too. At $21 billion, Etched is now marked above the $20 billion Nvidia paid in December to license Groq's technology and hire its leadership — meaning the most valuable independent challenger to Nvidia's inference franchise shipped its first commercial rack seven weeks ago. Etched has also shed the narrative that dogged it early: the original Sohu design hard-wired transformer models into silicon. Current systems run any frontier model, with DeepSeek, Qwen, Mamba and Llama already in production.

## What to watch

The gap between one rack and a gigawatt is where chip startups historically die. Etched says it is building three hardware generations in parallel while converting its $1 billion order book into installed capacity — a supply chain problem involving TSMC allocation, advanced packaging and high-bandwidth memory, all of which Nvidia has locked up years ahead. Watch for the second and third customer deliveries, for independent benchmarks putting real tokens-per-dollar numbers against Nvidia's Blackwell and Rubin systems, and for whether any frontier lab among those contracts goes on the record.

'Our first deployment is a small step forward in our mission to run the world's inference,' Uberti said. 'It took us three years to deliver our first rack from scratch. Our next one will be much faster.'
