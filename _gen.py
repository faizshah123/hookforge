#!/usr/bin/env python3
"""Generate HookForge HTML pages. Run from /workspace/hookforge."""
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
SITE = "https://hookforge.app"
TODAY = "2026-11-03"
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
"""


def head(title, desc, path, extra="", og_type="website", image="/img/og.svg"):
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
<link rel="apple-touch-icon" href="/img/favicon.svg">
<link rel="manifest" href="/manifest.webmanifest">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="HookForge">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}{image}">
<link rel="stylesheet" href="/css/app.css">
{extra}
</head>
"""


def crumbs(items):
    lis = []
    schema = []
    for i, (name, href) in enumerate(items, 1):
        if href:
            lis.append(f'<a href="{href}">{name}</a>')
        else:
            lis.append(f"<span>{name}</span>")
        schema.append(
            f'{{"@type":"ListItem","position":{i},"name":"{name}"'
            + (f',"item":"{SITE}{href}"' if href else "")
            + "}"
        )
    html = ' / '.join(lis)
    ld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(schema)}]}}</script>'
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb">{html}</nav>\n{ld}'


ORG = f'''<script type="application/ld+json">{{
  "@context":"https://schema.org",
  "@graph":[
    {{
      "@type":"Organization",
      "@id":"{SITE}/#org",
      "name":"HookForge",
      "url":"{SITE}/",
      "logo":"{SITE}/img/favicon.svg",
      "email":"hello@hookforge.app",
      "description":"Free TikTok, YouTube Shorts, and Instagram Reels hook and caption generator for US creators."
    }},
    {{
      "@type":"WebSite",
      "@id":"{SITE}/#site",
      "url":"{SITE}/",
      "name":"HookForge",
      "inLanguage":"en-US",
      "publisher":{{"@id":"{SITE}/#org"}},
      "potentialAction":{{
        "@type":"SearchAction",
        "target":"{SITE}/blog/?q={{search_term_string}}",
        "query-input":"required name=search_term_string"
      }}
    }}
  ]
}}</script>'''

APP_SCHEMA = f'''<script type="application/ld+json">{{
  "@context":"https://schema.org",
  "@type":"SoftwareApplication",
  "name":"HookForge Hook Generator",
  "applicationCategory":"MultimediaApplication",
  "operatingSystem":"Web",
  "offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},
  "url":"{SITE}/",
  "description":"Free browser tool that writes TikTok hooks, Shorts intros, Reels captions, CapCut on-screen text, and hashtags. No account.",
  "featureList":["TikTok hooks","YouTube Shorts intros","Instagram Reels captions","CapCut on-screen text","Hashtag packs","Local copy, no signup"],
  "inLanguage":"en-US",
  "audience":{{"@type":"Audience","geographicArea":{{"@type":"Country","name":"United States"}}}}
}}</script>'''


def faq_ld(pairs):
    ents = ",".join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in pairs
    )
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{ents}]}}</script>'


def faq_html(pairs):
    bits = []
    for q, a in pairs:
        bits.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    return '<div class="faq">' + "".join(bits) + "</div>"


