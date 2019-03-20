from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from framework.selenium import extended_expected_conditions as EEC
from pages.page import Page


class SearchControl(Page):

    def search(self, search_term):
        search_field = self.selenium.wait.until(
            EEC.visibility_of_any_element_located(SearchControlLocators.SEARCH_FIELD))

        search_field.send_keys(search_term)
        search_field.send_keys(Keys.ENTER)


class SearchControlLocators(object):
    SEARCH_FIELD = (By.NAME, 'search')
