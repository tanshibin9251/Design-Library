# -*- coding: utf-8 -*-
"""生成每套风格母版的示例页 demo.html（纯 HTML + CSS 变量，无外部依赖，字体除外）。"""
from html import escape as e
from pathlib import Path

HERE = Path(__file__).parent


def I(t, d, x=""):
    return {"t": t, "d": d, "x": x}


def ph(label, ratio="4/3", soft=False, style=""):
    return f'<div class="ph{" soft" if soft else ""}" data-l="{e(label)}" style="aspect-ratio:{ratio};{style}"></div>'


# ---------------------------------------------------------------- 文案 + 版式配置
# tok：形状/字阶 token。sections：区块顺序。
S = {}

S["enterprise-blue"] = dict(
    tok=dict(radius="6px", hlh="1.12", hw="700", hcase="none", hls="-.01em", h1="60px", h2="40px", h3="22px", pad="88px", ew="600", stat="var(--c-accent)"),
    brand="Northgate Advisory", nav=["Services", "Industries", "Case studies", "About"], navcta="Book a call", navv="bar",
    eyebrow="Engineering & IT consulting", h1="Infrastructure decisions your board can sign off on.",
    lead="We help mid-sized companies plan, migrate and run critical systems, with fixed scopes and one accountable lead.",
    cta1="Book a discovery call", cta2="See case studies",
    stats=[("120+", "Projects delivered"), ("98%", "Client retention"), ("15 yrs", "In business"), ("24/7", "Support cover")],
    items_title="What we take off your plate", items_eyebrow="Services",
    items=[I("Systems audit", "A fixed-fee review of your stack, risks and cost, delivered as a ranked action plan."), I("Cloud migration", "Staged moves with rollback points, so operations never stop."), I("Managed IT", "Monitoring, patching and a named engineer who knows your setup."), I("Security & compliance", "Policies, controls and evidence ready for the next audit.")],
    quote=("They replaced three vendors with one plan, and the first quarter already paid for it.", "Operations Director, Logistics client"),
    cta_title="Tell us what is slowing you down.", cta_text="Reply within one working day. No sales deck.",
    foot=["Services", "Company", "Contact"], sections=["hero_split", "stats", "services_list", "quote", "cta_band"], foot_v="cols",
)

S["modern-saas"] = dict(
    tok=dict(radius="14px", hlh="1.08", hw="700", hcase="none", hls="-.025em", h1="68px", h2="42px", h3="21px", pad="96px", ew="500", stat="var(--c-primary)"),
    brand="Flowdesk", nav=["Product", "Pricing", "Docs", "Changelog"], navcta="Start free", navv="bar",
    eyebrow="New · Automations 2.0", h1="Run your whole team's work in one calm place.",
    lead="Plan, track and automate projects without the tool sprawl. Set up in minutes, not weeks.",
    cta1="Start free trial", cta2="Watch 2-min demo",
    items_title="Everything in one workspace", items_eyebrow="Features",
    items=[I("Smart boards", "Switch between list, board and timeline without losing context. Every view stays in sync."), I("Automations", "If this, then that, with no code."), I("Reports", "Live dashboards that update themselves."), I("Integrations", "Connect Slack, Google Drive, GitHub and 40+ more tools, with two-way sync and no glue code to maintain.")],
    plans=[("Starter", "$0", "For individuals", ["3 projects", "Basic boards", "Community support"]), ("Team", "$12", "per seat / month", ["Unlimited projects", "Automations", "Priority support", "Reports"]), ("Business", "$24", "per seat / month", ["SSO & audit log", "Advanced permissions", "Dedicated manager"])],
    quote=("We cut status meetings in half in the first month.", "Head of Product, Series B startup"),
    cta_title="Ready when you are.", cta_text="Free for 14 days. No credit card.",
    foot=["Product", "Resources", "Company"], sections=["hero_center", "logos", "services_bento", "pricing", "cta_band"], foot_v="cols",
)

