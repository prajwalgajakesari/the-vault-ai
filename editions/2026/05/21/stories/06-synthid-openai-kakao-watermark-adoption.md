---
headline: "OpenAI and Kakao Adopt Google SynthID as AI Watermarking Goes Industry-Wide"
slug: synthid-openai-kakao-watermark-adoption
category: llms-genai
story_number: "06"
date: 2026-05-21
---

Google's invisible watermarking technology SynthID is rapidly becoming the de facto standard for identifying AI-generated content, as a wave of new adoption announcements at Google I/O 2026 confirmed that even the company's fiercest rivals are lining up behind its approach.

OpenAI, South Korean tech giant Kakao, voice synthesis leader ElevenLabs, and Nvidia all committed to embedding SynthID in their AI-generated outputs, marking the most significant consolidation around a single content-provenance technology since the generative AI boom began. The announcements, made on May 19 at Google's annual developer conference, signal that the industry is moving past fragmented approaches to AI transparency and toward a unified framework for tracking machine-made media.

## The Scale of SynthID

The numbers tell the story of a technology that has quietly achieved massive reach. SynthID has now watermarked more than 100 billion images and videos and the equivalent of 60,000 years of audio across Google's own products. Its verification tools, which allow users to check whether content was AI-generated, have been used 50 million times globally since being integrated into the Gemini app.

Now Google is pushing that verification capability far beyond its chatbot. Starting immediately, Google Search features including Lens, AI Mode, and Circle to Search will be able to identify SynthID-watermarked content. Chrome will gain the same detection tools in the coming weeks. Users will be able to simply ask whether an image was made with AI and receive an answer grounded in both SynthID's invisible watermark and C2PA Content Credentials metadata.

## OpenAI Embraces a Rival's Technology

The most striking announcement was OpenAI's decision to adopt SynthID. The company will embed the invisible watermark across all images generated through ChatGPT, Codex, and the OpenAI API. Alongside SynthID, OpenAI is formally joining the Coalition for Content Provenance and Authenticity (C2PA) open standard and has taken a seat on its steering committee.

The dual-layer approach pairs C2PA's visible metadata -- which records a file's origin and editing history -- with SynthID's invisible watermark, which persists even through screenshots, resizing, and compression. OpenAI is also previewing a public verification tool that checks for both signals, though for now it only covers images produced by OpenAI's own models.

The partnership is notable for what it represents strategically. SynthID was developed by Google DeepMind, and OpenAI's willingness to embed a competitor's technology in its core products suggests that the industry recognizes standardization as more important than proprietary advantage when it comes to content authenticity.

## Kakao Breaks Ground in Asia

Kakao became the first Asian company to adopt SynthID, applying the watermark to its in-house AI model Kanana. The integration will initially appear in the KakaoTalk Kanana Template feature, which generates short videos from images shared on the messaging platform using the Kanana Kinema model. Kakao's image generation tool Kanana Collage will also carry the watermark.

The adoption is significant for expanding SynthID's geographic reach. As deepfake concerns mount across Asia -- where messaging platforms like KakaoTalk are central to daily communication -- Kakao's move provides a template for other regional tech companies to follow. South Korea has been particularly aggressive in pursuing AI content regulation, and Kakao's proactive adoption positions the company favorably with regulators.

## A Broader Coalition Forms

ElevenLabs, whose voice synthesis technology has been at the center of numerous deepfake audio controversies, is also bringing SynthID to its AI-generated audio outputs. The addition is particularly meaningful given the growing concern about synthetic voice content in political campaigns and fraud schemes.

Nvidia, meanwhile, is applying SynthID to AI-generated video from its Cosmos world foundation models, extending the watermark into the emerging category of AI-created video content used in robotics simulation and autonomous vehicle training.

Google also announced a new AI Content Detection API on its Gemini Enterprise Agent Platform, giving businesses the ability to detect AI-generated content from both Google and third-party models. Launch partners include Shutterstock, Avid, Canva, Snap, and Fox Sports -- though Adobe, a C2PA co-founder, was a notable absence.

## What This Means for AI Transparency

The consolidation around SynthID represents a turning point for AI content provenance. For years, the industry debated whether watermarking, metadata standards, or detection models offered the best path forward. The answer, it now appears, is all three working in concert -- with SynthID and C2PA forming complementary layers that together create a more resilient system than either could alone.

Yet significant challenges remain. SynthID watermarks only work when companies voluntarily embed them, leaving open-source models and smaller providers outside the system. Detection tools are only as useful as the platforms willing to check for watermarks, and the verification infrastructure needed to make this work at internet scale is still being built.

The practical impact will depend on whether the momentum continues. With Google, OpenAI, Kakao, ElevenLabs, and Nvidia now aligned, a critical mass of AI-generated content will carry provenance signals. But the deepfake arms race is far from over -- and the companies most likely to produce harmful synthetic content are precisely those least likely to adopt voluntary watermarking standards.

Still, the breadth of adoption announced at I/O 2026 is unprecedented. For the first time, the major AI labs appear to agree that the question is not whether to watermark AI content, but how quickly they can make it universal.