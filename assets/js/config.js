/* =====================================================================
   Snap.Cash — SITE CONFIG (edit this one file to switch things on)
   ===================================================================== */
window.SNAP_CONFIG = {
  siteName: "Snap.Cash",
  siteUrl: "https://snap.cash",

  /* Contact routing key (obfuscated on purpose — do not paste a raw address here). */
  k: "bW9jLmxpYW1nQDFhc2tyb3diZXc=",

  /* Form delivery endpoint (FormSubmit AJAX). After the first submission, FormSubmit sends
     one activation email; confirm it once. You may then replace the routing key with the
     random alias FormSubmit gives you by setting formAlias below (keeps it even more private). */
  formEndpoint: "https://formsubmit.co/ajax/",
  formAlias: "",

  /* Google AdSense — paste your publisher ID (e.g. "ca-pub-1234567890123456") to activate all ad slots. */
  adsenseClient: "",
  adSlots: { header: "", inContent: "", sidebar: "", footer: "" },

  /* Google Analytics 4 — e.g. "G-XXXXXXXXXX" (optional) */
  ga4: "",

  /* Donation / support links — paste your own payment links; empty ones fall back to the pledge form. */
  donate: {
    paypal: "",          // e.g. https://www.paypal.com/donate/?hosted_button_id=XXXX
    buymeacoffee: "",    // e.g. https://www.buymeacoffee.com/yourname
    kofi: "",            // e.g. https://ko-fi.com/yourname
    stripe: "",          // e.g. https://donate.stripe.com/XXXX
    patreon: ""          // e.g. https://www.patreon.com/yourname
  },

  /* Sponsorship / domain inquiry link (shown on top of every page) */
  inquiryUrl: "https://web.works/contact",

  /* Social profiles (optional) */
  social: { youtube: "", x: "", instagram: "", tiktok: "", facebook: "", linkedin: "" }
};
