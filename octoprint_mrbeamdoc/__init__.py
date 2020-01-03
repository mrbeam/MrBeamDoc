#!/usr/bin/env python
# coding=utf-8



from __version import __version__


class MrBeamDocPlugin(object):

    def __init__(self):
        pass

    def initialize(self):
        pass


__plugin_name__ = "MrBeamDoc"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = MrBeamDocPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {}
