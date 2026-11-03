#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://hookforge.app"
YEAR = "2026"

NAV = """
<header class="site-header">
  <a class="skip" href="#main">Skip to content</a>
  <div class="wrap bar">
    <a class="logo" href="/" aria-label="HookForge home">
      <svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#c8f542"/><path d="M14 42 L32 12 L50 42 H14z" fill="#0b0c0e"/></svg>
      HookForge
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" id="menu-btn">Menu</button>
    <nav class="nav" id="nav" aria-label="Primary">
      <a href="/">Generator</a>
      <a href="/tiktok-hook-generator/">TikTok</a>
      <a href="/youtube-shorts-intro-generator/">Shorts</a>
      <a href="/instagram-reels-caption-generator/">Reels</a>
      <a href="/capcut-text-generator/">CapCut</a>
      <a href="/viral-hook-formulas/">Formulas</a>
      <a href="/swipe-file/">Swipe file</a>
      <a href="/blog/">Blog</a>
    </nav>
  </div>
</header>
"""
FOOT = f"""
<footer class="site-footer">
  <div class="wrap footgrid">
    <div>
      <a class="logo" href="/">HookForge</a>
      <p>Free TikTok, Shorts, and Reels hook generator for US creators. No signup. No email wall. English (US).</p>
      <p>&copy; <span id="y">{YEAR}</span> HookForge. Not affiliated with TikTok, YouTube, Instagram, Meta, or CapCut.</p>
    </div>
    <div>
      <strong>Tools</strong>
      <a href="/tiktok-hook-generator/">TikTok hook generator</a>
      <a href="/youtube-shorts-intro-generator/">YouTube Shorts intros</a>
      <a href="/instagram-reels-caption-generator/">Reels captions</a>
      <a href="/capcut-text-generator/">CapCut on-screen text</a>
      <a href="/facebook-reels-hook-generator/">Facebook Reels hooks</a>
    </div>
    <div>
      <strong>Learn</strong>
      <a href="/viral-hook-formulas/">10 hook formulas</a>
      <a href="/swipe-file/">Free swipe file</a>
      <a href="/guides/how-to-write-tiktok-hooks/">How to write TikTok hooks</a>
      <a href="/blog/">Creator blog</a>
      <a href="/embed/">Embed the widget</a>
    </div>
    <div>
      <strong>Site</strong>
      <a href="/about/">About</a>
      <a href="/contact/">Contact</a>
      <a href="/privacy/">Privacy</a>
      <a href="/terms/">Terms</a>
      <a href="/rss.xml">RSS</a>
      <a href="/sitemap.xml">Sitemap</a>
    </div>
  </div>
</footer>
<script src="/js/nav.js" defer></script>
<script src="/js/data.js" defer></script>
<script src="/js/app.js" defer></script>
"""


def head(title, desc, path, extra="", og_type="article"):
    canon = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="author" content="HookForge">
<meta name="theme-color" content="#0b0c0e">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en-US" href="{canon}">
<link rel="alternate" hreflang="x-default" href="{canon}">
<link rel="alternate" type="application/rss+xml" title="HookForge blog" href="/rss.xml">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="/manifest.webmanifest">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="HookForge">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="stylesheet" href="/css/app.css">
{extra}
</head>
"""


def crumbs(items):
    lis, schema = [], []
    for i, (name, href) in enumerate(items, 1):
        lis.append(f'<a href="{href}">{name}</a>' if href else f"<span>{name}</span>")
        schema.append(
            '{"@type":"ListItem","position":%d,"name":"%s"%s}'
            % (i, name, (',"item":"%s%s"' % (SITE, href)) if href else "")
        )
    return (
        f'<nav class="crumbs wrap" aria-label="Breadcrumb">{" / ".join(lis)}</nav>\n'
        + '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        + ",".join(schema)
        + "]}</script>"
    )


def article_ld(title, desc, path, date, wordcount):
    return f'''<script type="application/ld+json">{{
  "@context":"https://schema.org",
  "@type":"BlogPosting",
  "headline":"{title}",
  "description":"{desc}",
  "datePublished":"{date}",
  "dateModified":"{date}",
  "inLanguage":"en-US",
  "wordCount":{wordcount},
  "author":{{"@type":"Organization","name":"HookForge","url":"{SITE}/"}},
  "publisher":{{"@type":"Organization","name":"HookForge","logo":{{"@type":"ImageObject","url":"{SITE}/img/favicon.svg"}}}},
  "mainEntityOfPage":"{SITE}{path}",
  "image":"{SITE}/img/og.svg"
}}</script>'''


POSTS = [
    dict(
        slug="tiktok-hook-formulas-that-still-work",
        date="2026-10-12",
        title="TikTok Hook Formulas That Still Work in 2026",
        h1="TikTok hook formulas that still work in 2026",
        desc="Ten TikTok hook formulas US creators still use: question, mistake, POV, number, and more — with examples you can film today.",
        body="""
