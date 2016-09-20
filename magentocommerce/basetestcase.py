#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import unittest
from selenium import webdriver
from tools.read_settings import get_settings

BROWSER = get_settings()['browser']


class BaseTestCase(unittest.TestCase):
    @staticmethod
    def get_browser():
        if BROWSER == 'firefox':
            driver = webdriver.Firefox()
        elif BROWSER == 'chrome':
            driver = webdriver.Chrome()
        else:
            raise Exception('browser not allowed')
        return driver

    def SetUp(self):
        self.driver = self.get_browser()
        self.driver.implicitly_wait(get_settings()['wait'])
        self.driver.maximize_window()
        self.driver.get(get_settings()['url'])

    def tearDown(self):
        self.driver.quit()

