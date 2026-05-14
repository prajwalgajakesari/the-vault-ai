#!/usr/bin/env python3
import json, pathlib, re, html as html_mod

EDITION_DIR = pathlib.Path.home() / "Projects/the-vault-ai/editions/2026/05/13"
STORIES_DIR = EDITION_DIR / "stories"

with open(EDITION_DIR / "metadata.json") as f:
    meta = json.load(f)

CATEGORY_COLORS = {"business": "#e8a735", "llms-genai": "#a78bfa", "research": "#5eead4", "policy": "#fb7185"}
CATEGORY_LABELS = {"business": "Business", "llms-genai": "LLMs &amp; GenAI", "research": "Research", "policy": "Policy"}
CATEGORY_ICONS = {
    "business": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "llms-genai": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>',
    "research": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "policy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
}

FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800&display=swap" rel="stylesheet">'

CSS_VARS = """:root {
  --bg: #101014; --surface: #18181c; --text: #b8b8bf; --text-strong: #ececef;
  --text-muted: #5a5a63; --accent: #c084fc;
  --business: #e8a735; --llms-genai: #a78bfa; --research: #5eead4; --policy: #fb7185;
}"""

def md_to_html(md_text):
    lines = md_text.strip().split("\n")
    if lines and lines[0].strip() == "---":
        end = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end = i
                break
        if end > 0:
            lines = lines[end+1:]
    out = []
    in_list = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        if stripped.startswith("## "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f'<h2>{inline_md(stripped[3:])}</h2>')
        elif stripped.startswith("# "):
            continue
        elif stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f'<li>{inline_md(stripped[2:])}</li>')
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f'<p>{inline_md(stripped)}</p>')
    if in_list:
        out.append("</ul>")
    return "\n".join(out)