<p>Trend audio changes weekly. First-line jobs do not. If a stranger cannot tell what the video is about before the beat drops, you do not have a hook. You have a shrug.</p>
<p>This piece maps the same ten patterns we ship in the <a href="/tiktok-hook-generator/">TikTok hook generator</a>. Steal the pattern. Replace the object. Do not steal someone else’s story.</p>
<h2>1. Question</h2>
<p>Best when the viewer is already guilty. “Wait, you season chicken in the pan?” works because millions of US kitchens do. “Are you ready to level up?” works for nobody.</p>
<h2>2. Contrarian</h2>
<p>Pick a tip your niche repeats. Kill it in one clause. Then show the replacement in the next second. If you cannot show it, do not say it.</p>
<h2>3. Number</h2>
<p>Numbers feel specific even when they are small. “4 resume lines US recruiters skip” is a listicle people will watch. “Many resume mistakes” is fog.</p>
<h2>4. Mistake</h2>
<p>Name the error, not the person. “This is why your rice looks wet on camera” invites a fix. “You are bad at cooking” invites a swipe.</p>
<h2>5. POV</h2>
<p>POV still works when the scene is boring and true: parking lots, break rooms, apartment hallways. Fantasy POV without a punchline is cosplay.</p>
<h2>6. Before / after</h2>
<p>Two states. Same kitchen. Same jacket. No miracle body or money claims. If you need a disclaimer, you picked the wrong niche for this site.</p>
<h2>7. Loophole</h2>
<p>A software or filming workaround — never a legal, tax, or medical loophole. “Album trick for cleaner auto captions” is in bounds.</p>
<h2>8. Story open</h2>
<p>Start after the boring part. “I almost posted without the overlay” is a story. “So today I wanted to talk about” is a hostage situation.</p>
<h2>9. Negative</h2>
<p>“Do not say hey guys” is a complete hook if the next frame shows what to say instead.</p>
<h2>10. Pattern interrupt</h2>
<p>Put a sticky note on the lens. Write the hook on a paper plate. Weird only helps if it is still on-topic.</p>
<h2>How to test without lying to yourself</h2>
<p>Post two versions of the same video with different first seconds. Keep the rest identical. Watch 1-second hold, not vanity likes. If both flop, the topic is the problem, not the generator.</p>
<p>Full table: <a href="/viral-hook-formulas/">10 formulas</a>. Raw lines: <a href="/swipe-file/">swipe file</a>. Overlay: <a href="/capcut-text-generator/">CapCut text</a>.</p>
""",
    ),
    dict(
        slug="youtube-shorts-first-3-seconds",
        date="2026-10-18",
        title="YouTube Shorts: What to Put in the First 3 Seconds",
        h1="YouTube Shorts: what to put in the first 3 seconds",
        desc="A practical first-3-seconds checklist for YouTube Shorts: overlay text, visual interrupt, and a spoken line that matches. Free intro generator included.",
        body="""
