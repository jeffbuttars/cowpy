#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

__version__ = '1.1.0'

setup(name='cowpy',
      description="A cowsay clone for python in one file.",
      author="Jeff Buttars",
      author_email="jeffbuttars@gmail.com",
      url="https://github.com/jeffbuttars/cowpy",
      version=__version__,
      packages=['cowpy'],
      scripts=['scripts/cowpy', 'scripts/cowpy.bat']
      )
