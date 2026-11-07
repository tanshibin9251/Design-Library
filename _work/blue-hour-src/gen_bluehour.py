import sys, json
sys.path.insert(0, r"C:/Users/TANSHI~1/AppData/Local/Temp/claude/c--Users-Tan-Shi-Bin-My-Drive-DATA-LIBRARY-CUSTOM-SITE-BUILDER-Design-Library-public-html/17b625fe-de54-4c04-8ca6-5efbafa022c0/scratchpad")
from pathlib import Path
import bh_art, bh_css, bh_js

LIB = Path(r"c:/Users/Tan Shi Bin/My Drive/DATA LIBRARY/CUSTOM SITE BUILDER/Design Library/library")
SLUG = "blue-hour"
D = LIB / "templates" / SLUG


def A(name, label=None, cls=""):
    return bh_art.art(name, label, ("ap-art bh-art " + cls).strip())


ARROW = '<svg class="bh-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
LOGO = '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3.5 25h33" stroke="currentColor" stroke-width="2" fill="none"/><path d="M9 25a11 11 0 0 1 22 0z" fill="currentColor"/><path d="M20 5v4M8 11l3 3M32 11l-3 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/></svg>'

# ------------------------------------------------------------------ nav + footer
RS_DEFS = ('<svg class="rs-defs" aria-hidden="true" focusable="false"><filter id="rs-fr" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="1 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 1 0"/></filter>'
           '<filter id="rs-fg" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 0  0 1 0 0 0  0 0 0 0 0  0 0 0 1 0"/></filter>'
           '<filter id="rs-fb" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 1 0 0  0 0 0 1 0"/></filter></svg>')

EXTRA_CSS = '''
[hidden]{display:none!important}
.bh-rad{position:relative;display:inline-block}.bh-rad input{position:absolute;opacity:0;inset:0;width:100%;height:100%;margin:0;cursor:pointer}
.bh-rad span{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border:1.5px solid var(--c-border);border-radius:99px;font:700 12px/1 var(--f-head);letter-spacing:.14em;text-transform:uppercase;color:var(--bh-ink2);transition:background .25s,color .25s,border-color .25s}
.bh-rad input:checked+span{background:var(--c-primary);color:var(--on-primary);border-color:var(--c-primary)}.bh-rad input:focus-visible+span{outline:3px solid var(--c-accent);outline-offset:3px}
.bh-ok{outline:none}
.bh-hero h1{color:inherit}
.bh-state .bh-lead{font-size:clamp(1.1rem,2vw,1.5rem);color:var(--c-primary)}
'''

NAV = ('<style>' + bh_css.build() + EXTRA_CSS + '</style>' + RS_DEFS +
       f'<header class="bh-top"><div class="bh-in bh-bar"><a class="bh-brand" href="{{{{p:home}}}}" aria-label="Blue Hour, home">{LOGO}<span>Blue<b>Hour</b></span></a>'
       '<nav class="bh-nav" id="bh-nav" aria-label="Main"><a href="{{p:expeditions}}" data-k="expeditions">Expeditions</a><a href="{{p:journal}}" data-k="journal">Journal</a><a href="{{p:prints}}" data-k="prints">Prints</a><a href="{{p:about}}" data-k="about">Studio</a></nav>'
       '<a class="pf pf-sm pf-solid" href="{{p:contact}}">Enquire</a>'
       '<button class="bh-burger" type="button" aria-expanded="false" aria-controls="bh-nav" aria-label="Menu"><i></i><i></i><i></i></button></div><div class="bh-prog" aria-hidden="true"><i></i></div></header>'
       '<script>' + bh_js.JS + '</script>')

FOOT = ('<footer class="bh-foot"><div class="bh-in"><p class="big" aria-hidden="true">Blue Hour</p><div class="cols">'
        f'<div><a class="bh-brand" href="{{{{p:home}}}}">{LOGO}<span>Blue<b>Hour</b></span></a><p style="margin-top:14px">Small-group photo expeditions, planned around the twenty minutes either side of sunset and sunrise. 蓝调时刻 · 小团摄影远征。</p></div>'
        '<div><h4>Explore</h4><a href="{{p:expeditions}}">Expeditions</a><a href="{{p:expedition}}">Lofoten in winter</a><a href="{{p:journal}}">Field journal</a><a href="{{p:prints}}">Prints</a></div>'
        '<div><h4>Studio</h4><a href="{{p:about}}">About &amp; team</a><a href="{{p:contact}}">Enquire</a><a href="{{p:404}}">404</a><a href="#top" data-top>Back to top</a></div>'
        '<div><h4>Dispatches</h4><p>One letter a month: a place, a picture, what went wrong.</p><form data-form><input type="email" placeholder="you@example.com" aria-label="Email address" required><button class="pf pf-sm pf-solid" type="submit">Join</button></form></div></div>'
        '<div class="base"><span>© 2026 Blue Hour Expeditions · template demo content · prices are illustrative (RM)</span><span>Drawn placeholder scenes — replace with your photographs</span></div></div></footer>')

# ------------------------------------------------------------------ helpers
FACTS = lambda items: '<div class="bh-facts">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items) + "</div>"
FAQ = lambda items: '<div class="bh-faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def cta(kicker, title, lead, b1=("Enquire about a trip", "contact"), b2=("Browse the prints", "prints")):
    return (f'<section class="bh-cta"><div class="bh-in"><span class="bh-k">{kicker}</span><h2 data-sc>{title}</h2><p class="bh-lead">{lead}</p>'
            f'<div class="bh-actions"><a class="pf pf-solid" href="{{{{p:{b1[1]}}}}}">{b1[0]}</a><a class="pf" href="{{{{p:{b2[1]}}}}}">{b2[0]}</a></div></div></section>')


def cf(rows, arts, tag="View trip"):
    li = "".join(f'<li data-s="{s}"><a class="cf-row" href="{{{{p:expedition}}}}"><span class="no">0{i + 1}</span><span class="t">{t}</span><span class="c">{c}</span><span class="y">{y}</span><span class="cf-inline" aria-hidden="true"></span></a></li>'
                 for i, (t, c, y, s) in enumerate(rows))
    fa = "".join(f'<div class="cf-a">{A(a, "", "")}</div>' for a in arts)
    return f'<div data-cf><ul class="cf-list">{li}</ul><div class="cf-float" aria-hidden="true"><div class="cf-box">{fa}<span class="cf-tag">{tag}</span></div></div></div>'