def inline_md(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def add_drop_cap(body_html):
    return body_html.replace("<p>", '<p class="drop-cap">', 1)

COMMON_CSS = CSS_VARS + """
* { margin:0; padding:0; box-sizing:border-box; }
body { background:var(--bg); color:var(--text); font-family:'DM Sans',sans-serif; line-height:1.6; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
.container { max-width:740px; margin:0 auto; padding:0 24px; }
"""

ARTICLE_CSS = COMMON_CSS + """
/* NAV */
.top-nav { position:sticky; top:0; z-index:100; background:rgba(16,16,20,0.92); backdrop-filter:blur(12px); border-bottom:1px solid rgba(255,255,255,0.06); padding:14px 0; }
.top-nav .container { display:flex; justify-content:space-between; align-items:center; }
.top-nav .back { display:flex; align-items:center; gap:6px; color:var(--text-muted); font-size:14px; }
.top-nav .back:hover { color:var(--text); }
.top-nav .brand { font-weight:700; font-size:14px; letter-spacing:2px; color:var(--text-muted); }
/* PROGRESS */
.progress-bar { position:fixed; top:0; left:0; height:3px; background:var(--accent); z-index:200; transition:width .1s; width:0%; }
/* HERO */
.article-hero { padding:60px 0 40px; }
.cat-tag { display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:1.5px; padding:5px 12px; border-radius:20px; margin-bottom:20px; }
.cat-tag svg { width:14px; height:14px; }
h1 { font-family:'Source Serif 4',serif; font-size:clamp(28px,5vw,42px); font-weight:700; color:var(--text-strong); line-height:1.2; margin-bottom:16px; }
.meta-row { display:flex; gap:20px; color:var(--text-muted); font-size:13px; }
/* TAKEAWAY */
.takeaway { background:var(--surface); border-left:3px solid var(--accent); border-radius:0 8px 8px 0; padding:20px 24px; margin:32px 0; }
.takeaway-label { font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:var(--accent); margin-bottom:8px; }
.takeaway p { color:var(--text-strong); font-family:'Source Serif 4',serif; font-size:17px; line-height:1.6; }
/* BODY */
.article-body { font-family:'Source Serif 4',serif; font-size:17px; line-height:1.8; color:var(--text); }
.article-body h2 { font-family:'DM Sans',sans-serif; font-size:20px; font-weight:700; color:var(--text-strong); margin:36px 0 16px; }
.article-body p { margin-bottom:20px; }
.article-body ul { margin:0 0 20px 24px; }
.article-body li { margin-bottom:8px; }
.article-body .drop-cap::first-letter { font-size:3.4em; float:left; line-height:0.8; margin:4px 10px 0 0; color:var(--text-strong); font-weight:700; }
/* PULL QUOTE */
.pull-quote { border-left:3px solid var(--accent); padding:24px 0 24px 28px; margin:36px 0; }
.pull-quote blockquote { font-family:'Source Serif 4',serif; font-size:20px; font-style:italic; color:var(--text-strong); line-height:1.5; margin-bottom:12px; }
.pull-quote cite { font-size:13px; color:var(--text-muted); font-style:normal; }
/* DATA STRIP */
.data-strip { display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:1px; background:rgba(255,255,255,0.04); border-radius:10px; overflow:hidden; margin:36px 0; }
.stat-cell { background:var(--surface); padding:20px; text-align:center; }
.stat-val { font-size:24px; font-weight:800; color:var(--text-strong); }
.stat-label { font-size:12px; color:var(--text-muted); margin-top:4px; }
/* SOURCES */
.sources-section { margin:40px 0; padding-top:32px; border-top:1px solid rgba(255,255,255,0.06); }
.sources-section h3 { font-size:14px; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:var(--text-muted); margin-bottom:16px; }
.source-list { list-style:none; }
.source-list li { margin-bottom:10px; }
.source-list a { display:inline-flex; align-items:center; gap:8px; font-size:14px; }
.source-list img { width:16px; height:16px; border-radius:2px; }
/* PREV/NEXT */
.article-nav { display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:40px 0; padding-top:32px; border-top:1px solid rgba(255,255,255,0.06); }
.article-nav a { display:block; background:var(--surface); border-radius:10px; padding:20px; font-size:14px; color:var(--text); }
.article-nav a:hover { background:rgba(255,255,255,0.05); text-decoration:none; }
.article-nav .label { font-size:11px; text-transform:uppercase; letter-spacing:1px; color:var(--text-muted); margin-bottom:6px; }
.article-nav .next { text-align:right; }
/* FOOTER */
footer { border-top:1px solid rgba(255,255,255,0.06); padding:32px 0; margin-top:40px; text-align:center; color:var(--text-muted); font-size:13px; }
"""

INDEX_CSS = COMMON_CSS.replace("max-width:740px", "max-width:960px") + """
.edition-header { padding:64px 0 40px; text-align:center; }
.overline { font-size:11px; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:var(--accent); margin-bottom:12px; }
.edition-header h1 { font-family:'Source Serif 4',serif; font-size:clamp(28px,5vw,44px); color:var(--text-strong); margin-bottom:8px; }
.edition-header .date { font-size:16px; color:var(--text-muted); }
/* STATS ROW */
.stats-row { display:flex; justify-content:center; gap:40px; padding:20px 0 40px; border-bottom:1px solid rgba(255,255,255,0.06); margin-bottom:40px; }
.stats-row .stat { text-align:center; }
.stats-row .stat-val { font-size:28px; font-weight:800; color:var(--text-strong); }
.stats-row .stat-label { font-size:12px; color:var(--text-muted); }
/* FEATURED */
.featured-card { background:var(--surface); border-radius:14px; padding:36px; margin-bottom:48px; border:1px solid rgba(255,255,255,0.06); }
.featured-label { font-size:11px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--accent); margin-bottom:16px; }
.featured-card h2 { font-family:'Source Serif 4',serif; font-size:clamp(22px,4vw,32px); color:var(--text-strong); line-height:1.25; margin-bottom:12px; }
.featured-card h2 a { color:var(--text-strong); }
.featured-card h2 a:hover { color:var(--accent); text-decoration:none; }
.featured-card .excerpt { font-size:15px; color:var(--text); margin-bottom:16px; line-height:1.6; }
.featured-card .card-meta { font-size:13px; color:var(--text-muted); }
/* FILTERS */
.filters { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:36px; }
.filters button { background:var(--surface); border:1px solid rgba(255,255,255,0.08); color:var(--text-muted); font-family:'DM Sans',sans-serif; font-size:13px; font-weight:600; padding:7px 16px; border-radius:20px; cursor:pointer; transition:all .2s; }
.filters button:hover, .filters button.active { color:var(--text-strong); border-color:var(--accent); background:rgba(192,132,252,0.1); }
/* CATEGORY SECTIONS */
.cat-section { margin-bottom:48px; }
.cat-section-header { display:flex; align-items:center; gap:10px; margin-bottom:20px; }
.cat-section-header svg { width:20px; height:20px; }
.cat-section-header h2 { font-size:18px; font-weight:700; }
/* STORY CARDS */
.story-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:16px; }
.story-card { background:var(--surface); border-radius:10px; padding:24px; border:1px solid rgba(255,255,255,0.04); transition:border-color .2s; }
.story-card:hover { border-color:rgba(255,255,255,0.12); }
.story-card .cat-badge { font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; display:inline-flex; align-items:center; gap:5px; }
.story-card .cat-badge svg { width:12px; height:12px; }
.story-card h3 { font-family:'Source Serif 4',serif; font-size:16px; font-weight:600; color:var(--text-strong); line-height:1.35; margin-bottom:8px; }
.story-card h3 a { color:var(--text-strong); }
.story-card h3 a:hover { color:var(--accent); text-decoration:none; }
.story-card .excerpt { font-size:13px; color:var(--text-muted); line-height:1.5; margin-bottom:10px; }
.story-card .card-meta { font-size:12px; color:var(--text-muted); }
/* FOOTER */
footer { border-top:1px solid rgba(255,255,255,0.06); padding:32px 0; margin-top:40px; text-align:center; color:var(--text-muted); font-size:13px; }
footer a { color:var(--accent); }
"""

def hex_to_rgba(hex_color, alpha):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return f"rgba({r},{g},{b},{alpha})"

# ===== ARTICLE PAGE GENERATOR =====
def gen_article_page(story, idx, stories):
    cat = story["category"]
    cat_color = CATEGORY_COLORS[cat]
    cat_label = CATEGORY_LABELS[cat]
    cat_icon = CATEGORY_ICONS[cat]
    slug = story["slug"]

    md_path = STORIES_DIR / f'{story["story_number"]}-{slug}.md'
    md_text = md_path.read_text()
    body_html = md_to_html(md_text)
    body_html = add_drop_cap(body_html)

    cat_bg = hex_to_rgba(cat_color, 0.12)

    # Pull quote
    pq_html = ""
    if story.get("pull_quote"):
        pq = story["pull_quote"]
        pq_html = f'''<div class="pull-quote">
  <blockquote>&ldquo;{html_mod.escape(pq["text"])}&rdquo;</blockquote>
  <cite>&mdash; {html_mod.escape(pq["attribution"])}, {html_mod.escape(pq["role"])}</cite>
</div>'''

    # Data strip
    ds_html = ""
    if story.get("data_points"):
        cells = "\n".join(
            f'<div class="stat-cell"><div class="stat-val">{html_mod.escape(d["value"])}</div><div class="stat-label">{html_mod.escape(d["label"])}</div></div>'
            for d in story["data_points"]
        )
        ds_html = f'<div class="data-strip">{cells}</div>'

    # Sources
    src_html = ""
    if story.get("sources"):
        items = "\n".join(
            f'<li><a href="{s["url"]}" target="_blank" rel="noopener"><img src="https://www.google.com/s2/favicons?domain={s["domain"]}&amp;sz=32" alt="">{html_mod.escape(s["name"])}</a></li>'
            for s in story["sources"]
        )
        src_html = f'<div class="sources-section"><h3>Sources ({len(story["sources"])})</h3><ul class="source-list">{items}</ul></div>'

    # Prev/next
    nav_parts = []
    if idx > 0:
        ps = stories[idx-1]
        nav_parts.append(f'<a href="{ps["slug"]}.html"><div class="label">&larr; Previous</div>{html_mod.escape(ps["headline"][:60])}</a>')
    else:
        nav_parts.append('<div></div>')
    if idx < len(stories)-1:
        ns = stories[idx+1]
        nav_parts.append(f'<a href="{ns["slug"]}.html" class="next"><div class="label">Next &rarr;</div>{html_mod.escape(ns["headline"][:60])}</a>')
    else:
        nav_parts.append('<div></div>')
    nav_html = f'<div class="article-nav">{nav_parts[0]}{nav_parts[1]}</div>'

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(story["headline"])} | The Vault AI</title>
{FONT_LINK}
<style>{ARTICLE_CSS}</style>
</head>
<body>
<div class="progress-bar" id="progress"></div>
<nav class="top-nav"><div class="container">
  <a href="index.html" class="back">&larr; Back to edition</a>
  <div class="brand">THE VAULT</div>
