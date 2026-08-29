The heaviest rainfall ever recorded in New York City measures 200 millimetres. A new machine-learning method out of MIT can hand a city planner a map of the storm that drops 300 — where it lands, how wide it spreads, how hard it falls — even though no such storm exists anywhere in the record the model was trained on.

That is the claim at the center of an open-access paper published Aug. 20 in Nature Communications by Kai Chang, a graduate student in MIT’s Department of Mechanical Engineering, and Themis Sapsis, the William I. Koch Professor of Mechanical and Ocean Engineering. Their method, Extreme Event Aware learning — shortened to eta-learning, after the Greek letter used in the paper — inverts the founding assumption of catastrophe modelling: that to simulate a disaster, you first have to have observed one.

“We are trying to model extreme, unprecedented events that no one has seen before, that are not in the dataset,” Chang says.

The gap is not academic. Insurers, grid operators and municipal engineers all want an answer to the same question — what does a once-in-a-century storm look like here? — and their tools are trained on datasets that must already contain century-scale events in order to learn what produces them. The historical record is thinnest exactly where the stakes are highest.

“An event like Hurricane Katrina is something that happens every 30 to 40 years,” Sapsis says. “What will be the Katrina that happens every 100 years? How bad will it be? That’s exactly what we’re trying to quantify, to help planners prepare for plausible extreme scenarios.”

## How it works

The method leans on a split that turns out to be unusually productive. Point statistics describe how often a single number — say, the maximum rainfall anywhere on a map — reaches a given level. Spatial maps describe how an event is distributed across a region. The first is cheap to collect over long horizons; the second is expensive and scarce.

Chang and Sapsis train on both, but not on the same slice of data. For their demonstration they pulled 25 years of hourly total precipitation over the continental United States from the ERA5-Land reanalysis, covering 1999 through 2023, and pooled it into 9,044 daily maps. From that full record they computed the point statistics: how frequently the map-wide rainfall maximum hits each level, tail included.

Then they deliberately starved the spatial half of the model. The map-to-map component was trained on paired low-resolution and high-resolution fields drawn from only the first six months of the record — roughly two percent of the data, a window containing few or none of the heaviest events. The algorithm learned how coarse patterns correspond to fine detail, and the long-run point statistics were then used to constrain how extreme that generated detail could become.

The result fits the observed spatial data while staying consistent with a prescribed distribution of extremes, including regions of it the model never witnessed. A conventional mean-squared-error map trained the same way simply flattens the tail — it ignores extremes entirely — while the eta-map reproduces the true tail beyond a quantile value of 150 and tracks sensible behaviour at thresholds from 154 up to 214. Correcting the tail also improved the fit in the bulk. Theoretical guarantees arrive by way of optimal transport.

The user-facing version of all this is a prompt. Ask what a once-in-a-century storm looks like for a named city and the model returns maps — each with its own footprint, coverage and intensity.

“Someone can say, ‘I’m interested in building things to withstand the risk of an event that happens every 100 years,’” Chang says. “What we can do then is produce thousands of possible realizations that will happen with this sort of rare frequency.”

## Analysis

Generative models are, by construction, conservative about their tails. Trained to reproduce a distribution, they generate near its mass and grow less reliable as you push outward — epistemic uncertainty is worst exactly where the risk lives. Most fixes involve finding more tail data. Eta-learning takes the opposite route: it treats a low-dimensional summary statistic as a hard constraint and lets that statistic drag the high-dimensional generator into territory the pixels never covered. That is a genuinely different answer to out-of-distribution generation, and it is portable to any domain where you can name an observable that indicates extremeness.

The commercial pull is obvious. Catastrophe modelling underwrites insurance pricing, reinsurance capacity and the siting of data centres and transmission lines. Those models are backward-looking in a climate that is no longer stationary — a hundred-year floodplain drawn from twentieth-century observations describes a world that has moved on. A method that generates plausible maps beyond the record gives stress-testers something to stress against.

The caveats are equally clear. The paper is candid that the eta-map gets the magnitude of extremes right while spatial localisation stays imperfect, because distribution-matching regularisation carries no explicit spatial guidance. In one test case it generated an extreme where the ground truth had none — defensible probabilistically, awkward if a planner reads a single sample as a forecast. And the apparatus is only as good as the prescribed tail: feed it a hypothesised distribution and it faithfully produces a heavier tail than reality contains. That flexibility is the feature and the failure mode at once.

Sapsis frames the stakes in supply-chain terms rather than meteorological ones. “A single extreme event propagates through supply chains, energy markets, and food systems in weeks,” he says. “Being able to put a probability on an event that hasn’t happened yet is now a question of national and economic resilience.”

## What to watch

Three things. Whether the method survives contact with hazards beyond precipitation — floods and wildfires each need their own point statistics and spatial data first. Whether the localisation weakness can be closed with added physical constraints, which is what stands between an interesting result and a tool an engineering firm will sign off on. And whether the non-weather applications land: Chang has flagged financial market crashes as a target. The work was funded in part by a Vannevar Bush Faculty Fellowship and the U.S. Air Force Office of Scientific Research — a sign the resilience-planning community is already watching.
