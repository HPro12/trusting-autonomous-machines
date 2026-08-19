#!/usr/bin/env python3
"""Generate the five report figures as self-contained HTML (rendered to PNG).

Redesign v2 — "Meridian" editorial system:
  - serif titles (Georgia) over a sans data face, for a policy-paper feel
  - a three-color argument palette: NAVY = structure, TEAL = measured/positive,
    AZURE = the gap / the demanded standard / tension
  - richer infographic patterns than v1 (momentum flywheel, bullseye + progression
    key, a gap chart that draws the *missing* Chinese data, a cyclical pentagon,
    an energy-label-style autonomy card)
Authored at ~1.6x scale for crisp embedding at report width. Aspect ratios are
pinned to the docx drawing extents so the PNGs drop in without touching XML.
"""
import math, pathlib

OUT = pathlib.Path(__file__).parent

# ---- palette -----------------------------------------------------------------
# Matched to the published site's :root tokens (hpro12.github.io/trusting-autonomous-machines):
# warm paper, deep navy, teal for measured/positive, and AZURE as the tension / gap accent.
PAPER, PANEL = "#FBFBF8", "#EEF2F7"       # --bg, --surface-2
INK, SUB, MUT = "#1A2330", "#48525F", "#7B8695"  # --ink, --sub, --mut
LINE = "#E2E7EE"                          # --line
NAVY, NAVY2, NAVY_T = "#14243D", "#0F1B2E", "#EAF0F8"  # --navy, --navy-2
TEAL, TEALD, TEAL_T = "#2A9D8F", "#1F7A6E", "#E3F3F0"  # --accent, --accent-strong
AZURE, AZURED, AZURE_T = "#3E6FB0", "#2E5488", "#E4ECF7"  # --azure = the gap / demanded standard / tension

SERIF = '"Iowan Old Style",Georgia,"Times New Roman",serif'
SANS = '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif'


def page(w, h, body, extra=""):
    return f"""<!doctype html><html><head><meta charset=utf-8>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{w}px;height:{h}px;background:{PAPER};font-family:{SANS};color:{INK};
  -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}}
.wrap{{width:{w}px;height:{h}px;position:relative;overflow:hidden;background:{PAPER}}}
text{{font-family:{SANS}}}
.serif{{font-family:{SERIF}}}
{extra}
</style></head><body><div class=wrap>{body}</div></body></html>"""


def pt(cx, cy, R, deg):  # angle clockwise from top (12 o'clock)
    r = math.radians(deg)
    return cx + R * math.sin(r), cy - R * math.cos(r)


def txt(x, y, s, size, fill=INK, anchor="middle", weight="400", serif=False,
        italic=False, spacing=None, opacity=None):
    fam = SERIF if serif else SANS
    extra = ""
    if spacing is not None:
        extra += f' letter-spacing="{spacing}"'
    if italic:
        extra += ' font-style="italic"'
    if opacity is not None:
        extra += f' opacity="{opacity}"'
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" '
            f'font-family=\'{fam}\' font-weight="{weight}" fill="{fill}"{extra}>{s}</text>')


