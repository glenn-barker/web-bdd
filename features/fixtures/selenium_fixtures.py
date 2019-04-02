from behave import fixture
from behave.fixture import use_fixture_by_tag
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions
from framework.selenium_helpers.selenium_wrapper import SeleniumWrapper


@fixture
def chrome(context):
    # -- FIXTURE SETUP
    try:
        chrome_options = ChromeOptions()

        if should_use_headless(context):
            chrome_options.headless = True

        # Launch Chrome browser with Selenium.
        driver = webdriver.Chrome(chrome_options=chrome_options)

        # Store reference to Selenium wrapper in Scenario Context so all step definitions & page objects can use it.
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Chrome!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def edge(context):
    # -- FIXTURE SETUP
    try:
        edge_options = EdgeOptions()

        if should_use_headless(context):
            print("WARNING: Headless execution is NOT supported by Edge!")
            print("Ignoring headless flag and continuing execution with Edge in full UI mode.")

        # Launch Edge browser with Selenium.
        driver = webdriver.Edge(capabilities=edge_options.to_capabilities())

        # Store reference to Selenium wrapper in Scenario Context so all step definitions & page objects can use it.
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Edge!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def firefox(context):
    # -- FIXTURE SETUP
    try:
        firefox_options = FirefoxOptions()

        if should_use_headless(context):
            firefox_options.headless = True

        # Launch Firefox browser with Selenium.
        driver = webdriver.Firefox(options=FirefoxOptions)

        # Store reference to Selenium wrapper in Scenario Context so all step definitions & page objects can use it.
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Firefox!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def ie(context):
    # -- FIXTURE SETUP
    try:
        ie_options = IEOptions()

        if should_use_headless(context):
            print("WARNING: Headless execution is NOT supported by IE!")
            print("Ignoring headless flag and continuing execution with IE in full UI mode.")

        # Launch IE browser with Selenium.
        driver = webdriver.Ie(ie_options=ie_options)

        # Store reference to Selenium wrapper in Scenario Context so all step definitions & page objects can use it.
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing IE!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def safari(context):
    # -- FIXTURE SETUP
    try:
        if should_use_headless(context):
            print("WARNING: Headless execution is NOT supported by Safari!")
            print("Ignoring headless flag and continuing execution with Safari in full UI mode.")

        # Launch Safari browser with Selenium.
        driver = webdriver.Safari()

        # Store reference to Selenium wrapper in Scenario Context so all step definitions & page objects can use it.
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Safari!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def selenium_browser(context):
    # Using the `fixture.browser` fixture should do a lookup on the config and return an appropriate
    # sub-fixture, e.g.: `fixture.browser.chrome`.
    browser = context.config.userdata.get("browser", "chrome").lower()
    fixture_tag = f"fixture.browser.{browser}"
    try:
        yield use_fixture_by_tag(fixture_tag, context, fixture_registry)
    except LookupError:
        raise ValueError(f"Unsupported browser option: {browser}")


fixture_registry = {
    # Map each valid `@fixture` tag with the appropriate test fixture.
    "fixture.browser": selenium_browser,
    "fixture.browser.chrome": chrome,
    "fixture.browser.edge": edge,
    "fixture.browser.firefox": firefox,
    "fixture.browser.ie": ie,
    "fixture.browser.safari": safari,
}


def should_use_headless(context):
    # Poll either the cmd line args OR the specified JSON config to determine whether to use headless mode or not.
    return context.config.userdata.getbool("headless", False)