DEP = [("Lofoten in winter", "Norway · 9 days", "Jan 2027 · 3 seats", "winter"), ("Skeleton Coast", "Namibia · 10 days", "Jun 2026 · 2 seats", "summer"),
       ("Torres del Paine", "Chile · 11 days", "Nov 2026 · 5 seats", "autumn"), ("Kyoto in the rain", "Japan · 7 days", "Jun 2026 · 4 seats", "summer"),
       ("Faroe Islands", "Denmark · 8 days", "Sep 2026 · 6 seats", "autumn"), ("Iceland, south coast", "Iceland · 8 days", "Feb 2027 · 7 seats", "winter")]
DEP_ART = ["aurora", "dunes", "peaks", "city", "sea", "forest"]


def cr_row(i, shape, art, title, text, exif, rev):
    return (f'<div class="row{" rev" if rev else ""}"><figure class="cr-fig cr-{shape}" data-cr style="margin:0"><div class="cr-clip">{A(art, title)}</div></figure>'
            f'<div><span class="no">0{i}</span><h3>{title}</h3><p>{text}</p><div class="bh-exif">' + "".join(f'<span class="bh-tag">{e}</span>' for e in exif) + '</div></div></div>')


def ss_art(name, label):
    return A(name, label, "ss-art")


# ------------------------------------------------------------------ HOME
ss = [("aurora", "Lofoten, Norway", "Winter · January to March", "Fishing cabins under green aurora, black beaches, and peaks that rise straight out of the sea.", ["Aurora", "Long exposure", "Seascape"]),
      ("dunes", "Skeleton Coast, Namibia", "Dry season · June to August", "Fog-bound dunes, shipwrecks in the sand and a sky that turns to copper for ten minutes.", ["Dunes", "Silhouettes", "Wide angle"]),
      ("peaks", "Torres del Paine, Chile", "Summer · November to March", "Granite towers lit from behind, a lake like glass and weather that changes the picture hourly.", ["Mountains", "Reflections", "Weather"]),
      ("city", "Kyoto in the rain, Japan", "Rainy season · June, November", "Wet lanes, lantern glow and the pagoda lit blue for a few minutes after the street lamps come on.", ["Street", "Night", "Reflections"])]
ss_html = "".join(f'<article class="ss-s">{ss_art(a, t)}<div class="ss-t"><span class="ss-no">0{i + 1} / 04</span><h3>{t}</h3><p><b style="color:var(--c-accent);font-weight:600">{when}</b><br>{d}</p><ul>' + "".join(f"<li>{x}</li>" for x in tg) + f'</ul><a class="bh-link" href="{{{{p:expedition}}}}">Plan this trip {ARROW}</a></div></article>'
                  for i, (a, t, when, d, tg) in enumerate(ss))

pd_steps = [("The brief", "A call a month before: what you shoot, what you want to shoot, what you are afraid of. We build the week around you."),
            ("Arrival", "We land, drop bags and walk to the first location while there is still light, no itinerary, just orientation."),
            ("Scout by day", "Mornings are for walking the ground we will use at dusk. Light changes everything, so we plan the angles in advance."),
            ("Blue hour", "Out an hour before the light turns, home when it is gone. Eight photographers, two guides, tripods in a line."),
            ("Review", "Every evening we edit together over dinner: three keepers each, one honest note, then sleep. Prints follow within a month.")]
pd_html = "".join(f'<article class="pd-i"><span class="pd-dot" aria-hidden="true">{i + 1}</span><div class="tx"><h3>{t}</h3><p>{d}</p></div></article>' for i, (t, d) in enumerate(pd_steps))

vs = [("sea", "Eleven minutes of blue", "Field notes · 8 min"), ("forest", "Photographing fog without losing it", "Technique · 6 min"), ("dunes", "Packing for a desert you cannot leave", "Gear · 5 min")]
vs_html = "".join(f'<figure class="vs-c">{A(a, t)}<figcaption><b><a href="{{{{p:story}}}}" style="text-decoration:none;color:inherit">{t}</a></b><span>{m}</span></figcaption></figure>' for a, t, m in vs)

