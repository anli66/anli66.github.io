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
        self.ids=set()
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag=='a':
            self.links.append(attrs.get('href',''))
            self.active += attrs.get('aria-current')=='page'
        if tag=='img' and not attrs.get('src','').startswith('https:'):
            assert Path(attrs['src']).exists(), attrs['src']
        self.headings += tag=='h1'

pages=list(Path('.').glob('*.html'))
assert len(pages)==7
for page in pages:
    text=page.read_text(encoding='utf-8')
    parser=PageParser()
    parser.feed(text)
    assert parser.active==1 and parser.headings==1, page
    assert 'Lisowka' not in text, page
    assert 'collaborators.html' not in text, page
    for link in parser.links:
        if not link.startswith(('https:', 'mailto:', '#')):
            assert Path(link.split('#')[0]).exists(), (page,link)
        if not link.startswith(('https:', 'mailto:')) and '#' in link:
            target,fragment=link.split('#',1)
            target_parser=PageParser()
            target_parser.feed(Path(target or page).read_text(encoding='utf-8'))
            assert fragment in target_parser.ids, (page,link)
    if len(sys.argv)>1:
        with urlopen(sys.argv[1].rstrip('/')+'/'+page.name) as response:
            assert response.status==200, page
print('PASS: seven pages; all local links resolve; one main heading and active navigation item per page; name corrected.')
