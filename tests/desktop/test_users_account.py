#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.desktop.home import Home


class TestAccounts:

    @pytest.mark.nondestructive
    def test_user_can_login_and_logout_using_browser_id(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.go_to_homepage()
        home_page.login()

        home_page.write_cookie_to_file()

    @pytest.mark.nondestructive
    def test_user_can_login_and_logout(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.go_to_homepage()
        home_page.read_cookie_from_file()
        home_page.go_to_homepage()

