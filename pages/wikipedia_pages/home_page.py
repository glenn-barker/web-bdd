from selenium.webdriver.support import expected_conditions as EC
from pages.page import Page


class HomePage(Page):
    PAGE_URL = "https://www.wikipedia.org"

    def visit(self):
        self.selenium.driver.get(HomePage.PAGE_URL)
        self.verify_is_loaded()

    def verify_is_loaded(self):
        self.selenium.load_wait.until(
            EC.title_is("Wikipedia"),
            f"The Wikipedia homepage did not load on {self.selenium.driver.current_url}")
