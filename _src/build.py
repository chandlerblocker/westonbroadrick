#!/usr/bin/env python3
"""
Builds the Weston Broadrick Studio website.

Everything the site says lives in the PROJECTS list and the copy blocks
below. Edit those, then run:   python3 _src/build.py
It rewrites every .html page. Styles are in css/site.css, behavior in js/site.js.

Page addresses match the old Squarespace site (/projects/pala, /contact, ...)
so existing links and Google results keep working.
"""
import json
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.westonbroadrick.com"
EMAIL = "weston@westonbroadrick.com"
PHONE = "602.628.1132"
PHONE_LINK = "+16026281132"
YEAR = "2026"
IMAGES = json.load(open(os.path.join(ROOT, "images.json")))

# ---------------------------------------------------------------------------
# Projects, in the order they appear on the Projects page.
# Each page ends with its header photo repeated full width, unless "repeat_hero": False.
# "seo" = the description Google and link previews show (not visible on the page, keep under 160 characters).
# gallery rows:  ("two", a, b)      two portraits side by side
#                ("offset", a, b)   tall photo + wide photo, staggered
#                ("full", a)        one photo, full width
#                ("inset", a)       one photo, full width with side margins
#                ("narrow", a)      one tall photo, centered
#                ("full-float", a, (b, "pos-tr"), (c, "pos-bl"))  full-width a, with round
#                                   photos floating on top (tr = top right, bl = bottom left)
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "pala", "seo": "Pa\u2019La, Phoenix. A wood-fired restaurant interior by Weston Broadrick Studio: red octopus murals, brass lamps and layered lounge seating.", "name": "Pa’La", "sector": "Restaurant", "location": "Phoenix, Arizona",
        "hero": "pala-01", "tile": "pala-01", "repeat_hero": False,
        "lead": "",
        "body": "",
        "gallery": [
            ("offset", "pala-02", "pala-04"),
            ("full-float", "pala-05", ("pala-07", "pos-tr inside big"), ("pala-08", "pos-bl inside big")),
            ("two", "pala-lounge", "pala-03"),
            ("full", "pala-01"),
            ("full", "pala-06"),
        ],
    },
    {
        "slug": "fetacowboy", "seo": "Feta Cowboy, Tempe. A restaurant interior by Weston Broadrick Studio: hand-painted cowboy mural, cowhide seating and a sculptural branch chandelier.", "name": "Feta Cowboy", "sector": "Restaurant", "location": "Tempe, Arizona",
        "hero": "feta-04", "tile": "feta-cover",
        "lead": "", "body": "",
        "gallery": [
            ("two", "feta-cover", "feta-02"),
            ("full-float", "feta-01", ("feta-03", "pos-tr m-br")),
        ],
    },
    {
        "slug": "pita-jungle", "seo": "Pita Jungle Arcadia, Phoenix. A restaurant interior by Weston Broadrick Studio: sculptural dome pendants, deep green walls and a painted mural.", "name": "Pita Jungle", "sector": "Restaurant", "location": "Arcadia, Phoenix",
        "hero": "pita-02", "tile": "pita-02", "repeat_hero": False,
        "lead": "", "body": "",
        "gallery": [
            ("offset", "pita-01", "pita-02"),
        ],
    },
    {
        "slug": "residential", "seo": "Residential interiors by Weston Broadrick Studio. Layered, collected rooms of leather, reclaimed wood, gallery walls and rich textiles.", "name": "Residential", "sector": "Residential", "location": "Arizona",
        "hero": "res-03", "tile": "res-03", "hide_sector": True,
        "lead": "", "body": "",
        "gallery": [
            ("two", "res-01", "res-02"),
            ("offset", "res-04", "res-09"),
            ("two", "res-05", "res-06"),
            ("two", "res-07", "res-08"),
        ],
    },
    {
        "slug": "nonprofit", "seo": "The Boho Beach House: a coastal-inspired playhouse designed and donated by Weston Broadrick Studio for PANDA\u2019s annual fundraiser.", "name": "Nonprofit", "sector": "Nonprofit", "location": "Phoenix, Arizona",
        "hero": "np-01", "tile": "np-01", "hide_sector": True, "repeat_hero": False,
        "subtitle": "The Boho Beach House",
        "lead": "The Boho Beach House is a coastal-inspired playhouse created in support of PANDA and its annual fundraising efforts.",
        "body": "Designed and donated by the studio, and realized in collaboration with Sonora West Development and PHX Architecture, the project reflects a balance of playfulness and considered design.",
        "gallery": [
            ("two", "np-01", "np-02"),
        ],
    },
]

