#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Base(Page):

    def login(self, user="default"):
        self.header.click_login()

        credentials = self.testsetup.credentials[user]
        from browserid import BrowserID
        pop_up = BrowserID(self.selenium, self.timeout)
        pop_up.sign_in(credentials['email'], credentials['password'])
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.header.username == credentials['email'])

    def write_cookie_to_file(self):
        data = self.selenium.get_cookies()
        stream = file('/home/florinstrugariu/webqa/Marketplace/Bebe/marketplace-tests/tests/desktop/cookie.yaml', 'w')
        import yaml
        yaml.dump(data, stream)

    def read_cookie_from_file(self):
        stream = file('/home/florinstrugariu/webqa/Marketplace/Bebe/marketplace-tests/tests/desktop/cookie.yaml', 'r')
        import yaml
        data =  yaml.load(stream)
        
        for cookie in data:
            print self.selenium.current_url
            print cookie['domain']
            if cookie['domain'] == '.marketplace-dev.allizom.org':
                cookie['domain'] = 'marketplace-dev.allizom.org'
            self.selenium.add_cookie(cookie)


    @property
    def header(self):
        return self.HeaderRegion(self.testsetup)

    class HeaderRegion(Page):

        #Not LoggedIn
        _login_locator = (By.CSS_SELECTOR, "a.browserid")

        #LoggedIn
        _account_controller_locator = (By.CSS_SELECTOR, "#site-footer > a:nth-child(1)")
        _logout_locator = (By.CSS_SELECTOR, "li.nomenu.logout > a")

        def click_login(self):
            self.selenium.find_element(*self._login_locator).click()

        @property
        def username(self):
            return self.selenium.find_element(*self._account_controller_locator).text

        def click_logout(self):
            self.selenium.find_element(*self._logout_locator).click()
