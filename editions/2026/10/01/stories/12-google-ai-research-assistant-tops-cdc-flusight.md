Every flu season, dozens of academic, government and industry teams send forecasts to the US Centers for Disease Control and Prevention, each predicting how many people will end up in the hospital. For the 2025-26 season, the best individual entry did not come from a human modeler. It came from an AI system that writes forecasting software.

The CDC's end-of-season FluSight evaluation, published September 30, 2026, named Google's Google_SAI-FluEns the top performer among individual team submissions. It ranked first of the 39 models that qualified for scoring. Google built those forecasts with Empirical Research Assistance (ERA), a Google Research tool that uses a large language model to generate, test and refine scientific code.

"This performance validates our confidence that AI combined with human ingenuity will improve our ability to forecast diseases worldwide," Zahra Shamsi of Google Research wrote in the company's announcement.

## The Scorecard

The size of the field matters here. According to the CDC report, 34 teams submitted influenza hospital admission forecasts from 53 different models during the season. Only 39 of those models submitted at least 75% of the forecast targets, which was the bar for inclusion in the analysis. The CDC scored forecasts for the 50 states and Washington, D.C. National forecasts were left out because of differences in scale, and Puerto Rico was left out because of data availability.

The main metric was relative weighted interval score (WIS). WIS measures how well a model's full set of prediction intervals, not just its single best guess, matches what actually happened. Scores are computed on log-transformed admission counts and compared with a naive baseline that simply carries the previous week's count forward. A score below 1 beats the baseline. Thirty-three of the 39 models cleared that bar.

The CDC also builds a FluSight ensemble, which takes the median of participating models' forecasts and is what the agency uses in its public messaging. The ensemble ranked seventh overall. It was also one of 12 models that beat the baseline in every jurisdiction. Google's ERA-built model finished above it.

The season itself was a hard test. The CDC rated it moderate, but weekly hospital admissions peaked above 40,000 nationally in the week ending December 27, 2025, after rising from mid-November. Even the ensemble's prediction intervals missed the late-December surge and the steep drop in mid-January. Around the peak, fewer than 25% of two-week-ahead prediction intervals across jurisdictions contained the observed value. Ensemble forecasts "may not always reliably predict rapid changes in disease trends, such as increases observed at the season onset and changes at the peak," the CDC wrote.

## How the System Works

ERA does not forecast flu by itself. It builds the software that does. A preprint posted in May 2026 by Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich and Shamsi describes the approach. An LLM guides a tree search that writes candidate forecasting programs, scores them against a defined quality measure, and keeps refining the strongest branches. The CDC report cites both that preprint and the ERA paper published this year in *Nature*.

The flu entry was prospective, meaning the forecasts were made in real time and scored against data that did not yet exist when they were submitted. When the FluSight challenge opened in November 2025, Google began sending weekly forecasts for every US state. The team later joined the CDC's live forecasting hubs for COVID-19 and RSV. Public leaderboards run by Reich, a University of Massachusetts Amherst biostatistics professor who consults on the project, showed Google "performing at or near the top" for both flu and COVID-19 during its submission periods, according to an April Google Research post. The preprint reports that an ensemble of the machine-generated models matched or beat the CDC's human-curated hub ensembles out of sample. It also says the system produced usable RSV forecasts in data-scarce "cold start" conditions.

This is a step up from ERA's first public test. In a September 2025 preprint, Google showed ERA could match or beat existing COVID-19 hospitalization forecasting tools *retrospectively*. FluSight is a live, independently scored competition, which makes it a much stronger result.

## Why It Matters

The way this result was produced matters more than the ranking. Google did not hand-build a better flu model. It aimed a code-writing AI at a well-defined scoring problem, and that system came up with the winning approach. That is the main claim behind ERA and related Google efforts such as its AI co-scientist: wherever a scientific task can be scored automatically, an LLM-guided search can explore far more candidate methods than a human team could.

Google's research team made the public-health case directly: "An AI-powered tool that can meet or exceed the forecasting accuracy of leading public health agency tools promises huge public health benefit for tracking newer conditions and in broader locations." Many state and local health departments do not have modeling staff. A system that can quickly produce a competitive forecaster for a new pathogen or region, as the RSV cold-start results suggest, could close that gap.

The result has limits. It covers one season, on one primary metric, against one baseline. The CDC's own report shows that every approach struggled at turning points, and those are the weeks hospitals care about most. The CDC also pointed out that its model categories, including "AI/ML," were assigned from self-reported metadata and were not used in scoring. FluSight rewards accuracy, not method.

## What to Watch

The 2026-27 FluSight season opens in the coming weeks, and a second strong season would mean much more than one. Watch whether Google_SAI-FluEns keeps its edge around the season peak, where every model struggled last winter. Watch whether ERA does as well in the CDC's forthcoming evaluation of flu emergency-department-visit forecasts. And watch how quickly ERA moves from Google's trusted-tester program into the hands of public health agencies that could use it without a Google research team behind them.
