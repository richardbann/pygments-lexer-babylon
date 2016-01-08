import codecs

from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from pygments import highlight


JSX = '/pygments-lexer-babylon/test/input.jsx'
HTML = '/pygments-lexer-babylon/test/input.html'
TEMPLATE = '/pygments-lexer-babylon/test/template.html'
OUT_JSX = '/pygments-lexer-babylon/test/jsx_output.html'
OUT_HTML = '/pygments-lexer-babylon/test/html_output.html'

with open(JSX, 'r') as f:
    code = f.read()


lexer = get_lexer_by_name('jsx')
formatter = get_formatter_by_name('html')
highlighted = highlight(code, lexer, formatter)


with open(TEMPLATE) as t:
    template = t.read()


with codecs.open(OUT_JSX, 'w', 'utf-8') as f:
    template = template.replace('---', highlighted)
    f.write(template)


with open(HTML, 'r') as f:
    code = f.read()


lexer = get_lexer_by_name('htmlx')
formatter = get_formatter_by_name('html')
highlighted = highlight(code, lexer, formatter)


with open(TEMPLATE) as t:
    template = t.read()


with codecs.open(OUT_HTML, 'w', 'utf-8') as f:
    template = template.replace('---', highlighted)
    f.write(template)
