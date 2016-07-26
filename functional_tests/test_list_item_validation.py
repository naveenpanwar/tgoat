from unittest import skip

from .base import FunctionalTest
from lists.forms import DUPLICATE_ITEM_ERROR, EMPTY_ITEM_ERROR

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blark
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for item, which now works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second black list item
        self.get_item_input_box().send_keys('\n')
         
        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        #Edith goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        #She accidentally tries to enter a duplicate Item
        self.get_item_input_box().send_keys('Buy wellies\n')

        #She sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, DUPLICATE_ITEM_ERROR)

    def test_error_messages_are_cleared_on_input(self):
        #Edith starts a new list in a way that causes validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys("\n")
        error = self.find_element_by_css_selector(".has_error")
        self.assertTrue(error.is_displayed())

        # She starts typing in the inputbox to clear the error
        self.get_item_input_box().send_keys("a")

        # She is pleased to see that the error message disappers
        error = self.find_element_by_css_selector(".has_error")
        self.assertFalse(error.is_displayed())
