/* ============================================================================
   glossary.js — shared click-to-explain glossary for "Trust the Machine".
   Included by index.html + all 5 chapters. Self-injects its CSS.

   window.Glossary.wrap(rootEl)  — wrap known terms under rootEl in tappable spans
   window.Glossary.refresh()     — re-wrap the whole document (used on lang toggle)

   Reads window.LANG ('en'|'zh'). Plain, one-breath definitions for someone who
   has never heard the term. EN matching uses word boundaries; ZH uses the exact
   substrings the chapters actually use.
   ============================================================================ */
(function(){
  if (window.Glossary) return;                       // idempotent include

  /* ---- term dictionary. key → {en:{def,why?}, zh:{def,why?}, en:[surfaces], zh:[surfaces]} ---- */
  var TERMS = {
    'levels': {
      en:{def:'A 0–5 scale for how much a car can drive itself. 0 = you do everything; 5 = it needs no driver at all. The higher the number, the more the machine does.'},
      zh:{def:'衡量一辆车能自己开多少的 0–5 级刻度。0 级＝全靠你；5 级＝完全不需要驾驶员。数字越大，机器做得越多。'},
      match_en:['Level 0','Level 1','Level 2','Level 3','Level 4','Level 5','L0','L1','L2','L3','L4','L5','L2-plus-plus','L2+'],
      match_zh:['L0','L1','L2','L3','L4','L5']
    },
    'takeover': {
      en:{def:'The moment the car gives control back and expects you to drive again — usually because it has hit something it cannot handle.', why:'These handbacks often come with almost no warning, at the hardest moment. That gap is where most of the danger lives.'},
      zh:{def:'车把控制权交还给你、要你重新接手开车的那一刻——通常是因为它遇到了自己搞不定的情况。', why:'这种交还往往几乎没有预警，且发生在最棘手的时刻。危险大多就藏在这道落差里。'},
      match_en:['takeover request','takeover','take over','hand back','hands back','handover','handoff','handed back','hand the wheel back'],
      match_zh:['接管']
    },
    'fallback': {
      en:{def:'The car\'s backup plan when its main driving system fails — slow down, pull over, or ask you to take the wheel.'},
      zh:{def:'当主驾驶系统失效时，车的备用方案——减速、靠边停车，或让你来接手。'},
      match_en:['fallback','fall back'],
      match_zh:['兜底','后备']
    },
    'override': {
      en:{def:'When the human grabs control back from the car — braking, steering, or switching the system off mid-drive.'},
      zh:{def:'人从车手里夺回控制权——中途踩刹车、打方向，或直接关掉系统。'},
      match_en:['override','overrides','overriding'],
      match_zh:['接管掉','强行干预']
    },
    'sensor fusion': {
      en:{def:'Blending what several sensors "see" — camera, radar, laser — into one picture, so a mistake by one is caught by the others.', why:'No single sensor is right all the time. Fusing them is how the car stays reliable when one is fooled by rain, glare, or dark.'},
      zh:{def:'把多个传感器"看到"的东西——摄像头、雷达、激光——融合成同一幅画面，好让某一个出错时，其他能补上。', why:'没有哪个单一传感器永远正确。融合，正是车在某个传感器被雨、眩光或黑暗骗到时仍能保持可靠的办法。'},
      match_en:['sensor fusion','fuse the sensors','fusing'],
      match_zh:['传感器融合','融合']
    },
    'sensor': {
      en:{def:'A device that lets the car sense the world — a camera, a radar, a laser scanner. Its eyes and ears.'},
      zh:{def:'让车感知世界的部件——摄像头、雷达、激光扫描仪。相当于它的眼睛和耳朵。'},
      match_en:['sensors','sensor'],
      match_zh:['传感器']
    },
    'lidar': {
      en:{def:'A spinning laser that measures distance by timing light bounces, building a precise 3D map of everything around the car — even in the dark.'},
      zh:{def:'一种旋转的激光，靠计算光线反射的时间来测距，为车周围的一切建出精确的三维地图——即使在黑暗中也行。'},
      match_en:['LiDAR','lidar'],
      match_zh:['激光雷达']
    },
    'radar': {
      en:{def:'Radio waves that measure how far away things are and how fast they move. Works through rain and fog where cameras struggle.'},
      zh:{def:'用无线电波测量物体的距离和移动速度。在摄像头吃力的雨天和雾中照样管用。'},
      match_en:['radar'],
      match_zh:['毫米波雷达','雷达']
    },
    'point cloud': {
      en:{def:'The cloud of millions of dots a laser scanner paints onto the world — each dot a point it has measured. Together they form a 3D shape.'},
      zh:{def:'激光扫描仪在世界上"点"出的成百上千万个点——每个点都是它测到的一处。合起来就构成一个三维形状。'},
      match_en:['point cloud','point-cloud'],
      match_zh:['点云']
    },
    'bounding box': {
      en:{def:'The box the car draws around each thing it spots — a car, a person — to say "an object is here, this big."'},
      zh:{def:'车在识别到的每样东西——一辆车、一个人——周围画出的框，表示"这里有个物体，这么大"。'},
      match_en:['bounding box','bounding boxes'],
      match_zh:['检测框','边界框']
    },
    'confidence': {
      en:{def:'How sure the car is about what it just saw, as a percentage. 95% means fairly sure; 40% means it is guessing.', why:'The car acts on these odds every instant. A low score at the wrong moment is how it misses a real hazard — or brakes for a ghost.'},
      zh:{def:'车对刚看到的东西有多确定，用百分比表示。95% 表示相当有把握；40% 表示它在猜。', why:'车每一瞬间都在按这些概率行动。在错误的时刻出现一个低分，就是它漏掉真实危险、或为幻影急刹的原因。'},
      match_en:['confidence score','detection confidence','certainty score','confidence','certainty'],
      match_zh:['置信度','置信','把握']
    },
    'adaptive weighting': {
      en:{def:'The car trusting whichever sensor is most reliable right now — leaning on radar in fog, on the camera in bright daylight.'},
      zh:{def:'车此刻更信任哪个传感器最靠谱，就多听它的——雾天靠雷达，大晴天靠摄像头。'},
      match_en:['adaptive weighting','adaptively weight','weighting'],
      match_zh:['自适应加权','动态加权']
    },
    'graceful degradation': {
      en:{def:'When something fails, the car eases off carefully instead of quitting all at once — slowing and warning you rather than dropping the wheel.'},
      zh:{def:'出问题时，车小心地逐步降级，而不是一下子全部罢工——先减速、先提醒你，而不是直接甩开方向盘。'},
      match_en:['graceful degradation','degrade gracefully','degraded','degradation'],
      match_zh:['优雅降级','降级']
    },
    'false alarm': {
      en:{def:'The car braking or warning for a danger that was not really there — a shadow, a plastic bag, a harmless reflection.'},
      zh:{def:'车为一个其实并不存在的危险而急刹或报警——一片阴影、一个塑料袋、一次无害的反光。'},
      match_en:['false alarm','false alarms','false positive','false positives'],
      match_zh:['误报','假警报']
    },
    'perception': {
      en:{def:'The car\'s job of turning raw sensor data into an understanding of the scene: that is a truck, that is a child, that is a lane line.'},
      zh:{def:'车把原始传感器数据转化为对场景理解的工作：那是卡车，那是小孩，那是车道线。'},
      match_en:['perception'],
      match_zh:['感知']
    },
    'long tail': {
      en:{def:'The endless list of rare, weird situations a car meets once in a million miles — a couch on the freeway, a person in a costume. Common driving is easy; the long tail is what is hard.', why:'A car can be safe 99.9% of the time and still fail on the strange 0.1%. Those rare cases are exactly where trust is won or lost.'},
      zh:{def:'车每开上百万英里才会碰上一次的、没完没了的罕见怪状况——高速上的一张沙发、一个穿着奇装的人。日常驾驶很容易；难的正是这条"长尾"。', why:'一辆车可以在 99.9% 的时间里都安全，却仍在那诡异的 0.1% 上翻车。信任的得失，恰恰就在这些罕见情形里。'},
      match_en:['long tail','long-tail'],
      match_zh:['长尾']
    },
    'edge case': {
      en:{def:'A rare, tricky situation the car was not really built for — the kind that shows up at the very edge of what it can handle.'},
      zh:{def:'一种罕见、棘手、车其实没怎么被设计来应对的情形——出现在它能力最边缘的那种。'},
      match_en:['edge case','edge cases','corner case','corner cases'],
      match_zh:['边缘情况','极端情况','边角案例']
    },
    'near-miss': {
      en:{def:'A close call that did not become a crash — but easily could have. Engineers study these to catch problems before someone gets hurt.'},
      zh:{def:'一次差点酿成事故、却没真撞上的险情——但很容易就撞了。工程师研究这些，好在有人受伤前发现问题。'},
      match_en:['near-miss','near miss','near-misses','close call'],
      match_zh:['险情','险些事故']
    },
    'disengagement': {
      en:{def:'When a self-driving car switches itself off and hands back to a human, because it is no longer sure it can cope.'},
      zh:{def:'自动驾驶车因为不再确定自己应付得来，而主动关闭、把控制权交还给人的时刻。'},
      match_en:['disengagement','disengagements','disengage'],
      match_zh:['脱离','退出接管']
    },
    'black box': {
      en:{def:'A system whose inner reasoning you cannot see. It gives an answer, but not a readable "why" — even its makers cannot fully trace the decision.', why:'If you cannot see why it chose what it did, you cannot be sure when it will choose wrong. That is the hard part of trusting it.'},
      zh:{def:'一个你看不到内部推理的系统。它给出答案，却没有可读的"为什么"——连造它的人都无法完全追溯这个决定。', why:'如果你看不到它为什么这么选，就无法确定它什么时候会选错。这正是信任它的难处。'},
      match_en:['black box','black-box'],
      match_zh:['黑箱','黑盒']
    },
    'deep learning': {
      en:{def:'A way of building software that learns from millions of examples instead of being given rules. It learns to drive by watching, the way a person learns a knack — not from a rulebook.', why:'Because it learned by example rather than rules, no one can read back a clean list of reasons for any single decision.'},
      zh:{def:'一种让软件从上百万个例子中学习、而非被灌输规则的做法。它靠"看"来学开车，就像人练出一门手艺——而不是照着规则手册。', why:'正因为它是靠例子而非规则学来的，谁也无法为任何单个决定回读出一份清清楚楚的理由清单。'},
      match_en:['deep-learning model','deep learning','deep-learning','neural network','neural net','the model','model output'],
      match_zh:['深度学习','神经网络','深度学习模型']
    },
    'rule-based': {
      en:{def:'Old-style software that follows fixed "if this, then that" rules a human wrote. Easy to read and check — but brittle when the world does something the rules never named.'},
      zh:{def:'老派软件，遵循人写好的固定"如果……就……"规则。好读、好核查——但当世界做出规则从未提及的事时，就很脆弱。'},
      match_en:['rule-based stack','rule-based','rules-based'],
      match_zh:['基于规则','规则式']
    },
    'interpretability': {
      en:{def:'How easily a human can understand why the system did what it did. Low interpretability means even the engineers are partly guessing.'},
      zh:{def:'人能多容易地弄懂系统为何那样做。可解释性低，意味着连工程师都在一定程度上靠猜。'},
      match_en:['interpretability','interpretable','explainability'],
      match_zh:['可解释性','可解释']
    },
    'actuator': {
      en:{def:'The part that actually moves things — the motor that turns the wheel or pushes the brake once the software has decided.'},
      zh:{def:'真正让东西动起来的部件——软件做出决定后，那个转动方向盘或踩下刹车的马达。'},
      match_en:['actuator','actuators'],
      match_zh:['执行器','作动器']
    },
    'driver monitoring': {
      en:{def:'A camera or sensor that watches the driver to check they are still paying attention — and nags them if their eyes leave the road.'},
      zh:{def:'一个盯着驾驶员、确认其仍在专心的摄像头或传感器——一旦你的视线离开道路，它就会提醒你。'},
      match_en:['driver-monitoring','driver monitoring','driver attention monitoring'],
      match_zh:['驾驶员监控','注意力监测']
    },
    'odd': {
      en:{def:'The exact conditions a self-driving car is allowed to run in — which roads, which weather, which speeds. Outside that box, it is not designed to drive.'},
      zh:{def:'自动驾驶车被允许运行的确切条件——哪些道路、哪种天气、哪种速度。超出这个范围，它就不是被设计来开的。'},
      match_en:['operational design domain','defined domain','operating domain','ODD'],
      match_zh:['运行设计域','设计运行范围','限定域']
    },
    'geofence': {
      en:{def:'An invisible boundary on the map. The car will only drive itself inside this zone it knows by heart, and refuses beyond it.'},
      zh:{def:'地图上一道看不见的边界。车只在这片它烂熟于心的区域里自动驾驶，越界就不干了。'},
      match_en:['geofence','geofenced','geo-fence'],
      match_zh:['地理围栏','电子围栏']
    },
    'liability': {
      en:{def:'Who the law holds responsible — and who pays — when something goes wrong. With driver-assist, that is usually still you, not the carmaker.', why:'This is the question that decides who bears the cost of a crash. For most systems on sale today, the answer in court is: the human.'},
      zh:{def:'出事时，法律认定谁该负责、由谁买单。用辅助驾驶时，这通常仍是你，而不是车厂。', why:'正是这个问题决定了谁来承担事故的代价。对当今在售的大多数系统而言，法庭上的答案是：人。'},
      match_en:['product-liability','product liability','liability boundary','liability','liable'],
      match_zh:['责任归属','产品责任','担责','责任']
    },
    'robotaxi': {
      en:{def:'A taxi with no driver — it drives, you ride. Runs only inside a mapped area it has been cleared for.'},
      zh:{def:'没有司机的出租车——它开，你坐。只在获准的、已建图的区域内运行。'},
      match_en:['robotaxi','robotaxis','robo-taxi'],
      match_zh:['无人出租车','自动驾驶出租车','机器人出租车']
    },
    'av': {
      en:{def:'Autonomous vehicle — a car that can drive itself, to some degree, without a person steering.'},
      zh:{def:'自动驾驶车辆——一辆能在某种程度上自己开、无需人操控方向的车。'},
      match_en:['autonomous vehicle','autonomous vehicles','AVs','AV'],
      match_zh:['自动驾驶车辆','自动驾驶汽车']
    },
    'assist': {
      en:{def:'Driver-assist: the car helps with steering and speed, but you are still the driver and must watch the road the whole time.'},
      zh:{def:'辅助驾驶：车帮你转向和控速，但开车的仍是你，全程都得盯着路。'},
      match_en:['driver-assist','driver assist','assistance','assist'],
      match_zh:['辅助驾驶','辅助']
    }
  };

  /* ---- CSS (self-injected) ---- */
  var CSS = ''
    + '.gl-term{color:#bcd4ff;cursor:help;white-space:nowrap;'
    +   'border-bottom:1px dashed rgba(138,176,224,.7);'
    +   'background:linear-gradient(180deg,rgba(138,176,224,0) 60%,rgba(138,176,224,.14) 100%);'
    +   'border-radius:2px;transition:color .15s,background .15s,transform .15s;position:relative}'
    + '.gl-term:after{content:"";position:absolute;top:-.28em;right:-.42em;width:.34em;height:.34em;'
    +   'border-radius:50%;background:#8AB0E0;box-shadow:0 0 6px rgba(138,176,224,.9);'
    +   'animation:gl-pulse 2.6s ease-in-out infinite}'
    + '.gl-term:hover{color:#eaf3ff;background:rgba(138,176,224,.22);transform:translateY(-1px)}'
    + '.gl-term.gl-open{color:#fff;background:rgba(138,176,224,.28)}'
    + '@keyframes gl-pulse{0%,100%{opacity:.35;transform:scale(.8)}50%{opacity:1;transform:scale(1.15)}}'
    + '#gl-pop{position:fixed;z-index:9999;max-width:min(340px,86vw);opacity:0;transform:translateY(6px) scale(.98);'
    +   'pointer-events:none;transition:opacity .18s ease,transform .18s ease;'
    +   'background:linear-gradient(180deg,rgba(20,27,50,.98),rgba(12,17,34,.98));'
    +   'border:1px solid rgba(138,176,224,.34);border-radius:14px;padding:14px 16px 15px;'
    +   'box-shadow:0 22px 55px rgba(0,0,0,.6);color:#eaf0ff;font-size:15px;line-height:1.5;text-align:left}'
    + '#gl-pop.show{opacity:1;transform:translateY(0) scale(1);pointer-events:auto}'
    + '#gl-pop .gl-h{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#8AB0E0;margin-bottom:.45rem;font-weight:800}'
    + '#gl-pop .gl-def{color:#e9f0ff}'
    + '#gl-pop .gl-why{margin-top:.6rem;padding-top:.55rem;border-top:1px solid rgba(138,176,224,.18);color:#b9c6e6;font-size:13.5px}'
    + '#gl-pop .gl-why b{color:#f5b13f;font-weight:800;letter-spacing:.03em}'
    + '#gl-pop .gl-x{position:absolute;top:8px;right:11px;color:#7f8db0;cursor:pointer;font-size:16px;line-height:1;border:none;background:none}'
    + '#gl-pop .gl-x:hover{color:#eaf0ff}'
    + '@media (prefers-reduced-motion: reduce){.gl-term:after{animation:none;opacity:.7}#gl-pop{transition:opacity .12s}.gl-term{transition:none}}';

  function injectCSS(){
    if (document.getElementById('gl-style')) return;
    var s = document.createElement('style'); s.id='gl-style'; s.textContent=CSS;
    (document.head||document.documentElement).appendChild(s);
  }

  /* ---- build matchers ---- */
  function esc(s){ return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'); }
  var reEn=null, reZh=null, surfaceKey={};
  function buildMatchers(){
    var en=[], zh=[]; surfaceKey={};
    Object.keys(TERMS).forEach(function(key){
      (TERMS[key].match_en||[]).forEach(function(s){ en.push(s); surfaceKey[s.toLowerCase()]=key; });
      (TERMS[key].match_zh||[]).forEach(function(s){ zh.push(s); surfaceKey[s]=key; });
    });
    en.sort(function(a,b){return b.length-a.length;});      // longest-first so "sensor fusion" beats "sensor"
    zh.sort(function(a,b){return b.length-a.length;});
    reEn = en.length ? new RegExp('\\b('+en.map(esc).join('|')+')\\b','gi') : null;
    reZh = zh.length ? new RegExp('('+zh.map(esc).join('|')+')','g') : null;   // CJK: no word boundary
  }

  var SKIP = {A:1,BUTTON:1,KBD:1,INPUT:1,TEXTAREA:1,SCRIPT:1,STYLE:1,SELECT:1,OPTION:1,SVG:1,CANVAS:1};

  /* ---- wrap known terms under root; first occurrence of each term per wrap call ---- */
  function wrap(root){
    if (!root || !reEn) return;
    var lang = window.LANG==='zh' ? 'zh' : 'en';
    var re = lang==='zh' ? reZh : reEn;
    if (!re) return;
    var used = {};
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function(n){
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode;
        while (p && p!==root){
          if (p.nodeType===1){
            if (SKIP[p.tagName]) return NodeFilter.FILTER_REJECT;
            if (p.classList && p.classList.contains('gl-term')) return NodeFilter.FILTER_REJECT;
          }
          p = p.parentNode;
        }
        re.lastIndex=0; return re.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var nodes=[]; while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function(node){
      var text=node.nodeValue, out=null, last=0, m; re.lastIndex=0;
      while ((m=re.exec(text))){
        var key = surfaceKey[lang==='zh'?m[0]:m[0].toLowerCase()];
        if (!key || used[key]){ continue; }            // one wrap per term per call → no clutter
        used[key]=1;
        out = out || document.createDocumentFragment();
        if (m.index>last) out.appendChild(document.createTextNode(text.slice(last,m.index)));
        var span=document.createElement('span'); span.className='gl-term'; span.dataset.term=key; span.textContent=m[0];
        out.appendChild(span); last=m.index+m[0].length;
      }
      if (out){ if (last<text.length) out.appendChild(document.createTextNode(text.slice(last))); node.parentNode.replaceChild(out,node); }
    });
  }

  /* ---- popup ---- */
  var pop=null;
  function ensurePop(){
    if (pop) return pop;
    pop=document.createElement('div'); pop.id='gl-pop';
    pop.innerHTML='<button class="gl-x" aria-label="close">×</button><div class="gl-h"></div><div class="gl-def"></div><div class="gl-why"></div>';
    document.body.appendChild(pop);
    pop.querySelector('.gl-x').addEventListener('click', hide);
    return pop;
  }
  var openTerm=null;
  function show(span){
    var key=span.dataset.term, t=TERMS[key]; if(!t) return;
    var lang=window.LANG==='zh'?'zh':'en', d=t[lang]||t.en;
    ensurePop();
    pop.querySelector('.gl-h').textContent=span.textContent;
    pop.querySelector('.gl-def').textContent=d.def||'';
    var why=pop.querySelector('.gl-why');
    if (d.why){ why.style.display=''; why.innerHTML='<b>'+(lang==='zh'?'为何重要':'Why it matters')+'</b> — '+d.why; }
    else why.style.display='none';
    if (openTerm) openTerm.classList.remove('gl-open');
    openTerm=span; span.classList.add('gl-open');
    // position: below the term, clamped into the viewport
    pop.style.left='-9999px'; pop.classList.add('show');
    var r=span.getBoundingClientRect(), pw=pop.offsetWidth, ph=pop.offsetHeight, M=10;
    var left=Math.min(Math.max(M, r.left), window.innerWidth-pw-M);
    var top=r.bottom+8; if (top+ph>window.innerHeight-M) top=Math.max(M, r.top-ph-8);
    pop.style.left=left+'px'; pop.style.top=top+'px';
  }
  function hide(){ if(!pop) return; pop.classList.remove('show'); if(openTerm){openTerm.classList.remove('gl-open');openTerm=null;} }

  // capture phase: a term click must win before the beat/overlay's own click-to-advance handler
  document.addEventListener('click', function(e){
    var span=e.target.closest && e.target.closest('.gl-term');
    if (span){ e.stopPropagation(); e.preventDefault(); (span===openTerm)?hide():show(span); return; }
    if (pop && !e.target.closest('#gl-pop')) hide();
  }, true);
  document.addEventListener('keydown', function(e){ if(e.key==='Escape') hide(); });
  window.addEventListener('scroll', hide, true);
  window.addEventListener('resize', hide);

  function refresh(){ wrap(document.body); }

  buildMatchers();
  if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', injectCSS);
  else injectCSS();

  window.Glossary = { wrap:wrap, refresh:refresh, hide:hide, TERMS:TERMS };
})();
