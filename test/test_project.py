import os

import pytest
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from pygments import highlight


thisdir = os.path.dirname(__file__)
inputdir = os.path.join(thisdir, 'inputfiles')
expdir = os.path.join(thisdir, 'expected')


def hljsx(code):
    lexer = get_lexer_by_name('jsx')
    formatter = get_formatter_by_name('html')
    hl = highlight(code, lexer, formatter)
    if isinstance(hl, str):
        return hl
    return hl.encode('utf-8')


def test_works():
    assert 1 == 1


def get_code(filename):
    path = os.path.join(inputdir, filename)
    with open(path, 'r') as f:
        return f.read()


def get_expected(filename):
    path = os.path.join(expdir, filename)
    with open(path, 'r') as f:
        return f.read()


def test_jsx():
    fn = 'example.jsx'
    code = get_code(fn)
    assert hljsx(code) == get_expected(fn)


def test_syntax_error_in_jsx():
    fn = 'syntaxerror.jsx'
    code = get_code(fn)
    assert hljsx(code) == get_expected(fn)


def test_wrong_nodecommand():
    fake_command = 'fake_command'
    os.environ['PYGMENTS_NODE_COMMAND'] = fake_command
    with pytest.raises(OSError) as excinfo:
        hljsx('')
    assert 'PYGMENTS_NODE_COMMAND' in str(excinfo.value)
    assert fake_command in str(excinfo.value)
