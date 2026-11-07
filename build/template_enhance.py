"""Export the same accessible fragment foundations to preview, HTML, PHP and JSON.

Only inert demo forms opt in. Existing custom handlers are left intact.
"""
from html import escape
from pathlib import Path
import re

RUNTIME = Path(__file__).resolve().parent.parent / 'library' / 'runtime'

def normalize_cart(x):
    """Keep even the no-JS sample summaries consistent; no real fees are inferred."""
    if x['slug']=='restaurant-warm' or 'cart' not in x['pages']:
        return
    cart=x['pages']['cart']
    rows=[]
    for block in re.split(r'<div class="crow">',cart)[1:]:
        name=re.search(r'<h3>(.*?)</h3>',block,re.S)
        price=re.search(r'<b>\s*(RM|\$|€|£)\s*([\d,.]+)\s*</b>',block)
        if name and price:rows.append((name[1],price[1],float(price[2].replace(',',''))))
    if not rows:return
    currency=rows[0][1];total=sum(r[2] for r in rows)
    amount=lambda n:escape(currency)+' '+format(n,',.2f')
    summary='<li><span>Subtotal</span><b>'+amount(total)+'</b></li><li><span>Demo delivery / fees</span><b>Not applied</b></li><li class="tot"><span>Total</span><b>'+amount(total)+'</b></li>'
    x['pages']['cart']=re.sub(r'(<ul class="kv">).*?</ul>',lambda m:m[1]+summary+'</ul>',cart,count=1,flags=re.S)
    if 'checkout' in x['pages']:
        checkout=x['pages']['checkout']
        lines=''.join('<li><span>1 × '+name+'</span><b>'+amount(price)+'</b></li>' for name,_,price in rows)
        checkout=re.sub(r'(<ul class="kv">).*?</ul>',lambda m:m[1]+lines+'<li class="tot"><span>Total · demo only</span><b>'+amount(total)+'</b></li></ul>',checkout,count=1,flags=re.S)
        checkout=re.sub(r'(<button[^>]*type="submit"[^>]*>).*?</button>',lambda m:m[1]+'Preview checkout · '+amount(total)+'</button>',checkout,count=1,flags=re.S)
        checkout=re.sub(r'<label\b[^>]*>\s*<span>(?:Card number|Expiry|CVC)</span>.*?</label>','',checkout,flags=re.S)
        x['pages']['checkout']=checkout

def enhance(x):
    if x['format'] != 'fragments' or x['slug'] == 'cafe-bakery':
        return x
    normalize_cart(x)
    nav = x['nav']
    nav = '<a class="dl-skip" href="#dl-content">Skip to content</a>' + nav
    # Keep existing mobile navigation; add one only where it is absent.
    if '<details' not in nav:
        links = []
        groups = {}
        for page in x['pagelist']:
            if page['slug'] in ('404', 'coming-soon'):
                continue
            groups.setdefault(page.get('group') or 'Pages', []).append(page)
        for group, pages in groups.items():
            links.append('<h4>' + escape(group) + '</h4>')
            for page in pages:
                links.append('<a href="{{p:' + page['slug'] + '}}">' + escape(page['label']) + '</a>')
        mobile = '<details class="dl-mobile"><summary>Menu</summary><nav class="dl-mobile-links" aria-label="Template pages">' + ''.join(links) + '</nav></details>'
        end = nav.rfind('</div></header>')
        if end >= 0:
            nav = nav[:end] + mobile + nav[end:]
        elif '</header>' in nav:
            nav = nav.replace('</header>', mobile + '</header>', 1)
    nav = '<span data-dl-template="' + escape(x['slug']) + '" hidden></span><style>' + (RUNTIME / 'template-ux.css').read_text(encoding='utf-8') + '</style>' + nav
    nav += '<script>' + (RUNTIME / 'template-ux.js').read_text(encoding='utf-8') + '</script>'
    nav += '<script>' + (RUNTIME / 'template-commerce.js').read_text(encoding='utf-8') + '</script>'
    interactions = x['dir'] / 'interactions.js'
    if interactions.exists():
        nav += '<script>' + interactions.read_text(encoding='utf-8') + '</script>'
    x['nav'] = nav
    x['foot'] = re.sub(r'<footer\b', '<footer data-dl-footer', x['foot'], count=1)
    for slug, page in x['pages'].items():
        available = {p['slug'] for p in x['pagelist']}
        def route_action(match):
            label = re.sub('<[^>]*>', '', match[3]).strip()
            if not re.match(r'^(Choose|Select|Get started|Start|Book|Reserve|Buy|Subscribe|Apply|Join)\b', label, re.I):
                return match[0]
            candidates = ('signup', 'booking', 'reservations', 'contact')
            target = next((p for p in candidates if p in available), None)
            return match[1].replace('href="#"', 'href="{{p:' + target + '}}"') + match[2] + match[3] + '</a>' if target else match[0]
        page = re.sub(r'(<a\b[^>]*href="#")([^>]*>)(.*?)</a>', route_action, page, flags=re.S)
        page = re.sub(r'<form\b([^>]*?)\s+onsubmit="return false;?"', r'<form\1 data-dl-demo-form', page)
        if 'data-dl-demo-form' in page:
            page = page.replace('We confirm by email within one working day.', 'Demo only: details are checked in this browser. No request or email is sent.')
        page = re.sub(r'<div class="pager">(?:(?!</div>).)*</div>', '<p class="muted">All sample items are shown on this page.</p>', page, flags=re.S)
        # Give the skip link one target per visible page in the preview.
        page = '<div tabindex="-1" data-dl-content>' + page + '</div>'
        x['pages'][slug] = page
    return x
