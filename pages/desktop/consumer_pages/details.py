#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page
from pages.desktop.consumer_pages.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common import by


class Details(Base):
    """APP details page
    https://marketplace-dev.allizom.org/en-US/app/ app name
    app_name => the name of the app displayed
    """

    _purchase_locator = (By.CSS_SELECTOR, "section.product-details > div.actions > a.premium")

    def __init__(self, testsetup, app_name=False):
        Base.__init__(self, testsetup)
        if app_name:
            self._page_title = "%s | Mozilla Marketplace" % app_name

    def click_purchase(self):
        self.selenium.find_element(*self._purchase_locator).click()
        return self.PreAproval(self.testsetup)

    class PreAproval(Page):
        _root_locator = (By.ID, 'pay')

        _one_time_payment_locator = (By.ID, 'payment-confirm')

        def __init__(self, testsetup):
            Page.__init__(self, testsetup)
            self._root_element = self.selenium.find_element(*self._root_locator)

        def click_one_time_payment(self):
            self._root_element.find_element(*self._one_time_payment_locator).click()

            from pages.desktop.consumer_pages.paypall_frame import PayPalFrame
            return PayPalFrame(self.testsetup)
