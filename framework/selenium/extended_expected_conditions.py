from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

# Based on:
# selenium/py/selenium/webdriver/support/expected_conditions.py


# noinspection PyPep8Naming
class visibility_of_any_element_located(object):
    """
    An expectation for checking that ANY element matching the locator
    is present on the DOM of a page and visible. Visibility means that
    the element is not only displayed but also has a height and width
    that is greater than 0.
    locator - used to find the element
    returns the WebElement once it is located and visible
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elements = _find_elements(driver, self.locator)
            visible_elements = [element for element in elements if element.is_displayed()]
            if visible_elements:
                return visible_elements[0]
            else:
                return False
        except StaleElementReferenceException:
            return False


# noinspection PyPep8Naming,SpellCheckingInspection
class any_element_to_be_clickable(object):
    """ An Expectation for checking that ANY element matching the locator
        is visible and enabled such that you can click it."""
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elements = _find_elements(driver, self.locator)
            clickable_elements = [element for element in elements if element.is_displayed() and element.is_enabled()]
            if clickable_elements:
                return clickable_elements[0]
            else:
                return False
        except StaleElementReferenceException:
            return False


def _find_element(driver, by):
    """Looks up an element. Logs and re-raises ``WebDriverException``
    if thrown."""
    try:
        return driver.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e


def _find_elements(driver, by):
    try:
        return driver.find_elements(*by)
    except WebDriverException as e:
        raise e
