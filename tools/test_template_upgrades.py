"""Regression checks for shared template enhancements and curated photography."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT/'build'))
import dlib
import site_export

class Elements(HTMLParser):
    def __init__(self):
        super().__init__();self.tags=[]
    def handle_starttag(self,tag,attrs):
        self.tags.append((tag,dict(attrs)))

class TemplateUpgrades(unittest.TestCase):
    def test_every_declared_page_and_local_destination_exists(self):
        failures=[]
        for slug in dlib.template_slugs():
            x=dlib.load_template(slug);available={p['slug'] for p in x['pagelist']}
            self.assertEqual(available,set(x['pages']),slug)
            for source in [x['nav'],x['foot'],*x['pages'].values()]:
                for target in re.findall(r'\{\{p:([^}]+)\}\}',source):
                    if target not in available:failures.append(slug+': '+target)
        self.assertEqual([],sorted(set(failures)))

    def test_shared_behaviour_is_exported_and_demo_forms_opt_in(self):
        for slug in dlib.template_slugs():
            x=dlib.load_template(slug)
            if slug=='cafe-bakery':continue
            self.assertIn('data-dl-template="'+slug+'"',x['nav'])
            if '<footer' in x['foot']:
                self.assertIn('data-dl-footer',x['foot'])
            html=site_export.page_file(x,site_export.settings(x),'home','html')
            self.assertIn('template behaviour',html)
            self.assertIn('Nothing was sent, charged, booked or stored.',html)
            for page in x['pages'].values():
                self.assertNotIn('onsubmit="return false"',page)

    def test_remote_sources_and_delivered_resolution(self):
        for p in (ROOT/'library/templates').glob('*/images.json'):
            m=json.loads(p.read_text(encoding='utf-8'))
            for photo in m['images']:
                self.assertGreaterEqual(min(photo['original_width'],photo['original_height']),1080,p)
                self.assertGreaterEqual(max(photo['original_width'],photo['original_height']),1920,p)
                self.assertTrue(photo['url'].startswith('https://images.unsplash.com/'))
                self.assertTrue(photo['source'].startswith('https://unsplash.com/photos/'))
                self.assertTrue(photo['author'])
            x=dlib.load_template(p.parent.name)
            for photo in m['images']:
                self.assertIn(photo['url'],''.join(x['pages'].values()))
                self.assertIn(photo['source'],x['foot'])

    def test_explicit_bug_regressions(self):
        x=dlib.load_template('modern-saas')
        self.assertIn('{{p:demo}}',x['pages']['home'])
        self.assertNotIn('Watch 2-min demo',x['pages']['home'])
        self.assertIn('demo',{p['slug'] for p in x['pagelist']})
        self.assertEqual(1,len([p for p in x['pagelist'] if p['label']=='Features']))
        x=dlib.load_template('restaurant-warm')
        self.assertNotIn('var t=8,n=[]',x['pages']['home'])
        self.assertNotIn('RM 579',x['pages']['checkout'])
        self.assertNotIn('Card number',x['pages']['checkout'])
        self.assertNotIn('Wash cold',x['pages']['product'])
        self.assertIn('data-rw-product="7"',x['pages']['shop'])

if __name__=='__main__':unittest.main()
