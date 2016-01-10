import codecs
import os

from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from pygments import highlight


INPUTDIR = '/pygments-lexer-babylon/test/inputfiles'
OUTPUTDIR = '/pygments-lexer-babylon/test/outputfiles'
TEMPLATE = '/pygments-lexer-babylon/test/template.html'


with open(TEMPLATE) as t:
    template = t.read()
formatter = get_formatter_by_name('html')


for f in os.listdir(INPUTDIR):
    fullpath = os.path.join(INPUTDIR, f)
    lexername = os.path.splitext(f)[1].lstrip('.')
    lexer = get_lexer_by_name(lexername)

    with open(fullpath, 'r') as fp:
        code = fp.read()

    highlighted = highlight(code, lexer, formatter)

    outname = os.path.join(OUTPUTDIR, '%s.html' % f)
    with codecs.open(outname, 'w', 'utf-8') as o:
        out = template.replace('---', highlighted)
        o.write(out)