</div></nav>

<main class="container">
<div class="article-hero">
  <div class="cat-tag" style="color:{cat_color};background:{cat_bg}">{cat_icon} {cat_label}</div>
  <h1>{html_mod.escape(story["headline"])}</h1>
  <div class="meta-row">
    <span>{story["reading_time_min"]} min read</span>
    <span>{story["word_count"]:,} words</span>
    <span>{len(story.get("sources",[]))} sources</span>
  </div>
</div>

<div class="takeaway">
  <div class="takeaway-label">Key Takeaway</div>
  <p>{html_mod.escape(story["key_takeaway"])}</p>
</div>

<article class="article-body">
{body_html}
</article>

{pq_html}
{ds_html}
{src_html}
{nav_html}
</main>

<footer><div class="container">&copy; 2026 The Vault AI &middot; <a href="https://news.promtvault.app">news.promtvault.app</a></div></footer>

<script>
window.addEventListener('scroll',function(){{
  var h=document.documentElement;
  var pct=(h.scrollTop/(h.scrollHeight-h.clientHeight))*100;
  document.getElementById('progress').style.width=pct+'%';
}});
</script>
</body></html>'''
    return page

# ===== INDEX PAGE GENERATOR =====
def gen_index_page():
    stories = meta["stories"]
    featured = stories[0]
    fc = featured["category"]
    fc_color = CATEGORY_COLORS[fc]

    cats_order = ["business","llms-genai","research","policy"]
    cat_sections = ""
    for cat in cats_order:
        cat_stories = [s for s in stories if s["category"] == cat]
        if not cat_stories:
            continue
        color = CATEGORY_COLORS[cat]
        icon = CATEGORY_ICONS[cat]
        label = CATEGORY_LABELS[cat]
        cards = ""
        for s in cat_stories:
            cards += f'''<div class="story-card" data-cat="{cat}">
  <div class="cat-badge" style="color:{color}">{icon} {label}</div>
  <h3><a href="{s["slug"]}.html">{html_mod.escape(s["headline"])}</a></h3>
  <p class="excerpt">{html_mod.escape(s.get("article_excerpt","")[:120])}</p>
  <div class="card-meta">{s["reading_time_min"]} min &middot; {s["word_count"]:,} words &middot; {len(s.get("sources",[]))} sources</div>
