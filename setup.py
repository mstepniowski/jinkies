#!/usr/bin/env python
from distutils.core import setup


setup(
    name='jinkies',
    version='0.1',
    description='Jinkies!',
    author='Jason Moiron',
    author_email='jmoiron@jmoiron.net',
    url='http://github.com/jmoiron/jinkies',
    platforms='Cross Platform',
    install_requires=["docopt>=0.6"],
    py_modules=['jinkies'],
    entry_points = {
        'console_scripts': ['jinkies=jinkies:main']
    }
)
