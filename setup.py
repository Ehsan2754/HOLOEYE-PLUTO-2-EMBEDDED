#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

from io import open
import os
import setuptools

CLASSIFIERS = []
INSTALL_REQUIRES = []

BASE_DIR = os.path.dirname(__file__)
PKG_DIR = os.path.join(BASE_DIR, "holoeye_embedded")

meta = {}
with open(os.path.join(PKG_DIR, "__meta__.py")) as f:
    exec(f.read(), meta)

with open(os.path.join(BASE_DIR, "README.md")) as f:
    long_description = f.read()


setuptools.setup(
    name=meta["__packagename__"],
    version=meta["__version__"],

    description=meta["__summary__"],
    long_description=long_description,
    license=meta["__license__"],
    url=meta["__uri__"],

    author=meta["__author__"],
    author_email=meta["__email__"],

    classifiers=CLASSIFIERS,

    install_requires=INSTALL_REQUIRES,

    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
)
