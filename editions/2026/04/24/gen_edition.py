import json, pathlib, re

EDITION_DIR = pathlib.Path('~/Projects/the-vault-ai/editions/2026/04/24').expanduser()
meta = json.loads((EDITION_DIR / 'metadata.json').read_text())

CATEGORY_COLORS = {'business': '#e8a735', 'llms-genai': '#a78bfa', 'research': '#5eead4', 'policy': '#fb7185'}
CATEGORY_ICONS = {
    'business': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    'llms-genai': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg>',
    'research': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    'policy': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
}
FONTS_LINK = '<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800&display=swap" rel="stylesheet">'

def md_to_html(md_text):
    html_parts = []
    for para in md_text.strip().split('\n\n'):
        para = para.strip()
        if not para:
            continue
        if para.startswith('# '):
            continue
        if para.startswith('## '):
            html_parts.append(f'<h2>{para[3:]}</h2>')
        elif para.startswith('### '):
            html_parts.append(f'<h3>{para[4:]}</h3>')
        else:
            para = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', para)
            para = re.sub(r'\*(.+?)\*', r'<em>\1</em>', para)
            html_parts.append(f'<p>{para}</p>')
    return '\n'.join(html_parts)

stories = meta['stories']

ARTICLE_CSS = """
:root{--bg:#101014;--surface:#18181c;--surface-2:#1f1f24;--border:rgba(255,255,255,.07);--border-hover:rgba(255,255,255,.14);--text:#b8b8bf;--text-strong:#ececef;--text-muted:#5a5a63;--accent:#c084fc;--cat-color:CAT_COLOR}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--text);font-family:'Source Serif 4',Georgia,serif;line-height:1.7}
nav{position:sticky;top:0;z-index:100;backdrop-filter:blur(12px);background:rgba(16,16,20,.85);border-bottom:1px solid var(--border);padding:.75rem 2rem;display:flex;align-items:center;gap:1rem;font-family:'DM Sans',sans-serif}
nav a{color:var(--text-muted);text-decoration:none;font-size:.85rem;display:flex;align-items:center;gap:.35rem}
nav a:hover{color:var(--text-strong)}nav svg{width:16px;height:16px}
nav .brand{color:var(--text-strong);font-weight:700;letter-spacing:.08em;font-size:.85rem;margin-left:auto}
.article-header{max-width:720px;margin:3rem auto 0;padding:0 1.5rem}
.cat-tag{display:inline-flex;align-items:center;gap:.4rem;font-family:'DM Sans',sans-serif;font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--cat-color);background:color-mix(in srgb,var(--cat-color) 10%,transparent);padding:.3rem .7rem;border-radius:4px}
.cat-tag svg{width:14px;height:14px}
.article-header h1{font-family:'DM Sans',sans-serif;font-size:2.2rem;font-weight:800;color:var(--text-strong);line-height:1.2;margin:.8rem 0}
.meta-row{display:flex;flex-wrap:wrap;gap:1rem;font-family:'DM Sans',sans-serif;font-size:.8rem;color:var(--text-muted);margin:1rem 0 2rem;align-items:center}
.meta-row span{display:flex;align-items:center;gap:.3rem}.meta-row svg{width:14px;height:14px}
.takeaway{max-width:720px;margin:0 auto 2rem;padding:1rem 1.5rem;background:color-mix(in srgb,var(--cat-color) 5%,var(--surface));border-radius:8px;border:1px solid color-mix(in srgb,var(--cat-color) 15%,transparent);font-family:'DM Sans',sans-serif}
.takeaway .label{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--cat-color);display:flex;align-items:center;gap:.35rem;margin-bottom:.4rem}
.takeaway .label svg{width:14px;height:14px}.takeaway p{font-size:.9rem;color:var(--text-strong)}
.article-body{max-width:720px;margin:0 auto;padding:0 1.5rem}
.article-body p{margin-bottom:1.3rem;font-size:1.05rem}
.article-body p:first-of-type::first-letter{font-size:3.2em;float:left;line-height:.8;margin:.05em .12em 0 0;font-weight:700;color:var(--text-strong)}
.article-body h2{font-family:'DM Sans',sans-serif;font-size:1.3rem;font-weight:700;color:var(--text-strong);margin:2rem 0 .8rem}
.article-body h3{font-family:'DM Sans',sans-serif;font-size:1.1rem;font-weight:600;color:var(--text-strong);margin:1.5rem 0 .6rem}
.pull-quote{margin:2rem 0;padding:1rem 1.5rem;border-radius:6px;background:var(--surface)}
.pull-quote blockquote{font-style:italic;font-size:1.1rem;color:var(--text-strong);margin-bottom:.4rem}
.pull-quote cite{font-family:'DM Sans',sans-serif;font-size:.8rem;color:var(--text-muted);font-style:normal}
.data-strip{display:flex;gap:1rem;flex-wrap:wrap;margin:2rem 0;padding:1rem 0}
.stat-cell{flex:1;min-width:100px;text-align:center;padding:.8rem;background:var(--surface);border-radius:6px}
.stat-value{font-family:'DM Sans',sans-serif;font-size:1.4rem;font-weight:700;color:var(--text-strong)}
.stat-label{font-family:'DM Sans',sans-serif;font-size:.7rem;color:var(--text-muted);margin-top:.2rem}
.sources{max-width:720px;margin:2rem auto;padding:1.5rem;border-top:1px solid var(--border)}
.sources h3{font-family:'DM Sans',sans-serif;font-size:.85rem;font-weight:600;color:var(--text-strong);margin-bottom:.8rem}
.source-list{display:flex;flex-wrap:wrap;gap:.6rem}
.source-list a{display:flex;align-items:center;gap:.4rem;padding:.35rem .7rem;background:var(--surface);border:1px solid var(--border);border-radius:4px;font-family:'DM Sans',sans-serif;font-size:.8rem;color:var(--text);text-decoration:none}
.source-list a:hover{border-color:var(--border-hover);color:var(--text-strong)}
.source-list img{width:16px;height:16px;border-radius:2px}
.article-nav{max-width:720px;margin:2rem auto;padding:1.5rem;display:flex;justify-content:space-between;gap:1rem;border-top:1px solid var(--border)}
.article-nav a{font-family:'DM Sans',sans-serif;font-size:.85rem;color:var(--text-muted);text-decoration:none}
.article-nav a:hover{color:var(--text-strong)}
footer{text-align:center;padding:2rem;font-family:'DM Sans',sans-serif;font-size:.75rem;color:var(--text-muted);border-top:1px solid var(--border);margin-top:2rem}
.progress-bar{position:fixed;top:0;left:0;height:2px;background:var(--cat-color);z-index:200;transition:width .1s}
"""