HOME = (
    '<section data-nav="home" class="bh-hero" id="top"><div class="bh-stars" aria-hidden="true"></div><div class="bh-in"><span class="bh-k">Small-group photo expeditions · 2026 / 27</span>'
    '<div class="mt" data-mt><h1 class="mt-t"><span class="mt-a">Blue</span><span class="mt-b">Hour</span></h1></div>'
    '<div class="bh-herorow"><p class="bh-lead">We take eight photographers at a time to the edge of the map, and keep them out for the twenty minutes when the sky is neither day nor night.</p>'
    '<div class="bh-actions"><a class="pf pf-solid" href="{{p:expeditions}}">See departures</a><a class="pf" href="{{p:story}}">Read the journal</a></div></div><span class="bh-cue">Scroll</span></div></section>'
    '<section class="bh-sec"><div class="bh-in"><div class="bh-state"><div><span class="bh-k">The idea</span><p class="bh-lead" style="margin-top:0">Most trips are planned around the high sun. Ours are planned around its absence.</p></div>'
    '<div><p class="st" data-sl>Every picture we are proud of was made in the minutes either side of sunrise and sunset, when the light is soft, the sky is blue and a place finally looks like itself. So we plan each expedition around those minutes, and fill the rest of the day with scouting, sleep and very good food.</p>'
    '<div class="bh-mini"><div><b>8</b><span>guests per trip, never more</span></div><div><b>2</b><span>guides: a photographer and a local</span></div><div><b>20</b><span>minutes of blue light on a good evening</span></div></div></div></div></div></section>'
    '<section class="bh-ss"><div class="bh-in" style="padding-bottom:clamp(24px,4vw,48px)"><span class="bh-k">Where we go</span><h2 class="bh-h">Four places, <em>four kinds of blue.</em></h2></div>'
    f'<div><section class="ss-sec" data-ss style="--n:4"><div class="ss-stage"><div class="ss-bar" aria-hidden="true"></div>{ss_html}<div class="ss-rail" role="group" aria-label="Destinations"></div></div></section></div></section>'
    '<section class="bh-sec bh-dusk"><div class="bh-in"><div class="bh-head"><div><span class="bh-k">Last season</span><h2 class="bh-h">Four frames, <em>four settings.</em></h2></div><a class="bh-link" href="{{p:journal}}">All stories ' + ARROW + '</a></div><div class="bh-fr">'
    + cr_row(1, "circle", "sea", "The lighthouse at 21:40", "A 25-second exposure on a flat sea. The moon did the work; we only had to stand still and not breathe.", ["f/4", "25 s", "ISO 800", "24 mm"], False)
    + cr_row(2, "diamond", "forest", "Fog between the pines", "We waited two mornings for this. The third, the valley filled up and the light came through at a low angle.", ["f/5.6", "1/60", "ISO 400", "70 mm"], True)
    + cr_row(3, "blinds", "aurora", "Green over the cabins", "Aurora is the easy part. The hard part is finding the one cabin window that is warm and the one rock that is not in the way.", ["f/2.8", "10 s", "ISO 3200", "20 mm"], False)
    + cr_row(4, "arch", "peaks", "First light on the towers", "Three hours of walking in the dark for six minutes of orange on grey granite. Nobody complained.", ["f/8", "1/125", "ISO 200", "35 mm"], True)
    + '</div></div></section>'
    '<section class="bh-sec bh-dep"><div class="bh-in"><div class="bh-head"><div><span class="bh-k">Next departures</span><h2 class="bh-h">Pick a place, <em>find a date.</em></h2></div><a class="bh-link" href="{{p:expeditions}}">All departures ' + ARROW + '</a></div>'
    + cf(DEP, DEP_ART) + '</div></section>'
    '<section class="bh-sec bh-deep"><div class="bh-in"><div class="bh-head"><div><span class="bh-k">How a trip unfolds</span><h2 class="bh-h">Five stops, <em>one long evening.</em></h2></div></div>'
    f'<div><div class="pd-wrap" data-pd><svg class="pd-svg" aria-hidden="true"><path class="pd-bg"/><path class="pd-fg"/></svg>{pd_html}</div></div></div></section>'
    '<section class="bh-sec"><div class="bh-in"><div class="bh-head"><div><span class="bh-k">From the journal</span><h2 class="bh-h">Notes from <em>the field.</em></h2></div><a class="bh-link" href="{{p:journal}}">Read the journal ' + ARROW + '</a></div>'
    f'<div style="width:min(900px,100%);margin:0 auto"><div class="vs-list" data-vs>{vs_html}</div></div></div></section>'
    + cta("Seats are small", "Come out after dark.", "Most departures fill four to six months ahead. Tell us where you would like to be at dusk and we will tell you when.")
)

# ------------------------------------------------------------------ EXPEDITIONS
EXPS = (
    '<section data-nav="expeditions" class="bh-ph"><div class="bh-in"><div class="row"><div><span class="bh-k">2026 / 27 departures</span><h1>Departures</h1>'
    '<p class="bh-lead">Eight seats a trip. Pick a season, pick a place, and we will send the full itinerary and kit list within a day.</p></div>'
    f'<div class="sp" data-sp>{A("aurora", "Aurora over Lofoten")}</div></div></div></section>'
    '<section class="bh-sec" style="padding-top:0"><div class="bh-in"><div class="bh-head"><div class="bh-chips" data-filter="[data-cf]" role="group" aria-label="Filter by season">'
    '<button type="button" class="bh-chip" data-f="all" aria-pressed="true">All</button><button type="button" class="bh-chip" data-f="winter" aria-pressed="false">Winter</button>'
    '<button type="button" class="bh-chip" data-f="summer" aria-pressed="false">Summer</button><button type="button" class="bh-chip" data-f="autumn" aria-pressed="false">Autumn</button></div>'
    '<p class="bh-p" style="margin:0"><b data-count style="color:var(--c-accent)">6</b> departures shown</p></div><div class="bh-dep">' + cf(DEP, DEP_ART) + '</div></div></section>'
    '<section class="bh-sec bh-dusk"><div class="bh-in"><div class="bh-two"><div><span class="bh-k">Included</span><h2 class="bh-h" style="font-size:clamp(1.8rem,3.6vw,2.6rem)">Everything <em>except the flight.</em></h2>'
    '<ul class="bh-list"><li>Lodging, all meals and local transport</li><li>A lead photographer and a local guide, always two</li><li>Nightly edit sessions with honest feedback</li><li>Three signed A3 prints from your own picks</li><li>Pre-trip call and a written kit list</li></ul></div>'
    '<div><span class="bh-k">Not included</span><h2 class="bh-h" style="font-size:clamp(1.8rem,3.6vw,2.6rem)">What <em>you bring.</em></h2>'
    '<ul class="bh-list bh-no"><li>International flights and travel insurance</li><li>Camera, lenses and a sturdy tripod (we help you choose)</li><li>Warm layers: we send a list for every place</li><li>Personal spending and gratuities</li></ul></div></div></div></section>'
    '<section class="bh-sec"><div class="bh-in"><span class="bh-k">Good to know</span><h2 class="bh-h" style="margin-bottom:32px">Questions <em>before you book.</em></h2>'
    + FAQ([("Do I need a professional camera?", "No. Any camera with manual mode and a tripod is enough. We have mirrorless loaners for a small deposit."),
           ("How fit do I need to be?", "Each trip lists a level. Most are walks under five kilometres on uneven ground, with some dark early starts."),
           ("What if the weather ruins the night?", "Weather is part of the picture. We keep two spare evenings in every itinerary and move locations to chase clear sky."),
           ("Can I come on my own?", "Most guests do. Rooms are single by default and the group is small enough to feel like friends by day three.")]) + '</div></section>'
    + cta("Not sure which one?", "Ask us, we love this question.", "Tell us what you like to photograph and how you like to travel. We will point you to the right trip, even if it is not ours.", ("Ask about a trip", "contact"), ("Read the journal", "journal"))
)

