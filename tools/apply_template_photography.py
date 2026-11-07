"""Apply explicitly curated template image choices. Preview by default; --apply writes.

Never maps a stock interior to an actual product, person, before/after or customer case.
"""
import argparse
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

def image(item, eager=False):
    url = item['url'] + '?auto=format&fit=crop&w=1920&h=1280&q=85'
    return '<img src="' + escape(url, quote=True) + '" alt="' + escape(item['alt'], quote=True) + '" width="1920" height="1280" ' + ('loading="eager" fetchpriority="high"' if eager else 'loading="lazy"') + ' decoding="async"><span class="dl-stock-label">Illustrative stock image</span>'

def run(write=False):
    manifest = json.loads((ROOT/'library/photography/remote.json').read_text(encoding='utf-8'))
    items = {x['id']:x for x in manifest['images']}
    cafe = json.loads((ROOT/'library/templates/cafe-bakery/images.json').read_text(encoding='utf-8'))
    items.update({x['id']:x for x in cafe['images']})
    plans = json.loads((ROOT/'library/photography/placements.json').read_text(encoding='utf-8'))
    # These labels describe spaces, never the identity of a named individual or product.
    hero_labels = {'calm-spa':'Hero image','casa-makeover':'Happy room (缺图)',
        'homestay-stays':'Hero stay photo (缺图)','oakline-furniture':'Room scene · living room (缺图)',
        'reflex-point':'Quiet room, window light (缺图)','renovo-studio':'Hero project image (缺图)',
        'thai-touch':'Treatment room (缺图)','trailhead-outdoor':'Full-bleed mountain photo (缺图)',
        'wedding-photo':'Hero wedding photo (缺图)',
        'kissa-showa':'Counter & siphon, afternoon light (缺图)',
        'pet-boutique':'Hero pet (缺图)', 'curve-modern':'Sofa (缺图)',
        'heirloom-classic':'The Dining Room'}
    for slug,plan in plans.items():
        ids = plan['images']
        selected = [items[i] for i in ids]
        for item in selected:
            assert min(item['original_width'], item['original_height']) >= 1080, item['id']
        directory = ROOT/'library/templates'/slug
        p = directory/'pages/home.html';home = p.read_text(encoding='utf-8')
        if 'data-dl-photo-edition' in home:
            print(slug + ': already applied');continue
        used = []
        target = hero_labels.get(slug)
        if target:
            pattern = r'(<div\b[^>]*class="[^"]*\bph\b[^"]*"[^>]*data-l="' + re.escape(target) + r'"[^>]*>)(.*?)</div>'
            def replace(match):
                used.append(selected[0]['id'])
                opening = re.sub(r'class="([^"]*)"', lambda m:'class="'+m[1]+' dl-visual"', match[1])
                opening = opening.replace('data-l="'+target+'"','data-l="Illustrative stock reference" data-dl-photo-edition')
                return opening + image(selected[0], True) + match[2] + '</div>'
            home = re.sub(pattern, replace, home, count=1, flags=re.S)
        remaining = [x for x in selected if x['id'] not in used]
        if remaining:
            figures = ''.join('<figure><div class="dl-visual" style="aspect-ratio:3/2">'+image(x)+'</div><figcaption>'+escape(x['alt'])+'</figcaption></figure>' for x in remaining)
            section = '<section class="dl-photo-story" data-dl-photo-edition><div class="dl-photo-wrap"><div class="dl-photo-head"><h2>'+escape(plan['heading'])+'</h2><p>'+escape(plan['description'])+'</p></div><div class="dl-photo-grid">'+figures+'</div></div></section>'
            end = home.find('</section>')
            home = home[:end+10] + section + home[end+10:] if end>=0 else home+section
        # Per-template records make the images inspectable without loading a central index.
        record = {'purpose':manifest['purpose'],'license_url':manifest['license_url'],'checked_at':manifest['checked_at'],'images':selected}
        credits = '<details class="dl-credits"><summary>Illustrative photography &amp; credits</summary><p>Stock references for layout demonstration; replace before customer launch. Remote images require internet access.</p><ul>'+''.join('<li><a href="'+escape(x['source'],quote=True)+'" target="_blank" rel="noopener noreferrer">'+escape(x['alt'])+'</a> — '+escape(x['author'])+'</li>' for x in selected)+'</ul><a href="https://unsplash.com/license" target="_blank" rel="noopener noreferrer">Unsplash licence</a></details>'
        foot=(directory/'footer.html').read_text(encoding='utf-8')
        end=foot.rfind('</footer>');foot=foot[:end]+'<div class="wrap">'+credits+'</div>'+foot[end:] if end>=0 else foot+credits
        doc=(directory/'TEMPLATE.md').read_text(encoding='utf-8')+'\n## 高清外链摄影版本（2026-11-07）\n已添加按行业选择的外链示意摄影，来源、作者、原始宽高见 images.json。首图/特色图维持比例、按位置裁切，非首屏延迟加载；加载失败显示缺图。照片不保存在仓库或导出包内，预览及导出需要联网。库存图不代表实际产品、人员、房源、客户项目或成果；未找到对应真实资产的占位保留，不冒用照片。\n'
        if write:
            p.write_text(home,encoding='utf-8');(directory/'footer.html').write_text(foot,encoding='utf-8');(directory/'images.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(directory/'TEMPLATE.md').write_text(doc,encoding='utf-8')
        print(slug+': '+str(len(selected))+' image sources, '+str(len(used))+' hero placements')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args();run(args.apply)
