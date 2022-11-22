#!/usr/bin/env python
# coding=utf-8
import os

DOC_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def get_version():
    return __version__


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
