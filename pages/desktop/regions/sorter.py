#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from pages.page import Page


class Sorter(Page):

    _sort_locator = (By.XPATH, "//div[@id='sorter']//li/a[normalize-space(text())='%s']")

    _selected_sort_by_locator = (By.CSS_SELECTOR, '#sorter > ul > li.selected > a')
    _sorter_header_locator = (By.CSS_SELECTOR, "#sorter > h3")

    _loading_balloon_locator = (By.CSS_SELECTOR, ".items")

    @property
    def sorter_header(self):
        return self.selenium.find_element(*self._sorter_header_locator).text

    def sort_by(self, type):
        """
        Method that accesses the sort region in the search results page
        :Args:
         - type - sort type that will be applied. String that contains the method name.
                  Available sort options can be found in the SortMethod class

         :Usage:
          - sort_by("Newest")
        """
        try:
            click_element = self.selenium.find_element(self._sort_locator[0], self._sort_locator[1] % type)
        except NoSuchElementException:
            Assert.fail("Sort method not available")

        click_element.click()
        WebDriverWait(self.selenium, 10).until(lambda s: self.selenium.execute_script("return jQuery.active == 0"))

    @property
    def sorted_by(self):
        return self.selenium.find_element(*self._selected_sort_by_locator).text

    class SortMethod:
        #consumer pages sort filters
        newest = "Newest"
        relevance = "Relevance"
        weekly_downloads = "Weekly Downloads"
        top_rated = "Top Rated"
        price = "Price"

        #developer pages sort filters
        name = "Name"
        created = "Created"
