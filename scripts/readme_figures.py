"""Generates the profile README's SVG figures in GitHub's own palette.

Each SVG carries both palettes and switches on prefers-color-scheme, with a
transparent background, so it sits on GitHub's page in either theme.

Usage: python3 scripts/readme_figures.py [<out-dir> [<preview-dir>]]

With no arguments it rewrites assets/*.svg. A preview dir also gets a
.light.svg and .dark.svg of each figure with the palette forced, for checking
both themes side by side. assets/apextracker-dashboard.png is a screenshot and
is not generated here.
"""
import math
import re
import sys
from pathlib import Path

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "assets"
PREVIEW = Path(sys.argv[2]) if len(sys.argv) > 2 else None

LIGHT = {
    "fg": "#1f2328", "muted": "#59636e", "border": "#d1d9e0", "subtle": "#f6f8fa",
    "canvas": "#ffffff", "neutral": "#818b98",
    "accent": "#0969da", "accent-bg": "#ddf4ff",
    "ok": "#1a7f37", "ok-bg": "#dafbe1",
    "warn": "#9a6700", "warn-bg": "#fff8c5",
    "danger": "#d1242f", "danger-bg": "#ffebe9",
}
DARK = {
    "fg": "#f0f6fc", "muted": "#9198a1", "border": "#3d444d", "subtle": "#151b23",
    "canvas": "#0d1117", "neutral": "#656c76",
    "accent": "#4493f8", "accent-bg": "#121d2f",
    "ok": "#3fb950", "ok-bg": "#12261e",
    "warn": "#d29922", "warn-bg": "#272115",
    "danger": "#f85149", "danger-bg": "#25171c",
}
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"


def css(force=None):
    def block(p):
        return "".join(f"--{k}:{v};" for k, v in p.items())
    rules = [f"svg{{{block(DARK if force == 'dark' else LIGHT)}}}"]
    if not force:
        rules.append(f"@media (prefers-color-scheme:dark){{svg{{{block(DARK)}}}}}")
    names = list(LIGHT)
    for n in names:
        rules.append(f".f-{n}{{fill:var(--{n})}}")
        rules.append(f".s-{n}{{stroke:var(--{n})}}")
    rules.append(f"text{{font-family:{SANS}}}")
    rules.append(f".mono{{font-family:{MONO}}}")
    rules.append(".n{fill:none}")
    return "<style>" + "".join(rules) + "</style>"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, s, size=14, fill="fg", weight=None, anchor=None, mono=False, ls=None, extra=""):
    a = [f'x="{x}"', f'y="{y}"', f'font-size="{size}"']
    cls = f"f-{fill}" + (" mono" if mono else "")
    a.append(f'class="{cls}"')
    if weight:
        a.append(f'font-weight="{weight}"')
    if anchor:
        a.append(f'text-anchor="{anchor}"')
    if ls:
        a.append(f'letter-spacing="{ls}"')
    return f"<text {' '.join(a)}{extra}>{esc(s)}</text>"


def R(x, y, w, h, fill="subtle", stroke="border", rx=6, sw=1, extra=""):
    cls = (f"f-{fill}" if fill else "n") + (f" s-{stroke}" if stroke else "")
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}" stroke-width="{sw}"{extra}/>'


def P(d, stroke="border", sw=1.5, fill=None, extra=""):
    cls = (f"f-{fill}" if fill else "n") + (f" s-{stroke}" if stroke else "")
    return f'<path d="{d}" class="{cls}" stroke-width="{sw}"{extra}/>'


def arrow(x1, y, x2, stroke="neutral", sw=1.5):
    """Horizontal arrow from x1 to x2 at y."""
    return (P(f"M{x1} {y} H{x2 - 1}", stroke, sw)
            + P(f"M{x2 - 6} {y - 4.5} L{x2} {y} L{x2 - 6} {y + 4.5}", stroke, sw,
                extra=' stroke-linecap="round" stroke-linejoin="round"'))


def fallback(markup):
    """Repeat the light palette as plain attributes, for renderers that drop <style>."""
    def attrs(m):
        out = []
        for c in m.group(1).split():
            if c == "n":
                out.append('fill="none"')
            elif c == "mono":
                out.append(f'font-family="{MONO}"')
            elif c[:2] in ("f-", "s-") and c[2:] in LIGHT:
                out.append(f'{"fill" if c[0] == "f" else "stroke"}="{LIGHT[c[2:]]}"')
        return m.group(0) + (" " + " ".join(out) if out else "")
    return re.sub(r'class="([^"]*)"', attrs, markup)


