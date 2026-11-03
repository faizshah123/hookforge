(function () {
  const D = window.HF_DATA;
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));

  function seedFrom(str) {
    let h = 2166136261;
    for (let i = 0; i < str.length; i++) h = Math.imul(h ^ str.charCodeAt(i), 16777619);
    return h >>> 0;
  }
  function rng(seed) {
    let s = seed || 1;
    return function () {
      s = (s * 1664525 + 1013904223) >>> 0;
      return s / 4294967296;
    };
  }
  function pick(rand, arr) { return arr[Math.floor(rand() * arr.length)]; }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  function clip(s, n) { s = s.replace(/\s+/g, " ").trim(); return s.length <= n ? s : s.slice(0, n - 1).trim() + "…"; }
  function words(s) { return (s.match(/[A-Za-z0-9']+/g) || []).length; }

  function parseIdea(idea, niche) {
    const raw = (idea || "").trim();
    const topic = raw || ("a " + niche.toLowerCase() + " clip");
    const noun = topic.replace(/^(how to|why|what|when|the)\s+/i, "").replace(/[.?!]+$/, "");
    return { topic, noun, niche };
  }

  function buildHooks(ctx, platform, tone, n) {
    const { topic, noun, niche } = ctx;
    const t = topic.replace(/[.?!]+$/, "");
    const N = niche.replace(/&/g, "and");
    const lines = [
      "Wait… you still " + t + " like this?",
      "POV: you just learned " + t + " the hard way.",
      "Nobody in " + N + " talks about this part of " + t + ".",
      "I lost 3 hours because I did " + t + " wrong.",
      "If your " + t + " looks mid, it’s this one setting.",
      "Do not post " + t + " until you hear this.",
      "US creators using " + t + " are quietly winning comments.",
      "The 7-second version of " + t + " nobody teaches.",
      "This is the " + t + " advice I wish I had in 2024.",
      "Stop copying " + t + " tutorials that skip the hook.",
      t + " — but make it scroll-stopping in 8 words.",
      "Why your " + t + " dies at 200 views.",
      "I tested " + t + " for 14 days. Here’s the ugly part.",
      "Your " + t + " is fine. Your first line is not.",
      "Tell me you do " + t + " without telling me.",
      "The unsexy truth about " + t + ".",
      "If I had to restart " + t + " tomorrow, I’d do this first.",
      "Comment “HOOK” if your " + t + " needs a rewrite.",
      "This " + t + " trick is legal, free, and overused by no one.",
      "On-screen text that actually sells " + t + ".",
      "Save this before you film " + t + ".",
      "The caption that made " + t + " perform 4x.",
      "You’re filming " + t + ". You’re not opening it.",
      "A boring " + t + " with a violent first frame.",
      "Parents in the US keep asking me about " + t + ".",
      "Day 1 vs day 30 of posting " + t + ".",
      "I was wrong about " + t + ". Watch.",
      "Three signs your " + t + " hook is dead on arrival.",
      "Steal this " + t + " opener. I don’t care.",
      "The algorithm didn’t kill your " + t + ". The first second did."
    ];
    const seed = seedFrom([t, N, platform, tone, n, Date.now().toString().slice(0, 8)].join("|"));
    const rand = rng(seed);
    const shuffled = lines.slice().sort(() => rand() - 0.5);
    const formulas = D.formulas;
    return shuffled.slice(0, n).map((text, i) => {
      const f = formulas[i % formulas.length];
      const hook = clip(cap(text), 78);
      return {
        i: i + 1,
        formula: f.name,
        hook,
        onScreen: clip(hook.replace(/^POV:\s*/i, "").replace(/[.]+$/, ""), 42),
        words: words(hook)
      };
    });
  }

  function captionFor(ctx, platform, tone, hooks) {
    const h = hooks[0] ? hooks[0].hook : ctx.topic;
    const p = D.platforms[platform] || D.platforms.tiktok;
    const body = [
      h,
      "",
      "I broke this down so you can film today — no course, no email wall.",
      "Hook → on-screen text → caption. Copy what you need.",
      "",
      "Which line would you actually say out loud? Comment the number.",
      "",
      "Follow for more free " + p.label + " openers for US creators."
    ].join("\n");
    return clip(body, platform === "reels" ? 2200 : 2200);
  }

  function hashtags(ctx, platform) {
    const p = D.platforms[platform] || D.platforms.tiktok;
    const nicheSlug = ctx.niche.toLowerCase().replace(/[^a-z0-9]+/g, "");
    const ideaSlug = ctx.noun.toLowerCase().replace(/[^a-z0-9]+/g, "").slice(0, 18);
    const core = [nicheSlug, ideaSlug, "contentcreator", "uscreator", "hook", "captionideas", "creatorhelp"].filter(Boolean);
    const tags = Array.from(new Set(p.tags.concat(core))).slice(0, 9);
    return tags.map((t) => "#" + t);
  }

  function cta(platform) {
    const map = {
      tiktok: "Follow for daily free hooks. Duet this with your take.",
      shorts: "Subscribe for Shorts openers. Comment your niche.",
      reels: "Save this Reel and try line #1 tomorrow.",
      capcut: "Paste the on-screen text into CapCut Auto captions.",
      facebook: "Share to your Page, then pin the comment with the full list."
    };
    return map[platform] || map.tiktok;
  }

  function render(out, data) {
    out.innerHTML = "";
    const block = (title, html) => {
      const el = document.createElement("article");
      el.className = "hook";
      el.innerHTML = '<div class="meta"><strong>' + title + '</strong><button type="button" class="copy">Copy</button></div>' + html;
      const btn = $(".copy", el);
      const payload = el.querySelector("[data-copy]") ? el.querySelector("[data-copy]").textContent : el.innerText.replace(/^Copy\n?/, "");
      btn.addEventListener("click", async () => {
        try { await navigator.clipboard.writeText(payload.trim()); btn.textContent = "Copied"; setTimeout(() => btn.textContent = "Copy", 1200); }
        catch (e) { btn.textContent = "Select & copy"; }
      });
      out.appendChild(el);
    };

    data.hooks.forEach((h) => {
      block("Hook " + h.i + " · " + h.formula + " · " + h.words + " words",
        '<p data-copy>' + escapeHtml(h.hook) + '</p><p class="meta">On-screen: ' + escapeHtml(h.onScreen) + "</p>");
    });
    block("Caption", "<pre data-copy style='white-space:pre-wrap;margin:0;font:inherit'>" + escapeHtml(data.caption) + "</pre>");
    block("Hashtags", "<p data-copy>" + escapeHtml(data.tags.join(" ")) + "</p>");
    block("CTA + CapCut text", "<p data-copy>" + escapeHtml(data.cta + "\n\n" + data.hooks.map((h, i) => (i + 1) + ". " + h.onScreen).join("\n")) + "</p>");

    const preview = $("#preview");
    if (preview) {
      $(".os", preview).textContent = data.hooks[0].onScreen;
      $(".cap", preview).textContent = clip(data.caption.replace(/\n+/g, " "), 90);
      $(".badge", preview).textContent = data.platformLabel;
    }
    const json = {
      "@context": "https://schema.org",
      "@type": "HowTo",
      name: "Generated " + data.platformLabel + " hook pack",
      step: data.hooks.map((h) => ({ "@type": "HowToStep", name: h.formula, text: h.hook }))
    };
    let ld = $("#live-howto");
    if (!ld) {
      ld = document.createElement("script");
      ld.type = "application/ld+json";
      ld.id = "live-howto";
      document.head.appendChild(ld);
    }
    ld.textContent = JSON.stringify(json);
    try {
      const hist = JSON.parse(localStorage.getItem("hf-hist") || "[]");
      hist.unshift({ t: Date.now(), niche: data.niche, idea: data.idea, platform: data.platform });
      localStorage.setItem("hf-hist", JSON.stringify(hist.slice(0, 12)));
    } catch (e) {}
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }

  function generate() {
    const niche = $("#niche").value;
    const idea = $("#idea").value;
    const platform = $("#platform").value;
    const tone = $("#tone").value;
    const n = Math.min(12, Math.max(6, parseInt($("#count").value, 10) || 10));
    const ctx = parseIdea(idea, niche);
    const hooks = buildHooks(ctx, platform, tone, n);
    const data = {
      niche, idea: ctx.topic, platform,
      platformLabel: (D.platforms[platform] || {}).label || platform,
      hooks,
      caption: captionFor(ctx, platform, tone, hooks),
      tags: hashtags(ctx, platform),
      cta: cta(platform)
    };
    render($("#results"), data);
    $("#results-wrap").hidden = false;
    $("#results-wrap").scrollIntoView({ behavior: "smooth", block: "start" });
    const url = new URL(location.href);
    url.searchParams.set("niche", niche);
    url.searchParams.set("idea", ctx.topic.slice(0, 80));
    url.searchParams.set("p", platform);
    history.replaceState(null, "", url);
  }

  function fillSelect(id, items, getVal, getLabel) {
    const el = document.getElementById(id);
    if (!el) return;
    el.innerHTML = items.map((it) => {
      const v = getVal ? getVal(it) : it;
      const l = getLabel ? getLabel(it) : it;
      return "<option value=\"" + v + "\">" + l + "</option>";
    }).join("");
  }

  function boot() {
    const navBtn = $(".menu-btn");
    const nav = $(".nav");
    if (navBtn && nav) navBtn.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      navBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });

    if (!$("#hook-form")) return;
    fillSelect("niche", D.niches);
    fillSelect("platform", Object.keys(D.platforms), (k) => k, (k) => D.platforms[k].label);
    fillSelect("tone", D.tones);
    const params = new URLSearchParams(location.search);
    if (params.get("niche") && D.niches.includes(params.get("niche"))) $("#niche").value = params.get("niche");
    if (params.get("idea")) $("#idea").value = params.get("idea");
    if (params.get("p") && D.platforms[params.get("p")]) $("#platform").value = params.get("p");
    const preset = document.body.getAttribute("data-platform");
    if (preset && D.platforms[preset]) $("#platform").value = preset;
    $$(".chip").forEach((c) => c.addEventListener("click", () => {
      $("#idea").value = c.getAttribute("data-idea");
      $$(".chip").forEach((x) => x.classList.remove("on"));
      c.classList.add("on");
    }));
    $("#hook-form").addEventListener("submit", (e) => { e.preventDefault(); generate(); });
    $("#shuffle") && $("#shuffle").addEventListener("click", generate);
    if (params.get("idea")) generate();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
