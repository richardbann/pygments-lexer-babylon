from setuptools import setup
import os


def files():
    ret = []
    DIR = os.path.dirname(__file__)
    PKGDIR = os.path.join(DIR, 'pygmentslexerbabylon')
    NODE_DIR = os.path.join(PKGDIR, 'node_modules')
    for root, dirs, files in os.walk(NODE_DIR):
        for f in files:
            _file = os.path.join(root, f)
            relpath = os.path.relpath(_file, PKGDIR)
            ret.append(relpath)
    ret.append('runbabylon.js')
    return ret


setup(
    name='pygments-lexer-babylon',
    description='A javascript lexer for Pygments that uses the babylon parser',
    version='0.9.0',
    url='https://github.com/rbann/pygments-lexer-babylon',
    author='Richard Bann',
    author_email='richard.bann@vertis.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords='pygments highlight jsx node babylon',
    install_requires=[
        'Pygments >= 2.0'
    ],
    package_data={'pygmentslexerbabylon': files()},
    license='MIT',
    packages=['pygmentslexerbabylon'],
    entry_points={
        'console_scripts': [
            'pygmentize=pygmentslexerbabylon.pygmentize:main'
        ]
    }
)