# ============================================================ Fig 1: Flywheel
def flywheel():
    W, H = 1600, 1180
    cx, cy, R, nr = 800, 610, 352, 140
    svg = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    svg.append(f'''<defs>
      <linearGradient id="spin" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="{TEAL}"/><stop offset="1" stop-color="{NAVY}"/></linearGradient>
      <marker id="mspin" markerWidth="12" markerHeight="12" refX="6" refY="6" orient="auto">
        <path d="M0,0 L11,6 L0,12 z" fill="{NAVY}"/></marker>
      <marker id="mspinT" markerWidth="12" markerHeight="12" refX="6" refY="6" orient="auto">
        <path d="M0,0 L11,6 L0,12 z" fill="{TEAL}"/></marker></defs>''')

    # header
    svg.append(txt(96, 96, "The Trust Flywheel", 46, INK, "start", "700", serif=True))
    svg.append(txt(98, 138, "It turns only while transparency keeps it coupled.",
                   23, SUB, "start", "400"))

    # outer track
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{LINE}" stroke-width="3"/>')

    nodes = [  # (name, deg, sub, emphasis)
        ("Exposure", 0, "real-world operation", False),
        ("Evidence", 90, "data accumulates", False),
        ("Transparency", 180, "made public", True),
        ("Trust", 270, "public confidence", False),
    ]
    half = math.degrees(math.asin(nr / R)) + 5  # gap so arrows clear the nodes
    # clockwise momentum arcs
    for i in range(4):
        a0 = nodes[i][1] + half
        a1 = nodes[(i + 1) % 4][1] - half + (360 if (i + 1) % 4 == 0 else 0)
        x0, y0 = pt(cx, cy, R, a0)
        x1, y1 = pt(cx, cy, R, a1)
        emph = (i == 2)  # Transparency -> Trust : the coupling
        col, mk, sw = ((TEAL, "mspinT", 12) if emph else (NAVY2, "mspin", 7))
        svg.append(f'<path d="M {x0:.1f} {y0:.1f} A {R} {R} 0 0 1 {x1:.1f} {y1:.1f}" '
                   f'fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" '
                   f'marker-end="url(#{mk})" opacity="{1 if emph else 0.9}"/>')

    # outer italic captions
    caps = [("generates evidence", 45), ("disclosed openly", 135),
            ("earns trust", 225), ("wider exposure", 315)]
    for s, deg in caps:
        x, y = pt(cx, cy, R + 60, deg)
        svg.append(txt(x, y + 6, s, 21, MUT, "middle", "400", serif=True, italic=True))

    # hub
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="118" fill="{NAVY}"/>')
    svg.append(txt(cx, cy - 20, "THE TRUST", 27, "#FFFFFF", "middle", "700", spacing="1"))
    svg.append(txt(cx, cy + 12, "FLYWHEEL", 27, "#FFFFFF", "middle", "700", spacing="1"))
    svg.append(txt(cx, cy + 48, "turns on transparency", 18, "#AFC4E0", "middle", "400", italic=True, serif=True))

    # nodes
    for i, (name, deg, sub, emph) in enumerate(nodes):
        x, y = pt(cx, cy, R, deg)
        fill = NAVY if emph else PAPER
        stroke = TEAL if emph else NAVY
        tcol = "#FFFFFF" if emph else INK
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{nr}" fill="{fill}" '
                   f'stroke="{stroke}" stroke-width="{6 if emph else 3.5}"/>')
        # step badge
        bx, by = x, y - 62
        bcol = TEAL if emph else NAVY_T
        btc = "#FFFFFF" if emph else NAVY
        svg.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="26" fill="{bcol}"/>')
        svg.append(txt(bx, by + 9, str(i + 1), 26, btc, "middle", "800"))
        svg.append(txt(x, y + 16, name, 30, tcol, "middle", "700"))
        scol = "#C6D6EC" if emph else SUB
        svg.append(txt(x, y + 50, sub, 19, scol, "middle", "400"))
        if emph:
            svg.append(txt(x, y + 92, "the coupling", 18, TEAL_T, "middle", "700", spacing="2"))

    svg.append('</svg>')
    return page(W, H, "".join(svg))


