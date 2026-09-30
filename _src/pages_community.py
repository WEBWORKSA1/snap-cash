from layout import page, page_hero, ad, newsletter_band, support_band, faq, INQUIRY

PAGES = {}
HP = '<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">'
STATUS = '<div class="form-status" role="status"></div>'

# ---------------------------------------------------------------- CONTESTS
PAGES["contests.html"] = page("contests.html", "Free Giveaways, Challenges & Prizes",
  "Enter free Snap.Cash giveaways and money challenges. No purchase necessary. Earn bonus entries by referring friends.",
  page_hero("Contests & prizes", "Free to enter. Real prizes. Zero catch.", "Enter our current giveaway, join a money challenge, and earn bonus entries for every friend you refer. No purchase necessary.", ["Contests"]) + f"""
<section class="section" style="padding-top:24px"><div class="container two-col">
  <div class="panel">
    <span class="eyebrow">🏆 Featured giveaway</span><h2>The $500 Snap Start Giveaway</h2>
    <p class="muted">One winner receives a $500 prize (cash via PayPal or a gift card of equivalent value). Entry period ends Dec 31, 2026, 11:59 p.m. ET.</p>
    <div class="countdown" data-countdown="2026-12-31T23:59:59-05:00" style="margin:16px 0"></div>
    <form class="form" data-form="Giveaway entry" data-success="You're entered! 🎉 Share your referral link below to earn bonus entries.">
      {HP}<input type="hidden" name="Contest" value="$500 Snap Start Giveaway">
      <div class="form-row"><div><label for="c-name">Full name</label><input id="c-name" name="Full name" required autocomplete="name"></div>
      <div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required autocomplete="email"></div></div>
      <div class="form-row"><div><label for="c-country">Country / state or province</label><input id="c-country" name="Location" required placeholder="e.g. Texas, USA"></div>
      <div><label for="c-ref">Referral code <span class="muted">(if a friend sent you)</span></label><input id="c-ref" name="Referred by" data-ref-field></div></div>
      <div><label for="c-q">Skill-testing question (required for Canadian entrants): (12 × 3) + 4 − 10 = ?</label><input id="c-q" name="Skill question answer" inputmode="numeric"></div>
      <label class="check"><input type="checkbox" name="Age & rules" value="confirmed" required> I'm 18+ (or the age of majority where I live) and agree to the <a href="contest-rules.html">Official Rules</a>.</label>
      <label class="check"><input type="checkbox" name="Newsletter opt-in" value="yes"> Optional: also send me the Snap.Cash Daily.</label>
      <button class="btn btn-accent btn-lg btn-block" type="submit">Enter free →</button>{STATUS}
      <p class="form-note">NO PURCHASE NECESSARY. A purchase will not increase your chances of winning. Void where prohibited. See <a href="contest-rules.html">Official Rules</a>.</p>
    </form>
  </div>
  <aside><div class="sticky-side">
    <div class="card"><h3>🔗 Earn bonus entries</h3><p class="muted small">Each friend who enters with your code earns you +3 bonus entries (max 30).</p>
      <label for="my-code">Your referral link</label><input id="my-code" readonly value="">
      <button class="btn btn-primary btn-sm" style="margin-top:10px" data-copy="#my-code">Copy link</button></div>
    <div class="card" style="margin-top:16px"><h3>🗓️ Upcoming</h3><ul class="feed">
      <li><span class="avatar">💡</span><div><b>Side Hustle Story Contest</b><br><span class="small muted">Share how you earned your first $100. Judged. Prize pool funded by sponsors.</span></div></li>
      <li><span class="avatar">🧾</span><div><b>30-Day No-Spend Challenge</b><br><span class="small muted">Community challenge with weekly random prizes.</span></div></li>
      <li><span class="avatar">🎥</span><div><b>Creator Challenge</b><br><span class="small muted">Best 60-sec money tip video wins a paid creator contract.</span></div></li></ul></div>
  </div></aside>
</div></section>
{ad("inContent")}
<section class="section alt"><div class="container two-col">
  <div><span class="eyebrow">Sponsors</span><h2>Sponsor a prize, reach thousands of engaged entrants</h2><p class="muted">Brands can fund prizes and receive logo placement, newsletter features and opt-in entrant leads (with explicit consent).</p><a class="btn btn-primary" href="advertise.html#sponsor">Sponsor a giveaway</a></div>
  <div class="panel"><h3>Suggest a contest or prize</h3>
    <form class="form" data-form="Contest idea">{HP}<input name="Name" placeholder="Your name" required aria-label="Name"><input type="email" name="email" placeholder="Email" required aria-label="Email"><textarea name="Idea" placeholder="Your contest or challenge idea" required aria-label="Idea"></textarea><button class="btn btn-primary" type="submit">Send idea</button>{STATUS}</form></div>
</div></section>
<script>(function(){{var c='SC'+Math.random().toString(36).slice(2,8).toUpperCase();try{{c=localStorage.getItem('sc-mycode')||c;localStorage.setItem('sc-mycode',c)}}catch(e){{}}var i=document.getElementById('my-code');if(i)i.value=location.origin+location.pathname+'?ref='+c}})();</script>
""", active="contests.html")