# ------------------------------------------------------------------ EXPEDITION DETAIL
it = [("Day 1–2 · Arrive in Svolvær", "Land, drop bags and walk to the harbour for a first look at the light. Briefing over dinner."), ("Day 3 · Reine at dusk", "Red cabins, black water and the first aurora forecast. Our first real blue hour."),
      ("Day 4–5 · The beaches", "Haukland and Uttakleiv at low tide, then a long evening on the dunes with the sea at our back."), ("Day 6 · Weather day", "Rest, edit and print. If the sky opens, we go; if not, nobody is sorry."),
      ("Day 7–8 · Henningsvær", "Football pitch on a rock, harbour reflections and the last aurora window of the trip."), ("Day 9 · Farewell", "A last sunrise at the fjord, a final edit over breakfast and a flight home with a full card.")]
it_html = "".join(f'<article class="pd-i"><span class="pd-dot" aria-hidden="true">{i + 1}</span><div class="tx"><h3>{t}</h3><p>{d}</p></div></article>' for i, (t, d) in enumerate(it))
EXP = (
    '<section data-nav="expeditions" class="bh-zp"><div><section class="zp-sec" data-zp><div class="zp-stage"><div class="zp-pic">' + A("aurora", "Aurora over a fishing village in Lofoten") + '</div>'
    '<div class="zp-lead"><h2>One frame, one place</h2><span>Lofoten · Scroll to step inside</span></div>'
    '<div class="zp-over"><small>Departure 14 January 2027</small><h3>Lofoten in winter</h3></div>'
    '<div class="zp-card"><b>Eight seats. Three left.</b><p>Nine days of aurora, black beaches and fishing cabins, with two guides and a nightly edit.</p><a href="{{p:contact}}">Reserve a seat</a></div></div></section></div></section>'
    '<section class="bh-sec" style="padding-bottom:clamp(24px,4vw,48px)"><div class="bh-in">' + FACTS([("9", "days on the ground"), ("8", "guests, 2 guides"), ("3+", "aurora nights planned"), ("Easy", "walks under 5 km")]) + '</div></section>'
    '<section class="bh-sec" style="padding-top:clamp(24px,4vw,48px)"><div class="bh-in"><div class="bh-lay"><div><span class="bh-k">The itinerary</span><h2 class="bh-h" style="margin-bottom:clamp(28px,5vw,56px)">Nine days, <em>in order.</em></h2>'
    f'<div><div class="pd-wrap" data-pd><svg class="pd-svg" aria-hidden="true"><path class="pd-bg"/><path class="pd-fg"/></svg>{it_html}</div></div>'
    '<div class="bh-two" style="margin-top:clamp(40px,6vw,72px)"><div><h3>Included</h3><ul class="bh-list"><li>8 nights in fishing cabins (shared kitchens, private rooms)</li><li>All breakfasts, five dinners, a harbour-side seafood night</li><li>Minibus and boat transfers</li><li>Three signed A3 prints</li></ul></div>'
    '<div><h3>Bring</h3><ul class="bh-list bh-no"><li>Camera with manual mode, wide lens, sturdy tripod</li><li>Warm layers and spikes for your boots</li><li>Flights to Svolvær (we advise on timing)</li></ul></div></div>'
    '<div style="margin-top:clamp(40px,6vw,72px)"><span class="bh-k">Good to know</span>' + FAQ([("What are the odds of seeing aurora?", "In a nine-day window, high. We have seen it on 8 of the last 9 trips, but we never promise a sky."), ("How cold does it get?", "Around −5 to −10 °C at night, with wind. We send a layering guide and lend spikes."), ("Is it suitable for beginners?", "Yes. We run a short exposure workshop on day one."), ("What is the cancellation policy?", "Full refund up to 90 days before departure, 50% up to 45 days. Insurance is required.")]) + '</div></div>'
    '<aside class="bh-reserve bh-card" aria-label="Reserve a seat"><div class="pr">RM 18,900<small>per guest</small></div><dl><div><dt>Departure</dt><dd>14 Jan 2027</dd></div><div><dt>Duration</dt><dd>9 days</dd></div><div><dt>Group</dt><dd>8 guests</dd></div><div><dt>Seats left</dt><dd style="color:var(--c-accent)">3</dd></div></dl>'
    '<a class="pf pf-solid" href="{{p:contact}}" style="justify-content:center">Reserve a seat</a><p class="bh-p" style="font-size:13px">RM 3,000 holds your place. Balance due 90 days before.</p></aside></div></div></section>'
    + cta("Other places", "Not Lofoten? Try the dunes.", "Skeleton Coast, Torres del Paine, Kyoto, the Faroes. Every trip is built around the same twenty minutes.", ("All departures", "expeditions"), ("Ask a question", "contact"))
)

# ------------------------------------------------------------------ JOURNAL
J = [("forest", "Photographing fog without losing it", "Technique · 6 min", "technique", "Fog flattens everything. Here is how to keep depth, colour and a little mystery."),
     ("dunes", "Packing for a desert you cannot leave", "Gear · 5 min", "gear", "Sand, wind and one spare lens cap: the short list we actually carry."),
     ("city", "Kyoto after the rain", "Field notes · 7 min", "notes", "Why we plan the Kyoto trip for the wettest weeks of the year."),
     ("peaks", "Six minutes of orange on granite", "Field notes · 9 min", "notes", "A pre-dawn walk in Patagonia, told in the order it happened."),
     ("aurora", "Aurora settings that work", "Technique · 5 min", "technique", "A starting point for exposure, focus and white balance under green light."),
     ("sea", "Is a tripod really worth the weight?", "Gear · 4 min", "gear", "Our honest answer after nine trips: yes, but not that one.")]
