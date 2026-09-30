from layout import page, page_hero, ad, newsletter_band, support_band, faq, quiz, SITE

PAGES = {}

# ---------------------------------------------------------------- HOME
home_faq, home_faq_ld = faq([
    ("What is Snap.Cash?", "Snap.Cash is a free, independent money hub that shows you fast, legitimate ways to make, save and find cash — side hustles, cashback apps, sign-up bonuses, calculators and step-by-step guides."),
    ("Is Snap.Cash free?", "Yes. Every tool, guide and the Cash Finder quiz are 100% free. We're supported by advertising, partner commissions and reader donations — never by paywalls."),
    ("How can I make money fast today?", "The fastest legit options are usually selling items you no longer need, gig delivery with instant cash-out, unused gift card exchanges and paid micro-tasks. Take the 2-minute Cash Finder for a plan matched to your situation."),
    ("Are you connected to Snapchat or Cash App?", "No. Snap.Cash is an independent publication and is not affiliated with Snap Inc., Block, Inc., Cash App, or the discontinued Snapcash feature."),
    ("How do you choose what to recommend?", "We rank methods on payout speed, earning potential, start-up cost, legitimacy and user experience. Partner compensation never changes our ratings — see How We Make Money."),
])

cats = [("make-money.html", "⚡", "Make money fast", "24+ legit side hustles filtered by speed, tools and pay."),
        ("cashback.html", "💸", "Cashback & rewards", "Get paid for shopping you already do. Stack apps for 2–3× returns."),
        ("tools.html", "🧮", "10 free calculators", "Side-hustle profit, debt payoff, savings growth, loan payments & more."),
        ("guides.html", "📚", "Step-by-step guides", "Plain-English playbooks for $100 today to $1,000 a month."),
        ("videos.html", "🎬", "Video hub", "Curated how-to videos from trusted finance educators."),
        ("contests.html", "🏆", "Contests & prizes", "Free-to-enter giveaways, challenges and community prizes.")]
cat_html = "".join(f'<a class="card cat-card reveal" href="{h}"><div class="ico">{e}</div><h3>{t}</h3><p>{d}</p></a>' for h, e, t, d in cats)

