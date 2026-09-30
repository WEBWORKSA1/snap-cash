# Snap.Cash — Phase-wise Build Prompts

Use these prompts in order with an AI coding assistant to rebuild or extend the site. Phases 1–6 are **already implemented** in this repo. Phases 7–10 are the growth roadmap.

---

## Phase 0 — Global rules (paste before every phase)
> You are building **Snap.Cash**, an independent "fast, legit ways to make, save & find cash" hub. Stack: static HTML, one CSS file, vanilla JS. No build step at runtime, and it must be hostable on the GitHub Pages free plan. Every link must be relative, so it works both at `/snap-cash/` and on a custom domain.
> - **Top of every page:** a bar reading "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership" that links to https://web.works/contact.
> - **All forms** post via AJAX to one hidden endpoint. The destination address is stored obfuscated in `assets/js/config.js` and assembled at runtime. **Never** print an email address or a `mailto:` link anywhere.
> - **Brand safety:** always write "Snap.Cash". Never write "Snapcash". No Snapchat or Cash App colours, logos or payment features. Include the non-affiliation notice in every footer.
> - Mobile-first. WCAG AA contrast. Dark mode. No fake reviews, ratings or user counts.

## Phase 1 — Foundation & design system
> Create `assets/css/style.css` with design tokens (green money palette, amber accent, Inter + Space Grotesk, 16px radius), light and dark themes, and components: buttons, cards, chips, forms, a multi-step quiz, calculator panels, a result box, FAQ accordions, a CTA band, the cookie banner, a sticky mobile CTA, a modal and ad slots. Create a Python generator (`_src/layout.py`) that outputs head (SEO, Open Graph, JSON-LD), the top bar, a sticky header with nav, the disclosure strip, the footer (trademark, copyright, not-advice notices), the cookie consent banner, the exit-intent modal and the script tags.

## Phase 2 — Core pages & content
> Build: Home (hero, above-the-fold Cash Finder, trust stats, category cards, fastest-cash grid, inline calculator, videos, giveaway teaser, FAQ with FAQPage schema, newsletter, support band). Also Make Money (a searchable directory filtered by speed and "what I have"), Cashback (app comparison plus 4-layer stacking), Guides index plus 7 long-form guides (Article schema, TOC, embedded calculator, related links), Video hub, About, and How We Make Money.

## Phase 3 — Lead-generation engine
> Build a 6-step quiz: goal → amount → speed → assets (multi-select) → country/postcode → name, email, optional phone. It should have a progress bar, auto-advance, back buttons, URL pre-fill (`?goal=earn&method=…`), and separate consent boxes for email (required), SMS (optional) and partners (optional). On submit, POST all answers and show an instant "Top 5 fastest cash moves" result, ranked by matching assets and speed. Add a dedicated `get-matched.html` landing page with benefits, FAQ and a B2B "become a lead partner" block. Put a newsletter form on every page and a desktop exit-intent playbook offer.

## Phase 4 — Monetisation layer
> Add config-driven AdSense: a publisher ID in `config.js` activates every `.ad-slot` (header, inContent, sidebar), loaded only after the visitor consents. Add optional GA4. Add `ads.txt`, `robots.txt`, `sitemap.xml` and a manifest. Add lite YouTube embeds (thumbnail first, `youtube-nocookie` iframe on click) driven by `data.js`. Add an Advertise page with sponsorship, newsletter, giveaway and lead-partner packages and an inquiry form with budget and interest fields.

## Phase 5 — Community: donations, contests, hiring
> Support page: preset amounts, custom amount, PayPal/Stripe/Buy Me a Coffee/Ko-fi/Patreon buttons read from config (falling back to a pledge form), fund allocation ("operations, promotion & marketing, hiring, prizes"), a supporters-wall opt-in, 3 membership tiers and a non-deductible notice. Contests page: live countdown, entry form, referral link with bonus entries, upcoming challenges, a prize-sponsor block, and a separate Official Rules page (NO PURCHASE NECESSARY, eligibility, ARV, odds, skill-testing question). Careers page: role cards, "write for us", and an application form.

## Phase 6 — Legal, QA & deploy
> Add the Disclaimer (trademark non-affiliation, copyright, DMCA, affiliate, earnings, not-advice), Privacy (AdSense cookie language, CCPA "Do Not Sell or Share", GDPR/PIPEDA/Law 25, CAN-SPAM/CASL, SMS) and Terms pages, plus a 404 page that works at any depth. QA: no horizontal scroll at 390px, no console errors, every form posts, `grep` finds zero email addresses. Deploy to GitHub Pages.

## Phase 7 — Growth: programmatic SEO (next)
> Generate 100+ long-tail pages from `data.js`: "/how-to-make-money-with-[asset]", "/[city]-side-hustles", "/[app]-review", "/[app]-vs-[app]". Each page gets unique intro copy, a pay table, a calculator embed, FAQ schema and internal links. Add breadcrumbs schema and an HTML sitemap.

## Phase 8 — Offers & bonus tracker
> Add `offers.json` (bank bonuses and cashback boosts with expiry dates) that renders a filterable "Live Bonuses" page with "ends soon" badges and a weekly auto-generated email digest. Mark sponsored rows clearly.

## Phase 9 — Accounts & personalisation (optional backend)
> Add optional sign-in (e.g. Supabase or Firebase free tier): saved plans, a goal tracker ("$0 → $1,000"), streaks, and supporter badges. Keep static hosting. Call the backend from the client only.

## Phase 10 — Scale
> Launch a YouTube Shorts series built from the guides and embed it on the site. Add multilingual versions (fr-CA, es, hi). Pursue direct lead-buyer deals. Run A/B tests on quiz headlines and CTA copy through a lightweight experiment flag in `config.js`.
