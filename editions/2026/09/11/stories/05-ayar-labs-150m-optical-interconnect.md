# Nvidia, AMD and Intel All Backed the Same Startup. It Sells Light.

In an industry where Nvidia, AMD and Intel spend their days trying to take share from one another, there is one San Jose company all three have quietly written checks into. Ayar Labs Inc. does not build a GPU, a CPU or an AI accelerator. It builds the thing that connects them — and it builds it out of photons.

On Sept. 10, Ayar Labs said it had raised an additional **$150 million** from an undisclosed investor, extending the Series E it closed in March and lifting the primary capital it has raised in 2026 to **$650 million**. Total outside funding now stands just above **$1 billion** for a company founded in 2015 that did not raise meaningful venture money until 2020, when it took in $35 million. A concurrent **$225 million secondary** sale of existing shareholder stock priced the company above **$5 billion**, roughly 33 percent above the $3.75 billion valuation set by the March round. Neither the company nor its announcement disclosed a revised valuation on the primary round itself.

The March round was a $500 million Series E led by Neuberger Berman, with Alchip Technologies, ARK Invest, Insight Partners, MediaTek, the Qatar Investment Authority, Sequoia Global Equities and 1789 Capital joining existing backers. The strategic roster is the striking part: AMD, Intel, MediaTek, Nvidia, Alchip and, disclosed for the first time this week, Taiwanese data center manufacturer Wiwynn Corp.

“Copper interconnect is becoming the limiting factor for AI scale-up,” said co-founder and Chief Executive Mark Wade. “This funding allows us to move faster on manufacturing-ready co-packaged optics at scale. We're deepening our work across the foundry and packaging ecosystem and growing our engineering capacity to support customer programs worldwide.”

## What Ayar Labs Actually Sells

The product is called **TeraPHY**, an electro-optical chiplet that sits inside the same package as an accelerator or switch ASIC, paired with a remote laser module called **SuperNova**. Instead of driving electrical signals down copper traces and cables, the chiplet converts data to light at the edge of the compute die and pushes it onto fiber.

The performance numbers are the argument. Ayar Labs has demonstrated commercial-grade optical I/O at **4 Tbps** using eight 256G optical ports, and its earlier terabit-class links ran at roughly **5 picojoules per bit** — an efficiency figure DARPA's PIPES program, which funded early work in the field, wants to push below 1 pJ/bit at more than 100 Tbps per package. The rack-scale reference architecture Ayar Labs announced with Wiwynn in March scales to **1,024 accelerators**, each carrying more than **100 Tbps** of optical connectivity under liquid cooling.

The new money goes toward making that manufacturable rather than demonstrable. Ayar Labs said the capital funds product development, validation, manufacturing-ecosystem readiness and volume production prep, plus a new **Bengaluru Design Center** joining engineering sites in the U.S. and Hsinchu, Taiwan.

Wade told *Reuters* the clock is the real constraint. “We build the optical chip, and our optical chip gets fed into the customer's product,” he said. “If my customer's products are looking to ramp in the 2028-2029 time frame, we have to have all of our stuff qualified for volume production by the end of 2027.” Mass-market availability, he said, arrives in early 2028.

## Why Three Rivals Funded the Same Supplier

The bet rests on a physical wall, not a market forecast.

AI training clusters are built in two dimensions. **Scale-up** is the tightly coupled domain — the accelerators that behave like one giant chip, sharing memory over very fast, very low-latency links. **Scale-out** is the looser Ethernet or InfiniBand fabric stitching those domains into a cluster. Scale-up has historically been copper, because copper over 30 centimeters is cheap, reliable and effectively free in power terms.

Copper fails on three axes at once as that domain grows. Signal integrity degrades with distance, so reach caps out around a rack. Power per bit climbs steeply as aggregate bandwidth rises, and at thousands of GPUs the drive energy becomes a line item nobody can defend. And dense copper bundles run hot next to high-power processors.

The result is that the scale-up domain has been pinned to roughly the size of a rack. Optical I/O is the mechanism for unpinning it — for making multiple racks behave like a single coherent compute domain rather than a cluster connected through conventional networking. That is why *every* accelerator vendor wants it, and why none of them wants to be the only one without it.

That explains the unusual cap table. Nvidia, AMD and Intel are not investing in Ayar Labs to beat each other; they are each buying optionality on a component that determines how large their own products can scale. Nvidia is simultaneously building its own silicon photonics switches and has pulled Ayar Labs into the NVLink Fusion ecosystem, which it joined in June — alongside rival Lightmatter, which joined the same program weeks earlier. Broadcom is pushing its own co-packaged Ethernet switches. Celestial AI, the other well-funded independent, was acquired in December 2025 for $3.25 billion, rising to $5.5 billion with earnouts. Ayar Labs is now the largest independent left standing, which is precisely what makes it valuable to chipmakers who would rather not buy their interconnect from Nvidia or Broadcom.

## What to Watch

The demonstrations are done. The open question is yield, test cost and packaging throughput — whether optical engines can be fabricated, fiber-coupled, burned in and integrated at semiconductor volumes and semiconductor economics. Wade's own end-of-2027 qualification deadline is the metric that matters; miss it and customer ramps in 2028-2029 slip with it.

Watch three signals over the next eighteen months: whether a named hyperscaler or accelerator vendor commits publicly to TeraPHY in a shipping product, whether the Bengaluru and Hsinchu build-out translates into parallel customer programs rather than headcount, and whether the >$5 billion secondary mark holds when the next primary round prices. A $1 billion war chest buys Ayar Labs time. It does not buy it a manufacturing line.
