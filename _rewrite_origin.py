#!/usr/bin/env python3
"""Rewrite hookforge.app + root paths for GitHub Pages project sites."""
from pathlib import Path
import os
import re

ROOT = Path(__file__).resolve().parent
OLD = "https://hookforge.app"

repo = os.environ.get("GITHUB_REPOSITORY", "")
owner = os.environ.get("GITHUB_REPOSITORY_OWNER", "")
if "/" in repo:
    owner, name = repo.split("/", 1)
else:
    name = os.environ.get("GITHUB_PAGES_REPO", "hookforge")

forced = os.environ.get("SITE_ORIGIN", "").rstrip("/")
if forced:
    site = forced
    from urllib.parse import urlparse
    path = urlparse(forced).path.rstrip("/")
    base = path
else:
    if owner and name.lower() == f"{owner}.github.io".lower():
        site = f"https://{owner}.github.io"
        base = ""
    elif owner:
        site = f"https://{owner}.github.io/{name}"
        base = f"/{name}"
    else:
        raise SystemExit("Set GITHUB_REPOSITORY or SITE_ORIGIN")

SKIP = {".py", ".pyc", ".md"}
TEXT = {".html", ".xml", ".txt", ".webmanifest", ".css", ".js", ".svg"}


def rewrite(text: str) -> str:
    text = text.replace(OLD, site)
    if not base:
        return text

    def abs_url(m):
        attr, quote, path = m.group(1), m.group(2), m.group(3)
        if path.startswith("//") or path.startswith(base + "/"):
            return m.group(0)
        return f"{attr}={quote}{base}{path}{quote}"

    text = re.sub(
        r"""\b(href|src|action|content)=(['"])(/(?!/)[^'"]*)\2""",
        abs_url,
        text,
    )
    return text


n = 0
for p in ROOT.rglob("*"):
    if not p.is_file() or p.suffix in SKIP or p.name.startswith("_"):
        continue
    if p.suffix not in TEXT and p.name not in {"robots.txt", "humans.txt", "llms.txt", "security.txt"}:
        continue
    raw = p.read_text(encoding="utf-8")
    out = rewrite(raw)
    if out != raw:
        p.write_text(out, encoding="utf-8")
        n += 1
print(f"origin={site} base={base or '/'} files={n}")