PAGES["index.html"] = page("index.html", "Snap.Cash — Fast, Legit Ways to Make, Save & Find Cash",
  "Find your fastest legit cash in 2 minutes. Free side-hustle directory, cashback stacking, money calculators, guides, videos and giveaways.",
  f"""
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="eyebrow">⚡ Free · Independent · No paywalls</span>
    <h1>Turn <span class="hl">spare time</span> into cash — <span class="rotator" data-rotate="today|this week|this month">today</span></h1>
    <p class="lead">Snap.Cash matches you with fast, legit ways to earn, save and stack cashback — plus free calculators that show exactly what each move is worth.</p>
    <div class="hero-cta"><a class="btn btn-primary btn-lg" href="#cash-finder">Find my fastest cash →</a><a class="btn btn-ghost btn-lg" href="tools.html">Run the numbers</a></div>
    <div class="trust-row"><span>No credit check</span><span>Never sells your data</span><span>2-minute quiz</span></div>
  </div>
  <div>{quiz()}</div>
</div></section>

<section class="section" style="padding-top:24px"><div class="container">
  <div class="stats">
    <div class="stat"><strong>24+</strong><span>Vetted ways to earn</span></div>
    <div class="stat"><strong>10</strong><span>Free money calculators</span></div>
    <div class="stat"><strong>2 min</strong><span>To your personal plan</span></div>
    <div class="stat"><strong>$0</strong><span>Cost, forever</span></div>
  </div>
</div></section>
{ad("header")}
<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Start here</span><h2>Everything you need to make money move</h2><p class="muted">Pick a lane — or let the Cash Finder pick for you.</p></div>
  <div class="grid g3" style="margin-top:28px">{cat_html}</div>
</div></section>

<section class="section alt"><div class="container">
  <div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:12px"><div><span class="eyebrow">⚡ Cash today</span><h2>Fastest legit ways to earn right now</h2></div><a class="btn btn-ghost" href="make-money.html">See all methods →</a></div>
  <div class="grid g3" id="hustle-grid" data-limit="6" style="margin-top:20px"></div>
  <p class="small muted" style="margin-top:14px">*Pay ranges are typical estimates, vary by location and demand, and are not guarantees.</p>
</div></section>

<section class="section"><div class="container two-col">
  <div class="reveal"><span class="eyebrow">How it works</span><h2>From "I need money" to a plan in 3 steps</h2>
    <ol class="list-check" style="font-size:1.05rem">
      <li><b>Answer 5 quick questions</b> — how much, how fast, and what you've got (phone, car, skills, spare room).</li>
      <li><b>Get your ranked plan</b> — the top 5 methods for you, with real pay ranges and start-up costs.</li>
      <li><b>Run the numbers &amp; go</b> — use our calculators, guides and videos to start today.</li>
    </ol><a class="btn btn-primary" href="get-matched.html">Get my plan</a></div>
  <div class="panel reveal"><h3>🧮 Quick check: how fast can you hit your goal?</h3><div id="calc-app" data-only="goal,hustle"></div></div>
</div></section>
{ad("inContent")}
<section class="section alt"><div class="container">
  <div class="center"><span class="eyebrow">Watch &amp; learn</span><h2>Money skills in minutes</h2></div>
  <div class="grid g3" id="video-grid" data-limit="3" style="margin-top:24px"></div>
  <div class="center" style="margin-top:20px"><a class="btn btn-ghost" href="videos.html">Open the video hub →</a></div>
</div></section>

<section class="section"><div class="container grid g2">
  <div class="card reveal"><span class="eyebrow">🏆 Live giveaway</span><h3>The $500 Snap Start Giveaway</h3><p class="muted">Free to enter. Earn bonus entries by sharing. No purchase necessary.</p><div class="countdown" data-countdown="2026-12-31T23:59:59-05:00"></div><p></p><a class="btn btn-accent" href="contests.html">Enter free →</a></div>
  <div class="card reveal"><span class="eyebrow">🤝 For brands</span><h3>Reach motivated earners &amp; savers</h3><p class="muted">Sponsored placements, newsletter features, giveaway sponsorships and lead-generation partnerships.</p><a class="btn btn-primary" href="advertise.html">Advertise with us</a> <a class="btn btn-ghost" href="https://web.works/contact" data-inquiry target="_blank" rel="noopener">Domain inquiry</a></div>
</div></section>

<section class="section alt"><div class="container" style="max-width:860px"><div class="center"><span class="eyebrow">FAQ</span><h2>Questions, answered</h2></div>{home_faq}</div></section>
{newsletter_band()}
{support_band()}
""", active="index.html",
  extra_ld=[{"@context": "https://schema.org", "@type": "WebSite", "name": "Snap.Cash", "url": SITE}, home_faq_ld],
  scripts='<script src="assets/js/calc.js" defer></script>')

# ---------------------------------------------------------------- MAKE MONEY
mm_faq, mm_faq_ld = faq([
    ("What's the fastest way to make money today?", "Selling items you already own, gig delivery with instant pay-out, gift card exchanges and plasma donation (where eligible) typically pay the same day."),
    ("How can I make money with just a phone?", "Surveys, micro-tasks, app testing, cashback receipt scanning, selling items on marketplaces and delivery gigs can all be done primarily from a smartphone."),
    ("Which side hustles pay the most?", "Skill-based work (freelancing, tutoring, AI data training for experts, trades) usually pays the most per hour. Asset-based income (renting a room or car) can pay the most per month."),
    ("How do I spot a scam?", "Never pay to get a job, never deposit a check and send money back, and never share login codes. Read our scam-avoidance guide."),
])
PAGES["make-money.html"] = page("make-money.html", "24+ Legit Ways to Make Money Fast (Filter by Speed & Tools)",
  "Filter legit side hustles by how fast they pay and what you have — phone, car, computer, skills or spare room. Real pay ranges and start-up costs.",
  page_hero("Make money", "Legit ways to make money — filtered for <em>you</em>", "Filter by how fast you need cash and what you've got. Every method shows typical pay, start-up cost and how quickly you can get paid.", ["Make money"]) + f"""
<section class="section" style="padding-top:24px"><div class="container">
  <input class="search" id="hustle-search" type="search" placeholder="Search e.g. delivery, tutoring, sell…" aria-label="Search methods" style="margin-bottom:16px">
  <div class="filters" aria-label="Speed"><b class="small" style="align-self:center;margin-right:6px">Speed:</b><button class="chip active" data-f-speed="all">All</button><button class="chip" data-f-speed="today">⚡ Cash today</button><button class="chip" data-f-speed="week">This week</button><button class="chip" data-f-speed="month">This month</button></div>
  <div class="filters" aria-label="What you have"><b class="small" style="align-self:center;margin-right:6px">I have:</b><button class="chip active" data-f-need="all">Anything</button><button class="chip" data-f-need="phone">📱 Phone</button><button class="chip" data-f-need="car">🚗 Car</button><button class="chip" data-f-need="computer">💻 Computer</button><button class="chip" data-f-need="skills">🧠 Skills</button><button class="chip" data-f-need="home">🏠 Space</button><button class="chip" data-f-need="shopping">🛒 Shopping</button><button class="chip" data-f-need="outdoor">🚶 Local time</button></div>
  <p class="small muted"><b id="hustle-count">0</b> methods match. *Pay ranges are typical U.S. estimates and not guarantees.</p>
  <div class="grid g3" id="hustle-grid"></div>
</div></section>
{ad("inContent")}
<section class="section alt"><div class="container two-col">
  <div><span class="eyebrow">Not sure where to start?</span><h2>Get a ranked plan built around your time, tools and goal</h2><p class="muted">The Cash Finder weighs speed, earning potential and start-up cost to rank your top five moves — then emails you the full plan.</p><ul class="list-check"><li>Personalized to your country</li><li>Only legit, vetted methods</li><li>Free, no credit check</li></ul></div>
  <div>{quiz()}</div>
</div></section>
<section class="section"><div class="container" style="max-width:860px"><h2>Make money FAQ</h2>{mm_faq}</div></section>
{newsletter_band()}
""", active="make-money.html", extra_ld=mm_faq_ld)

