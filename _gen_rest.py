#!/usr/bin/env python3
from pathlib import Path
import html as htmllib

ROOT = Path(__file__).resolve().parent
SITE = "https://hookforge.app"
YEAR = "2026"
TODAY = "2026-11-03"

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


def head(title, desc, path, extra="", og_type="website"):
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
    lis = []
    schema = []
    for i, (name, href) in enumerate(items, 1):
        lis.append(f'<a href="{href}">{name}</a>' if href else f"<span>{name}</span>")
        schema.append(
            '{"@type":"ListItem","position":%d,"name":"%s"%s}'
            % (i, name, (',"item":"%s%s"' % (SITE, href)) if href else "")
        )
    html = " / ".join(lis)
    ld = (
        '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        + ",".join(schema)
        + "]}</script>"
    )
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb">{html}</nav>\n{ld}'


def page(path, title, desc, h1, inner, extra="", og="website", trail=None):
    html = head(title, desc, path, extra=extra, og_type=og)
    html += "<body>\n" + NAV
    if trail:
        html += crumbs(trail)
    html += f'<main id="main"><section><div class="wrap prose"><h1>{h1}</h1>{inner}</div></section></main>\n'
    html += FOOT + "\n</body></html>"
    p = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    if path.endswith(".html"):
        p = ROOT / path
    elif path != "/":
        p = ROOT / path.strip("/") / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print("wrote", p.relative_to(ROOT))


def faq_ld(pairs):
    ents = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a)
        for q, a in pairs
    )
    return (
        '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        + ents
        + "]}</script>"
    )


# ---- formulas ----
formulas = [
    ("Question", "Ask something the viewer is already doing.", "Wait, you season chicken in the pan?"),
    ("Contrarian", "Kill a tip everyone repeats.", "Stop filming GRWM in the bathroom light."),
    ("Number", "One number plus a concrete object.", "4 resume lines US recruiters skip."),
    ("Mistake", "Name the error, not the person.", "This is why your rice looks wet on camera."),
    ("POV", "Drop them into a scene.", "POV: you opened CapCut with no first line."),
    ("Before / after", "Two states, no miracle claims.", "Day 1 vs day 14 of posting at 7am ET."),
    ("Loophole", "A workaround that is not medical or legal advice.", "The album trick that still auto-captions cleaner."),
    ("Story open", "Start mid-action.", "I almost posted without the overlay. Glad I didn’t."),
    ("Negative", "What not to do in the first second.", "Do not say hey guys. Say the object."),
    ("Pattern interrupt", "Weird, specific, visual.", "I wrote my hook on a sticky note on the lens."),
]
rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td><em>{c}</em></td></tr>" for a, b, c in formulas)
form_faqs = [
    ("What is a hook formula?", "A reusable first-line pattern. You fill it with your object, not a celebrity name."),
    ("Which formula is best for TikTok?", "Question and mistake still travel. Test two formulas on the same video idea."),
    ("Can I mix formulas?", "Yes. Many strong opens are a mistake plus a number. Keep the spoken line under 12 words."),
]
page(
    "viral-hook-formulas/",
    "10 Viral Hook Formulas for TikTok, Shorts, and Reels | HookForge",
    "Ten reusable hook formulas for TikTok, YouTube Shorts, and Instagram Reels, with US examples you can steal. Free, no signup.",
    "10 viral hook formulas that still work in 2026",
    f"""
<p class="lede">Formulas are scaffolding. If you paste them without a specific object — a Costco chicken, a $4 thrift jacket, a wet rice cooker — they sound like every other “viral hooks” carousel.</p>
<table><thead><tr><th>Formula</th><th>Job</th><th>US example</th></tr></thead><tbody>{rows}</tbody></table>
<p>Generate a pack with these mixed in on the <a href="/">free hook generator</a>. For spoken vs overlay, read <a href="/guides/how-to-write-tiktok-hooks/">how to write TikTok hooks</a>.</p>
<h2>How to practice</h2>
<ol>
<li>Pick one object in your room.</li>
<li>Write all ten formulas about that object in ten minutes.</li>
<li>Circle the two you would say to a coworker, not to an algorithm.</li>
<li>Film only those two. Do not film the clever one you would never say.</li>
</ol>
<h2>FAQ</h2>
<div class="faq">
<details><summary>What is a hook formula?</summary><p>A reusable first-line pattern. You fill it with your object, not a celebrity name.</p></details>
<details><summary>Which formula is best for TikTok?</summary><p>Question and mistake still travel. Test two formulas on the same video idea.</p></details>
<details><summary>Can I mix formulas?</summary><p>Yes. Many strong opens are a mistake plus a number. Keep the spoken line under 12 words.</p></details>
</div>
<p>Related: <a href="/swipe-file/">80 ready first lines</a> · <a href="/tiktok-hook-generator/">TikTok generator</a> · <a href="/blog/tiktok-hook-formulas-that-still-work/">formulas deep dive</a></p>
""",
    extra=faq_ld(form_faqs),
    trail=[("Home", "/"), ("Viral hook formulas", None)],
)