S["bold-studio"] = dict(
    tok=dict(radius="0", hlh=".95", hw="400", hcase="uppercase", hls=".01em", h1="120px", h2="64px", h3="28px", pad="100px", ew="700", stat="var(--c-accent)", h1big="170px"),
    brand="Kiln Studio", nav=[], navcta="Menu", navv="min",
    eyebrow="Brand · Web · Motion", h1="We make brands impossible to ignore.",
    lead="An independent design studio for people who would rather be remembered than liked.",
    cta1="See our work", cta2="",
    items_title="Selected work", items_eyebrow="2024 — 2026",
    items=[I("Maison Verde", "Identity & packaging", "01"), I("Pulse Festival", "Campaign & web", "02"), I("Atlas Coffee", "Brand & retail", "03"), I("Northbound", "Film titles & motion", "04")],
    cta_title="hello@kiln.studio", cta_text="Got a project? Write to us.",
    foot=["Work", "Studio", "Social"], sections=["hero_full", "work_asym", "cta_giant"], foot_v="min",
)

S["boutique-rose"] = dict(
    tok=dict(radius="10px", hlh="1.12", hw="600", hcase="none", hls="-.01em", h1="64px", h2="42px", h3="20px", pad="88px", ew="600", stat="var(--c-primary)"),
    brand="Maison Rosée", nav=["New in", "Dresses", "Beauty", "Gifts", "Journal"], navcta="Bag (2)", navv="center",
    eyebrow="Autumn collection", h1="Pieces you will reach for every morning.",
    lead="Small-batch dresses and skincare, made to be worn often and kept for years.",
    cta1="Shop the collection", cta2="Our story",
    items_title="New this week", items_eyebrow="Just landed",
    items=[I("Silk Slip Dress", "", "RM 289"), I("Rose Hip Face Oil", "", "RM 96"), I("Linen Wrap Top", "", "RM 159"), I("Pearl Hair Clip Set", "", "RM 45"), I("Cashmere Scarf", "", "RM 219"), I("Rosewater Mist", "", "RM 58"), I("Wide Leg Trousers", "", "RM 199"), I("Velvet Scrunchie", "", "RM 29")],
    strip=[("Free shipping", "On orders over RM 150"), ("Easy returns", "30 days, no questions"), ("Gift wrapped", "Free on every order")],
    cta_btn="Join the list", cta_title="Join the list, get 10% off.", cta_text="New arrivals and private sales, once a week.",
    foot=["Shop", "Help", "About"], sections=["hero_split_rev", "products", "strip", "cta_band"], foot_v="cols",
)

S["magazine-classic"] = dict(
    tok=dict(radius="2px", hlh="1.18", hw="700", hcase="none", hls="-.005em", h1="52px", h2="34px", h3="22px", pad="72px", ew="600", stat="var(--c-accent)", fsb="18px"),
    brand="The Meridian", nav=["Business", "Tech", "Culture", "Opinion", "Podcasts"], navcta="Subscribe", navv="center",
    eyebrow="Business", h1="Why the region's quietest industry is suddenly the most watched.",
    lead="After a decade of steady growth, regional logistics is attracting capital, talent and scrutiny. Our reporters spent three months on the ground.",
    cta1="Read the story", cta2="",
    items_title="Latest", items_eyebrow="Today",
    items=[I("The four-day week, one year on", "What employers learned when the pilot became policy.", "Work"), I("Inside the last film-camera factory", "A visit to the plant that refuses to close.", "Culture"), I("How a village bank survived", "Microloans, tea and a stubborn manager.", "Money"), I("Letters: your reply on housing", "Readers respond to our series.", "Opinion"), I("The quiet return of the night train", "Rail is back, and so are the sleepers.", "Travel")],
    cta_btn="Subscribe free", cta_title="The week in five emails.", cta_text="Our editors' picks, every Friday morning.",
    foot=["Sections", "About", "Follow"], sections=["hero_mag", "articles", "cta_band"], foot_v="cols",
)