PAGES["contest-rules.html"] = page("contest-rules.html", "Official Contest Rules",
  "Official rules for Snap.Cash giveaways and contests. No purchase necessary.",
  page_hero("Legal", "Official Rules — $500 Snap Start Giveaway", "NO PURCHASE NECESSARY TO ENTER OR WIN. A PURCHASE OR PAYMENT WILL NOT INCREASE YOUR CHANCES OF WINNING. VOID WHERE PROHIBITED.", ["Contest rules"]) + """
<section class="section"><div class="container article">
<h2>1. Sponsor</h2><p>The giveaway is sponsored by Snap.Cash ("Sponsor"). Contact the Sponsor via the <a href="contact.html">contact form</a>.</p>
<h2>2. Eligibility</h2><p>Open to legal residents of the 50 United States and D.C., Canada, the United Kingdom and Australia who are 18 years of age or older (or the age of majority in their jurisdiction) at the time of entry. Employees, contractors and immediate family members of the Sponsor and its partners are not eligible. Void in Quebec and where prohibited or restricted by law.</p>
<h2>3. Entry period</h2><p>The giveaway begins on October 1, 2026 at 12:00 a.m. ET and ends on December 31, 2026 at 11:59 p.m. ET ("Entry Period"). The Sponsor's computer is the official timekeeping device.</p>
<h2>4. How to enter</h2><p>Complete the entry form on the Contests page. Limit one (1) base entry per person and email address. Bonus entries: receive three (3) bonus entries for each eligible person who enters using your referral link, up to thirty (30) bonus entries. Automated, scripted or bulk entries are void.</p>
<h2>5. Prize</h2><p>One (1) Grand Prize: $500 USD paid via PayPal or a gift card of equivalent value, at the winner's choice. Approximate Retail Value (ARV): $500. Prizes are non-transferable; no substitution except by Sponsor if a prize becomes unavailable. Winners are responsible for all applicable taxes.</p>
<h2>6. Winner selection &amp; odds</h2><p>One winner will be selected by random drawing from all eligible entries within seven (7) days after the Entry Period ends. Odds of winning depend on the number of eligible entries received. Canadian residents must correctly answer a time-limited mathematical skill-testing question to be declared a winner.</p>
<h2>7. Notification</h2><p>The winner will be notified by email and must respond within seven (7) days, and may be required to sign an affidavit of eligibility and release. If a winner cannot be contacted or is ineligible, an alternate winner may be drawn.</p>
<h2>8. General conditions</h2><p>By entering, participants agree to these Official Rules and the Sponsor's decisions, which are final. The Sponsor may cancel, modify or suspend the giveaway if fraud, technical failure or any other factor impairs its integrity. This promotion is in no way sponsored, endorsed, administered by or associated with Facebook, Instagram, TikTok, X, YouTube or any other social platform.</p>
<h2>9. Privacy</h2><p>Personal information is used to administer the giveaway and as described in our <a href="privacy.html">Privacy Policy</a>. Newsletter sign-up is optional and not required to enter.</p>
<h2>10. Winner's list</h2><p>For the winner's name (available 30 days after the drawing), submit a request through the <a href="contact.html">contact form</a>.</p>
<p class="small muted">Operators: before launching, review these rules with counsel and register/bond where required (e.g. certain U.S. states for prizes over $5,000).</p>
</div></section>""", show_disclosure=False)