# ============================================================ Fig 2: Ring map
def ringmap():
    W, H = 1600, 1240
    cx, cy = 585, 650
    svg = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    svg.append(f'''<defs><marker id="inw" markerWidth="14" markerHeight="14" refX="7" refY="6" orient="auto">
        <path d="M0,0 L12,6 L0,12 z" fill="{TEAL}"/></marker></defs>''')

    svg.append(txt(96, 92, "The Whitelist Ring Map", 46, INK, "start", "700", serif=True))
    svg.append(txt(98, 134, "Operators earn scope from the outside in — the access model already in force.",
                   23, SUB, "start", "400"))

    rings = [  # outer -> inner : (num, name, r, fill, gate)
        (1, "Closed test road", 468, PAPER, "entry: closed-course validation"),
        (2, "Open road, safety driver", 362, "#F2F5F9", "gate: supervised safe mileage"),
        (3, "Open-road driverless", 252, NAVY_T, "gate: audited disengagement rate"),
        (4, "Core-city districts", 140, NAVY, "gate: sustained safety record"),
    ]
    for num, name, r, fill, gate in rings:
        stroke = NAVY if fill == NAVY else "#CFD8E3"
        sw = 0 if fill == NAVY else 2.5
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    # inward arrow (left)
    ax0, ax1 = cx - 545, cx - 168
    svg.append(f'<path d="M {ax0} {cy} L {ax1} {cy}" fill="none" stroke="{TEAL}" '
               f'stroke-width="7" stroke-linecap="round" marker-end="url(#inw)"/>')
    svg.append(txt(ax0 - 4, cy - 26, "Operators earn access inward", 23, TEALD, "start", "800"))
    svg.append(txt(ax0 - 4, cy + 34, "on accumulated safe mileage", 20, MUT, "start", "400", serif=True, italic=True))

    # numbered stage badges on the top of each band
    for num, name, r, fill, gate in rings:
        by = (cy - r + 34) if fill != NAVY else (cy - 70)
        bcol = "#FFFFFF" if fill == NAVY else NAVY
        btc = NAVY if fill == NAVY else "#FFFFFF"
        svg.append(f'<circle cx="{cx}" cy="{by}" r="21" fill="{bcol}"/>')
        svg.append(txt(cx, by + 8, str(num), 23, btc, "middle", "800"))
    svg.append(txt(cx, cy - 6, "Core-city", 27, "#FFFFFF", "middle", "700"))
    svg.append(txt(cx, cy + 26, "districts", 27, "#FFFFFF", "middle", "700"))

    # right-hand progression key (inner at top -> outer at bottom)
    kx, ky, rowh = 1120, 250, 132
    svg.append(txt(kx, ky - 46, "How scope opens", 24, INK, "start", "700", serif=True))
    for i, (num, name, r, fill, gate) in enumerate(reversed(rings)):  # inner->outer top->bottom
        y = ky + i * rowh
        dot = NAVY if num == 4 else (TEAL if num == 3 else "#9FB0C6")
        svg.append(f'<circle cx="{kx+22}" cy="{y+16}" r="20" fill="{dot}"/>')
        svg.append(txt(kx + 22, y + 24, str(num), 21, "#FFFFFF", "middle", "800"))
        svg.append(txt(kx + 60, y + 12, name, 24, INK, "start", "700"))
        svg.append(txt(kx + 60, y + 44, gate, 19, SUB, "start", "400"))
        if i < 3:
            svg.append(f'<line x1="{kx+22}" y1="{y+42}" x2="{kx+22}" y2="{y+rowh-6}" '
                       f'stroke="{LINE}" stroke-width="2.5"/>')

    # documentary note
    svg.append(f'<line x1="96" y1="{H-92}" x2="{W-96}" y2="{H-92}" stroke="{LINE}" stroke-width="2"/>')
    svg.append(txt(96, H - 52, "Documentary, not aspirational: this depicts the whitelist-and-rings model as it operates today.",
                   20, MUT, "start", "400", serif=True, italic=True))
    svg.append('</svg>')
    return page(W, H, "".join(svg))


