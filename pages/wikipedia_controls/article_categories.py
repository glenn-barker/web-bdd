from selenium.webdriver.common.by import By
from pages.page import Page


class ArticleCategories(Page):

    def __init__(self, selenium):
        super().__init__(selenium)

        categories_container = self.selenium.find_visible_element(ArticleCategoriesLocator.CATEGORIES_CONTAINER)
        category_items = categories_container.find_elements(By.TAG_NAME, 'li')

        self.category_links = [li.find_element(By.TAG_NAME, 'a') for li in category_items]
        self.category_names = [a.text for a in self.category_links]

    def verify_exists(self, categories):
        missing_categories = [category for category in categories if category not in self.category_names]
        assert not missing_categories, \
            f"The following expected article categories are missing: {', '.join(missing_categories)}"

    def click(self, category):
        self.verify_exists([category])
        link = next(a for a in self.category_links if a.text == category)
        link.click()


class ArticleCategoriesLocator(object):
    CATEGORIES_CONTAINER = (By.ID, 'mw-normal-catlinks')