# ---------------------------------------------------------------- SUPPORT / DONATE
PAGES["support.html"] = page("support.html", "Support Snap.Cash — Donate, Sponsor & Fund Prizes",
  "Support free money tools and guides. Donate once or monthly to fund operations, promotions, marketing, hiring talent and contest prizes.",
  page_hero("Support us", "Help keep money help free for everyone", "Snap.Cash has no paywalls. Your support funds operations, new tools, promotion &amp; marketing, hiring talented creators, and prizes for our community contests.", ["Support"]) + f"""
<section class="section" style="padding-top:24px"><div class="container two-col">
  <div class="panel" id="pledge">
    <h2>Make a contribution</h2>
    <p class="muted small">Choose an amount, then pay with your preferred method — or submit a pledge and we'll send you a secure payment link.</p>
    <div class="amounts" role="group" aria-label="Amount"><button class="amt" data-amt="5">$5</button><button class="amt" data-amt="10">$10</button><button class="amt sel" data-amt="25">$25</button><button class="amt" data-amt="50">$50</button><button class="amt" data-amt="100">$100</button><button class="amt" data-amt="250">$250</button></div>
    <div style="margin-top:12px"><label for="custom-amt">Custom amount (USD)</label><input id="custom-amt" type="number" min="1" step="1" placeholder="Other amount"></div>
    <div class="hero-cta"><a class="btn btn-primary" data-pay="paypal" href="#pledge">PayPal</a><a class="btn btn-ghost" data-pay="stripe" href="#pledge">Card (Stripe)</a><a class="btn btn-ghost" data-pay="buymeacoffee" href="#pledge">☕ Buy Me a Coffee</a><a class="btn btn-ghost" data-pay="kofi" href="#pledge">Ko-fi</a><a class="btn btn-ghost" data-pay="patreon" href="#pledge">Patreon (monthly)</a></div>
    <hr style="border:0;border-top:1px solid var(--line);margin:8px 0 20px">
    <h3>Pledge form</h3>
    <form class="form" data-form="Donation pledge" data-success="Thank you! We'll email you a secure payment link shortly. ❤">
      {HP}<input type="hidden" id="donation-amount" name="Amount (USD)" value="25">
      <div class="form-row"><div><label for="d-name">Name</label><input id="d-name" name="Name" required autocomplete="name"></div><div><label for="d-email">Email</label><input id="d-email" type="email" name="email" required autocomplete="email"></div></div>
      <div class="form-row"><div><label for="d-freq">Frequency</label><select id="d-freq" name="Frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div>
      <div><label for="d-fund">Direct my support to</label><select id="d-fund" name="Fund"><option>Where it's needed most</option><option>Operations &amp; hosting</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contest prizes</option><option>New free tools</option></select></div></div>
      <div><label for="d-msg">Message <span class="muted">(optional, may be shown publicly)</span></label><textarea id="d-msg" name="Message" style="min-height:80px"></textarea></div>
      <label class="check"><input type="checkbox" name="Show name publicly" value="yes"> Show my first name on the supporters wall</label>
      <button class="btn btn-primary btn-block" type="submit">Pledge my support ❤</button>{STATUS}
      <p class="form-note">Contributions support an independent publication and are not tax-deductible. No goods or services are provided in exchange.</p>
    </form>
  </div>
  <aside><div class="sticky-side">
    <div class="card"><h3>Where your money goes</h3><div class="table-wrap"><table><tr><td>🖥️ Operations &amp; hosting</td><td><b>25%</b></td></tr><tr><td>📣 Promotion &amp; marketing</td><td><b>25%</b></td></tr><tr><td>👩‍💻 Hiring writers &amp; developers</td><td><b>30%</b></td></tr><tr><td>🏆 Contests &amp; prizes</td><td><b>20%</b></td></tr></table></div><p class="small muted">Target allocation. We publish updates as the community grows.</p></div>
    <div class="card" style="margin-top:16px"><h3>Supporter perks</h3><ul class="list-check small"><li>Supporters wall shout-out</li><li>Early access to new tools</li><li>Bonus contest entries (where legally permitted, free alternative entry always available)</li><li>Monthly supporters get a members-only deals digest</li></ul></div>
  </div></aside>
</div></section>
<section class="section alt" id="tiers"><div class="container"><div class="center"><span class="eyebrow">Monthly membership</span><h2>Become a Snap.Cash Insider</h2></div>
  <div class="grid g3" style="margin-top:24px">
    <div class="card tier"><h3>Supporter</h3><div class="price">$3<span class="small muted">/mo</span></div><ul><li>Supporters wall</li><li>Insider newsletter</li></ul><a class="btn btn-ghost btn-block" data-pay="patreon" href="#pledge">Join</a></div>
    <div class="card tier featured"><span class="ribbon">Most popular</span><h3>Insider</h3><div class="price">$9<span class="small muted">/mo</span></div><ul><li>Everything in Supporter</li><li>Early tool access</li><li>Members-only deals digest</li></ul><a class="btn btn-primary btn-block" data-pay="patreon" href="#pledge">Join</a></div>
    <div class="card tier"><h3>Patron</h3><div class="price">$29<span class="small muted">/mo</span></div><ul><li>Everything in Insider</li><li>Name a monthly prize</li><li>Quarterly Q&amp;A invite</li></ul><a class="btn btn-ghost btn-block" data-pay="patreon" href="#pledge">Join</a></div>
  </div></div></section>
<section class="section"><div class="container center"><h2>Are you a business?</h2><p class="muted">Sponsorships unlock logo placement, newsletter features and giveaway partnerships.</p><a class="btn btn-primary" href="advertise.html#sponsor">See sponsorship options</a></div></section>
""", active="support.html")

