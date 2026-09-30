/* Snap.Cash content data — add rows to expand the directory, apps table and video hub. */
window.SNAP_DATA = {
  /* speed: today | week | month ; needs: phone, car, computer, home, skills, shopping, outdoor */
  hustles: [
    {n:"Food & grocery delivery",e:"🛵",c:"Gig apps",speed:"today",needs:["car","phone"],pay:"$15–$25/hr*",start:"$0",d:"Deliver meals or groceries on your own schedule with apps like DoorDash, Instacart or Uber Eats. Many offer instant or same-day cash-out."},
    {n:"Rideshare driving",e:"🚗",c:"Gig apps",speed:"week",needs:["car","phone"],pay:"$18–$30/hr*",start:"$0",d:"Drive with Uber or Lyft. Background check takes a few days; instant pay-out features are available on most platforms."},
    {n:"Sell unused stuff",e:"📦",c:"Sell",speed:"today",needs:["phone"],pay:"$50–$500 one-off",start:"$0",d:"List electronics, clothes, furniture and collectibles on Facebook Marketplace, eBay, Poshmark or local groups. Fastest legit cash for most people."},
    {n:"Sell unused gift cards",e:"🎁",c:"Sell",speed:"today",needs:["phone"],pay:"70–92% of face value",start:"$0",d:"Exchange unwanted gift cards for cash through reputable gift card exchange marketplaces."},
    {n:"Paid online surveys",e:"📝",c:"Online",speed:"today",needs:["phone","computer"],pay:"$1–$5/hr*",start:"$0",d:"Low pay but zero skill barrier. Best used in idle minutes. Cash-out thresholds often start around $5."},
    {n:"Paid research studies",e:"🔬",c:"Online",speed:"week",needs:["computer"],pay:"$8–$20/hr*",start:"$0",d:"Academic and AI-training studies (e.g. Prolific, User Interviews) pay far better than surveys and are consistently legit."},
    {n:"Website & app testing",e:"🧪",c:"Online",speed:"week",needs:["computer","phone"],pay:"$10–$60/test*",start:"$0",d:"Record your screen and voice while you try a website or app, then share honest feedback (e.g. UserTesting, Userlytics)."},
    {n:"Freelancing",e:"💻",c:"Skills",speed:"week",needs:["computer","skills"],pay:"$20–$100+/hr*",start:"$0",d:"Writing, design, video editing, coding, virtual assistance — sell your skills on Upwork, Fiverr or direct to clients."},
    {n:"AI data training / annotation",e:"🤖",c:"Online",speed:"week",needs:["computer","skills"],pay:"$15–$40/hr*",start:"$0",d:"Rate AI responses, label data or write expert prompts. Domain experts (coding, nursing, law, math) earn the higher end."},
    {n:"Online tutoring",e:"🎓",c:"Skills",speed:"week",needs:["computer","skills"],pay:"$20–$60/hr*",start:"$0",d:"Tutor school subjects, test prep or languages on tutoring marketplaces or privately."},
    {n:"Pet sitting & dog walking",e:"🐶",c:"Local",speed:"week",needs:["phone","outdoor"],pay:"$15–$30/visit*",start:"$0",d:"Rover and Wag connect you to pet owners nearby. Great ratings snowball into steady repeat bookings."},
    {n:"Task & handyman gigs",e:"🧰",c:"Local",speed:"week",needs:["phone","outdoor","skills"],pay:"$25–$60/hr*",start:"$0–$100",d:"Furniture assembly, mounting TVs, moving help, yard work — list yourself on TaskRabbit or local boards."},
    {n:"Rent out a room or space",e:"🏠",c:"Assets",speed:"month",needs:["home"],pay:"$300–$1,500/mo*",start:"$0–$300",d:"Rent a spare room, parking spot or storage space. Check local rules and your lease first."},
    {n:"Rent out your car",e:"🔑",c:"Assets",speed:"month",needs:["car"],pay:"$300–$800/mo*",start:"$0",d:"Peer-to-peer car sharing (e.g. Turo, Getaround) turns idle car days into income."},
    {n:"Cashback & rewards apps",e:"💸",c:"Save",speed:"today",needs:["shopping","phone"],pay:"1–10% back*",start:"$0",d:"Get paid for purchases you already make with apps like Rakuten, Ibotta and Fetch. Stack them for bigger returns."},
    {n:"Bank account sign-up bonuses",e:"🏦",c:"Save",speed:"month",needs:["phone"],pay:"$100–$500 per bonus*",start:"Direct deposit",d:"Banks pay new customers for opening accounts and setting up direct deposit. Read the terms carefully."},
    {n:"Mystery shopping",e:"🕵️",c:"Local",speed:"week",needs:["phone","outdoor"],pay:"$10–$50/visit*",start:"$0",d:"Evaluate stores and restaurants. Only use established companies — never pay to join."},
    {n:"Content creation (short video)",e:"🎬",c:"Skills",speed:"month",needs:["phone","skills"],pay:"Varies widely",start:"$0",d:"Build an audience on YouTube, TikTok or Instagram and monetize via ads, sponsorships and affiliate links."},
    {n:"Print-on-demand & digital products",e:"🖨️",c:"Online",speed:"month",needs:["computer","skills"],pay:"Varies widely",start:"$0–$50",d:"Sell designs, templates or printables on Etsy or your own store with zero inventory."},
    {n:"Plasma donation",e:"🩸",c:"Local",speed:"today",needs:["outdoor"],pay:"$30–$100/visit*",start:"$0",d:"Many centers pay new donors bonus rates. Eligibility and health screening apply; follow medical guidance."},
    {n:"Babysitting & senior care",e:"🧸",c:"Local",speed:"week",needs:["phone","skills"],pay:"$18–$30/hr*",start:"$0",d:"Care platforms connect families with vetted sitters and companions."},
    {n:"Flip items (thrift → resale)",e:"🔁",c:"Sell",speed:"week",needs:["car","phone"],pay:"$100–$2,000/mo*",start:"$50–$200",d:"Buy underpriced items at thrift stores and garage sales, resell online at market price."},
    {n:"Micro-tasks",e:"✅",c:"Online",speed:"today",needs:["computer","phone"],pay:"$2–$8/hr*",start:"$0",d:"Tiny paid tasks (tagging, transcribing, receipts). Low pay; good for filling idle time."},
    {n:"Recycle cans, phones & electronics",e:"♻️",c:"Sell",speed:"today",needs:["outdoor"],pay:"$5–$200",start:"$0",d:"Trade in old phones and electronics or return deposit containers for quick cash."}
  ],
  /* Cashback & reward apps — facts are general; confirm current bonuses on each provider's site. */
  apps: [
    {n:"Rakuten",t:"Online shopping cashback",min:"$5.01",how:"PayPal or check",best:"Online retail, travel",color:"#bf0000"},
    {n:"Ibotta",t:"Grocery & in-store rebates",min:"$20",how:"Bank, PayPal, gift cards",best:"Groceries",color:"#e0115f"},
    {n:"Fetch",t:"Receipt scanning points",min:"Gift cards from ~$3",how:"Gift cards",best:"Any receipt",color:"#7b2ff7"},
    {n:"TopCashback",t:"Online shopping cashback",min:"No minimum",how:"Bank, PayPal, gift cards (+bonus)",best:"High cashback rates",color:"#1c6ee8"},
    {n:"Survey Junkie",t:"Paid surveys",min:"$5",how:"PayPal, gift cards",best:"Idle-time earning",color:"#0aa06e"},
    {n:"Prolific",t:"Academic & AI studies",min:"$5 / £5",how:"PayPal",best:"Better-paid online studies",color:"#222f5b"},
    {n:"Upside",t:"Gas & dining cashback",min:"$10",how:"Bank, PayPal, gift cards",best:"Drivers",color:"#1b8a4a"},
    {n:"Honey / browser coupon tools",t:"Auto-apply coupons",min:"Points-based",how:"Gift cards",best:"Checkout discounts",color:"#f26c21"}
  ],
  /* Video hub — YouTube video IDs (educational, embeddable). Replace/extend freely. */
  videos: [
    {id:"WgVPgNFgrAo",t:"Compound Interest Explained",by:"NerdWallet",cat:"Save & grow"},
    {id:"Rm6UdfRs3gw",t:"Compound interest introduction",by:"Khan Academy",cat:"Save & grow"},
    {id:"wf91rEGw88Q",t:"Compound Interest Explained",by:"Investopedia",cat:"Save & grow"},
    {id:"_ot0W2bQXbU",t:"How to Budget Money the Easy Way — 50/30/20",by:"YouTube creator",cat:"Budgeting"},
    {id:"b9iwISYBI-g",t:"How to Budget Smarter: The 50/30/20 Rule",by:"YouTube creator",cat:"Budgeting"},
    {id:"f9Vx2zvCjIQ",t:"13 Side Hustles That Actually Make Money",by:"YouTube creator",cat:"Side hustles"},
    {id:"XfVWYSoxiv8",t:"The 5 Best Side Hustles",by:"YouTube creator",cat:"Side hustles"},
    {id:"p3e5H59ra_g",t:"Side Hustles That Pay Daily for Beginners",by:"YouTube creator",cat:"Side hustles"},
    {id:"SiBDyxz5UpU",t:"Easiest Way to Start a Side Hustle",by:"YouTube creator",cat:"Side hustles"}
  ]
};