# ---- swipe file ----
swipes = []
objects = [
    "Costco rotisserie chicken",
    "a $4 thrift jacket",
    "wet rice in the cooker",
    "a 9-to-5 resume",
    "January gym guilt",
    "a tiny studio apartment",
    "CapCut auto captions",
    "a Target dollar-spot find",
    "Sunday meal prep containers",
    "a cracked phone screen",
]
starts = [
    "Wait, you still {o} like this?",
    "POV: {o} just ruined the take.",
    "Do not film {o} until this overlay is on.",
    "The unsexy truth about {o}.",
    "I wasted a Sunday on {o}.",
    "Your {o} is fine. Your first line is not.",
    "US kitchens keep lying about {o}.",
    "Stop copying tutorials that skip {o}.",
]
for o in objects:
    for s in starts:
        swipes.append(s.format(o=o))
swipes = swipes[:80]
lis = "".join(f"<li>{htmllib.escape(s)}</li>" for s in swipes)
page(
    "swipe-file/",
    "Free TikTok Hook Swipe File (80 First Lines) | HookForge",
    "80 free TikTok, Shorts, and Reels first lines you can rewrite. US objects, no email gate. Copy, film, cite HookForge if you publish the list.",
    "Free swipe file: 80 first lines",
    f"""
<p class="lede">These are raw first lines, not finished videos. Swap the object for yours. If a line mentions a brand, that is an example, not an ad.</p>
<p>Want lines matched to one idea? Use the <a href="/">generator</a> instead of scrolling 80 generics.</p>
<ol>{lis}</ol>
<h2>License</h2>
<p>Free to film. If you republish the list on your own blog, keep a link to this page. That is the off-page deal: you get copy, crawlers see a citation.</p>
<p>More structure: <a href="/viral-hook-formulas/">10 formulas</a>. Overlay length: <a href="/blog/capcut-on-screen-text-tips/">CapCut text tips</a>.</p>
""",
    trail=[("Home", "/"), ("Swipe file", None)],
)

# ---- embed ----
page(
    "embed/",
    "Embed the Free Hook Generator on Your Blog | HookForge",
    "Embed HookForge’s free TikTok hook generator with a short iframe. Keep the credit link. Fastest legal backlink for creator blogs.",
    "Embed HookForge on your site",
    """
<p class="lede">Paste the iframe. Keep the credit line. Do not wrap it in a click-tracker that strips the referrer if you want the SEO juice to flow.</p>
<pre><code>&lt;iframe src="https://hookforge.app/embed/widget.html" title="HookForge free hook generator" loading="lazy" style="width:100%;min-height:640px;border:0;border-radius:14px"&gt;&lt;/iframe&gt;
&lt;p&gt;Hook generator by &lt;a href="https://hookforge.app/"&gt;HookForge&lt;/a&gt;&lt;/p&gt;</code></pre>
<p>The widget is a slim form. Full formulas stay on this domain so Google still has a reason to rank the main site.</p>
<p>Preview:</p>
<iframe src="/embed/widget.html" title="HookForge widget preview" style="width:100%;min-height:640px;border:1px solid #2a3140;border-radius:14px"></iframe>
<h2>Why this exists</h2>
<p>Off-page SEO for a new domain is slow if you wait for strangers. Giving other creator blogs a useful embed is a clean, disclosed way to earn links. No PBNs. No blog-comment spam. No fake news mentions.</p>
""",
    trail=[("Home", "/"), ("Embed", None)],
)

