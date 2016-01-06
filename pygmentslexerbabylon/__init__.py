from lexer import BabylonLexer  # noqa


__all__ = ['BabylonLexer']


def register():
    from pygments.lexers import _mapping

    del _mapping.LEXERS['JavascriptLexer']
    _mapping.LEXERS['BabylonLexer'] = (
        'pygmentslexerbabylon', 'Babylon',
        ('js', 'jsx', 'javascript'),
        ('*.js', '*.jsx', '*.jsm'),
        ('application/javascript', 'application/x-javascript',
         'text/x-javascript', 'text/javascript'))
