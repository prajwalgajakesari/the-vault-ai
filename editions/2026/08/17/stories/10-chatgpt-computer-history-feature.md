OpenAI has given ChatGPT a working memory of your desktop, and it built the thing by conspicuously avoiding the one design decision that sank Microsoft's attempt: it never looks at your screen.

The feature is called Computer History, and it is rolling out now to ChatGPT Pro, Business and Enterprise subscribers on the macOS desktop app. In OpenAI's launch video, Dominik Kundel, a developer-experience engineer at the company, asked the assistant in voice mode what the last Google Doc he had viewed was. ChatGPT named it. He then asked whether he had shared it with colleagues, and the model worked through his Slack history to check. Then he asked for a summary of his morning, and got one.

No screenshots were involved in any of it.

"Computer History doesn't rely on screen or audio capture," Kundel said in the announcement video. "Instead, it captures interaction events like clicking, typing, app switches, and more, so it can capture memories faster and more efficiently."

## What an 'event' actually contains

The distinction is not cosmetic. Computer History replaces Chronicle, a research preview OpenAI shipped to Codex for Mac in April that worked by periodically screenshotting the display. This is a rebuild, not a rename. It constructs what OpenAI's documentation calls an "interaction-event stream" from allowed apps and websites: clicks, typing, keyboard shortcuts, app switches, and whatever context macOS surfaces through its accessibility APIs. It captures no screenshots, screen recordings, microphone input or system audio, and never touches private-mode browsing. Tellingly, it does not request macOS Screen Recording permission at all.

Those raw events sit temporarily on the Mac inside the ChatGPT App Group container, and OpenAI says they are deleted after 48 hours. Periodically, the app spins up an ephemeral Codex session that reads the event stream and distills it into memories — plain-text Markdown files written to `~/.codex/memories/extensions/skysight/`. That summarization step happens on OpenAI's servers; the company says it does not retain the event files afterward and does not use them for training.

John Voorhees, managing editor at MacStories, spent a day with the feature and documented the output: a timestamped entry roughly every ten minutes, each a Markdown file with YAML front matter listing the apps involved, a narrative summary, and a section headed "Important non-obvious context about the user" enumerating file names, document titles and the people he had messaged. One ten-minute entry ran just shy of 700 words.

Voorhees was enthusiastic about the premise and blunt about the trade. "Every thread is like Groundhog Day for an agent," he wrote of the tedium of re-explaining context to Codex. But he drew the line plainly: "If you're not comfortable with letting Codex use your Mac interactions to generate memories and then sending those memories to ChatGPT or Codex as context, you shouldn't turn on Computer History." Before enabling it, he excluded Passwords, 1Password and Keychain Access.

## The controls, and the gaps

OpenAI has front-loaded the consent machinery. Computer History is off by default for everyone. In Business and Enterprise workspaces an administrator must explicitly grant access first, and even then each member has to opt in individually — admin approval alone enables nothing. It also requires Memories to be on, and is unavailable in the European Economic Area, the United Kingdom and Switzerland.

Users can run an exclusion list or a stricter "include only these apps" allowlist covering apps and website URLs, pause collection from the macOS menu bar, and clear the last ten minutes, hour, day, or everything. Deleting a timeline item also deletes the underlying events and any memories derived from them.

The gap is what happens to the files once they exist. OpenAI's own documentation states that Computer History files "can contain sensitive information," that "they are not encrypted by Computer History," and that "other programs running as your macOS user may be able to access them." The memories are readable plaintext in a home directory, protected by nothing stronger than the Mac account itself.

## Why It Matters

The Microsoft Recall precedent is the obvious frame, and OpenAI has clearly studied it. When Recall shipped in 2024, security researcher Kevin Beaumont showed its database sat in plaintext in an AppData folder and could be lifted wholesale — "stealing everything you've ever typed or viewed on your own Windows PC is now possible with two lines of code," as he put it, calling the launch "an act of self harm at Microsoft in the name of AI, and by proxy real customer harm." Microsoft pulled the feature, made it opt-in, and rebuilt it around encryption and Windows Hello.

Computer History dodges the screenshot problem and lands opt-in from day one. But it swaps a visual archive for something arguably more useful to an attacker: a structured, pre-summarized, machine-readable account of what a person did, which files they touched and who they talked to — in plaintext, on disk.

The sharper issue is that this is not a passive log. It is agent context, wired into a system that can act. OpenAI says so itself, in a documentation section titled "Prompt injection risk": "Computer History increases the risk of prompt injection from content in apps and websites. For example, if you visit a website containing malicious instructions, ChatGPT or Codex might follow those instructions." Once a compromised page, a malicious browser extension or a poisoned document can write into the same event stream that becomes the agent's memory, the threat stops being data theft and becomes instruction smuggling. Tenable researchers have already catalogued multiple indirect prompt-injection paths into ChatGPT's existing memory system; Computer History widens the aperture.

## What to Watch

Three things. Whether OpenAI encrypts the memory directory or gates it behind Touch ID — the most obvious hardening move, and the one Microsoft was forced into. Whether the EEA, UK and Switzerland rollout arrives on the promised timeline or stalls under GDPR scrutiny, which would say a lot about how confident OpenAI's lawyers are in the events-not-screenshots distinction. And whether the first credible prompt injection landing through Computer History gets demonstrated in a researcher's lab or discovered on someone's actual laptop.