S["fine-dining"] = dict(
    tok=dict(radius="0", hlh="1.08", hw="600", hcase="none", hls=".01em", h1="76px", h2="48px", h3="28px", pad="104px", ew="500", stat="var(--c-accent)"),
    brand="Auberge Noir", nav=["Menu", "Wine", "Private dining", "Contact"], navcta="Reserve", navv="center_dark",
    eyebrow="Seasonal tasting menus", h1="An evening, unhurried.",
    lead="Twelve seats at the pass. One tasting menu, built around what arrived this morning.",
    cta1="Reserve a table", cta2="View the menu",
    items_title="Tonight's menu", items_eyebrow="Seven courses · RM 480",
    items=[I("Oyster, cucumber, dill", "Hand-dived, cured in kombu", "I"), I("Wagyu tartare", "Smoked egg yolk, shallot", "II"), I("Hokkaido scallop", "Brown butter, finger lime", "III"), I("Duck, three ways", "Fig, black garlic jus", "IV"), I("Aged sourdough", "Cultured butter, sea salt", "V"), I("Pre-dessert", "Yuzu granita, basil", "VI"), I("Chocolate, olive oil", "Maldon, rosemary", "VII"), I("Petit fours", "To finish", "VIII")],
    cta_title="Reserve your evening", cta_text="Dinner Tuesday to Saturday, from 6.30 pm.",
    foot=["Visit", "Hours", "Follow"], sections=["hero_frame", "menu", "hours", "cta_band_light"], foot_v="cols",
)

S["restaurant-warm"] = dict(
    tok=dict(radius="16px", hlh="1.15", hw="700", hcase="none", hls="0", h1="58px", h2="38px", h3="22px", pad="84px", ew="700", stat="var(--c-accent)"),
    brand="Kopi & Kaya", nav=["Menu", "Our story", "Catering", "Visit"], navcta="Order online", navv="bar",
    eyebrow="Family kitchen since 1987", h1="Home cooking, made the slow way.",
    lead="Roasted every morning, simmered all afternoon. Come hungry, leave like family.",
    cta1="See today's menu", cta2="Book a table",
    items_title="Crowd favourites", items_eyebrow="From the kitchen",
    items=[I("Hainanese chicken rice", "Poached to order, with ginger and chilli.", "RM 14"), I("Kaya toast set", "Charcoal toast, soft eggs, kopi O.", "RM 9"), I("Beef rendang", "Eight hours, one pot, no shortcuts.", "RM 22")],
    hours=[("Opening hours", "Mon–Sun · 7 am – 9 pm"), ("Find us", "12 Jalan Bunga, Georgetown"), ("Call or WhatsApp", "+60 12-345 6789")],
    cta_title="Feeding a crowd?", cta_text="Catering for 20 to 500, delivered hot.",
    foot=["Eat", "Visit", "Follow"], sections=["hero_split", "dishes", "hours_dark", "cta_band"], foot_v="cols",
)

S["construction-pro"] = dict(
    tok=dict(radius="2px", hlh="1.05", hw="700", hcase="uppercase", hls=".01em", h1="72px", h2="44px", h3="24px", pad="88px", ew="700", stat="var(--c-accent)"),
    brand="Ironbridge Build", nav=["Services", "Projects", "Process", "Contact"], navcta="Get a quote", navv="bar",
    eyebrow="Licensed · Insured · Since 2004", h1="Built right. Finished on time.",
    lead="Renovation and commercial fit-out with one site manager from first sketch to final inspection.",
    cta1="Request a quote", cta2="View projects",
    stats=[("350+", "Projects completed"), ("20 yrs", "On site"), ("100%", "Licensed & insured"), ("0", "Missed handovers")],
    items_title="What we build", items_eyebrow="Services",
    items=[I("Home renovation", "Kitchens, bathrooms and full-house refurbishments, managed end to end."), I("Commercial fit-out", "Shops, offices and clinics, delivered to your opening date."), I("Roofing & waterproofing", "Leaks fixed once, backed by a written 10-year warranty.")],
    steps=[("01", "Site visit", "We measure, listen and photograph. Free."), ("02", "Fixed quote", "Itemised, with no surprise add-ons."), ("03", "Build", "One site manager, daily updates."), ("04", "Handover", "Walkthrough, snag list and warranty.")],
    cta_title="Need a quote this week?", cta_text="Send us your plans or photos. We reply within 24 hours.",
    foot=["Services", "Company", "Contact"], sections=["hero_split_dark", "stats", "services_alt", "steps", "cta_band"], foot_v="cols",
)

