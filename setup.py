import os
from setuptools import setup

setup(
    name = "swing",
    version = "0.0.4",
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
