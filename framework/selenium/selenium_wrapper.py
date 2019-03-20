from selenium.webdriver.support.ui import WebDriverWait


class SeleniumWrapper:

    IMPLICIT_WAIT = 10
    LOAD_WAIT = 60

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(SeleniumWrapper.IMPLICIT_WAIT)

        self.wait = WebDriverWait(self.driver, SeleniumWrapper.IMPLICIT_WAIT)
        self.load_wait = WebDriverWait(self.driver, SeleniumWrapper.LOAD_WAIT)
