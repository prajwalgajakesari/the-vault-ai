# GPT-6 Astra and Claude Opus 5 Crack Long-Unsolved Enigma Messages

For 21 years, an 82-letter German Army radio message from July 10, 1941 sat on a short list of Enigma traffic that nobody could read. This month it fell to OpenAI's GPT-6 Astra, and less than a week later Anthropic's Claude Opus 5 broke a second message from the same list. Together, the two breaks suggest that frontier AI models can now handle historical codebreaking, work that until recently needed a team of specialists.

Both results were confirmed by Frode Weierud, a retired electrical engineer who runs the **Crypto Cellar** research site. The site keeps a public list of World War II Enigma intercepts that are still unbroken, usually because the operator made a mistake or because the surviving transcription is corrupted. Weierud says that after these two breaks, **seven unbroken messages remain**, plus one where the plaintext is known but the key has not been recovered.

## How Astra Found Its Way In

Developer Carter Leffen gave GPT-6 Astra an open-ended job: look at the unbroken messages on Crypto Cellar and see if any of them could be cracked. According to Weierud's write-up, the model picked message Nr. 172, known by its indicator **MVUEH**, as the best candidate. It then guessed that the plaintext of a related message from the same day, Nr. 173, SIPVX, might overlap with it. SIPVX had been broken in 2017 and contained a town name repeated twice, ROSENOWROSENOW. Astra used those 14 letters as a *crib*, a piece of text it expected to find in the plaintext. It then wrote its own Enigma simulator and a software version of the Bombe, the codebreaking machine built at Bletchley Park, in Python and C++. The work ran over September 14 and 15.

The decrypted message turned out to be an ordinary request. According to Leffen's case study, a sender tentatively identified as Waschbusch asks for his route of march, says he is in Rosenow, and wants an immediate reply by radio. Getting there was hard. The key used Enigma I with reflector B, rotor order II-V-III and ten plugboard pairs. Weierud says it was "completely different from the other keys from 10 July 1941." The published ciphertext also contained transcription errors, and the left rotor stepped over at the 72nd letter, which is rare. Leffen's case study says all **43,016 search batches** were accounted for and that separate implementations reproduced the full message.

Weierud received the solution on September 15 and says "it was immediately clear he had found the correct key and plaintext." He was even more impressed by how Astra got there. "GPT-6 Astra is behaving like a very professional cryptanalyst and archive researcher," he wrote. "What it has achieved in two days would take a human researcher weeks or even months." He added that he had personally spent several weeks on the German Bundesarchiv files the model cited.

That archival detail raised a question. Astra's logs cite files, including RS 3-3/20a and RS 3-3/63b, that are not hosted on Crypto Cellar, and they mention a "private collection." Weierud says he does not know how the model reached them. He doubts they mattered much to the break.

## Opus 5 Follows

Weierud says the MVUEH result prompted a second attempt. Jack Willis, a cybersecurity executive, used Claude Opus 5 to break the 63-letter message Nr. 205 NF / Nr. 285 **FMNGI**, dated July 31, 1941, and contacted Weierud on September 21. TechCrunch reports that Willis steered his model much more than Leffen did. The crib here was XHARTJENSTEINX, an officer's signature that appears often in the traffic.

## Why It Matters

Amateur Enigma breaking has a history. In 2006, German cryptographer Stefan Krah's **M4 Message Breaking Project** spread a brute-force search across thousands of volunteer PCs and broke two of three naval intercepts that Bletchley Park never read, the first within weeks of launch. That was a large collective effort aimed at a narrow search problem. The MVUEH break is different in kind. One model chose the target, found a related message, came up with the crib, wrote the tools and checked the result. The search is the easy part of historical cryptanalysis. The hard part is the judgment about where to look.

How much of that judgment came from the model is still disputed. Leffen's own case study calls it "a researcher-led investigation" in which he set the goal and pushed the work forward. Weierud's account, and Leffen's post on X, credit the model with far more autonomy. The Opus 5 break was clearly a human-AI collaboration. Either way, both results passed independent expert checks, which many AI capability claims do not.

The security angle is harder to ignore. Enigma is obsolete, and nobody's secrets are at risk. But OpenAI markets Astra on cybersecurity, among other things, and in both breaks the models went looking for primary sources. In Astra's case, the expert who checked the result cannot say where some of those sources came from.

## What to Watch

The obvious next step is the seven messages left on Crypto Cellar's list. Some of them are unbroken because the transcriptions are damaged, not because anyone ran out of computing power, so they will show whether these models can reason around bad data. Weierud says he is still going through Astra's logs, and a full account of how it found the Bundesarchiv files will say as much about agent behavior as about cryptanalysis. For now, a list that barely changed in two decades has lost two entries in a single week.
