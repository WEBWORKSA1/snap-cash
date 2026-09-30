"""Shared layout for Snap.Cash static pages."""
import datetime, json

SITE = "https://snap.cash"
YEAR = datetime.date.today().year
INQUIRY = "https://web.works/contact"

LOGO = ('<svg viewBox="0 0 48 48" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#19d18a"/><stop offset="1" stop-color="#00866a"/></linearGradient></defs>'
        '<rect width="48" height="48" rx="13" fill="url(#lg)"/><circle cx="24" cy="24" r="14" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/>'
        '<path d="M27 8 14 27h9l-3 13 14-20h-9z" fill="#ffd34d" stroke="#073b27" stroke-width="1.5" stroke-linejoin="round"/></svg>')

NAV = [("make-money.html", "Make Money"), ("cashback.html", "Cashback"), ("tools.html", "Tools"),
       ("guides.html", "Guides"), ("videos.html", "Videos"), ("contests.html", "Contests"), ("support.html", "Support")]


def head(title, desc, path, base="", extra_ld=None, noindex=False):
    canon = f"{SITE}/{path}" if path != "index.html" else f"{SITE}/"
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": "Snap.Cash", "url": SITE,
           "logo": f"{SITE}/assets/img/favicon.svg"}]
    if extra_ld:
        ld += extra_ld if isinstance(extra_ld, list) else [extra_ld]
    full = title if "Snap.Cash" in title else f"{title} | Snap.Cash"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#00a86b">
<meta property="og:type" content="website"><meta property="og:site_name" content="Snap.Cash">
<meta property="og:title" content="{full}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{base}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>"""


def header(active, base=""):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{base}{h}"{cur if h == active else ""}>{t}</a>' for h, t in NAV)
    mlinks = "".join(f'<a href="{base}{h}">{t}</a>' for h, t in NAV) + \
        f'<a href="{base}advertise.html">Advertise &amp; Partner</a><a href="{base}careers.html">Careers</a><a href="{base}contact.html">Contact</a>'
    return f"""
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note"><a href="{INQUIRY}" data-inquiry target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="{base}index.html" aria-label="Snap.Cash home">{LOGO}<span>Snap<b>.</b>Cash</span></a>
    <nav class="nav-links" aria-label="Main">{links}</nav>
    <div class="nav-actions">
      <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
      <a class="btn btn-primary btn-sm" href="{base}get-matched.html">Get My Cash Plan</a>
      <button class="icon-btn menu-toggle" aria-label="Open menu" aria-expanded="false"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    </div>
  </div>
  <nav class="mobile-menu" aria-label="Mobile">{mlinks}</nav>
</header>"""


def disclosure(base=""):
    return (f'<div class="disclosure-strip">Advertiser disclosure: some links may earn us a commission at no cost to you. '
            f'It never changes our rankings. <a href="{base}how-we-make-money.html">How we make money</a></div>')


def ad(kind="inContent"):
    return f'<div class="container"><div class="ad-slot" data-ad="{kind}" aria-label="Advertisement">Advertisement</div></div>'


def newsletter_band(base="", title="One smart money move. Every morning.", sub="Join the free Snap.Cash Daily: fresh side hustles, cashback stacks, bonus alerts and giveaways. 60 seconds to read. No spam, unsubscribe anytime."):
    return f"""
<section class="section"><div class="container">
  <div class="cta-band reveal">
    <div><span class="eyebrow" style="background:#0e4d34;color:#9ff0c9">Free newsletter</span><h2>{title}</h2><p>{sub}</p></div>
    <form class="form" data-form="Newsletter" data-success="You're in! Check your inbox for a welcome gift.">
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
      <div class="inline-form"><input type="text" name="First name" placeholder="First name" required autocomplete="given-name" aria-label="First name">
      <input type="email" name="email" placeholder="Email address" required autocomplete="email" aria-label="Email"></div>
      <label class="check" style="color:#c7f3de"><input type="checkbox" name="Email consent" value="yes" required> I agree to receive the Snap.Cash newsletter. See our <a style="color:#ffd566" href="{base}privacy.html">Privacy Policy</a>.</label>
      <button class="btn btn-accent btn-block" type="submit">Send me the daily money move →</button>
      <div class="form-status" role="status"></div>
    </form>
  </div>
</div></section>"""


def support_band(base=""):
    return f"""
<section class="section alt"><div class="container center">
  <span class="eyebrow">Reader supported</span><h2>Keep Snap.Cash free for everyone</h2>
  <p class="muted" style="max-width:60ch;margin:0 auto 20px">Your support funds new tools, research, contests &amp; prizes, promotion, and hiring talented writers and developers.</p>
  <div class="hero-cta" style="justify-content:center"><a class="btn btn-primary" href="{base}support.html">❤ Support us</a><a class="btn btn-ghost" href="{base}advertise.html">Become a sponsor</a></div>
</div></section>"""


