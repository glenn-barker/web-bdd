from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from framework.selenium import extended_expected_conditions as EEC
from pages.page import Page


class ArticlePage(Page):

    def verify_title_equals(self, article_title):
        article_header = self.selenium.wait.until(
            EEC.visibility_of_any_element_located(ArticlePageLocators.ARTICLE_HEADER))

        assert article_header.text == article_title, \
            f"The article on {self.selenium.driver.current_url} is {article_header.text} instead of {article_title}"


class ArticlePageLocators(object):
    ARTICLE_HEADER = (By.ID, 'firstHeading')
