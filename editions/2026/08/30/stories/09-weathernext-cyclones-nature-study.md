Google DeepMind published in Nature on August 6 the peer-reviewed case for a model that had already been in operational use for more than a year. WeatherNext Cyclones, evaluated against historical storms from 2023 to 2025, beat the leading physics-based systems on all three quantities that matter to a hurricane forecaster: where the storm goes, how strong it gets, and how far its damaging winds extend. Averaged across those measures, the model bought forecasters more than 24 hours. Its three-day forecast was about as accurate as what the best operational guidance had been delivering at two days.

That is a large step in a field that moves in increments. DeepMind and its co-authors, who include forecasters from the National Hurricane Center, the UK Met Office and Colorado State's Cooperative Institute for Research in the Atmosphere, put the jump at roughly a decade's worth of progress against the historical trend line.

The specific numbers: at five days, WeatherNext Cyclones recorded an average track error of 230 kilometres, against 370 km for ECMWF's ENS ensemble, the global reference system, and 335 km for GenCast, DeepMind's own general-purpose ensemble. At three days, position error fell to roughly 100 km. On intensity, historically the harder problem, the model logged an average three-day error near 11 knots, ahead of NOAA's high-resolution regional HWRF system. It has been running in real time since June 2025.

## Two problems, one model

The technical claim underneath the numbers is that WeatherNext collapses a trade-off forecasters have lived with for decades. Track is governed by continental-scale steering currents, best captured by coarse global models; intensity by thermodynamics inside the storm's core, a few tens of kilometres across, which has demanded high-resolution regional models. No single system did both well.

**"Tropical storms and hurricanes can change very quickly in terms of their structure and their intensity, which makes them more challenging to predict than other types of weather systems,"** said Michael Brennan, director of the National Hurricane Center.

WeatherNext Cyclones was co-trained on two data sources at once: roughly 20 terabytes of global atmospheric reanalysis, and IBTrACS, the expert-curated archive of nearly 5,000 observed storms going back to 1980. It runs on input at 28x28 km resolution, roughly 100 times coarser than the regional models it outperforms on intensity, a result the authors concede they cannot fully explain and flag as an open research question. A compact variant, WeatherNext 2-mini, works at 111x111 km and still performs competitively.

The other half of the design is probabilistic. Rather than a single track, the model uses Functional Generative Networks to produce a spread of scenarios. In the 2025 season it generated 50 members per storm, matching the ensemble size of physics-based systems; this year DeepMind scaled to 1,000. Because a 15-day forecast takes under a minute on a single TPU, ensemble size is cheap in a way it is not for physics simulations, and large ensembles are what let forecasters attach probabilities to tail risks such as rapid intensification.

**"They're very hard to predict because complex interactions make their path and intensity chaotic. So we think AI can provide a solution here,"** DeepMind research scientist Ferran Alet said of cyclones when the model first went public.

## Why it matters

The reason this reads as more than a benchmark result is Hurricane Melissa. In October 2025 the NHC forecast, for the first time in its history, that a Category 1 storm would reach Category 5. WeatherNext was among the guidance behind that call: the model had placed Melissa at Category 5 strength making landfall in Jamaica five days out with 80 percent confidence, rising to near certainty at three days. Melissa went from a 70 mph tropical storm to a 140 mph Category 4 in 18 hours and became the strongest hurricane on record to strike Jamaica.

The NHC's 2025 verification report found WeatherNext was the top-performing individual model for both track and intensity that season. That is the transition worth marking. AI weather models spent 2023 and 2024 posting strong scores on reanalysis benchmarks; in 2025 one entered an operational guidance suite alongside HAFS, satellite feeds and hurricane hunter data, and stayed there.

The payoff is measured in preparation time. **"With early evacuation and better preparation, that reduction in harm really does make a difference to our people,"** said Evan Thompson, principal director of the Meteorological Service Jamaica. Tropical cyclones have killed more than 700,000 people and caused $1.4 trillion in losses globally over the past 50 years, by DeepMind's accounting.

The caveats belong here too. ECMWF's own AI group has documented a systematic weakness in machine-learning forecasts: trained to minimise mean-squared error, they smooth extremes and under-predict the most intense storms, a problem the field attributes to data imbalance and grid resolution rather than to any one architecture. WeatherNext's generative approach is a partial answer, not a general one, and the model does not ingest satellite imagery or ocean heat content directly. DeepMind is explicit that its output is guidance: every warning is still issued by a national meteorological authority.

## What to watch

DeepMind released code and weights for WeatherNext Cyclones, WeatherNext 2 and WeatherNext 2-mini on GitHub under an Apache 2.0 licence. The immediate question is whether meteorological services outside the US and Europe can put them to work. DeepMind says collaborations are under way with PAGASA in the Philippines, Taiwan's CWA, Indonesia's BMKG and Vietnam's VNMHA, with Japan, Australia and India named as next steps. Those are basins where lead time is scarcest and population exposure highest.

Second, the 2026 Atlantic season is the first live test of the 1,000-member ensemble in operations.

Third, watch ECMWF, which is building its own AI forecasting stack and has published a lightweight correction scheme that narrows part of the intensity gap. The interesting question is not which lab wins but whether independent verification, from agencies other than the NHC and across basins other than the Atlantic, reproduces the one-day advantage. A decade of progress claimed in a single paper is a claim that a season of storms will either confirm or trim.