def footer(base=""):
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div class="foot-brand"><a class="logo" href="{base}index.html" style="color:#fff">{LOGO}<span>Snap<b>.</b>Cash</span></a>
        <p style="margin-top:12px">Fast, legit ways to make, save and find cash — with free tools, honest reviews and zero paywalls.</p>
        <a class="btn btn-accent btn-sm" href="{base}get-matched.html">Take the 2-minute Cash Finder</a></div>
      <div><h4>Earn &amp; save</h4><ul><li><a href="{base}make-money.html">Ways to make money</a></li><li><a href="{base}cashback.html">Cashback &amp; rewards</a></li><li><a href="{base}tools.html">Money calculators</a></li><li><a href="{base}guides.html">Guides</a></li><li><a href="{base}videos.html">Video hub</a></li></ul></div>
      <div><h4>Community</h4><ul><li><a href="{base}contests.html">Contests &amp; prizes</a></li><li><a href="{base}support.html">Donate / support</a></li><li><a href="{base}careers.html">Careers &amp; write for us</a></li><li><a href="{base}get-matched.html">Get matched</a></li></ul></div>
      <div><h4>Business</h4><ul><li><a href="{base}advertise.html">Advertise</a></li><li><a href="{base}advertise.html#partner">Partnerships</a></li><li><a href="{base}advertise.html#sponsor">Sponsorship</a></li><li><a href="{INQUIRY}" data-inquiry target="_blank" rel="noopener">Domain inquiry</a></li><li><a href="{base}contact.html">Contact</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="{base}about.html">About</a></li><li><a href="{base}how-we-make-money.html">How we make money</a></li><li><a href="{base}disclaimer.html">Disclaimers &amp; trademarks</a></li><li><a href="{base}privacy.html">Privacy &amp; cookies</a></li><li><a href="{base}terms.html">Terms of use</a></li><li><a href="{base}contest-rules.html">Official contest rules</a></li></ul></div>
    </div>
    <div class="legal">
      <p><b>Trademark notice:</b> Snap.Cash is an independent publication. It is not affiliated with, endorsed by, or sponsored by Snap Inc. (Snapchat), Block, Inc. (Cash App / Square), or the discontinued "Snapcash" payment feature. All third-party product names, logos and brands are the property of their respective owners and are used for identification purposes only.</p>
      <p><b>Not financial advice:</b> Content is for education only. Earnings shown are estimates, not guarantees. We may receive compensation from partners, which never influences our editorial ratings. <a href="{base}disclaimer.html">Full disclaimers</a>.</p>
      <p>© <span data-year>{YEAR}</span> Snap.Cash. All rights reserved. Original content, design and code are protected by copyright.</p>
    </div>
  </div>
</footer>
<div class="cookie" role="dialog" aria-label="Cookie consent"><b>We value your privacy 🍪</b><p class="small muted" style="margin:6px 0 0">We use cookies for analytics and personalized ads (Google AdSense). You can accept all or keep only essential cookies. <a href="{base}privacy.html#cookies">Learn more</a></p>
  <div class="btns"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div></div>
<div class="sticky-cta"><span>⚡ Find your fastest cash in 2 min</span><a class="btn btn-primary btn-sm" href="{base}get-matched.html">Start free</a></div>
<div class="modal" id="exit-modal" role="dialog" aria-modal="true" aria-labelledby="exit-title"><div class="panel">
  <button class="icon-btn close" data-close-modal aria-label="Close">✕</button>
  <span class="eyebrow">Before you go</span><h3 id="exit-title">Get the free "Make $500 This Month" playbook</h3>
  <p class="muted small">24 proven methods, sorted by speed. Delivered to your inbox with the Snap.Cash Daily.</p>
  <form class="form" data-form="Exit-intent playbook" data-success="Sent! Check your inbox.">
    <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
    <input type="email" name="email" placeholder="Your best email" required aria-label="Email">
    <label class="check"><input type="checkbox" name="Email consent" value="yes" required> Yes, send me the playbook and newsletter.</label>
    <button class="btn btn-primary btn-block" type="submit">Send my playbook</button><div class="form-status" role="status"></div>
  </form></div></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="{base}assets/js/config.js"></script>
<script src="{base}assets/js/data.js"></script>
<script src="{base}assets/js/app.js" defer></script>"""


def page(path, title, desc, body, active="", base="", extra_ld=None, scripts="", show_disclosure=True, noindex=False):
    return (head(title, desc, path, base, extra_ld, noindex) + f'\n<body data-base="{base}">' + header(active, base) +
            (disclosure(base) if show_disclosure else "") + '\n<main id="main">' + body + '</main>' + footer(base) +
            scripts + "\n</body>\n</html>\n")


def page_hero(eyebrow, h1, lead, crumbs=None, base="", extra=""):
    bc = ""
    if crumbs:
        bc = '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="' + base + 'index.html">Home</a> › ' + " › ".join(crumbs) + "</nav>"
    return f'<section class="page-hero"><div class="container">{bc}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div></section>'


def faq(items):
    html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, ld


def quiz(base="", heading="Find your fastest legit cash — in 2 minutes"):
    def opts(items):
        return "".join(f'<button type="button" class="opt" data-v="{v}"><span class="e">{e}</span>{t}</button>' for v, e, t in items)
    return f"""
