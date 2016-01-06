from .lexer import BabylonLexer, BabylonHtmlLexer  # noqa


__all__ = ['BabylonLexer', 'BabylonHtmlLexer']


def register():
    from pygments.lexers import _mapping

    del _mapping.LEXERS['JavascriptLexer']
    del _mapping.LEXERS['HtmlLexer']

    _mapping.LEXERS['BabylonLexer'] = (
        'pygmentslexerbabylon', 'Babylon',
        ('js', 'jsx', 'javascript'),
        ('*.js', '*.jsx', '*.jsm'),
        ('application/javascript', 'application/x-javascript',
         'text/x-javascript', 'text/javascript'))
    _mapping.LEXERS['BabylonHtmlLexer'] = (
        'pygmentslexerbabylon', 'BabylonHTML',
        ('html',),
        ('*.html', '*.htm', '*.xhtml', '*.xslt'),
        ('text/html', 'application/xhtml+xml'))
