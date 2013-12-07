#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=2:sw=2:expandtab
"""paths.metadata

		Python utility module for dealing with local paths
"""

package = 'paths'
project = "paths"
project_no_spaces = project.replace(' ', '')
version = '0.0.1'
description = 'Python utility module for dealing with local paths'
authors = ['Nik Cubrilovic']
authors_string = ', '.join(authors)
emails = ['nikcub@gmail.com']
license = 'MIT'
copyright = '2013 ' + authors_string
url = 'http://github.com/nikcub/paths'

VERSION = (0, 0, 1, 'alpha', 1)

def get_version(version=None):
  if version is None:
    version = VERSION
  assert version[3] in ('alpha', 'beta', 'rc', 'final')
  parts = 2 if version[2] == 0 else 3
  main = '.'.join(str(x) for x in version[:parts])
  sub = ''
  if version[3] != 'final':
    mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
    sub = mapping[version[3]] + str(version[4])
  return main + sub

def get_status(version=None):
  if version is None:
    version = VERSION
  assert version[3] in ('alpha', 'beta', 'rc', 'final')
  return version[3]

