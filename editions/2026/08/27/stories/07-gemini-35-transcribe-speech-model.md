The most consequential line in Google's new transcription launch is not a benchmark number. It is a configuration flag.

Gemini 3.5 Transcribe, introduced August 26, ships with two transcription modes. `verbatim` returns what was actually said, filler words and false starts intact. `smart` returns what Google thinks you meant. Google's own developer documentation gives the example: the spoken sentence "Um, so for the meeting, I think we should, uh, invite Alice and, wait no, Bob and Carol" comes back from smart mode as "For the meeting, I think we should invite Bob and Carol."

Alice is gone. Not marked as retracted, not struck through. Gone. For a meeting note, that is exactly right. For a deposition, a clinical encounter or a recorded interview, it is a record that no longer matches the audio it came from.

## What actually shipped

Google positions the model as its most precise speech-to-text system yet and the successor to Chirp 3, its 2025 transcription model. It ships as two endpoints: `gemini-3.5-transcribe` for pre-recorded audio via the Interactions API, and `gemini-3.5-transcribe-live` for bidirectional streaming with sub-second latency via the Live API. Both are in public preview through the Gemini API and Google AI Studio.

"Unlike conventional speech recognition models that struggle with background noise, complex jargon, and disfluency cleanup, Gemini 3.5 Transcribe converts raw audio directly into accurate, polished, formatted text," wrote Diego Melendo Casado, senior director of engineering for Gemini Audio, and Luke Leonhard, the team's chief of staff, in the launch post.

The feature list is genuinely broad: automatic language detection across 85-plus locales, code-switching handled mid-sentence, custom vocabulary of up to 1,000 phrases (Google recommends staying under 100), speaker diarization, and word-level timestamps. It is already live in Gboard's Rambler on Android, the Gemini app on macOS, and Google Antigravity, with Chrome next.

Two details the blog post glosses over. The post says diarization handles "up to three speakers"; the API documentation says up to eight, with attribution beyond two marked experimental. And the docs warn that enabling word-level timestamps "may degrade overall transcription accuracy" - an awkward footnote for anyone building an evidentiary pipeline, where timestamps are not optional.

## The benchmark is measuring the wrong thing

Google reports a 4.0% word error rate for streaming and 2.6% for non-streaming, credited to Artificial Analysis. Citing an independent evaluator rather than a self-run eval is to Google's credit, and the figure checks out on the public leaderboard.

What it is not is an average across 85 languages. Artificial Analysis's AA-WER v2 index is roughly eight hours of audio from three sets: a proprietary voice-agent corpus called AA-AgentTalk at 50% weight, the English subset of VoxPopuli at 25%, and six earnings-call recordings at 25%. All English. The 2.6% describes English performance on eight hours of audio, six files of which carry a quarter of the weight.

Google does publish a multilingual figure, and it is roughly double: 5.50% streaming and 5.04% non-streaming on the FLEURS benchmark, "across a set of top languages and locales." Google does not say which languages, or how many. That is the number that should back the 85-language claim, and it is the one with the missing methodology.

The sharper problem is that the benchmark is structurally incapable of measuring the feature Google is selling. Artificial Analysis normalizes both the reference transcript and the model output with OpenAI's Whisper normalizer, which strips filler words like "uh" and "um" before scoring, and it prompts every model it tests with "Transcribe the audio verbatim, outputting only spoken words in sequence." Disfluency removal is invisible to the score, and the score measures verbatim mode. Smart transcription, the headline capability, has no published error rate of any kind.

On that board Google is competitive but not dominant. ElevenLabs Scribe v2 posts 2.2% at an estimated $3.67 per thousand audio minutes, against Google's 2.6% at $5.00. Microsoft's MAI-Transcribe-1.5 hits 2.4%; AssemblyAI's Universal-3 Pro, 3.1% at $3.50. Deepgram's Nova-3 is less accurate at 5.2% but runs at 540 times real time against Google's 79.6. Google's pitch is not the lowest error rate. It is the editing.

## Who gets edited most

The case against silent editing is not hypothetical, and the best evidence comes from the model Google is trying to beat. In Careless Whisper, a 2024 paper led by Cornell's Allison Koenecke with the University of Virginia's Mona Sloane, researchers ran 13,140 audio segments through OpenAI's Whisper and found that "roughly 1% of audio transcriptions contained entire hallucinated phrases or sentences which did not exist in any form in the underlying audio." Thirty-eight percent of those included explicit harms.

The mechanism matters. The paper found that "hallucinations disproportionately occur for individuals who speak with longer shares of non-vocal durations - a common symptom of aphasia," and warned the same bias "could also arise for any demographic group with speech impairments yielding more disfluencies (such as speakers with other speech impairments like dysphonia, the very elderly, or non-native language speakers)."

That is precisely the population whose speech smart transcription will rewrite most aggressively. A model that removes disfluencies works hardest on the speakers who produce the most of them, and it leaves no mark when it does.

Verbatim output has an auditing property that edited output does not: you can play the audio and compare. A cleaned transcript looks equally plausible whether the cleanup was right or wrong, and the only way to catch a bad deletion is to re-listen to the whole recording, which defeats the point of a transcript. In dictation - Rambler, the macOS app, Chrome soon - no recording is kept at all. The source is destroyed at the moment of capture.

Google has drawn the boundary in roughly the right place. Verbatim is the API default; smart is opt-in. And smart mode is explicitly incompatible with both word timestamps and speaker diarization, so you cannot generate an edited transcript that also carries the metadata that would make it look like a record of proceedings. That is a deliberate constraint and a good one.

The exposure is downstream. Google's own launch post names IntelliTek Health, which says it uses the model for real-time clinical transcription across primary care and medical specialties. The risk is not that Google mislabels its modes. It is that a product manager sets mode to smart because the notes read better, and nobody in the compliance chain knows the flag exists.

## What to watch

Two things. Whether Google publishes per-language error rates and names the FLEURS locale set behind that 5.04% figure; a single multilingual average over an undisclosed language list is a marketing artifact, not a measurement. And whether anyone - Artificial Analysis, an academic group, a large customer - builds an evaluation that can score smart mode at all. Word error rate cannot: deleting a word you should have kept and correctly dropping a filler are the same edit distance. That requires a semantic fidelity metric that does not yet exist in public form.

The transcription industry has spent a decade optimizing a single number. Google just shipped a product whose main feature that number cannot see.