S["calm-spa"] = dict(
    tok=dict(radius="24px", hlh="1.12", hw="600", hcase="none", hls="0", h1="64px", h2="42px", h3="26px", pad="96px", ew="600", stat="var(--c-primary)"),
    brand="Still Water", nav=["Treatments", "Packages", "About", "Journal"], navcta="Book now", navv="center",
    eyebrow="Day spa & wellness", h1="Slow down. You have arrived.",
    lead="Massage, facials and quiet rooms, designed to let your shoulders drop the moment you walk in.",
    cta1="Book a treatment", cta2="View packages",
    items_title="Treatments", items_eyebrow="Restore",
    items=[I("Deep tissue massage", "Slow, focused work on tension you have been carrying for months."), I("Hydrating facial", "Gentle, plant-based, and finished with a warm towel ritual."), I("Couples retreat", "Private suite, two therapists, tea and silence in between.")],
    quote=("I fell asleep in the first ten minutes and woke up a different person.", "Mei Ling, monthly guest"),
    cta_title="Your hour is waiting.", cta_text="First visit? Enjoy a complimentary foot soak.",
    foot=["Visit", "Treatments", "Follow"], sections=["hero_center_soft", "services_alt", "quote", "cta_band"], foot_v="cols",
)

S["fitness-energy"] = dict(
    tok=dict(radius="4px", hlh=".98", hw="800", hcase="uppercase", hls="-.01em", h1="96px", h2="52px", h3="26px", pad="92px", ew="800", stat="var(--c-accent)", h1big="140px"),
    brand="Forge Fitness", nav=["Programs", "Trainers", "Schedule", "Join"], navcta="Free trial", navv="bar",
    eyebrow="Strength · Conditioning · Community", h1="Earn it. Every single rep.",
    lead="Coached small-group training for people who are done guessing. First week is on us.",
    cta1="Claim free week", cta2="See schedule",
    items_title="Choose your fight", items_eyebrow="Programs",
    items=[I("Strength 45", "Heavy compound lifts, coached in groups of six.", "01"), I("HIIT Burn", "Thirty minutes. Heart rate up, excuses down.", "02"), I("Mobility", "Move better, hurt less, recover faster.", "03"), I("Athlete Prep", "Speed, power and testing for competitors.", "04")],
    plans=[("Drop-in", "RM 45", "per class", ["Any class", "No commitment"]), ("Monthly", "RM 289", "per month", ["Unlimited classes", "Free assessment", "Guest pass"]), ("Annual", "RM 2,490", "per year", ["Everything in Monthly", "2 months free", "PT session"])],
    cta_title="Your first week is free.", cta_text="Walk in any time or book a tour.",
    foot=["Train", "Gym", "Follow"], sections=["hero_diag", "programs", "pricing", "cta_band"], foot_v="cols",
)

# ---------------------------------------------------------------- 区块
def nav(c):
    v = c["navv"]
    links = "".join(f'<li><a href="#">{e(x)}</a></li>' for x in c["nav"])
    if v == "min":
        return f'<header class="nav nav-min"><div class="wrap"><a class="logo" href="#">{e(c["brand"])}</a><a class="navmenu" href="#">{e(c["navcta"])} +</a></div></header>'
    cls = {"bar": "nav-bar", "center": "nav-center", "center_dark": "nav-center nav-dark"}[v]
    btn = f'<a class="btn" href="#">{e(c["navcta"])}</a>'
    if v.startswith("center"):
        return f'<header class="nav {cls}"><div class="wrap"><a class="logo" href="#">{e(c["brand"])}</a><ul>{links}</ul></div></header>'
    return f'<header class="nav {cls}"><div class="wrap"><a class="logo" href="#">{e(c["brand"])}</a><ul>{links}</ul>{btn}</div></header>'


def actions(c):
    b = f'<a class="btn" href="#">{e(c["cta1"])}</a>'
    if c["cta2"]:
        b += f'<a class="btn ghost" href="#">{e(c["cta2"])}</a>'
    return f'<div class="actions">{b}</div>'


def hero_text(c):
    return f'<div><span class="eyebrow">{e(c["eyebrow"])}</span><h1>{e(c["h1"])}</h1><p class="lead">{e(c["lead"])}</p>{actions(c)}</div>'


def hero_split(c, rev=False, dark=False):
    return f'<section class="hero{" dark" if dark else ""}{" rev" if rev else ""}"><div class="wrap grid2">{hero_text(c)}{ph("Hero image", "4/5", soft=not dark)}</div></section>'


