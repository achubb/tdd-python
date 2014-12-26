from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        # New todo app - check out the homepage
        self.browser.get('http://localhost:8000')

        # The page title and header mention To-Do
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User is invited to enter a todo item straight away

        # User enters "Buy Peacock Feathers"

        # When user hits enter the page updates and now reads:
        # "1. Buy Peacock Feathers" as an item in the todo list

        # There is still a text box inviting the user to add more items. User enters:
        # Use peacock feathers to make a fly"

        # The page updates again, with both items on the list

        # User wonders whether the site will remember her list. Then sees some text to that effect.

        # User visits the URL, the list is still there.

        # Satified, user leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')