# ---------------------------------------------------------------- ADVERTISE / PARTNER / SPONSOR
PAGES["advertise.html"] = page("advertise.html", "Advertise, Sponsor & Partner with Snap.Cash",
  "Reach motivated earners and savers with sponsored placements, newsletter features, giveaway sponsorships and consent-based lead-generation partnerships.",
  page_hero("For brands", "Reach people actively looking to earn, save &amp; borrow smarter", "Snap.Cash readers arrive with intent: they want a new income stream, a better account, a cashback app or a way out of debt.", ["Advertise"], extra=f'<div class="hero-cta"><a class="btn btn-primary" href="#inquiry">Start a conversation</a><a class="btn btn-ghost" href="{INQUIRY}" data-inquiry target="_blank" rel="noopener">Acquire / invest in this domain</a></div>') + f"""
<section class="section" style="padding-top:24px" id="sponsor"><div class="container"><div class="grid g4">
  <div class="card"><div class="ico">📌</div><h3>Sponsored placements</h3><p class="muted small">Featured listing in our directory, apps table or guide pages — clearly labeled "Sponsored".</p></div>
  <div class="card"><div class="ico">✉️</div><h3>Newsletter features</h3><p class="muted small">Dedicated or shared slots in the Snap.Cash Daily.</p></div>
  <div class="card"><div class="ico">🏆</div><h3>Giveaway sponsorship</h3><p class="muted small">Fund a prize; get branding, social reach and opt-in entrant leads.</p></div>
  <div class="card" id="partner"><div class="ico">🎯</div><h3>Lead partnerships</h3><p class="muted small">CPL/CPA programs with TCPA/CASL-friendly, explicit opt-in consent.</p></div>
</div></div></section>
<section class="section alt"><div class="container two-col">
  <div><span class="eyebrow">Audience</span><h2>Who reads Snap.Cash</h2><ul class="list-check"><li>Side-hustlers &amp; gig workers looking for new income</li><li>Deal hunters &amp; cashback stackers</li><li>Young professionals building savings &amp; credit</li><li>People comparing debt payoff &amp; borrowing options</li></ul>
    <h3 style="margin-top:24px">Ideal partners</h3><p class="muted">Banks &amp; neobanks · Fintech &amp; budgeting apps · Cashback &amp; rewards apps · Gig &amp; freelance platforms · Insurance · Education &amp; courses · Tax software</p>
    <p class="small muted">We don't accept payday lenders, "get rich quick" schemes, MLMs or anything that fails our editorial review.</p></div>
  <div class="panel" id="inquiry"><h3>Advertising &amp; partnership inquiry</h3>
    <form class="form" data-form="Advertising / partnership inquiry" data-success="Thanks! Our partnerships team will reply within 2 business days.">{HP}
      <div class="form-row"><div><label for="a-name">Your name</label><input id="a-name" name="Name" required autocomplete="name"></div><div><label for="a-co">Company</label><input id="a-co" name="Company" required autocomplete="organization"></div></div>
      <div class="form-row"><div><label for="a-email">Work email</label><input id="a-email" type="email" name="email" required autocomplete="email"></div><div><label for="a-web">Website</label><input id="a-web" type="url" name="Website" placeholder="https://"></div></div>
      <div class="form-row"><div><label for="a-type">Interested in</label><select id="a-type" name="Interest" required><option value="">Select…</option><option>Sponsored placement</option><option>Newsletter sponsorship</option><option>Giveaway / prize sponsorship</option><option>Lead-generation partnership</option><option>Display advertising</option><option>Content / creator partnership</option><option>Domain / website acquisition</option><option>Investment / joint venture</option></select></div>
      <div><label for="a-budget">Monthly budget (USD)</label><select id="a-budget" name="Budget"><option>Under $1,000</option><option>$1,000 – $5,000</option><option>$5,000 – $20,000</option><option>$20,000+</option><option>Performance (CPL/CPA)</option></select></div></div>
      <div><label for="a-msg">Goals &amp; details</label><textarea id="a-msg" name="Message" required></textarea></div>
      <button class="btn btn-primary btn-block" type="submit">Send inquiry</button>{STATUS}</form></div>
</div></section>
""", active="")

