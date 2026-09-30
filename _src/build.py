#!/usr/bin/env python3
"""Build Snap.Cash.

  python3 _src/build.py            -> GitHub Pages (Jekyll) output: small pages + _includes/header.html & footer.html
  python3 _src/build.py --static   -> fully expanded static HTML (for Netlify/Vercel/any host, or local preview)
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
from layout import page, page_hero, SITE, LOGO
import pages_main, pages_community, pages_legal, guides

pages = {}
for mod in (pages_main, pages_community, pages_legal):
    pages.update(mod.PAGES)
pages.update(guides.build_guides())

# 404 — works at any depth on GitHub Pages (project path or custom domain)
p404 = page("404.html", "Page not found", "This page could not be found.",
            page_hero("404", "This page took the cash and ran 💨", "The page you're looking for doesn't exist or has moved.") +
            '<section class="section" style="padding-top:0"><div class="container"><div class="hero-cta"><a class="btn btn-primary" href="index.html">Go home</a><a class="btn btn-ghost" href="make-money.html">Ways to make money</a><a class="btn btn-ghost" href="tools.html">Calculators</a></div></div></section>',
            noindex=True, show_disclosure=False)
p404 = p404.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<script>document.write(\'<base href="\'+(/^\\/snap-cash\\//i.test(location.pathname)?location.pathname.slice(0,11):"/")+\'">\')</script>', 1)
pages["404.html"] = p404

STATIC = "--static" in sys.argv
import re, layout
from layout import NAV, header, footer

LB = "{{ include.base }}"
HDR_T = header("", LB)
for h, t in NAV:  # add active-state logic to the main nav only (first occurrence)
    HDR_T = HDR_T.replace(f'<a href="{LB}{h}">{t}</a>', f'<a href="{LB}{h}"{{% if include.active == "{h}" %}} aria-current="page"{{% endif %}}>{t}</a>', 1)
FTR_T = footer(LB)


def liquid_emulate(tpl, base, active=""):
    out = tpl.replace(LB, base)
    return re.sub(r'\{% if include\.active == "([^"]+)" %\}( aria-current="page")\{% endif %\}', lambda m: m.group(2) if m.group(1) == active else "", out)


assert liquid_emulate(HDR_T, "", "tools.html") == header("tools.html", "")
assert liquid_emulate(FTR_T, "../") == footer("../")


def jekyllize(path, html):
    base = "../" if "/" in path else ""
    active = next((h for h, _ in [("", "")] + NAV if header(h, base) in html), None)
    assert active is not None, f"header not found in {path}"
    out = html.replace(header(active, base), f'\n{{% include header.html base="{base}" active="{active}" %}}', 1)
    assert footer(base) in out, f"footer not found in {path}"
    out = out.replace(footer(base), f'\n{{% include footer.html base="{base}" %}}', 1)
    # self-check: emulated Liquid render must equal the fully static page
    check = out.replace(f'\n{{% include header.html base="{base}" active="{active}" %}}', liquid_emulate(HDR_T, base, active))
    check = check.replace(f'\n{{% include footer.html base="{base}" %}}', liquid_emulate(FTR_T, base))
    assert check == html, f"jekyll round-trip mismatch in {path}"
    return "---\nlayout: null\n---\n" + out


for path, html in pages.items():
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html if STATIC else jekyllize(path, html))
if not STATIC:
    os.makedirs(os.path.join(ROOT, "_includes"), exist_ok=True)
    open(os.path.join(ROOT, "_includes/header.html"), "w", encoding="utf-8").write(HDR_T)
    open(os.path.join(ROOT, "_includes/footer.html"), "w", encoding="utf-8").write(FTR_T)
    open(os.path.join(ROOT, "_config.yml"), "w").write("# GitHub Pages (Jekyll) config for Snap.Cash\nexclude: [README.md, docs, _src]\ndefaults:\n  - scope:\n      path: \"\"\n    values:\n      layout: null\n")

# sitemap / robots / ads.txt / manifest / icons
urls = [p for p in pages if p != "404.html"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in sorted(urls):
    loc = SITE + "/" + ("" if u == "index.html" else u)
    pr = "1.0" if u == "index.html" else ("0.9" if u in ("get-matched.html", "make-money.html", "tools.html") else "0.7")
    sm.append(f"  <url><loc>{loc}</loc><lastmod>2026-09-30</lastmod><priority>{pr}</priority></url>")
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
if not os.path.exists(os.path.join(ROOT, "ads.txt")):
    open(os.path.join(ROOT, "ads.txt"), "w").write("# Replace pub-0000000000000000 with your AdSense publisher ID, then remove the leading '#'.\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
open(os.path.join(ROOT, "manifest.webmanifest"), "w").write(json.dumps({
    "name": "Snap.Cash", "short_name": "Snap.Cash", "start_url": "./index.html", "display": "standalone",
    "background_color": "#f7faf8", "theme_color": "#00a86b",
    "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2))
os.makedirs(os.path.join(ROOT, "assets/img"), exist_ok=True)
open(os.path.join(ROOT, "assets/img/favicon.svg"), "w").write(LOGO.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1))
open(os.path.join(ROOT, "assets/img/og-image.svg"), "w").write(
    '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#053322"/><stop offset="1" stop-color="#0b6a45"/></linearGradient></defs>'
    '<rect width="1200" height="630" fill="url(#g)"/><path d="M640 90 450 360h130l-45 190 205-290H610z" fill="#ffd34d" opacity=".95"/>'
    '<text x="80" y="300" font-family="Arial,Helvetica,sans-serif" font-size="110" font-weight="800" fill="#fff">Snap.Cash</text>'
    '<text x="84" y="380" font-family="Arial,Helvetica,sans-serif" font-size="40" fill="#bff5dc">Fast, legit ways to make, save &amp; find cash</text></svg>')
nj = os.path.join(ROOT, ".nojekyll")
if STATIC:
    open(nj, "w").write("")
elif os.path.exists(nj):
    os.remove(nj)
print(f"Built {len(pages)} pages ({'static' if STATIC else 'GitHub Pages/Jekyll'} mode)")
