# pygments-lexer-babylon
A javascript lexer for Pygments that uses the babylon parser


## WARNING!
`Node.js` must be installed to use this package and must be available as `nodejs`. If the following command works,
you are most probably OK:
```
nodejs -v
```

## Why?
Pygments can not properly highlight new and shiny `javascript` (particulary `jsx`).
Until all these features are implemented in Pygments, you can use this package as a fallback.
Also, it is a good fun to experiment with various technologies :wink:.

## Install
Nothing too much here, apart from the `Node.js` dependency:
```
pip install pygments-lexer-babylon
```
This will install `Pygments` for you (>=2.0), so if something depends on an older version, `virtualenv` is recommended.
(Or use `docker`...)

## Usage
The importable name of the package: `pygmentslexerbabylon`.
It provides two lexers: `BabylonLexer` and `BabylonHtmlLexer`. The latter is needed because the built in
`HtmlLexer` hard codes the usage of `JavascriptLexer` between `<script>` tags.

If you have "manual" control over which lexer to use, do something like this:
```python
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygmentslexerbabylon import BabylonLexer

lexer = BabylonLexer()  # You select it manually...
formatter = HtmlFormatter(linenos=True, cssclass="source")
code = '<ReactComponent/>'
result = highlight(code, lexer, formatter)
```

In some cases you do not have control over the selected lexer. Let's say, you use Markdown, which turns out to
use code like this:
```python
from pygments.lexers import get_lexer_by_name, guess_lexer

try:
    lexer = get_lexer_by_name(self.lang)
except ValueError:
    try:
        lexer = guess_lexer(self.src)
    except ValueError:
        lexer = get_lexer_by_name('text')
```
What you can do in this case is "register" our lexers, so `Pygments` will know that if it
gets a `lang` like `js` or `jsx`, the lexer to return is our `BabylonLexer`. (Same for `html`)
Put the following somewhere in your code (before using `Pygments`):
```python
from pygmentslexerbabylon import register
register()
```

If you use the `pygmentize` command, be very careful: this package overwrites
the original script and uses the new lexers. If you do not like this behavior,
send an issue and we can figure out a better way.

## Gotchas
- It is a bit slower than `Pygments`...
- May fail for really large files (0.5 MB worked for me though)
- Produces slightly different result than the original `Pygments` lexer
- Overwrites the `pygmentize` command