<p>Shorts intros fail in three boring ways: a wave, a logo, or a sentence you cannot read. The first three seconds should answer “what is this” without sound.</p>
<h2>Second 0–1: picture</h2>
<p>Hands already doing the thing. A receipt. A cracked screen. Not your face saying the channel name. Channel name is for the end card.</p>
<h2>Second 1–2: overlay</h2>
<p>Eight words or fewer, high contrast, away from the like column. Generate overlay-sized lines with the <a href="/youtube-shorts-intro-generator/">Shorts intro generator</a>.</p>
<h2>Second 2–3: voice matches text</h2>
<p>If the overlay says “wet rice” and you say “hey y’all welcome back,” you trained the viewer to ignore both.</p>
<h2>What not to pack in</h2>
<ul>
<li>A 12-word thesis.</li>
<li>Three hashtags on screen.</li>
<li>A promise you cannot show in 30 seconds.</li>
</ul>
<p>After the open, you still need a reason to loop. Last frame should make the first frame make sense again. More on spoken vs overlay: <a href="/guides/how-to-write-tiktok-hooks/">hook writing guide</a>.</p>
""",
    ),
    dict(
        slug="instagram-reels-caption-length",
        date="2026-10-22",
        title="Instagram Reels Caption Length: What to Write After the Hook",
        h1="Instagram Reels caption length (and what belongs in the first line)",
        desc="How long a Reels caption should be, what to put before the fold, and how to pair it with a spoken hook. Free Reels caption generator.",
        body="""
<p>Instagram truncates captions. If the first line is “Link in bio” you already lost the save. The video hook stops the thumb; the caption earns the bookmark.</p>
<h2>A working shape</h2>
<ol>
<li>First line: the same idea as the spoken hook, not a duplicate word-for-word if that looks spammy.</li>
<li>Four to eight lines of useful detail a mute scroller can use later.</li>
<li>One question that is answerable in a comment (“1 or 2?”).</li>
<li>Hashtags last. A handful of true tags, not 30.</li>
</ol>
<p>There is no magic character count. There is a magic job: be useful after the video ends. Generate a draft with the <a href="/instagram-reels-caption-generator/">Reels caption generator</a>, then cut anything you would not comment on a friend’s Reel.</p>
<h2>Cover text</h2>
<p>Cover text is a billboard, not a paragraph. Match it to the <a href="/capcut-text-generator/">CapCut overlay</a> so the grid does not lie.</p>
""",
    ),
    dict(
        slug="capcut-on-screen-text-tips",
        date="2026-10-26",
        title="CapCut On-Screen Text Tips That Do Not Cover Your Face",
        h1="CapCut on-screen text tips that do not cover your face",
        desc="How to place CapCut on-screen text in the safe area, how long the line should be, and how to generate overlay copy without logging into CapCut.",
        body="""
<p>Auto captions are a safety net. They are not a hook. If the first readable words are “um so basically,” you paid for a microphone and used none of it.</p>
<h2>Write the overlay before you record</h2>
<p>Use the <a href="/capcut-text-generator/">CapCut text generator</a>, copy the on-screen field, paste into CapCut Text. Group words in 2–3 word chunks so they do not wrap into a wall.</p>
<h2>Safe area</h2>
<p>Leave the right third of the frame for likes and the bottom for captions + TikTok or Shorts UI. Center-left or upper-third is safer than dead center on a talking head.</p>
<h2>Contrast beats fonts</h2>
<p>A thick sans with a stroke beats a script font that looks “branded” and unreadable on a bus. If you cannot read it at arm’s length, neither can a viewer.</p>
<h2>Match the voice</h2>
<p>Do not overlay “4 resume lines” while saying “today I want to chat about careers.” Pick one sentence. Film that sentence.</p>
<p>Related: <a href="/youtube-shorts-intro-generator/">Shorts intros</a> · <a href="/blog/youtube-shorts-first-3-seconds/">first 3 seconds</a>.</p>
""",
    ),
    dict(
        slug="hashtag-strategy-us-creators-2026",
        date="2026-10-29",
        title="Hashtag Strategy for US Creators in 2026 (Short-Form)",
        h1="Hashtag strategy for US creators in 2026",
        desc="A sane hashtag strategy for TikTok, Shorts, and Reels: few true tags, US English, no banned bait. HookForge includes a short pack with every generate.",
        body="""