# ---------------------------------------------------------------- CASHBACK
PAGES["cashback.html"] = page("cashback.html", "Best Cashback & Rewards Apps + How to Stack Them",
  "Compare popular cashback and rewards apps by minimum cash-out and payout method, and learn how to stack them for 2–3× the rewards.",
  page_hero("Cashback & rewards", "Get paid for shopping you already do", "Compare popular cashback and rewards apps, then stack them. Most people leave $300–$700 a year on the table.*", ["Cashback"]) + f"""
<section class="section" style="padding-top:24px"><div class="container two-col">
  <div><h2>Popular cashback &amp; rewards apps compared</h2><p class="small muted">We don't publish fake ratings. Confirm current sign-up bonuses and terms on each provider's official site.</p>
    <div class="grid" id="apps-grid"></div></div>
  <aside><div class="sticky-side"><div class="panel"><h3>💸 What's your cashback worth?</h3><div id="calc-app" data-only="cashback"></div></div>{ad("sidebar").replace('class="container"','')}</div></aside>
</div></section>
<section class="section alt"><div class="container">
  <div class="center"><span class="eyebrow">The stacking method</span><h2>Stack 4 layers on one purchase</h2></div>
  <div class="grid g4" style="margin-top:24px">
    <div class="card"><div class="ico">1️⃣</div><h3>Portal</h3><p class="muted small">Start at an online cashback portal before you click through to the store.</p></div>
    <div class="card"><div class="ico">2️⃣</div><h3>Coupon</h3><p class="muted small">Apply a store coupon or promo code (check portal terms allow it).</p></div>
    <div class="card"><div class="ico">3️⃣</div><h3>Card</h3><p class="muted small">Pay with a cashback or rewards credit card you pay off in full each month.</p></div>
    <div class="card"><div class="ico">4️⃣</div><h3>Receipt</h3><p class="muted small">Scan your receipt in a receipt-rewards app for bonus points.</p></div>
  </div>
  <div class="center" style="margin-top:24px"><a class="btn btn-primary" href="guides/cashback-stacking.html">Read the full stacking guide →</a></div>
</div></section>
{ad("inContent")}
{newsletter_band(title="Never miss a cashback spike", sub="We send limited-time cashback boosts and bank bonus alerts the moment they go live.")}
""", active="cashback.html", scripts='<script src="assets/js/calc.js" defer></script>')

# ---------------------------------------------------------------- TOOLS
tools_faq, tools_faq_ld = faq([
    ("Are these calculators accurate?", "They use standard financial formulas (amortization, compound interest) and give reliable estimates. Real results depend on taxes, fees and rates you're offered."),
    ("Do you store what I type?", "No. All calculations run in your browser. Nothing you enter into a calculator is sent to us."),
    ("Can I embed a calculator on my site?", "Yes — contact us through the Advertise & Partner page for a free embed with attribution."),
])
PAGES["tools.html"] = page("tools.html", "10 Free Money Calculators — Side Hustle, Debt, Savings, Loans",
  "Free, private money calculators: side-hustle profit, how fast to reach $X, gig driver profit, cashback savings, debt payoff, compound growth, 50/30/20, loan payment, salary and emergency fund.",
  page_hero("Free tools", "Money calculators that answer “is it worth it?”", "Ten fast, private calculators. Results update as you type — nothing is sent to our servers.", ["Tools"]) + f"""
<section class="section" style="padding-top:24px"><div class="container"><div id="calc-app"></div></div></section>
{ad("inContent")}
<section class="section alt"><div class="container" style="max-width:860px"><h2>Calculator FAQ</h2>{tools_faq}</div></section>
{newsletter_band()}
""", active="tools.html", extra_ld=tools_faq_ld, scripts='<script src="assets/js/calc.js" defer></script>')