# ============================================================ Fig 3: Trust gap
def trustgap():
    W, H = 1680, 1080
    svg = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    svg.append(f'''<defs>
      <pattern id="hatch" width="14" height="14" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
        <rect width="14" height="14" fill="{PANEL}"/>
        <line x1="0" y1="0" x2="0" y2="14" stroke="#C9D2DC" stroke-width="3"/></pattern></defs>''')

    x0, x1 = 250, 1470
    base, top100 = 760, 236

    def yv(p):
        return base - (base - top100) * p / 100

    # title
    svg.append(txt(96, 108, "The Trust Gap", 46, INK, "start", "700", serif=True))
    svg.append(txt(98, 150, "Asymmetric tolerance: we accept human error as fate, yet demand near-perfection of a machine.",
                   22, SUB, "start", "400"))

    # gridlines
    for p in (0, 25, 50, 75, 100):
        y = yv(p)
        dash = "" if p in (0, 100) else '6 9'
        svg.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{LINE}" '
                   f'stroke-width="{2.5 if p in (0,100) else 1.5}" stroke-dasharray="{dash}"/>')
        svg.append(txt(x0 - 20, y + 7, f"{p}%", 21, MUT, "end", "400"))
    ymid = (top100 + base) / 2
    svg.append(f'<text x="{x0-108}" y="{ymid:.0f}" transform="rotate(-90 {x0-108} {ymid:.0f})" '
               f'text-anchor="middle" font-size="22" font-family=\'{SANS}\' font-weight="600" '
               f'fill="{SUB}">Public acceptance</text>')

    bw = 250
    cA, cG, cC = 470, 830, 1190  # column centers

    # A: measured AV safety (teal) + uncertainty whisker
    mv = 78
    svg.append(f'<rect x="{cA-bw/2}" y="{yv(mv):.1f}" width="{bw}" height="{base-yv(mv):.1f}" rx="7" fill="{TEAL}"/>')
    for a, b in [(mv - 13, mv + 8)]:
        svg.append(f'<line x1="{cA}" y1="{yv(a):.1f}" x2="{cA}" y2="{yv(b):.1f}" stroke="{TEALD}" stroke-width="5"/>')
        for yy in (yv(a), yv(b)):
            svg.append(f'<line x1="{cA-30}" y1="{yy:.1f}" x2="{cA+30}" y2="{yy:.1f}" stroke="{TEALD}" stroke-width="5"/>')

    # G: China -- no public dataset (ghost hatched column)
    svg.append(f'<rect x="{cG-bw/2}" y="{top100:.1f}" width="{bw}" height="{base-top100:.1f}" rx="7" '
               f'fill="url(#hatch)" stroke="#B9C3CE" stroke-width="2.5" stroke-dasharray="9 8"/>')
    svg.append(txt(cG, ymid - 6, "?", 66, MUT, "middle", "800", serif=True))
    svg.append(txt(cG, ymid + 34, "no public", 20, SUB, "middle", "600"))
    svg.append(txt(cG, ymid + 60, "dataset", 20, SUB, "middle", "600"))

    # C: standard demanded (azure)
    dv = 99.5
    svg.append(f'<rect x="{cC-bw/2}" y="{yv(dv):.1f}" width="{bw}" height="{base-yv(dv):.1f}" rx="7" fill="{AZURE}"/>')

    # gap bracket between A(top) and C(top)
    gx = cC + bw / 2 + 34
    gy0, gy1 = yv(dv), yv(mv + 8)
    svg.append(f'<line x1="{gx}" y1="{gy0:.1f}" x2="{gx}" y2="{gy1:.1f}" stroke="{AZURED}" stroke-width="3.5"/>')
    for yy in (gy0, gy1):
        svg.append(f'<line x1="{gx-16}" y1="{yy:.1f}" x2="{gx+16}" y2="{yy:.1f}" stroke="{AZURED}" stroke-width="3.5"/>')
    gm = (gy0 + gy1) / 2
    svg.append(txt(gx + 30, gm - 8, "THE", 30, AZURED, "start", "800"))
    svg.append(txt(gx + 30, gm + 28, "TRUST GAP", 30, AZURED, "start", "800"))
    svg.append(txt(gx + 30, gm + 60, "what evidence must close", 18, SUB, "start", "400", serif=True, italic=True))

    # column labels (title color-coded to its column; no leading dot — it collided)
    def collab(cxc, t1, t2, col):
        svg.append(txt(cxc, base + 46, t1, 23, col, "middle", "800"))
        svg.append(txt(cxc, base + 78, t2, 19, SUB, "middle", "400"))
    collab(cA, "Measured AV safety", "published operator data", TEALD)
    collab(cG, "China", "no official disclosure", MUT)
    collab(cC, "Standard demanded", "of a machine (near-perfect)", AZURED)

    # source note
    ny = H - 108
    svg.append(f'<line x1="96" y1="{ny-28}" x2="{W-96}" y2="{ny-28}" stroke="{LINE}" stroke-width="2"/>')
    svg.append(txt(96, ny + 4, "Plotted on published international figures (operator safety reports; RAND on the mileage needed to demonstrate",
                   19, MUT, "start", "400"))
    svg.append(txt(96, ny + 32, "safety statistically). Comparable Chinese disengagement / incident data is not public —",
                   19, MUT, "start", "400"))
    svg.append(txt(96, ny + 60, "that the data is missing is itself part of the argument.",
                   19, AZURED, "start", "600", serif=True, italic=True))
    svg.append('</svg>')
    return page(W, H, "".join(svg))