jc = "".join(f'<a class="bh-jc" href="{{{{p:story}}}}" data-s="{s}"><div class="rs" data-rs role="img" aria-label="{t}"><div class="rs-base">{bh_art.svg_only(a)}</div></div><small>{m}</small><h3>{t}</h3><p>{d}</p></a>' for a, t, m, s, d in J)
JOURNAL = (
    '<section data-nav="journal" class="bh-ph"><div class="bh-in"><span class="bh-k">Field journal</span><h1>Notes from <span style="color:var(--c-accent)">the field</span></h1>'
    '<p class="bh-lead">Field notes, technique and honest gear opinions from the people who run the trips. One new piece every two weeks.</p></div></section>'
    '<section class="bh-sec" style="padding-top:0"><div class="bh-in"><div class="bh-two" style="align-items:center;margin-bottom:clamp(48px,8vw,100px)"><figure class="cr-fig cr-circle" data-cr style="margin:0;aspect-ratio:4/3"><div class="cr-clip">' + A("sea", "Moon over the sea, Lofoten") + '</div></figure>'
    '<div><span class="bh-k">Featured · Field notes</span><h2 class="bh-h" style="font-size:clamp(1.9rem,4vw,3rem)">Eleven minutes of blue</h2><p class="bh-p" style="margin:16px 0 24px">What it takes to be in the right place for the shortest, quietest light of the day. A long evening on the Lofoten coast, told minute by minute.</p>'
    '<a class="bh-link" href="{{p:story}}">Read the story ' + ARROW + '</a></div></div>'
    '<div class="bh-head"><div class="bh-chips" data-filter=".bh-jcards" role="group" aria-label="Filter stories"><button type="button" class="bh-chip" data-f="all" aria-pressed="true">All</button><button type="button" class="bh-chip" data-f="notes" aria-pressed="false">Field notes</button>'
    '<button type="button" class="bh-chip" data-f="technique" aria-pressed="false">Technique</button><button type="button" class="bh-chip" data-f="gear" aria-pressed="false">Gear</button></div>'
    '<p class="bh-p" style="margin:0"><b data-count style="color:var(--c-accent)">6</b> stories</p></div>'
    f'<div class="bh-jcards">{jc}</div></div></section>'
    + cta("One letter a month", "Dispatches, no filler.", "A place, a picture and what went wrong. Unsubscribe whenever, and we will not take it personally.", ("Join the list", "contact"), ("See departures", "expeditions"))
)

# ------------------------------------------------------------------ STORY
STORY = (
    '<section data-nav="journal" class="bh-art-hero"><div class="bh-in"><div class="bh-meta"><span><b>Field notes</b></span><span>Lofoten, Norway</span><span>8 min read</span><span>By Mara Lindqvist</span></div>'
    '<div class="mt" data-mt style="margin-top:28px"><h1 class="mt-t"><span class="mt-a">Eleven</span><span class="mt-b">Minutes</span></h1></div>'
    '<p class="bh-lead">of blue, on a flat sea, with the lighthouse still lit. A long evening told in the order it happened.</p></div></section>'
    '<div class="bh-wide"><figure class="cr-fig cr-arch" data-cr style="margin:0">' + '<div class="cr-clip">' + A("sea", "Moon over a calm sea with a lighthouse") + '</div></figure><p class="bh-cap">Moon, sea and the Hamnøy light, 21:40. 25 s at f/4, ISO 800.</p></div>'
    '<article class="bh-prose"><p class="dc" data-sl>At 21:12 the sun had been gone for an hour and the sea had gone the colour of a bruise. Nobody spoke. Eight tripods stood in a loose line on the rocks, and the only sound was the shutter of someone who could not wait.</p>'
    '<p>The trick with blue hour is that it is not an hour. On this coast, in January, it is closer to eleven minutes: the sky has to be dark enough that the lighthouse beam reads, and bright enough that the water still holds a colour. Miss either end and you have a nice picture of nothing.</p>'
    '<h2>What we got wrong, twice</h2><p>The first night we arrived late and shot into the sun. The second we arrived early and shot the wrong rock. On the third we sat on the beach for forty minutes with our backs to the view, and turned around together at 21:29.</p>'
    '<blockquote data-sc>Patience is a lens, and it is the only one you cannot lose.</blockquote>'
    '<p>Here is what I tell every group on the walk down: pick one foreground, one frame and one setting. When the colour arrives, do not change any of them. Change your breathing instead.</p></article>'
    '<div class="bh-wide"><figure class="cr-fig cr-diamond" data-cr style="margin:0">' + '<div class="cr-clip">' + A("aurora", "Aurora above fishing cabins") + '</div></figure><p class="bh-cap">Same evening, 23:05, looking the other way. 10 s at f/2.8, ISO 3200.</p></div>'
    '<article class="bh-prose"><h2>The settings, for the record</h2><table class="bh-tbl"><thead><tr><th>Frame</th><th>Exposure</th><th>ISO</th><th>Lens</th></tr></thead><tbody><tr><td>Lighthouse</td><td>25 s · f/4</td><td>800</td><td>24 mm</td></tr><tr><td>Reflection</td><td>8 s · f/5.6</td><td>400</td><td>35 mm</td></tr><tr><td>Aurora</td><td>10 s · f/2.8</td><td>3200</td><td>20 mm</td></tr></tbody></table>'
    '<p>None of it is secret. All of it is boring. The magic is being on the rocks at 21:29 with your hands warm and your mind quiet.</p></article>'
    '<section class="bh-sec"><div class="bh-in"><div class="bh-next"><a class="bh-jc bh-card" href="{{p:journal}}" style="padding:clamp(20px,3vw,32px)"><small>All stories</small><h3>Back to the journal</h3><p>Field notes, technique and honest gear opinions.</p></a>'
    '<a class="bh-jc bh-card" href="{{p:expedition}}" style="padding:clamp(20px,3vw,32px)"><small>Go there</small><h3>Lofoten in winter</h3><p>Nine days, eight seats, the same eleven minutes.</p></a></div></div></section>'
)

# ------------------------------------------------------------------ PRINTS
PR = [("sea", "Hamnøy, 21:40", 480, "Lofoten, 2025"), ("forest", "Fog between the pines", 480, "Faroe Islands, 2024"), ("aurora", "Green over the cabins", 520, "Lofoten, 2025"),
      ("peaks", "First light on the towers", 520, "Patagonia, 2024"), ("dunes", "Copper hour", 480, "Skeleton Coast, 2023"), ("city", "Pagoda after rain", 560, "Kyoto, 2024")]