def svg(w, h, title, desc, body, force=None):
    body = [fallback("".join(body))]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d" font-family="{SANS}">'
            f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>'
            f'{css(force)}{"".join(body)}</svg>\n')


def write(name, w, h, title, desc, body):
    (OUT / name).write_text(svg(w, h, title, desc, body))
    if PREVIEW:
        (PREVIEW / name.replace(".svg", ".light.svg")).write_text(svg(w, h, title, desc, body, "light"))
        (PREVIEW / name.replace(".svg", ".dark.svg")).write_text(svg(w, h, title, desc, body, "dark"))


# ---------------------------------------------------------------- header
def header():
    b = []
    W, H = 1200, 200
    b.append(T(4, 34, "SOFTWARE  ·  SYSTEMS  ·  AI", 14, "muted", 600, mono=True, ls=2))
    b.append(T(0, 106, "Aaditya Desai", 68, "fg", 700, ls=-1.5))
    b.append(T(4, 146, "Computer Engineering at San José State University, class of 2028", 21, "muted"))
    # status pill, in the style of a GitHub label
    b.append(R(2, 162.5, 356, 35, "ok-bg", "ok", rx=17.5))
    b.append(f'<circle cx="23" cy="180" r="5" class="f-ok"/>')
    b.append(T(39, 186, "Open to Summer 2027 internships", 17, "ok", 600))
    # trace motif, kept from the earlier header
    g = ['<g transform="translate(0 -58)">']
    g.append('<g class="n s-border" stroke-width="2">'
             '<path d="M858 104 H926 V72 H1028"/><path d="M858 158 H902 V198 H1032 V244 H1106"/>'
             '<path d="M926 104 V142 H1070"/><path d="M1028 72 V112 H1110"/><path d="M1110 112 V170 H1160"/></g>')
    g.append('<g class="f-canvas s-accent" stroke-width="3">')
    for cx, cy in [(858, 104), (858, 158), (926, 104), (1028, 72), (1070, 142), (1032, 198), (1106, 244), (1160, 170)]:
        g.append(f'<circle cx="{cx}" cy="{cy}" r="6.5"/>')
    g.append("</g>")
    g.append('<circle cx="984" cy="158" r="50" class="f-fg"/>')
    g.append(T(984, 173, "AD", 42, "canvas", 700, "middle", ls=-1))
    g.append("</g>")
    b.append("".join(g))
    write("profile-header.svg", W, H, "Aaditya Desai",
          "Computer Engineering student at San José State University, class of 2028, open to Summer 2027 internships.", b)


