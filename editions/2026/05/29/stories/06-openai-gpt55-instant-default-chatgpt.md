---
headline: "OpenAI Makes GPT-5.5 Instant Default in ChatGPT, Cutting Hallucinations 52 Percent"
slug: openai-gpt55-instant-default-chatgpt
category: llms-genai
story_number: "06"
date: 2026-05-29
sources:
  - name: OpenAI Blog
    url: https://openai.com/index/gpt-5-5-instant/
    domain: openai.com
  - name: TechCrunch
    url: https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/
    domain: techcrunch.com
  - name: The Decoder
    url: https://the-decoder.com/chatgpt-update-rolls-out-gpt-5-5-instant-with-fewer-hallucinations-and-more-personalized-answers/
    domain: the-decoder.com
  - name: 9to5Mac
    url: https://9to5mac.com/2026/05/05/gpt-5-5-instant-makes-chatgpt-more-accurate-while-nixing-gratuitous-emojis/
    domain: 9to5mac.com
---

# OpenAI Makes GPT-5.5 Instant Default in ChatGPT, Cutting Hallucinations 52 Percent

Every time you open ChatGPT now, a different brain is answering. On May 5, OpenAI flipped the switch on GPT-5.5 Instant, replacing GPT-5.3 Instant as the default model powering the world\u2019s most-used AI chatbot. The headline number is hard to ignore: a 52.5 percent reduction in hallucinated claims across high-stakes domains like medicine, law, and finance, according to the company\u2019s internal evaluations.

For hundreds of millions of ChatGPT users, the upgrade landed silently\u2014no opt-in required, no toggle to flip. One day the model behind the chat window was GPT-5.3 Instant; the next, it was its successor. That seamlessness is by design. OpenAI is betting that the best model updates are the ones users feel rather than configure.

## The Hallucination Problem Gets Halved

The centerpiece of the GPT-5.5 Instant release is factual reliability. OpenAI reported that in internal testing, the new model produced 52.5 percent fewer hallucinated claims than GPT-5.3 Instant on prompts covering medicine, law, and finance\u2014domains where a fabricated citation or invented statute can carry real consequences. The hallucination rate dropped from 18.7 percent to 8.9 percent in those areas.

On a separate test set drawn from conversations that users had previously flagged for factual errors\u2014the hardest cases, in other words\u2014inaccurate claims fell by 37.3 percent.

\u201cInstant is now more dependable, with significant improvements in factuality across the board and the largest gains in domains where accuracy matters most,\u201d OpenAI wrote in its announcement blog post.

Those are meaningful numbers, but they come with a caveat worth stating plainly: 8.9 percent is not zero. Roughly nine out of every hundred specialized answers may still contain inaccuracies. For professionals relying on ChatGPT in clinical or legal workflows, the improvement narrows the trust gap without closing it entirely.

## Beyond Accuracy: Benchmarks, Speed, and Tone

The gains extend well beyond hallucination metrics. On AIME 2025, a competitive mathematics exam, GPT-5.5 Instant scored 81.2 percent\u2014a leap from the 65.4 percent achieved by its predecessor. The GPQA benchmark for PhD-level science reasoning climbed from 78.5 to 85.6 percent. On MMMU-Pro, which tests expert-level multimodal reasoning, the model improved from 69.2 to 76.0 percent.

Response latency also dropped by roughly 40 percent compared to GPT-5.3 Instant, meaning the model is not just smarter but faster\u2014a combination that rarely arrives in the same update.

OpenAI also took aim at a complaint that had become a running joke among power users: the relentless emoji use and over-formatted responses that characterized earlier Instant models. The company said GPT-5.5 Instant delivers \u201ctighter and more to-the-point\u201d answers, with fewer unnecessary follow-up questions and, notably, no more \u201cgratuitous emojis.\u201d The update follows GPT-5.3 Instant\u2019s March release, which itself had promised to make ChatGPT \u201cless cringe.\u201d

## Memory Gets Smarter\u2014and More Transparent

Perhaps the most architecturally interesting addition is what OpenAI calls \u201cmemory sources.\u201d GPT-5.5 Instant can now reference past conversations, uploaded files, and connected Gmail accounts to personalize responses\u2014and crucially, it shows users which stored context shaped a given reply.

This transparency layer lets users see exactly what information the model drew on, flag entries as relevant or irrelevant, edit stored memories, or delete them entirely. OpenAI noted that memory sources are not passed along when a chat is shared, and temporary chats neither read from nor update memory\u2014a privacy guardrail that addresses one of the more obvious concerns with persistent personalization.

Enhanced personalization is rolling out first to Plus and Pro users on the web, with mobile support coming soon. Free, Go, Business, and Enterprise plans are expected to gain access in the coming weeks.

## The Deprecation Playbook

For developers, GPT-5.5 Instant is available through the API as \u201cchat-latest.\u201d Paid users can still access GPT-5.3 Instant through model configuration settings, but only for three months before it is retired.

OpenAI has learned\u2014sometimes painfully\u2014that model transitions are not purely technical events. When the company deprecated GPT-4o in February 2026, the backlash was fierce. Users who had formed attachments to that model\u2019s conversational style signed petitions and described it as their \u201cbest friend.\u201d The three-month grace period for GPT-5.3 Instant suggests OpenAI is building in more runway for users to adjust, even as it moves decisively toward newer architectures.

## What It Means

GPT-5.5 Instant represents the clearest evidence yet that the frontier of AI competition has shifted from raw capability to reliability. The largest language models can already write code, summarize case law, and draft marketing copy. The question that matters now\u2014for enterprises evaluating AI procurement, for developers building on these APIs, and for the hundreds of millions of casual users who treat ChatGPT as a daily utility\u2014is whether they can be trusted to get the facts right.

A 52 percent reduction in hallucinations is substantial, but it is an improvement on a curve, not a finish line. The remaining 8.9 percent error rate in specialized domains means that human verification remains essential for any high-stakes application. OpenAI\u2019s decision to pair accuracy gains with memory transparency signals that the company understands trust is built not just through better outputs, but through letting users see how those outputs are produced.

For now, the upgrade is live, the emojis are gone, and ChatGPT is\u2014by the numbers, at least\u2014more honest than it was last week. Whether that is enough depends on what you are asking it.