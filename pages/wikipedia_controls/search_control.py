from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.page import Page


class SearchControl(Page):

    def __init__(self, selenium):
        super().__init__(selenium)

        self.search_field = self.selenium.find_visible_element(SearchControlLocators.SEARCH_FIELD)

    def search(self, search_term):
        self.search_field.send_keys(search_term)
        self.search_field.send_keys(Keys.ENTER)


class SearchControlLocators(object):
    SEARCH_FIELD = (By.NAME, 'search')
