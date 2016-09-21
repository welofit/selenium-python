#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import logging
from tools.read_settings import get_settings
import sys

settings = get_settings()
_logger = None


def read_log():
    log_level = settings['log_level']
    values_log_settings = {'WARN': logging.WARN, 'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'ERROR': logging.ERROR,
                           'CRITICAL': logging.CRITICAL}

    for k, v in values_log_settings.items():
        if log_level == k:
            log_level = v
            return log_level


def get_logger():
    global _logger
    if _logger is None:
        log = read_log()
        logging.basicConfig(stream=sys.stdout, level=log, format='[%(levelname)s] : %(message)s')
        _logger = logging.getLogger()

    return _logger
