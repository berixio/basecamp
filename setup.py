import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'basecamp',
    version = '0.0.1',
    author = 'Matias Saguir',
    author_email = 'mativs@gmail.com',
    description = ('Almost complete warapper around the Basecamp API. It is '
                  'written in Python and based upon the excellent ElementTree '
                  'package. Forked from the project '
                  'https://github.com/qpleple/basecamp-python-client'),
    license = "MIT",
    keywords = "basecamp api",
    url = 'https://github.com/nowherefarm/basecamp',
    packages=['basecamp'],
    long_description=read('README'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Bug Tracking',
    ],
)