# ---------------------------------------------------------------- rung ladder
def rung():
    W, H = 960, 348
    rows = [  # id, name, speedup over the tree-walker on fib, step over the rung below
        ("09", "+ ARM64 JIT", 38.84, "4.54×", "jit"),
        ("08", "+ constant folding", 8.55, "1.02×", ""),
        ("07", "+ inline caching", 8.41, "1.46×", ""),
        ("06", "+ superinstructions", 5.76, "1.01×", ""),
        ("05", "Register VM", 5.71, "1.41×", ""),
        ("04", "+ NaN-boxed values", 4.06, "0.90×", "slow"),
        ("03", "+ computed-goto dispatch", 4.53, "1.19×", ""),
        ("02", "Stack VM", 3.80, "3.80×", ""),
        ("01", "Tree-walker", 1.00, "base", ""),
    ]
    b = []
    x0, x1 = 300, 700          # bar track, log scale 1x..40x
    top, rh = 44, 29

    def bx(v):
        return x0 + (x1 - x0) * math.log(v) / math.log(40)

    b.append(T(0, 18, "RUNG", 12, "muted", 600, mono=True, ls=1.2))
    b.append(T(x0, 18, "SPEED ON fib, LOG SCALE", 12, "muted", 600, mono=True, ls=1.2))
    b.append(T(826, 18, "VS TREE-WALKER", 12, "muted", 600, "end", True, 1.2))
    b.append(T(960, 18, "VS RUNG BELOW", 12, "muted", 600, "end", True, 1.2))
    for v in (1, 2, 5, 10, 20, 40):
        x = round(bx(v), 1)
        b.append(P(f"M{x} {top - 6} V{top + rh * len(rows)}", "border", 1))
        b.append(T(x, top - 11, f"{v}×", 11.5, "muted", anchor="middle", mono=True))
    for i, (num, name, v, step, kind) in enumerate(rows):
        y = top + i * rh
        b.append(P(f"M0 {y} H{W}", "border", 1))
        cy = y + rh / 2
        strong = kind == "jit"
        b.append(T(0, cy + 5, num, 13, "accent" if strong else "muted", 600, mono=True))
        b.append(T(34, cy + 5, name, 15, "fg", 600 if strong else None))
        color = {"jit": "accent", "slow": "danger"}.get(kind, "neutral")
        w = max(3, round(bx(v) - x0, 1))
        b.append(R(x0, y + 7.5, w, rh - 15, color, None, rx=2))
        b.append(T(826, cy + 5, f"{v:.2f}×", 15, "fg", 700 if strong else None, "end", True))
        sc = {"slow": "danger"}.get(kind, "fg" if strong else "muted")
        b.append(T(960, cy + 5, ("▼ " if kind == "slow" else "") + step, 14, sc, 600 if kind else None, "end", True))
    yb = top + rh * len(rows)
    b.append(P(f"M0 {yb} H{W}", "border", 1))
    fy = yb + 27
    b.append(R(0, fy - 11, 12, 12, "accent", None, rx=2))
    b.append(T(19, fy, "native ARM64 code", 13.5, "muted"))
    b.append(R(160, fy - 11, 12, 12, "danger", None, rx=2))
    b.append(T(179, fy, "slower than the rung below", 13.5, "muted"))
    b.append(T(960, fy, "Each rung is the one below plus one change. Apple M1 Pro, median per-call time.", 13.5, "muted", anchor="end"))
    write("rung-ladder.svg", W, H, "Rung's optimization ladder on the fib benchmark",
          "Nine rungs from a tree-walking interpreter to a baseline ARM64 JIT, each one the rung below plus one change. "
          "Speed on fib relative to the tree-walker: stack VM 3.80x, computed goto 4.53x, NaN-boxing 4.06x (slower than the rung below), "
          "register VM 5.71x, superinstructions 5.76x, inline caching 8.41x, constant folding 8.55x, ARM64 JIT 38.84x.", b)


