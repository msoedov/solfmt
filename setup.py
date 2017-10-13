# -*- coding: utf-8 -*-
from setuptools import setup

try:
    long_description = open("Readme.md").read()
except IOError:
    long_description = """
"""

setup(
    name="solfmt",
    version="0.1.1",
    description="Solfmt code formatter for Solidity",
    license="MIT",
    author="Alex Myasoedov",
    author_email="msoedov@gmail.com",
    packages=['.'],
    install_requires=['fire'],
    entry_points={
        'console_scripts': ['solfmt=app:entrypoint'],
    },
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ])