def hero_center(c, soft=False):
    mock = '<div class="mock"><div class="bar"><i></i><i></i><i></i></div><div class="body"><div class="side"><b></b><b></b><b></b><b></b></div><div class="main"><div></div><div></div><div></div><div></div></div></div></div>'
    extra = mock if not soft else ph("Hero image", "21/9", soft=True, style="margin-top:56px")
    return f'<section class="hero hero-center"><div class="wrap"><span class="eyebrow">{e(c["eyebrow"])}</span><h1 style="max-width:16ch;margin:0 auto">{e(c["h1"])}</h1><p class="lead" style="margin-left:auto;margin-right:auto">{e(c["lead"])}</p>{actions(c)}{extra}</div></section>'


def hero_full(c, diag=False):
    if diag:
        return f'<section class="hero hero-full hero-diag dark" style="padding-top:clamp(70px,9vw,120px)"><div class="wrap"><span class="eyebrow">{e(c["eyebrow"])}</span><h1 style="font-size:clamp(46px,10vw,var(--h1big))">{e(c["h1"])}</h1><p class="lead">{e(c["lead"])}</p>{actions(c)}</div></section>'
    return f'<section class="hero-full"><div class="wrap"><span class="eyebrow">{e(c["eyebrow"])}</span><h1>{e(c["h1"])}</h1><p class="lead">{e(c["lead"])}</p></div>{ph("Full-bleed work image", "21/9")}</section>'


def hero_frame(c):
    return f'<section class="dark" style="padding:clamp(14px,3vw,34px)"><div class="frame"><span class="eyebrow">{e(c["eyebrow"])}</span><h1>{e(c["h1"])}</h1><p class="lead">{e(c["lead"])}</p>{actions(c)}</div></section>'


def hero_mag(c):
    side = "".join(f'<article><span class="tag">{e(i["x"])}</span><h3>{e(i["t"])}</h3><p class="muted" style="font-size:15px;margin-top:6px">{e(i["d"])}</p></article>' for i in c["items"][:3])
    return f'<section><div class="wrap mag"><div>{ph("Lead image", "16/10")}<span class="tag" style="margin-top:20px">{e(c["eyebrow"])}</span><h1>{e(c["h1"])}</h1><p class="lead" style="margin-top:0">{e(c["lead"])}</p><a class="btn" href="#">{e(c["cta1"])}</a></div><div class="side">{side}</div></div></section>'


def logos(c):
    return '<div class="wrap"><div class="logos">' + "".join(f"<span>{n}</span>" for n in ["Acme", "Globex", "Initech", "Umbra", "Vertex"]) + "</div></div>"


def head(c, title=None, eyebrow=None, right=""):
    return f'<div class="head"><div><span class="eyebrow">{e(eyebrow or c["items_eyebrow"])}</span><h2>{e(title or c["items_title"])}</h2></div>{right}</div>'


def stats(c, cls="alt"):
    return f'<section class="sec tight {cls}"><div class="wrap"><div class="stats">' + "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in c["stats"]) + "</div></div></section>"


def services_list(c):
    rows = "".join(f'<div class="row"><span class="n">0{n}</span><h3>{e(i["t"])}</h3><p>{e(i["d"])}</p><span class="arr">→</span></div>' for n, i in enumerate(c["items"], 1))
    return f'<section class="sec"><div class="wrap">{head(c)}<div class="rows">{rows}</div></div></section>'


def services_bento(c):
    cards = ""
    for n, i in enumerate(c["items"]):
        hl = " hl" if n == 3 else ""
        cards += f'<div class="card{hl}"><div class="ico">{n + 1}</div><h3>{e(i["t"])}</h3><p>{e(i["d"])}</p></div>'
    return f'<section class="sec alt"><div class="wrap">{head(c)}<div class="bento">{cards}</div></div></section>'


def services_alt(c):
    rows = ""
    for n, i in enumerate(c["items"], 1):
        rows += f'<div class="alt-row">{ph(i["t"], "5/4", soft=True)}<div><span class="num">0{n}</span><h3 style="margin-top:8px">{e(i["t"])}</h3><p>{e(i["d"])}</p><a class="btn ghost" href="#" style="margin-top:20px">Learn more</a></div></div>'
    return f'<section class="sec"><div class="wrap">{head(c)}{rows}</div></section>'