# ---------------------------------------------------------------- visionassist
def vision():
    W, H = 960, 356
    b = []
    FT, F, FW, FH, HZ, CAM = 0.3048, 900, 720, 1280, 100, 1.6
    objs = [  # cls, height m, width m, tier, conf, lateral ft, forward ft (the devsite figure's scene)
        ("chair", 0.9, 0.5, "High", 0.91, -0.9, 4.4),
        ("person", 1.7, 0.5, "Medium", 0.88, 1.7, 7.8),
        ("cup", 0.12, 0.08, "Low", 0.62, 0.7, 4.95),
        ("dog", 0.55, 0.7, "Medium", 0.79, -1.6, 11.9),
    ]
    col = {"chair": "danger", "person": "warn", "dog": "ok", "cup": "neutral"}

    def head(x, n, title, sub):
        b.append(T(x, 16, f"{n}  {title}", 12, "muted", 600, mono=True, ls=1.2))
        b.append(T(x, 37, sub, 14, "fg"))

    # 1. camera frame ------------------------------------------------------
    head(0, "1", "CAMERA FRAME", "YOLOv8n, about 200 ms a frame")
    fx, fy, k = 26, 56, 164 / FW
    fw, fh = 164, round(FH * k, 1)
    b.append(f'<clipPath id="fr"><rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="4"/></clipPath>')
    b.append(R(fx, fy, fw, fh, "subtle", None, rx=4))
    g = ['<g clip-path="url(#fr)">']
    hy = fy + HZ * k
    g.append(P(f"M{fx} {hy:.1f} H{fx + fw}", "border", 1, extra=' stroke-dasharray="4 4"'))
    boxes = {}
    for cls, Hm, Wm, tier, conf, x, y in sorted(objs, key=lambda o: -math.hypot(o[5], o[6])):
        d = math.hypot(x, y)
        dm = d * FT
        cx = FW / 2 + F * math.tan(math.atan2(x, y))
        w = Wm * F / dm
        base = HZ + CAM * F / dm
        topp = base - Hm * F / dm
        est = (Hm * F / (min(base, FH) - max(topp, 0))) / FT
        boxes[cls] = (d, est)
        X, Y, Wd, Hd = fx + (cx - w / 2) * k, fy + topp * k, w * k, (base - topp) * k
        c = col[cls]
        g.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{Wd:.1f}" height="{Hd:.1f}" class="f-{c}" fill-opacity="0.14" stroke="none"/>')
        g.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{Wd:.1f}" height="{Hd:.1f}" class="n s-{c}" stroke-width="{2 if cls == "chair" else 1.5}"/>')
        lab = f"{cls} {conf:.2f}"
        if cls == "chair":
            g.append(T(round(X + 4, 1), round(Y + 14, 1), lab, 10.5, c, 600, mono=True))
        elif cls == "dog":
            g.append(T(round(X, 1), round(Y - 5, 1), lab, 10.5, c, 600, mono=True))
        elif cls == "person":
            g.append(T(fx + fw - 5, round(Y + Hd + 14, 1), lab, 10.5, c, 600, "end", True))
        else:
            g.append(T(fx + fw - 5, round(Y - 6, 1), lab, 10.5, c, 600, "end", True))
    g.append("</g>")
    b.append("".join(g))
    b.append(R(fx, fy, fw, fh, None, "border", rx=4, sw=1.5))
    b.append(T(fx + fw + 6, hy + 4, "horizon", 11, "muted"))

    # 2. top view ----------------------------------------------------------
    ox, cy0, s = 262, 204, 31          # wearer position, px per foot
    head(ox - 16, "2", "DISTANCE AND RISK", "Distance from box height. Riskiest object first, then nearest.")
    ytop, ybot = cy0 - 3 * s, cy0 + 3 * s   # corridor walls, 6 ft apart
    xend = ox + 14 * s
    b.append(f'<clipPath id="co"><rect x="{ox}" y="{ytop}" width="{xend - ox}" height="{ybot - ytop}"/></clipPath>')
    g = ['<g clip-path="url(#co)">']
    g.append(f'<rect x="{ox}" y="{ytop}" width="{xend - ox}" height="{ybot - ytop}" class="f-ok-bg"/>')
    g.append(f'<circle cx="{ox}" cy="{cy0}" r="{9 * s}" class="f-warn-bg"/>')
    g.append(f'<circle cx="{ox}" cy="{cy0}" r="{6 * s}" class="f-danger-bg"/>')
    g.append(f'<circle cx="{ox}" cy="{cy0}" r="{9 * s}" class="n s-warn" stroke-width="1.5" stroke-dasharray="5 5"/>')
    g.append(f'<circle cx="{ox}" cy="{cy0}" r="{6 * s}" class="n s-danger" stroke-width="1.5" stroke-dasharray="5 5"/>')
    half = math.atan(FW / 2 / F)
    ex = xend + 40
    dy = (ex - ox) * math.tan(half)
    g.append(P(f"M{ox} {cy0} L{ex} {cy0 - dy:.1f} M{ox} {cy0} L{ex} {cy0 + dy:.1f}", "accent", 1.2))
    g.append("</g>")
    b.append("".join(g))
    b.append(P(f"M{ox} {ytop} H{xend} M{ox} {ybot} H{xend}", "fg", 2))
    # zone names above the corridor
    for label, rng, c, xa in (("WARNING", "under 6 ft", "danger", ox + 2.6 * s), ("CAUTION", "6 to 9 ft", "warn", ox + 6.85 * s), ("SAFE", "over 9 ft", "ok", ox + 11.2 * s)):
        b.append(T(round(xa, 1), ytop - 24, label, 11.5, c, 700, "middle", True, 1))
        b.append(T(round(xa, 1), ytop - 9, rng, 12, "muted", anchor="middle"))
    # distance axis
    for ft in range(0, 15, 2):
        x = ox + ft * s
        b.append(P(f"M{x} {ybot} V{ybot + 6}", "fg", 1.5))
        b.append(T(x, ybot + 21, f"{ft}" + (" ft" if ft == 14 else ""), 12, "muted", anchor="middle", mono=True))
    # wearer
    b.append(f'<circle cx="{ox}" cy="{cy0}" r="9" class="f-canvas s-fg" stroke-width="2"/>')
    b.append(P(f"M{ox + 9} {cy0 - 5} L{ox + 17} {cy0} L{ox + 9} {cy0 + 5} Z", "fg", 1, "fg"))
    b.append(T(ox - 15, cy0 + 4, "wearer", 12, "muted", anchor="end"))
    # objects (forward = right, lateral ft positive = down)
    for cls, Hm, Wm, tier, conf, x, y in objs:
        px, py = ox + y * s, cy0 + x * s
        c = col[cls]
        d, est = boxes[cls]
        if cls == "chair":
            b.append(P(f"M{ox + 17} {cy0} L{px - 13:.1f} {py + 3:.1f}", "danger", 1.5, extra=' stroke-dasharray="3 4"'))
            b.append(f'<rect x="{px - 12:.1f}" y="{py - 12:.1f}" width="24" height="24" rx="2" class="f-canvas s-danger" stroke-width="2.5"/>')
            b.append(P(f"M{px - 12:.1f} {py - 5:.1f} H{px + 12:.1f}", "danger", 2))
        elif cls == "person":
            b.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="7" ry="13" class="f-canvas s-warn" stroke-width="2"/>')
            b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" class="f-canvas s-warn" stroke-width="2"/>')
        elif cls == "dog":
            b.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="13" ry="6" class="f-canvas s-ok" stroke-width="2"/>')
            b.append(f'<circle cx="{px - 14:.1f}" cy="{py:.1f}" r="4" class="f-canvas s-ok" stroke-width="2"/>')
        else:
            b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" class="f-canvas s-neutral" stroke-width="2"/>')
            b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="1.6" class="f-neutral"/>')
        name, dist = cls.upper(), f"{est:.1f} ft" + (", low risk" if cls == "cup" else "")
        wn, wd = len(name) * 7.7 + 2, len(dist) * 7.0
        cwid = round(wn + wd + 22, 1)
        chx, chy = {"chair": (px - 104, py - 52), "cup": (px + 13, py - 10), "person": (px + 16, py - 10), "dog": (px - 27 - cwid, py - 10)}[cls]
        b.append(R(round(chx, 1), round(chy, 1), cwid, 20, "canvas", c, rx=4))
        b.append(T(round(chx + 8, 1), round(chy + 14.5, 1), name, 11.5, c, 700, mono=True, ls=0.6))
        b.append(T(round(chx + 8 + wn + 6, 1), round(chy + 14.5, 1), dist, 11.5, "muted", mono=True))

    # 3. speech ------------------------------------------------------------
    sx = 746
    head(sx, "3", "SPEECH", "Piper, offline, to earbuds")
    b.append(R(sx, 78, 214, 92, "danger-bg", "danger", rx=8, sw=1.5))
    b.append(P(f"M{sx} 116 l-10 8 l10 8", "danger", 1.5, "danger-bg", extra=' stroke-linejoin="round"'))
    b.append(P(f"M{sx} 117.5 V130.5", "danger-bg", 2.5))
    b.append(T(sx + 18, 115, "“Stop. Chair,", 21, "fg", 700))
    b.append(T(sx + 18, 143, "2 steps ahead.”", 21, "fg", 700))
    lines = ["One announcement at a time,", "in feet and steps.", "", "Under 6 ft it starts with “stop”.", "The cup is low risk, so it stays", "silent. Past 9 ft, everything does."]
    for i, ln in enumerate(lines):
        if ln:
            b.append(T(sx, 198 + i * 19, ln, 13.5, "muted"))
    b.append(T(sx, ybot + 21, "Simulated scene", 12, "muted", mono=True))
    write("visionassist-scene.svg", W, H, "How VisionAssist turns a camera frame into one spoken warning",
          "A simulated scene in three steps. One: the camera frame, with YOLOv8n boxes around a chair, a cup, a person and a dog. "
          "Two: a top view with the wearer on the left and three zones by estimated distance: warning under 6 feet, caution from 6 to 9 feet, safe over 9 feet. "
          "The chair at 4.5 feet is the highest-risk object. Three: the device says: Stop. Chair, 2 steps ahead.", b)


