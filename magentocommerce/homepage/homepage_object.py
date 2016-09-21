#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import sys
import os

sys.path.append(os.path.abspath(os.path.join(__file__, '../..')))

from base import BasePage
from base import InvalidPageException


class HomePage(BasePage):
    # get locator o homepage
    _homepage_div_locator = 'div.slideshow-container'

    # supuestamente hay que añadir un init..

    def _validate_page(self, driver):
        try:
            driver.find_element_by_class_name(self._homepage_div_locator)
        except:
            raise InvalidPageException("Page not loaded")


