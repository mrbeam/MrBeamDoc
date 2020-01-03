#!/usr/bin/env python
# coding=utf-8

import octoprint.plugin


from __version import __version__


class MrBeamDocPlugin(octoprint.plugin.AssetPlugin):
    pass


__plugin_name__ = "MrBeamDoc"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = MrBeamDocPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {}
