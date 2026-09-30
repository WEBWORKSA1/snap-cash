from layout import page, page_hero, YEAR

PAGES = {}
UPDATED = "September 30, 2026"

PAGES["disclaimer.html"] = page("disclaimer.html", "Disclaimers, Trademark & Copyright Notice",
  "Snap.Cash trademark and copyright notice, affiliate disclosure, earnings disclaimer and not-financial-advice statement.",
  page_hero("Legal", "Disclaimers, trademark &amp; copyright", f"Last updated {UPDATED}.", ["Disclaimers"]) + f"""
<section class="section" style="padding-top:24px"><div class="container article">
<h2 id="trademark">Trademark notice &amp; non-affiliation</h2>
<p>"Snap.Cash" is the name of this independent website and refers to the domain name snap.cash. The name describes a general concept — quick ("snap") money ("cash") — and is presented as <b>Snap.Cash</b> with its own original logo, colours and design.</p>
<p>Snap.Cash is <b>not affiliated with, associated with, authorized by, endorsed by, or in any way officially connected with</b> Snap Inc., Snapchat, Block, Inc., Square, Cash App, or the former "Snapcash" peer-to-peer payment feature offered by Snap Inc. and Square (discontinued in 2018). "Snapchat," "Snap," "Cash App," "Square" and related names, marks, emblems and images are registered or unregistered trademarks of their respective owners.</p>
<p>Snap.Cash does not offer peer-to-peer payments, money transmission, banking or lending services, and does not use or imitate any third party's trade dress. All other product and company names mentioned on this site (for example, cashback apps, gig platforms and financial institutions) are trademarks™ or registered® trademarks of their respective holders, used for identification and commentary purposes only (nominative fair use). Their mention does not imply any affiliation or endorsement.</p>
<p>If you believe any content on this site infringes your trademark, please use the <a href="contact.html">contact form</a> (topic: "Correction / feedback") and we will review promptly.</p>
<h2 id="copyright">Copyright notice</h2>
<p>© {YEAR} Snap.Cash. All rights reserved. The original text, graphics, logo, calculators, source code and overall design of this website are protected by copyright and other intellectual property laws. You may share links and short quotations with attribution. You may not copy, republish or redistribute substantial portions without written permission.</p>
<p>Third-party videos are embedded via YouTube's official embed player and remain the property of their creators. Third-party trademarks and content remain the property of their owners.</p>
<h3>DMCA / copyright complaints</h3><p>To report content you believe infringes your copyright, send a notice via the <a href="contact.html">contact form</a> including: identification of the work, the URL of the material, your contact details, a good-faith statement, and a statement under penalty of perjury that you are authorized to act. We respond to valid notices promptly.</p>
<h2 id="affiliate">Affiliate &amp; advertiser disclosure</h2>
<p>Snap.Cash may receive compensation when you click links or sign up for products mentioned on this site. This may influence where products appear on a page but never our editorial ratings. Sponsored content is labeled. See <a href="how-we-make-money.html">How we make money</a>.</p>
<h2 id="earnings">Earnings disclaimer</h2>
<p>Pay ranges and earnings examples are estimates based on publicly available information and typical results. They are not guarantees or promises of income. Your results depend on your location, effort, skills, market demand and other factors. Many people earn less than the figures shown.</p>
<h2 id="advice">Not financial, legal or tax advice</h2>
<p>All content, tools and calculators are for general educational purposes only and do not constitute financial, investment, legal or tax advice. Consult a qualified professional before making financial decisions. Calculator results are estimates.</p>
<h2 id="accuracy">Accuracy</h2>
<p>Offers, rates, bonuses and terms change frequently. Always confirm current details on the provider's official website before signing up.</p>
</div></section>""", show_disclosure=False)

