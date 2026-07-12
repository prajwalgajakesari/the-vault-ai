Most of the AI boom has been a story about text and, more recently, about generating video from scratch. TwelveLabs is betting the bigger prize is the footage that already exists. On July 1, the San Francisco- and Seoul-based startup said it had raised $100 million in Series B funding to keep building foundation models that let machines understand video the way they now parse documents, pushing its total capital raised past $207 million.

The round was co-led by New Enterprise Associates and NAVER Ventures, with participation from Amazon, Radical Ventures, Korea Investment Partners, Index Ventures, Quadrille Capital and Red Bull Ventures. It follows a roughly $50 million Series A co-led by NEA and NVIDIA's NVentures, and lands as enterprises move from pilots to production deployments of video AI.

## The contrarian bet

TwelveLabs' pitch rests on a distinction that is easy to miss in a market obsessed with Sora and Veo. It does not generate video. It makes existing video queryable. "Five years ago, we made a contrarian bet: the substrate of machine intelligence is recorded reality in motion, not language," said CEO and co-founder Jae Lee. "Language is downstream of understanding. Video is the data understanding has to answer to."

That thesis has a striking data point behind it: video accounts for as much as 90% of the world's data, yet most of it is effectively dark matter to machines, accessible only through filenames, folders, transcripts and human memory. The last decade made text programmable, turning words into tokens and documents into context for agents. Video, TwelveLabs argues, has not had that moment.

## Marengo and Pegasus

The company's answer is two foundation models built for video rather than adapted from language systems. Marengo, whose 3.0 version shipped late last year, is an embedding model that maps visual, audio, speech and on-screen text into a single searchable representation. TwelveLabs bills it as the most powerful video embedding model available, capable of turning raw footage into a semantic layer that machines can search at scale.

Pegasus, the video-language model now in a 1.5 release, turns those representations into structured data: scene boundaries, entities, temporal segments and semantic context a system can reason over. The company likens it to a domain-specific language for video, making footage parseable the way markup languages make documents readable by browsers. Crucially, TwelveLabs says its architecture builds a persistent memory of every video it ingests, rather than re-inspecting clips from scratch on each query. Both models are distributed through Amazon Bedrock and the company's own API.

## Who is buying

TwelveLabs says it has established deep traction in media and entertainment and is moving into the public sector, working with governments on mission-critical workflows. Additional demand is coming from advertising, security, sports and automotive, industries where enormous volumes of information sit locked inside footage. Earlier this month the company shipped Rodeo, its first application-layer product, signaling a move up the stack from raw models toward tools that operators and creators can use without integration work.

Investors framed the round as validation of a category, not just a company. "Jae and his team built the foundation models that set the standard for what video understanding can be," said Tiffany Luck, a partner at NEA, adding that "as video understanding moves from novel capability to essential infrastructure, we believe TwelveLabs is the company defining what comes next." YJ Park, general partner at NAVER Ventures, noted that TwelveLabs was the firm's first-ever investment: "When we first met Jae, he described TwelveLabs as the visual cortex for future AI agents. That framing has only sharpened over time."

## An under-served modality

The strategic logic is that video understanding has been overshadowed by two louder AI stories: text-based large language models and generative video from OpenAI's Sora, Google's Veo and Runway. Those systems create pixels. TwelveLabs indexes reality. General-purpose LLMs can technically ingest video, but they sample a handful of frames, miss what happens in between, and reset with every query. Feeding entire libraries into a context window is computationally infeasible at enterprise cost. That gap is the moat TwelveLabs is trying to widen.

The risk is that the same hyperscalers it partners with could subsume the category. As part of the raise, TwelveLabs deepened its tie to Amazon, naming AWS its preferred cloud provider under a multiyear commitment to optimize inference on Trainium chips and launch new models on AWS first. Google and others have their own multimodal ambitions.

## What to watch next

Three signals will show whether the bet pays off: how quickly Rodeo and the application layer convert model access into recurring enterprise revenue; whether the new New York and London offices translate government and media interest into signed deployments; and whether frontier labs decide native video understanding is worth building in-house rather than buying. If footage truly becomes as programmable as text, TwelveLabs wants to own the layer that makes it so.