# ============================================================ Fig 4: TRUST pentagon
def pentagon():
    W, H = 1680, 1320
    cx, cy, R, nr = 840, 690, 430, 152
    svg = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    svg.append(f'''<defs><marker id="cyc" markerWidth="13" markerHeight="13" refX="6" refY="6" orient="auto">
        <path d="M0,0 L11,6 L0,12 z" fill="{TEAL}"/></marker></defs>''')

    svg.append(txt(96, 96, "The TRUST Framework", 46, INK, "start", "700", serif=True))
    svg.append(txt(98, 138, "Five pillars that hold each other up — a cycle, not a checklist.",
                   23, SUB, "start", "400"))

    # cycle order (see §5): Validation -> Transparency -> Understanding -> Responsibility -> Governance
    pillars = [
        ("T", "Transparency", "discloses the evidence"),
        ("R", "Responsibility", "makes it binding"),
        ("U", "Understanding", "makes it legible"),
        ("S", "Safety Validation", "produces the evidence"),
        ("T", "Trustworthy Gov.", "keeps the loop adaptive"),
    ]
    angs = [i * 72 for i in range(5)]
    pos = [pt(cx, cy, R, a) for a in angs]

    # reinforcement edges (complete graph, faint)
    for i in range(5):
        for j in range(i + 1, 5):
            x0, y0 = pos[i]; x1, y1 = pos[j]
            svg.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                       f'stroke="#C9D6E6" stroke-width="2" opacity="0.6"/>')

    # perimeter cycle arrows (clockwise) between adjacent nodes
    half = math.degrees(math.asin(nr / R)) + 5
    for i in range(5):
        a0 = angs[i] + half
        a1 = angs[(i + 1) % 5] - half + (360 if (i + 1) % 5 == 0 else 0)
        x0, y0 = pt(cx, cy, R, a0); x1, y1 = pt(cx, cy, R, a1)
        svg.append(f'<path d="M {x0:.1f} {y0:.1f} A {R} {R} 0 0 1 {x1:.1f} {y1:.1f}" '
                   f'fill="none" stroke="{TEAL}" stroke-width="5" stroke-linecap="round" marker-end="url(#cyc)"/>')

    # center hub
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="104" fill="{NAVY}"/>')
    svg.append(txt(cx, cy - 6, "TRUST", 44, "#FFFFFF", "middle", "800", spacing="1"))
    svg.append(txt(cx, cy + 32, "five pillars", 19, "#AFC4E0", "middle", "400", italic=True, serif=True))

    # nodes
    for (letter, name, role), (x, y) in zip(pillars, pos):
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{nr}" fill="{PAPER}" stroke="{NAVY}" stroke-width="4"/>')
        svg.append(f'<circle cx="{x:.1f}" cy="{y-52:.1f}" r="36" fill="{TEAL_T}" stroke="{TEAL}" stroke-width="3"/>')
        svg.append(txt(x, y - 40, letter, 40, TEALD, "middle", "800", serif=True))
        svg.append(txt(x, y + 22, name, 26, INK, "middle", "700"))
        svg.append(txt(x, y + 54, role, 18, SUB, "middle", "400"))

    svg.append(txt(cx, H - 42, "Every edge is a reinforcement relationship; the arrows are the cycle that keeps it current.",
                   22, MUT, "middle", "400", serif=True, italic=True))
    svg.append('</svg>')
    return page(W, H, "".join(svg))


