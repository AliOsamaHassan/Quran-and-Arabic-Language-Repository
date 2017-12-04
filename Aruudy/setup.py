import os
from setuptools import setup

def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except IOError:
        return ''

setup(
    name = "aruudy",
    version = "0.1.2",
    author = "Abdelkrime Aries",
    author_email = "kariminfo0@gmail.com",
    description = ("Arabic poetry package"),
    license = "Apache-2.0",
    keywords = "arabic nlp languages poetry",
    url = "https://github.com/kariminf/aruudy",
    packages=['aruudy', 'aruudy.poetry'],
    scripts=['exec/aruudy'],
    long_description=readme()
)