</div>'''
        cat_sections += f'''<div class="cat-section" data-cat="{cat}">
  <div class="cat-section-header" style="color:{color}">{icon}<h2>{label}</h2></div>
  <div class="story-grid">{cards}</div>
</div>
'''

    filter_btns = '<button class="active" onclick="filterCat(\'all\')">All</button>'
    for cat in cats_order:
        if meta["categories"].get(cat, 0) > 0:
            color = CATEGORY_COLORS[cat]
            label = CATEGORY_LABELS[cat]
            filter_btns += f'<button onclick="filterCat(\'{cat}\')" style="--fc:{color}">{label} ({meta["categories"][cat]})</button>'

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Vault AI &middot; {html_mod.escape(meta["display_date"])}</title>
{FONT_LINK}
<style>{INDEX_CSS}</style>
</head>
<body>

<div class="container">
<div class="edition-header">
  <div class="overline">DAILY INTELLIGENCE BRIEF</div>
  <h1>The Vault AI</h1>
  <div class="date">{meta["day_of_week"]}, {meta["display_date"]}</div>
</div>

<div class="stats-row">
  <div class="stat"><div class="stat-val">{meta["story_count"]}</div><div class="stat-label">Stories</div></div>
  <div class="stat"><div class="stat-val">{meta["total_words"]:,}</div><div class="stat-label">Words</div></div>
  <div class="stat"><div class="stat-val">{meta["total_reading_time_min"]}</div><div class="stat-label">Min Read</div></div>
</div>

<div class="featured-card" style="border-left:3px solid {fc_color}">
  <div class="featured-label">Featured Story</div>
  <h2><a href="{featured["slug"]}.html">{html_mod.escape(featured["headline"])}</a></h2>
  <p class="excerpt">{html_mod.escape(featured.get("article_excerpt",""))}</p>
  <div class="card-meta">{featured["reading_time_min"]} min read &middot; {featured["word_count"]:,} words &middot; {len(featured.get("sources",[]))} sources</div>
</div>

<div class="filters">{filter_btns}</div>

{cat_sections}
</div>

<footer><div class="container">&copy; 2026 The Vault AI &middot; <a href="https://news.promtvault.app">news.promtvault.app</a></div></footer>

<script>
function filterCat(cat) {{
  document.querySelectorAll('.filters button').forEach(function(b){{b.classList.remove('active')}});
  event.target.classList.add('active');
  document.querySelectorAll('.cat-section').forEach(function(s){{
    s.style.display=(cat==='all'||s.dataset.cat===cat)?'':'none';
  }});
}}
</script>
</body></html>'''
    return page

