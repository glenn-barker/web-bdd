from selenium.webdriver.support.ui import WebDriverWait
from framework.selenium_helpers import extended_expected_conditions as EEC


class SeleniumWrapper:

    IMPLICIT_WAIT = 10
    LOAD_WAIT = 60

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(SeleniumWrapper.IMPLICIT_WAIT)

        self.wait = WebDriverWait(self.driver, SeleniumWrapper.IMPLICIT_WAIT)
        self.load_wait = WebDriverWait(self.driver, SeleniumWrapper.LOAD_WAIT)

    def find_visible_element(self, by, error_message=''):
        element = self.wait.until(EEC.visibility_of_any_element_located(by), error_message)
        return element

    def find_visible_elements(self, by, parent_element=None):
        elements = self.driver.find_elements(*by) if parent_element is None else parent_element.find_elements(*by)
        visible_elements = [element for element in elements if element.is_displayed()]
        return visible_elements
