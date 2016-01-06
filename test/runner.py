import codecs

from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from pygments import highlight

from pygmentslexerbabylon import register
register()

JSX = '/pygments-lexer-babylon/test/input.jsx'
TEMPLATE = '/pygments-lexer-babylon/test/template.html'
OUT = '/pygments-lexer-babylon/test/output.html'

with open(JSX, 'r') as f:
    code = f.read()


lexer = get_lexer_by_name('jsx')
formatter = get_formatter_by_name('html')
highlighted = highlight(code, lexer, formatter)


with open(TEMPLATE) as t:
    template = t.read()


with codecs.open(OUT, 'w', 'utf-8') as f:
    template = template.replace('---', highlighted)
    f.write(template)