def work_asym(c):
    a = "".join(f'<a href="#">{ph(i["t"], "16/10")}<h3>{e(i["t"])}</h3><span class="muted">{e(i["d"])} · {e(i["x"])}</span></a>' for i in c["items"])
    return f'<section class="sec"><div class="wrap">{head(c)}<div class="work">{a}</div></div></section>'


def products(c):
    p = ""
    for n, i in enumerate(c["items"]):
        tag = '<span class="tag">NEW</span>' if n in (0, 3) else ""
        p += f'<div>{tag}{ph(i["t"], "3/4", soft=True)}<h3>{e(i["t"])}</h3><span class="price">{e(i["x"])}</span></div>'
    return f'<section class="sec"><div class="wrap">{head(c, right="<a class=\"btn ghost\" href=\"#\">View all</a>")}<div class="products">{p}</div></div></section>'


def articles(c):
    out = ""
    for n, i in enumerate(c["items"][2:5]):
        out += f'<article>{ph(i["t"], "16/10" if n else "16/11")}<span class="meta">{e(i["x"])}</span><h3>{e(i["t"])}</h3><p class="muted" style="font-size:16px">{e(i["d"])}</p></article>'
    return f'<section class="sec alt"><div class="wrap">{head(c)}<div class="articles">{out}</div></div></section>'


def menu(c):
    its = "".join(f'<div class="it"><div class="l"><b>{e(i["t"])}</b><i></i><em>{e(i["x"])}</em></div><p>{e(i["d"])}</p></div>' for i in c["items"])
    return f'<section class="sec loose dark"><div class="wrap"><div style="text-align:center;margin-bottom:56px"><span class="eyebrow">{e(c["items_eyebrow"])}</span><h2>{e(c["items_title"])}</h2></div><div class="menu">{its}</div></div></section>'


def dishes(c):
    d = "".join(f'<div>{ph(i["t"], "4/3", soft=True)}<div class="info"><h3>{e(i["t"])}<em>{e(i["x"])}</em></h3><p>{e(i["d"])}</p></div></div>' for i in c["items"])
    return f'<section class="sec"><div class="wrap">{head(c)}<div class="dishes">{d}</div></div></section>'


def steps(c):
    s = "".join(f"<div><b>STEP {a}</b><h3>{e(b)}</h3><p>{e(d)}</p></div>" for a, b, d in c["steps"])
    return f'<section class="sec alt"><div class="wrap">{head(c, "How a project runs", "Process")}<div class="steps">{s}</div></div></section>'


def pricing(c):
    out = ""
    for n, (nm, amt, per, feats) in enumerate(c["plans"]):
        li = "".join(f"<li>{e(f)}</li>" for f in feats)
        hl = " hl" if n == 1 else ""
        out += f'<div class="card{hl}"><h3>{e(nm)}</h3><div class="amt">{e(amt)} <small>{e(per)}</small></div><ul>{li}</ul><a class="btn{"" if n == 1 else " ghost"}" href="#">Choose {e(nm)}</a></div>'
    return f'<section class="sec"><div class="wrap">{head(c, "Simple pricing", "Plans")}<div class="pricing">{out}</div></div></section>'


def programs(c):
    rows = "".join(f'<div class="row"><span class="n">{e(i["x"])}</span><h3>{e(i["t"])}</h3><p>{e(i["d"])}</p><span class="arr">→</span></div>' for i in c["items"])
    return f'<section class="sec"><div class="wrap">{head(c)}<div class="rows">{rows}</div></div></section>'


def quote(c):
    q, w = c["quote"]
    return f'<section class="sec alt"><div class="wrap quote"><blockquote>“{e(q)}”</blockquote><cite>— {e(w)}</cite></div></section>'


def strip(c):
    s = "".join(f'<div><h3 style="font-size:18px">{e(a)}</h3><p class="muted" style="font-size:15px">{e(b)}</p></div>' for a, b in c["strip"])
    return f'<section class="sec tight band2"><div class="wrap"><div class="stats">{s}</div></div></section>'


def hours(c, dark=False):
    h = "".join(f"<div><h4>{e(a)}</h4><p>{e(b)}</p></div>" for a, b in (c.get("hours") or [("Opening hours", "Tue–Sat · 6.30 pm – late"), ("Address", "88 Orchard Lane"), ("Reservations", "+60 3-1234 5678")]))
    return f'<section class="sec tight {"band2" if dark else "alt"}"><div class="wrap"><div class="hours">{h}</div></div></section>'


