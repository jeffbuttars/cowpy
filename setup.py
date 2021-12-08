#!/usr/bin/env python

from setuptools import setup  # type: ignore

__version__ = "1.1.3"

setup(
    name="cowpy",
    description="A cowsay clone for python in one file.",
    author="Jeff Buttars",
    author_email="jeffbuttars@gmail.com",
    url="https://github.com/jeffbuttars/cowpy",
    python_requires=">=3.0",
    version=__version__,
    packages=["cowpy"],
    license="Apache License 2.0",
    license_files=("LICENSE.md",),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    scripts=["scripts/cowpy", "scripts/cowpy.bat"],
)