FIRST = PROJECTS[0]["slug"]  # where "Projects" links go

# Order on the home page (matches the current site)
HOME_ORDER = ["pala", "fetacowboy", "pita-jungle", "residential", "nonprofit"]

# Photo descriptions, read aloud by screen readers and used by Google Images
ALT = {
    "pala-01": "Red octopus mural spanning the bar ceiling at Pa’La",
    "pala-02": "Lounge seating against a slatted wood wall at Pa’La",
    "pala-03": "Brass table lamp in front of red octopus artwork at Pa’La",
    "pala-04": "White lounge chairs beneath an exposed steel ceiling at Pa’La",
    "pala-05": "High-top tables along floor-to-ceiling windows at Pa’La",
    "pala-06": "Dining room with bistro chairs and framed art at Pa’La",
    "pala-07": "Dining room with iron chandeliers and an open stair at Pa’La",
    "pala-08": "Wood-fired kitchen counter under globe pendants at Pa’La",
    "pala-lounge": "Low banquette lounge with warm pendant lighting at Pa’La",
    "feta-cover": "Long dining room with banquette and dome pendants at Feta Cowboy",
    "feta-01": "Hand-painted cowboy mural over the dining room at Feta Cowboy",
    "feta-02": "Cowhide-upholstered chairs at navy tables, Feta Cowboy",
    "feta-03": "Ceramic salt and pepper shakers with a cowboy illustration",
    "feta-04": "Sculptural branch chandelier framed in light at Feta Cowboy",
    "pita-01": "Dining room with pendant lighting at Pita Jungle Arcadia",
    "pita-02": "Bar with black dome pendants and a painted mural at Pita Jungle Arcadia",
    "res-01": "Living room with a leather chair and a reclaimed wood table",
    "res-02": "Library shelves with a table lamp and collected objects",
    "res-03": "Entry hall with staircase, red runner, and wood console",
    "res-04": "Living room with built-in shelving and leather club chairs",
    "res-05": "Game room with a billiards table and gallery wall",
    "res-06": "Sitting room layered with a collected gallery wall",
    "res-07": "Study with a writing desk and framed artwork",
    "res-08": "Desk vignette with a large iron clock",
    "res-09": "Bedroom with a tufted headboard and linen bedding",
    "np-01": "Colorful textiles and lanterns inside the Boho Beach House playhouse",
    "np-02": "Layered rugs and cushions inside the Boho Beach House playhouse",
    "studio-weston": "Weston Broadrick",
}

# Studio copy, word for word from the current site
STUDIO_LEAD = "Weston Broadrick Studio is a Phoenix-based interior design practice specializing in office, restaurant and hospitality environments."
STUDIO_PARAS = [
    "Founded by Weston Broadrick, the studio is known for creating refined, immersive interiors that elevate the guest experience while supporting the operational goals of each client.",
    "Weston brings over a decade of experience from Ralph Lauren Home, where he developed a deep understanding of craftsmanship, materiality, and the art of layered, narrative-driven spaces. Influenced by Ralph Lauren’s distinct point of view—where heritage, lifestyle, and environment intersect—his work reflects a balance of timeless design and modern sensibility.",
    "The studio designs office, residential, hospitality, and retail interiors. Each project is approached as a complete experience, where layout, lighting, texture, and detail work together to shape how a space feels and functions.",
    "Weston Broadrick Studio works with a discerning clientele and takes on a limited number of projects each year to maintain the highest standards of craft. This selective approach fosters a highly collaborative and considered design process, ensuring each interior is both visually compelling and deeply functional—spaces that captivate guests and endure over time.",
]
HOME_LEAD = "A Phoenix-based interior design studio specializing in office, restaurant and hospitality spaces."
HOME_BODY = "With over a decade of experience at Ralph Lauren Home, Weston brings a refined, detail-driven approach to creating spaces that elevate the guest experience and support business growth. The studio works with a discerning clientele and takes on a limited number of projects each year to maintain the highest standards of craft."
DESCRIPTION = "Weston Broadrick Studio is a Phoenix interior design studio specializing in office, restaurant and hospitality spaces, shaped by over a decade at Ralph Lauren Home."


