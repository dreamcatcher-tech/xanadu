from html.parser import HTMLParser
import sys

class MDConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.md = []
        self.href_stack = []
        self.list_depth = 0
        self.in_pre = False
        self.skip_pre = True
        self.skip_content = False
        self.in_head = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "head":
            self.in_head = True
            return
        if self.in_head:
            return
        if tag in ("h1","h2","h3","h4","h5","h6"):
            level = int(tag[1])
            self.md.append('\n' + '#' * level + ' ')
        elif tag == "p":
            self.md.append('\n\n')
        elif tag == "br":
            self.md.append('\n')
        elif tag == "hr":
            self.md.append('\n\n---\n\n')
        elif tag == "b":
            self.md.append('**')
        elif tag == "i" or tag == "em":
            self.md.append('*')
        elif tag == "pre":
            if self.skip_pre:
                self.skip_pre = False
                self.in_pre = False
                self.skip_content = True
            else:
                self.in_pre = True
                self.md.append('\n\n```\n')
        elif tag == "img":
            alt = ''
            src = ''
            for k,v in attrs:
                if k.lower() == 'alt':
                    alt = v
                elif k.lower() == 'src':
                    src = v
            self.md.append(f'![{alt}]({src})')
        elif tag == "a":
            href = ''
            for k,v in attrs:
                if k.lower() == 'href':
                    href = v
            if href and not href.startswith('#'):
                self.md.append('[')
                self.href_stack.append(href)
            else:
                self.href_stack.append(None)
        elif tag in ("ul","ol"):
            self.list_depth += 1
        elif tag == "li":
            self.md.append('\n' + '  '* (self.list_depth-1) + '- ')

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "head":
            self.in_head = False
            return
        if self.in_head:
            return
        if tag in ("b",):
            self.md.append('**')
        elif tag in ("i","em"):
            self.md.append('*')
        elif tag == "pre":
            if self.skip_content:
                self.skip_content = False
            elif self.in_pre:
                self.in_pre = False
                self.md.append('\n```\n')
        elif tag == "a":
            href = self.href_stack.pop() if self.href_stack else None
            if href:
                self.md.append(f']({href})')
        elif tag in ("ul","ol"):
            if self.list_depth > 0:
                self.list_depth -= 1

    def handle_data(self, data):
        if not self.skip_content and not self.in_head:
            self.md.append(data)

    def handle_entityref(self, name):
        entity_map = {'nbsp': ' ', 'amp': '&', 'lt': '<', 'gt': '>'}
        self.md.append(entity_map.get(name, ''))

    def get_md(self):
        text = ''.join(self.md)
        return text.strip()

if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path, 'r', encoding='utf8', errors='ignore') as f:
            html = f.read()
        parser = MDConverter()
        parser.feed(html)
        md = parser.get_md()
        print(md)
