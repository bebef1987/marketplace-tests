#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from unittestzero import Assert
from pages.desktop.consumer_pages.home import Home


class TestPurchaseApp:

    _app_name = 'Campfire'

    def test_that_purchasess_an_app_without_pre_auth(self, mozwebqa):
        home = Home(mozwebqa)

        home.go_to_homepage()
        home.login()

        Assert.true(home.is_the_current_page)

        search = home.header.search(self._app_name)
        Assert.true(search.is_the_current_page)

        details = search.results[0].clcik_name()
        pre_aproval = details.click_purchase()

        paypal_frame = pre_aproval.click_one_time_payment()

        paypall_popup = paypal_frame.login_to_paypal()
        Assert.true(paypall_popup.is_user_logged_into_paypal)

        paypall_popup.click_pay()
        paypall_popup.close_paypal_popup()

        Assert.true(details.is_app_installing())

        self.request_refund_procedure(mozwebqa, self._app_name)

    def request_refund_procedure(self, mozwebqa, app_name):
        home = Home(mozwebqa)
        home.go_to_homepage()

        if not home.footer.is_user_logged_in:
            home.login()
        Assert.true(home.is_the_current_page)
        Assert.true(home.footer.is_user_logged_in)

        account_history = home.footer.click_account_history()
        purchesed_apps = account_history.purchesed_apps

        stop = True
        idx = 0
        while stop:
            if purchesed_apps[idx].name == app_name:
                app_support = purchesed_apps[idx].click_request_support()

                request_refund = app_support.click_request_refund()
                account_history = request_refund.click_continue()
                stop = False
            else:
                idx = idx + 1

        Assert.equal(account_history.succsessful_notification_text, "Refund is being processed.")
