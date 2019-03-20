from behave import fixture, use_fixture
from behave.fixture import use_fixture_by_tag
from selenium import webdriver
from framework.selenium.selenium_wrapper import SeleniumWrapper


@fixture
def selenium_browser_chrome(context):
    # -- FIXTURE SETUP
    context.selenium = SeleniumWrapper(webdriver.Chrome())
    yield context.selenium.driver
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


fixture_registry = {
    "fixture.browser.chrome": selenium_browser_chrome,
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)


# def before_scenario(context, scenario):
#     use_fixture(selenium_browser_chrome, context)
