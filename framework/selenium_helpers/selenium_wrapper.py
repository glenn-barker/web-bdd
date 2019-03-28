from selenium.webdriver.support.ui import WebDriverWait
from framework.selenium_helpers import extended_expected_conditions as EEC


class SeleniumWrapper:

    def __init__(self, context, driver):
        element_timeout = context.config.userdata.getint("element_timeout", 10)
        page_timeout = context.config.userdata.getint("page_timeout", 60)

        self.driver = driver
        self.driver.implicitly_wait(element_timeout)

        self.wait = WebDriverWait(self.driver, element_timeout)
        self.load_wait = WebDriverWait(self.driver, page_timeout)

    def find_visible_element(self, by, error_message=''):
        element = self.wait.until(EEC.visibility_of_any_element_located(by), error_message)
        return element

    def find_visible_elements(self, by, parent_element=None):
        elements = self.driver.find_elements(*by) if parent_element is None else parent_element.find_elements(*by)
        visible_elements = [element for element in elements if element.is_displayed()]
        return visible_elements