def cta_band(c, light=False):
    cls = "alt" if light else "dark"
    return f'<section class="sec {cls}"><div class="wrap ctaband"><div><h2>{e(c["cta_title"])}</h2><p>{e(c["cta_text"])}</p></div><a class="btn" href="#">{e(c.get("cta_btn") or c["cta1"])}</a></div></section>'


def cta_giant(c):
    return f'<section class="dark"><div class="wrap giant"><span class="eyebrow">{e(c["cta_text"])}</span><a href="#">{e(c["cta_title"])}</a></div></section>'


def footer(c):
    cols = "".join(f'<div><h4>{e(t)}</h4><ul><li>About</li><li>Contact</li><li>FAQ</li></ul></div>' for t in c["foot"])
    dark = "dark" if c["foot_v"] == "min" else "band2"
    return f'<footer class="foot {dark}"><div class="wrap"><div class="cols"><div><a class="logo" href="#" style="color:inherit">{e(c["brand"])}</a><p style="margin-top:12px;opacity:.7;max-width:30ch">Placeholder copy. Replace with the client\'s own words.</p></div>{cols}</div><div class="copy">© 2026 {e(c["brand"])}. Template preview from Design Library.</div></div></footer>'


SEC = {
    "hero_split": lambda c: hero_split(c), "hero_split_rev": lambda c: hero_split(c, rev=True), "hero_split_dark": lambda c: hero_split(c, dark=True),
    "hero_center": lambda c: hero_center(c), "hero_center_soft": lambda c: hero_center(c, soft=True),
    "hero_full": hero_full, "hero_diag": lambda c: hero_full(c, diag=True), "hero_frame": hero_frame, "hero_mag": hero_mag,
    "logos": logos, "stats": stats, "services_list": services_list, "services_bento": services_bento, "services_alt": services_alt,
    "work_asym": work_asym, "products": products, "articles": articles, "menu": menu, "dishes": dishes, "steps": steps,
    "pricing": pricing, "programs": programs, "quote": quote, "strip": strip, "hours": hours, "hours_dark": lambda c: hours(c, True),
    "cta_band": cta_band, "cta_band_light": lambda c: cta_band(c, True), "cta_giant": cta_giant,
}


def gurl(families):
    return "https://fonts.googleapis.com/css?family=" + "|".join(f.replace(" ", "+") + ":300,400,500,600,700,800" for f in families) + "&display=swap"


def render(slug, info):
    """info: parse_design() 的结果（colors / fonts）。返回完整 demo.html。"""
    c = S[slug]
    col = info["colors"]
    heads, body = info["fonts"]["head"], info["fonts"]["body"]
    CJK = ",'Noto Sans SC','Noto Serif SC',sans-serif"
    t = c["tok"]
    tok = dict(h1big=t["h1"], fsb="16px")
    tok.update(t)
    css_vars = (
        f"--c-primary:{col['primary']};--c-secondary:{col['secondary']};--c-text:{col['text']};--c-accent:{col['accent']};--c-surface:{col['surface']};--c-border:{col['border']};"
        f"--f-head:'{heads}'{CJK};--f-body:'{body}'{CJK};--radius:{tok['radius']};--hlh:{tok['hlh']};--hw:{tok['hw']};--hcase:{tok['hcase']};--hls:{tok['hls']};"
        f"--h1:{tok['h1']};--h2:{tok['h2']};--h3:{tok['h3']};--h1big:{tok['h1big']};--pad:{tok['pad']};--ew:{tok['ew']};--fs-body:{tok['fsb']};--stat:{tok['stat']}"
    )
    # 同一套风格里 hero 之后的区块：按 sections 顺序渲染
    parts = [nav(c)] + [SEC[s](c) for s in c["sections"]] + [footer(c)]
    families = sorted({heads, body})
    css = (HERE / "demo.css").read_text(encoding="utf-8")
    js = (HERE / "demo.js").read_text(encoding="utf-8")
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{e(info["title"])} · demo</title>
<link rel="stylesheet" href="{gurl(families)}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Noto+Sans+SC:400,500,700&display=swap">
<style>:root{{{css_vars}}}
{css}</style></head><body>
{"".join(parts)}
<script>{js}</script></body></html>'''
