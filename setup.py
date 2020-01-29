import os
import sys

from setuptools import setup, find_packages

_INSTALL_REQUIRES = [
    "requests",
    "pytest",
    "munch"
]

setup(name="assigment1",
    classifiers = [
          "Programming Language :: Python :: 3.8",
          ],
    description="assigment1",
    license="BSD3",
    author="Niv",
    author_email="nivw2008@fastmail.fm",
    version="0.0.1",
    packages=find_packages(exclude=["tests"]),
    install_requires=_INSTALL_REQUIRES,
    scripts=[],
    namespace_packages=[]
    )