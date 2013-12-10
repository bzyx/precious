import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

project = "precious"

setup(
    name = "precious",
    version = "0.0.1",
    author = "Marcin Jabrzyk, Marius Rejdak",
    author_email = "marcin.Jabrzyk@gmail.com, mariuswol@gmail.com",
    description = ("Python Continuous Integration Server"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/precious",
    packages=['precious', 'tests'],
    include_package_data=True,
    long_description=read('README.md'),
    install_requires = read("requirements.txt"),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers"
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities"
        "License :: OSI Approved :: BSD License",
    ],
)
