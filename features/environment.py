from behave import fixture
from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import json
from framework.selenium_helpers.selenium_wrapper import SeleniumWrapper


@fixture
def selenium_browser_chrome(context):
    # -- FIXTURE SETUP
    context.selenium = SeleniumWrapper(context, webdriver.Chrome())
    yield context.selenium.driver
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def selenium_browser(context):
    browser = context.config.userdata.get("browser", "chrome").lower()

    if browser == "chrome":
        yield from selenium_browser_chrome(context)
    elif browser == "firefox":
        raise NotImplementedError("No Firefox support yet")
    elif browser == "ie":
        raise NotImplementedError("No IE support yet")
    else:
        raise ValueError(f"Browser option {browser} is invalid")


fixture_registry = {
    # Map each valid @fixture tag with the appropriate test fixture.
    "fixture.browser": selenium_browser,
    "fixture.browser.chrome": selenium_browser_chrome,
}


def before_all(context):
    # Load and update settings from JSON config file.
    # Note that all of the options provided in the config.json can also be provided as cmd line params to
    # override the defaults specified in the config.
    with open("config.json") as json_file:
        json_data = json.load(json_file)

    context.config.update_userdata(json_data)


def before_tag(context, tag):
    # @fixture tags can be used to enable fixtures like web browsers and other resources required throughout the test.
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)