for i, story in enumerate(stories):
    slug = story['slug']
    num = story['story_number']
    cat = story['category']
    color = CATEGORY_COLORS.get(cat, '#c084fc')
    cat_icon = CATEGORY_ICONS.get(cat, '')
    md_file = EDITION_DIR / 'stories' / f'{num}-{slug}.md'
    if not md_file.exists():
        print(f'SKIP {num}-{slug}.md not found')
        continue
    article_html = md_to_html(md_file.read_text())
    pq = story.get('pull_quote', {})
    pull_quote_html = ''
    if pq and pq.get('text'):
        pull_quote_html = f'<div class="pull-quote" style="border-left:2px solid {color}"><blockquote>&ldquo;{pq["text"]}&rdquo;</blockquote><cite>&mdash; {pq.get("attribution","")}, {pq.get("role","")}</cite></div>'
    dp = story.get('data_points', [])
    data_strip_html = ''
    if dp:
        cells = ''.join(f'<div class="stat-cell"><div class="stat-value">{d["value"]}</div><div class="stat-label">{d["label"]}</div></div>' for d in dp)
        data_strip_html = f'<div class="data-strip" style="border-top:1px solid {color}20">{cells}</div>'
    sources = story.get('sources', [])
    source_links = ''.join(f'<a href="{s["url"]}" target="_blank" rel="noopener"><img src="https://www.google.com/s2/favicons?domain={s["domain"]}&sz=32" alt="">{s["name"]}</a>' for s in sources)
    sources_html = f'<div class="sources"><h3>Sources</h3><div class="source-list">{source_links}</div></div>' if sources else ''
    prev_link = ''
    next_link = ''
    if i > 0:
        ps = stories[i-1]
        prev_link = f'<a href="{ps["story_number"]}-{ps["slug"]}.html" class="nav-prev">&larr; {ps["headline"][:50]}</a>'
    if i < len(stories) - 1:
        ns = stories[i+1]
        next_link = f'<a href="{ns["story_number"]}-{ns["slug"]}.html" class="nav-next">{ns["headline"][:50]} &rarr;</a>'

    css = ARTICLE_CSS.replace('CAT_COLOR', color)
    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{story["headline"]} &mdash; The Vault AI</title>
{FONTS_LINK}
<style>{css}</style></head><body>
<div class="progress-bar" id="pb"></div>
<nav>
  <a href="../index.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg> Back</a>
  <span class="brand">THE VAULT</span>