# ---- about ----
page(
    "about/",
    "About HookForge — Free US Creator Hook Tool",
    "HookForge is a free, no-signup TikTok, Shorts, and Reels hook generator for US creators. No courses. No YMYL advice.",
    "About HookForge",
    """
<p>HookForge is a small web tool. It writes first lines, on-screen text, captions, and hashtags for short-form video. It does not run ads inside the generator today. It does not sell your ideas.</p>
<p>We built it because “creator education” sites hide the useful part behind an email wall. The useful part is a sentence you can say in one breath.</p>
<h2>Who it is for</h2>
<p>US-based TikTok, Shorts, Reels, and Facebook Reels makers who already have a niche and need a draft opener. Students, side hustlers, small shops, hobby cooks — not agencies buying 10,000 spam blogs.</p>
<h2>Who it is not for</h2>
<p>Medical, legal, or get-rich advice. We will not generate supplement claims or crypto pitches on purpose. If a line sounds like a guarantee, delete it.</p>
<h2>How ranking is supposed to work</h2>
<p>On-page: one intent per URL, real H1, FAQs, internal links, schema. Technical: static files, canonicals, sitemap, robots, RSS, llms.txt, hreflang. Off-page: embeddable widget, swipe file people can cite, RSS for news readers. No fake reviews.</p>
<p>Contact: <a href="/contact/">contact page</a>. Privacy: <a href="/privacy/">privacy</a>.</p>
""",
    trail=[("Home", "/"), ("About", None)],
)

# ---- contact ----
page(
    "contact/",
    "Contact HookForge",
    "Contact HookForge about the free TikTok hook generator, embeds, corrections, or DMCA. US English.",
    "Contact",
    """
<p>Email <a href="mailto:hello@hookforge.app">hello@hookforge.app</a> for corrections, embed help, or takedown requests.</p>
<p>We do not offer social-account recovery, “boost” services, or paid shoutouts. If a stranger messages you claiming to be HookForge support, they are not.</p>
<h2>Corrections</h2>
<p>If a blog example is outdated, send the URL and the fix. We care more about accurate creator advice than about keeping a dated hook up.</p>
<address>HookForge · United States · hello@hookforge.app</address>
""",
    extra='<script type="application/ld+json">{"@context":"https://schema.org","@type":"ContactPage","name":"Contact HookForge","url":"https://hookforge.app/contact/"}</script>',
    trail=[("Home", "/"), ("Contact", None)],
)

# ---- privacy ----
page(
    "privacy/",
    "Privacy Policy | HookForge",
    "HookForge privacy policy. The generator runs in your browser. We do not sell creator ideas or require an account.",
    "Privacy policy",
    f"""
<p>Last updated {TODAY}.</p>
<p>HookForge is a static site plus client-side JavaScript. Generating hooks does not require an account.</p>
<h2>What we collect</h2>
<ul>
<li>Standard web logs on whatever host serves the files (IP, user agent, referrer). We do not use those to sell ads today.</li>
<li>Optional local history in your browser (<code>localStorage</code> key <code>hf-hist</code>) so shuffle can remember recent niches. You can clear site data anytime.</li>
<li>If you email us, we keep the message long enough to reply.</li>
</ul>
<h2>What we do not collect</h2>
<ul>
<li>TikTok, Google, Meta, or CapCut passwords. We never ask.</li>
<li>Payment cards. The tool is free.</li>
<li>Health or financial account data. Do not paste it into the idea box.</li>
</ul>
<h2>Cookies</h2>
<p>No tracking pixels ship with this version. If a future host injects analytics, this page will name it.</p>
<h2>Children</h2>
<p>The site is written for adults and working teens who already post publicly. It is not directed at children under 13.</p>
<h2>Contact</h2>
<p><a href="mailto:hello@hookforge.app">hello@hookforge.app</a></p>
""",
    trail=[("Home", "/"), ("Privacy", None)],
)

# ---- terms ----
page(
    "terms/",
    "Terms of Use | HookForge",
    "Terms for the free HookForge TikTok hook generator. No warranties. You own what you film. Do not abuse the site.",
    "Terms of use",
    f"""
<p>Last updated {TODAY}.</p>
<p>HookForge is provided free, as is. Output is a draft. You are responsible for what you publish, including copyright, likeness, and platform rules.</p>
<h2>License to you</h2>
<p>You may film and post generated lines. You may not copy the site design, scrape at a rate that harms the host, or imply we endorse your video.</p>
<h2>No guarantees</h2>
<p>We do not promise views, revenue, employment, or algorithmic favor. “Viral” in our copy means “written to stop a thumb,” not “will go viral.”</p>
<h2>Acceptable use</h2>
<ul>
<li>No malware, phishing, or credential collection via our embed.</li>
<li>No medical, legal, or financial advice presented as ours.</li>
<li>No impersonation of TikTok, YouTube, Instagram, Meta, or CapCut.</li>
</ul>
<p>Trademarks belong to their owners. HookForge is not affiliated with them.</p>
<p>Governing language: English (US). Contact: hello@hookforge.app</p>
""",
    trail=[("Home", "/"), ("Terms", None)],
)

print("static pages done")
