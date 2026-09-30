/* Snap.Cash — core interactions. Vanilla JS, no build step. */
(function(){
  "use strict";
  var C = window.SNAP_CONFIG || {}, D = window.SNAP_DATA || {}, B = document.body.getAttribute("data-base") || "";
  var $ = function(s,r){return (r||document).querySelector(s)}, $$ = function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  var store = {get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
  var sstore = {get:function(k){try{return sessionStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{sessionStorage.setItem(k,v)}catch(e){}}};
  function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
  function toast(msg){var t=$("#toast");if(!t)return;t.textContent=msg;t.style.display="block";clearTimeout(t._h);t._h=setTimeout(function(){t.style.display="none"},3200)}
  window.snapToast = toast;

  /* ---------- theme ---------- */
  var saved = store.get("sc-theme"); if(saved) document.documentElement.setAttribute("data-theme",saved);
  $$("[data-theme-toggle]").forEach(function(b){b.addEventListener("click",function(){
    var cur=document.documentElement.getAttribute("data-theme")||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");
    var nx=cur==="dark"?"light":"dark";document.documentElement.setAttribute("data-theme",nx);store.set("sc-theme",nx)})});

  /* ---------- mobile menu ---------- */
  var mt=$(".menu-toggle"), mm=$(".mobile-menu");
  if(mt&&mm) mt.addEventListener("click",function(){var o=mm.classList.toggle("open");mt.setAttribute("aria-expanded",o)});

  /* ---------- misc ---------- */
  $$("[data-year]").forEach(function(e){e.textContent=new Date().getFullYear()});
  $$("[data-inquiry]").forEach(function(a){a.href=C.inquiryUrl||"https://web.works/contact"});
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.12}) : null;
  $$(".reveal").forEach(function(e){io?io.observe(e):e.classList.add("in")});

  /* rotating hero word */
  $$("[data-rotate]").forEach(function(el){var w=el.getAttribute("data-rotate").split("|"),i=0;setInterval(function(){i=(i+1)%w.length;el.textContent=w[i]},2200)});

  /* sticky mobile CTA */
  var sc=$(".sticky-cta"); if(sc){window.addEventListener("scroll",function(){sc.classList.toggle("show",window.scrollY>600)},{passive:true})}

  /* ---------- cookie consent + ads + analytics ---------- */
  var consent=store.get("sc-consent"), ck=$(".cookie");
  function loadThirdParty(){
    if(C.ga4 && !window._ga4){window._ga4=1;var g=document.createElement("script");g.async=1;g.src="https://www.googletagmanager.com/gtag/js?id="+C.ga4;document.head.appendChild(g);
      window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag("js",new Date());gtag("config",C.ga4)}
    if(C.adsenseClient && /^ca-pub-\d+$/.test(C.adsenseClient) && !window._ads){window._ads=1;
      var s=document.createElement("script");s.async=1;s.crossOrigin="anonymous";s.src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client="+C.adsenseClient;document.head.appendChild(s);
      $$(".ad-slot").forEach(function(slot){var type=slot.getAttribute("data-ad")||"inContent";slot.classList.add("filled");
        slot.innerHTML='<ins class="adsbygoogle" style="display:block" data-ad-client="'+C.adsenseClient+'"'+((C.adSlots&&C.adSlots[type])?' data-ad-slot="'+C.adSlots[type]+'"':'')+' data-ad-format="auto" data-full-width-responsive="true"></ins>';
        try{(window.adsbygoogle=window.adsbygoogle||[]).push({})}catch(e){}});
    }
  }
  if(!consent && ck) ck.classList.add("show"); else if(consent==="all") loadThirdParty();
  $$("[data-consent]").forEach(function(b){b.addEventListener("click",function(){var v=b.getAttribute("data-consent");store.set("sc-consent",v);ck&&ck.classList.remove("show");if(v==="all")loadThirdParty()})});

  /* ---------- lite YouTube ---------- */
  function mountVideo(el){
    var id=el.getAttribute("data-yt"), t=el.getAttribute("data-title")||"Video";
    el.innerHTML='<img loading="lazy" alt="'+esc(t)+'" src="https://i.ytimg.com/vi/'+id+'/hqdefault.jpg"><span class="play" aria-hidden="true">▶</span>';
    el.setAttribute("role","button");el.setAttribute("tabindex","0");el.setAttribute("aria-label","Play: "+t);
    function play(){el.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0" title="'+esc(t)+'" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'}
    el.addEventListener("click",play);el.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();play()}});
  }
  var vg=$("#video-grid");
  if(vg && D.videos){var limit=+(vg.getAttribute("data-limit")||99);
    vg.innerHTML=D.videos.slice(0,limit).map(function(v){return '<article class="card reveal in" data-tags="'+esc(v.cat)+'"><div class="video" data-yt="'+esc(v.id)+'" data-title="'+esc(v.t)+'"></div><h3 style="margin-top:12px;font-size:1rem">'+esc(v.t)+'</h3><p class="small muted" style="margin:0">'+esc(v.by)+' · <span class="tag green">'+esc(v.cat)+'</span> · <a href="https://www.youtube.com/watch?v='+esc(v.id)+'" target="_blank" rel="noopener">Watch on YouTube</a></p></article>'}).join("")}
  $$("[data-yt]").forEach(mountVideo);

  /* ---------- hustle directory ---------- */
  var hg=$("#hustle-grid");
  function renderHustles(list){
    if(!hg)return; var limit=+(hg.getAttribute("data-limit")||999);
    hg.innerHTML=list.slice(0,limit).map(function(h){return '<article class="card"><div class="ico">'+h.e+'</div><h3>'+esc(h.n)+'</h3><div><span class="tag green">'+esc(h.pay)+'</span><span class="tag">Start: '+esc(h.start)+'</span><span class="tag gold">'+({today:"⚡ Cash today",week:"This week",month:"This month"})[h.speed]+'</span></div><p class="muted small" style="margin-top:10px">'+esc(h.d)+'</p><a class="btn btn-ghost btn-sm" href="'+B+'get-matched.html?goal=earn&method='+encodeURIComponent(h.n)+'">Get a personalized plan →</a></article>'}).join("")||'<p class="muted">No matches — try another filter.</p>';
    var cnt=$("#hustle-count"); if(cnt) cnt.textContent=list.length;
  }
  if(hg && D.hustles){
    var state={speed:"all",need:"all",q:""};
    function apply(){renderHustles(D.hustles.filter(function(h){
      return (state.speed==="all"||h.speed===state.speed)&&(state.need==="all"||h.needs.indexOf(state.need)>-1)&&(!state.q||(h.n+" "+h.d+" "+h.c).toLowerCase().indexOf(state.q)>-1)}))}
    $$("[data-f-speed]").forEach(function(b){b.addEventListener("click",function(){$$("[data-f-speed]").forEach(function(x){x.classList.remove("active")});b.classList.add("active");state.speed=b.getAttribute("data-f-speed");apply()})});
    $$("[data-f-need]").forEach(function(b){b.addEventListener("click",function(){$$("[data-f-need]").forEach(function(x){x.classList.remove("active")});b.classList.add("active");state.need=b.getAttribute("data-f-need");apply()})});
    var hs=$("#hustle-search"); if(hs) hs.addEventListener("input",function(){state.q=hs.value.trim().toLowerCase();apply()});
    apply();
  }

  /* ---------- apps table ---------- */
  var at=$("#apps-grid");
  if(at && D.apps){at.innerHTML=D.apps.map(function(a){return '<article class="card offer"><div class="logo-badge" style="background:'+a.color+'">'+esc(a.n.charAt(0))+'</div><div><h3 style="margin:0">'+esc(a.n)+'</h3><div class="small muted">'+esc(a.t)+'</div><ul><li>Minimum cash-out: <b>'+esc(a.min)+'</b></li><li>Payout: '+esc(a.how)+'</li><li>Best for: '+esc(a.best)+'</li></ul></div><div><a class="btn btn-primary btn-sm" href="'+B+'get-matched.html?goal=save&app='+encodeURIComponent(a.n)+'">Get stacking plan</a></div></article>'}).join("")}

  /* ---------- countdowns ---------- */
  $$("[data-countdown]").forEach(function(el){
    var end=new Date(el.getAttribute("data-countdown")).getTime();
    function tick(){var s=Math.max(0,Math.floor((end-Date.now())/1000));var d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),x=s%60;
      el.innerHTML=[[d,"days"],[h,"hrs"],[m,"min"],[x,"sec"]].map(function(p){return '<div><b>'+p[0]+'</b><small>'+p[1]+'</small></div>'}).join("")}
    tick();setInterval(tick,1000)});

  /* ---------- referral code for contests ---------- */
  var ref=new URLSearchParams(location.search).get("ref"); if(ref) sstore.set("sc-ref",ref.slice(0,24));
  $$("[data-ref-field]").forEach(function(i){i.value=sstore.get("sc-ref")||""});
  $$("[data-copy]").forEach(function(b){b.addEventListener("click",function(){var t=$(b.getAttribute("data-copy"));if(!t)return;t.select&&t.select();
    (navigator.clipboard?navigator.clipboard.writeText(t.value):Promise.reject()).then(function(){toast("Copied!")},function(){document.execCommand&&document.execCommand("copy");toast("Copied!")})})});

  /* ---------- donation widget ---------- */
  var amt=25;
  $$(".amt").forEach(function(b){b.addEventListener("click",function(){$$(".amt").forEach(function(x){x.classList.remove("sel")});b.classList.add("sel");amt=+b.getAttribute("data-amt");var ca=$("#custom-amt");if(ca)ca.value="";var da=$("#donation-amount");if(da)da.value=amt})});
  var ca=$("#custom-amt"); if(ca) ca.addEventListener("input",function(){$$(".amt").forEach(function(x){x.classList.remove("sel")});amt=+ca.value||0;var da=$("#donation-amount");if(da)da.value=amt});
  $$("[data-pay]").forEach(function(b){var k=b.getAttribute("data-pay"),url=C.donate&&C.donate[k];
    if(url){b.href=url;b.target="_blank";b.rel="noopener"}else{b.href="#pledge";b.addEventListener("click",function(){toast("Use the pledge form — we'll send you a secure payment link.")})}});

  /* ---------- forms (hidden routing) ---------- */
  function route(){ if(C.formAlias) return C.formEndpoint+C.formAlias; try{return C.formEndpoint+atob(C.k).split("").reverse().join("")}catch(e){return ""} }
  function send(form,extra){
    var st=form.querySelector(".form-status"), btn=form.querySelector("[type=submit]");
    var fd=new FormData(form); if(fd.get("_honey")) return Promise.resolve(true);
    var data={}; fd.forEach(function(v,k){ if(k==="_honey")return; data[k]=data[k]?data[k]+", "+v:v });
    Object.keys(extra||{}).forEach(function(k){data[k]=extra[k]});
    data._subject="[Snap.Cash] "+(form.getAttribute("data-form")||"Form")+" submission"; data._template="table"; data._captcha="false";
    data["Page"]=location.href; data["Submitted"]=new Date().toISOString(); if(sstore.get("sc-ref")) data["Referral code"]=sstore.get("sc-ref");
    if(btn){btn.disabled=true;btn._t=btn.textContent;btn.textContent="Sending…"}
    return fetch(route(),{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(data)})
      .then(function(r){return r.json().catch(function(){return {}}).then(function(j){if(!r.ok||j.success==="false")throw new Error(j.message||"Send failed");return j})})
      .then(function(){ if(st){st.className="form-status ok";st.textContent=form.getAttribute("data-success")||"Thanks! We received your submission and will be in touch shortly."}
        form.reset(); if(window.gtag) gtag("event","generate_lead",{form:form.getAttribute("data-form")}); return true })
      .catch(function(){ if(st){st.className="form-status err";st.textContent="Sorry — that didn't go through. Please check your connection and try again."} return false })
      .finally(function(){ if(btn){btn.disabled=false;btn.textContent=btn._t} });
  }
  window.snapSend=send;
  $$("form[data-form]:not([data-quiz])").forEach(function(f){f.addEventListener("submit",function(e){e.preventDefault(); if(!f.checkValidity()){f.reportValidity();return} send(f)})});

  /* ---------- multi-step quiz / lead funnel ---------- */
  $$("form[data-quiz]").forEach(function(form){
    var steps=$$(".step",form), bar=$(".progress i",form), i=0, answers={};
    var qs=new URLSearchParams(location.search);
    function show(n){i=Math.max(0,Math.min(n,steps.length-1));steps.forEach(function(s,k){s.classList.toggle("active",k===i)});
      if(bar) bar.style.width=Math.round((i)/(steps.length-1)*100)+"%";
      var sc=$(".step-count",steps[i]); if(sc) sc.textContent="Step "+(i+1)+" of "+steps.length;
      var f=steps[i].querySelector("input:not([type=hidden]),select,textarea"); if(f&&i>0&&window.innerWidth>700) setTimeout(function(){f.focus()},250)}
    $$(".opt",form).forEach(function(o){o.addEventListener("click",function(){
      var step=o.closest(".step"), name=step.getAttribute("data-name"), multi=step.hasAttribute("data-multi");
      if(multi){o.classList.toggle("sel");answers[name]=$$(".opt.sel",step).map(function(x){return x.getAttribute("data-v")}).join(", ")}
      else{$$(".opt",step).forEach(function(x){x.classList.remove("sel")});o.classList.add("sel");answers[name]=o.getAttribute("data-v");
        var branch=o.getAttribute("data-goto"); setTimeout(function(){show(branch?steps.indexOf($('[data-id="'+branch+'"]',form)):i+1)},220)}
    })});
    $$("[data-next]",form).forEach(function(b){b.addEventListener("click",function(){
      var fields=$$("input,select,textarea",steps[i]).filter(function(x){return x.type!=="hidden"}), ok=fields.every(function(x){return x.checkValidity()});
      if(!ok){fields.forEach(function(x){x.reportValidity()});return}
      var step=steps[i]; if(step.hasAttribute("data-multi") && !answers[step.getAttribute("data-name")]){toast("Pick at least one option");return}
      show(i+1)})});
    $$("[data-prev]",form).forEach(function(b){b.addEventListener("click",function(){show(i-1)})});
    /* preselect from URL (?goal=earn) */
    var g=qs.get("goal"); if(g){var o=$('.step[data-name="goal"] .opt[data-v="'+g+'"]',form); if(o) o.click()}
    if(qs.get("method")) answers["Interested method"]=qs.get("method"); if(qs.get("app")) answers["Interested app"]=qs.get("app");
    form.addEventListener("submit",function(e){e.preventDefault(); if(!form.checkValidity()){form.reportValidity();return}
      var extra={}; Object.keys(answers).forEach(function(k){extra["Quiz: "+k]=answers[k]});
      send(form,extra).then(function(ok){ if(!ok) return; var r=$(".quiz-result",form.parentNode)||$(".quiz-result");
        if(r){r.hidden=false; r.innerHTML=buildResult(answers); r.scrollIntoView({behavior:"smooth",block:"start"})} form.hidden=true });
    });
    show(0);
  });
  function buildResult(a){
    var need=(a.assets||"").toLowerCase(), speed=a.speed||"", list=(D.hustles||[]).slice();
    list.forEach(function(h){var s=0;h.needs.forEach(function(n){if(need.indexOf(n)>-1)s+=2});
      if(/today/i.test(speed)&&h.speed==="today")s+=3; if(/week/i.test(speed)&&h.speed!=="month")s+=2; if(/month/i.test(speed))s+=1; h._s=s});
    list.sort(function(x,y){return y._s-x._s});
    return '<div class="panel"><span class="eyebrow">Your Snap.Cash plan</span><h2>Your top 5 fastest cash moves</h2><p class="muted">Based on your answers. Your full personalized plan is on its way to your inbox.</p><ol class="result-list">'+
      list.slice(0,5).map(function(h){return '<li><b>'+h.e+' '+esc(h.n)+'</b> — '+esc(h.pay)+'. '+esc(h.d)+'</li>'}).join("")+
      '</ol><div class="hero-cta"><a class="btn btn-primary" href="'+B+'tools.html">Run the numbers →</a><a class="btn btn-ghost" href="'+B+'make-money.html">Browse all ways to earn</a></div><p class="small muted">*Earnings are estimates, not guarantees. See our <a href="'+B+'disclaimer.html">earnings disclaimer</a>.</p></div>';
  }

  /* ---------- exit intent (desktop, once per session) ---------- */
  var ex=$("#exit-modal");
  if(ex && !sstore.get("sc-exit") && window.matchMedia("(min-width:1000px)").matches){
    document.addEventListener("mouseout",function h(e){ if(!e.relatedTarget && e.clientY<8){ ex.classList.add("show"); sstore.set("sc-exit","1"); document.removeEventListener("mouseout",h) } });
  }
  $$("[data-close-modal]").forEach(function(b){b.addEventListener("click",function(){b.closest(".modal").classList.remove("show")})});
  $$(".modal").forEach(function(m){m.addEventListener("click",function(e){if(e.target===m)m.classList.remove("show")})});
  document.addEventListener("keydown",function(e){if(e.key==="Escape")$$(".modal.show").forEach(function(m){m.classList.remove("show")})});
})();
