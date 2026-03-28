<p align="center">
  <img src="https://img.shields.io/badge/AI-Daily%20Newsletter-8b5cf6?style=for-the-badge&logo=openai&logoColor=white" alt="AI Newsletter" />
  <img src="https://img.shields.io/badge/stories-15--20%20daily-06b6d4?style=for-the-badge" alt="15-20 stories" />
  <img src="https://img.shields.io/badge/updated-every%20morning-f59e0b?style=for-the-badge" alt="Updated daily" />
</p>

<h1 align="center">The Vault — AI Edition</h1>

<p align="center">
  <strong>Your daily curated intelligence brief on the world of artificial intelligence.</strong><br/>
  15-20 hand-picked stories every morning — covering models, research, business, and policy.
</p>

<p align="center">
  <a href="#-whats-inside">What's Inside</a> •
  <a href="#-how-to-read">How to Read</a> •
  <a href="#-repository-structure">Repo Structure</a> •
  <a href="#-categories">Categories</a> •
  <a href="archive/index.md">Archive</a>
</p>

---

## 🎯 What's Inside

Every morning at 8 AM, the previous day's most important AI developments are researched, written up, and published here. No fluff, no filler — just the stories that matter.

Each edition includes:

- **Individual story pages** — every story gets its own Markdown and beautifully styled HTML file
- **Daily digest** — a single-page overview of all stories in Markdown
- **Styled edition** — a premium dark-themed HTML page with all stories, designed for comfortable reading
- **Structured metadata** — a JSON file indexing every story for programmatic access

---

## 📖 How to Read

| Format | File | Best For |
|--------|------|----------|
| Quick scan | `digest.md` | Skim headlines and summaries in Markdown |
| Full experience | `index.html` | Read the styled daily edition in your browser |
| Deep dive | `stories/*.html` | Read individual stories as standalone pages |
| Build with it | `metadata.json` | Programmatic access to all story data |

**Jump to the latest edition →** Check the [`editions/`](editions/) folder or browse the [archive](archive/index.md).

---

## 🗂 Repository Structure

```
the-vault-ai/
│
├── editions/                         # All published editions
│   └── 2026/
│       └── 03/
│           └── 29/
│               ├── index.html        # Styled daily edition page
│               ├── digest.md         # Markdown digest of all stories
│               ├── metadata.json     # Edition metadata & story index
│               └── stories/
│                   ├── 01-story-slug.md
│                   ├── 01-story-slug.html
│                   ├── 02-story-slug.md
│                   ├── 02-story-slug.html
│                   └── ...
│
├── archive/
│   └── index.md                      # Running log of all editions
│
├── LICENSE
└── README.md
```

---

## 🏷 Categories

Each story is tagged with one of four categories:

| Category | Color | Covers |
|----------|-------|--------|
| **LLMs & GenAI** | 🟣 Purple | Model releases, tool updates, prompt engineering, ChatGPT/Claude/Gemini/Llama |
| **Research** | 🔵 Cyan | Papers, benchmarks, breakthroughs from top labs and academia |
| **Business** | 🟡 Amber | Funding, acquisitions, product launches, enterprise adoption |
| **Policy** | 🔴 Red | Regulation, AI safety, ethics, open vs. closed source debates |

---

## ⚡ How It Works

1. **Research** — 8-10 targeted web searches covering all categories from the previous day
2. **Curate** — Filter down to the 15-20 most significant stories
3. **Write** — Each story gets an editorial-quality write-up with source attribution
4. **Design** — Stories are published as both Markdown and styled HTML with a dark editorial theme
5. **Publish** — Each file is committed individually and pushed to this repo

---

## 📊 Stats

Every edition produces:

- **15-20** individual stories
- **30-40+** files per day (MD + HTML for each story, plus digest, index, and metadata)
- **25-40+** granular commits per edition
- **4** content categories covered

---

## 📜 License

MIT — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <sub>Curated daily by <a href="https://github.com/prajwalgajakesari">prajwalgajakesari</a></sub>
</p>