# ---------------------------------------------------------------- CAREERS
roles = [("Freelance Personal Finance Writer", "Remote · Contract", "Write clear, well-researched guides on side hustles, cashback and saving."),
         ("SEO & Content Strategist", "Remote · Part-time", "Own keyword strategy, internal linking and content refreshes."),
         ("Short-form Video Creator / Editor", "Remote · Per project", "Turn our guides into 30–90 second videos for YouTube Shorts, TikTok and Reels."),
         ("Front-end Developer (JS)", "Remote · Contract", "Build new interactive calculators and tools."),
         ("Partnerships & Ad Sales", "Remote · Commission", "Bring in sponsors, lead partners and giveaway prize sponsors."),
         ("Community & Contest Manager", "Remote · Part-time", "Run giveaways, challenges and our supporter community.")]
role_html = "".join(f'<article class="card"><h3>{t}</h3><span class="tag green">{m}</span><p class="muted small" style="margin-top:8px">{d}</p><a class="btn btn-ghost btn-sm" href="#apply" onclick="document.getElementById(\'j-role\').value=\'{t}\'">Apply →</a></article>' for t, m, d in roles)
PAGES["careers.html"] = page("careers.html", "Careers & Write for Us — Join Snap.Cash",
  "Join Snap.Cash as a writer, video creator, developer, SEO strategist or partnerships lead. Remote, flexible roles.",
  page_hero("Careers", "Help millions make smarter money moves", "We're a remote-first team hiring talented writers, creators, developers and growth people. Flexible, paid, and meaningful.", ["Careers"]) + f"""
<section class="section" style="padding-top:24px"><div class="container"><div class="grid g3">{role_html}</div></div></section>
<section class="section alt"><div class="container two-col">
  <div><span class="eyebrow">Why Snap.Cash</span><h2>Work that actually helps people</h2><ul class="list-check"><li>100% remote, async-friendly</li><li>Paid per project or retainer</li><li>Bylines and portfolio-building work</li><li>Performance bonuses for top content</li></ul>
    <h3 style="margin-top:20px">Write for us</h3><p class="muted">Have a real story about earning or saving money? Pitch us — we pay for accepted guest articles. Include 2–3 headline ideas and links to your writing.</p></div>
  <div class="panel" id="apply"><h3>Apply or pitch</h3>
    <form class="form" data-form="Careers application" data-success="Thanks for applying! We review every application and reply within 7 days.">{HP}
      <div class="form-row"><div><label for="j-name">Full name</label><input id="j-name" name="Name" required autocomplete="name"></div><div><label for="j-email">Email</label><input id="j-email" type="email" name="email" required autocomplete="email"></div></div>
      <div class="form-row"><div><label for="j-role">Role</label><input id="j-role" name="Role" required list="rolelist" placeholder="Role or 'Guest writer'"><datalist id="rolelist">{"".join(f"<option>{r[0]}</option>" for r in roles)}<option>Guest writer pitch</option></datalist></div>
      <div><label for="j-loc">Location / time zone</label><input id="j-loc" name="Location"></div></div>
      <div><label for="j-link">Portfolio / LinkedIn / GitHub</label><input id="j-link" type="url" name="Portfolio" placeholder="https://" required></div>
      <div><label for="j-msg">Why you? (and pitch ideas, if writing)</label><textarea id="j-msg" name="Message" required></textarea></div>
      <button class="btn btn-primary btn-block" type="submit">Submit application</button>{STATUS}</form></div>
</div></section>
""", active="")

