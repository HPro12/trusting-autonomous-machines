# i18n contract — paste verbatim, then translate

`index.html` is the WORKING reference. Read it to see the pattern in situ:
- CSS block `#langtoggle` inside `<style>`
- `<button id="langtoggle" …>中文</button>` as the first element in `<body>`
- the i18n **core `<script>`** (with `window.ZH = {…}`) placed BEFORE all other scripts
- `data-i18n` on static text elements; `tr("…")` around JS/canvas display strings
- `window.onLangChange = <re-render current screen>` near the end of the page script

## 1. CSS — add inside the chapter's `<style>` (verbatim)
```css
  /* ---------------- language toggle (shared across all pages) ---------------- */
  #langtoggle{position:fixed; top:14px; right:14px; z-index:100;
    font:600 12.5px/1 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; letter-spacing:.02em;
    color:#ECEEF2; background:rgba(20,22,28,.72); border:1px solid rgba(255,255,255,.14); border-radius:999px;
    padding:9px 14px; cursor:pointer; backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
    box-shadow:0 8px 30px rgba(0,0,0,.30); transition:color .2s,border-color .2s,background .2s}
  #langtoggle:hover{color:#fff; border-color:rgba(255,255,255,.28); background:rgba(28,31,39,.82)}
```
If a full-screen overlay (start screen, decision, outcome) has a z-index ≥ 100, bump `#langtoggle` z-index above it so it stays clickable. If an existing control already sits at the top-right corner (e.g. a mute chip), offset the toggle left of it (`right:` larger) so they don't overlap.

## 2. Button — first element inside `<body>` (verbatim)
```html
<button id="langtoggle" type="button" aria-label="切换语言 / Switch language">中文</button>
```

## 3. i18n core `<script>` — place as the FIRST `<script>` in the body, before three.js and before any game script (so `window.tr` / `window.LANG` exist when game code runs). Verbatim except you FILL `window.ZH`.
```html
<script>
/* i18n core — identical on every page. English is the source of truth; ZH maps normalized
   English -> Simplified Chinese. Language persists in localStorage['ttm.lang']. */
window.ZH = { /* FILL: every user-visible English string (normalized) -> Chinese */ };
(function(){
  var LKEY='ttm.lang';
  function norm(s){ return (s||"").replace(/&nbsp;/g," ").replace(/\s+/g," ").trim(); }
  try{ window.LANG = localStorage.getItem(LKEY)==='zh' ? 'zh' : 'en'; }catch(e){ window.LANG='en'; }
  window.tr = function(s){ var z=window.ZH[norm(s)]; return (window.LANG==='zh'&&z!=null) ? z : s; };
  var origin = new WeakMap();
  function applyStatic(){
    document.documentElement.lang = window.LANG==='zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      if(!origin.has(el)) origin.set(el, el.innerHTML);
      var en=origin.get(el), z=window.ZH[norm(en)];
      el.innerHTML = (window.LANG==='zh' && z!=null) ? z : en;
    });
    var b=document.getElementById('langtoggle'); if(b) b.textContent = window.LANG==='zh' ? 'EN' : '中文';
  }
  window.applyI18n = function(){ applyStatic(); if(typeof window.onLangChange==='function') window.onLangChange(); };
  window.toggleLang = function(){
    window.LANG = window.LANG==='zh' ? 'en' : 'zh';
    try{ localStorage.setItem(LKEY, window.LANG); }catch(e){}
    window.applyI18n();
  };
  document.addEventListener('DOMContentLoaded', function(){
    var b=document.getElementById('langtoggle'); if(b) b.addEventListener('click', window.toggleLang);
    window.applyI18n();
  });
})();
</script>
```

## 4. Static DOM
Add a bare `data-i18n` attribute to every element that directly contains user-visible English text (headings, paragraphs, buttons, labels, hints, the start screen, the debrief). Put the Chinese in `window.ZH` keyed by the element's **normalized English innerHTML** (collapse whitespace, `&nbsp;`→space). Elements with inline markup (`<strong>`, `<span>`, `<br>`) are fine — the key is the full innerHTML string; copy it exactly into ZH.
Do NOT tag a container whose children are wired to JS by id — tag the inner text leaf instead.

## 5. JS + canvas strings
Wrap every user-visible display string with `tr("…")` at the point it is written to the DOM or drawn on canvas (`ctx.fillText`), and add its English→Chinese entry to ZH. Because `tr()` reads the live `window.LANG`, per-frame canvas text switches automatically. For text baked once into a texture, updating on the next regeneration is acceptable — do not rebuild the render engine for it (leave a `// ponytail:` note).
Do NOT wrap non-visible strings: element ids, class names, CSS text, audio scene names ('calm'/'tense'/'dawn'), event types, keys.

## 6. Live toggle
Define `window.onLangChange` to re-render whatever text is currently on screen (current dialogue beat, the open decision/options, the outcome panel, the debrief, and the mute chip label) so a mid-experience toggle updates immediately. If the chapter keeps a "current step" variable, re-invoke its render with it.

## Shared glossary (use these EXACT translations for consistency across all chapters + landing)
- Trust the Machine → 信任机器
- Can You Trust Your Car? → 你能信任你的车吗？
- The Night Drive → 夜间行驶 · Inside the Machine → 机器之内 · The Long Tail → 长尾 · Who's Responsible? → 谁来负责？ · The Trust Gap → 信任鸿沟
- driver → 驾驶员 · passenger → 乘客 · evaluator → 评估者 · regulator → 监管者 · city → 城市
- Continue → 继续 · Continue → → 继续 → · Continue to Chapter N ↗ → 前往第 N 章 ↗
- Drive again → 再驾驶一次 · Replay → 重玩
- Debrief → 复盘 · Chapter N · Debrief → 第 N 章 · 复盘 · Your last human decision → 你最后一次由人做出的决定
- Trust in system → 系统信任 · Attention left → 剩余注意力
- Sound → 声音 · Muted → 已静音 · KM/H → 公里/时
- Start driving → → 开始驾驶 → · change lane → 变道
- TAKE OVER — CHANGE LANE → 接管——请变道
- trust → 信任 · safety → 安全 · near-miss → 险情 · robotaxi → 无人驾驶出租车
- Keep Latin keycaps as-is (A, D, M, ←, →, Space, Enter). Keep digits, units-with-digits, road names (G2), and proper nouns.
- Voice: calm, precise, cinematic (the "Deliberate" tone). Use full-width Chinese punctuation （，。：？！——「」）.

## Also
- In `onLangChange`, set `document.title = tr("<the English title>")` and add that title to ZH.
- Keep English as the literal in the markup/JS — never replace it; translation is layered on top.
- Do NOT change game logic, ids, classes, Three.js, audio, or the `cytc.v1` save keys.

## Self-check before returning (REQUIRED)
Run a coverage check and report numbers:
1. Extract every `data-i18n` element's normalized English innerHTML → confirm each is a key in `window.ZH`.
2. Extract every `tr("…")` / `tr('…')` literal argument → confirm each normalized key is in `window.ZH`.
3. List any English display string you could NOT confidently place, with a reason.
Report: # static tagged, # tr() call sites, # ZH keys, and any gaps.