def tool_form(h1, lede, default_platform="tiktok"):
    chips = [
        ("GRWM but honest", "GRWM but I tell you the product I actually returned"),
        ("$20 Costco haul", "Costco haul under $20 for a week of lunches"),
        ("gym fail", "first week back at the gym after skipping January"),
        ("apartment tour", "tiny US apartment tour that is not aesthetic"),
        ("resume hook", "resume tip that got me more interviews without a course"),
        ("recipe 30s", "one-pan dinner in 30 seconds of talking"),
    ]
    chip_html = "".join(f'<button type="button" class="chip" data-idea="{v}">{k}</button>' for k, v in chips)
    return f'''
<main id="main">
<section class="hero">
  <div class="wrap grid-2">
    <div>
      <span class="kicker">Free · No signup · Runs in your browser</span>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
      <form id="hook-form" class="card" action="#results-wrap">
        <div class="row">
          <div>
            <label for="niche">Niche</label>
            <select id="niche" name="niche" required></select>
          </div>
          <div>
            <label for="platform">Platform</label>
            <select id="platform" name="platform" required></select>
          </div>
        </div>
        <label for="idea">Video idea (plain English)</label>
        <textarea id="idea" name="idea" required maxlength="240" placeholder="Example: thrift flip a $4 jacket into a work outfit"></textarea>
        <p class="chips" aria-label="Idea starters">{chip_html}</p>
        <div class="row">
          <div>
            <label for="tone">Tone</label>
            <select id="tone" name="tone"></select>
          </div>
          <div>
            <label for="count">How many hooks</label>
            <select id="count" name="count">
              <option value="8">8</option>
              <option value="10" selected>10</option>
              <option value="12">12</option>
            </select>
          </div>
        </div>
        <div class="actions">
          <button class="btn btn-lime" type="submit">Generate hooks</button>
          <button class="btn btn-ghost" type="button" id="shuffle">Shuffle again</button>
        </div>
        <p class="notice" style="margin-top:12px">This is a writing aid. It does not promise views, and it does not give medical, legal, or money-making guarantees. Keep claims you film truthful.</p>
      </form>
      <div class="statrow">
        <div class="stat"><b>10 hooks</b><span>plus caption, CTA, hashtags</span></div>
        <div class="stat"><b>$0</b><span>no email, no watermark</span></div>
        <div class="stat"><b>US English</b><span>built for American creators</span></div>
      </div>
    </div>
    <div>
      <div class="phone" aria-hidden="true">
        <div class="screen" id="preview">
          <span class="badge">Preview</span>
          <div class="os">Your first line goes here</div>
          <div class="cap">Caption preview after you generate.</div>
        </div>
      </div>
    </div>
  </div>
</section>
<section id="results-wrap" hidden>
  <div class="wrap">
    <h2>Your pack — copy what you need</h2>
    <p class="lede">Hooks are short on purpose. If a line is longer than 8–12 words, cut it before you film.</p>
    <div class="out" id="results"></div>
  </div>
</section>
'''


HOME_FAQS = [
    ("Is the HookForge TikTok hook generator free?",
     "Yes. The generator, swipe file, and formula pages are free. There is no account, trial, or watermark. You can copy every line."),
    ("Do I need to log in to TikTok, CapCut, or Instagram?",
     "No. HookForge runs in the browser. It never asks for your social passwords and never posts for you."),
    ("Does this work for YouTube Shorts and Instagram Reels too?",
     "Yes. Pick the platform in the form. You get a first line, on-screen text, a caption, hashtags, and a CTA matched to that app."),
    ("Will these hooks get me on For You?",
     "No honest tool can promise that. Retention, topic, and posting cadence matter more than any generator. Use these as first drafts, then say them out loud."),
    ("Is my video idea stored on a server?",
     "Generation runs on your device. A short local history may stay in your browser storage. See the privacy page. We do not sell creator ideas."),
    ("Can I embed HookForge on my blog?",
     "Yes. Copy the iframe on the embed page and keep the credit link. That is also the easiest legal backlink you can give us."),
]

HOW_STEPS = '''<script type="application/ld+json">{
  "@context":"https://schema.org",
  "@type":"HowTo",
  "name":"How to generate a TikTok or Reels hook with HookForge",
  "totalTime":"PT1M",
  "supply":[{"@type":"HowToSupply","name":"A one-sentence video idea"}],
  "tool":[{"@type":"HowToTool","name":"HookForge"}],
  "step":[
    {"@type":"HowToStep","position":1,"name":"Pick niche and platform","text":"Choose your niche and TikTok, Shorts, Reels, CapCut, or Facebook Reels."},
    {"@type":"HowToStep","position":2,"name":"Describe the video","text":"Write one sentence in plain English. Do not paste a script."},
    {"@type":"HowToStep","position":3,"name":"Generate and copy","text":"Hit generate, copy a hook under 12 words, paste on-screen text into CapCut, and film the first second on that line."}
  ]
}</script>'''


def write(path, html):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print("wrote", path)


