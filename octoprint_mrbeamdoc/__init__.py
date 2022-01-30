#!/usr/bin/env python
# coding=utf-8
import os

from __version import __version__

DOC_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def get_version():
    return __version__
