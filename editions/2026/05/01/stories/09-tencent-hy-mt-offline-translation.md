---
headline: "Tencent Open-Sources Hy-MT1.5, a 440MB Translation Model That Runs Offline and Outperforms Google Translate"
slug: tencent-hy-mt-offline-translation
category: llms-genai
story_number: "09"
date: 2026-05-01
---

# Tencent Open-Sources Hy-MT1.5, a 440MB Translation Model That Runs Offline and Outperforms Google Translate

A translation model that fits in less space than a single Spotify playlist, runs entirely offline on a smartphone, handles 33 languages, and still manages to outperform Google Translate -- that is the pitch behind Tencent's newly open-sourced Hy-MT1.5-1.8B-1.25bit, released on April 29 through the company's Hunyuan AI division. At just 440 megabytes, the model represents a remarkable feat of compression engineering that could reshape how billions of people access translation technology in low-connectivity environments.

## From 3.3 Gigabytes to 440 Megabytes

The 440MB model is not a new architecture built from scratch. It is the result of an aggressive quantization pipeline applied to Tencent's HY-MT1.5-1.8B, a 1.8-billion-parameter translation model that the Hunyuan team first open-sourced on December 30, 2025, alongside its larger 7B-parameter sibling. In its original FP16 precision, the 1.8B model weighs in at 3.3 gigabytes -- already small by large language model standards, but still too heavy for comfortable on-device deployment.

To bridge that gap, the team applied a quantization technique called Sherry, which was accepted at the ACL 2026 conference. Sherry uses a 3:4 fine-grained sparsity strategy: for every four model weights, the three most important are stored in just 1-bit precision (values of -1 or +1), while the fourth is zeroed out entirely. The result packs four weights into five bits, achieving an effective bit-width of 1.25 -- an 87 percent compression rate with what Tencent describes as "minimal accuracy loss."

"The 1.25-bit quantization achieves power-of-two alignment, which is critical for efficient mobile CPU inference," the Tencent Hunyuan team wrote in their technical documentation. The model is paired with a custom STQ mobile CPU kernel that enables ordinary smartphones to run high-quality offline translation smoothly, without any cloud dependency.

## Benchmark Performance

The numbers behind the 440MB model are striking. Despite its extreme compression, Hy-MT1.5-1.8B-1.25bit comprehensively surpasses models many times its size in translation quality benchmarks. According to Tencent's published evaluations, the quantized model outperforms Tower-Plus-72B (a model with 40 times more parameters), Qwen3-32B, and several mainstream commercial APIs including Microsoft Translator, Doubao Translator, and -- most notably -- Google Translate.

The model natively supports 33 languages and 1,056 translation directions, covering major world languages such as English, Chinese, Japanese, German, and French, as well as less commonly supported languages including Tibetan and Mongolian, plus five additional dialect variations.

"It is irresponsible for translation technology to remain dependent on cloud connectivity when billions of users live in regions with unreliable internet," said a representative from the Tencent Hunyuan team in a statement accompanying the release. "On-device translation is not a nice-to-have -- it is a necessity for genuine global accessibility."

The original unquantized HY-MT1.5-1.8B already delivered impressive latency numbers. When the base model debuted, it trended to the number one spot on Hugging Face, with Tencent reporting inference latency of just 0.18 seconds -- fast enough for real-time conversational translation.

## Why 1.25-Bit Matters

The quantization breakthrough here extends beyond translation. The Sherry technique demonstrates that large language models can be compressed to bit-widths previously considered impractical while retaining task-specific performance that rivals or exceeds full-precision models orders of magnitude larger. If this approach generalizes, it could accelerate the deployment of specialized AI models on edge devices across healthcare, education, and emergency response -- domains where offline capability and small footprints are not optional.

The model's 440MB footprint compares favorably to the download size of many common mobile applications. WhatsApp, for example, occupies roughly 200MB on most devices, while games routinely exceed one gigabyte. The implication is that a user could carry a 33-language translation engine alongside their everyday apps with negligible impact on storage.

## The Competitive Landscape

Tencent's release lands in an increasingly crowded field of on-device AI translation. Google has been expanding offline capabilities in Google Translate for years, most recently adding 33 new languages for offline use in a 2023 update. Meta has invested heavily in its SeamlessM4T multilingual model family. Apple integrated on-device translation into iOS starting with iOS 14.

But none of these competitors have open-sourced a model this small that performs at this level. The open-source release -- available on both Hugging Face and GitHub under the Tencent-Hunyuan organization -- means any developer can integrate the model into their own applications without licensing fees, API costs, or data-sharing requirements. For privacy-conscious users and organizations operating in sensitive environments, the fully offline, fully local architecture eliminates the risk of translation data being transmitted to external servers.

## The Bigger Picture

The HY-MT1.5 family originated from Tencent's championship-winning entry at WMT25 (the Workshop on Machine Translation), giving the models a competitive pedigree that few open-source translation projects can claim. The 7B variant, designed for cloud deployment, adds advanced capabilities like terminology intervention, contextual translation, and formatted translation -- features typically reserved for expensive enterprise APIs.

With the 1.25-bit release, Tencent is making a clear statement: state-of-the-art translation no longer requires a data center, a cloud subscription, or even an internet connection. It just requires 440 megabytes of storage and a phone.
