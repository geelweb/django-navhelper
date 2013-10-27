#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# License: MIT
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""
django navhelper setup script
"""

__author__ = "Guillaume Luchet <guillaume@geelweb.org>"
__version__ = "0.1"

import os, sys
from setuptools import setup, find_packages

author_data = __author__.split(" ")
maintainer = " ".join(author_data[0:-1])
maintainer_email = author_data[-1]
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

if __name__ == "__main__":
    setup(
        name="django-navhelper",
        version=__version__,
        description="Django template tags designed to help the navigation rendering",
        long_description=README,
        author=maintainer,
        author_email=maintainer_email,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        url="https://github.com/geelweb/django-navhelper",
        download_url="https://github.com/geelweb/django-navhelper/tarball/%s" % __version__,
        license='MIT',
        namespace_packages = ['geelweb', 'geelweb.django'],
        packages=find_packages('src'),
        package_dir = {'':'src'},
        package_data = {},
        keywords = ['django', 'menu', 'navigation'],
        )


