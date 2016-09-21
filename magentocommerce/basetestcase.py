#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import unittest
from selenium import webdriver
from tools.read_settings import get_settings
import os


BROWSER = get_settings()['browser']


class BaseTestCase(unittest.TestCase):
    @staticmethod
    def get_browser():
        if BROWSER == 'firefox':
            driver = webdriver.Firefox()
        elif BROWSER == 'chrome':
            os.path.abspath(os.path.join(__file__, '../..', 'chromedriver'))
            driver = webdriver.Chrome()
        else:
            raise Exception('browser not allowed')
        return driver

    @classmethod
    def SetUpClass(cls):
        cls.driver = cls.get_browser()
        cls.driver.implicitly_wait(get_settings()['wait'])
        cls.driver.maximize_window()
        # Open URL in the browser
        cls.driver.get(get_settings()['url'])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


