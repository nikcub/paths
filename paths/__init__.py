#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=2:sw=2:expandtab
"""
  paths.__init__.py

  Python utility module for dealing with local paths

  :copyright: Copyright (C) 2013 Nik Cubrilovic and others, see AUTHORS
  :license: MIT, see LICENSE for more details.
"""

import os
import inspect

from .metadata import get_version

__appname__ = 'paths'
__version__ = get_version()
__author__ = 'Nik Cubrilovic <nikcub@gmail.com>'
__email__ = 'nikcub@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2013, Nik Cubrilovic. All rights reserved.'

# __all__ = ['find', 'Locate']

def file():
  return get_calling_file()
  # print inspect.stack()[-1][1]
  # print inspect.getfile(inspect.stack()[0]) # script filename (usually with path)
  print type(filename)
  print os.path.abspath(filename) # script directory
  # get_calling_file()
  # print inspect.stack()[1][3]
  return os.path.basename(__file__)

def dir():
  return get_calling_dir()

def find(basepath, pattern=None, callback=None):
  for root, dirs, files in os.walk(basepath):
    for basename in files:
      if fnmatch.fnmatch(basename, pattern):
        filename = os.path.join(root, basename)
        yield filename

def expand(path):
  return os.path.expandpath(os.path.expandvars(os.path.expanduser))

def get_calling_file():
  frame,filename,line_number,function_name,lines,index=inspect.getouterframes(inspect.currentframe())[2]
  # print(frame,filename,line_number,function_name,lines,index)
  return os.path.abspath(filename)

def get_calling_dir():
  return os.path.dirname(os.path.abspath(inspect.getouterframes(inspect.currentframe())[2][1]))

def find_up(basepath, pattern=None):
  pass

def is_exe(fpath):
  return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

def which(program):
  fpath, fname = os.path.split(program)
  if fpath:
    if is_exe(program):
      return program
  else:
    for path in os.environ["PATH"].split(os.pathsep):
      path = path.strip('"')
      exe_file = os.path.join(path, program)
      if is_exe(exe_file):
        return exe_file

  return None

def get_cwd():
  if not '__file__' in globals():
    cwd = os.path.abspath(os.getcwd())
  else:
    cwd = os.path.dirname(os.path.abspath(__file__))
  return os.path.realpath(cwd)

def find_executable(executable, path=None):
  """Tries to find 'executable' in the directories listed in 'path'.

  A string listing directories separated by 'os.pathsep'; defaults to
  os.environ['PATH'].  Returns the complete filename or None if not found.
  """
  if path is None:
    path = os.environ['PATH']
  paths = path.split(os.pathsep)
  base, ext = os.path.splitext(executable)

  if (sys.platform == 'win32' or os.name == 'os2') and (ext != '.exe'):
    executable = executable + '.exe'

  if not os.path.isfile(executable):
    for p in paths:
      f = os.path.join(p, executable)
      if os.path.isfile(f):
        # the file exists, we have a shot at spawn working
        return f
    return None
  else:
    return executable


class Locate():
  def __init__(self, cr):
    self.cr = cr

  def __enter__(self):
    self.cr.save()
    return self.cr

  def __exit__(self, type, value, traceback):
    self.cr.restore()

