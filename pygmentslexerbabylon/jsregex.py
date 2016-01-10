import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import String, Text


__all__ = ['JSRegexLexer']


R = String.Regex


class JSRegexLexer(RegexLexer):
    name = 'Javascript Regex'
    aliases = ['jsre']
    filenames = ['*.jsre']

    flags = re.DOTALL | re.UNICODE | re.MULTILINE

    tokens = {
        'root': [
            (r'/', R.Delimiter, 'inside'),
            (r'[^/]+', Text),
        ],
        'inside': [
            # char classes
            (r'\.|\\d|\\D|\\w|\\W|\\s|\\S|\\t|\\r|\\n|\\v|\\f', R.Class),
            (r'\[\\b\]|\\0|\\c[A-Z]|\\x\d\d|\\u[0-9a-fA-F]{4}', R.Class),
            (r'\\u\{[0-9a-fA-F]{4}\}', R.Class),

            # escaping
            (r'(\\)(\*|\.|/|\\)', bygroups(R.Escape, R.Pattern)),

            (r'(/)([gimuy]*)', bygroups(R.Delimiter, R.Modifier), '#pop'),

            (r'[^/+]', R.Pattern),
        ]
    }