PAGES["privacy.html"] = page("privacy.html", "Privacy & Cookie Policy",
  "How Snap.Cash collects, uses and protects your information, including cookies, Google AdSense and your privacy rights.",
  page_hero("Legal", "Privacy &amp; cookie policy", f"Last updated {UPDATED}.", ["Privacy"]) + """
<section class="section" style="padding-top:24px"><div class="container article">
<h2>What we collect</h2><ul><li><b>Information you give us</b> through forms (name, email, optional phone, quiz answers, messages, applications, pledges and contest entries).</li><li><b>Usage data</b> via cookies and similar technologies if you consent (pages viewed, device, approximate location).</li><li><b>Calculator inputs</b> are processed only in your browser and are never sent to us.</li></ul>
<h2>How we use it</h2><ul><li>To send the plan, newsletter or reply you requested.</li><li>To administer contests, donations, job applications and partnership inquiries.</li><li>To improve the site and measure performance.</li><li>To show advertising (with consent where required).</li></ul>
<h2>Sharing</h2><p>We <b>never sell</b> your personal information. Form submissions are delivered to us through a form-processing service (FormSubmit). We share your details with a named partner <b>only</b> if you tick the optional partner-offers box, and you may withdraw consent anytime.</p>
<h2 id="cookies">Cookies &amp; advertising</h2><p>With your consent, we use Google Analytics and Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You may opt out of personalized advertising at <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="noopener" target="_blank">aboutads.info</a>. Choose "Essential only" in our cookie banner to decline non-essential cookies. To change your choice, clear this site's data in your browser.</p>
<h2>Your rights</h2><p>Depending on where you live (e.g. GDPR/UK GDPR, CCPA/CPRA, PIPEDA and Québec Law 25), you may have the right to access, correct, delete or port your data, to object to processing, and to opt out of the "sale" or "sharing" of personal information. <b>Do Not Sell or Share My Personal Information:</b> we do not sell or share personal information for cross-context behavioural advertising without consent; to make a request, use the <a href="contact.html">contact form</a> (topic: Privacy request).</p>
<h2>Email &amp; SMS</h2><p>Every email includes an unsubscribe link (CAN-SPAM / CASL). SMS alerts are sent only with separate express consent; reply STOP to cancel.</p>
<h2>Children</h2><p>This site is not directed to children under 16 and we do not knowingly collect their data.</p>
<h2>Retention &amp; security</h2><p>We keep data only as long as needed for the purpose collected. The site is served over HTTPS.</p>
<h2>Contact</h2><p>Privacy questions: use the <a href="contact.html">contact form</a>.</p>
</div></section>""", show_disclosure=False)

PAGES["terms.html"] = page("terms.html", "Terms of Use",
  "Terms governing use of the Snap.Cash website, tools and content.",
  page_hero("Legal", "Terms of use", f"Last updated {UPDATED}.", ["Terms"]) + """
<section class="section" style="padding-top:24px"><div class="container article">
<h2>1. Acceptance</h2><p>By using Snap.Cash you agree to these Terms, our <a href="privacy.html">Privacy Policy</a> and <a href="disclaimer.html">Disclaimers</a>.</p>
<h2>2. Educational content only</h2><p>Content and tools are for information only and are not professional advice. You are responsible for your own decisions.</p>
<h2>3. Third-party sites &amp; offers</h2><p>We link to third-party websites and offers we don't control. Their terms and privacy policies apply. We are not responsible for their products, services or content.</p>
<h2>4. User submissions</h2><p>You agree that information you submit is accurate and that you have the right to submit it. You grant us a licence to use contest entries, testimonials and guest content you submit for the purposes described when you submitted them.</p>
<h2>5. Prohibited use</h2><p>No scraping at scale, automated form submissions, fraudulent contest entries, attempts to disrupt the site, or unlawful use.</p>
<h2>6. Intellectual property</h2><p>The site's original content, design and code are owned by Snap.Cash and protected by copyright. See our <a href="disclaimer.html#copyright">copyright notice</a>.</p>
<h2>7. Donations</h2><p>Contributions are voluntary, non-refundable except where required by law, and not tax-deductible.</p>
<h2>8. Disclaimer of warranties &amp; limitation of liability</h2><p>The site is provided "as is" without warranties of any kind. To the maximum extent permitted by law, Snap.Cash is not liable for any indirect, incidental or consequential damages arising from your use of the site.</p>
<h2>9. Changes</h2><p>We may update these Terms. Continued use means you accept the updated Terms.</p>
<h2>10. Contact</h2><p>Questions? Use the <a href="contact.html">contact form</a>.</p>
</div></section>""", show_disclosure=False)