# ---------- HOME ----------
home_extra = ORG + APP_SCHEMA + faq_ld(HOME_FAQS) + HOW_STEPS + '<script src="/js/data.js" defer></script><script src="/js/app.js" defer></script>'
home = head(
    "Free TikTok Hook Generator (Shorts + Reels Captions) | HookForge",
    "Free TikTok hook generator for US creators. Get 10 hooks, on-screen text, captions, and hashtags for Shorts, Reels, and CapCut. No signup.",
    "/",
    extra=home_extra,
) + f"""<body data-platform="tiktok">
{NAV}
{tool_form(
  "Free TikTok hook generator for US creators",
  "Type a video idea. Get 10 scroll-stopping first lines, CapCut on-screen text, a caption, hashtags, and a CTA. Built for TikTok, YouTube Shorts, and Instagram Reels. No email wall."
)}
<section class="alt">
  <div class="wrap">
    <h2>Why a hook tool beats another tips blog</h2>
    <p class="lede">US short-form is a daily habit. Creators do not need another 2,000-word lecture. They need a first line they can say in one breath before the coffee cools.</p>
    <div class="cards">
      <article><h3>On-page, not a course</h3><p>The generator is the page. Google can index the tool, the formulas, and the examples. You leave with copy, not a funnel.</p></article>
      <article><h3>Platform-aware</h3><p>TikTok wants a spoken open. Shorts wants a visual interrupt. Reels wants a saveable caption. CapCut wants short on-screen text. Pick one.</p></article>
      <article><h3>US English, US niches</h3><p>Costco, thrift, gym-after-January, tiny apartments, resumes — not generic “grow your brand” sludge.</p></article>
    </div>
  </div>
</section>
<section>
  <div class="wrap prose">
    <h2>How to use this TikTok hook generator</h2>
    <ol>
      <li>Pick a niche you actually post. Fake niches make fake hooks.</li>
      <li>Write one sentence: what happens on camera, not your life story.</li>
      <li>Generate 10 lines. Read them out loud. Keep the one you would say to a friend.</li>
      <li>Paste the on-screen text into CapCut. Film the first second on that line, not on “hey guys.”</li>
      <li>Use the caption as a draft. Cut anything you would not comment on someone else’s video.</li>
    </ol>
    <p>If you want the method without the form, read <a href="/guides/how-to-write-tiktok-hooks/">how to write TikTok hooks</a> and steal from the <a href="/viral-hook-formulas/">10 formulas</a>.</p>
    <h2>What “good” looks like in 2026</h2>
    <p>A usable hook is under 12 words, names a specific object or mistake, and does not promise a miracle. “Wait, your rice cooker can do that?” beats “You will not believe this life hack.” Specific beats loud.</p>
    <p>We keep health, crypto, and get-rich claims out of the default packs. If your niche is fitness, talk form and filming — not supplements or diagnoses.</p>
    <h2>Internal map for crawlers and humans</h2>
    <p>Start with the <a href="/tiktok-hook-generator/">TikTok hook generator</a>, then <a href="/youtube-shorts-intro-generator/">YouTube Shorts intros</a>, <a href="/instagram-reels-caption-generator/">Reels captions</a>, <a href="/capcut-text-generator/">CapCut text</a>, and <a href="/facebook-reels-hook-generator/">Facebook Reels</a>. Pair with the <a href="/swipe-file/">swipe file</a> and the <a href="/blog/">blog</a>.</p>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <h2>People also ask</h2>
    {faq_html(HOME_FAQS)}
  </div>
</section>
<section>
  <div class="wrap">
    <h2>Next</h2>
    <div class="cards">
      <a href="/tiktok-hook-generator/"><h3>TikTok-only landing</h3><p>Same tool, TikTok-first copy and FAQs.</p></a>
      <a href="/swipe-file/"><h3>80 free first lines</h3><p>Static swipe file you can scrape and cite.</p></a>
      <a href="/embed/"><h3>Embed on your site</h3><p>Iframe + credit link. Off-page SEO you control.</p></a>
    </div>
  </div>
</section>
</main>
{FOOT}
</body></html>"""
write("index.html", home)