<div class="panel quiz" id="cash-finder">
  <div class="progress" aria-hidden="true"><i></i></div>
  <form data-form="Cash Finder lead" data-quiz novalidate>
    <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
    <div class="step" data-name="goal"><div class="step-count"></div><h3>{heading}</h3><p class="muted small">What do you want to do first?</p>
      <div class="options">{opts([("earn","⚡","Earn extra cash"),("save","💸","Save &amp; get cashback"),("debt","🧾","Crush my debt"),("borrow","🏦","Compare borrowing options"),("business","🤝","Grow my business / partner")])}</div></div>
    <div class="step" data-name="amount"><div class="step-count"></div><h3>How much do you need?</h3>
      <div class="options">{opts([("$100","💵","About $100"),("$500","💰","About $500"),("$1,000","🤑","$1,000+"),("$5,000+","🏆","$5,000 or more")])}</div>
      <div class="step-nav"><button type="button" class="btn btn-ghost btn-sm" data-prev>← Back</button></div></div>
    <div class="step" data-name="speed"><div class="step-count"></div><h3>How fast?</h3>
      <div class="options">{opts([("Today","⚡","Today"),("This week","📅","This week"),("This month","🗓️","This month"),("Flexible","🌱","I'm flexible")])}</div>
      <div class="step-nav"><button type="button" class="btn btn-ghost btn-sm" data-prev>← Back</button></div></div>
    <div class="step" data-name="assets" data-multi><div class="step-count"></div><h3>What do you have? <span class="muted small">(pick all)</span></h3>
      <div class="options">{opts([("phone","📱","A smartphone"),("car","🚗","A car"),("computer","💻","A computer"),("home","🏠","Spare room / space"),("skills","🧠","A skill or trade"),("shopping","🛒","Regular shopping"),("outdoor","🚶","Time to get out locally")])}</div>
      <div class="step-nav"><button type="button" class="btn btn-ghost btn-sm" data-prev>← Back</button><button type="button" class="btn btn-primary btn-sm" data-next>Next →</button></div></div>
    <div class="step"><div class="step-count"></div><h3>Where are you?</h3>
      <div class="form-row"><div><label for="q-country">Country</label><select id="q-country" name="Country" required><option value="">Select…</option><option>United States</option><option>Canada</option><option>United Kingdom</option><option>Australia</option><option>India</option><option>Other</option></select></div>
      <div><label for="q-zip">ZIP / postal code <span class="muted">(optional)</span></label><input id="q-zip" name="Postal code" autocomplete="postal-code" maxlength="10"></div></div>
      <div class="step-nav"><button type="button" class="btn btn-ghost btn-sm" data-prev>← Back</button><button type="button" class="btn btn-primary btn-sm" data-next>Next →</button></div></div>
    <div class="step"><div class="step-count"></div><h3>Where should we send your personalized plan?</h3>
      <div class="form"><div class="form-row"><div><label for="q-name">First name</label><input id="q-name" name="First name" required autocomplete="given-name"></div>
      <div><label for="q-email">Email</label><input id="q-email" type="email" name="email" required autocomplete="email"></div></div>
      <div><label for="q-phone">Mobile <span class="muted">(optional — for SMS bonus alerts)</span></label><input id="q-phone" type="tel" name="Phone" autocomplete="tel"></div>
      <label class="check"><input type="checkbox" name="Email consent" value="yes" required> Email me my plan and the Snap.Cash Daily. Unsubscribe anytime.</label>
      <label class="check"><input type="checkbox" name="SMS consent" value="yes"> Optional: text me time-sensitive bonus alerts. Msg &amp; data rates may apply. Reply STOP to cancel.</label>
      <label class="check"><input type="checkbox" name="Partner offers consent" value="yes"> Optional: I'd like to be contacted about relevant offers from vetted partners.</label>
      <button class="btn btn-primary btn-lg btn-block" type="submit">Get my free cash plan →</button>
      <div class="form-status" role="status"></div>
      <p class="form-note">🔒 Free. No credit check. Your info is never sold. We only share it with a partner if you tick the partner box. <a href="{base}privacy.html">Privacy</a></p></div>
      <div class="step-nav"><button type="button" class="btn btn-ghost btn-sm" data-prev>← Back</button></div></div>
  </form>
</div>
<div class="quiz-result" hidden></div>"""
