from behave import given, when, then
from pages.wikipedia_pages.article_page import ArticlePage
from pages.wikipedia_controls.article_categories import ArticleCategories


@when(u'the first link in the Wikipedia article is clicked')
def step_impl(context):
    article_page = ArticlePage(context.selenium)
    article_page.click_first_link()


@when(u'the {category} category link is clicked')
def step_impl(context, category):
    article_categories = ArticleCategories(context.selenium)
    article_categories.click(category)


@then(u'the following Wikipedia categories should be available')
def step_impl(context):
    expected_categories = [table_row['Category'] for table_row in context.table]

    article_categories = ArticleCategories(context.selenium)
    article_categories.verify_exists(expected_categories)
