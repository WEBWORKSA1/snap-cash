# Snap.Cash

**Fast, legit ways to make, save & find cash.** Snap.Cash is a static website hosted on GitHub Pages (free plan). It includes a lead-generation quiz, a side-hustle directory, a cashback comparison, 10 calculators, 7 guides, a video hub, contests, donations, careers and advertiser pages.

- 🌐 Live: https://webworksa1.github.io/Snap-Cash/
- 📈 Strategy & research: [`docs/STRATEGY.md`](docs/STRATEGY.md)
- 🧭 Phase-wise build prompts: [`docs/PHASE-PROMPTS.md`](docs/PHASE-PROMPTS.md)

## How it's built & deployed
Page HTML is generated from `_src/*.py`. On every push to `main`, the GitHub Action in `.github/workflows/pages.yml` runs `python3 _src/build.py` and publishes the finished site to the `gh-pages` branch. GitHub Pages serves that branch. To preview locally, run `python3 _src/build.py`, then `python3 -m http.server`.

## Go-live checklist
1. **Pages:** go to repo **Settings → Pages** and set *Source* to "Deploy from a branch", branch `gh-pages` / root. GitHub usually sets this automatically.
2. **Forms:** the first time any form is submitted on the live site, FormSubmit sends a one-time **activation email** to the site owner's inbox. Click *Activate*. After that, every form delivers. Optional: paste the random alias FormSubmit gives you into `formAlias` in `assets/js/config.js`.
3. **AdSense:** add your `ca-pub-…` ID to `adsenseClient` in `assets/js/config.js`, then update `ads.txt` (it's generated from `_src/build.py` the first time). Ads load only after the visitor gives cookie consent.
4. **Donations:** paste your PayPal, Stripe, Buy Me a Coffee, Ko-fi and Patreon links into `donate` in `config.js`. Any empty link falls back to the pledge form.
5. **Custom domain (snap.cash):** in your registrar, add `A` records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153` (plus `CNAME www → webworksa1.github.io`). Then go to **Settings → Pages → Custom domain → `snap.cash`** and tick *Enforce HTTPS*. All links are relative, so nothing breaks.
6. **Analytics (optional):** add a GA4 ID to `ga4` in `config.js`.

## Editing content
- The directory, apps and videos live in `assets/js/data.js`. Add rows there.
- To add or change a calculator, edit the `CALCS` array in `assets/js/calc.js`.
- Pages live in `_src/pages_main.py`, `_src/pages_community.py`, `_src/pages_legal.py` and `_src/guides.py`. The shared layout is in `_src/layout.py`.

## Legal
Snap.Cash is an independent publication. It is **not** affiliated with Snap Inc. (Snapchat), Block, Inc. (Cash App / Square), or the discontinued "Snapcash" feature. Third-party names are used for identification only. © Snap.Cash. All rights reserved. See `disclaimer.html`.
