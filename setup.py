#!/usr/bin/env python

from setuptools import setup

__version__ = "1.1.1"

setup(name="cowpy",
      description="A cowsay clone for python in one file.",
      author="Jeff Buttars",
      author_email="jeffbuttars@gmail.com",
      url="https://github.com/jeffbuttars/cowpy",
      version=__version__,
      packages=["cowpy"],
      license="MIT",
      license_files=("LICENSE.md",),
      scripts=["scripts/cowpy", "scripts/cowpy.bat"]
      )