# ---------------------------------------------------------------- VIDEOS
PAGES["videos.html"] = page("videos.html", "Money Video Hub — Side Hustles, Budgeting & Saving",
  "Curated videos on side hustles, budgeting, compound interest and saving from trusted finance educators.",
  page_hero("Video hub", "Learn money skills in minutes", "Hand-picked videos from trusted educators. Tap to play — videos load only when you click, so the page stays fast.", ["Videos"]) + f"""
<section class="section" style="padding-top:24px"><div class="container"><div class="grid g3" id="video-grid"></div>
<p class="small muted" style="margin-top:18px">Videos are embedded from YouTube and belong to their respective creators. Inclusion is not an endorsement by or of Snap.Cash. Creators: want to be featured? <a href="advertise.html#partner">Partner with us</a>.</p></div></section>
{ad("inContent")}
<section class="section alt"><div class="container center"><span class="eyebrow">Creators wanted</span><h2>Make videos about money? Get paid to create with us.</h2><p class="muted">We hire freelance video creators and editors for our channel.</p><a class="btn btn-primary" href="careers.html">See open roles</a></div></section>
{newsletter_band()}
""", active="videos.html")

# ---------------------------------------------------------------- GET MATCHED (dedicated lead gen)
gm_faq, gm_faq_ld = faq([
    ("Does this affect my credit score?", "No. The Cash Finder never runs a credit check."),
    ("Will you sell my information?", "Never. We only share your details with a specific partner if you tick the optional partner box — and you can withdraw consent any time."),
    ("What happens after I submit?", "You'll see your top five methods instantly, and we'll email your full personalized plan plus the Snap.Cash Daily (unsubscribe anytime)."),
    ("Is it really free?", "Yes. We're paid by advertisers and partners, not by you."),
])
PAGES["get-matched.html"] = page("get-matched.html", "Get Your Free Personalized Cash Plan in 2 Minutes",
  "Answer 5 quick questions and get your top 5 fastest legit ways to earn, save or crush debt — free, private, no credit check.",
  f"""
<section class="hero"><div class="container hero-grid">
  <div><span class="eyebrow">Free · 2 minutes · No credit check</span>
    <h1>Your personal <span class="hl">cash plan</span>, built in 2 minutes</h1>
    <p class="lead">Tell us your goal, timeline and what you've got. We'll rank the fastest legit ways to get there — and email you the full plan.</p>
    <ul class="list-check"><li>Ranked by speed, pay and start-up cost</li><li>Only vetted, legit methods</li><li>Covers earning, saving, debt payoff and borrowing options</li><li>Your data is never sold</li></ul>
    <div class="badges"><span>🔒 Encrypted (HTTPS)</span><span>🚫 No spam</span><span>✉️ Unsubscribe anytime</span></div>
  </div>
  <div>{quiz(heading="Let's build your cash plan")}</div>
</div></section>
<section class="section alt"><div class="container"><div class="grid g3">
  <div class="card"><div class="ico">🎯</div><h3>Matched, not generic</h3><p class="muted">Your answers weight each method by speed, tools and goal size.</p></div>
  <div class="card"><div class="ico">📬</div><h3>Full plan by email</h3><p class="muted">Step-by-step next actions, the calculators to use and the guides to read.</p></div>
  <div class="card"><div class="ico">🔔</div><h3>Optional bonus alerts</h3><p class="muted">Opt in to hear about limited-time sign-up bonuses and cashback spikes.</p></div>
</div></div></section>
<section class="section"><div class="container two-col">
  <div><span class="eyebrow">For businesses</span><h2>Want qualified leads from motivated earners &amp; savers?</h2><p class="muted">Banks, fintechs, gig platforms, insurers, course creators and cashback apps: we run opt-in, consent-first lead programs and sponsored placements.</p><a class="btn btn-primary" href="advertise.html#partner">Become a lead partner →</a></div>
  <div style="max-width:860px"><h3>FAQ</h3>{gm_faq}</div>
</div></section>
""", active="", extra_ld=gm_faq_ld, show_disclosure=True)
