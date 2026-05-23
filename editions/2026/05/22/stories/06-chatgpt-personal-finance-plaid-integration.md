# OpenAI Launches ChatGPT Personal Finance With Plaid Integration Across 12,000 Banks

*A year after Intuit killed Mint, OpenAI is stepping into the void — armed with GPT-5.5, a freshly acquired fintech team, and a data pipeline into nearly every bank account in America.*

---

On May 15, OpenAI launched a personal finance feature inside ChatGPT that lets Pro subscribers in the U.S. connect their bank accounts, credit cards, and investment portfolios directly to the chatbot. The integration, built on a partnership with Plaid, gives users a live financial dashboard covering portfolio performance, spending patterns, subscription tracking, and upcoming payments — all surfaced through natural-language conversation with a model that can reason about their actual numbers.

The move is OpenAI's most direct foray yet into the managed-money software market, a space that has been in turmoil since Intuit shut down Mint in early 2024 and scattered its 3.6 million users across competing apps. This time, the competitor entering the market is not another budgeting tool — it is the world's most widely used AI platform, arriving with 200 million existing users who already ask it financial questions every month.

---

## How It Works

Users access the feature by selecting "Finances" in the ChatGPT sidebar or typing "@Finances, connect my accounts" in any conversation. From there, Plaid's Link flow handles the authentication process, connecting to more than 12,000 financial institutions — including Chase, Fidelity, Charles Schwab, Robinhood, American Express, and Capital One. Once accounts are linked, ChatGPT can answer questions ranging from granular ("Has my spending on restaurants changed in the past three months?") to strategic ("Help me build a plan to be ready to buy a house in my area in five years").

The feature is powered by GPT-5.5 Thinking, OpenAI's most capable reasoning model, which the company says scored 60% on a custom FinanceAgent benchmark developed with more than 50 financial professionals. OpenAI noted that GPT-5.5 is specifically stronger at reasoning with context than prior models — a property that matters when parsing months of transaction history and mapping it to a user's stated goals.

On the security side, the integration is read-only: ChatGPT can see balances, transactions, investments, and liabilities, but cannot view full account numbers or initiate any changes to accounts. Users can disconnect accounts from Settings > Apps > Finances at any time, and disconnected data is fully removed from ChatGPT within 30 days. Users can also view and delete financial memories from within the Finances page.

---

## The Hiro Acquisition Behind the Product

The launch did not come out of nowhere. In April, OpenAI acquired the team behind Hiro, a two-year-old AI personal finance startup backed by Ribbit Capital, General Catalyst, and Restive Ventures. Hiro had been specifically training models to handle financial math with high accuracy, including a verification feature that let users audit the model's calculations. The startup shut down its product on April 20 and deleted all user data by May 13, with roughly 10 employees joining OpenAI.

OpenAI acknowledged that Hiro's expertise was useful in building the product but did not specify what percentage of the feature the acquired team built. This marks OpenAI's second fintech acquisition, following its purchase of personal finance app Roi in October 2025.

---

## Plaid's Strategic Read

For Plaid, the partnership is a flagship validation of a broader bet the company has made on AI as the next major distribution channel for its financial data infrastructure. Plaid CTO Will Robinson, writing on the company's blog, framed the partnership as the practical realization of a thesis he had outlined earlier in the year about "purpose-built infrastructure" for intelligent finance.

"Over 200 million people turn to ChatGPT with personal finance related questions every month," Robinson wrote. "Plaid's connectivity powers real-time answers, grounded in someone's actual accounts and cash flow."

Robinson also highlighted a specific technical capability Plaid brings to the partnership: its transaction foundation model, trained on de-identified data across the Plaid network, which the company says classifies income 48% more accurately than raw bank data alone. That accuracy uplift matters when ChatGPT is trying to distinguish freelance income from a transfer from a friend, or a recurring subscription from a one-time charge.

OpenAI Product Lead Ty Geri described the core value proposition simply: "Finances are deeply personal and shaped by individual goals, priorities, and everyday realities. But understanding the full picture of your personal finances can be difficult because information is spread across different apps, accounts and spreadsheets. With Plaid's secure, trusted way to connect financial accounts, ChatGPT helps people better understand where their money is going, spot patterns and tradeoffs, and make more informed decisions in the context of the life they want to build."

---

## The Privacy Question

The feature is already facing scrutiny. An industry lawsuit filed days after the launch cites data-sharing practices and argues that OpenAI, as an AI company rather than a regulated financial institution, is not subject to the same consumer protections that govern banks and credit unions. Chris Powell, head of deposits at Citizens Bank, offered a blunt assessment in coverage by American Banker: sharing nonpublic financial data with an AI company carries real risk precisely because those companies are not held to the same regulatory standards.

OpenAI has countered with its read-only access model and transparent deletion controls. The company has also positioned Plaid — an established, trusted intermediary with a decade of consumer financial connections — as a trust signal in its own right. Plaid's Portal product already lets users manage which apps have access to their data, independently of any individual app's interface.

Whether those safeguards will be sufficient for regulators — and whether consumers will care — will likely become clearer as the product moves beyond its Pro-only preview.

---

## The Competitive Landscape

OpenAI is not alone in spotting the opportunity. Perplexity launched a competing financial research product around the same time, built on its Computer agent architecture. Traditional fintech players, including the incumbent Intuit (which OpenAI plans to integrate as a future partner, enabling tax-impact analysis and credit approval modeling), are navigating the same AI transition. Ariana-Michele Moore, a strategic advisor at Datos Insights covering retail banking and payments, captured the directional shift: "The last decade of digital banking rewarded convenience. The next rewards control. AI is the inflection point: seeing your finances and finally knowing what to do about them."

Plaid's own consumer research reinforces the demand signal: 64% of consumers who have used AI for finances say it improved their ability to evaluate financial products, and 53% say it helped them manage day-to-day spending. More than half of Americans now say managing money without AI will soon feel outdated.

---

## What to Watch

The current rollout covers web and iOS for ChatGPT Pro subscribers in the U.S. OpenAI has said it will expand to Plus users after gathering feedback, though no timeline has been given. The planned Intuit integration — which would unlock tax modeling and credit analysis — is the capability most likely to define whether this feature evolves from a dashboard into something genuinely advisory.

The deeper question the product poses is one of positioning. OpenAI has been careful to frame this as a tool that helps users understand their finances, not give regulated financial advice. That distinction may become harder to maintain as the feature grows more capable and specific. The line between "here is what your spending patterns suggest" and "here is what you should do" is thin — and for 200 million people already asking ChatGPT for money guidance, it may already be a distinction without a practical difference.

---

*Sources: [TechCrunch](https://techcrunch.com/2026/05/15/openai-launches-chatgpt-for-personal-finance-will-let-you-connect-bank-accounts/), [OpenAI](https://openai.com/index/personal-finance-chatgpt/), [Plaid](https://plaid.com/blog/chatgpt-personal-finance-plaid/), [American Banker](https://www.americanbanker.com/news/openai-launches-personal-finance-tools-for-chatgpt-pro-users), [TechCrunch (Hiro acquisition)](https://techcrunch.com/2026/04/13/openai-has-bought-ai-personal-finance-startup-hiro/), [Engadget](https://www.engadget.com/2173768/chatgpt-will-offer-personalized-financial-advice-if-you-connect-your-bank-account/)*
