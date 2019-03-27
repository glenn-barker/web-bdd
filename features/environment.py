from behave import fixture
from behave.fixture import use_fixture_by_tag
from selenium import webdriver
from framework.selenium_helpers.selenium_wrapper import SeleniumWrapper


@fixture
def selenium_browser_chrome(context):
    # -- FIXTURE SETUP
    context.selenium = SeleniumWrapper(webdriver.Chrome())
    yield context.selenium.driver
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def selenium_browser(context):
    # TODO: Add logic here to return one of several possible generator types for different browsers read from a config.
    yield from selenium_browser_chrome(context)


fixture_registry = {
    "fixture.browser": selenium_browser,
    "fixture.browser.chrome": selenium_browser_chrome,
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)
