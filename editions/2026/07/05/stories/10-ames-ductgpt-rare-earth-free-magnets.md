At Ames National Laboratory, a physics-trained AI first built to design metals for fusion reactors is being turned loose on a different national problem: finding powerful permanent magnets that don't depend on the rare-earth elements the United States mostly buys from China.

The tool is called DuctGPT, and it is the work of Ames Lab scientist Prashant Singh, whose team built it on top of AtomGPT, a model originally developed at the National Institute of Standards and Technology. Fine-tuned on materials-science data, DuctGPT is a generative transformer — the same broad family of AI as chatbots — that lets a researcher describe the properties they need in plain language and get back candidate combinations of elements in seconds. It debuted for fusion, where the goal was ductile, heat-tolerant refractory alloys. Now Singh is extending the same physics-informed approach to one of the U.S. Department of Energy's most strategically loaded materials problems.

## How the workflow works

The premise is that raw data is not enough. Instead of training a model purely on past experiments — which can only predict within the range of what has already been made — Singh's group embeds the underlying physics of magnetism into the model: how a material's atomic structure and electronic behavior determine magnetization strength, resistance to demagnetization, energy storage, and performance at high temperatures.

"Understanding the physics of materials is important to include in AI frameworks when you are trying to design new materials. If you just use the data to train your models, you are going to get only the predictions within the range of information you have," Singh said. "But once you understand the physics of what controls specific properties, then you and your agentic tools or AI frameworks can search arbitrary material space."

The workflow pairs that physics-informed screening with high-throughput simulation, then hands promising candidates to Ames Lab's synthesis and testing facilities for confirmation. For DuctGPT's fusion work, queries run on an ordinary desktop rather than a supercomputer, which Singh says cuts discovery time "from months to days or hours." The magnet effort, published as a roadmap in Advanced Functional Materials and tied to DOE's Genesis Mission, aims to bring that same speed to magnetic materials — and to weigh cost and availability as it searches. "Supply chain conditions shift by the hour, material costs fluctuate, availability changes daily," Singh said. "By factoring those conditions into the discovery process, we can better target materials that are not only high-performing but also practical to produce and scale."

## Building on real magnet chemistry

The AI is not starting from nothing. In earlier work published in Chemistry of Materials, an Ames team built a machine-learning model to predict the Curie temperature — the point at which a material loses its magnetism — of new compounds, and tested it on magnets based on cerium, zirconium, and iron, all comparatively abundant, domestic elements. "The next super magnet must not only be superb in performance, but also rely on abundant domestic components," said Ames scientist Andriy Palasyuk, who proposed that test case. Senior researcher Yaroslav Mudryk called high Curie temperature "an important first step in the discovery of materials that can sustain magnetic properties at elevated temperatures."

Singh frames the lab's edge as data no rival has. "What sets Ames apart is seven decades of work in critical materials — a depth of knowledge no other lab can match," he said. "We have proprietary magnetic material data exclusive to Ames. Adding AI to that base lets us explore new materials and magnetic possibilities faster."

## Why It Matters

Rare-earth magnets — chiefly neodymium-iron-boron, often doped with dysprosium or terbium for heat resistance — are the invisible muscle inside EV motors, wind turbines, hard drives, and guided weapons. China dominates their production and processing, and in April 2025 it added seven rare earths to its export-control list, followed by broader restrictions in October, sending automakers and defense contractors scrambling. Washington responded in kind: in July 2025 the Defense Department took a roughly $400 million equity stake in domestic producer MP Materials, becoming its largest shareholder.

Against that backdrop, AI-accelerated materials discovery is being cast as a matter of national security, not just efficiency. If physics-informed models can compress a search that has run for more than 20 years on trial-and-error into a fraction of the time, they could widen the field of viable rare-earth-free magnets faster than any lab bench alone.

One caveat is worth stating plainly: some coverage has overstated the story. DuctGPT has not yet produced a proven rare-earth-free magnet, and Ames's magnet work is a published roadmap plus supporting models — a method for hunting candidates, not a finished replacement for neodymium magnets.

## What to Watch

Watch for Singh's group to report specific rare-earth-free candidate compositions that survive synthesis and testing, and for the magnet workflow to be released as an interactive, agentic tool the way DuctGPT was. The larger test is whether any AI-screened candidate reaches the performance and cost thresholds industry actually needs — and whether DOE's Genesis Mission can turn a promising method into magnets rolling off a domestic production line.