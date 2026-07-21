# Amazon's Custom Chip Business Passed a $20 Billion Run Rate, and Its Biggest Customers Are Nvidia's

Somewhere between the Prime Day promos and the warehouse robots, Amazon quietly became one of the three largest datacenter chip businesses on earth — and it did it without selling a single chip to anyone.

That is the strange, load-bearing fact underneath a number Andy Jassy dropped on Amazon's first-quarter earnings call in April and that Wall Street has spent the months since slowly digesting: the company's custom silicon operation — Graviton server CPUs, Trainium AI accelerators, and Nitro data-plane chips — is running above a $20 billion annual revenue run rate, growing at triple-digit rates year over year and roughly 40% quarter over quarter. All of it consumed internally, by AWS, on behalf of customers who rent the capacity rather than buy the parts.

“As best as we can tell, our custom silicon business is now one of the top three datacenter chip businesses in the world,” Jassy said on the call, adding the counterfactual that has become the most-quoted line of the quarter: “If our chips business was a standalone business and sold chips produced this year to AWS and other third parties as other leading chip companies do, our annual revenue run rate would be $50 billion.”

## The backlog is the story

The run rate is impressive. The order book is the part that should worry Santa Clara.

Jassy disclosed more than $225 billion in multi-year revenue commitments tied to Trainium. Unlike a bookings pipeline, these are contracted — and the names attached are precisely the customers Nvidia has spent three years courting. Anthropic has committed to securing up to five gigawatts of current and future Trainium generations, part of a multi-year arrangement tied to well over $100 billion in AWS spend. OpenAI, which spent most of the AI era as a Microsoft-and-Nvidia story, has committed to roughly two gigawatts of Trainium capacity, ramping in 2027. Meta signed on to deploy tens of millions of Graviton cores for agentic workloads. Uber moved real-time ride-matching onto Graviton4 and began piloting Trainium3 for dispatch and ranking models.

A caveat worth stating plainly: the shape of these commitments is uneven. The Anthropic and OpenAI deals are disclosed in gigawatts, not dollars, and capacity converts to revenue only as power and racks come online. Meta's commitment is to Graviton CPUs, not to AI accelerators — a real win, but not a Nvidia substitution. Uber's Trainium exposure was described at pilot scale as of April, with Graviton4 carrying the production workload. Secondary outlets have also published conflicting figures for the size of OpenAI's underlying AWS pact, ranging from $38 billion to $50 billion. And the $20 billion, the $50 billion hypothetical and the $225 billion all trace to one primary source: Jassy, on one earnings call. Treat them as management disclosure rather than audited segment reporting. Amazon does not break out the chip unit's profitability at all.

## Why customers are signing

The pitch is not that Trainium beats Nvidia's best silicon. It is that it does not have to.

“Our Trainium2 chip has about 30% better price-performance than comparable GPUs, and has largely sold out,” Jassy said. Trainium3, which began shipping at the start of 2026, is 30% to 40% more price-performant than Trainium2 and is nearly fully subscribed. Much of Trainium4, still roughly 18 months from broad availability, has already been reserved. On the CPU side, Jassy said Graviton delivers up to 40% better price-performance than any x86 processor and is now used by 98% of the top 1,000 EC2 customers.

Independent analyses put Trainium3 behind Nvidia's Blackwell B200 on raw dense throughput but competitive with the H200 — and materially cheaper per chip-hour. For workloads that are power-limited rather than FLOPS-limited, which is now most of them, that is an easy trade.

## Analysis: the erosion is structural, not competitive

The usual framing — Trainium versus Blackwell, challenger versus incumbent — misses what is actually happening. Nvidia is not losing a bake-off. It is losing the ability to set the price of its own alternative.

Amazon remains an enormous Nvidia customer; the same quarter that touted Trainium also announced plans to deploy more than a million Nvidia GPUs starting in 2026. But every gigawatt AWS fills with its own silicon is a gigawatt whose margin Amazon keeps, and every Trainium quote a customer can wave at a Nvidia sales rep is leverage. Nvidia's extraordinary gross margins were never purely a function of technology; they were a function of there being no credible substitute at scale. Google has TPUs, Microsoft has Maia, Meta is building its own training silicon. Amazon is furthest along at converting that bet into contracted revenue.

The bear case is real, and it is about capital rather than competition. Amazon expects roughly $200 billion in capital expenditures in 2026, and trailing-twelve-month free cash flow has collapsed to $1.2 billion from $25.9 billion a year earlier. A $225 billion backlog is only an asset if the demand behind it survives contact with an AI spending correction — and investor patience with unmonetized infrastructure is visibly thinning across the sector.

Motley Fool analyst Daniel Sparks framed the shareholder calculus about as cleanly as anyone: “I don't think Trainium needs to beat Nvidia for Amazon shareholders to win.”

## What to watch next

Three things. First, whether Amazon goes merchant. Reports that it is exploring direct sales of Trainium chips and full server racks to outside datacenters remain unconfirmed by the company; that decision would convert Jassy's $50 billion hypothetical into a real income statement and a real war with Nvidia. Second, Amazon's Q2 results, which will show whether the sequential 40% jump in the silicon unit was a step function or a trend line. Third, Nvidia's Vera Rubin ramp: if Rubin lands on schedule, Trainium's price advantage compresses fast. If it slips, the hyperscalers get another four quarters to entrench their own designs — and pricing power, once surrendered from the inside, is very hard to take back.
