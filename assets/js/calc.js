/* Snap.Cash calculators — definition-driven. Add a new calculator by adding an object to CALCS. */
(function(){
  "use strict";
  var money=function(v){return (v<0?"-":"")+"$"+Math.abs(v).toLocaleString(undefined,{maximumFractionDigits:0})};
  var money2=function(v){return "$"+v.toLocaleString(undefined,{minimumFractionDigits:2,maximumFractionDigits:2})};
  function amort(P,apr,n){var r=apr/1200;return r?P*r/(1-Math.pow(1+r,-n)):P/n}
  var CALCS=[
    {id:"hustle",name:"Side-hustle earnings",icon:"💼",cta:["Find the best-paying hustle for you","make-money.html"],
     inputs:[["rate","Pay per hour ($)",22],["hours","Hours per week",10],["weeks","Weeks per year",48],["costs","Expenses (% of gross)",15],["tax","Estimated tax rate (%)",20]],
     run:function(v){var g=v.rate*v.hours*v.weeks,c=g*v.costs/100,t=(g-c)*v.tax/100,n=g-c-t;
       return {big:money(n/12)+"/mo",label:"Estimated take-home",rows:[["Gross per year",money(g)],["Expenses",money(c)],["Tax set-aside",money(t)],["Net per year",money(n)],["Net per hour",money2(n/Math.max(1,v.hours*v.weeks))]]}}},
    {id:"goal",name:"How fast can I make $X?",icon:"⚡",cta:["Get your 2-minute cash plan","get-matched.html?goal=earn"],
     inputs:[["goal","Cash goal ($)",1000],["rate","Net earnings per hour ($)",18],["hours","Hours available per week",12]],
     run:function(v){var h=v.goal/Math.max(.01,v.rate),w=h/Math.max(.1,v.hours);
       return {big:(w<1?Math.ceil(w*7)+" days":w.toFixed(1)+" weeks"),label:"Time to reach your goal",rows:[["Total hours needed",h.toFixed(1)],["Per day (7-day week)",(v.hours/7).toFixed(1)+" hrs"],["Hit 50% by",(w/2).toFixed(1)+" weeks"]]}}},
    {id:"gig",name:"Gig driver profit",icon:"🚗",cta:["Compare gig apps","make-money.html"],
     inputs:[["gross","Gross earnings per hour ($)",24],["miles","Miles driven per hour",14],["cpm","Car cost per mile ($)",0.35],["hours","Hours per week",15]],
     run:function(v){var cost=v.miles*v.cpm,net=v.gross-cost;
       return {big:money2(net)+"/hr",label:"Real profit after car costs",rows:[["Car cost per hour",money2(cost)],["Weekly net",money(net*v.hours)],["Monthly net",money(net*v.hours*4.33)],["Yearly net",money(net*v.hours*52)]]}}},
    {id:"cashback",name:"Cashback savings",icon:"💸",cta:["See the best cashback apps","cashback.html"],
     inputs:[["groc","Monthly groceries ($)",600],["online","Monthly online shopping ($)",250],["gas","Monthly gas ($)",180],["dine","Monthly dining ($)",200],["rate","Average cashback (%)",3]],
     run:function(v){var m=(v.groc+v.online+v.gas+v.dine)*v.rate/100;
       return {big:money(m*12)+"/yr",label:"Free money from purchases you already make",rows:[["Per month",money2(m)],["Over 5 years",money(m*60)],["If invested at 5% for 10 yrs",money(m*((Math.pow(1+.05/12,120)-1)/(.05/12)))]]}}},
    {id:"debt",name:"Debt payoff",icon:"🧾",cta:["Get a debt-free plan","get-matched.html?goal=debt"],
     inputs:[["bal","Balance ($)",5000],["apr","Interest rate (APR %)",22],["pay","Monthly payment ($)",250]],
     run:function(v){var r=v.apr/1200,b=v.bal,m=0,int=0,ser=[];
       if(v.pay<=b*r) return {big:"Never",label:"Payment doesn't cover interest",rows:[["Minimum to make progress",money2(b*r+1)]]};
       while(b>0&&m<600){var i=b*r;int+=i;b=b+i-v.pay;m++;if(m%Math.max(1,Math.ceil(m/12))===0)ser.push(Math.max(0,b))}
       return {big:m+" months",label:"Until you're debt-free",rows:[["Total interest paid",money(int)],["Total paid",money(v.bal+int)],["Pay +$100/mo instead",payoff(v.bal,v.apr,v.pay+100)+" months"]],series:ser}}},
    {id:"grow",name:"Compound savings growth",icon:"📈",cta:["Find high-yield savings options","guides/high-yield-savings-guide.html"],
     inputs:[["init","Starting amount ($)",1000],["monthly","Monthly deposit ($)",200],["rate","Annual return (%)",5],["years","Years",10]],
     run:function(v){var r=v.rate/1200,b=v.init,ser=[];for(var m=1;m<=v.years*12;m++){b=b*(1+r)+v.monthly;if(m%12===0)ser.push(b)}
       var dep=v.init+v.monthly*v.years*12;return {big:money(b),label:"Future balance",rows:[["Total deposited",money(dep)],["Interest earned",money(b-dep)]],series:ser}}},
    {id:"budget",name:"50/30/20 budget",icon:"🧮",cta:["Read the budgeting guide","guides/50-30-20-budget.html"],
     inputs:[["inc","Monthly take-home pay ($)",4000]],
     run:function(v){return {big:money(v.inc*.2)+"/mo",label:"Savings & debt payoff (20%)",rows:[["Needs (50%)",money(v.inc*.5)],["Wants (30%)",money(v.inc*.3)],["Savings/debt (20%)",money(v.inc*.2)],["Saved per year",money(v.inc*.2*12)]]}}},
    {id:"loan",name:"Loan payment",icon:"🏦",cta:["Compare loan options","get-matched.html?goal=borrow"],
     inputs:[["amt","Loan amount ($)",10000],["apr","APR (%)",11],["term","Term (months)",36]],
     run:function(v){var p=amort(v.amt,v.apr,v.term);return {big:money2(p)+"/mo",label:"Estimated monthly payment",rows:[["Total interest",money(p*v.term-v.amt)],["Total repaid",money(p*v.term)]]}}},
    {id:"wage",name:"Hourly ↔ salary",icon:"⏱️",cta:["Earn more on the side","make-money.html"],
     inputs:[["rate","Hourly rate ($)",25],["hours","Hours per week",40],["weeks","Paid weeks per year",52]],
     run:function(v){var y=v.rate*v.hours*v.weeks;return {big:money(y)+"/yr",label:"Annual gross salary",rows:[["Monthly",money(y/12)],["Bi-weekly",money(y/26)],["Weekly",money(y/52)],["Daily (5-day week)",money(v.rate*v.hours/5)]]}}},
    {id:"emergency",name:"Emergency fund",icon:"🛟",cta:["Build it faster with a side hustle","get-matched.html?goal=earn"],
     inputs:[["exp","Monthly essential expenses ($)",2500],["months","Months of cover",3],["have","Already saved ($)",500],["save","Can save per month ($)",300]],
     run:function(v){var t=v.exp*v.months,gap=Math.max(0,t-v.have),m=Math.ceil(gap/Math.max(1,v.save));
       return {big:money(t),label:"Emergency fund target",rows:[["Still needed",money(gap)],["Months to reach it",gap?m:"Done ✓"],["With +$200/mo side income",gap?Math.ceil(gap/(v.save+200))+" months":"Done ✓"]]}}}
  ];
  function payoff(bal,apr,pay){var r=apr/1200,b=bal,m=0;while(b>0&&m<600){b=b*(1+r)-pay;m++}return m}
  var root=document.getElementById("calc-app"); if(!root) return;
  var base=root.getAttribute("data-base")||"",only=root.getAttribute("data-only"), list=only?CALCS.filter(function(c){return only.split(",").indexOf(c.id)>-1}):CALCS;
  var tabs='<div class="tabs" role="tablist">'+list.map(function(c,i){return '<button class="chip tab'+(i?"":" active")+'" role="tab" data-tab="'+c.id+'">'+c.icon+" "+c.name+'</button>'}).join("")+'</div>';
  var bodies=list.map(function(c,i){return '<div class="calc'+(i?"":" active")+'" id="calc-'+c.id+'" role="tabpanel"><div class="panel"><h3>'+c.icon+" "+c.name+'</h3><div class="form">'+
    c.inputs.map(function(f){return '<div><label for="'+c.id+'-'+f[0]+'">'+f[1]+'</label><input type="number" inputmode="decimal" step="any" min="0" id="'+c.id+'-'+f[0]+'" data-k="'+f[0]+'" value="'+f[2]+'"></div>'}).join("")+
    '</div><p class="form-note" style="margin-top:12px">Estimates only — not financial advice.</p></div><div class="result-box" aria-live="polite"><div class="small" data-label></div><div class="big" data-big></div><div data-rows></div><div class="bar-chart" data-chart></div><a class="btn btn-accent btn-block" style="margin-top:18px" href="'+base+c.cta[1]+'">'+c.cta[0]+' →</a></div></div>'}).join("");
  root.innerHTML=tabs+bodies;
  list.forEach(function(c){var el=document.getElementById("calc-"+c.id);
    function upd(){var v={};el.querySelectorAll("[data-k]").forEach(function(i){v[i.getAttribute("data-k")]=parseFloat(i.value)||0});var r=c.run(v);
      el.querySelector("[data-big]").textContent=r.big;el.querySelector("[data-label]").textContent=r.label;
      el.querySelector("[data-rows]").innerHTML=r.rows.map(function(x){return '<div class="row"><span>'+x[0]+'</span><b>'+x[1]+'</b></div>'}).join("");
      var ch=el.querySelector("[data-chart]"); if(r.series&&r.series.length){var mx=Math.max.apply(null,r.series)||1;ch.style.display="flex";ch.innerHTML=r.series.slice(0,40).map(function(s){return '<span style="height:'+(s/mx*100)+'%" title="'+money(s)+'"></span>'}).join("")}else ch.style.display="none"}
    el.addEventListener("input",upd);upd()});
  root.querySelectorAll("[data-tab]").forEach(function(b){b.addEventListener("click",function(){
    root.querySelectorAll("[data-tab]").forEach(function(x){x.classList.remove("active")});b.classList.add("active");
    root.querySelectorAll(".calc").forEach(function(x){x.classList.toggle("active",x.id==="calc-"+b.getAttribute("data-tab"))});
    if(history.replaceState) history.replaceState(null,"","#"+b.getAttribute("data-tab"))})});
  var h=location.hash.slice(1); if(h){var t=root.querySelector('[data-tab="'+h+'"]'); if(t) t.click()}
})();
