#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=2:sw=2:expandtab

import os
import sys

from setuptools import setup, find_packages

sys.path.append('.')
from paths import metadata
from paths.metadata import get_version

VERSION = get_version()

def read(filename):
  with open(os.path.join(os.path.dirname(__file__), filename)) as f:
    return f.read()

setup_dict = dict(
    name=metadata.package,
    version=VERSION,
    author=metadata.authors[0],
    author_email=metadata.emails[0],
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.md'),
    download_url=metadata.url,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
    ],
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    entry_points={
    }
)


def main():
  setup(**setup_dict)

if __name__ == '__main__':
  main()