# ============================================================ Fig 5: Autonomy label
def label():
    W, H = 1560, 1528
    levels = ["L2", "L3", "L4", "L5"]
    active = "L4"
    con = [
        ("Automation level", "L4 — driverless within limits"),
        ("Where it drives (ODD)", "Daytime, mapped urban roads,<br>up to 60 km/h, clear or light rain"),
        ("Key limitations", "No highways · no heavy rain / snow ·<br>no unmapped areas · no night operation"),
        ("Driver must be ready to", "Nothing inside the ODD; take over<br>only on request to exit the ODD"),
    ]
    reg = [
        ("Disengagement rate", "1 per 12,400 km (rolling 90 days)"),
        ("Incident history", "P0: 0 · P1: 2 · P2: 14 (last 12 months)"),
        ("Detailed operating bounds", "Geofence v3.2 · 42 km² · speed ≤ 60 km/h ;<br>ODD suspends: visibility &lt; 100 m, flood alert"),
        ("Validation & audit", "Third-party certified · audited 2026-Q1"),
    ]

    def scale():
        cells = "".join(f'<div class="lvl {"on" if lv==active else ""}">{lv}</div>' for lv in levels)
        return f'<div class=scale><div class=scalelab>SAE level</div><div class=lvls>{cells}</div></div>'

    def rows(items):
        return "".join(f'<div class=row><div class=ic></div><div class=k>{k}</div>'
                       f'<div class=v>{v}</div></div>' for k, v in items)

    body = f"""
    <div class=card>
      <div class=head>
        <div><div class=eyebrow>STANDARDIZED DISCLOSURE</div>
          <div class="title serif">Autonomy Label</div>
          <div class=system>Sample system · urban robotaxi</div></div>
        <div class=badge>{active}</div>
      </div>
      {scale()}
      <div class=tier>
        <div class=tierhead><span class="rail t"></span>Consumer tier
          <span class=note>read in seconds</span></div>
        {rows(con)}
      </div>
      <div class="tier reg">
        <div class=tierhead><span class="rail n"></span>Regulator tier
          <span class=note>full disclosure</span></div>
        {rows(reg)}
      </div>
      <div class=foot>Read like an energy or nutrition label — the consumer tier for the public, the regulator tier for oversight.</div>
    </div>"""

    extra = f"""
    .card{{margin:34px;width:{W-68}px;border:2.5px solid {INK};border-radius:16px;overflow:hidden;background:{PAPER}}}
    .head{{display:flex;justify-content:space-between;align-items:center;background:{NAVY};color:#fff;padding:32px 40px}}
    .eyebrow{{font-size:19px;letter-spacing:4px;color:{TEAL};font-weight:800}}
    .title{{font-size:56px;font-weight:700;margin-top:4px;color:#fff}}
    .system{{font-size:22px;color:#B7C6DD;margin-top:8px;font-weight:500}}
    .badge{{background:{TEAL};color:#fff;font-size:64px;font-weight:800;border-radius:16px;
      padding:12px 34px;line-height:1;box-shadow:0 6px 0 {TEALD}}}
    .scale{{display:flex;align-items:center;gap:20px;padding:22px 40px;background:{PANEL};border-bottom:2px solid {LINE}}}
    .scalelab{{font-size:20px;font-weight:700;color:{SUB};letter-spacing:1px}}
    .lvls{{display:flex;gap:12px;flex:1}}
    .lvl{{flex:1;text-align:center;font-size:30px;font-weight:800;color:{MUT};background:#fff;
      border:2px solid {LINE};border-radius:10px;padding:12px 0}}
    .lvl.on{{color:#fff;background:{TEAL};border-color:{TEALD};box-shadow:0 4px 0 {TEALD};transform:scale(1.04)}}
    .tier{{padding:10px 40px 20px}}
    .tier.reg{{background:#FAFBFD;border-top:2px solid {LINE}}}
    .tierhead{{display:flex;align-items:center;font-size:27px;font-weight:800;color:{INK};margin:20px 0 10px}}
    .rail{{width:14px;height:30px;border-radius:4px;margin-right:16px}}
    .rail.t{{background:{TEAL}}} .rail.n{{background:{NAVY}}}
    .note{{margin-left:auto;font-size:18px;font-weight:700;color:{MUT};letter-spacing:1.5px;text-transform:uppercase}}
    .row{{display:flex;align-items:flex-start;padding:16px 0;border-bottom:1.5px solid {LINE}}}
    .row:last-child{{border-bottom:none}}
    .ic{{width:12px;height:12px;border-radius:50%;background:{LINE};margin:9px 20px 0 4px;flex:none}}
    .k{{width:34%;font-size:22px;font-weight:700;color:{SUB};padding-right:20px}}
    .v{{width:60%;font-size:23px;font-weight:600;color:{INK};line-height:1.4}}
    .foot{{padding:22px 40px 28px;font-size:20px;font-style:italic;color:{MUT};line-height:1.45;
      border-top:2px solid {LINE};font-family:{SERIF}}}
    """
    return page(W, H, body, extra)


figs = {"fig1_flywheel": flywheel(), "fig2_ringmap": ringmap(), "fig3_trustgap": trustgap(),
        "fig4_pentagon": pentagon(), "fig5_label": label()}
for name, html in figs.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
    print("wrote", name)
