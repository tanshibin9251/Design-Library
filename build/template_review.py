"""Read-only structural signals for library browsing and the review inventory.

These signals are not a browser accessibility/functional certification.
"""
from html.parser import HTMLParser
from pathlib import Path
import re


class Signals(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = 0
        self.remote_images = 0
        self.placeholders = 0
        self.forms = 0
        self.blocked_forms = 0
        self.vectors = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'img':
            self.images += 1
            self.remote_images += bool(re.match(r'https?://', attrs.get('src', '')))
        if tag == 'svg':
            self.vectors += 1
        if 'ph' in attrs.get('class', '').split():
            self.placeholders += 1
        if tag == 'form':
            self.forms += 1
            self.blocked_forms += 'return false' in attrs.get('onsubmit', '')


def inspect_template(directory):
    directory = Path(directory)
    signals = Signals()
    for page in sorted((directory / 'pages').glob('*.html')):
        signals.feed(page.read_text(encoding='utf-8'))
    return dict(images=signals.images, remote_images=signals.remote_images,
                placeholders=signals.placeholders, forms=signals.forms,
                blocked_forms=signals.blocked_forms, vectors=signals.vectors,
                check='Source inspection; browser behaviour not certified')