prs = "".join(f'<article class="bh-pr"><div class="ld" data-ld role="img" aria-label="{t}">{bh_art.svg_only(a)}</div><div class="row"><h3>{t}</h3><span class="p" data-base="{p}">RM {p}</span></div><small>Edition of 25 · {w}</small><a class="pf pf-sm bh-add" href="#" data-add>Add to list</a></article>' for a, t, p, w in PR)
PRINTS = (
    '<section data-nav="prints" class="bh-ph"><div class="bh-in"><span class="bh-k">The print room</span><h1>Prints</h1><p class="bh-lead">Open editions of 25, pigment on cotton rag, signed and numbered by the photographer who made them. Move across a picture to feel it ripple.</p></div></section>'
    '<section class="bh-sec" style="padding-top:0"><div class="bh-in"><div class="bh-pick" data-picker><fieldset><legend>Size</legend><div class="bh-chips"><label class="bh-rad"><input type="radio" name="sz" value="1" checked><span>A3</span></label><label class="bh-rad"><input type="radio" name="sz" value="1.9"><span>A2</span></label><label class="bh-rad"><input type="radio" name="sz" value="3.2"><span>A1</span></label></div></fieldset>'
    '<fieldset><legend>Finish</legend><div class="bh-chips"><label class="bh-rad"><input type="radio" name="fn" value="0" checked><span>Matte rag</span></label><label class="bh-rad"><input type="radio" name="fn" value="120"><span>Baryta</span></label><label class="bh-rad"><input type="radio" name="fn" value="380"><span>Framed</span></label></div></fieldset></div>'
    f'<div class="bh-pgrid">{prs}</div></div></section>'
    '<section class="bh-sec bh-dusk"><div class="bh-in"><div class="bh-vals"><div class="bh-card"><span class="bh-k">Paper</span><h3>Cotton rag, 310 gsm</h3><p>Museum-grade pigment inks with a gamut wide enough for the blues we care about.</p></div>'
    '<div class="bh-card"><span class="bh-k">Edition</span><h3>Twenty-five, then done</h3><p>Each picture is printed to order and numbered. When the edition closes, it closes.</p></div>'
    '<div class="bh-card"><span class="bh-k">Delivery</span><h3>Rolled or flat, insured</h3><p>Shipped in a rigid tube within ten days. Framed prints travel flat in a custom crate.</p></div></div></div></section>'
    + cta("Printing from a trip?", "Your best frame, on paper.", "Every guest receives three signed A3 prints from their own picks. More can be ordered, in any size.", ("Ask about prints", "contact"), ("See departures", "expeditions"))
)

# ------------------------------------------------------------------ ABOUT
tun = [("aurora", "2018", "First trip", "Four friends, one rented van and a lot of wrong turns."), ("sea", "2019", "First prints", "A small edition sold out in a weekend, so we made another."),
       ("dunes", "2021", "The first desert", "Namibia taught us that fog is a collaborator, not a problem."), ("city", "2023", "Kyoto in the rain", "The trip that made us a studio instead of a hobby."),
       ("peaks", "2025", "Eight seats, forever", "We stopped growing on purpose. Smaller is the whole point.")]
tun_html = "".join(f'<figure class="zt-f">{A(a, t)}<figcaption><small>{y}</small><b>{t}</b></figcaption></figure>' for a, y, t, d in tun)
TEAM = [("Mara Lindqvist", "Lead photographer", "Shoots in the dark for a living. Believes every picture is a promise to the place.", 0), ("Tane Aroha", "Guide & logistics", "Knows every road, every ferry and every kitchen that will feed us at 23:00.", 1), ("Jun Wei Tan", "Prints & editing", "Runs the nightly edit and the print room. Gentle, and terrifyingly honest.", 0)]
team_html = "".join(f'<div class="bh-tm">{A("person", n, "")}<small>{r}</small><h3>{n}</h3><p>{d}</p></div>' for n, r, d, s in TEAM)
ABOUT = (
    '<section data-nav="about" class="bh-ph"><div class="bh-in"><span class="bh-k">The studio</span><h1>Small on purpose</h1>'
    '<p class="st" style="font:600 clamp(1.4rem,3vw,2.3rem)/1.25 var(--f-head);color:var(--c-primary);max-width:30em;margin-top:24px" data-sl>We started as four friends chasing the light across a map. We are still a handful of people, still taking eight guests at a time, and still happiest on a cold rock waiting for a sky to change.</p></div></section>'
    '<section class="bh-nmroot"><div><section class="nm-sec" data-nm data-vals="8,17,42,380" data-suf="+,+,+,+" style="--n:3"><div class="nm-stage"><div class="nm-copy"><span class="nm-eye">The studio, by the numbers</span><div class="nm-num" aria-live="off"><b data-nn>8</b><small data-ns>+</small></div>'
    '<div class="nm-labels"><p class="nm-l">Years leading expeditions</p><p class="nm-l">Countries on our map</p><p class="nm-l">Trips led, start to finish</p><p class="nm-l">Guests who came back for more</p></div></div>'
    '<svg class="nm-svg" viewBox="-100 -100 200 200" role="img" aria-label="A shape that morphs from circle to square to triangle to star"><polygon points=""/></svg><div class="nm-dots" aria-hidden="true"><i class="on"></i><i></i><i></i><i></i></div></div></section></div></section>'
    '<section class="bh-sec bh-deep" style="padding-bottom:0"><div class="bh-in"><span class="bh-k">How we got here</span><h2 class="bh-h">Five frames <em>from the studio.</em></h2></div>'
    f'<div><section class="zt-sec" data-zt style="--n:4"><div class="zt-stage"><div class="zt-title"><h2>Keep going</h2><span>Scroll to fly through</span></div>{tun_html}</div></section></div></section>'
    f'<section class="bh-sec"><div class="bh-in"><div class="bh-head"><div><span class="bh-k">The people</span><h2 class="bh-h">Three people, <em>two tripods each.</em></h2></div></div><div class="bh-team">{team_html}</div></div></section>'
    '<section class="bh-sec bh-dusk"><div class="bh-in"><div class="bh-vals"><div class="bh-card"><span class="bh-k">01</span><h3>Leave no trace</h3><p>We carry out what we carry in, stay on the paths and never move a rock for a picture.</p></div>'
    '<div class="bh-card"><span class="bh-k">02</span><h3>Hire local, always</h3><p>Every trip has a local guide, a local kitchen and local lodging. The money stays where the pictures are.</p></div>'
    '<div class="bh-card"><span class="bh-k">03</span><h3>Keep it small</h3><p>Eight guests and two guides. Not a number we will round up, however nicely you ask.</p></div></div></div></section>'
    + cta("Join us", "Bring a tripod. We will bring the dark.", "Departures fill four to six months ahead. Tell us where you would like to be at dusk.", ("Enquire about a trip", "contact"), ("See departures", "expeditions"))
)

