#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import json


def read(json_file):
    with open(json_file) as f:
        data = json.loads(f.read())
    return data
