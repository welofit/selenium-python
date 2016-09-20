#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import ConfigParser
import os

_settings = None
SECTION = 'GLOBAL'
main_directory = os.path.split(os.path.abspath(__file__))[0]


def get_settings():
    global _settings
    if _settings is None:
        _settings = ConfigParser.SafeConfigParser()
        settings_path = os.path.abspath(os.path.join(main_directory, '../', 'settings.cfg'))
        _settings.read(settings_path)

    settings_conf = {'url': _settings.get(SECTION, 'url'), 'browser': _settings.get(SECTION, 'browser'),
                     'so': _settings.get(SECTION, 'so')}

    return settings_conf