# ---------------------------------------------------------------- CONTACT
PAGES["contact.html"] = page("contact.html", "Contact Snap.Cash",
  "Contact the Snap.Cash team for questions, corrections, partnerships and press.",
  page_hero("Contact", "We'd love to hear from you", "Questions, corrections, partnership ideas or press — send us a note and we'll reply within 2 business days.", ["Contact"]) + f"""
<section class="section" style="padding-top:24px"><div class="container two-col">
  <div class="panel"><form class="form" data-form="Contact" data-success="Message sent! We'll get back to you within 2 business days.">{HP}
    <div class="form-row"><div><label for="ct-name">Name</label><input id="ct-name" name="Name" required autocomplete="name"></div><div><label for="ct-email">Email</label><input id="ct-email" type="email" name="email" required autocomplete="email"></div></div>
    <div><label for="ct-topic">Topic</label><select id="ct-topic" name="Topic"><option>General question</option><option>Correction / feedback</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Press / media</option><option>Contest question</option><option>Privacy request</option><option>Domain / website inquiry</option></select></div>
    <div><label for="ct-msg">Message</label><textarea id="ct-msg" name="Message" required></textarea></div>
    <label class="check"><input type="checkbox" name="Privacy consent" value="yes" required> I agree that Snap.Cash may use my details to reply to this message.</label>
    <button class="btn btn-primary btn-block" type="submit">Send message</button>{STATUS}</form></div>
  <aside><div class="card"><h3>Other ways to reach us</h3><ul class="list-check"><li><a href="advertise.html#inquiry">Advertising &amp; partnerships</a></li><li><a href="careers.html#apply">Careers &amp; guest writing</a></li><li><a href="support.html#pledge">Donations &amp; support</a></li><li><a href="{INQUIRY}" data-inquiry target="_blank" rel="noopener">Domain / website / sponsorship inquiry</a></li></ul>
    <p class="small muted">We never ask for passwords, bank logins or upfront fees. If someone claiming to be Snap.Cash does, it's a scam.</p></div></aside>
</div></section>""", active="", show_disclosure=False)

