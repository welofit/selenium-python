#!/usr/bin/python
# _*_ coding: UTF-8 _*_

from abc import abstractmethod


class BasePage(object):

    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return


class InvalidPageException(Exception):
    pass