<p>Hashtags do not rescue a dead first second. They can still help people who search a niche, and they can still hurt you if they are lies.</p>
<h2>Rules we actually use in the generator</h2>
<ul>
<li>Nine tags or fewer.</li>
<li>One niche tag, one format tag, one intent tag.</li>
<li>No “fypシ” spam piles.</li>
<li>No tags for a city you are not in or a brand you did not use.</li>
</ul>
<p>Facebook cares less. Instagram still reads the caption. TikTok still pretends it does not care and then surfaces search. Generate per platform on the <a href="/">home tool</a> instead of copying one pack everywhere.</p>
<h2>Searchable titles still matter</h2>
<p>On-screen text and spoken words that match a real query — “tiny apartment tour,” “Costco lunch” — do more than a wall of tags. Pair this with <a href="/blog/how-to-write-a-hook-in-under-10-seconds/">writing a hook in 10 seconds</a>.</p>
""",
    ),
    dict(
        slug="how-to-write-a-hook-in-under-10-seconds",
        date="2026-11-01",
        title="How to Write a Hook in Under 10 Seconds",
        h1="How to write a hook in under 10 seconds",
        desc="A 10-second drill for TikTok and Reels hooks: object, formula, out-loud test. Then generate backups with HookForge if you stall.",
        body="""
<p>Set a timer. You get ten seconds of thinking, not ten seconds of filming. The drill:</p>
<ol>
<li>Name one object in the frame (2 seconds).</li>
<li>Pick one formula: question, mistake, or number (2 seconds).</li>
<li>Say a line under 12 words out loud (6 seconds).</li>
</ol>
<p>If you cannot say it, you cannot film it. Write it down. If the timer rings on mush, hit the <a href="/">hook generator</a> with that object as the idea and steal a cleaner version.</p>
<h2>Examples</h2>
<ul>
<li>Object: cracked screen. Line: “Do not film this crack until the overlay is on.”</li>
<li>Object: meal-prep containers. Line: “Sunday containers that are not aesthetic. They work.”</li>
<li>Object: thrift jacket. Line: “$4 jacket. Work outfit. No haul music.”</li>
</ul>
<p>More patterns: <a href="/viral-hook-formulas/">formulas</a>. More raw lines: <a href="/swipe-file/">swipe file</a>.</p>
""",
    ),
    dict(
        slug="best-free-tiktok-caption-generators",
        date="2026-11-02",
        title="Best Free TikTok Caption Generators (What to Avoid)",
        h1="Best free TikTok caption generators — and what to skip",
        desc="What a free TikTok caption generator should do in 2026: no email wall, no fake virality scores, hooks plus captions. How HookForge compares.",
        body="""
<p>Most “free TikTok caption generators” are email traps with five lorem lines. If a tool scores your hook 98/100, close the tab. Nobody has that oracle.</p>
<h2>A decent free tool does four things</h2>
<ul>
<li>Gives you a first line, not only hashtags.</li>
<li>Lets you copy without an account.</li>
<li>Admits it cannot promise views.</li>
<li>Works for Shorts and Reels when you ask, not only TikTok.</li>
</ul>
<p>That is the bar we built to. Open the <a href="/tiktok-hook-generator/">TikTok hook generator</a>, the <a href="/instagram-reels-caption-generator/">Reels caption generator</a>, or the <a href="/youtube-shorts-intro-generator/">Shorts intro generator</a>. No score. No drip course.</p>
<h2>What we will not add</h2>
<p>Fake follower counts, “post now” astrology, or medical/finance scripts. If you need those, you need a different kind of site — and probably a lawyer.</p>
<p>Compare methods, not marketing: <a href="/guides/how-to-write-tiktok-hooks/">write hooks yourself</a>.</p>
""",
    ),
    dict(
        slug="reels-vs-shorts-hooks",
        date="2026-11-03",
        title="Reels vs Shorts Hooks: What to Change When You Cross-Post",
        h1="Reels vs Shorts hooks: what to change when you cross-post",
        desc="Cross-posting Reels and Shorts? Change overlay density, caption, and CTA. Keep the video if you must. Free generators for each platform.",
        body="""