# ===== DIGEST GENERATOR =====
def gen_digest():
    lines = []
    lines.append("# The Vault AI -- Daily Digest")
    lines.append(f"**{meta['day_of_week']}, {meta['display_date']}** | {meta['story_count']} stories | {meta['total_words']:,} words | {meta['total_reading_time_min']} min total read time")
    lines.append("")
    lines.append("---")
    lines.append("")

    cats_order = ["business","llms-genai","research","policy"]
    cat_plain = {"business":"Business","llms-genai":"LLMs & GenAI","research":"Research","policy":"Policy"}
    for cat in cats_order:
        cat_stories = [s for s in meta["stories"] if s["category"] == cat]
        if not cat_stories:
            continue
        lines.append(f"## {cat_plain[cat]}")
        lines.append("")
        for s in cat_stories:
            lines.append(f"### {s['headline']}")
            lines.append(f"*{s['reading_time_min']} min read | {s['word_count']:,} words | {len(s.get('sources',[]))} sources*")
            lines.append("")
            lines.append(f"**Key Takeaway:** {s['key_takeaway']}")
            lines.append("")
            if s.get("data_points"):
                for dp in s["data_points"]:
                    lines.append(f"- **{dp['value']}** -- {dp['label']}")
                lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("*Generated by [The Vault AI](https://news.promtvault.app)*")
    return "\n".join(lines)

# ===== MAIN =====
if __name__ == "__main__":
    stories = meta["stories"]
    for i, story in enumerate(stories):
        html_content = gen_article_page(story, i, stories)
        out_path = EDITION_DIR / f'{story["slug"]}.html'
        out_path.write_text(html_content)
        print(f"  [article] {out_path.name}")

    index_html = gen_index_page()
    (EDITION_DIR / "index.html").write_text(index_html)
    print("  [index] index.html")

    digest_md = gen_digest()
    (EDITION_DIR / "digest.md").write_text(digest_md)
    print("  [digest] digest.md")

    print("DONE")
