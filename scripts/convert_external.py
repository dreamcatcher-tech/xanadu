import os
import sys
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from html_to_md import MDConverter

NAV = """
[download](green/download/index.html)
[download](gold/download/index.html)
[history](history/index.html)
[Related Sites](related.html)

_[contact us](contact.html)_
or [![](images/cmn.gif)](http://www.blindpay.com/crit-me-now.cgi)

[![Golden Key](images/key.gif)](http://www.privacy.org/ipc/) [![Blue Ribbon](images/ribbon.gif)](http://mirrors.yahoo.com/eff/blueribbon.html)
"""

external_dir = 'external'
md_dir = 'md'
for fname in os.listdir(external_dir):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(external_dir, fname)
    with open(path, 'r', encoding='utf8', errors='ignore') as f:
        html = f.read()
    parser = MDConverter()
    parser.feed(html)
    md = parser.get_md()
    base = os.path.splitext(fname)[0]
    outname = base.upper() + '.md' if base.lower() == 'faq' else base + '.md'
    outpath = os.path.join(md_dir, outname)
    with open(outpath, 'w', encoding='utf8') as f:
        f.write(md)
        f.write('\n\n')
        f.write(NAV.strip())
        f.write('\n')
    print('wrote', outpath)