# ------------------------------------------------------------------ CONTACT
CONTACT = (
    '<section data-nav="contact" class="bh-ph"><div class="bh-in"><span class="bh-k">Enquire</span><h1 data-sc>Tell us where you want to be at dusk.</h1><p class="bh-lead">We answer every message within one working day, usually with more questions than you asked.</p></div></section>'
    '<section class="bh-sec" style="padding-top:0"><div class="bh-in"><div class="bh-lay"><div><form class="bh-form" data-form><div class="g2"><label>Your name<input type="text" required autocomplete="name"></label><label>Email<input type="email" required autocomplete="email"></label></div>'
    '<div class="g2"><label>Trip<select><option>Lofoten in winter · Jan 2027</option><option>Skeleton Coast · Jun 2026</option><option>Torres del Paine · Nov 2026</option><option>Kyoto in the rain · Jun 2026</option><option>Faroe Islands · Sep 2026</option><option>Not sure yet</option></select></label>'
    '<label>Group size<select><option>Just me</option><option>Two of us</option><option>Three or four</option></select></label></div><label>Tell us about your photography<textarea placeholder="What do you shoot, and what would you like to learn?"></textarea></label>'
    '<div><button class="pf pf-solid" type="submit">Send enquiry</button></div></form><div class="bh-ok bh-card" tabindex="-1" role="status"><b>Thank you.</b> This is a demo form, so nothing was sent. In a real site this would reach the studio inbox.</div></div>'
    '<aside class="bh-card bh-reserve" style="gap:18px"><div><span class="bh-k" style="margin-bottom:8px">Studio</span><p class="bh-p" style="margin:0">hello@bluehour.example<br>+60 12 000 0000</p></div><div><span class="bh-k" style="margin-bottom:8px">Hours</span><p class="bh-p" style="margin:0">Mon to Fri, 10:00 to 18:00 (MYT). Evenings when we are out of town: we answer the next morning.</p></div>'
    '<div><span class="bh-k" style="margin-bottom:8px">Prints &amp; press</span><p class="bh-p" style="margin:0">prints@bluehour.example</p></div></aside></div></div></section>'
    '<section class="bh-sec bh-dusk"><div class="bh-in"><span class="bh-k">Before you ask</span><h2 class="bh-h" style="margin-bottom:32px">A few <em>quick answers.</em></h2>' + FAQ([("How soon should I book?", "Four to six months ahead for most departures. Winter aurora trips go fastest."), ("Do you offer private trips?", "Yes, for groups of four to eight. We will build the itinerary around you."), ("Can I pay in instalments?", "A deposit holds your seat; the balance is due 90 days before departure, split in two if you prefer.")]) + '</div></section>'
)

NF = ('<section data-nav="" class="bh-nf"><div class="bh-in"><p class="big">404</p><h1 data-sc>Lost in the blue hour</h1><p class="bh-lead" style="margin:16px auto 28px">This page is somewhere between day and night. Head back and we will find you a better view.</p>'
      '<div class="bh-actions" style="justify-content:center"><a class="pf pf-solid" href="{{p:home}}">Back to the start</a><a class="pf" href="{{p:expeditions}}">See departures</a></div></div></section>')

PAGES = dict(home=HOME, expeditions=EXPS, expedition=EXP, journal=JOURNAL, story=STORY, prints=PRINTS, about=ABOUT, contact=CONTACT)
PAGES["404"] = NF
PAGELIST = [("home", "Home: the blue hour", "Explore"), ("expeditions", "Departures (list + filter)", "Explore"), ("expedition", "Expedition: Lofoten in winter", "Explore"), ("journal", "Field journal", "Read"),
            ("story", "Story: Eleven minutes of blue", "Read"), ("prints", "Prints (liquid distort)", "Shop"), ("about", "The studio", "Studio"), ("contact", "Enquire", "Studio"), ("404", "404 error", "Utility")]

# ------------------------------------------------------------------ write
if D.exists():
    import shutil
    shutil.rmtree(D)
(D / "pages").mkdir(parents=True)
(D / "nav.html").write_text(NAV, encoding="utf8")
(D / "footer.html").write_text(FOOT, encoding="utf8")
for k, v in PAGES.items():
    (D / "pages" / f"{k}.html").write_text(v, encoding="utf8")
meta = {"format": "fragments", "slug": SLUG, "name": "Blue Hour", "zh": "蓝调时刻",
        "tag": "An immersive photo-expedition site: type that holds a moving picture, a pinned scene stack, an image that follows your cursor, a route that draws itself and prints that ripple. Night-violet with first-light gold.",
        "colors": {"primary": "#f3ecdf", "secondary": "#9a93d0", "text": "#e9e6f3", "accent": "#f2b84b", "surface": "#0e0c22", "border": "#2a2650"},
        "fonts": {"head": "Josefin Sans", "body": "Source Serif 4"},
        "tok": {"hlh": "1.02", "hw": "700", "hcase": "none", "hls": "-.015em", "h1": "104px", "h2": "58px", "h3": "26px", "pad": "112px", "ew": "700", "stat": "var(--c-accent)", "radius": "14px"},
        "types": ["portfolio", "company", "blog"], "industries": ["travel", "photography"], "styles": ["photo", "darkluxury", "typographic", "aurora"], "license": "库内自有",
        "pages": [{"slug": s, "label": l, "group": g} for s, l, g in PAGELIST]}
(D / "template.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf8")
print("written", {k: len(v) for k, v in PAGES.items()}, "nav", len(NAV), "foot", len(FOOT))

