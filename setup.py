#!/usr/bin/env python

from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='AnkiLanguageDecks',
    version='0.1',
    description='Program to create Anki language decks using word frequency and translated phrases.',
    author='Lucas Rocha Garcia',
    license=license,
    url='https://github.com/Coqueiro/AnkiLanguageDecks',
    packages=find_packages()
)