<p>The file can be the same. The first line often should not. Shorts viewers tolerate denser overlays. Reels viewers still read captions like a blog.</p>
<h2>Change these three</h2>
<ol>
<li><strong>Overlay:</strong> Shorts can be blunter. Reels cover text has to look good on a grid.</li>
<li><strong>Caption:</strong> Reels wants a saveable paragraph. Shorts description can be shorter.</li>
<li><strong>CTA:</strong> Subscribe vs save vs follow. Do not say “link in bio” on a platform where that is weak.</li>
</ol>
<p>Generate twice: <a href="/youtube-shorts-intro-generator/">Shorts</a> and <a href="/instagram-reels-caption-generator/">Reels</a>. If you also ship TikTok, run <a href="/tiktok-hook-generator/">TikTok</a> as the spoken-first version.</p>
<p>Facebook is a fourth dialect — plainer English, share CTA. That generator is <a href="/facebook-reels-hook-generator/">here</a>.</p>
""",
    ),
]


def write_post(p):
    path = f"/blog/{p['slug']}/"
    wc = len(p["body"].split())
    extra = article_ld(p["title"], p["desc"], path, p["date"], wc)
    html = head(p["title"] + " | HookForge", p["desc"], path, extra=extra)
    html += "<body>\n" + NAV + crumbs([("Home", "/"), ("Blog", "/blog/"), (p["h1"], None)])
    html += f'''<main id="main"><article class="wrap prose">
<p class="kicker">Blog · {p["date"]} · US creators</p>
<h1>{p["h1"]}</h1>
{p["body"]}
<p class="notice">Draft lines only. No view guarantees. Not medical, legal, or financial advice.</p>
<p>Try the matching tool: <a href="/">generate hooks</a>.</p>
</article></main>
'''
    html += FOOT + "\n</body></html>"
    dest = ROOT / "blog" / p["slug"] / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("wrote", dest.relative_to(ROOT))


for p in POSTS:
    write_post(p)

# blog index
cards = []
for p in POSTS:
    cards.append(
        f'<a href="/blog/{p["slug"]}/"><h3>{p["h1"]}</h3><p>{p["desc"]}</p><p class="kicker">{p["date"]}</p></a>'
    )
idx = head(
    "HookForge Blog — TikTok, Shorts, and Reels Hooks",
    "Free guides on TikTok hooks, YouTube Shorts intros, Instagram Reels captions, CapCut text, and hashtags for US creators.",
    "/blog/",
    extra="",
    og_type="website",
)
idx += (
    "<body>\n"
    + NAV
    + crumbs([("Home", "/"), ("Blog", None)])
    + f'''<main id="main"><section><div class="wrap">
<h1>HookForge blog</h1>
<p class="lede">Short, practical pieces that support the generator. No email drip. No “I made $10k” screenshots.</p>
<div class="cards">{"".join(cards)}</div>
<p style="margin-top:24px">Also: <a href="/guides/how-to-write-tiktok-hooks/">how to write TikTok hooks</a> · <a href="/viral-hook-formulas/">formulas</a> · <a href="/swipe-file/">swipe file</a></p>
</div></section></main>
'''
    + FOOT
    + "\n</body></html>"
)
(ROOT / "blog" / "index.html").write_text(idx, encoding="utf-8")
print("wrote blog/index.html")

# guide
guide_body = """
<p class="lede">A hook is the first thing a stranger understands. On TikTok that is usually a spoken line plus on-screen text in the first second. This guide is the manual. The <a href="/tiktok-hook-generator/">generator</a> is the shortcut.</p>
<h2>Step 1 — Pick an object, not a vibe</h2>
<p>“Get ready with me” is a vibe. “The concealer I returned to Ulta” is an object. Objects film. Vibes ramble.</p>
<h2>Step 2 — One job for the first second</h2>
<p>Name the object, the mistake, or the number. Do not name your channel. Do not thank subscribers who are not there yet.</p>
<h2>Step 3 — Say it out loud</h2>
<p>If you laugh from embarrassment, the line is trying too hard. If you run out of air, it is too long. Under 12 words.</p>
<h2>Step 4 — Overlay matches voice</h2>
<p>CapCut should show the same sentence, shorter if needed. See <a href="/blog/capcut-on-screen-text-tips/">on-screen text tips</a>.</p>
<h2>Step 5 — Caption does leftover work</h2>
<p>Details, a question, hashtags last. Reels especially: <a href="/blog/instagram-reels-caption-length/">caption length</a>.</p>
<h2>Step 6 — Test two opens, not two personalities</h2>
<p>Same footage, different first second. Read hold time. Then stop tinkering for a week and post.</p>
<h2>Worked example</h2>
<p>Niche: cooking. Object: wet rice. Question formula: “Wait, your rice looks wet on camera too?” Overlay: “Wet rice. It’s the lid.” Caption: how you vented the cooker, question “lid on or off?”, few tags.</p>
<p>Generate backups: <a href="/">HookForge</a>. Steal patterns: <a href="/viral-hook-formulas/">10 formulas</a>. Steal lines: <a href="/swipe-file/">swipe file</a>.</p>
"""
howto = '''<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"HowTo",
  "name":"How to write a TikTok hook",
  "description":"Six steps to write a TikTok hook in US English without a course.",
  "totalTime":"PT10M",
  "step":[
    {"@type":"HowToStep","position":1,"name":"Pick an object","text":"Choose a physical object in the frame, not a vibe."},
    {"@type":"HowToStep","position":2,"name":"One job","text":"Name the object, mistake, or number in the first second."},
    {"@type":"HowToStep","position":3,"name":"Say it out loud","text":"Keep the line under 12 words."},
    {"@type":"HowToStep","position":4,"name":"Match overlay","text":"CapCut text should match the spoken line."},
    {"@type":"HowToStep","position":5,"name":"Caption leftovers","text":"Details and hashtags go in the caption."},
    {"@type":"HowToStep","position":6,"name":"Test two opens","text":"Same video, two first seconds. Read hold time."}
  ]
}</script>'''
g = head(
    "How to Write TikTok Hooks (Free Guide) | HookForge",
    "Step-by-step guide to writing TikTok hooks for US creators: object, first second, out-loud test, CapCut overlay, caption. Free generator included.",
    "/guides/how-to-write-tiktok-hooks/",
    extra=howto,
    og_type="article",
)
g += (
    "<body>\n"
    + NAV
    + crumbs([("Home", "/"), ("Guides", "/blog/"), ("How to write TikTok hooks", None)])
    + f'<main id="main"><article class="wrap prose"><h1>How to write TikTok hooks</h1>{guide_body}</article></main>\n'
    + FOOT
    + "\n</body></html>"
)
dest = ROOT / "guides" / "how-to-write-tiktok-hooks" / "index.html"
dest.parent.mkdir(parents=True, exist_ok=True)
dest.write_text(g, encoding="utf-8")
print("wrote guides/how-to-write-tiktok-hooks/index.html")

# rss
items = []
for p in POSTS:
    items.append(
        f"""<item>
<title>{p['title']}</title>
<link>{SITE}/blog/{p['slug']}/</link>
<guid>{SITE}/blog/{p['slug']}/</guid>
<pubDate>{p['date']}</pubDate>
<description>{p['desc']}</description>
</item>"""
    )
rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>HookForge Blog</title>
<link>{SITE}/blog/</link>
<description>TikTok, Shorts, and Reels hook guides for US creators.</description>
<language>en-us</language>
<lastBuildDate>{TODAY if False else "2026-11-03"}</lastBuildDate>
{''.join(items)}
</channel>
</rss>
"""
(ROOT / "rss.xml").write_text(rss, encoding="utf-8")
print("wrote rss.xml")