# ---------------------------------------------------------------- apextracker
def apex():
    W, H = 760, 412
    b = []

    def cap(x, y, s, anchor=None):
        b.append(T(x, y, s, 12, "muted", 600, anchor, True, 1.2))

    # trackers
    cap(0, 14, "SIX TRACKERS")
    tr = ["Budget", "Study timer", "Screen time", "Reminders", "Notes", "Reading queue"]
    ty0, th, tg = 28, 34, 8
    tw = 168
    pos = {}
    for i, name in enumerate(tr):
        y = ty0 + i * (th + tg)
        pos[name] = y + th / 2
        b.append(R(0.5, y, tw, th, "subtle", "border"))
        b.append(T(14, y + 22, name, 15, "fg", 600))
    # goals
    gx, gw = 258, 232
    cap(gx, 14, "GOALS, CHECKED AUTOMATICALLY")
    goals = [("Screen time under 6h", "Screen time", True), ("Study 2h", "Study timer", False), ("Read 1+ papers", "Reading queue", True)]
    gy0, gh, gg = 28, 52, 12
    gpos = []
    for i, (name, src, met) in enumerate(goals):
        y = gy0 + i * (gh + gg)
        gpos.append(y + gh / 2)
        b.append(R(gx, y, gw, gh, "ok-bg" if met else "subtle", "ok" if met else "border"))
        if met:
            b.append(f'<circle cx="{gx + 22}" cy="{y + gh / 2}" r="9" class="f-ok"/>')
            b.append(P(f"M{gx + 17.5} {y + gh / 2 + 0.5} l3.2 3.2 l6 -6.6", "canvas", 2, extra=' stroke-linecap="round" stroke-linejoin="round"'))
        else:
            b.append(f'<circle cx="{gx + 22}" cy="{y + gh / 2}" r="8.5" class="n s-neutral" stroke-width="1.5"/>')
        b.append(T(gx + 42, y + 22, name, 15, "fg", 600))
        b.append(T(gx + 42, y + 40, ("Met, read from " if met else "Open, read from ") + src.lower(), 12.5, "ok" if met else "muted"))
    # manual goal
    my = gy0 + 3 * (gh + gg)
    b.append(R(gx, my, gw, 40, None, "border", extra=' stroke-dasharray="4 4"'))
    b.append(R(gx + 14, my + 12, 16, 16, None, "neutral", rx=3, sw=1.5))
    b.append(T(gx + 42, my + 25, "Workout, ticked by hand", 14, "muted"))
    # tracker -> goal connectors
    for (name, src, met), gy in zip(goals, gpos):
        y1 = pos[src]
        xm = (tw + gx) / 2 + 4
        b.append(P(f"M{tw + 1} {y1} C{xm} {y1} {xm} {gy} {gx - 7} {gy}", "ok" if met else "neutral", 1.5))
        b.append(P(f"M{gx - 7} {gy - 4.5} L{gx - 1} {gy} L{gx - 7} {gy + 4.5}", "ok" if met else "neutral", 1.5, extra=' stroke-linecap="round" stroke-linejoin="round"'))
    # day score + heatmap
    hx = 582
    cap(hx, 14, "ONE SCORE A DAY")
    b.append(T(hx, 62, "2 / 4", 34, "fg", 700, mono=True))
    b.append(T(hx, 84, "goals met today", 13.5, "muted"))
    ba, bb = gy0 + 6, gy0 + 3 * (gh + gg) + 34
    b.append(P(f"M{gx + gw + 8} {ba} h7 V{bb} h-7", "neutral", 1.5))
    b.append(arrow(gx + gw + 15, (ba + bb) / 2, hx - 10))
    cell, gap = 20, 4
    shades = [  # share of goals met, by week, invented only as texture and labelled as such
        [2, 2, 3, 1, 2, 0, 1], [3, 4, 2, 2, 3, 1, 0], [1, 2, 2, 4, 3, 2, 2], [2, 3, 1, 2, 2, None, None]]
    hy0 = 122
    for j, ch in enumerate("SMTWTFS"):
        b.append(T(hx + j * (cell + gap) + cell / 2, hy0 - 8, ch, 11, "muted", anchor="middle", mono=True))
    for r, row in enumerate(shades):
        for c, v in enumerate(row):
            x, y = hx + c * (cell + gap), hy0 + r * (cell + gap)
            if v is None:
                b.append(R(x, y, cell, cell, "subtle", "border", rx=3))
                continue
            op = (0, 0.25, 0.5, 0.75, 1)[v]
            b.append(R(x, y, cell, cell, "subtle", "border", rx=3))
            if op:
                b.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" class="f-ok" fill-opacity="{op}"/>')
    tx, ty = hx + 4 * (cell + gap), hy0 + 3 * (cell + gap)
    b.append(R(tx - 2.5, ty - 2.5, cell + 5, cell + 5, None, "fg", rx=5, sw=1.5))
    b.append(T(hx, hy0 + 4 * (cell + gap) + 14, "Each day is shaded by the", 12.5, "muted"))
    b.append(T(hx, hy0 + 4 * (cell + gap) + 31, "share of its goals met.", 12.5, "muted"))

    # storage layer
    sy = 296
    cap(0, sy, "ON THE PHONE, WORKS OFFLINE")
    cap(W, sy, "OPTIONAL", "end")
    by, bh = sy + 14, 76
    cols = [("Room database", "The single source of truth,", "15 hand-written migrations"),
            ("Encrypted at rest", "SQLCipher, with the key in", "the Android Keystore"),
            ("Five home widgets", "Start the study timer or", "add an expense from home")]
    cw, cg = 180, 10
    for i, (h1, l1, l2) in enumerate(cols):
        x = 0.5 + i * (cw + cg)
        b.append(R(x, by, cw, bh, "subtle", "border"))
        b.append(T(x + 13, by + 25, h1, 14.5, "fg", 600))
        b.append(T(x + 13, by + 45, l1, 12.5, "muted"))
        b.append(T(x + 13, by + 62, l2, 12.5, "muted"))
    x = 0.5 + 3 * (cw + cg) + 14
    b.append(P(f"M{x - 12.5} {by + bh / 2} H{x - 2}", "neutral", 1.5, extra=' stroke-dasharray="3 3"'))
    b.append(R(x, by, W - x - 0.5, bh, None, "border", extra=' stroke-dasharray="4 4"'))
    b.append(T(x + 13, by + 25, "Cloud sync", 14.5, "fg", 600))
    b.append(T(x + 13, by + 45, "Firebase Auth", 12.5, "muted"))
    b.append(T(x + 13, by + 62, "and Firestore", 12.5, "muted"))
    b.append(T(W, by + bh + 20, "Heatmap shading is illustrative", 12, "muted", anchor="end", mono=True))
    write("apextracker-map.svg", W, H, "How ApexTracker turns six trackers into one score a day",
          "Six trackers (budget, study timer, screen time, reminders, notes, reading queue) feed goals that are checked automatically, "
          "such as screen time under 6 hours, study 2 hours, and read one or more papers. The share of goals met shades each day on a heatmap. "
          "Everything runs on the phone: a Room database with 15 hand-written migrations, encrypted at rest with SQLCipher under an Android Keystore key, "
          "and 5 home-screen widgets. Cloud sync through Firebase is optional.", b)


