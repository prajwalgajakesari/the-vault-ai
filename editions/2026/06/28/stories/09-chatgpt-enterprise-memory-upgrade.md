OpenAI spent the back half of June quietly rewiring how its biggest paying customers actually use ChatGPT. Over a string of release notes, the company simplified the model picker for Business and Enterprise workspaces, deepened the memory that powers personalized responses, and — on June 26 — pulled GPT-4.5 out of the app entirely. Taken together, the changes point at a single ambition: make the most capable version of ChatGPT feel less like a menu of cryptic engine names and more like a tool that already knows your work.

The headline for enterprise admins is twofold. First, the model picker on web, iOS, and Android has been collapsed into a shorter, plainer-language set of choices oriented around speed versus reasoning effort. Second, the memory system that lets ChatGPT carry context across conversations is getting richer — and, crucially, more auditable — for the workspaces that have historically been most nervous about it.

## A simpler picker, and the end of "Thinking Light"

According to OpenAI's release notes, the redesigned picker drops the old "Thinking" nomenclature in favor of effort tiers. "Thinking Standard is now Medium, Thinking Extended is now High, and Thinking Heavy is now Extra High," the notes state for the consumer rollout that landed June 10. "Pro Standard and Pro Extended remain available under Pro. Thinking Light is no longer available." For Business and Enterprise, the same logic applies: the picker now surfaces Instant, Medium, High, Extra High, Pro Standard, and Pro Extended, with all six options available to Enterprise and Edu workspaces subject to workspace access settings.

OpenAI is explicit that this is an interface change, not a model change. The update makes it "easier to choose the balance of speed and reasoning effort that works best for your task," the notes say, "without changing the underlying models or usage limits." Instant can now automatically switch to Medium when a request benefits from more reasoning — a behavior users can toggle in settings. On mobile, the picker sits at the top of the conversation; on web, it lives in the message composer.

The retirement of "Thinking Light" is the small detail that says the most. It signals OpenAI's growing confidence that GPT-5.5 Instant — which the company described in a June 24 note as "our most-used model in ChatGPT" — is fast and cheap enough to serve as the default floor, removing the need for a separate ultra-light reasoning rung.

## Memory gets deeper, and a paper trail

The more consequential change for enterprises is memory. OpenAI's June 4 note described an upgrade so ChatGPT can "better keep your context up to date, helping responses stay more relevant," reducing "stale or contradictory saved memories." Memories are now updated automatically rather than only when a user manually saves them, and Plus and Pro users got twice as much memory capacity.

For Enterprise, the rollout came with guardrails that reflect how sensitive automatic memory is in a corporate setting. The improved memory draws richer context from past chats, surfaces a memory summary of what ChatGPT may use to personalize responses, and shows the sources beneath a personalized answer — so a user can see which past chats, memories, or custom instructions shaped a given response. Users can correct an entry, delete a referenced chat, mark a source as not relevant, or turn memory off. On the admin side, the feature shipped with roughly a two-week early-access window during which administrators could enable "Use improved memory" in workspace settings; after that period it turns on by default for eligible workspaces unless an admin opts out.

That sources-and-summary design is the tell. Enterprises balk at black-box personalization; an auditable memory that shows its work — and gives admins an opt-out — is OpenAI's attempt to make automatic memory palatable to legal and security teams.

## The personalization race, and what model consolidation signals

The memory push lands squarely in a three-way contest. Anthropic has leaned on long-context Projects and connected knowledge for Claude, while Google has wired Gemini into the Workspace corpus of Gmail, Docs, and Drive — a structural personalization advantage OpenAI lacks. OpenAI's counter is conversational memory that compounds over time inside ChatGPT itself, paired with the transparency controls that enterprise buyers demand. Whoever makes "the assistant that already knows your context" both useful and governable wins the seat-by-seat enterprise market.

The model-picker simplification points the same direction. For most of the past two years, OpenAI's lineup ballooned into an alphabet soup that confused even sophisticated users. Folding those names into effort tiers — and retiring GPT-4.5 on June 26, with existing conversations automatically continuing on GPT-5.5 — is a deliberate move toward a world where users pick how hard the model should think rather than which model to summon. (The GPT-4.5 retirement, announced May 28, applies to ChatGPT only; OpenAI says there are no changes to the API.)

## What to watch

Three things. First, whether the improved Enterprise memory clears procurement: the opt-out-by-default posture and source-level transparency will be scrutinized by data-governance teams, and adoption numbers — which OpenAI has not disclosed — will tell the real story. Second, whether effort-based tiers stick across the industry or whether buyers still want to pin specific model versions for reproducibility and compliance. And third, how aggressively OpenAI keeps pruning its model roster: GPT-4.5 lasted barely four months. If the cadence holds, the next consolidation is already on the calendar.
