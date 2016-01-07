import sys
import pygments.cmdline


def main():
    try:
        from pygmentslexerbabylon import register
        register()
        sys.exit(pygments.cmdline.main(sys.argv))
    except KeyboardInterrupt:
        sys.exit(1)
