import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "swing",
    version = "0.0.3",
    author = "monklof",
    author_email = "monklof@gmail.com",
    description = ("Configuration switcher by an environment variable inspired by Common Lisp's envy"),
    license = "MIT",
    keywords = "configuration switcher, configuration management",
    url = "https://github.com/monklof/swing",
    packages=['swing', 'tests'],
    test_suite = 'nose.collector',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
