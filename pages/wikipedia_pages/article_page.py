from selenium.webdriver.common.by import By
from pages.page import Page


class ArticlePage(Page):

    def __init__(self, selenium):
        super().__init__(selenium)

        article_header = self.selenium.find_visible_element(ArticlePageLocators.ARTICLE_HEADER)
        self.title = article_header.text

    def verify_title_equals(self, article_title):
        assert self.title == article_title, \
            f"The article on {self.selenium.driver.current_url} is {self.title} instead of {article_title}"

    def click_first_link(self):
        article_body_links = self.selenium.find_visible_elements(ArticlePageLocators.ARTICLE_BODY_LINKS)
        first_link = article_body_links[0]
        print(f"Clicking on {first_link.text} link.")
        first_link.click()


class ArticlePageLocators(object):
    ARTICLE_HEADER = (By.ID, 'firstHeading')
    ARTICLE_BODY = (By.ID, 'bodyContent')
    ARTICLE_BODY_LINKS = (By.XPATH, '//div[@id="bodyContent"]//p[not(@class)]//a[contains(@href, "/")]')
