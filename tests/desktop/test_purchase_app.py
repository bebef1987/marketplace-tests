#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from unittestzero import Assert
from pages.desktop.consumer_pages.home import Home
import time


class TestPurchaseApp:

    def test_that_purchasess_an_app_without_pre_auth(self, mozwebqa):
        home = Home(mozwebqa)

        home.go_to_homepage()
        home.login()

        Assert.true(home.is_the_current_page)

        search = home.header.search('Checkers')
        Assert.true(search.is_the_current_page)

        details = search.results[0].clcik_name()
        pre_aproval = details.click_purchase()

        paypal_frame = pre_aproval.click_one_time_payment()

        paypall_popup = paypal_frame.login_to_paypal()
        Assert.true(paypall_popup.is_user_logged_into_paypal)

        paypall_popup.click_pay()
        paypall_popup.close_paypal_popup()

        time.sleep(200)