# ------------------------------------------------------------------ docs + live map
(D / "TEMPLATE.md").write_text("""# Blue Hour（蓝调时刻）

An immersive photo-expedition site: type that holds a moving picture, a pinned scene stack, an image that follows your cursor, a route that draws itself and prints that ripple. Night-violet ground with first-light gold. All pictures are drawn SVG placeholders; swap in photographs.

- **字体**：标题 Josefin Sans · 正文 Source Serif 4

## 页面（9）
""" + "\n".join(f"- {l}（`{s}`）" for s, l, g in PAGELIST) + """

## 用到的「沉浸式」效果（均来自库里的效果，已改成按页面作用域运行）
- 首页：`img-mask-text`（BLUE HOUR 字里的图）、`text-split-lines`、`scroll-scene-stack`、`img-clip-reveal`、`cursor-image-follow`、`scroll-path-draw`、`scroll-velocity-skew`、`text-scramble`、`button-pointer-fill`
- 出发列表：`img-strip-slices`、`cursor-image-follow`（带季节筛选）
- 出发详情：`img-scroll-zoom-pin`、`scroll-path-draw`
- 日志：`img-rgb-split`、`img-clip-reveal`；文章：`img-mask-text`、`text-split-lines`、`img-clip-reveal`、`text-scramble`
- 作品印刷：`img-liquid-distort`（WebGL，无 WebGL 时回退为原图）
- 关于：`scroll-number-morph`、`scroll-zoom-tunnel`、`text-split-lines`

## 换成真实照片
- 每个 `.ap-art`（里面是 SVG）换成 `<img>`（`object-fit:cover`）即可；`.ss-art`、`.cr-clip`、`.zp-pic`、`.zt-f`、`.cf-a`、`.sp`、`.rs-base`、`.ld` 都是同样的做法。
- 把文字里的占位文案、价格（RM）和日期换成客户的真实内容。
""", encoding="utf8")

sd = LIB / "styles" / SLUG
sd.mkdir(parents=True, exist_ok=True)
(sd / "DESIGN.md").write_text("""# Blue Hour

> 自有原创母版，授权 ok。所有图片都是自绘 SVG 占位（极光 / 沙丘 / 雪峰 / 海岸 / 夜城 / 雾林 / 人像剪影），颜色全部走主题变量；换成真实照片即可。

- **适合**：Portfolio / Company / Blog；旅行摄影远征、摄影工作室、摄影师个人站、目的地体验品牌、纪实摄影日志

## Feel
日落后的二十分钟：天空还没黑透，岸上的灯刚亮。午夜紫黑做底，第一缕光的金色只用在最需要被看见的地方，字大得像片头字幕，图随你的滚动一幕一幕换。

## 调色
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#f3ecdf` | 暖纸白：标题、按钮填充（深色站点里 primary 就是「亮色」） |
| Secondary | `#9a93d0` | 暮色薰衣草：辅助字、渐变、星空光晕 |
| Text | `#e9e6f3` | 正文 |
| Accent | `#f2b84b` | 第一缕光：主按钮、Kicker、数字、高亮词、路径线 |
| Surface | `#0e0c22` | 午夜紫黑；交替段落用 surface 混 secondary 的「暮色带」 |
| Border | `#2a2650` | 细线、卡片描边 |

金色落在 surface 上约 10:1，薰衣草约 6.4:1，暖纸白 > 15:1。

## 字体
标题 **Josefin Sans** 700（几何、带电影字幕感；Hero 与页头用全大写 + 紧字距，章节标题用句首大写）；正文 **Source Serif 4**（长文用衬线，读起来像游记）。
中文配 Noto Sans SC / Noto Serif SC，中文标题不要斜体。

## 构图特征（Design signature）
1. **Hero 是一个字，不是一张图**：超大的 BLUE / HOUR 当窗口，里面是随滚动移动的黄昏渐变和旋转色轮；首屏内一眼能读到价值主张和两个按钮。
2. **钉住一屏，换四个目的地**：Scene Stack，新图从下方擦上来盖住旧图，文字交叉淡入，底部有可点的场景序号和顶部进度条。
3. **出发列表就是大字目录**：悬停某一行，那一行对应的图跟着光标浮动并微倾斜；键盘聚焦固定在行右侧；触屏点一行在行内展开。
4. **一条会自己画出来的路线**：弯曲的金线穿过编号站点，文字永远在曲线外侧，站点被线碰到才点亮。
5. **版面在呼吸**：整页分「夜（surface）/ 暮色带 / 更深的夜」三种底，段落之间用大量留白，图片用圆、菱形、百叶、拱形遮罩随滚动展开。
6. **印刷页的图会泛起水波**（WebGL），日志封面在你快速滚动时红蓝错位；这两处都有无 WebGL / 减少动态时的纯静态回退。
7. **页脚是一个描边的大字 Wordmark**，不是链接墙。

## 不要
- 不要把图片放进圆角卡片网格里就算完（图要么出血，要么被形状遮罩，要么跟着滚动动）。
- 不要强制劫持滚动：钉住的区块高度有限，最后一定放开；所有钉住效果在「减少动态」下都退化成普通上下排列。
- 不要用 Emoji 或字符当图标；不要一整屏只剩动画没有可读文字。
- 不要把金色用到正文、整块背景或次要按钮上；金色是「看这里」。
- 不要在手机上依赖悬停；不要在首屏放自动播放的声音 / 视频。
- 不要把真实照片裁成与占位图不同的比例而不检查遮罩效果（遮罩与缩放按 4:5 / 16:9 调过）。
""", encoding="utf8")

lm = LIB / "runtime" / "live-map.json"
cur = json.loads(lm.read_text(encoding="utf8")) if lm.exists() else {}
cur[SLUG] = []          # this template ships its own motion; keep the generic Live layer off
lm.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf8")

o = LIB / "templates" / "order.json"
lst = json.loads(o.read_text(encoding="utf8"))
if SLUG not in lst:
    lst.append(SLUG)
    o.write_text(json.dumps(lst, ensure_ascii=False, indent=1), encoding="utf8")
print("docs + order + live-map done")