# ---------------------------------------------------------------- ABOUT
PAGES["about.html"] = page("about.html", "About Snap.Cash",
  "Snap.Cash is an independent money hub helping people find fast, legit ways to earn, save and find cash.",
  page_hero("About", "Money help that's fast, honest and free", "Snap.Cash exists because the internet is full of “make money fast” hype. We cut through it with vetted methods, transparent math and zero paywalls.", ["About"]) + """
<section class="section" style="padding-top:24px"><div class="container article">
<h2>Our mission</h2><p>Help people find the fastest <em>legitimate</em> path to the cash they need — whether that's $100 by Friday or an extra $1,000 a month — and keep more of it through cashback, smarter saving and lower-cost debt.</p>
<h2>How we rate methods</h2><ul class="list-check"><li><b>Speed to first dollar</b> — how quickly you actually get paid.</li><li><b>Earning potential</b> — realistic, not best-case, pay ranges.</li><li><b>Start-up cost &amp; risk</b> — we flag anything that asks for money upfront.</li><li><b>Legitimacy</b> — company track record, reviews and complaint history.</li><li><b>Experience</b> — cash-out thresholds, payout methods and support.</li></ul>
<h2>Editorial independence</h2><p>Advertisers and partners never pay for positive coverage. Sponsored content is always labeled. Read <a href="how-we-make-money.html">how we make money</a>.</p>
<h2>Independent brand</h2><p>Snap.Cash is not affiliated with Snap Inc., Snapchat, Block, Inc., Cash App or the discontinued Snapcash feature. See our <a href="disclaimer.html">trademark notice</a>.</p>
</div></section>""", show_disclosure=False)

PAGES["how-we-make-money.html"] = page("how-we-make-money.html", "How We Make Money",
  "Transparency on how Snap.Cash is funded: display ads, affiliate commissions, sponsorships, lead partnerships and reader donations.",
  page_hero("Transparency", "How Snap.Cash makes money", "We keep every tool and guide free. Here's exactly how that's funded.", ["How we make money"]) + """
<section class="section" style="padding-top:24px"><div class="container article">
<div class="table-wrap"><table><tr><th>Source</th><th>How it works</th></tr>
<tr><td>Display advertising</td><td>Google AdSense and similar networks show ads. Ads are labeled "Advertisement" and never placed inside forms or calculators.</td></tr>
<tr><td>Affiliate commissions</td><td>Some links pay us a commission if you sign up or buy. It costs you nothing extra.</td></tr>
<tr><td>Sponsorships</td><td>Brands may sponsor placements, newsletter slots or giveaways. Always labeled "Sponsored".</td></tr>
<tr><td>Lead partnerships</td><td>If — and only if — you tick the optional partner box, we may introduce you to a vetted partner who pays us a referral fee.</td></tr>
<tr><td>Reader support</td><td>Donations and memberships fund operations, marketing, hiring and prizes.</td></tr></table></div>
<div class="callout"><b>Our promise:</b> compensation never determines our ratings or which methods we recommend. We rank by speed, pay, cost, legitimacy and user experience.</div>
<p>This disclosure is made in accordance with the U.S. Federal Trade Commission's Guides Concerning the Use of Endorsements and Testimonials in Advertising, and equivalent rules in Canada, the UK and elsewhere.</p>
</div></section>""", show_disclosure=False)
