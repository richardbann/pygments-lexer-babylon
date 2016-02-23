import os

import pytest
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from pygments import highlight


def test_works():
    assert 1 == 1


def test_jsx():
    path = '/pygments-lexer-babylon/test/inputfiles/example.jsx'
    with open(path, 'r') as fp:
        code = fp.read()
    lexer = get_lexer_by_name('jsx')
    formatter = get_formatter_by_name('testcase')
    highlighted = highlight(code, lexer, formatter)
    print(highlighted)


def test_syntax_error_in_jsx():
    path = '/pygments-lexer-babylon/test/inputfiles/syntaxerror.jsx'
    with open(path, 'r') as fp:
        code = fp.read()
    lexer = get_lexer_by_name('jsx')
    formatter = get_formatter_by_name('testcase')
    highlighted = highlight(code, lexer, formatter)
    print(highlighted)


def test_wrong_nodecommand():
    os.environ['PYGMENTS_NODE_COMMAND'] = 'no_such_command'
    lexer = get_lexer_by_name('jsx')
    formatter = get_formatter_by_name('testcase')
    with pytest.raises(OSError) as excinfo:
        highlight('', lexer, formatter)
    assert 'PYGMENTS_NODE_COMMAND' in str(excinfo.value)
    assert 'no_such_command' in str(excinfo.value)