# ---------------------------------------------------------------- oss scout
def scout():
    W, H = 960, 246
    b = []
    stages = [("01", "SCAN", "Find issues", ["Nightly GitHub Action.", "Plain Python, no AI."], "muted"),
              ("02", "PREPARE", "Draft one fix", ["A Claude routine drafts", "one tested fix a night."], "muted"),
              ("03", "REVIEW", "I decide", ["Private dashboard.", "I read it and choose."], "accent"),
              ("04", "ACT", "Open the PR", ["Re-checks the issue and", "the project's rules first."], "warn")]
    cw, cy, ch = 204, 76, 118
    xs = [0, 240, 480, 756]

    def bracket(xa, xb, label, sub, color):
        b.append(P(f"M{xa + 1} 62 V54 H{xb - 1} V62", color, 1.5))
        m = (xa + xb) / 2
        b.append(T(m, 22, label, 12, color, 700, "middle", True, 1.4))
        b.append(T(m, 43, sub, 13.5, "muted", anchor="middle"))

    bracket(xs[0], xs[1] + cw, "UNATTENDED", "No write token. A guard hook blocks every GitHub write.", "muted")
    bracket(xs[2], xs[2] + cw, "ME", "A human in the loop", "accent")
    bracket(xs[3], xs[3] + cw, "WRITE TOKEN", "Runs only on my tap", "warn")
    for x, (num, tag, title, lines, color) in zip(xs, stages):
        hot = color != "muted"
        b.append(R(x + 0.5, cy, cw - 1, ch, f"{color}-bg" if hot else "subtle", color if hot else "border", rx=8))
        b.append(T(x + 16, cy + 26, f"{num}  {tag}", 12, color, 700, mono=True, ls=1.4))
        b.append(T(x + 16, cy + 56, title, 21, "fg", 600))
        for i, ln in enumerate(lines):
            b.append(T(x + 16, cy + 80 + i * 18, ln, 13.5, "muted"))
    my = cy + ch / 2
    b.append(arrow(xs[0] + cw + 9, my, xs[1] - 8))
    b.append(arrow(xs[1] + cw + 9, my, xs[2] - 8))
    # the one tap, between review and act
    b.append(arrow(xs[2] + cw + 9, my, xs[3] - 8, "ok", 2))
    px = (xs[2] + cw + xs[3]) / 2
    b.append(R(px - 31, my - 34, 62, 22, "ok-bg", "ok", rx=11))
    b.append(T(px, my - 18.5, "ONE TAP", 11, "ok", 700, "middle", True, 0.6))
    b.append(T(0, H - 8, "Status on the public page is read back from GitHub, never self-reported.", 13.5, "muted"))
    write("oss-scout-flow.svg", W, H, "How OSS Scout keeps a human in charge",
          "Four stages: scan, prepare, review, act. Scan and prepare run unattended and cannot write to GitHub. "
          "Only the act stage holds the write token, and it starts only when Aaditya taps approve.", b)


