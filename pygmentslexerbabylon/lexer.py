from subprocess import check_output, STDOUT, CalledProcessError
import os
import json
import re

from pygments.lexer import Lexer
from pygments.token import (Text, Comment, String, Keyword, Name,
                            Number, Punctuation, Error, Operator)


JSFILE = os.path.join(os.path.dirname(__file__), 'runbabylon.js')
CMD = ['node', JSFILE]
RESERVED_WORDS = (
    'break', 'case', 'catch', 'continue', 'debugger', 'default', 'do', 'else',
    'finally', 'for', 'function', 'if', 'return', 'switch', 'throw', 'try',
    'var', 'let', 'const', 'while', 'with', 'new', 'this', 'super', 'class',
    'extends', 'export', 'import', 'yield', 'null', 'true', 'false', 'in',
    'instanceof', 'typeof', 'void', 'delete'
)
OPERATORS = (
    '=', '_=', '++/--', 'prefix', '||', '&&', '|', '^', '&', '==/!=', '</>',
    '<</>>', '+/-', '%', '*', '/', '**'
)
PUNCTUATORS = (
    '[', ']', '{', '}', '(', ')', ',', ';', ':', '::', '.', '?', '=>',
    'template', '...', '`', '${', '@'
)


def gettokentype(text, tokens, i):
    token = tokens[i]
    start, end, ttype = tuple(token)
    # value = text[start:end]
    prevtype = tokens[i - 1][2] if i > 0 else None
    nexttype = tokens[i + 1][2] if i < len(tokens) - 1 else None

    if ttype == 'CommentBlock':
        return Comment.Multiline
    elif ttype == 'CommentLine':
        return Comment.Single
    elif ttype == 'regexp':
        return String.Regex
    elif ttype == 'string':
        return String
    elif ttype == 'num':
        return Number

    # reserved words
    elif ttype in RESERVED_WORDS:
        return Keyword

    # jsx
    elif ttype in ('jsxTagStart', 'jsxTagEnd'):
        return Name.Tag
    elif ttype == '/' and any([prevtype == 'jsxTagStart',
                               nexttype == 'jsxTagEnd']):
        return Name.Tag
    elif ttype == 'jsxName' and any([prevtype == 'jsxTagStart',
                                     nexttype == 'jsxTagEnd']):
        return Name.Tag
    elif ttype == 'jsxName':
        return Name.Attribute

    # operators
    elif ttype in OPERATORS:
        return Operator

    # templates
    elif ttype == 'template':
        return String
    elif ttype == '${':
        return String.Interpol
    elif ttype == '}' and nexttype == 'template':
        return String.Interpol
    elif ttype == '`':
        return String.Backtick

    elif ttype in PUNCTUATORS:
        return Punctuation

    elif ttype == 'name':
        return Name.Other

    return Text


class BabylonLexer(Lexer):
    name = 'Babylon'

    def get_tokens_unprocessed(self, text):
        inp = bytes(text, encoding='utf-8')
        try:
            out = check_output(CMD, input=inp, stderr=STDOUT)
        except CalledProcessError as e:
            err = e.output.decode('utf-8')
            print(err)
            m = re.search(r'\((\d+):(\d+)\)', err)
            if m:
                row, col = m.groups()
                row, col = int(row), int(col)
                lines = text.split('\n')
                position = sum([len(l) + 1 for l in lines[:row - 1]])
                position += col
                yield (0, Text, text[:position])
                if text[position:]:
                    yield (position, Error, text[position:])
            else:
                yield (0, Error, text)
        else:
            tokens = json.loads(out.decode('utf-8'))

            position = 0
            for i, token in enumerate(tokens):
                start, end = token[0], token[1]

                if position < start:
                    yield (position, Text, text[position:start])
                    position = start - 1

                value = text[start:end]
                yield (position, gettokentype(text, tokens, i), value)
                position = end

            if position < len(text):
                yield (position, Text, text[position:])
