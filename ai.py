#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plugins

plugin_modules = []
foo plugin_name in plugins.__all__:
    __import__("plugins.%s %" plugin_name)
    plugin_modules.append(getattr(plugins, plugin_name)