# ---------------------------------------------------------------- alta
def alta():
    W, H = 960, 236
    b = []
    stages = [("01", "STUDENT'S BOARD", "Four probes", ["Color-coded probes read", "the real circuit's voltages."], "muted"),
              ("02", "PROBE POD, MY PART", "Bare-metal C", ["Arduino Uno, no libraries.", "≈1,200 samples a second."], "accent"),
              ("03", "AGENT", "Measure first", ["Claude Opus 5.5 with tools", "to probe, read, and diagnose."], "muted"),
              ("04", "VOICE", "Talks it through", ["Cartesia speech. First words", "in a median 2.57 s."], "muted")]
    cw, gap, ch = 216, 32, 112
    for i, (num, tag, title, lines, color) in enumerate(stages):
        x = i * (cw + gap)
        hot = color != "muted"
        b.append(R(x + 0.5, 0.5, cw - 1, ch, f"{color}-bg" if hot else "subtle", color if hot else "border", rx=8))
        b.append(T(x + 16, 25, f"{num}  {tag}", 12, color, 700, mono=True, ls=1.2))
        b.append(T(x + 16, 54, title, 21, "fg", 600))
        for j, ln in enumerate(lines):
            b.append(T(x + 16, 78 + j * 18, ln, 13.5, "muted"))
        if i:
            b.append(arrow(x - gap + 7, ch / 2, x - 6))
    # example exchange
    y0 = 150
    b.append(T(0, y0 - 8, "AN EXCHANGE, READINGS SIMULATED", 12, "muted", 600, mono=True, ls=1.2))
    eh = 76

    def reading(x, w, volts, color, note):
        b.append(R(x + 0.5, y0 + 0.5, w - 1, eh, f"{color}-bg", color, rx=8))
        b.append(f'<circle cx="{x + 21}" cy="{y0 + 21}" r="5" class="f-warn"/>')
        b.append(T(x + 33, y0 + 25.5, "YELLOW PROBE", 11.5, "muted", 700, mono=True, ls=1))
        b.append(T(x + 16, y0 + 59, volts, 26, color, 700, mono=True))
        b.append(T(x + 122, y0 + 51, note[0], 12.5, "muted"))
        b.append(T(x + 122, y0 + 66, note[1], 12.5, "muted"))

    reading(0, 236, "5.01 V", "danger", ("expected", "about 2 V"))
    b.append(arrow(243, y0 + eh / 2, 262))
    bx, bw = 268, 398
    b.append(R(bx + 0.5, y0 + 0.5, bw - 1, eh, "subtle", "border", rx=8))
    b.append(T(bx + 16, y0 + 25.5, "ALTA", 11.5, "accent", 700, mono=True, ls=1))
    b.append(T(bx + 16, y0 + 48, "“Yellow reads 5.01 V. You expected about 2.", 15, "fg", 600))
    b.append(T(bx + 16, y0 + 67, "What's between the rail and this row?”", 15, "fg", 600))
    b.append(arrow(bx + bw + 7, y0 + eh / 2, 718, "ok", 2))
    b.append(T((bx + bw + 718) / 2, y0 + eh / 2 - 9, "student", 11.5, "muted", anchor="middle"))
    b.append(T((bx + bw + 718) / 2, y0 + eh / 2 + 19, "fixes it", 11.5, "muted", anchor="middle"))
    reading(724, 236, "2.01 V", "ok", ("confirmed, no", "button press"))
    write("alta-bench.svg", W, H, "How Alta finds a fault on a real breadboard",
          "Four stages: probes on the student's board, a probe pod running bare-metal C on an Arduino Uno at 1,200 samples a second, "
          "a Claude Opus 5.5 agent that measures before it diagnoses, and Cartesia voice with first words in a median 2.57 seconds. "
          "Below, a simulated exchange: the yellow probe reads 5.01 volts where about 2 was expected, Alta asks what is between the rail and this row, "
          "the student fixes it, and the probe reads 2.01 volts, confirmed with no button press.", b)


for fn in (header, rung, alta, vision, apex, scout):
    fn()
print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
