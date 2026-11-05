from pathlib import Path
from html.parser import HTMLParser
from urllib.request import urlopen
import sys

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.active=0
        self.headings=0
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='a':
            self.links.append(attrs.get('href',''))
            self.active += attrs.get('aria-current')=='page'
        self.headings += tag=='h1'

pages=list(Path('.').glob('*.html'))
assert len(pages)==6
for page in pages:
    text=page.read_text(encoding='utf-8')
    parser=PageParser()
    parser.feed(text)
    assert parser.active==1 and parser.headings==1, page
    assert 'Lisowka' not in text, page
    for link in parser.links:
        if not link.startswith(('https:', '#')):
            assert Path(link).exists(), (page,link)
    if len(sys.argv)>1:
        with urlopen(sys.argv[1].rstrip('/')+'/'+page.name) as response:
            assert response.status==200, page
print('PASS: six pages; all local links resolve; one main heading and active navigation item per page; name corrected.')