# ---------- platform landings ----------
platforms = [
    dict(
        slug="tiktok-hook-generator",
        platform="tiktok",
        h1="TikTok hook generator (free, no login)",
        title="TikTok Hook Generator — 10 Free First Lines | HookForge",
        desc="Free TikTok hook generator. Type your video idea and get 10 first lines, on-screen text, captions, and hashtags. No signup. Built for US TikTok.",
        lede="TikTok still rewards the first second. This page writes spoken openers, not essays. Paste one into CapCut, film, post.",
        body="""
<h2>What a TikTok hook has to do</h2>
<p>On TikTok the viewer is already mid-scroll. Your first line has to name a situation they recognize in under a second: a Costco receipt, a failed gym selfie, a thrift tag. If the line could fit any niche, it fits none.</p>
<p>Use this generator when you have a video idea and zero patience for a blank caption box. It is a <strong>TikTok hook generator</strong>, not a growth agency. It will not post for you and it will not guess the For You algorithm.</p>
<h2>On-page checklist we follow</h2>
<ul>
<li>One H1 that matches the query “tiktok hook generator”.</li>
<li>The form is above the fold. You do not hunt for the tool.</li>
<li>Examples are US-specific so the copy does not sound like a translation.</li>
<li>FAQs use the same words people type into Google.</li>
<li>Related URLs: <a href="/youtube-shorts-intro-generator/">Shorts</a>, <a href="/instagram-reels-caption-generator/">Reels</a>, <a href="/capcut-text-generator/">CapCut</a>.</li>
</ul>
<h2>How we write the lines</h2>
<p>Each pack mixes ten formulas: question, contrarian, number, mistake, POV, before/after, loophole (non-legal), story open, negative, pattern interrupt. You can read the full list on <a href="/viral-hook-formulas/">viral hook formulas</a>.</p>
<p>Keep spoken hooks under 12 words. If you need a lecture, that is a carousel or a blog post — try our <a href="/guides/how-to-write-tiktok-hooks/">hook writing guide</a>.</p>
""",
        faqs=[
            ("What is a TikTok hook?", "The first line or on-screen text in the opening second. It should name a specific situation so a stranger stops."),
            ("How long should a TikTok hook be?", "Aim for 8 to 12 words. If you cannot say it in one breath, cut it."),
            ("Are these hooks unique?", "They are generated from your idea plus formula patterns. Edit them so they sound like you. Do not paste claims you cannot back up."),
            ("Can I use this commercially?", "Yes. Free output is yours to film. Do not scrape the site in a way that knocks it over. See terms."),
        ],
    ),
    dict(
        slug="youtube-shorts-intro-generator",
        platform="shorts",
        h1="YouTube Shorts intro generator",
        title="YouTube Shorts Intro Generator (Free Hooks) | HookForge",
        desc="Free YouTube Shorts intro generator. Get a first-frame line, on-screen text, and a caption. No account. Made for US Shorts creators.",
        lede="Shorts intros die when they start with a wave. This tool writes the first frame: a sentence the viewer can read without sound.",
        body="""
<h2>Shorts are not vertical YouTube</h2>
<p>People open Shorts with the sound off more often than they admit. Your intro has to work as <strong>on-screen text</strong> first, voice second. That is why this YouTube Shorts intro generator always returns a short overlay line.</p>
<p>Pair it with a hard visual: hands already doing the thing, not a face saying hello. Then stack a spoken line that matches the overlay so accessibility and retention both win.</p>
<h2>Intro patterns that still work</h2>
<ul>
<li>Number + object: “3 resume lines US hiring managers skip.”</li>
<li>Negative: “Do not start your Short with your name.”</li>
<li>Mistake: “This is why your rice looks wet on camera.”</li>
<li>Loop: last frame should make the first frame make sense again.</li>
</ul>
<p>Need spoken-first instead? Use the <a href="/tiktok-hook-generator/">TikTok hook generator</a>. Need captions for the description box? Steal structure from <a href="/instagram-reels-caption-generator/">Reels captions</a>.</p>
""",
        faqs=[
            ("How long should a YouTube Shorts intro be?", "The first second. Overlay text should be readable in a glance — under 8 words if you can."),
            ("Does YouTube rank Shorts on the first line?", "Retention and audience signals matter more than a keyword in the spoken intro. Still, a clear first line helps humans stay."),
            ("Can I use these intros on long videos?", "You can. Long videos still need a cold open. Just do not stuff the same 8-word line into a 12-minute intro."),
        ],
    ),
    dict(
        slug="instagram-reels-caption-generator",
        platform="reels",
        h1="Instagram Reels caption generator",
        title="Instagram Reels Caption Generator (Free) | HookForge",
        desc="Free Instagram Reels caption generator plus spoken hooks and hashtags. No login. Written for US Reels, not generic Instagram quotes.",
        lede="Reels get saved when the caption is useful after the video ends. This page writes the spoken hook and the caption together.",
        body="""
<h2>Captions are the second product</h2>
<p>On Instagram the video stops people; the caption gets the save. A Reels caption generator that only dumps hashtags is wasting the box. We write a hook, a short body, a question, and a follow CTA.</p>
<p>Keep the first line of the caption interesting even in the truncated preview. Put hashtags at the end, not in the first 125 characters.</p>
<h2>Reels vs TikTok copy</h2>
<p>Reels audiences still read more. You can be slightly warmer. You still cannot ramble. If you want punchier spoken opens, generate on <a href="/tiktok-hook-generator/">TikTok</a> and paste the caption from this page.</p>
<p>Cover text should match the <a href="/capcut-text-generator/">CapCut on-screen line</a> so the grid thumbnail does not lie.</p>
""",
        faqs=[
            ("How long should an Instagram Reels caption be?", "Long enough to be useful, short enough to finish. Lead with one strong line. Hashtags go last."),
            ("How many hashtags should I use on Reels?", "A tight set beats 30 junk tags. This tool returns a short pack. Delete anything that is not true of the video."),
            ("Can I generate cover text here?", "Yes. Each hook includes an on-screen version sized for a phone overlay."),
        ],
    ),
    dict(
        slug="capcut-text-generator",
        platform="capcut",
        h1="CapCut on-screen text generator",
        title="CapCut Text Generator — On-Screen Hooks (Free) | HookForge",
        desc="Free CapCut text generator for on-screen hooks. Short lines that fit a phone overlay, plus captions. No CapCut login required.",
        lede="CapCut Auto captions will not save a weak first line. Generate overlay text that fits a 9:16 frame, then paste it.",
        body="""
<h2>On-screen text is a layout problem</h2>
<p>If the line wraps to four rows, nobody reads it. This CapCut text generator clips overlay copy so it can sit in the safe area above your face or hands.</p>
<p>Workflow: generate here → copy “On-screen” → CapCut Text tool → 2–3 word groups, high contrast, not over the TikTok UI. Then record voice that matches, not a different script.</p>
<h2>Do not auto-caption secrets</h2>
<p>Auto captions will happily subtitle a mumbled “um.” Write the overlay first so you are not editing 40 bad words later. More pacing notes: <a href="/blog/capcut-on-screen-text-tips/">CapCut on-screen text tips</a>.</p>
""",
        faqs=[
            ("Does this connect to CapCut?", "No. It never asks for a CapCut account. You paste text into the app yourself."),
            ("What font should I use?", "Whatever you can read at arm’s length. High contrast beats a trendy script font."),
            ("Can I generate auto-captions?", "We generate the lines you should show. CapCut still does speech-to-text on your voiceover."),
        ],
    ),
    dict(
        slug="facebook-reels-hook-generator",
        platform="facebook",
        h1="Facebook Reels hook generator",
        title="Facebook Reels Hook Generator (Free) | HookForge",
        desc="Free Facebook Reels hook generator for US Pages and creators. First lines, captions, and CTAs. No Facebook login.",
        lede="Facebook Reels still play in the feed with sound off. Write a first line a parent can understand without a trend audio.",
        body="""
<h2>Facebook is not TikTok with a blue icon</h2>
<p>The median Facebook Reels viewer is older, often watching on Wi-Fi at the kitchen table. Jargon dies. Specific household objects live. This Facebook Reels hook generator leans toward plain US English.</p>
<p>CTAs that work here: share to a Page, comment a number, send to a sibling. “Link in bio” is weaker than on Instagram.</p>
<p>If you cross-post, generate once per platform. Do not ship the same “fyp” hashtag pack to Facebook. Switch the dropdown, hit shuffle, post the Facebook version to Facebook.</p>
""",
        faqs=[
            ("Should I post the same Reel to Facebook and Instagram?", "You can cross-post the video. Rewrite the hook and hashtags. This page exists so that rewrite takes one minute."),
            ("Do hashtags matter on Facebook Reels?", "Less than on TikTok. A clear first line and a shareable caption matter more."),
        ],
    ),
]

for p in platforms:
    extra = APP_SCHEMA + faq_ld(p["faqs"]) + '<script src="/js/data.js" defer></script><script src="/js/app.js" defer></script>'
    html = head(p["title"], p["desc"], f"/{p['slug']}/", extra=extra)
    html += f'<body data-platform="{p["platform"]}">\n{NAV}\n'
    html += crumbs([("Home", "/"), (p["h1"], None)])
    html += tool_form(p["h1"], p["lede"], p["platform"])
    html += f'<section class="alt"><div class="wrap prose">{p["body"]}<h2>FAQ</h2>{faq_html(p["faqs"])}</div></section>\n</main>\n{FOOT}\n</body></html>'
    write(f"{p['slug']}/index.html", html)

print("core pages done")
