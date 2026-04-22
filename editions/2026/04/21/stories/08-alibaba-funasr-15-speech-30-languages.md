---
headline: "Alibaba Ships Fun-ASR 1.5, a 30-Billion-Parameter Speech Model Covering 30 Languages"
slug: alibaba-funasr-15-speech-30-languages
category: llms-genai
story_number: "08"
date: 2026-04-21
---

# Alibaba Ships Fun-ASR 1.5, a 30-Billion-Parameter Speech Model Covering 30 Languages

Alibaba's Tongyi Laboratory has released Fun-ASR 1.5, a 30-billion-parameter Mixture of Experts speech recognition model that can transcribe 30 languages, seven major Chinese dialect families, and more than 20 regional accents -- all within a single unified architecture. The model, which went live on April 20 on Alibaba Cloud's Bailian platform and the ModelScope community, represents one of the largest end-to-end automatic speech recognition systems publicly available today and signals a new front in the race to make AI truly multilingual.

## A Single Model for a Fractured Linguistic Landscape

Speech recognition has long struggled with the so-called long-tail problem: mainstream languages like English and Mandarin receive ample training data, while dialects, minority languages, and accented speech are left behind. Fun-ASR 1.5 tackles this head-on. Trained on tens of millions of hours of real speech data -- with more than 500,000 hours dedicated to Chinese dialect audio alone -- the model consolidates what would traditionally require dozens of separate language-specific systems into one.

The 30 supported languages span East Asian, Southeast Asian, South Asian, Middle Eastern, and European language families, including Chinese, English, Japanese, Korean, Vietnamese, Thai, Indonesian, Hindi, Arabic, French, German, Spanish, Portuguese, and Russian. Critically, the model handles code-switching between languages without requiring users to preset language tags, a feature that reflects how multilingual speakers actually talk.

On the Chinese dialect front, the seven major dialect groups covered are Wu, Cantonese, Min, Hakka, Gan, Xiang, and Jin. Internal benchmarks show a 56.2 percent reduction in character error rate for dialect scenarios compared to the previous Fun-ASR version, with five dialects now achieving above 90 percent accuracy.

"We look forward to collaborating with DingTalk to drive innovative applications of speech recognition technology in enterprise settings," said Li Xiangang, head of the speech team at Tongyi Lab, in an earlier statement about the Fun-ASR platform's enterprise direction. That vision is now taking concrete shape: Fun-ASR 1.5 is already being deployed through API services to clients in education, media, finance, technology, and culture.

## Beyond Words: Poetry, Punctuation, and Production-Ready Output

Tongyi Lab framed the 1.5 release around three core pillars: "hear more comprehensively, hear more accurately, write more standardized." The first two are addressed by the expanded language and dialect coverage. The third reflects a set of improvements that matter most in real-world deployment.

Fun-ASR 1.5 introduces intelligent punctuation prediction based on semantic context, eliminating the robotic, comma-spliced output that plagues many transcription systems. It also delivers significantly improved text normalization -- what engineers call inverse text normalization, or ITN -- automatically converting colloquial spoken forms into their standard written equivalents for dates, monetary amounts, phone numbers, and other structured data.

Perhaps the most culturally distinctive feature is the model's dedicated optimization for classical Chinese poetry recitation. Poetry presents a unique challenge for ASR systems: fluctuating tones, archaic vocabulary, and sentence structures that diverge sharply from modern spoken Chinese. Fun-ASR 1.5 achieves 97 percent character-level accuracy on classical poetry, according to internal evaluations -- a benchmark that will resonate in educational and cultural preservation contexts across the Chinese-speaking world.

## Competitive Context

Fun-ASR 1.5 enters an increasingly crowded field. OpenAI's Whisper remains the most widely used open-source multilingual ASR model, while Google's Universal Speech Model and Meta's Seamless suite have pushed the boundaries on language coverage. Within Alibaba's own ecosystem, the Qwen team recently released Qwen3-ASR, a separate open-weights speech recognition model.

What distinguishes Fun-ASR 1.5 is scale and specificity. At 30 billion parameters with MoE architecture, it dwarfs most competing ASR models. And its deep investment in Chinese dialectal variation -- a domain where global competitors have minimal coverage -- gives it a clear niche. According to GitHub benchmarks, the smaller Fun-ASR Nano model (800 million parameters) already achieves a 12.70 percent average word error rate on industry datasets, compared to 26.13 percent for GLM-ASR-nano, suggesting the full-scale 1.5 model will be even more competitive.

"Balancing generality and accuracy in AI speech has been a persistent industry challenge," Tongyi Lab noted in its announcement. Fun-ASR 1.5's unified architecture approach -- one model, many languages, many dialects -- is their answer.

## What It Means

The release matters beyond its technical specifications. As voice interfaces become the default interaction layer for AI assistants, customer service bots, and enterprise tools, the quality of the underlying ASR model determines who gets heard and who gets misunderstood. A Cantonese-speaking grandmother calling a government hotline, a Hakka-dialect teacher running a livestream class, a multilingual business meeting switching between Mandarin and English -- these are the real-world scenarios where Fun-ASR 1.5 aims to deliver.

Fun-ASR 1.5 is available now through Alibaba Cloud Bailian's API services and ModelScope. The underlying code is open-sourced on GitHub, and a technical paper is available on arXiv (2509.12508).