# ---------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------
def img(slug, p, sizes="100vw", cls="", eager=False, focus=""):
    """An <img> with a phone-sized version when one exists (srcset)."""
    m = IMAGES[slug]
    src = f"{p}images/{slug}.jpg"
    srcset = f' srcset="{p}images/{slug}-sm.jpg 1000w, {src} {m["w"]}w" sizes="{sizes}"' if m["sm"] else ""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    if focus:
        c += f' style="object-position:{focus}"'
    return (f'<img src="{src}"{srcset} width="{m["w"]}" height="{m["h"]}" '
            f'alt="{escape(ALT.get(slug, ""))}" data-full="{src}" {load} decoding="async"{c}>')


def head(title, p, path, desc=DESCRIPTION, og="res-01"):
    full_title = f"{title} — Weston Broadrick Studio" if title else "Weston Broadrick Studio — Interior Design, Phoenix"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{DOMAIN}/{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{DOMAIN}/images/{og}.jpg">
<meta property="og:url" content="{DOMAIN}/{path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#151412">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..600&family=Poppins:wght@300;400;500&display=swap">
<link rel="stylesheet" href="{p}css/site.css">
</head>"""


def header(p, current=""):
    def cur(key):
        return ' aria-current="page"' if key == current else ""
    home = p or "./"
    on_project = ' aria-current="true"' if current in [x["slug"] for x in PROJECTS] else ""
    # Projects opens a dropdown on desktop; in the phone menu the projects are listed underneath
    items = "".join(f'<li><a href="{p}projects/{x["slug"]}/"{cur(x["slug"])}>{escape(x["name"])}</a></li>' for x in PROJECTS)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="logo" href="{home}"><img src="{p}images/logo.png" width="1000" height="273" alt="Weston Broadrick Studio"></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav class="nav" id="site-nav" aria-label="Main">
    <a href="{home}"{cur("home")}>Home</a>
    <div class="nav-drop">
      <a href="{p}projects/{FIRST}/"{on_project} class="nav-drop-toggle">Projects</a>
      <ul class="nav-sub">{items}</ul>
    </div>
    <a href="{p}contact/"{cur("about")}>About</a>
  </nav>
</header>"""


def footer(p):
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-cta reveal">
      <a class="footer-email" href="mailto:{EMAIL}">{EMAIL}</a><br>
      <a class="footer-phone" href="tel:{PHONE_LINK}">{PHONE}</a>
    </div>
    <div class="footer-base">
      <span>&copy; {YEAR} Weston Broadrick Studio &middot; Phoenix, Arizona</span>
      <nav aria-label="Footer"><a href="{p}projects/{FIRST}/">Projects</a><a href="{p}contact/">About</a></nav>
    </div>
  </div>
</footer>
<script src="{p}js/site.js"></script>
</body>
</html>
"""


def work_rows(p, order):
    """The big alternating project list used on Home and Projects."""
    by_slug = {x["slug"]: x for x in PROJECTS}
    pattern = ["a", "b", "a", "c", "b"]  # a = photo left, b = photo right, c = full width
    sizes = {"a": "(max-width: 820px) 100vw, 66vw", "b": "(max-width: 820px) 100vw, 58vw", "c": "100vw"}
    out = []
    for i, slug in enumerate(order):
        pr = by_slug[slug]
        kind = pattern[i % len(pattern)]
        out.append(f"""  <a class="work {kind} reveal" href="{p}projects/{slug}/">
    <div class="work-media">{img(pr["tile"], p, sizes[kind])}</div>
    <div class="work-caption">
      <span class="eyebrow work-num">{i + 1:02d}</span>
      <h3 class="work-name">{escape(pr["name"])}</h3>
      <div class="work-type">{escape(pr["sector"])} &middot; {escape(pr["location"])}</div>
      <span class="eyebrow work-link">View project</span>
    </div>
  </a>""")
    return "\n".join(out)


def gallery(p, rows):
    out = []
    for row in rows:
        kind, shots = row[0], row[1:]
        if kind in ("two", "offset"):
            # Side-by-side pair: each photo's width follows its shape, so both
            # stand the same height and neither gets cropped (desktop).
            ratios = [IMAGES[s]["w"] / IMAGES[s]["h"] for s in shots]
            total = sum(ratios)
            figs = "".join(
                f'<figure style="--ar:{r:.4f};aspect-ratio:{IMAGES[s]["w"]} / {IMAGES[s]["h"]}">'
                f'{img(s, p, f"(max-width: 720px) 100vw, {round(100 * r / total)}vw")}</figure>'
                for s, r in zip(shots, ratios))
            out.append(f'<div class="g-row pair reveal">{figs}</div>')
        elif kind == "full":
            out.append(f'<div class="g-row reveal"><figure>{img(shots[0], p)}</figure></div>')
        elif kind == "full-float":
            # Full-width photo with round photos floating on top of it, overlapping
            # the rows above/below. Each float is (photo, position classes).
            big, floats = shots[0], shots[1:]
            circles = "".join(
                f'<div class="float-wrap {pos}"><figure class="float-circle">{img(s, p, "(max-width: 720px) 130px, 320px")}</figure></div>'
                for s, pos in floats)
            out.append(f'<div class="g-row has-float reveal"><figure>{img(big, p)}</figure>{circles}</div>')
        elif kind == "inset":
            out.append(f'<div class="g-row one-inset reveal"><figure>{img(shots[0], p, "80vw")}</figure></div>')
        elif kind == "narrow":
            out.append(f'<div class="g-row reveal" style="max-width:760px;margin:0 auto;width:100%"><figure>{img(shots[0], p, "(max-width: 720px) 100vw, 760px")}</figure></div>')
    return "\n".join(out)


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def build_home():
    p = ""
    schema = {
        "@context": "https://schema.org", "@type": "InteriorDesigner",
        "name": "Weston Broadrick Studio", "url": DOMAIN + "/", "email": EMAIL,
        "image": f"{DOMAIN}/images/res-01.jpg", "founder": {"@type": "Person", "name": "Weston Broadrick"},
        "address": {"@type": "PostalAddress", "addressLocality": "Phoenix", "addressRegion": "AZ", "addressCountry": "US"},
        "description": DESCRIPTION,
    }
    write("index.html", f"""{head("", p, "")}
<body class="has-hero">
{header(p, "home")}
<main id="main">
  <section class="hero">
    {img("res-01", p, eager=True, focus="50% 22%")}
    <div class="hero-text">
      <h1 class="visually-hidden">Weston Broadrick Studio</h1>
      <div class="hero-meta">
        <span class="eyebrow">Interior Design</span>
        <span class="eyebrow">Phoenix, Arizona</span>
        <div class="scroll-cue" aria-hidden="true"></div>
      </div>
    </div>
  </section>

  <section class="statement wrap">
    <div class="statement-grid reveal">
      <span class="eyebrow">Weston Broadrick Studio</span>
      <div>
        <p class="statement-lead">{escape(HOME_LEAD)}</p>
        <p class="statement-body">{escape(HOME_BODY)}</p>
      </div>
    </div>
  </section>

  <section class="index wrap" aria-labelledby="work-h">
    <div class="index-head"><h2 class="eyebrow" id="work-h" style="margin:0">Selected Work</h2></div>
{work_rows(p, HOME_ORDER)}
  </section>

</main>
<script type="application/ld+json">{json.dumps(schema)}</script>
{footer(p)}""")


def build_projects_index():
    # No Projects page any more — /projects (old Squarespace address) forwards to the first project
    write("projects/index.html", f"""<!doctype html><meta charset="utf-8"><title>Weston Broadrick Studio</title>
<link rel="canonical" href="{DOMAIN}/projects/{FIRST}/"><meta http-equiv="refresh" content="0; url={FIRST}/"><a href="{FIRST}/">Continue</a>""")

def build_project(i):
    pr = PROJECTS[i]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    prev = PROJECTS[(i - 1) % len(PROJECTS)]
    p = "../../"
    story = ""
    if pr["lead"] or pr["body"]:
        body = f'<p class="statement-body">{escape(pr["body"])}</p>' if pr["body"] else ""
        story = f"""  <section class="project-story wrap reveal">
    <p class="statement-lead">{escape(pr["lead"])}</p>
    {body}
  </section>"""
    subtitle = pr.get("subtitle", "Interior design")
    desc = pr.get("seo") or pr["lead"] or f"{pr['name']} — {pr['sector'].lower()} interior by Weston Broadrick Studio, {pr['location']}."
    write(f"projects/{pr['slug']}/index.html", f"""{head(pr["name"], p, f"projects/{pr['slug']}", desc, pr["hero"])}
<body class="has-hero">
{header(p, pr["slug"])}
<main id="main">
  <section class="hero">
    {img(pr["hero"], p, eager=True, focus=pr.get("focus", ""))}
    <div class="hero-text">
      <h1 class="hero-title">{escape(pr["name"])}</h1>
    </div>
  </section>
  <div class="wrap">
    <dl class="project-meta reveal">
      <div><dt class="eyebrow">Project</dt><dd>{escape(pr["name"])}</dd></div>
      {"" if pr.get("hide_sector") else f'<div><dt class="eyebrow">Sector</dt><dd>{escape(pr["sector"])}</dd></div>'}
      <div><dt class="eyebrow">Location</dt><dd>{escape(pr["location"])}</dd></div>
      <div><dt class="eyebrow">Scope</dt><dd>{escape(subtitle)}</dd></div>
    </dl>
  </div>
{story}
  <section class="gallery wrap" aria-label="{escape(pr['name'])} photographs">
{gallery(p, pr["gallery"] + ([("full", pr["hero"])] if pr.get("repeat_hero", True) else []))}
  </section>
  <div class="wrap">
    <nav class="project-nav" aria-label="More projects">
      <a class="pn-prev" href="{p}projects/{prev['slug']}/">
        <span class="eyebrow">Previous project</span>
        <span class="work-name">{escape(prev["name"])}</span>
      </a>
      <a class="pn-next" href="{p}projects/{nxt['slug']}/">
        <span class="eyebrow">Next project</span>
        <span class="work-name">{escape(nxt["name"])}</span>
      </a>
    </nav>
  </div>
</main>
{footer(p)}""")


def build_studio():
    p = "../"
    paras = "\n".join(f"        <p>{escape(t)}</p>" for t in STUDIO_PARAS)
    write("contact/index.html", f"""{head("About", p, "contact", og="studio-weston")}
<body>
{header(p, "about")}
<main id="main">
  <section class="page-head wrap">
    <h1 class="hero-title">About</h1>
  </section>
  <section class="wrap about-grid">
    {img("studio-weston", p, "(max-width: 820px) 100vw, 40vw")}
    <div class="about-copy reveal">
      <p class="statement-lead">{escape(STUDIO_LEAD)}</p>
{paras}
      <p style="margin-top:2.4em"><span class="eyebrow">Inquiries</span><br>
        <a class="work-link" style="margin-top:10px" href="mailto:{EMAIL}">{EMAIL}</a><br>
        <a class="work-link" style="margin-top:10px" href="tel:{PHONE_LINK}">{PHONE}</a></p>
    </div>
  </section>
</main>
{footer(p)}""")


def build_extras():
    # Old Squarespace address /home now forwards to the home page
    write("home/index.html", f"""<!doctype html><meta charset="utf-8"><title>Weston Broadrick Studio</title>
<link rel="canonical" href="{DOMAIN}/"><meta http-equiv="refresh" content="0; url=../"><a href="../">Continue</a>""")
    # "Page not found" — GitHub serves this from any depth, so it uses root paths
    write("404.html", f"""{head("Page not found", "/", "404")}
<body>
{header("/")}
<main id="main">
  <section class="page-head wrap" style="min-height:70vh">
    <span class="eyebrow">404</span>
    <h1 class="hero-title" style="margin-top:14px">Page not found</h1>
    <p style="margin-top:28px"><a class="work-link eyebrow" href="/projects/{FIRST}/">View projects</a></p>
  </section>
</main>
{footer("/")}""")
    urls = ["", "contact/"] + [f"projects/{x['slug']}/" for x in PROJECTS]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{DOMAIN}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    build_projects_index()
    for i in range(len(PROJECTS)):
        build_project(i)
    build_studio()
    build_extras()
