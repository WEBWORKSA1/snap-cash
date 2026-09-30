# Snap.Cash

**Fast, legit ways to make, save & find cash.** Snap.Cash is a static website hosted on GitHub Pages (free plan). It includes a lead-generation quiz, a side-hustle directory, a cashback comparison, 10 calculators, 7 guides, a video hub, contests, donations, careers and advertiser pages.

- 🌐 Live: https://webworksa1.github.io/snap-cash/
- 📈 Strategy & research: [`docs/STRATEGY.md`](docs/STRATEGY.md)
- 🧭 Phase-wise build prompts: [`docs/PHASE-PROMPTS.md`](docs/PHASE-PROMPTS.md)

## How it's built & deployed
The HTML pages in the repo root are generated from `_src/*.py`. After you edit anything in `_src/`, run `python3 _src/build.py` and commit the regenerated files. GitHub Pages serves the static files directly, with no build step, from the `gh-pages` branch or from `main` / root. To preview locally, run `python3 -m http.server`.

## Go-live checklist
1. **Pages:** go to repo **Settings → Pages → Build and deployment → Deploy from a branch**, then choose `gh-pages` (or `main`) and `/ (root)`.
2. **Forms:** the first time any form is submitted on the live site, FormSubmit sends a one-time **activation email** to the site owner's inbox. Click *Activate*. After that, every form delivers. Optional: paste the random alias FormSubmit gives you into `formAlias` in `assets/js/config.js`.
3. **AdSense:** add your `ca-pub-…` ID to `adsenseClient` in `assets/js/config.js`, then edit `ads.txt`. Ads load only after the visitor gives cookie consent.
4. **Donations:** paste your PayPal, Stripe, Buy Me a Coffee, Ko-fi and Patreon links into `donate` in `config.js`. Any empty link falls back to the pledge form.
5. **Custom domain (snap.cash):** in your registrar, add `A` records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153` (plus `CNAME www → webworksa1.github.io`). Then go to **Settings → Pages → Custom domain → `snap.cash`** and tick *Enforce HTTPS*. All links are relative, so nothing breaks.
6. **Analytics (optional):** add a GA4 ID to `ga4` in `config.js`.

## Editing content
- The directory, apps and videos live in `assets/js/data.js`. Add rows there. No rebuild is needed.
- To add or change a calculator, edit the `CALCS` array in `assets/js/calc.js`. No rebuild is needed.
- Pages live in `_src/pages_main.py`, `_src/pages_community.py`, `_src/pages_legal.py` and `_src/guides.py`. The shared layout is in `_src/layout.py`. Rebuild after editing any of these.

## Legal
Snap.Cash is an independent publication. It is **not** affiliated with Snap Inc. (Snapchat), Block, Inc. (Cash App / Square), or the discontinued "Snapcash" feature. Third-party names are used for identification only. © Snap.Cash. All rights reserved. See `disclaimer.html`.
