import os
import glob
import re
from html.parser import HTMLParser
from html import unescape

class HTMLToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.href_stack = []
        self.format_stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'br':
            self.out.append('  \n')
        elif tag == 'p':
            self.out.append('\n\n')
        elif tag in ['h1','h2','h3','h4','h5','h6']:
            level = int(tag[1])
            self.out.append('\n\n' + '#' * level + ' ')
        elif tag == 'a':
            self.href_stack.append(attrs.get('href',''))
            self.out.append('[')
        elif tag == 'img':
            src = attrs.get('src','')
            alt = attrs.get('alt','')
            self.out.append(f'![{alt}]({src})')
        elif tag in ['strong','b']:
            self.out.append('**')
            self.format_stack.append('**')
        elif tag in ['em','i','u']:
            ch = '*' if tag in ['em','i'] else '_'
            self.out.append(ch)
            self.format_stack.append(ch)
        elif tag == 'li':
            self.out.append('\n- ')
        elif tag == 'hr':
            self.out.append('\n\n---\n\n')

    def handle_endtag(self, tag):
        if tag == 'a':
            href = self.href_stack.pop() if self.href_stack else ''
            self.out.append(f']({href})')
        elif tag in ['strong','b','em','i','u']:
            if self.format_stack:
                ch = self.format_stack.pop()
                self.out.append(ch)
        elif tag == 'p':
            self.out.append('\n\n')
        elif tag in ['h1','h2','h3','h4','h5','h6']:
            self.out.append('\n\n')

    def handle_data(self, data):
        self.out.append(unescape(data))

    def get_markdown(self):
        text = ''.join(self.out)
        text = re.sub(r'[ \t\r\f\v]+', ' ', text)
        text = re.sub(r' *\n *', '\n', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = '\n'.join(line.strip() for line in text.splitlines())
        return text.strip() + '\n'

def convert_file(html_path, md_root='md'):
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    parser = HTMLToMarkdown()
    parser.feed(html)
    md_text = parser.get_markdown()

    rel_path = os.path.relpath(html_path)
    parts = rel_path.split(os.sep)
    parts.insert(0, md_root)
    parts[-1] = os.path.splitext(parts[-1])[0] + '.md'
    out_path = os.path.join(*parts)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md_text)
    print('Converted', html_path, '->', out_path)

if __name__ == '__main__':
    root = 'udanax'
    for html_file in glob.glob(os.path.join(root, '**', '*.html'), recursive=True):
        convert_file(html_file)