</nav>
<header class="article-header">
  <span class="cat-tag">{cat_icon} {cat.replace('-',' ').title()}</span>
  <h1>{story["headline"]}</h1>
  <div class="meta-row">
    <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> {story.get("reading_time_min",4)} min read</span>
    <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg> {story.get("word_count",800)} words</span>
    <span>{len(sources)} sources</span>
  </div>
</header>
<div class="takeaway">
  <div class="label"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg> KEY TAKEAWAY</div>
  <p>{story.get("key_takeaway","")}</p>
</div>
<div class="article-body">
{article_html}
{pull_quote_html}
{data_strip_html}
</div>
{sources_html}
<div class="article-nav">{prev_link}{next_link}</div>
<footer>The Vault &mdash; AI Edition &middot; Published {meta["display_date"]}</footer>
<script>window.addEventListener("scroll",function(){{var e=document.documentElement,t=e.scrollTop,s=e.scrollHeight-e.clientHeight;document.getElementById("pb").style.width=(t/s*100)+"%"}});</script>
</body></html>'''
    out = EDITION_DIR / 'stories' / f'{num}-{slug}.html'
    out.write_text(html)
    print(f'OK {num}-{slug}.html')

print('Story HTML done. Building index...')

# --- index.html ---
stats_total_words = meta.get('total_words', 0)
stats_reading_time = meta.get('total_reading_time_min', 0)
cats = meta.get('categories', {})

INDEX_CSS = """
:root{--bg:#101014;--surface:#18181c;--surface-2:#1f1f24;--border:rgba(255,255,255,.07);--border-hover:rgba(255,255,255,.14);--text:#b8b8bf;--text-strong:#ececef;--text-muted:#5a5a63;--accent:#c084fc}
*{margin:0;padding:0;box-sizing:border-box}body{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif}
nav{position:sticky;top:0;z-index:100;backdrop-filter:blur(12px);background:rgba(16,16,20,.85);border-bottom:1px solid var(--border);padding:.75rem 2rem;display:flex;align-items:center;gap:1rem}
nav a{color:var(--text-muted);text-decoration:none;font-size:.85rem;display:flex;align-items:center;gap:.35rem}nav a:hover{color:var(--text-strong)}
nav svg{width:16px;height:16px}nav .brand{color:var(--text-strong);font-weight:700;letter-spacing:.08em;font-size:.85rem}nav .nav-right{margin-left:auto;display:flex;gap:1rem}
.edition-header{text-align:center;padding:3rem 1.5rem 1.5rem}
.edition-header .overline{font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.15em;color:var(--accent)}
.edition-header h1{font-size:2rem;font-weight:800;color:var(--text-strong);margin:.5rem 0}
.edition-header .date-line{font-size:.9rem;color:var(--text-muted)}
.stats-row{display:flex;justify-content:center;gap:1.5rem;padding:1rem;flex-wrap:wrap}
.stats-row .chip{display:flex;align-items:center;gap:.35rem;padding:.3rem .7rem;background:var(--surface);border:1px solid var(--border);border-radius:20px;font-size:.8rem;color:var(--text-muted)}
.stats-row .chip svg{width:14px;height:14px}
.featured-area{max-width:800px;margin:2rem auto;padding:0 1.5rem}
.featured-card{display:block;padding:2rem;background:var(--surface);border:1px solid var(--border);border-radius:12px;text-decoration:none;transition:border-color .2s}
.featured-card:hover{border-color:var(--border-hover)}
.featured-card .cat-tag{display:inline-flex;align-items:center;gap:.4rem;font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;padding:.25rem .6rem;border-radius:4px;margin-bottom:.8rem}
.featured-card .cat-tag svg{width:12px;height:12px}
.featured-card h2{font-size:1.4rem;font-weight:700;color:var(--text-strong);margin-bottom:.6rem;line-height:1.3}
.featured-card p{font-size:.9rem;color:var(--text);margin-bottom:1rem;line-height:1.5}
.featured-card .read-link{font-size:.85rem;font-weight:600}
.filter-bar{max-width:800px;margin:1.5rem auto;padding:0 1.5rem;display:flex;gap:.5rem;flex-wrap:wrap}
.filter-btn{display:flex;align-items:center;gap:.35rem;padding:.4rem .8rem;background:var(--surface);border:1px solid var(--border);border-radius:6px;font-family:'DM Sans',sans-serif;font-size:.8rem;color:var(--text-muted);cursor:pointer;transition:all .2s}
.filter-btn:hover,.filter-btn.active{border-color:var(--border-hover);color:var(--text-strong)}
.filter-btn svg{width:14px;height:14px}
.cat-section{max-width:800px;margin:2rem auto;padding:0 1.5rem}
.cat-header{display:flex;align-items:center;gap:.6rem;margin-bottom:1rem}
.cat-icon{width:32px;height:32px;border-radius:6px;display:flex;align-items:center;justify-content:center}
.cat-icon svg{width:18px;height:18px}
.cat-header h2{font-size:1.1rem;font-weight:700;color:var(--text-strong)}
.cat-count{font-size:.75rem;color:var(--text-muted);background:var(--surface);padding:.15rem .5rem;border-radius:10px}
.card-grid{display:flex;flex-direction:column;gap:.6rem}
.story-card{display:flex;align-items:flex-start;gap:.8rem;padding:1rem;background:var(--surface);border:1px solid var(--border);border-radius:8px;text-decoration:none;transition:border-color .2s;position:relative;overflow:hidden}
.story-card:hover{border-color:var(--border-hover)}
.card-accent{position:absolute;top:0;left:0;right:0;height:2px;opacity:0;transition:opacity .2s}
.story-card:hover .card-accent{opacity:1}
.card-num{font-size:.75rem;font-weight:700;min-width:24px;text-align:center;padding-top:.1rem}
.card-body{flex:1;min-width:0}
.card-body h3{font-size:.95rem;font-weight:600;color:var(--text-strong);line-height:1.3;margin-bottom:.3rem}
.card-body .excerpt{font-size:.8rem;color:var(--text-muted);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;margin-bottom:.5rem}
.card-meta{display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-muted)}
.read-link{font-weight:600}
footer{text-align:center;padding:3rem 1.5rem;font-size:.75rem;color:var(--text-muted);border-top:1px solid var(--border);margin-top:3rem}
"""

cat_sections = ''
for cat_key in ['business', 'llms-genai', 'research', 'policy']:
    cat_stories = [s for s in stories if s['category'] == cat_key]
    if not cat_stories:
        continue
    color = CATEGORY_COLORS[cat_key]
    icon = CATEGORY_ICONS[cat_key]
    cards = ''
    for s in cat_stories:
        cards += f'<a href="stories/{s["story_number"]}-{s["slug"]}.html" class="story-card" data-cat="{cat_key}"><div class="card-accent" style="background:{color}"></div><div class="card-num" style="color:{color}">{s["story_number"]}</div><div class="card-body"><h3>{s["headline"]}</h3><p class="excerpt">{s.get("article_excerpt","")}</p><div class="card-meta"><span>{s.get("reading_time_min",4)} min</span><span class="read-link" style="color:{color}">Read &rarr;</span></div></div></a>'
    cat_sections += f'<section class="cat-section" data-cat="{cat_key}"><div class="cat-header"><div class="cat-icon" style="background:color-mix(in srgb,{color} 15%,transparent);color:{color}">{icon}</div><h2>{cat_key.replace("-"," ").title()}</h2><span class="cat-count">{len(cat_stories)}</span></div><div class="card-grid">{cards}</div></section>'

feat = stories[0]
fc = CATEGORY_COLORS.get(feat['category'], '#c084fc')
feat_html = f'<div class="featured-area"><a href="stories/{feat["story_number"]}-{feat["slug"]}.html" class="featured-card"><span class="cat-tag" style="color:{fc};background:color-mix(in srgb,{fc} 10%,transparent)">{CATEGORY_ICONS.get(feat["category"],"")} {feat["category"].replace("-"," ").title()}</span><h2>{feat["headline"]}</h2><p>{feat.get("article_excerpt","")}</p><span class="read-link" style="color:{fc}">Read full story &rarr;</span></a></div>'

filter_buttons = '<button class="filter-btn active" data-filter="all"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg> All</button>'
for ck in ['business','llms-genai','research','policy']:
    if cats.get(ck, 0) > 0:
        filter_buttons += f'<button class="filter-btn" data-filter="{ck}" style="--fc:{CATEGORY_COLORS[ck]}">{CATEGORY_ICONS[ck]} {ck.replace("-"," ").title()}</button>'

index_html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Vault &mdash; AI Edition &middot; {meta["display_date"]}</title>
{FONTS_LINK}
<style>{INDEX_CSS}</style></head><body>
<nav>
  <a href="../../.."><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg> Home</a>
  <span class="brand">THE VAULT</span>
  <div class="nav-right">
    <a href="../../../archive/">Archive</a>
    <a href="../../../feed.xml"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11a9 9 0 0 1 9 9"/><path d="M4 4a16 16 0 0 1 16 16"/><circle cx="5" cy="19" r="1"/></svg></a>
  </div>
</nav>
<header class="edition-header">
  <div class="overline">DAILY INTELLIGENCE BRIEF</div>
  <h1>The Vault &mdash; AI Edition</h1>
  <div class="date-line">{meta["day_of_week"]}, {meta["display_date"]}</div>
</header>
<div class="stats-row">
  <div class="chip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg> {meta["story_count"]} stories</div>
  <div class="chip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg> {stats_total_words:,} words</div>
  <div class="chip"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> {stats_reading_time} min read</div>
</div>
{feat_html}
<div class="filter-bar">{filter_buttons}</div>
{cat_sections}
<footer>The Vault &mdash; AI Edition &middot; {meta["display_date"]}<br>Curated daily at <a href="https://news.promtvault.app" style="color:var(--accent);text-decoration:none">news.promtvault.app</a></footer>
<script>
document.querySelectorAll('.filter-btn').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    document.querySelectorAll('.filter-btn').forEach(function(b){{b.classList.remove('active')}});
    btn.classList.add('active');
    var f=btn.dataset.filter;
    document.querySelectorAll('.cat-section').forEach(function(s){{s.style.display=(f==='all'||s.dataset.cat===f)?'':'none'}});
  }});
}});
</script>
</body></html>'''

(EDITION_DIR / 'index.html').write_text(index_html)
print('OK index.html')

# --- digest.md ---
digest_lines = [f'# The Vault — AI Edition: {meta["display_date"]}\n']
digest_lines.append(f'{meta["story_count"]} stories · {stats_total_words:,} words · {stats_reading_time} min total read\n')
for s in stories:
    digest_lines.append(f'## {s["story_number"]}. {s["headline"]}')
    digest_lines.append(f'**Category:** {s["category"]} | **Read time:** {s.get("reading_time_min",4)} min')
    digest_lines.append(f'{s.get("key_takeaway","")}\n')
(EDITION_DIR / 'digest.md').write_text('\n'.join(digest_lines))
print('OK digest.md')

print('DONE')
