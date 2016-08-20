import time

from .base import FunctionalTest

TEST_EMAIL = "edith@mockmyid.com"
class LoginTest(FunctionalTest):
    def test_login_with_persona_first_time(self):
        # Edith goes to the awesome superlists site
        # and notices a 'sign in' link for the first time
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        # A persona login box appers
        self.switch_to_new_window("Mozilla Persona")

        # Edith logis in with her email address
        ## use mockid.com for test email
        self.browser.find_element_by_id('authentication_email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()

        # The persona window closes
        self.switch_to_new_window("To-Do")

        # she can see that she is logged in
        self.wait_to_be_logged_in(TEST_EMAIL)

        # Refreshing the window she sees that it's a real session log in
        # not a one - off for that page
        self.browser.refresh()
        self.wait_to_be_logged_in(TEST_EMAIL)

        # Terrified of this new feature she reflexively chlicks log out
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(TEST_EMAIL)

        # The logged out status also persists after refreshes
        self.browser.refresh()
        self.wait_to_be_logged_out(TEST_EMAIL)

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to.window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail("could not find window")
